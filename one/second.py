def requireAdmin(orgFunction):
    def wrapper(*args,**kwargs):
        print(f"Entering the admin checking process")
        user = kwargs.get('user') # forget 1
        if not user or user.get('role') != 'ADMIN':
            return f"Not Authorised to Execute: {kwargs.get('userId')}"
        else : print("Authorized to execute")

        return orgFunction(*args,**kwargs)   #forget 2 orgFuntion instead of orgFunction with () brackets  # forget 3 : args,kwargs in bracket
        #forget4 * astric signs
    return wrapper

@requireAdmin
def executeTask(userId,user):
    print("executing")
    return "Success"


user1 = {
    "name": "Humam", "role": "USER"
}
user2 = {
    "name": "Humam", "role": "ADMIN"
}

print(executeTask(userId=1,user=user1))
print(executeTask(userId=2,user=user2))

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/humamul/AI-Learning.git
git push -u origin main