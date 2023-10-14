import requests

# Replace with your GitHub username and personal access token
username = "ahmed-2001M"
token = "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"

# Create a new repository on GitHub
repo_name = "test55"
repo_description = "Your repository description"
headers = {
    "Authorization": f"token {token}",
}
data = {
    "name": repo_name,
    "description": repo_description,
    "auto_init": True,  # Initialize with a README.md
}
repo_create_url = f"https://api.github.com/user/repos"
response = requests.post(repo_create_url, headers=headers, json=data)

if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully on GitHub.")
else:
    print(f"Failed to create repository. Status code: {response.status_code}")
    print(response.json())  # Print the response content for more details
    exit()


# Clone the newly created repository
repo_clone_url = f"https://github.com/{username}/{repo_name}.git"
clone_command = f"git clone {repo_clone_url}"
import subprocess

subprocess.run(clone_command, shell=True)

# Create a README.md file
with open(f"{repo_name}/README.md", "w") as readme_file:
    readme_file.write("# Welcome to My Repository!\n\nThis is the README.md file for your new repository.")

# Commit and push the README.md file
commit_message = "Initial commit: Add README.md"
add_command = "git add ."
commit_command = f'git commit -m "{commit_message}"'
push_command = "git push origin main"  # You might need to adjust the branch name

subprocess.run(add_command, shell=True, cwd=repo_name)
subprocess.run(commit_command, shell=True, cwd=repo_name)
subprocess.run(push_command, shell=True, cwd=repo_name)

print("README.md file created and pushed to the repository.")





# import requests

# # Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual token
# token = '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'
# headers = {
#     'Authorization': f'token {token}',
# }

# response = requests.get('https://api.github.com/user/repos', headers=headers)

# if response.status_code == 200:
#     # You can now work with the list of repositories in the response JSON.
#     repositories = response.json()
#     for repo in repositories:
#         print(repo['name'])
# else:
#     print('Failed to fetch repositories. Status code:', response.status_code)
