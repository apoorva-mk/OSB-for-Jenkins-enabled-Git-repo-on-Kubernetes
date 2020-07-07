import jenkins


# TODO: Use API token instead of password
server = jenkins.Jenkins('http://localhost:8080',
                         username='Apoorva', password='123456')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


# Creating a job
server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)
