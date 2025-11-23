import re


def render_template(template, context):
    """
    Render a template string with variable substitution.
    
    Args:
        template: A string containing {{ variable }} placeholders
        context: A dictionary containing values for substitution
    
    Returns:
        The rendered template string
    
    Example:
        >>> tpl = "Hello, {{ user.name }}!"
        >>> ctx = {"user": {"name": "Karthik"}}
        >>> render_template(tpl, ctx)
        'Hello, Karthik!'
    """
    def replace_variable(match):
        variable_path = match.group(1).strip()
        keys = variable_path.split('.')
        
        value = context
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return match.group(0)  # Return original if key not found
        
        return str(value)
    
    # Pattern to match {{ variable.path }}
    pattern = r'\{\{\s*([^}]+)\s*\}\}'
    return re.sub(pattern, replace_variable, template)


__all__ = ['render_template']
