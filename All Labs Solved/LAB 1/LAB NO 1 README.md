# AI-216: Programming for AI
## Lab 01 Complete Task Report (Tasks 1 – 9)

---

## 🧑‍🎓 Student & Project Details
- **Student Name:** Ali
- **Registration ID:** 10325
- **Course Title:** AI-216: Programming for AI
- **Repository Name:** `ALL LABS PFAI-10325`
- **Lab Folder:** `LAB 1`
- **Script File:** `Ali_10325_Lab1.py`

---

## 📌 Lab Overview
This report documents the step-by-step execution of **Tasks 1 through 9** for Lab 01. It covers repository workspace initialization, global identity configuration, gitignore rules, Python script implementation, branching/merging workflows, and remote synchronization with GitHub.

---

## 📋 Comprehensive Tasks 1 to 9 Report

### Task 1: Directory Architecture Setup
Created a clean directory structure for storing all lab coursework inside the main workspace `ALL LABS PFAI-10325`:
- `LAB 1/`
- `LAB 2/`
- `LAB 3/`
- `LAB 4/`

---

### Task 2: Git Repository Initialization
Initialized a local Git version control tracking system inside the workspace root directory.

**Command Executed:**
```bash
git init
Output: Initialized empty Git repository in .../ALL LABS PFAI-10325/.git/

Task 3: Developer Identity Configuration
Configured global Git user credentials (user.name and user.email) to ensure proper commit authorship and audit tracking.

Commands Executed:

Bash
git config --global user.name "AliShah zaib"
git config --global user.email "zaibalishah289@gmail.com"
Task 4: Python Script Development
Authored the main Lab 01 Python script named Ali_10325_Lab1.py inside the LAB 1/ directory.

Key Script Features:

Module-level docstrings containing Student Name, ID, and Course information.

Imported sys module to output system Python version details (sys.version).

Printed reflective output describing the significance of version control in AI programming.

Task 5: Root .gitignore Configuration
Created a root-level .gitignore file to ensure build artifacts, Python bytecode cache, and IDE configuration files are excluded from Git tracking.

File Contents (.gitignore):

Plaintext
# Python cache
__pycache__/
*.pyc

# Virtual environments
.venv/
venv/

# Jupyter checkpoints
.ipynb_checkpoints/

# VS Code settings
.vscode/
Task 6: Feature Branch Workflow Creation
Created and switched to a dedicated feature branch named week01-readme-improve to isolate feature updates from the master branch.

Command Executed:

Bash
git checkout -b week01-readme-improve
Output: Switched to a new branch 'week01-readme-improve'

Task 7: Staging and Initial Commit
Staged all workspace files (Ali_10325_Lab1.py, .gitignore, and documentation) and performed the initial version snapshot commit.

Commands Executed:

Bash
git add .
git commit -m "Lab01: initial push with script and gitignore"
Task 8: Comprehensive Lab Documentation (README.md)
Authored this detailed README.md report inside the LAB 1/ directory summarizing all 9 lab tasks, technical workflows, and learning outcomes.

Task 9: Branch Merging & GitHub Upstream Push
Switched back to the master branch, merged the week01-readme-improve feature branch, linked the local repository to GitHub, and executed the final remote push.

Commands Executed:

Bash
git checkout master
git merge week01-readme-improve
git remote add origin <your-github-repo-url>
git push -u origin master
🤖 AI / ML Relevance
Reproducibility: Version control guarantees that ML model scripts, dataset configurations, and pipeline code remain strictly tracked and reproducible.

Collaboration: Branch workflows allow data scientists to test experimental algorithms without polluting production codebases.

Auditability: Commit history tracks exact changes in model training parameters and script development.

📝 AI Usage & Prompt Log
Rule Verification: Consulted AI for best practices regarding .gitignore patterns for Python/VS Code workspaces.

Documentation Formatting: Verified GitHub Markdown styling for professional lab reporting.

Audit Check: Checked Git execution history via git log --oneline to confirm all tasks completed successfully.
