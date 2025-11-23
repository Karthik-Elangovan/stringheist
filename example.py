"""
Example usage of the stringheist library.
"""

from stringheist import render_template

# Basic usage
tpl = "Hello, {{ user.name }}!"
ctx = {"user": {"name": "Karthik"}}
print(render_template(tpl, ctx))  # Output: Hello, Karthik!

# Multiple variables
tpl = "{{ greeting }}, {{ user.name }}! You are {{ age }} years old."
ctx = {"greeting": "Hi", "user": {"name": "Alice"}, "age": 30}
print(render_template(tpl, ctx))  # Output: Hi, Alice! You are 30 years old.

# Deeply nested access
tpl = "City: {{ person.address.city }}, Country: {{ person.address.country }}"
ctx = {
    "person": {
        "address": {
            "city": "New York",
            "country": "USA"
        }
    }
}
print(render_template(tpl, ctx))  # Output: City: New York, Country: USA
