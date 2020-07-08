from github import Github, GithubException

SUCCESS = "Repository successfully created"

def create_new_repo(repo_name, auth_token):
    """
        This created a new repository and takes in Github PAT token for creation.
        
        Returns:
            the status code of the operation, 
            resultant class from the operation, 
            error/success messages
    """
    g = Github(auth_token)
    user = g.get_user()
    created_repo = ""
    try:
        created_repo = user.create_repo(repo_name)
        return 200, created_repo, SUCCESS
    except Exception as e:
        return e.status, e, e.data["message"]+e.data['errors'][0]["message"]
