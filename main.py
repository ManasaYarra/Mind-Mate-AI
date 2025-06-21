import openai

openai.api_key = "your-api-key"  # Replace with your actual OpenAI key

def check_in(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a friendly AI mental health assistant. Respond with empathy and helpful suggestions."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

# Try it
if __name__ == "__main__":
    msg = input("How are you feeling today?\n")
    print(check_in(msg))
