#!/usr/bin/env python3
"""Heuristic editor's warnings for Chinese humanist essays. No automatic rewriting."""
import argparse
import re
from pathlib import Path

CLICHES = (
    "值得注意的是", "首先", "其次", "最后", "换句话说", "本质上",
    "深刻变革", "时代洪流", "底层逻辑", "重塑", "赋能", "我们不禁",
    "不难发现", "由此可见", "显而易见", "未来已来"
)

def analyze(text: str):
    text = re.sub(r"(?ms)^---\s*\n.*?\n---\s*\n", "", text)
    text = re.sub(r"(?ms)^\x60\x60\x60.*?^\x60\x60\x60\s*$", "", text)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text)
                  if p.strip() and not p.lstrip().startswith("#")]
    narrative = [p for p in paragraphs if not p.startswith(("- ", "* ", "|", ">"))]
    sentences = [s.strip() for s in re.split(r"[。！？!?]", "\n".join(narrative)) if s.strip()]
    isolated = [p for p in narrative if len(re.sub(r"\s+", "", p)) < 35]
    antithesis = len(re.findall(r"不是[^。！？\n]{0,48}而是", text))
    cliche_counts = {word: text.count(word) for word in CLICHES if text.count(word)}
    return {
        "paragraphs": len(narrative),
        "sentences": len(sentences),
        "short_paragraphs_under_35_chars": len(isolated),
        "not_x_but_y_count": antithesis,
        "cliches": cliche_counts,
        "warnings": [
            *([f"Short standalone paragraphs: {len(isolated)}; read them in context."]
              if len(isolated) >= 4 else []),
            *([f"Repeated ‘不是X而是Y’: {antithesis}; review rhetorical rhythm."]
              if antithesis >= 3 else []),
            *([f"Formulaic words occur: {cliche_counts}; review but do not bulk-delete."]
              if sum(cliche_counts.values()) >= 5 else []),
        ],
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="UTF-8 .md or .txt draft")
    args = parser.parse_args()
    result = analyze(Path(args.file).read_text(encoding="utf-8"))
    for k, v in result.items():
        print(f"{k}: {v}")
    print("Manual editor judgement overrides these heuristics.")

if __name__ == "__main__":
    main()
