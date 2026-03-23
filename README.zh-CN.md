<div align="center">

# 🏆 OpenClaw Top 100 精选技能

<img src="https://img.shields.io/badge/技能数量-100-orange?style=for-the-badge" alt="100 Skills" />
<img src="https://img.shields.io/badge/每月更新-动态维护-green?style=for-the-badge" alt="Monthly Updates" />
<img src="https://img.shields.io/badge/精心筛选-专家推荐-blue?style=for-the-badge" alt="Expert Picks" />

**语言版本：**
[English](README.md) · [中文](README.zh-CN.md)

</div>

---

## 🌟 关于本项目

**OpenClaw Top 100** 是为 OpenClaw Agent 精心挑选的 100 个最核心、高质量的技能合集。就像山姆超市一样——SKU 少，但每一个都是同类最佳。告别在 400+ 选项中迷失，直接拿到你需要的，快速上手，高效完成任务。

> **核心理念：** 每个类别 1–2 个顶级技能，无重复，无噪音，只留精华。

本列表是**动态的**——每月根据社区使用数据、质量评估和覆盖需求进行审查和更新。落后的技能会被更好的替代品取代。

---

## 🚀 快速安装

```bash
# 克隆仓库
git clone https://github.com/LeoYeAI/openclaw-top100.git

# 复制单个技能到 OpenClaw 工作区
cp -r openclaw-top100/skills/<技能名称> ~/.openclaw/workspace/skills/

# 或一次性安装全部 100 个技能
cp -r openclaw-top100/skills/* ~/.openclaw/workspace/skills/
```

---

## 🗂️ 技能索引（100 个技能）

### 🤖 AI & 大模型工具（12 个）

| 技能 | 描述 |
|---|---|
| [`deep-research-pro`](skills/deep-research-pro/) | 多源深度研究 Agent，搜索网络、综合发现、生成带引用报告，无需 API Key。 |
| [`academic-deep-research`](skills/academic-deep-research/) | 严谨的学术研究，完整方法论，非黑盒 API 包装器。 |
| [`boost-prompt`](skills/boost-prompt/) | 交互式提示词优化工作流：审查范围、交付物和约束条件，将最终 Markdown 复制到剪贴板。 |
| [`prompt-engineering-expert`](skills/prompt-engineering-expert/) | 高级提示词工程专家，专注于自定义指令设计和 AI Agent 提示词优化。 |
| [`ai-model-router`](skills/ai-model-router/) | 智能 AI 模型路由器，根据任务类型自动切换本地和云端模型。 |
| [`computer-use`](skills/computer-use/) | 无头 Linux 服务器完整桌面控制，Xvfb + XFCE 虚拟桌面 + xdotool 自动化。 |
| [`browser-use`](skills/browser-use/) | 浏览器自动化，用于网页测试、表单填写、截图和数据提取。 |
| [`agent-browser`](skills/agent-browser/) | 基于 Rust 的高速无头浏览器自动化 CLI，带 Node.js 回退，专为 AI Agent 设计。 |
| [`gemini`](skills/gemini/) | Gemini CLI，用于单次问答、摘要和生成任务。 |
| [`summarize`](skills/summarize/) | 使用 summarize CLI 摘要 URL 或文件（网页/PDF/图片/音频/YouTube）。 |
| [`using-superpowers`](skills/using-superpowers/) | 每次对话开始时使用——建立如何发现和使用技能的规范，任何任务前必须调用。 |
| [`capability-evolver`](skills/capability-evolver/) | AI Agent 自我进化引擎，分析运行历史以识别改进点并应用协议约束的升级。 |

### 🔍 搜索与网络（8 个）

| 技能 | 描述 |
|---|---|
| [`web-search-plus`](skills/web-search-plus/) | 统一搜索技能，智能自动路由，多信号分析自动选择最优搜索引擎。 |
| [`duckduckgo-search`](skills/duckduckgo-search/) | 使用 DuckDuckGo 进行实时网络搜索，无需 API Key。 |
| [`brave-search`](skills/brave-search/) | 通过 Brave Search API 进行网络搜索和内容提取，轻量且注重隐私。 |
| [`exa-web-search-free`](skills/exa-web-search-free/) | 免费 Exa AI 搜索，支持网络/代码/公司研究，无 API 费用。 |
| [`firecrawl`](skills/firecrawl/) | 通过 Firecrawl API 进行网页抓取和搜索，支持 JS 渲染页面。 |
| [`multi-search-engine`](skills/multi-search-engine/) | 17 引擎多搜索集成（8 中文 + 9 全球），支持高级搜索运算符和时间过滤。 |
| [`news-summary`](skills/news-summary/) | 从聚合信源获取新闻更新、每日简报和主题摘要。 |
| [`youtube-transcript`](skills/youtube-transcript/) | 获取并摘要 YouTube 视频字幕，用于视频内容提取和总结。 |

### 📋 生产力与办公（10 个）

| 技能 | 描述 |
|---|---|
| [`calendar`](skills/calendar/) | 日历管理与日程安排，跨提供商创建活动和管理会议。 |
| [`todoist`](skills/todoist/) | 在 Todoist 中管理任务和项目——创建、完成、列表和组织。 |
| [`excel-xlsx`](skills/excel-xlsx/) | 读写生成 Excel 文件，支持正确的类型、日期、公式和跨平台兼容性。 |
| [`word-docx`](skills/word-docx/) | 读写生成 Word 文档，支持正确的结构、样式和跨平台兼容性。 |
| [`markdown-converter`](skills/markdown-converter/) | 使用 markitdown 将文档转换为 Markdown（PDF/Word/PPT/Excel/图片）。 |
| [`nano-pdf`](skills/nano-pdf/) | 使用 nano-pdf CLI 通过自然语言指令编辑 PDF。 |
| [`doc-coauthoring`](skills/doc-coauthoring/) | 引导用户完成结构化文档协作撰写工作流。 |
| [`writing-skills`](skills/writing-skills/) | 创建新技能、编辑现有技能或在部署前验证技能时使用。 |
| [`html-slide-creator`](skills/html-slide-creator/) | 创建零依赖、完全在浏览器中运行的 HTML 演示文稿。 |
| [`brainstorming`](skills/brainstorming/) | 任何创意工作前必须使用——创建功能、构建组件或修改现有系统。 |

### 💻 开发与运维（20 个）

| 技能 | 描述 |
|---|---|
| [`code-review`](skills/code-review/) | 系统化代码审查，覆盖安全性、性能、可维护性、正确性和测试。 |
| [`git-essentials`](skills/git-essentials/) | 版本控制、分支和协作的核心 Git 命令与工作流。 |
| [`github`](skills/github/) | GitHub CLI 交互——Issues、PR、仓库和工作流管理。 |
| [`docker-essentials`](skills/docker-essentials/) | 容器管理、镜像操作和调试的核心 Docker 命令与工作流。 |
| [`filesystem`](skills/filesystem/) | 高级文件系统操作——文件列表、内容搜索和批量处理。 |
| [`file-search`](skills/file-search/) | 使用 `fd` 和 `rg`（ripgrep）进行快速文件名和内容搜索。 |
| [`debug-pro`](skills/debug-pro/) | 专业调试工作流，系统性诊断、假设测试和修复验证。 |
| [`test-driven-development`](skills/test-driven-development/) | TDD 方法论——先写测试，实现通过，自信重构。 |
| [`api-design-principles`](skills/api-design-principles/) | 掌握 REST 和 GraphQL API 设计原则，构建直观、可扩展的 API。 |
| [`architecture-patterns`](skills/architecture-patterns/) | 实现经典后端架构模式，包括整洁架构、六边形架构和 DDD。 |
| [`microservices-patterns`](skills/microservices-patterns/) | 设计微服务架构，包含服务边界、事件驱动通信和弹性模式。 |
| [`next-best-practices`](skills/next-best-practices/) | Next.js 最佳实践——文件约定、RSC 边界、数据模式和错误处理。 |
| [`vercel-react-best-practices`](skills/vercel-react-best-practices/) | 来自 Vercel 工程团队的 React 和 Next.js 性能优化指南。 |
| [`typescript-advanced-types`](skills/typescript-advanced-types/) | 掌握 TypeScript 高级类型——泛型、条件类型、映射类型和工具类型。 |
| [`vitest`](skills/vitest/) | 基于 Vite 的高速单元测试框架，兼容 Jest API。 |
| [`verification-before-completion`](skills/verification-before-completion/) | 声明工作完成前必须运行验证检查，防止错误提交。 |
| [`mcp-builder`](skills/mcp-builder/) | 创建高质量 MCP（模型上下文协议）服务器的完整指南。 |
| [`n8n-workflow-automation`](skills/n8n-workflow-automation/) | 设计并输出 n8n 工作流 JSON，包含健壮的触发器、错误处理和重试机制。 |
| [`executing-plans`](skills/executing-plans/) | 在独立会话中执行书面实现计划，带审查检查点。 |
| [`breakdown-feature-implementation`](skills/breakdown-feature-implementation/) | 创建详细的功能实现计划，遵循结构化方法。 |

### 📈 营销与增长（9 个）

| 技能 | 描述 |
|---|---|
| [`marketing-skills`](skills/marketing-skills/) | 23 个营销手册，覆盖 CRO、SEO、文案、分析、实验、定价、发布和广告。 |
| [`copywriting`](skills/copywriting/) | 说服性、高转化内容的文案写作框架与技巧。 |
| [`seo-audit`](skills/seo-audit/) | 审计和诊断网站 SEO 问题——技术 SEO、Meta 标签、页面优化。 |
| [`programmatic-seo`](skills/programmatic-seo/) | 使用模板和数据大规模创建 SEO 驱动的页面——目录页、地区页、对比页。 |
| [`content-strategy`](skills/content-strategy/) | 内容策略规划——受众映射、内容支柱、分发渠道和效果衡量。 |
| [`launch-strategy`](skills/launch-strategy/) | 使用结构化框架规划产品发布、功能公告或发布策略。 |
| [`email-sequence`](skills/email-sequence/) | 创建或优化邮件序列、滴灌活动和生命周期邮件流。 |
| [`marketing-psychology`](skills/marketing-psychology/) | 将心理学原则和行为科学应用于营销。 |
| [`audit-website`](skills/audit-website/) | 使用 squirrelscan CLI 对网站进行 SEO、性能、安全审计，230+ 规则。 |

### 🎨 媒体与创意（6 个）

| 技能 | 描述 |
|---|---|
| [`media-generation`](skills/media-generation/) | 生成图像、编辑图像、创建短视频、运行修复/扩图和对象编辑。 |
| [`nano-banana-pro`](skills/nano-banana-pro/) | 使用 Nano Banana Pro（Gemini 3 Pro Image）生成/编辑图像，支持风格迁移。 |
| [`canvas-design`](skills/canvas-design/) | 使用设计哲学创建精美的 .png 和 .pdf 视觉作品。 |
| [`video-frames`](skills/video-frames/) | 使用 ffmpeg 从视频中提取帧或短片段。 |
| [`openai-whisper`](skills/openai-whisper/) | 使用 Whisper CLI 进行本地语音转文字，无需 API Key。 |
| [`edge-tts`](skills/edge-tts/) | 使用微软 Edge TTS 引擎进行文字转语音，支持多种语音和语言。 |

### 💰 金融与交易（6 个）

| 技能 | 描述 |
|---|---|
| [`yahoo-finance`](skills/yahoo-finance/) | 通过 Yahoo Finance 获取股票报价、基本面、盈利、期权、股息和分析师评级。 |
| [`eastmoney-financial-data-1-0-2`](skills/eastmoney-financial-data-1-0-2/) | 基于东方财富权威数据库，支持自然语言查询股票/基金/债券/指数行情及财务数据。 |
| [`eastmoney-financial-search-1-0-2`](skills/eastmoney-financial-search-1-0-2/) | 东方财富妙想智能金融搜索，获取新闻、公告、研报、政策等时效性信息。 |
| [`us-stock-analysis`](skills/us-stock-analysis/) | 全面的美股分析——基本面、技术面、盈利和行业对比。 |
| [`wyckoff-a-share`](skills/wyckoff-a-share/) | 基于股票代码、持仓、CSV 数据和可选图表图像运行威科夫大师级分析。 |
| [`trader-daily`](skills/trader-daily/) | 每日交易者工作流——市场概览、观察列表审查和绩效追踪。 |

### 💬 通讯与消息（6 个）

| 技能 | 描述 |
|---|---|
| [`gmail`](skills/gmail/) | Gmail 邮件管理——读取、撰写、发送、搜索和整理邮件。 |
| [`discord`](skills/discord/) | 通过 Agent 控制 Discord——发送消息、反应、发布贴纸和上传文件。 |
| [`telegram`](skills/telegram/) | 通过 Bot API 发送和接收 Telegram 消息。 |
| [`imap-smtp-email`](skills/imap-smtp-email/) | 通用 IMAP/SMTP 邮件访问，适用于任何邮件提供商，无需特定客户端。 |
| [`linkedin`](skills/linkedin/) | 通过浏览器中继进行 LinkedIn 自动化——消息、个人资料浏览和网络操作。 |
| [`x-twitter`](skills/x-twitter/) | 与 Twitter/X 交互——读取推文、搜索、发布、点赞、转推和管理时间线。 |

### 🧠 记忆与 Agent 增强（8 个）

| 技能 | 描述 |
|---|---|
| [`memory-setup`](skills/memory-setup/) | 启用并配置 Moltbot/Clawdbot 记忆搜索，实现持久化上下文。 |
| [`elite-longterm-memory`](skills/elite-longterm-memory/) | 终极 AI Agent 记忆系统——WAL 协议 + 向量搜索 + git-notes + 云同步。 |
| [`memory-manager`](skills/memory-manager/) | 本地记忆管理——压缩检测、自动快照和语义搜索。 |
| [`agent-autonomy-kit`](skills/agent-autonomy-kit/) | 增强 Agent 自主性——主动规划、自我纠错和目标持久化。 |
| [`dispatching-parallel-agents`](skills/dispatching-parallel-agents/) | 面对 2 个以上可并行的独立任务时使用，无需共享状态或顺序依赖。 |
| [`agent-team-orchestration`](skills/agent-team-orchestration/) | 编排 AI Agent 团队，用于复杂多步骤工作流，包含协调和交接协议。 |
| [`find-skills`](skills/find-skills/) | 当用户询问"如何做 X"或"找一个 X 的技能"时，帮助发现和安装 Agent 技能。 |
| [`auto-updater`](skills/auto-updater/) | 通过 cron 每天自动更新 Clawdbot 及所有已安装技能。 |

### 🔒 安全与审计（3 个）

| 技能 | 描述 |
|---|---|
| [`clawsec`](skills/clawsec/) | OpenClaw Agent 及其环境的安全审计和漏洞扫描。 |
| [`better-auth-best-practices`](skills/better-auth-best-practices/) | 集成 Better Auth——全面的 TypeScript 认证框架的最佳实践。 |
| [`ai-prompt-engineering-safety-review`](skills/ai-prompt-engineering-safety-review/) | 全面的 AI 提示词安全审查，分析提示词的安全性、偏见和注入风险。 |

### 📊 数据与分析（4 个）

| 技能 | 描述 |
|---|---|
| [`data-analysis`](skills/data-analysis/) | 以统计严谨性将原始数据转化为决策，避免分析陷阱。 |
| [`data-analyst`](skills/data-analyst/) | 完整数据分析师工作流——数据清洗、探索性分析、可视化和洞察生成。 |
| [`analytics-tracking`](skills/analytics-tracking/) | 分析追踪集成——事件设计、实现和跨平台验证。 |
| [`tushare-finance`](skills/tushare-finance/) | Tushare 金融数据接口，专为中国市场设计，支持 220+ 接口（股票/基金/期货/债券）。 |

### 📱 社交与内容（6 个）

| 技能 | 描述 |
|---|---|
| [`xiaohongshu-mcp`](skills/xiaohongshu-mcp/) | 小红书内容发布与管理，通过 MCP 接口操作。 |
| [`jike-publisher`](skills/jike-publisher/) | 使用浏览器自动化向即刻（Jike）发布内容。 |
| [`youtube-watcher`](skills/youtube-watcher/) | 获取 YouTube 视频字幕——摘要、回答问题或提取内容。 |
| [`weibo-trending-bot`](skills/weibo-trending-bot/) | 监控微博热搜话题并生成内容摘要。 |
| [`tiktok-viral-predictor`](skills/tiktok-viral-predictor/) | 基于内容分析、趋势和互动模式预测 TikTok 病毒式传播潜力。 |
| [`last30days`](skills/last30days/) | 研究过去 30 天内 Reddit + X + 网络上的任何话题，综合发现并生成即用内容。 |

### 🛠️ 实用工具（2 个）

| 技能 | 描述 |
|---|---|
| [`weather`](skills/weather/) | 获取任意地点的当前天气和预报，无需 API Key。 |
| [`changelog-curator`](skills/changelog-curator/) | 从提交摘要或发布说明中整理对外 Changelog，区分用户价值与内部改动。 |

---

## 🔄 动态更新机制

本列表**不是静态的**。每月我们会按照以下三个维度进行审查：

| 维度 | 评估内容 |
|---|---|
| **社区使用数据** | ClawHub 趋势数据和 GitHub Star 数量 |
| **质量信号** | 描述清晰度、是否积极维护、依赖是否正常 |
| **覆盖缺口** | 确保每个主要使用场景都有至少一个优质技能 |

落后的技能将被更好的替代品取代。目标始终是：**最好的 100 个，而不是最老的 100 个**。

---

## 🤝 贡献指南

如需提名新技能或报告失效技能：

1. 提交 [Issue](../../issues)，注明技能名称、类别和入选理由
2. 维护者每月审查提名并更新列表
3. 欢迎提交 PR：在同一类别中添加新技能并移除较弱的技能

---

## 📄 许可证

MIT 许可证——详见 [LICENSE](LICENSE)。

---

<div align="center">
<sub>精选自 <a href="https://github.com/LeoYeAI/openclaw-master-skills">openclaw-master-skills</a> · 为 OpenClaw 社区而建</sub>
</div>
