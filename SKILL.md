---
name: skill-upload-standard
description: Enforce professional GitHub documentation for Codex or Agent Skills before upload. Use when uploading, publishing, backing up, syncing, or creating a GitHub repository for any Skill; when the user says "上传技能", "发布Skill", "同步到GitHub", "技能说明", "上传规范", or wants every uploaded Skill to include detailed professional documentation. Do not use for ordinary non-Skill application deployment, throwaway drafts, or repositories that are not meant to document a reusable Skill.
---

# Skill Upload Standard

Use this Skill before publishing any Codex or Agent Skill to GitHub. It makes the upload package self-explanatory, source-aware, installable, usable, and reviewable.

## Operating Principles

- Every uploaded Skill must include a professional explanation of what it is, where it came from, how to install it, how to use it, what results to expect, and how it was validated.
- Treat source and rights as first-class metadata. If the Skill is derived from an upstream project, tutorial, template, article, or another account, document that source clearly.
- Do not upload third-party assets, source code, build artifacts, datasets, credentials, or extension packages unless the license and user request explicitly allow it.
- Default documentation language is Chinese for this user's repositories. Preserve official names, commands, file names, and API identifiers in English where needed.
- Keep the repository useful to a future operator who has no prior chat context.

## Workflow

1. Inspect the Skill being uploaded.
   - Read `SKILL.md`, supporting `references/`, scripts, templates, examples, and existing README files.
   - Identify whether the Skill is original, adapted from an upstream source, or only an installation guide for third-party software.
2. Read `references/upload-standard.md`.
   - Apply its required documentation sections and source disclosure rules.
3. Create or update the uploaded Skill documentation.
   - Use `templates/README.skill.md` for GitHub README structure.
   - Add `NOTICE.md` when upstream source, license, redistribution, or attribution needs to be explicit.
   - Add `docs/INSTALL.md`, `docs/USAGE.md`, or `docs/VALIDATION.md` when README would become too long.
4. Validate before publishing.
   - Run `python3 scripts/validate_skill_upload.py <path-to-skill-repo>`.
   - Fix every error. Warnings may remain only when documented in the final response.
5. Publish intentionally.
   - Stage only the Skill package and its documentation.
   - Commit with a clear message.
   - Push to GitHub.
   - Report the repository URL, changed files, validation commands, and any assumptions.

## Documentation Contract

The uploaded Skill must answer these questions:

- What is this Skill?
- Who should use it, and when should it trigger?
- What source, account, repository, or reference is it based on?
- What files are included?
- How do you install it?
- How do you use it?
- What output or effect should the user expect?
- What are the boundaries, non-goals, and safety restrictions?
- What validation was run?
- What license or redistribution constraints apply?

## Resource Routing

- Read `references/upload-standard.md` for the required upload policy and section-level writing rules.
- Use `templates/README.skill.md` when writing or replacing a GitHub README for an uploaded Skill.
- Use `templates/NOTICE.md` when the Skill has an upstream source, third-party content, private source, or licensing boundary.
- Run `scripts/validate_skill_upload.py` against the final repository before committing.

## Validation

Run:

```bash
python3 scripts/validate_skill_upload.py <path-to-skill-repo>
```

The upload is not ready until the validator exits successfully and the documentation answers the contract above.
