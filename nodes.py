
class TextPromptNode:
    """
    A simple node for defining a single piece of text (a variable).
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"default": "subject"}),
                "text": ("STRING", {"multiline": True, "dynamicPrompts": False}),
            }
        }

    RETURN_TYPES = ("PROMPT_VAR",)
    RETURN_NAMES = ("prompt_var",)
    FUNCTION = "get_text"
    CATEGORY = "PromptBuilder"
    DESCRIPTION = "Defines a text variable with a name. Connect this to the Prompt Builder to use in templates."

    def get_text(self, var_name="subject", text=""):
        return ({"name": var_name, "value": text},)


class TextPromptBuilder:
    """
    The central node that aggregates variables and applies them to a template.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {"multiline": True, "default": "{subject}, {style}", "dynamicPrompts": False}),
            },
            "optional": {
                "variable_a": ("*", {"forceInput": True}),
                "variable_b": ("*", {"forceInput": True}),
                "variable_c": ("*", {"forceInput": True}),
                "variable_d": ("*", {"forceInput": True}),
            }
        }

    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        return True

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "build_prompt"
    CATEGORY = "PromptBuilder"
    DESCRIPTION = "Aggregates variables (connect to variable_a/b/c/d) and inserts them into the template using {name} syntax."

    def build_prompt(self, template, variable_a="", variable_b="", variable_c="", variable_d=""):
        # Helper to extract value and name
        def parse_variable(var):
            if isinstance(var, dict) and "name" in var and "value" in var:
                return var["name"], var["value"]
            return None, str(var)

        # Process variables
        variables = {}
        raw_values = []
        
        for name, val in [("variable_a", variable_a), ("variable_b", variable_b), ("variable_c", variable_c), ("variable_d", variable_d)]:
            if val:
                custom_name, custom_value = parse_variable(val)
                # Add connection name mapping (e.g. variable_a, a)
                variables[name] = custom_value
                variables[name.split("_")[1]] = custom_value
                variables[name.split("_")[1].upper()] = custom_value
                raw_values.append(custom_value)
                
                # Add custom name mapping if available
                if custom_name:
                    variables[custom_name] = custom_value
            else:
                 # Handle empty/unconnected
                 variables[name] = ""
                 variables[name.split("_")[1]] = ""
                 variables[name.split("_")[1].upper()] = ""

        # Simple Python formatting
        try:
            # Check if the template uses placeholder syntax
            if "{" in template and "}" in template:
                prompt = template.format(**variables)
            else:
                # Default concatenation if no template markers found
                if not template.strip():
                     parts = [p for p in raw_values if p]
                     prompt = ", ".join(parts)
                else:
                    prompt = template
                    
        except KeyError as e:
            prompt = f"Error: Missing variable {e} in template. Available variables: {list(variables.keys())}"
        except Exception as e:
             prompt = f"Error: {e}"

        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "TextPromptNode": TextPromptNode,
    "TextPromptBuilder": TextPromptBuilder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextPromptNode": "Text Prompt Node",
    "TextPromptBuilder": "Text Prompt Builder"
}
