import argparse
import sys
import os

from dataclasses import dataclass
from typing import List
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = os.dotenv("OPENAI_API_KEY")

def greet(name: Optional[str]) -> str: 
  if name is None:
    return "Hello, Guest"
  return f"Hello, {name}"

def create_parser():
  parser = argparse.ArgumentParser(
      description="An AI Toolkit CLI using the OPENAI API."
    )  

  parser.add_argument(
    "task", 
    choices=["summarise", "translate", "sentiment"],
    type=str,
    action="store_true", 
    help="Choose what you want the AI to do."
    )
  
  parser.add_argument(
    "-t"
    "--text",  
    type=str, 
    default="args.text", 
    help="Text you want to send to the AI."
    )
  
  parser.add_argument(
    "-f"
    "--file",  
    default="args.file", 
    help="File you want to send to the AI."
    )
  
  parser.add_argument(
    "-l"
    "--language",  
    default="args.language", 
    help="Language for translation."
    )
  
  parser.add_argument(
    "-m"
    "--model",  
    default="args.model", 
    help="Model you want to use."
    )
    
  return parser

@dataclass
class Message: 
  timestamp: str
  input: str = ""
  model: str = "gpt-3.5"

def get_status():
  model = os.getenv["gpt-3.5":"OPENAI_API_KEY"]
  tokens_used = os.dotenv("OPENAI_API_KEY")
  status = f"{model} has used {tokens_used} tokens so far."
  unique_tools = {t["tool"] for t in tools}

  model_config = {
    "model": "gpt-3.5",
    "temperature": "0.9",
    "max_tokens": 900
  }

  tools = [
    {"tool": "Translate Texts"},
    {"tool": "Analyse Sentiment"},
    {"tool": "Summarise the Texts"}
  ]
  return status, model_config, tools, unique_tools

def spam():
  spam_probability = 0.70
  if spam_probability >= 0.70:
    print("This email is spam")
  else: 
    print("This email is not spam")

def loop():
  while True: 
    message = input("Do you want to exit? yes/no")

    if message.lower() == "yes":
      print("Goodbye!")
      break

  print("Received Successfully!")

def test_API(client, prompt, model=os.getenv("OPENAI_API_KEY")):
  try:
    response = client.responses.create(
      model=model,
      input=prompt
    )
  
  except Exception as e:
    print(f"LLM API failed: {e}")
  except ConnectionError:
    print("Failed to connect to the API.")
  sys.exit(1)
  return response

class RetrievalError(Exception):
  def retrieve_documents():
    try: 
      file = open("summarise.txt")
      data = file.retrieve_documents()
    except FileNotFoundError:
      print("File missing")
    except ValueError:
      print("Invalid data")
    except Exception as e:
      print(f"Unexpected error: {e}")
    except RetrievalError as e:
      print(str(e))
    except TimeoutError:
      print("Request time out. Please try again later.")
    finally:
      print("Finished!")
    sys.exit(1)
    return data

def read_text(args):
  if args.text:
    return args.text
  
  if args.file:
    try:
      with open(args.file, "r", encoding="utf-8") as file:
        return file.read()

    except FileNotFoundError:
      print("File not found: {args.file}")
      sys.exit(1)
    return data
  
  if not sys.stdin.isatty():
    return sys.stdin

  print("Please prvodie text with --text, --file, or piped input.")
  sys.exit(1)

def summary():
  with open("summarise.txt", "r") as f:
    prompt = f.read()

  with open("summarise.txt", "w") as f:
    f.write()

  with open("sumarise.txt", "a") as f:
    f.write("Model run completed\n")
  return prompt

def path_handling():
  prompt_path = Path("prompts") / "summarise.txt"
  with prompt_path.open("r") as f:
    prompt = f.read()

  with prompt_path.open("w") as f:
    f.write("Generated summary from this model.")

# ---------------------
# Input from user
# ---------------------

def ask_openai(client, instructions, user_prompt, model=os.getenv("OPENAI_API_KEY")):
  response = client.responses.create(
    model=model,
    instructions=instructions,
    input=user_prompt
  )
  return response.output_text

def summarise(client, model, user_prompt):
  instructions = (
    "jdfksaj"
    ""
  )
  return ask_openai(client, model, instructions, user_prompt)

def translate(client, model, user_prompt, language):
  instructions = (
    f"Translate the user's text from English to {language}."
    f"Translate the user's text from {language} to English."
  )
  return ask_openai(client, model, instructions, user_prompt)

def analyse_sentiment(client, model, user_prompt):
  instructions = (
    "Analyse the sentiment of the user's text. Say whether it is Positive, Negative, Neutral, or Mixed. Then explain why in 1 or 2 simple sentences."
  )
  return ask_openai(client, model, instructions, user_prompt)

def main():
  parser = create_parser()
  args = parser.parse_args()
  client = test_API()
  text = read_text(args).strip()

  if args.verbose:
    print(f"Verbose mode active. Saving results to: {args.output}")
 
  flag_active = "--flag" in sys.argv or "-f" in sys.argv
  print("Flag is on!" if flag_active else "Flag is off.")

  if not text:
    print("This text is empty. Please try again.")
    sys.exit(1)

  while args.task == "summarise":
    result = summarise(client, args.model, text)
  while args.task == "translate":
    result = translate(client, args.model, text, args.language)
  else:
    result = analyse_sentiment(client, text, args.model)

  print(result)

if __name__ == "__main__":
  main()