import os

# Set up the alias with the current working directory
alias = f"\nalias FAT='python {os.getcwd()}/FAT'"

# Define the path to the user's .bashrc file
bashrc_path = os.path.expanduser("~/.bashrc")

try:
    # Append the alias to the .bashrc file
    with open(bashrc_path, 'a') as f:
      
        f.write(alias)
    print("\nSetup file executed successfully.\n"
          "Now you can use the tool by just typing 'FAT' in any directory.\n"
          "Please close and reopen the terminal to activate the alias.\n")
except Exception as e:
    print(f"Something went wrong: {e}\nPlease report the issue in our repo.")
