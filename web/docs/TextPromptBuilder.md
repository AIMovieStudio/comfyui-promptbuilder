# Text Prompt Builder

Combines multiple text variables into a final prompt using a template.

## Description
This node takes inputs from multiple **Text Prompt Nodes** and assembles them based on a template string. It supports named placeholders (like `{subject}`) and input slot placeholders (like `{a}`).

## Inputs
- **template** (STRING): The template string. Use `{variable_name}` to insert variables.
- **variable_a** ... **variable_d**: Connect **Text Prompt Nodes** here.

## Outputs
- **string**: The final constructed prompt string.

## Template Syntax
- **By Name**: `{subject}` (matches `var_name` in the connected node)
- **By Slot**: `{variable_a}`, `{variable_b}`...
- **By Short Slot**: `{a}`, `{b}`...

## Usage Example
1. Connect a node with `var_name="subject"` to `variable_a`.
2. Connect a node with `var_name="style"` to `variable_b`.
3. Set template to: `Epic shot of {subject}, {style}`.
4. Result: "Epic shot of a confident Shiba Inu, wearing a superhero cape".

![Example](assets/comfyui-promptbuilder-cover.png)
