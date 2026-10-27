# Routing & integration | 四层技能不是四份重复摘要

此仓库提供原创“自适应导师”编排协议，**不镜像第三方代码、脚本或运行时**。用户必须在其 Agent 宿主中另行按上游说明安装；没有安装时以此 Skill 的通用指令执行并声明功能边界。

| 意图 | 推荐角色 | 上游项目 | 无上游时 |
| --- | --- | --- | --- |
| 首筛 / 10 分钟建立研究地图 | paper-reading | https://github.com/jxtse/scientific-research-skills | 提取问题、对象、核心机制、质量红旗与是否精读 |
| 精读概念、关键图表和证据 | paper-deep-reader | https://github.com/Linwei-Chen/paper-deep-reader-skill | 按 SKILL.md 逐页阅读和证据对照 |
| 文献查找、分类、比较、综述 | literature-review | https://github.com/ZhijianWei/literature-review-skill | 先检索可靠元数据，再做矩阵；缺全文标记摘要级 |
| 形成自己的论文与引用检查 | paper-spine | https://github.com/WUBING2023/PaperSpine | 先产研究问题、证据库、提纲；不冒称运行 PaperSpine |

## PaperSpine5 的独立安装说明
当前上游官方介绍 https://github.com/WUBING2023/PaperSpine/blob/main/README.en.md 和 https://github.com/WUBING2023/PaperSpine/blob/main/INSTALL.md 指出：PaperSpine5 需要按平台提供的完整套件、运行时和 Web 工作空间；单独放一份 Skill 文件不等于完整运行。官方 Windows Codex 安装在**克隆上游仓库后**使用：

    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target codex -CleanLegacy

这是上游 alpha 版本的官方指令，不在本仓库里自动执行、下载或升级。用户应检查发行包、安全边界和更新策略；不要把未知的第三方程序自动引入研究环境。若用户在其他宿主运行，请查对应官方说明。

## 组合执行示例
- “先告诉我值不值得读”：skim → 可选 close。
- “原文第 6 章怎么论证”：close；只在需要最新对照研究时 compare。
- “找设计领域后来怎么批评 Appraisal”：compare → close 回源核实。
- “我要把问题写成论文”：close/compare → research → 安装可用时交接 PaperSpine。

## 引文和版权
优先官方论文页面、用户上传原文、官方版本；第三方上游软件保留原仓库与许可证链接，不复制其文本或资产。用户上传的扫描 PDF 不公开上传到本仓库。所有外部运行或上传文稿应按用户授权与版权限制处理。