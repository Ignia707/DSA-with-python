
# * i skipped the basics

history = []

def browser_history (action, stack):
  if ".com" in action:
    stack.append(action)
    print(f"VISITED: {action}")
  
  elif action == "BACK":
    if stack:
      stack.pop()
      if stack:
        print(f"BACK TO: {stack[-1]}")
      else:
        print("Back to home page IG")
    else:
      print("Can't go back lol :)")
  
  print("=============================================")
  return history

actions = ["gemini.com", "google.com", "BACK", "BACK", "BACK"]

for cmd in actions:
  print(f"Current history: {browser_history(cmd, history)}")
  print("\n")