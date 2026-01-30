# Contributing to Social Media Context Reply Bot

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub and include:

* A clear and descriptive title
* Steps to reproduce the bug
* Expected behavior vs. actual behavior
* Your environment details (OS, Python version, LM Studio version)
* Any error messages or screenshots

### Suggesting Features

Feature suggestions are welcome! Please open an issue with:

* A clear description of the feature
* Why you think it would be useful
* Any implementation ideas (optional)

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature/fix: `git checkout -b feature-name`
3. Make your changes
4. Follow the coding style guidelines below
5. Test your changes thoroughly
6. Commit your changes with a clear message
7. Push to your fork: `git push origin feature-name`
8. Open a pull request

## Coding Guidelines

### Python Style

* Follow PEP 8 style guidelines
* Use meaningful variable and function names
* Add docstrings to functions and classes
* Keep functions focused and small
* Add type hints where appropriate

### Code Organization

* Keep the main script (`social_media_context_reply.py`) focused on core functionality
* Add new features in a modular way
* Consider creating separate modules for complex features

### Documentation

* Update README.md if you add new features
* Add inline comments for complex logic
* Update any relevant documentation

## Development Setup

1. Clone your fork locally
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make sure LM Studio is running with a model loaded

## Testing

* Test your changes with different LM Studio models
* Verify clipboard functionality works on your OS
* Test edge cases and error handling
* Ensure the hotkey combinations don't conflict

## Project Structure

```
SocialMediaReplier/
├── social_media_context_reply.py  # Main script
├── README.md                  # Project documentation
├── CODE_OF_CONDUCT.md         # Community guidelines
├── CONTRIBUTING.md            # This file
├── LICENSE                    # Project license
└── requirements.txt           # Python dependencies
```

## Getting Help

If you need help with contributing:

* Check existing issues and pull requests
* Read the documentation thoroughly
* Ask questions in issues (tag them as "question")

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in the README.md file. Thank you for making this project better!
