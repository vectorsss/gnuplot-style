# Contributing to gnuplot-style

Thank you for your interest in contributing to gnuplot-style! This document provides guidelines and instructions for contributing.

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/vectorsss/gnuplot-style.git
   cd gnuplot-style
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install in development mode with all dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=gnuplot_style

# Run specific test file
pytest tests/test_gnuplot_style.py -v

# Generate reference figures
python tests/test_reference_gnuplot_style.py
```

## Code Style

This project uses several tools to maintain code quality:

- **black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pydocstyle**: Docstring style checking

All these checks run automatically when you commit (via pre-commit hooks). You can also run them manually:

```bash
# Run all checks
pre-commit run --all-files

# Run individual tools
black src/ tests/
isort src/ tests/
flake8 src/ tests/
mypy src/
```

## Making Changes

1. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure:
   - All tests pass
   - Code follows the style guidelines
   - New features have tests
   - Documentation is updated if needed

3. Commit your changes:
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

## Submitting a Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Open a pull request on GitHub

3. Ensure all CI checks pass

4. Wait for review and address any feedback

## Guidelines

### Code Style
- Follow PEP 8
- Use type hints where appropriate
- Write clear, descriptive variable names
- Keep functions focused and small

### Documentation
- Use NumPy-style docstrings
- Include examples in docstrings where helpful
- Update README.md if adding new features

### Testing
- Write tests for all new functionality
- Ensure tests are clear and focused
- Aim for good test coverage

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 72 characters
- Add more detail in the body if needed

## Questions?

Feel free to open an issue if you have questions or need help with your contribution!
