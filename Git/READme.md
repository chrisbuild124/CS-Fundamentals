# GIT Commands 

### General - *general git understanding*
- `REMOTE`vs `LOCAL`
  - `REMOTE` = On GitHub
  - `LOCAL` = On local pc
- `Fork` vs `Clone` *Fork is very similar to clone*
  - Fork: **(REMOTE)**, upstream link
  - Clone: **(LOCAL)** no upstream link
- `Staging` vs `Commit` vs `Push`
  - `Staging` is temp storage for commit operations 
  - `Commit` is changes to local repo
    - Physical entity 
  - `Push` is changes to REMOTE repo
    - Transfer of physical entity
- The following are pushed to REMOTE when pushing **(LOCAL -> REMOTE)**
  - `Branches`
  - `Commits`
  - `Tags`
- local `.git` is NOT pushed to REMOTE repo
- `upstream` vs `downstream`
  - `upstream` is the parent repo
  - `downstream` is the child repo
- `origin` = substituted in https URL of repo

### Clone a repository - *downloads a repository and creates remote repository* **(LOCAL)**
- `git clone <repo-url>` **Note:** rep-url is under “code” ending in .git
  - Most times, paste into IDE’s clone feature instead of using git clone `<repo-url>`
  - Pick a repository location to store `.git` and repo files locally on pc
- - `git clone <repo-url> .` **Note:** puts files in current directory and doesn't create a file

### Clone fetch, upstream - *fetches latest commits from remote repo, no merge* **(LOCAL)**
- `git remote -v` **Note:** Displays current remote repo url connections
- `git remote add upstream <original-repo URL>.git`
- `git fetch upstream` **Note:** Fetches latest updates from upstream repos
- `git fetch origin`*Note:* Fetches latest updates from direct parent repo

### Clone merge - *merges latest commits after fetching* **(LOCAL)**
- `git merge upstream/main` **Note:** Merges latest fetch updates into current branch
- `git merge origin/main` *Note:* Merges latest fetch updates into current branch

### Clone pull - *fetch + merge*
- `git pull origin <branch:main example>` *Note:* Pulls latest updates from direct parent repo and merges into current branch
- `git pull upstream <branch:main example>` **Note:** Pulls latest updates from upstream repos and merges into current branch

### Fork a repository - *done on GitHub* **(Remote -> LOCAL)**
- Steps:
  1. Fork repo on GitHub **(REMOTE)**
  2. Clone forked repo to local pc **(LOCAL)**
  3. Add parent repo as remote to local pc **(LOCAL)**
     - `git remote add <upstream_name> <parent-repo-url>`
- Convention: Treat forked repo (downstream) main as identical to parent repo (upstream) main
- Very similar to clone, but:
  - done on GitHub, logged as forked
  - Github knows `origin` of forked repo

### Submodule - *create a direct import to a repository* **(LOCAL)**
- `git submodule add <submodule-repo-url> <desired path>/<submodule-folder-name>`
- `git submodule deinit -f <path>` *Note:* Deletes from .git configuration
- `rm -rf .git/modules/<path>` *Note:* Deletes from .gitmodules
- `git rm -f <path>` *Note:* Deletes from repository 

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

### Git rebase - *optional: moves commit history to a new base commit* **(LOCAL)**
- `git rebase <branch:origin/main>` *Note:* Moves oroginal branch commit. Could be used after pushing. 

### Git stage/commit undo - *(only do this if there are no pushes to REMOTE repo)* **(LOCAL)**
- `git reset <optional:mode> <optional:HEAD~<integer>> <optional: file name or path>`
  - If path, then git needs to be able to find it in current directory
  - If duplicate, then a path is needed
  - mode:
    - —hard - *not recommended* **Note:** Reset directory, staging, and git history back to commit
    - —mixed - *Reset staging and git history locally, does not reset directory*
    - —soft - *Combines all previous staging into one*
    - `HEAD~<integer>`
      - integer: default 1

### Git pushing **(REMOTE)**
- Push branch if branch does NOT exist on REMOTE repo
  - `git push -u origin <branch-name>`
- Push branch if it exists on REMOTE repo
  - `git push`

### Git pushing undo - **(LOCAL -> REMOTE)**
- **Way 1:** Undo commit/staging and restage/recommit (Erase History, see prev sections)
- **Way 2:** Undo the history - creates a new commit with reversed changed (New History)
  - `git revert <commit id>`
  - `git revert <optional:HEAD~<integer>>`
    - integer: default 1 
---
#### Copyright © 2026 Chris Sexton. All rights reserved.
