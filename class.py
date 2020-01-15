import os.path
#from git import *
import git, os, shutil

# create local Repo/Folder
if os.name == 'nt':
    UPLOAD_FOLDER = "%USERPROFILE%\Desktop\python1_test"
    #UPLOAD_FOLDER = "C:\python_test"
else:
    UPLOAD_FOLDER = "~/python1_test"

#if not os.path.exists(UPLOAD_FOLDER):
#    os.makedirs(UPLOAD_FOLDER)
#    print(UPLOAD_FOLDER)
new_path = os.path.join(UPLOAD_FOLDER)
DIR_NAME = new_path
REMOTE_URL = "https://github.com/Darth-Kordis/python_test.git"
NEW_BRANCH: str = 'another-new-one'

class git_operations():
    try:
        def __init__(self):
            self.DIR_NAME = DIR_NAME
            self.REMOTE_URL = REMOTE_URL
            self.NEW_BRANCH = NEW_BRANCH

        def git_clone(self):
            if not os.path.exists(DIR_NAME):
                if os.path.isdir(DIR_NAME):
                    shutil.rmtree(DIR_NAME)
                os.mkdir(DIR_NAME)
            print(DIR_NAME)
            print()
            if not os.listdir(DIR_NAME):
                repo = git.Repo.init(DIR_NAME)
                origin = repo.create_remote('origin', REMOTE_URL)
                origin.fetch()
                origin.pull(origin.refs[0].remote_head)
            print("repo cloned successfully")
            print()

        def git_branch(self):
            try:
                repo = git.Repo(DIR_NAME)
                if NEW_BRANCH not in repo.heads:
                    repo.git.branch(NEW_BRANCH)
                    print('branch "' + NEW_BRANCH + '" created successfully')
                else:
                    print('branch "' + NEW_BRANCH + '" is already exist')
                print("available branches:")
                print(repo.heads)
                print()
            except Exception as e:
                print(str(e))

        def git_checkout(self):
            try:
                repo = git.Repo(DIR_NAME)
                repo.git.checkout(NEW_BRANCH)
                branch = repo.active_branch
                print("active branch is: " + branch.name)
            except Exception as e:
                print(str(e))


        def git_commit(self):
            try:
                repo = git.Repo(DIR_NAME)
                commit_message = 'work in progress'
                repo.git.add('--all')
                repo.index.commit(commit_message)
            except Exception as e:
                print(str(e))

        def git_push(self):
            try:
                repo = git.Repo(DIR_NAME)
                origin = repo.remote('origin')
                branch = repo.active_branch
                origin.push(branch.name)
                repo.git.add(update=True)
                print("repo push successfully")
            except Exception as e:
                print(str(e))

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    git_operations()
    git_operations.git_clone('')
    git_operations.git_branch('')
    git_operations.git_checkout('')
    git_operations.git_commit('')
    git_operations.git_push('')