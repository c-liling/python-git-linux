# importing os module
import os

# Command to execute
# Using WSL OS command
repo_name = input("Please key in the Git Repository Name: ")
os.mkdir(f"{repo_name}")
os.chdir(f"{repo_name}")
os.system(f"git init")
create_file = input("Please input your file name and extension: ")
os.system(f"touch {create_file}")
os.system(f"git add .")
message = input("Please key in the message you will like to display: ")
os.system(f"git commit -m '{message}'")
os.system(f"git log")