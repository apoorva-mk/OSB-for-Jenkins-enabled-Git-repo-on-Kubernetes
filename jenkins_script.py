import jenkins
from github import Github

JENKINS_JOB_CREATION_SUCCESS = "Jenkins job successfully created"
JENKINS_JOB_CREATION_FAILURE = "Associated jenkins job couldn't be created"
JENKINS_JOB_DELETION_SUCCESS = "Jenkins job successfully deleted"
JENKINS_AUTH_FAILURE = "Unauthorised access to Jenkins server"


def create_new_jenkins_job(jenkins_host, username, password, job_name):
    """
        Creates a new jenkins job, associated with a github repository
        Returns:
            Status of the operation,
            Outcome of job creation operation 
    """
    server = jenkins.Jenkins(jenkins_host,username=username, password=password)

    """ Check of jenkins server is accessible """
    try:
        user = server.get_whoami()
    except:
        return 401, JENKINS_AUTH_FAILURE

    """ Create associated jenkins job """
    try:
        server.create_job(job_name, jenkins.EMPTY_CONFIG_XML)
        return 201, JENKINS_JOB_CREATION_SUCCESS
    except:
        return 400, JENKINS_JOB_CREATION_FAILURE


def delete_jenkins_job(jenkins_host, username, password, job_name):
    """
        This method is to delete a jenkins job on a server
        Returns:
            The HTTP status code, 
            relevant message of deletion operation
    """
    server = jenkins.Jenkins(jenkins_host,username=username, password=password)
    try:
        user = server.get_whoami()
    except:
        return 401, JENKINS_AUTH_FAILURE
    try:
        server.delete_job(job_name)
        return 201, JENKINS_JOB_DELETION_SUCCESS
    except:
        return 404, e+"(Jenkins job)"
    

def get_jenkins_job_name(auth_token, repo_name):
    """ 
        Create a unique name associated with the jenkins job, 
        something along the lines of "Slugs" used for webpages

        Returns:
            The name of the jenkins job to be created as a string
    """
    g = Github(auth_token)
    github_user_name = g.get_user().login
    job_name = github_user_name+"."+repo_name
    return job_name


""" Some tidbits of code (for authors reference -- kindly ignore)
    #TODO: Use API token instead of password
    server = jenkins.Jenkins('http://localhost:9090',username='apoorva', password='123456')
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))


    # Creating a job
    #server.create_job('empty2', jenkins.EMPTY_CONFIG_XML)
    jobs = server.get_jobs()
    for job in jobs:
        print(job)
        print("\n\n")
"""