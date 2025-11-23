# stringheist
String template rendering library with support for nested variable access.

## Installation

```bash
pip install -e .
```

## Usage

```python
from stringheist import render_template

# Basic usage
tpl = "Hello, {{ user.name }}!"
ctx = {"user": {"name": "Karthik"}}
print(render_template(tpl, ctx))  # Output: Hello, Karthik!
```

## Features

- Simple variable substitution with `{{ variable }}` syntax
- Support for nested dictionary access (e.g., `{{ user.name }}`)
- Multiple variable substitutions in a single template
- Graceful handling of missing keys (returns original placeholder)

## Testing

Run the tests using:

```bash
python -m unittest tests.test_render_template
```
