# Upload Standard Reference

Read this reference before uploading any Skill to GitHub.

## Required Documentation Sections

Every uploaded Skill repository should include a README with these sections or equivalent clear wording:

- `这是什么` / `What This Is`
- `来源与归属` / `Source and Ownership`
- `适用场景` / `When To Use`
- `能力与效果` / `Capabilities and Expected Results`
- `安装` / `Installation`
- `使用方法` / `Usage`
- `输入与输出` / `Inputs and Outputs`
- `文件结构` / `Repository Structure`
- `验证` / `Validation`
- `边界与注意事项` / `Limitations and Safety`
- `许可证` / `License`

Small Skills can combine sections, but none of the information may be missing.

## Source Disclosure Wording

Use direct wording:

- Original: `本 Skill 为原创工作流，由 GZ-L 维护。`
- Adapted: `本 Skill 改造自 <source>，主要改动包括 <scope>。`
- Benchmarked: `本 Skill 对标 <source> 的公开能力描述，没有复制未授权源码或资源。`
- Installer: `本仓库只提供安装说明和校验脚本，不重新分发上游软件本体。`
- Private workflow: `本 Skill 来自个人/团队工作流经验，不代表外部官方说明。`

## Documentation Quality Bar

Professional documentation is not long by default. It is specific:

- Names exact files and paths.
- Uses copy-pastable commands.
- Describes expected output.
- States assumptions.
- States what was validated.
- States what is not covered.

Avoid vague claims such as:

- `功能强大`
- `一键搞定`
- `效果很好`
- `支持各种场景`

Replace them with observable behavior and examples.

## Upload Workflow

1. Inspect the Skill folder.
2. Identify origin and ownership.
3. Fill README from `templates/README.skill.md`.
4. Add `NOTICE.md` if source or rights are non-trivial.
5. Run `scripts/validate_skill_upload.py <repo>`.
6. Fix all errors.
7. Commit and push.
8. Report URL, files changed, validation results, and assumptions.
