from github import Github
import base64
from github import Auth
from openai import OpenAI
try:
    auth = Auth.Token("github api key")
    g = Github(auth=auth)

    repo=g.get_repo("username/repository name") 
    # username/repository which needs to be accessed

    file_content=repo.get_contents("file name")
    # file name (inside the repo which needs to be analysed)

    decoded=base64.b64decode(file_content.content)
    code_snippet=decoded.decode('utf-8')
    # recieved contents of the file now use this with chatgpt for suggestions

    try:
        client = OpenAI(api_key="openai api key")

        messages = [
            {"role": "system", "content": "I assist in improving code quality, efficiency (especially time complexity), debugging, and always offer test cases for comprehensive code validation and testing."},
        ]

        while True:
            message = input("User Inputs (optional) : ")
            message=message+code_snippet

            if message:
                messages.append(
                    {"role": "user", "content": message},
                )

                stream = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=messages, 
                stream=True,
                )

                # printing
                for part in stream:
                    print(part.choices[0].delta.content or "", end=" ")

            print("\n",end="\n")

            x=input("type BREAK to end the session ")
            if(x.lower()=="break"):
                break

        # To close connections after use
        g.close()

    except Exception as openai_exception:
        print(f"OpenAI Exception: {openai_exception}")

except Exception as github_exception:
    print(f"GitHub Exception: {github_exception}")


