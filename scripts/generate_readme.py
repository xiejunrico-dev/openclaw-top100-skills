#!/usr/bin/env python3
"""
generate_readme.py — Regenerate README.md and README.zh-CN.md from skills directory.

Usage:
    python3 scripts/generate_readme.py

This script reads the SKILL.md of each skill in the skills/ directory,
extracts the description, and regenerates the README files.

Run this after making any changes to the skills/ directory.
"""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, 'skills')

# Category definitions — edit this to change order or groupings
CATEGORIES = {
    '🤖 AI & LLM Tools': [
        'deep-research-pro', 'academic-deep-research', 'boost-prompt', 'prompt-engineering-expert',
        'ai-model-router', 'computer-use', 'browser-use', 'agent-browser', 'gemini', 'summarize',
        'using-superpowers', 'capability-evolver',
    ],
    '🔍 Search & Web': [
        'web-search-plus', 'duckduckgo-search', 'brave-search', 'exa-web-search-free', 'firecrawl',
        'multi-search-engine', 'news-summary', 'youtube-transcript',
    ],
    '📋 Productivity & Office': [
        'calendar', 'todoist', 'excel-xlsx', 'word-docx', 'markdown-converter', 'nano-pdf',
        'doc-coauthoring', 'writing-skills', 'html-slide-creator', 'brainstorming',
    ],
    '💻 Development & DevOps': [
        'code-review', 'git-essentials', 'github', 'docker-essentials', 'filesystem', 'file-search',
        'debug-pro', 'test-driven-development', 'api-design-principles', 'architecture-patterns',
        'microservices-patterns', 'next-best-practices', 'vercel-react-best-practices',
        'typescript-advanced-types', 'vitest', 'verification-before-completion', 'mcp-builder',
        'n8n-workflow-automation', 'executing-plans', 'breakdown-feature-implementation',
    ],
    '📈 Marketing & Growth': [
        'marketing-skills', 'copywriting', 'seo-audit', 'programmatic-seo', 'content-strategy',
        'launch-strategy', 'email-sequence', 'marketing-psychology', 'audit-website',
    ],
    '🎨 Media & Creative': [
        'media-generation', 'nano-banana-pro', 'canvas-design', 'video-frames', 'openai-whisper', 'edge-tts',
    ],
    '💰 Finance & Trading': [
        'yahoo-finance', 'eastmoney-financial-data-1-0-2', 'eastmoney-financial-search-1-0-2',
        'us-stock-analysis', 'wyckoff-a-share', 'trader-daily',
    ],
    '💬 Communication & Messaging': [
        'gmail', 'discord', 'telegram', 'imap-smtp-email', 'linkedin', 'x-twitter',
    ],
    '🧠 Memory & Agent Enhancement': [
        'memory-setup', 'elite-longterm-memory', 'memory-manager', 'agent-autonomy-kit',
        'dispatching-parallel-agents', 'agent-team-orchestration', 'find-skills', 'auto-updater',
    ],
    '🔒 Security & Auditing': [
        'clawsec', 'better-auth-best-practices', 'ai-prompt-engineering-safety-review',
    ],
    '📊 Data & Analytics': [
        'data-analysis', 'data-analyst', 'analytics-tracking', 'tushare-finance',
    ],
    '📱 Social & Content': [
        'xiaohongshu-mcp', 'jike-publisher', 'youtube-watcher', 'weibo-trending-bot',
        'tiktok-viral-predictor', 'last30days',
    ],
    '🛠️ Utilities & Misc': [
        'weather', 'changelog-curator',
    ],
}


def get_desc(skill_name: str) -> str:
    md_path = os.path.join(SKILLS_DIR, skill_name, 'SKILL.md')
    if not os.path.exists(md_path):
        return f'*(skill not found: {skill_name})*'
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith('description:'):
                desc = line.replace('description:', '').strip().strip('"').strip("'")
                return desc
    return ''


def count_total() -> int:
    return sum(len(v) for v in CATEGORIES.values())


def generate_en() -> str:
    total = count_total()
    lines = [
        '<div align="center">\n',
        '# 🏆 OpenClaw Top 100 Skills\n',
        f'<img src="https://img.shields.io/badge/Skills-{total}-orange?style=for-the-badge" alt="{total} Skills" />\n',
        '<img src="https://img.shields.io/badge/Updated-Monthly-green?style=for-the-badge" alt="Monthly Updates" />\n',
        '<img src="https://img.shields.io/badge/Curated-Expert%20Picks-blue?style=for-the-badge" alt="Expert Picks" />\n',
        '\n**Languages:**\n[English](README.md) · [中文](README.zh-CN.md)\n\n</div>\n',
        '\n---\n',
        '\n## 🌟 About This Project\n',
        '\n**OpenClaw Top 100** is a curated collection of the most essential, high-quality skills for OpenClaw agents. '
        'Think of it like a premium warehouse store — fewer SKUs, but every single one is a best-in-class pick.\n',
        '\n> **Philosophy:** 1–2 top skills per category. No duplicates, no noise. Just the essentials.\n',
        '\nThis list is **dynamic** — reviewed and updated monthly.\n',
        '\n---\n',
        '\n## 🚀 Quick Install\n',
        '\n```bash\ngit clone https://github.com/LeoYeAI/openclaw-top100-skills.git\ncp -r openclaw-top100-skills/skills/* ~/.openclaw/workspace/skills/\n```\n',
        f'\n---\n\n## 🗂️ Skill Index ({total} Skills)\n',
    ]

    for cat, skills in CATEGORIES.items():
        lines.append(f'\n### {cat} ({len(skills)})\n')
        lines.append('| Skill | Description |\n|---|---|\n')
        for s in skills:
            desc = get_desc(s)
            lines.append(f'| [`{s}`](skills/{s}/) | {desc} |\n')

    lines.append('\n---\n\n## 🔄 Dynamic Update Policy\n')
    lines.append('\nThis list is reviewed monthly. Skills that fall behind are replaced by better alternatives.\n')
    lines.append('\n---\n\n## 📄 License\n\nMIT License — see [LICENSE](LICENSE) for details.\n')
    lines.append('\n---\n\n<div align="center">\n<sub>Curated from <a href="https://github.com/LeoYeAI/openclaw-master-skills">openclaw-master-skills</a> · Built for the OpenClaw community</sub>\n</div>\n')
    return ''.join(lines)


def generate_zh() -> str:
    total = count_total()
    zh_cats = {
        '🤖 AI & LLM Tools': '🤖 AI & 大模型工具',
        '🔍 Search & Web': '🔍 搜索与网络',
        '📋 Productivity & Office': '📋 生产力与办公',
        '💻 Development & DevOps': '💻 开发与运维',
        '📈 Marketing & Growth': '📈 营销与增长',
        '🎨 Media & Creative': '🎨 媒体与创意',
        '💰 Finance & Trading': '💰 金融与交易',
        '💬 Communication & Messaging': '💬 通讯与消息',
        '🧠 Memory & Agent Enhancement': '🧠 记忆与 Agent 增强',
        '🔒 Security & Auditing': '🔒 安全与审计',
        '📊 Data & Analytics': '📊 数据与分析',
        '📱 Social & Content': '📱 社交与内容',
        '🛠️ Utilities & Misc': '🛠️ 实用工具',
    }

    lines = [
        '<div align="center">\n',
        '# 🏆 OpenClaw Top 100 精选技能\n',
        f'<img src="https://img.shields.io/badge/技能数量-{total}-orange?style=for-the-badge" alt="{total} Skills" />\n',
        '<img src="https://img.shields.io/badge/每月更新-动态维护-green?style=for-the-badge" alt="Monthly Updates" />\n',
        '\n**语言版本：**\n[English](README.md) · [中文](README.zh-CN.md)\n\n</div>\n',
        '\n---\n',
        '\n## 🌟 关于本项目\n',
        '\n**OpenClaw Top 100** 是为 OpenClaw Agent 精心挑选的最核心、高质量的技能合集。就像山姆超市——SKU 少，但每一个都是同类最佳。\n',
        '\n> **核心理念：** 每个类别 1–2 个顶级技能，无重复，无噪音，只留精华。\n',
        '\n本列表是**动态的**——每月审查和更新。\n',
        '\n---\n',
        '\n## 🚀 快速安装\n',
        '\n```bash\ngit clone https://github.com/LeoYeAI/openclaw-top100-skills.git\ncp -r openclaw-top100-skills/skills/* ~/.openclaw/workspace/skills/\n```\n',
        f'\n---\n\n## 🗂️ 技能索引（{total} 个技能）\n',
    ]

    for cat, skills in CATEGORIES.items():
        cat_zh = zh_cats.get(cat, cat)
        lines.append(f'\n### {cat_zh}（{len(skills)} 个）\n')
        lines.append('| 技能 | 描述 |\n|---|---|\n')
        for s in skills:
            desc = get_desc(s)
            lines.append(f'| [`{s}`](skills/{s}/) | {desc} |\n')

    lines.append('\n---\n\n## 🔄 动态更新机制\n')
    lines.append('\n本列表每月审查，落后的技能将被更好的替代品取代。\n')
    lines.append('\n---\n\n## 📄 许可证\n\nMIT 许可证——详见 [LICENSE](LICENSE)。\n')
    lines.append('\n---\n\n<div align="center">\n<sub>精选自 <a href="https://github.com/LeoYeAI/openclaw-master-skills">openclaw-master-skills</a> · 为 OpenClaw 社区而建</sub>\n</div>\n')
    return ''.join(lines)


if __name__ == '__main__':
    en_path = os.path.join(REPO_ROOT, 'README.md')
    zh_path = os.path.join(REPO_ROOT, 'README.zh-CN.md')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(generate_en())
    print(f'✅ Written: {en_path}')

    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(generate_zh())
    print(f'✅ Written: {zh_path}')

    total = count_total()
    print(f'\nTotal skills: {total}')
