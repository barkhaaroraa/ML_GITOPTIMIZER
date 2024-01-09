import requests
from github import Github
import base64


from github import Auth

auth = Auth.Token("token")

g = Github(auth=auth)
user=g.get_user()
print(user.login)

repo=g.get_repo("barkhaaroraa/java_oops")
contents=repo.get_contents("")
for content in contents:
    print(content.name)

file_content=repo.get_contents("Simple3.java")
decoded=base64.b64decode(file_content.content)
print(decoded.decode('utf-8'))
# To close connections after use
g.close()