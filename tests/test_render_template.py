import unittest
from stringheist import render_template


class TestRenderTemplate(unittest.TestCase):
    
    def test_basic_variable(self):
        """Test basic variable substitution."""
        tpl = "Hello, {{ name }}!"
        ctx = {"name": "Karthik"}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, Karthik!")
    
    def test_nested_variable(self):
        """Test nested dictionary access."""
        tpl = "Hello, {{ user.name }}!"
        ctx = {"user": {"name": "Karthik"}}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, Karthik!")
    
    def test_deep_nested_variable(self):
        """Test deeply nested dictionary access."""
        tpl = "{{ person.address.city }}"
        ctx = {"person": {"address": {"city": "New York"}}}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "New York")
    
    def test_multiple_variables(self):
        """Test multiple variable substitutions."""
        tpl = "{{ greeting }}, {{ user.name }}! You are {{ age }} years old."
        ctx = {"greeting": "Hello", "user": {"name": "Karthik"}, "age": 25}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, Karthik! You are 25 years old.")
    
    def test_missing_key(self):
        """Test behavior when key is missing."""
        tpl = "Hello, {{ missing }}!"
        ctx = {"name": "Karthik"}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, {{ missing }}!")
    
    def test_missing_nested_key(self):
        """Test behavior when nested key is missing."""
        tpl = "Hello, {{ user.missing }}!"
        ctx = {"user": {"name": "Karthik"}}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, {{ user.missing }}!")
    
    def test_whitespace_handling(self):
        """Test that whitespace is handled correctly."""
        tpl = "Hello, {{user.name}}!"
        ctx = {"user": {"name": "Karthik"}}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, Karthik!")
        
        tpl = "Hello, {{  user.name  }}!"
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, Karthik!")
    
    def test_no_variables(self):
        """Test template with no variables."""
        tpl = "Hello, World!"
        ctx = {}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "Hello, World!")
    
    def test_empty_template(self):
        """Test empty template."""
        tpl = ""
        ctx = {"name": "Karthik"}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "")
    
    def test_numeric_value(self):
        """Test numeric value substitution."""
        tpl = "The answer is {{ value }}."
        ctx = {"value": 42}
        result = render_template(tpl, ctx)
        self.assertEqual(result, "The answer is 42.")


if __name__ == '__main__':
    unittest.main()
