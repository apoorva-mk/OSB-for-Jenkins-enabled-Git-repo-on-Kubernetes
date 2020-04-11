import os


repo_name = "test"


# Make the git directory
if os.system('mkdir '+repo_name) == 0:
    os.chdir(repo_name)

    # Initialize a new bare repo
    os.system('git init')
    os.system('touch Jenkinsfile')


else:
    print("Repo already exists")
