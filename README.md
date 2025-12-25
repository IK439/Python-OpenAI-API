# Python-OpenAI-API

This Python script uses the OpenAI API to generate HTML code for a recipe blog post. It customizes recipes based on a user's dietary restrictions, cuisine preferences, and available ingredients.  

## Features

- Collects user dietary restrictions, preferred cuisines, and available ingredients.  
- Sends structured prompts to OpenAI's GPT-3.5 model.  
- Generates an HTML-formatted recipe blog post including:  
  - Title  
  - Description  
  - Bulleted list of ingredients  
  - Numbered step-by-step instructions (maximum six steps)  
- Ensures the recipe only uses the ingredients provided by the user.  

## Usage

1. Define a `user_profile` dictionary with dietary restrictions, cuisine preferences, and available ingredients.  
2. Set up the system prompt with instructions for HTML output.  
3. Combine prompts and call `client.chat.completions.create()` from the OpenAI Python SDK.  
4. Receive the AI-generated HTML recipe post as output.  

```python
user_profile = {
  "dietary_restrictions": "nuts, pineapple",
  "cuisine_preferences": "chinese, indian",
  "ingredients_available": "salt, pepper"
}
```

The script will generate an HTML recipe that respects these restrictions and preferences.
