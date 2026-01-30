# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it to us privately before disclosing it publicly.

### How to Report

1. Email us at: [INSERT SECURITY EMAIL]
2. Include "Security Vulnerability" in the subject line
3. Provide as much detail as possible about the vulnerability
4. Include steps to reproduce (if applicable)

### What to Expect

* We will acknowledge receipt of your report within 48 hours
* We will provide a detailed response within 7 days
* We will work with you to understand and resolve the issue
* We will notify you when the patch is released

### Security Best Practices for Users

* This tool operates through your system clipboard - be aware of what you copy
* Ensure LM Studio is running locally and not exposed to the network
* Keep your Python dependencies updated
* Review the code before running if you have security concerns

### Privacy Considerations

This tool is designed with privacy in mind:

* No data is sent to external APIs (only local LM Studio)
* Clipboard content is processed locally
* No data is stored or logged persistently
* Network access is limited to localhost (LM Studio)

## Security Scope

The following security issues are within scope:

* Remote code execution vulnerabilities
* Data exposure or leakage
* Unauthorized network access
* Clipboard security issues
* Dependencies with known vulnerabilities

The following are out of scope:

* Issues with LM Studio itself (report to LM Studio team)
* General system security issues not related to this tool
* Social engineering attacks
