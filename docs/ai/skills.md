# Anthropic Agent Skills — Complete Tutorial

> **Last updated:** March 2026  
> **Applies to:** Claude API, Claude.ai (Pro/Max/Team/Enterprise), Claude Code  
> **Beta headers required:** `code-execution-2025-08-25`, `skills-2025-10-02`

---

## Table of Contents

1. [What Are Agent Skills?](#1-what-are-agent-skills)
2. [How Skills Work Under the Hood](#2-how-skills-work-under-the-hood)
3. [Skills vs Tools vs System Prompts](#3-skills-vs-tools-vs-system-prompts)
4. [Level 1 — Using Pre-built Anthropic Skills](#4-level-1--using-pre-built-anthropic-skills)
5. [Level 2 — Your First Custom Skill](#5-level-2--your-first-custom-skill)
6. [Level 3 — Skills with Reference Files](#6-level-3--skills-with-reference-files)
7. [Level 4 — Skills with Executable Scripts](#7-level-4--skills-with-executable-scripts)
8. [Level 5 — Multiple Skills & Versioning](#8-level-5--multiple-skills--versioning)
9. [Level 6 — Organizational & Enterprise Skills](#9-level-6--organizational--enterprise-skills)
10. [Skills in Claude Code](#10-skills-in-claude-code)
11. [Creating & Managing Custom Skills via API](#11-creating--managing-custom-skills-via-api)
12. [SKILL.md Reference](#12-skillmd-reference)
13. [Best Practices](#13-best-practices)
14. [Security Considerations](#14-security-considerations)
15. [Troubleshooting](#15-troubleshooting)
16. [Quick Reference Cheat Sheet](#16-quick-reference-cheat-sheet)

---

## 1. What Are Agent Skills?

Agent Skills are **modular, reusable capability packages** that extend what Claude can do. Each Skill is a folder containing:

- A `SKILL.md` file — instructions, metadata, and guidelines Claude reads
- Optional reference files — documentation, templates, checklists
- Optional scripts — Python or shell scripts Claude can execute

Think of a Skill as an **onboarding manual for Claude**. Instead of re-explaining your workflow or domain every conversation, you write it once as a Skill and Claude loads it automatically whenever it's relevant.

### Two types of Skills

| Type | Source | Use Case |
|------|--------|----------|
| **Anthropic pre-built** | Managed by Anthropic | PowerPoint, Excel, Word, PDF creation |
| **Custom** | Built by you / your org | Domain expertise, company workflows, specialized tasks |

### Where Skills run

Skills are available across:
- **Claude.ai** — web/mobile/desktop (Pro, Max, Team, Enterprise)
- **Claude API** — via the Messages API with beta headers
- **Claude Code** — via the filesystem or plugin marketplace
- **Agent SDK** — for building custom agents

---

## 2. How Skills Work Under the Hood

Understanding this makes you a better Skill author.

### Progressive disclosure

Claude does **not** dump an entire Skill into its context window at once. Instead:

```
1. System prompt loads — contains metadata (name, description) for ALL installed Skills
2. User sends a message
3. Claude sees the metadata and decides which Skill(s) are relevant
4. Claude reads the relevant SKILL.md using a Bash tool call
5. Claude may read additional bundled files if needed
6. Claude executes the task using the loaded instructions
```

This means:
- Skills only consume tokens when they're actually used
- You can bundle large reference files without paying the cost on every request
- The `description` field in frontmatter is the **primary routing signal** — write it carefully

### What happens in the context window

```
[System prompt]                    ← always present
[Skill metadata for all skills]    ← always present (just names + descriptions)
[User message]
  → Claude reads SKILL.md          ← only when skill is triggered
  → Claude reads references/*.md   ← only what's needed
  → Claude executes scripts        ← only if task requires it
```

---

## 3. Skills vs Tools vs System Prompts

| Dimension | Skills | Tools | System Prompt |
|-----------|--------|-------|---------------|
| **Scope** | Reusable across sessions | Per-request | Per-conversation |
| **Trigger** | Auto, based on task match | Explicit call | Always active |
| **Can run code** | Yes | Yes | No |
| **Can bundle files** | Yes | No | No |
| **Max per request** | 8 | Many | 1 |
| **Best for** | Domain expertise, workflows | External APIs, actions | Tone, persona, constraints |
| **Lives in** | Folder on filesystem / API | API request body | API request body |

**Rule of thumb:**
- Use a **Skill** when you find yourself pasting the same instructions across multiple conversations
- Use a **Tool** when Claude needs to call an external API or take a real-world action
- Use a **System Prompt** for persistent persona, tone, or behavioral rules

---

## 4. Level 1 — Using Pre-built Anthropic Skills

The fastest way to start. Anthropic provides four production-ready Skills:

| Skill ID | Capability |
|----------|-----------|
| `pptx` | Create and edit PowerPoint presentations |
| `xlsx` | Create and analyze Excel spreadsheets |
| `docx` | Create and edit Word documents |
| `pdf` | Generate PDF documents |

### Prerequisites

You need three beta headers on every request:

```
anthropic-beta: code-execution-2025-08-25
anthropic-beta: skills-2025-10-02
anthropic-beta: files-api-2025-04-14   ← only if downloading generated files
```

### Example: Create a PowerPoint presentation

**Python:**

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create a 5-slide presentation on RAG pipelines for a technical audience"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)

# Find the file_id in the response
for block in response.content:
    if hasattr(block, 'file_id'):
        print(f"Generated file ID: {block.file_id}")
```

**JavaScript / TypeScript:**

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();

const response = await client.beta.messages.create({
  model: 'claude-sonnet-4-6',
  max_tokens: 4096,
  betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
  container: {
    skills: [
      {
        type: 'anthropic',
        skill_id: 'pptx',
        version: 'latest'
      }
    ]
  },
  messages: [{
    role: 'user',
    content: 'Create a 5-slide presentation on RAG pipelines'
  }],
  tools: [{
    type: 'code_execution_20250825',
    name: 'code_execution'
  }]
});

console.log(response.content);
```

**cURL:**

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "max_tokens": 4096,
    "container": {
      "skills": [
        { "type": "anthropic", "skill_id": "pptx", "version": "latest" }
      ]
    },
    "messages": [{ "role": "user", "content": "Create a presentation about renewable energy" }],
    "tools": [{ "type": "code_execution_20250825", "name": "code_execution" }]
  }'
```

### Downloading the generated file

When Skills create files (PPTX, XLSX, DOCX, PDF), they return a `file_id`. Use the Files API to download:

```python
import anthropic

client = anthropic.Anthropic()

# After getting file_id from the response above...
file_content = client.beta.files.download(
    file_id="file_abc123",
    betas=["files-api-2025-04-14"]
)

with open("output.pptx", "wb") as f:
    f.write(file_content)
```

### Listing available pre-built Skills

```python
skills = client.beta.skills.list(
    source="anthropic",
    betas=["skills-2025-10-02"]
)
for skill in skills.data:
    print(f"{skill.id}: {skill.display_title}")
```

---

## 5. Level 2 — Your First Custom Skill

Custom Skills let you teach Claude your domain, workflow, or organizational knowledge.

### The minimal Skill structure

```
my-skill/
└── SKILL.md
```

That's it. One file is all you need to start.

### SKILL.md anatomy

```markdown
---
name: my-skill-name
description: >
  One to three sentences describing WHAT this skill does and WHEN Claude
  should use it. Be specific about trigger conditions.
  Use action-oriented language: "Use when user asks to...", "Handles..."
---

# Skill Title

[Your instructions here. Write as if briefing a new team member.]

## Section 1: Core Workflow

Step-by-step instructions...

## Section 2: Output Format

Specify exactly how output should look...

## Examples

Show Claude what good output looks like...

## Guidelines

- Guideline 1
- Guideline 2
```

### Example: Python Explainer Skill

```markdown
---
name: python-explainer
description: >
  Explains Python concepts clearly with beginner-friendly examples and real-world context.
  Use when user asks to explain Python syntax, patterns, built-ins, or best practices.
---

# Python Explainer Skill

When asked to explain any Python concept, always follow this structure:

## Required Output Format

**What it is:** One sentence plain-English definition.

**Simplest working example:**
```python
# Minimal code that demonstrates the concept
```

**What each line does:** Brief annotation of the example above.

**Real-world example:**
```python
# A practical use case you'd actually encounter
```

**Common gotchas:**
- Gotcha 1 with explanation
- Gotcha 2 with explanation

## Guidelines

- Calibrate complexity to beginner level unless user says otherwise
- Always run the simple example mentally to verify it works
- If the concept has performance implications, mention them
- Prefer stdlib examples over third-party libraries
```

### Uploading a custom Skill

**Step 1: Zip the skill folder**

```bash
cd my-skill/
zip -r ../my-skill.zip .
```

Or in Python:

```python
import zipfile, io, os

def zip_skill(skill_dir: str) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(skill_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, skill_dir)
                zf.write(filepath, arcname)
    buf.seek(0)
    return buf.read()
```

**Step 2: Upload via API**

```python
import anthropic, io, zipfile

client = anthropic.Anthropic()

skill_zip = zip_skill("./python-explainer")

skill = client.beta.skills.create(
    name="python-explainer",
    betas=["skills-2025-10-02"],
    file=("skill.zip", io.BytesIO(skill_zip), "application/zip")
)

print(f"Skill created: {skill.id}")
# Save this ID — you'll use it in every request
```

**Step 3: Use it**

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": skill.id,
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Explain Python list comprehensions"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

---

## 6. Level 3 — Skills with Reference Files

For complex domains, bundle reference material that Claude loads selectively.

### Folder structure

```
code-reviewer/
├── SKILL.md
└── references/
    ├── style-guide.md
    ├── security-checklist.md
    └── performance-tips.md
```

### SKILL.md with file references

```markdown
---
name: code-reviewer
description: >
  Reviews Python code for quality, security, and performance issues.
  Use when asked to review, audit, critique, or improve code.
  Produces structured feedback with severity ratings.
---

# Code Review Skill

You are a senior engineer performing a structured code review.

## Review Process

### Step 1: Style Review
Read `references/style-guide.md` and check code against every rule.

### Step 2: Security Audit
Read `references/security-checklist.md` and systematically check each item.

### Step 3: Performance Analysis
If the code involves loops, DB queries, or I/O, read `references/performance-tips.md`.

## Output Format

Produce a review with three sections:

### 🔴 Critical Issues
Must fix before merging. Include: file, line number, issue, fix.

### 🟡 Suggestions
Improvements that would meaningfully improve quality.

### 🟢 Praise
What's done well (always include at least one item).

## Severity Ratings
- **Critical:** Security vulnerability, data loss risk, or crash bug
- **Major:** Logic error or significant performance problem
- **Minor:** Style, naming, or readability issue
```

**references/style-guide.md:**

```markdown
# Python Style Guide

## Naming
- Variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

## Functions
- Max length: 30 lines
- Max parameters: 5 (use dataclass/dict for more)
- Every public function needs a docstring

## Imports
- Stdlib first, then third-party, then local
- No wildcard imports (`from x import *`)
- Unused imports are errors

## Error Handling
- Never use bare `except:`
- Always catch specific exceptions
- Log errors with context before re-raising
```

**references/security-checklist.md:**

```markdown
# Security Checklist

## Input Validation
- [ ] All user inputs validated and sanitized
- [ ] No string formatting in SQL queries (use parameterized queries)
- [ ] No `eval()` or `exec()` on user-provided strings

## Authentication & Authorization
- [ ] Passwords hashed (bcrypt/argon2, never MD5/SHA1)
- [ ] Auth checks on every protected endpoint
- [ ] No hardcoded credentials in source code

## Data Exposure
- [ ] No sensitive data in logs
- [ ] Error messages don't leak stack traces to users
- [ ] Secrets loaded from environment variables, not config files
```

---

## 7. Level 4 — Skills with Executable Scripts

Skills can bundle Python scripts that Claude runs during task execution.

### Folder structure

```
data-analyst/
├── SKILL.md
└── scripts/
    ├── clean_data.py
    ├── summarize_stats.py
    └── generate_chart.py
```

### SKILL.md

```markdown
---
name: data-analyst
description: >
  Analyzes CSV and Excel data files. Cleans raw data, produces descriptive
  statistics, and generates charts. Use when user uploads data or asks for
  data analysis, EDA, or visualization.
---

# Data Analyst Skill

You are a data analyst. When working with data files:

## Workflow

### 1. Clean the data
Run the cleaning script first — always:
```bash
python scripts/clean_data.py <input_file> cleaned.csv
```
Report the cleaning summary before proceeding.

### 2. Generate statistics
```bash
python scripts/summarize_stats.py cleaned.csv
```
Interpret the output in plain English. Flag any columns with >20% missing values.

### 3. Generate charts (when requested)
```bash
python scripts/generate_chart.py cleaned.csv <chart_type> <x_col> <y_col> output.png
```
Supported chart types: `line`, `bar`, `scatter`, `histogram`, `box`

## Output Format
Always structure your analysis as:
1. **Data Overview** — shape, columns, types
2. **Data Quality** — nulls, duplicates, anomalies found during cleaning
3. **Key Statistics** — mean, median, distribution notes per column
4. **Insights** — 3–5 plain-English findings
5. **Recommended Next Steps** — what to explore further
```

**scripts/clean_data.py:**

```python
#!/usr/bin/env python3
"""Clean a CSV/Excel file and report what was changed."""
import sys
import pandas as pd

def clean(input_path: str, output_path: str):
    # Load
    if input_path.endswith('.xlsx'):
        df = pd.read_excel(input_path)
    else:
        df = pd.read_csv(input_path)

    original_shape = df.shape
    original_dupes = df.duplicated().sum()

    # Clean column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r'[^\w\s]', '', regex=True)
        .str.replace(r'\s+', '_', regex=True)
    )

    # Remove completely empty rows/cols
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    df.to_csv(output_path, index=False)

    print(f"Original shape: {original_shape}")
    print(f"Final shape: {df.shape}")
    print(f"Rows removed: {original_shape[0] - df.shape[0]}")
    print(f"Duplicates removed: {original_dupes}")
    print(f"\nNull counts per column:")
    print(df.isnull().sum().to_string())
    print(f"\nNull % per column:")
    print((df.isnull().mean() * 100).round(1).to_string())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_data.py <input> <output>")
        sys.exit(1)
    clean(sys.argv[1], sys.argv[2])
```

**scripts/summarize_stats.py:**

```python
#!/usr/bin/env python3
"""Generate descriptive statistics for a cleaned CSV."""
import sys
import pandas as pd

def summarize(csv_path: str):
    df = pd.read_csv(csv_path)

    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    print("=== Numeric Columns ===")
    numeric = df.select_dtypes(include='number')
    if not numeric.empty:
        print(numeric.describe().round(2).to_string())
    else:
        print("No numeric columns found.")

    print("\n=== Categorical Columns ===")
    cat = df.select_dtypes(include='object')
    for col in cat.columns:
        print(f"\n{col}: {df[col].nunique()} unique values")
        print(df[col].value_counts().head(5).to_string())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarize_stats.py <csv_file>")
        sys.exit(1)
    summarize(sys.argv[1])
```

---

## 8. Level 5 — Multiple Skills & Versioning

### Using multiple Skills in one request

You can load up to **8 Skills per request**. Claude selects which ones to use based on task relevance.

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            # Anthropic pre-built skill
            {
                "type": "anthropic",
                "skill_id": "xlsx",
                "version": "latest"
            },
            # Your custom skills
            {
                "type": "custom",
                "skill_id": "skill_data_analyst_abc123",
                "version": "latest"
            },
            {
                "type": "custom",
                "skill_id": "skill_brand_guidelines_xyz789",
                "version": "2"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Analyze this sales CSV and generate a branded Excel report with charts"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

### When to combine Skills

| Scenario | Skills to combine |
|----------|-----------------|
| Analyze data → export to Excel | `data-analyst` + `xlsx` |
| Review code → write Word report | `code-reviewer` + `docx` |
| Parse PDF → create PowerPoint | `pdf` + `pptx` |
| Multi-domain knowledge base | Several domain Skills |

### Versioning strategy

```python
# PRODUCTION — always pin to a specific version
# Prevents unexpected behavior from Skill updates
{
    "type": "custom",
    "skill_id": "skill_abc123",
    "version": "1759178010641129"  # timestamp-based version ID
}

# DEVELOPMENT — always get the latest
{
    "type": "custom",
    "skill_id": "skill_abc123",
    "version": "latest"
}
```

**List versions for a Skill:**

```python
versions = client.beta.skills.versions.list(
    skill_id="skill_abc123",
    betas=["skills-2025-10-02"]
)
for v in versions.data:
    print(f"Version: {v.version_id}, Created: {v.created_at}")
```

### Prompt caching note

> ⚠️ **Important:** Changing the Skills list in your `container` parameter invalidates the prompt cache. If you're using prompt caching (`anthropic-beta: prompt-caching-2024-07-31`), keep your Skills list stable across requests.

---

## 9. Level 6 — Organizational & Enterprise Skills

### Workspace-wide deployment

Admins on Team and Enterprise plans can deploy Skills organization-wide:

1. Go to **Console → Settings → Skills**
2. Upload the Skill ZIP
3. Toggle "Deploy to workspace"
4. All users get the Skill automatically — no individual setup required

### Example: Company knowledge Skill

This pattern is powerful for customer support agents, internal assistants, or any use case where Claude needs to know your company deeply.

**Folder structure:**

```
acme-support-skill/
├── SKILL.md
├── references/
│   ├── product-catalog.md
│   ├── pricing-tiers.md
│   ├── faq.md
│   └── escalation-policy.md
└── scripts/
    └── lookup_customer.py
```

**SKILL.md:**

```markdown
---
name: acme-support-agent
description: >
  Handles customer support for Acme Corp. Knows all products, pricing, and policies.
  Use when user asks about Acme products, pricing, account issues, or needs support.
  Can look up customer records by account ID.
---

# Acme Support Agent

You are a friendly, knowledgeable support specialist for Acme Corp.

## Knowledge Base

**Products:** Read `references/product-catalog.md` for current offerings.
**Pricing:** Read `references/pricing-tiers.md` for exact prices and tiers.
**Common Issues:** Check `references/faq.md` first — most questions are answered there.

## Escalation Rules

Always follow `references/escalation-policy.md`. Key points:
- Never promise refunds without manager approval
- Escalate billing disputes over $500 immediately
- Security incidents go directly to security@acme.com

## Customer Lookup

When the user provides an account ID or email:
```bash
python scripts/lookup_customer.py --id <account_id>
python scripts/lookup_customer.py --email <email>
```
Use the returned data to personalize your response.

## Tone Guidelines

- Warm and professional
- Acknowledge frustration before solving
- Always confirm the issue is resolved before closing
- Sign off with: "Is there anything else I can help you with today?"
```

---

## 10. Skills in Claude Code

Claude Code supports Skills via the filesystem — no API upload needed.

### Installation options

**Option A: Manual install**

```bash
# Copy your skill folder to the Claude Code skills directory
cp -r ./my-skill ~/.claude/skills/my-skill

# Or symlink for active development
ln -s $(pwd)/my-skill ~/.claude/skills/my-skill
```

**Option B: Plugin marketplace**

```bash
# Install from the official Anthropic skills marketplace
claude plugins install anthropics/skills/data-analyst
claude plugins install anthropics/skills/code-reviewer
```

**Option C: Via version control (team sharing)**

```bash
# In your project repo, add a .claude/skills/ directory
mkdir -p .claude/skills
cp -r ./my-skill .claude/skills/

# Claude Code automatically discovers skills in .claude/skills/
# when running in that directory
```

### How Claude Code loads Skills

When you run a task, Claude Code:
1. Scans `~/.claude/skills/` and `.claude/skills/` in your project
2. Loads metadata from each `SKILL.md`
3. Reads the full Skill when a task matches

### Claude Code example

```bash
# With the data-analyst skill installed:
claude "Analyze the sales data in ./data/q4_sales.csv and tell me the top 5 products"

# Claude automatically triggers the data-analyst skill,
# runs the cleaning and stats scripts, and produces the analysis
```

---

## 11. Creating & Managing Custom Skills via API

### Create a Skill

```python
import anthropic, io, zipfile, os

client = anthropic.Anthropic()

# Helper to zip a skill directory
def zip_skill(directory: str) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, directory)
                zf.write(filepath, arcname)
    buf.seek(0)
    return buf.read()

skill_bytes = zip_skill("./my-skill")

skill = client.beta.skills.create(
    name="my-skill",
    betas=["skills-2025-10-02"],
    file=("skill.zip", io.BytesIO(skill_bytes), "application/zip")
)
print(f"Created skill: {skill.id}")
```

### List Skills

```python
# List your custom skills
custom_skills = client.beta.skills.list(
    source="custom",
    betas=["skills-2025-10-02"]
)

# List Anthropic's pre-built skills
anthropic_skills = client.beta.skills.list(
    source="anthropic",
    betas=["skills-2025-10-02"]
)

# List all skills
all_skills = client.beta.skills.list(
    betas=["skills-2025-10-02"]
)
```

### Retrieve a Skill

```python
skill = client.beta.skills.retrieve(
    skill_id="skill_abc123",
    betas=["skills-2025-10-02"]
)
print(f"Name: {skill.name}")
print(f"Created: {skill.created_at}")
```

### Update a Skill (create new version)

```python
updated_skill_bytes = zip_skill("./my-skill-v2")

new_version = client.beta.skills.versions.create(
    skill_id="skill_abc123",
    betas=["skills-2025-10-02"],
    file=("skill.zip", io.BytesIO(updated_skill_bytes), "application/zip")
)
print(f"New version: {new_version.version_id}")
```

### Delete a Skill

```python
client.beta.skills.delete(
    skill_id="skill_abc123",
    betas=["skills-2025-10-02"]
)
```

---

## 12. SKILL.md Reference

### Frontmatter fields

```yaml
---
name: skill-name                    # Required. kebab-case identifier.
description: >                      # Required. What the skill does + when to use it.
  One to three sentences.           # This is the PRIMARY routing signal — write carefully.
  Use action language.
version: "1.0"                      # Optional. Human-readable version string.
compatibility: claude               # Optional. Platform hints (claude, agentskills, etc.)
---
```

### Writing the `description` field

The description is how Claude decides whether to load your Skill. Write it as if giving instructions to a smart assistant:

```yaml
# ❌ Too vague — Claude won't know when to trigger this
description: Helps with data things.

# ❌ Too long — key triggers get buried
description: >
  This skill was created by the data team in Q3 2024 and handles many
  different kinds of data analysis tasks including cleaning, visualization,
  statistical analysis, and reporting across various formats.

# ✅ Clear, action-oriented, specific triggers
description: >
  Analyzes CSV and Excel data files using statistical methods.
  Use when user uploads data files or asks for data analysis, EDA,
  descriptive statistics, or data visualization.
```

### Instruction writing tips

| Do | Don't |
|----|-------|
| Write in imperative: "Read X, then do Y" | Write passively: "X should be read" |
| Specify exact filenames for references | Use vague references like "the guide" |
| Include output format examples | Leave output format ambiguous |
| Use headers to separate concerns | Write one long unbroken block of text |
| Include edge cases and gotchas | Assume Claude knows your domain |

### File organization patterns

**Pattern A: Simple (single SKILL.md)**
```
skill/
└── SKILL.md
```
Best for: Simple instructions, no reference material needed.

**Pattern B: Reference files**
```
skill/
├── SKILL.md
└── references/
    ├── guide-1.md
    └── guide-2.md
```
Best for: Domain knowledge, style guides, checklists.

**Pattern C: Scripts**
```
skill/
├── SKILL.md
└── scripts/
    ├── process.py
    └── helpers.py
```
Best for: Data processing, file manipulation, automation.

**Pattern D: Full**
```
skill/
├── SKILL.md
├── references/
│   ├── domain-knowledge.md
│   └── guidelines.md
├── scripts/
│   ├── main_script.py
│   └── utils.py
└── templates/
    └── output-template.md
```
Best for: Complex organizational workflows.

---

## 13. Best Practices

### Writing Skills

**Start with evaluation, not writing**
Before building a Skill, run Claude on 10–20 representative tasks without it. Note exactly where it fails or needs repeated guidance. Build the Skill to address those specific gaps.

**Keep SKILL.md focused**
If your SKILL.md exceeds ~500 lines, split content into reference files. SKILL.md should be the decision tree; reference files hold the detail.

**Use mutually exclusive sections**
If certain instructions are rarely needed together, put them in separate reference files. Claude will only read what the task requires.

**Code as documentation**
Scripts serve dual purpose: Claude can run them, or read them to understand the expected behavior. Comment your scripts clearly.

### API Usage

**Pin versions in production**

```python
# In production — never use "latest"
"version": "1759178010641129"

# In development — always use "latest"  
"version": "latest"
```

**Combine Skills purposefully**
Only include Skills relevant to the expected task. Loading 8 Skills when 1 is needed wastes tokens and can confuse routing.

**Handle file downloads**

```python
def extract_file_id(response) -> str | None:
    for block in response.content:
        if hasattr(block, 'file_id'):
            return block.file_id
        # Check nested content
        if hasattr(block, 'content'):
            for item in block.content:
                if hasattr(item, 'file_id'):
                    return item.file_id
    return None
```

### Prompt caching

Skills + prompt caching is powerful but has one gotcha:

```python
# ✅ Cache-friendly: stable skills list
container = {
    "skills": [
        {"type": "custom", "skill_id": "skill_abc", "version": "1759..."},
        {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
    ]
}

# ❌ Cache-busting: changing skills or versions breaks the cache
# Don't dynamically alter the skills list between requests
```

---

## 14. Security Considerations

> **Always use Skills from trusted sources only.** Skills can execute code and read files. A malicious Skill can exfiltrate data or take unintended actions.

### Before using a third-party Skill

Audit every file in the Skill ZIP:

```bash
# Inspect Skill contents before deploying
unzip -l third-party-skill.zip
unzip -p third-party-skill.zip SKILL.md
unzip -p third-party-skill.zip scripts/process.py
```

**Red flags to look for:**
- Network calls to unknown URLs
- File reads outside expected paths (`../../etc/passwd`)
- Environment variable access (`os.environ` for non-obvious vars)
- Shell commands that don't match the stated purpose
- Base64-encoded strings (possible obfuscation)

### Principle of least privilege

Design Skills to only access what they need:

```python
# ❌ Overly broad — reads anything
def process(input_path: str):
    with open(input_path) as f:  # Could be anywhere

# ✅ Constrained — only reads from expected directory
def process(input_filename: str):
    safe_dir = Path("./data")
    input_path = safe_dir / input_filename
    input_path = input_path.resolve()
    if not str(input_path).startswith(str(safe_dir.resolve())):
        raise ValueError("Path traversal detected")
    with open(input_path) as f:
        ...
```

### Trust hierarchy

| Source | Trust Level | Action |
|--------|------------|--------|
| Skills you wrote | High | Use freely |
| Anthropic pre-built | High | Use freely |
| Official partner Skills | Medium | Review before deploying |
| Unknown third-party | Low | Full audit required |

---

## 15. Troubleshooting

### Skill not triggering

**Problem:** Claude ignores the Skill and responds from general knowledge.

**Causes & fixes:**
1. **Description is too vague** — Rewrite to include specific trigger phrases ("Use when user asks to...", "Handles...", "Invoked when...")
2. **User prompt doesn't match description** — Test with prompts that use the exact language in your description
3. **Competing Skills** — If multiple Skills could match, the best-matching description wins
4. **Missing beta headers** — Verify `code-execution-2025-08-25` and `skills-2025-10-02` are both present

### Skill triggers but produces wrong output

**Problem:** Skill loads but Claude doesn't follow the instructions correctly.

**Fixes:**
1. **Rewrite instructions imperatively** — "Do X" not "X should be done"
2. **Add concrete examples** — Claude follows examples better than abstract rules
3. **Break into smaller steps** — Long instruction blocks get partially followed; numbered steps work better
4. **Add a "Do NOT" section** — Explicitly call out common mistakes

### Script execution errors

**Problem:** Scripts fail during execution.

**Debugging:**
```python
# Check if the code execution environment has the needed packages
response = client.beta.messages.create(
    ...
    messages=[{
        "role": "user",
        "content": "List all installed Python packages (run: pip list)"
    }],
    ...
)
```

**Common fixes:**
- Stick to packages available in the code execution sandbox (NumPy, Pandas, Matplotlib, Requests are standard)
- Add explicit error handling in scripts and print meaningful error messages
- Test scripts locally before bundling them

### File not found after generation

**Problem:** Skill generates a file but you can't download it.

**Fix:**
```python
# Search more thoroughly for file_id in nested response structures
import json

def find_file_ids(obj, found=None):
    if found is None:
        found = []
    if isinstance(obj, dict):
        if 'file_id' in obj:
            found.append(obj['file_id'])
        for v in obj.values():
            find_file_ids(v, found)
    elif isinstance(obj, list):
        for item in obj:
            find_file_ids(item, found)
    return found

response_dict = json.loads(response.model_dump_json())
file_ids = find_file_ids(response_dict)
print(f"Found file IDs: {file_ids}")
```

### Prompt cache invalidating unexpectedly

**Problem:** Cache is being busted even though you're not changing the prompt.

**Cause:** The Skills list in `container` is changing between requests (e.g., different version IDs, different order).

**Fix:** Hardcode the exact skills list as a constant and reuse it.

```python
SKILLS_CONFIG = {
    "skills": [
        {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
        {"type": "custom", "skill_id": "skill_abc123", "version": "1759178010641129"}
    ]
}

# Use the same object in every request — don't reconstruct it
```

---

## 16. Quick Reference Cheat Sheet

### API Request Template

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-6",           # or claude-opus-4-6
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",      # REQUIRED for skills
        "skills-2025-10-02",              # REQUIRED for skills
        # "files-api-2025-04-14",         # Add if downloading files
        # "prompt-caching-2024-07-31",    # Add if using caching
    ],
    container={
        "skills": [
            # Pre-built: pptx, xlsx, docx, pdf
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"},
            # Custom:
            {"type": "custom", "skill_id": "skill_XXXX", "version": "latest"},
        ]
    },
    messages=[{"role": "user", "content": "Your prompt here"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

### SKILL.md Template

```markdown
---
name: my-skill
description: >
  What this skill does. Use when user asks to [trigger condition].
  Handles [specific domain or task type].
---

# Skill Name

## Workflow
1. First step
2. Second step

## Output Format
Describe exactly what output should look like.

## Guidelines
- Key rule 1
- Key rule 2

## Examples
[Show good input/output examples]
```

### Pre-built Skill IDs

| Task | `skill_id` |
|------|-----------|
| PowerPoint | `pptx` |
| Excel | `xlsx` |
| Word document | `docx` |
| PDF | `pdf` |

### Key limits

| Limit | Value |
|-------|-------|
| Max Skills per request | 8 |
| Skill ZIP size | Check current docs |
| Skill SKILL.md size | Effectively unbounded (loaded progressively) |

### Useful links

- **Official docs:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- **API quickstart:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart
- **Skills cookbook:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/cookbook
- **Official skills repo:** https://github.com/anthropics/skills
- **Open standard:** https://agentskills.io
- **Anthropic Academy:** https://anthropic.skilljar.com

---

*This tutorial is maintained as a living document. Check the official Anthropic docs for the latest beta header versions and API changes.*