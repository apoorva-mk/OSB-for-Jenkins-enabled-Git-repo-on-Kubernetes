from github import Github

EVENTS = ["push", "pull_request"]
WEBHOOK_SUCCESS = "Web hook successfully added"
WEBHOOK_FAILURE = "Couldn't create webhook for the given repository"
REPOSITORY_FAILURE = "Error while accessing repository"

def create_webhook(auth_token, repo_name, webhook_url, endpoint):
    """ 
        Programmatically creates a web hook for a specified repository by the user.
        Send only the URL and not the protocol, right now this workd with HTTPS only
        Currently enabling triggers for only events specified in EVENTS
        Returns:
            Result of the operation as a string
    """

    config = {
        "url": "https://{host}/{endpoint}/".format(host=webhook_url, endpoint=endpoint),
        "content_type": "json"
    }

    g = Github(auth_token)
    user = g.get_user()
    try:
        repo = g.get_repo("{owner}/{repo_name}".format(owner=user.login, repo_name=repo_name))
        try:
            repo.create_hook("web", config, EVENTS, active=True)
            return True, WEBHOOK_SUCCESS
        except:
            return False, WEBHOOK_FAILURE
    except Exception as e:
        return False, REPOSITORY_FAILURE
        