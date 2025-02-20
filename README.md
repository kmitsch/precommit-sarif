# precommit-sarif

## Overview

This project is an exercise in setting up automatic security scans using Semgrep on developers' workstations, resulting in the generation of a SARIF report. The repo includes a GitHub workflow that verifies the presence of the report when a pull request is created.

## SAST Scanning Guidelines

To maintain secure code practices, the maintainers of this repository encourage all commits be scanned using Semgrep, a Static Application Security Testing (SAST) tool. It is suggested that contributors configure a pre-commit hook to automatically scan their code before committing changes. We see several benefits to this approach:
- Early Identification of Vulnerabilities: by running security checks locally before commits, developers can identify and fix vulnerabilities earlier in the development lifecycle, reducing remediation costs and risks.
- Consistent Security Standards: Automation ensures that all code is scanned against the same ruleset, maintaining consistent security standards across the codebase.
- Reduced Review Overhead: Automated checks provide initial security validation, allowing reviewers to focus on more complex code review aspects.

### Setting Up Semgrep for Pre-commit

1. **Install Semgrep:**
   - [Official quickstart](https://semgrep.dev/docs/getting-started/quickstart)

2. **Configure Pre-commit Hook:**
   Ensure you have `pre-commit` installed:
   - [Official pre-commit install instructions](https://pre-commit.com/#install)
   
   Then, clone or pull a fresh copy of this repo and ensure you now have a local copy of `.pre-commit-config.yaml` available in the base directory.
  
3. **Install the Pre-commit Hook:**
   Run the following from the root directory of the repo: 
   ```sh
   pre-commit install
   ```

4. **That's it**
   Your next commit will automatically run a Semgrep scan and generate a SARIF report.

### Running Semgrep Manually

To manually run a scan:
```sh
semgrep --config=p/python --sarif --output=semgrep-python-results.sarif
```

### SARIF Report

The scan generates a `semgrep-python-results.sarif` file, which should be included with submitted commits.

