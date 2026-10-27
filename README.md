# Olivia Skills

Olivia 的可复用创作规范，按独立 Skill 存档。

## 已有 Skill

### 1. 稚拙风 PPT · `naive-ppt`
[打开 SKILL.md](skills/naive-ppt/SKILL.md)

纯白底、大面积留白、橘红色 MS Paint 鼠标涂鸦。支持 HTML 演示、风格转绘与简洁文案。调用：`$naive-ppt`。

### 2. 极简编辑式研究信息图 PPT · `editorial-data-ppt`
[打开 SKILL.md](skills/editorial-data-ppt/SKILL.md) ｜ [视觉规范](skills/editorial-data-ppt/references/visual-system.md) ｜ [图表选型](skills/editorial-data-ppt/references/chart-selection.md) ｜ [反面案例](skills/editorial-data-ppt/references/anti-patterns.md)

2026-10 研究汇报与 Figma 走查的复用规范。借鉴小红书策略／营销提案的**编辑设计手法**：极简、留白、对齐、信息高密度、图表形式丰富、文字克制。项目实践为深色星空原底图、蓝白配色、白色数据底板，以及一级／二级／三级标签、设备条形图和独立占比圆环。强调证据链、真实数据、可编辑图层和少“AI味”。

调用：

> 使用 $editorial-data-ppt，把给定研究报告、案例库和原 PPT 变成可编辑 Figma 研究汇报。先核对去重口径和多选标签，优先复用原有风格。保留旧页，新增独立章节。

### 3. 文史思辨·缓慢推进 · **literary-inquiry-essay**
[主 Skill](skills/literary-inquiry-essay/SKILL.md) ｜ [叙事结构](skills/literary-inquiry-essay/references/narrative-architecture.md) ｜ [反 AI slop](skills/literary-inquiry-essay/references/voice-and-anti-slop.md) ｜ [引用规范](skills/literary-inquiry-essay/references/fact-and-theory.md) ｜ [成功/失败复盘](skills/literary-inquiry-essay/references/field-notes.md) ｜ [公众号排版](skills/literary-inquiry-essay/references/wechat-editorial.md)

以可信场景引出一条思想主线，理论为问题服务，认真处理反例，最后用意象回环；正文用连贯复合句承载论证，不制造口播式短句与空泛“哲学金句”。适用设计史、艺术、科技、人文经验等不同题材。调用：**$literary-inquiry-essay**。

### 4. 鼠标稚拙·文学封面 · **naive-editorial-cover**
[主 Skill](skills/naive-editorial-cover/SKILL.md) ｜ [视觉系统](skills/naive-editorial-cover/references/visual-system.md) ｜ [英文生成 Prompt](skills/naive-editorial-cover/references/prompt-recipes.md) ｜ [反面案例与QA](skills/naive-editorial-cover/references/anti-patterns-and-qa.md)

MS Paint 鼠标笨拙线稿：黑色抖线、克制蓝紫、白底、大留白和一个清晰的日常隐喻。默认微信横封1080×460 PNG，可换平台与配色。**与 $naive-ppt 的纯白橘红风严格区分**。调用：**$naive-editorial-cover**。

### 5. 论文精读与研究成长 · **adaptive-paper-reading**
[主 Skill](skills/adaptive-paper-reading/SKILL.md) ｜ [使用指南](skills/adaptive-paper-reading/README.md) ｜ [学习偏好](skills/adaptive-paper-reading/references/reader-profile.md) ｜ [证据协议](skills/adaptive-paper-reading/references/evidence.md) ｜ [迭代机制](skills/adaptive-paper-reading/references/learning-loop.md)

2026-10 新增：将论文 **速读 skim → 精读 close → 对读 compare → 研究 research** 编排为一个入口；根据阅读反馈适度调整讲解节奏，保留英文术语、原文页码、关键图表与研究方法，并区分作者证据、教学解释与 HCI 迁移性假说。可选对接 Paper Deep Reader、Paper Reading、Literature Review、PaperSpine5；这些第三方 Skill **需要独立安装**，本仓库不会自动下载或运行其程序。

调用示例：**$adaptive-paper-reading** 带我精读 Desmet 的 Designing Emotions，从 Figure 6-2 开始，每轮解释一个机制、保留证据出处，再提出一个最值得争辩的问题。

## 风格选择（不要混成一个默认风格）

| 目标 | 调用 | 视觉/语言边界 |
| --- | --- | --- |
| 文学思想随笔/人文评论 | $literary-inquiry-essay | 规定写法与核查，不强制使用旧文章题材或封面 |
| 公众号鼠标手绘封面 | $naive-editorial-cover | 白底黑线蓝紫；不等于 PPT 橘红 |
| 稚拙风演示/PPT | $naive-ppt | PPT 纯白、橘红 #E6532F、16:9 |
| 研究信息图与策略PPT | $editorial-data-ppt | 数据逻辑/母版优先，避免装饰性卡片 |
| 学术文献速读、精读、对读与研究思辨 | $adaptive-paper-reading | 原文证据、逐图解释、跨领域迁移与可撤销学习记录 |

组合示例：**“用 $literary-inquiry-essay 写一篇关于临摹与创新的文章，再用 $naive-editorial-cover 画微信横封；图中的物件必须来自本次文章。”**

可选编辑辅助：**python skills/literary-inquiry-essay/scripts/lint_essay.py draft.md**（只报警，不自动改写）。

## 使用

把 `skills/<name>/` 整个目录安装到所用 Agent 支持的 skills 位置。上传 GitHub **不等于已在 ChatGPT、Codex 或其他工具自动安装**。

## 关于公开仓库

此仓库为 public。这里只归档可复用的抽象设计系统、工作流和通用示例；不上传第三方小红书营销提案原文件、客户内部案例库、未授权品牌素材、隐私或真实受访记录。尊重第三方材料版权与项目保密要求。


## 2026-10-26 · editorial-data-ppt v1.1

本轮从多次研究型PPT与Figma协作中，把“简洁留白+高信息密度”与**数据可信、比例正确、最小变更、截图走查**合并为统一Skill。保持原有稚拙风 Skill 不动。

补充阅读：[数据统计契约](skills/editorial-data-ppt/references/data-contract.md) / [五种经典版式](skills/editorial-data-ppt/references/pattern-library.md) / [成功与反面复盘](skills/editorial-data-ppt/references/retrospective.md)。同步扩展了主Skill、视觉系统、图表选择、反面案例、Figma QA和Agent执行提示。

**公开仓库仅保存方法论和匿名化经验；不包含原始内部案例、受访信息、营销提案原件或客户品牌素材。**

## 2026-10-27 · Literary Essay & Naive Cover v1.0

从《十月之水》与《当智力成为水电煤》的多轮合作中，分离 **文风（论证、引用、句法与叙事）** 和 **封面（绘画技法、色系、构图与隐喻）**。新规范记录成功做法及被指出的失败：连续追问导致失焦、过密反转句、短句口播、哲学装饰、错误的免费=公平推论，以及封面AI光泽与图标堆积。

此仓库只保留方法与匿名化示例，不转载整篇第三方文章，也不把用户个别项目的内容设为永恒模板。

## 2026-10-27 · Adaptive Paper Reading v0.1

构建原创研究阅读编排器，保留本仓库独立 Skill 的约定，不打包第三方运行套件。通过“逐论点精读 → 一问一答 → 证据与反例 → HCI 迁移 → 经许可更新偏好”形成可演进学习闭环。首个脱敏案例来自 Desmet 的产品情绪模型与 AI 日程代理的行动授权边界；本地私有学习日志明确被 Git 忽略。公开 profile 只含非敏感、可修订的抽象偏好。
