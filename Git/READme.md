# GIT Commands

### Clone a repository - *downloads a repository and creates remote repository* **(LOCAL)**
- `git clone <repo-url>` **Note:** rep-url is under “code” ending in .git
    - Most times, paste into IDE’s clone feature instead of using git clone `<repo-url>`
    - Pick a repository location to store `.git` and repo files locally on pc

### Branches - *creating and switching to a branch* **(LOCAL)**
- *Both* creating and switching to branches:
    - `git checkout -b <branch-name>`
- *Only* switch to branch:
    - `git switch <branch-name>`
    - `git checkout <branch-name>` **Note:** outdated, not recommended
- *Only* create branch:
    - `git branch <branch-name>`

### Git statuses - *current git status* **(LOCAL)**
- `git status` **Note:** Displays status for deleted files, added files, untracked files, and branch you’re on

### Git staging - *deleted files, added files, untracked files* **(LOCAL)**
- Stage all files from current directory viewpoint:
    - `git add .` **Note:** Only stages files at/below current directory
    - `git add -A` **Note:** Stages all files in staging area
- Stage a file or folder
    - `git add <file or folder>`
        - If path, then git needs to be able to find it in current directory
        - If contains duplicate, then a path is needed
- Unstage all files in staging area
    - `git reset` **Note:** See “Git stage/commit undo” for more detail
    - `git restore --staged` **Note:** Outdated
- Stage certain chunks of area
    - `git add -p` **Note:** Certain lines of information
- Different of staged area
    - `git diff --staged`

### Git commit - *committing* **(LOCAL)**
- Commits messages to local repo
    - `git commit -m “<message>”`
- Stage & commit
    - `git commit -a -m “<message>”`
- View commit log (simplified)
    - `git log —oneline`
- View commit log
    - `git log`
- Undo last commit but keep staged changes
    - `git reset --soft HEAD~1` **Note:** See below for more detail

### Git undo stage/commit - *(only do this if there are no pushes to GitHub)* **(LOCAL)**
- `git reset <optional:mode> <optional:HEAD~<integer>> <optional: file name or path>`
    - If path, then git needs to be able to find it in current directory
    - If duplicate, then a path is needed
    - mode:
        - —hard - *not recommended* **Note:** Reset directory, staging, and git history back to commit
        - —mixed - *Reset staging and git history locally, does not reset directory*
        - —soft - *Combines all previous staging into one*
    - `HEAD~<integer>`
        - integer: default 1

### Git pushing **(GitHub)**
- Push branch if it does NOT exist on GitHub
    - `git push -u origin <branch-name>`
- Push branch if it exists on GitHub
    - `git push`

### Git pushing undo - **(LOCAL -> GitHub)**
- **Way 1:** Undo commit/staging and restage/recommit (Erase History)
- **Way 2:** Undo the history - creates a new commit with reversed changed (New History)
    - `git revert <commit id>`
    - `git revert <optional:HEAD~<integer>>`
        - integer: default 1 
---
#### Copyright © 2026 Chris Sexton. All rights reserved.
