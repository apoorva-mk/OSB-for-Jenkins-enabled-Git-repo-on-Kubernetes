from github import Github, GithubException

CREATION_SUCCESS = "Repository successfully created"
DELETION_SUCCESS = "Repository successfully deleted"
REPO_NOT_FOUND_FAILURE = "Repository not found"

def create_new_github_repo(repo_name, auth_token):
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
        return 201, created_repo, CREATION_SUCCESS
    except Exception as e:
        return e.status, e, e.data["message"]+e.data['errors'][0]["message"]



def delete_github_repo(auth_token, repo_name):
    """
        This method is used to delete an existing github repository
        PAT Token should have admin access for successful deletion

        Returns:
            status code, 
            outcome of deletion operation as a string
    """

    g = Github(auth_token)
    user = g.get_user()
    try:
        repo_to_be_deleted = user.get_repo(repo_name)
        try:
            repo_to_be_deleted.delete()
            return 202, DELETION_SUCCESS
        except Exception as e:
            return e.status, e.data["message"]
    except:
        return 404, REPO_NOT_FOUND_FAILURE
