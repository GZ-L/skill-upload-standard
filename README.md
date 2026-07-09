# Skill Upload Standard

这是一个给 GitHub 技能上传流程使用的统一规范。目标是：无论使用哪个上传 Skill、哪个上传脚本、哪个 Agent，只要上传的是 Codex / Agent Skill，就必须同时写出一份对应技能的详细、专业、可维护说明。

## 解决什么问题

很多 Skill 上传到 GitHub 后，只剩一个 `SKILL.md` 或一堆文件，缺少这些关键信息：

- 这是什么。
- 来源是谁。
- 适合什么场景。
- 怎么安装。
- 怎么使用。
- 输出效果怎么样。
- 有哪些边界和风险。
- 怎么验证它能用。
- 是否允许复制、改造或分发。

本仓库把这些要求固化成规范、模板、Skill 入口和校验脚本。

## 适用场景

这个规范适用于所有准备上传到 GitHub 的 Codex / Agent Skill。重点是让上传结果不只是一组文件，而是一份可以交给未来使用者直接理解和复用的专业 Skill 包。

## 什么时候使用

上传或发布任何 Skill 到 GitHub 前使用本规范，尤其是这些场景：

- 上传自己写的 Codex Skill。
- 上传 Agent Skill。
- 把本地 Skill 备份到 GitHub。
- 把已有工作流整理成可复用 Skill。
- 同步、迁移、发布、归档 Skill 仓库。
- 给第三方项目写 Skill 安装说明或使用说明。

不适用于普通 Web App、脚本工具、数据仓库或一次性草稿，除非它们被包装成可复用 Skill。

## 上传必须包含什么

最低要求：

- `SKILL.md`：技能入口，包含清晰 frontmatter 和可执行工作流。
- `README.md`：GitHub 主页说明，面向使用者而不是只面向作者。
- 来源说明：原创、改造、引用、对标或第三方依赖都必须写清楚。
- 安装说明：本地路径、安装命令、依赖、启用方式。
- 使用说明：触发词、典型流程、输入输出示例。
- 效果说明：能做到什么、不能做到什么、适合什么结果。
- 验证说明：跑过什么检查，如何复现验证。
- 版权/许可证边界：尤其是第三方素材、源码、Release 包和私有内容。

完整规范见 [docs/UPLOAD_STANDARD.md](docs/UPLOAD_STANDARD.md)。

## 推荐仓库结构

```text
my-skill/
├── SKILL.md
├── README.md
├── NOTICE.md
├── agents/
│   └── openai.yaml
├── docs/
│   ├── INSTALL.md
│   ├── USAGE.md
│   └── VALIDATION.md
├── references/
├── scripts/
└── templates/
```

小型 Skill 可以只保留 `SKILL.md`、`README.md`、`agents/openai.yaml` 和必要的 `NOTICE.md`。

## 使用方式

在上传 Skill 前，把本仓库作为标准引用：

```text
上传这个 Skill 前，请按 GZ-L/skill-upload-standard 的规范补齐 README、来源说明、安装说明、使用说明、效果说明和验证说明，并运行验证脚本。
```

也可以直接安装本仓库根目录作为 Skill，之后在上传任务中触发：

```text
Use $skill-upload-standard before uploading this Skill to GitHub.
```

## 校验

对准备上传的 Skill 仓库运行：

```bash
python3 scripts/validate_skill_upload.py /path/to/skill-repo
```

校验通过后再提交和推送。

## 本仓库内容

```text
.
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── docs/
│   └── UPLOAD_STANDARD.md
├── references/
│   └── upload-standard.md
├── scripts/
│   └── validate_skill_upload.py
└── templates/
    ├── NOTICE.md
    └── README.skill.md
```

## 维护原则

- 规范优先保证清晰、来源透明、可复现和可验证。
- 不把所有 Skill 强行变成复杂仓库。
- 文档可以拆分，但使用者必须能从 README 快速知道该 Skill 是否适合自己。
- 不上传未授权第三方内容，不在仓库中保存密钥、token、私有配置或 `.env`。
