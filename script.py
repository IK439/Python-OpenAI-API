from openai import OpenAI

client = OpenAI()

user_profile = {
  "dietary_restrictions": "nuts, pineapple",
  "cuisine_preferences": "chinese, indian",
  "ingredients_available": "salt, pepper"
}

# 3 string variables used to begin, and shape the user prompt
user_content1 = f"I want to create a recipe blog post. Here are my dietary restrictions: {user_profile['dietary_restrictions']}. My cuisine preferences include: {user_profile['cuisine_preferences']}. The ingredients I have available are: {user_profile['ingredients_available']}."

user_content2 = f"Please provide a blog post with a title, description, ingredients, and instructions. Format the ingredients and instructions as follows: Ingredients should be bulleted, and instructions should be numbered."

user_content3 = f"The recipe must use only the listed ingredients and should result in a single blog post with instructions not exceeding six steps"

# System and user prompt dictionaries containing instructions for the AI
system_prompt = {
  "role": "system",
  "content": "Generate an HTML code for a recipe blog that considers dietary restrictions, cuisine type, and ingredients."
}

user_prompt = {
  "role": "user",
  "content": user_content1 + "\n" + user_content2 + "\n" + user_content3
}

# Initiate a chat completion using the gpt-3.5 model
try:
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[system_prompt, user_prompt]
    )
  print(response.choices[0].message.content) # output the chat completion reply
except Exception as e:
  print(f"Error: {e}")