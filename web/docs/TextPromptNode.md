# Text Prompt Node

Defines a single text variable for use in the Prompt Builder.

## Description
This node allows you to create a modular text piece, like a subject, style, or quality modifier. You assign it a variable name (e.g., `subject`) and provide the text content.

## Inputs
- **var_name** (STRING): The name of the variable. This is how you will reference it in the Prompt Builder template (e.g., `{subject}`).
- **text** (STRING): The text content for this variable.

## Outputs
- **PROMPT_VAR**: A structured output containing the variable name and value.

## Usage Example
1. Add a **Text Prompt Node**.
2. Set `var_name` to `subject`.
3. Set `text` to `a confident Shiba Inu`.
4. Connect the output to a **Text Prompt Builder**.

![Example](assets/comfyui-promptbuilder-cover.png)
