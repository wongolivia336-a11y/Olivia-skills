# Adaptive Paper Reading · Olivia Research Companion

这是 Olivia-skills 的原创**论文阅读编排 Skill**，按现有仓库的独立目录规范保存。侧重点是精读与学术思辨，而不是一键生成学术综述或自动写完整论文。

## 能做什么
- 以文献原文为依据的四种模式：skim、close、compare、research。
- 每轮只解释一个关键机制，主动寻找反例，区分作者主张与 HCI 迁移假说。
- 管理阅读节奏、可公开的学习偏好种子、非公开本地复盘日志与审核后升级。
- 可选联动 Paper Deep Reader、Paper Reading、Literature Review 和 PaperSpine（安装与否分别判断）。

## 文件
- SKILL.md：总入口与触发条件
- references/reader-profile.md：安全的公开偏好初值
- references/routing.md：上游 Skill 路由与 PaperSpine 官方安装信息
- references/evidence.md：引文、页图与证据强度
- references/learning-loop.md：个人化的迭代与撤销规则
- templates/session-note.md：每篇文章的可复用结构化笔记
- examples/desmet-appraisal.md：第一份 Design + HCI 思辨示例
- scripts/log_reflection.py：经明确确认后写入本地非跟踪的简短学习事件

## 如何调用
将本目录完整拷贝至使用的 Agent 支持的 Skills 路径，重启或刷新 Skill 发现；并提出：

    使用 $adaptive-paper-reading 精读这篇论文。先给结构地图，然后从最重要的理论图开始，用一个 HCI 反例检查作者模型。每轮只问我一个真正有价值的问题。

**GitHub 存档并不等于该 Skill 已在 ChatGPT、Codex 或 Claude 主机中自动安装。** 第三方工具仍须根据官方说明另外部署。

## 维护
与现有 Skill 一样，采用小版本号、Git PR 和回归检查。公开仓库不提交 PDF 原文、用户私有的研究材料、完整聊天或任何个人敏感资料。