import random, os, time, tweepy
from openai import OpenAI

from twitter import *
import tweepy
client = OpenAI()

# OpenAI API setup

# Twitter API setup

client = tweepy.Client(
    bearer_token=your_bearer_token,
    consumer_key=your_api_key,
    consumer_secret=your_api_secret_key,
    access_token=your_access_token,
    access_token_secret=your_access_token_secret
)

prompts = [
    "Share a productivity tip for tech enthusiasts.",
    "Write an engaging tweet about the latest trends in AI.",
    "Share a fun fact about technology evolution.",
    "Offer advice on improving workflows with AI tools.",
    "Write a motivational tweet about tech careers.",
    "Suggest a productivity tool or app for developers.",
    "Create a quick tip for staying updated with AI news."
]

while True:
    # Select a random prompt
    prompt = random.choice(prompts)

    # Generate tweet using GPT
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a social media expert for tech, AI, and productivity."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=random.uniform(0.7, 1.0),
        top_p=random.uniform(0.8, 1.0)
    )
    tweet = response['choices'][0]['message']['content']


try:
    # Post a tweet
    response = client.create_tweet(text=tweet)
    print(f"Tweet posted successfully: {response}")
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")

try:
    user = client.get_me()
    print(f"App is authenticated. Logged in as: {user.data['username']}")
except tweepy.TweepyException as e:
    print(f"Authentication failed: {e}")
