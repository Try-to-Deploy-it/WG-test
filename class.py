import os.path
from git import *
import git, os, shutil

# create local Repo/Folder
UPLOAD_FOLDER = "F:\python\python_test"
#UPLOAD_FOLDER = input("enter folder path: ")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    print(UPLOAD_FOLDER)
new_path = os.path.join(UPLOAD_FOLDER)
DIR_NAME = new_path
REMOTE_URL = "https://github.com/Darth-Kordis/python_test.git"
#REMOTE_URL = input("enter remote url: ")
# REMOTE_URL looks "git@github.com:path of Repo"
# code for clone


class git_operations():
    try:
        def __init__(self):
            self.DIR_NAME = DIR_NAME
            self.REMOTE_URL = REMOTE_URL

#        def git_clone(self):

#            if os.path.isdir(DIR_NAME):
#                shutil.rmtree(DIR_NAME)
#            os.mkdir(DIR_NAME)
#            repo = git.Repo.init(DIR_NAME)
#            origin = repo.create_remote('origin', REMOTE_URL)
#            origin.fetch()
#            origin.pull(origin.refs[0].remote_head)

        def git_push(self):
          try:

            repo = Repo(DIR_NAME)
            commit_message = 'work in progress'
            # repo.index.add(u=True)
            repo.git.add('--all')
            repo.index.commit(commit_message)
            origin = repo.remote('origin')
            origin.push('master')
            repo.git.add(update=True)
            print("repo push succesfully")
          except Exception as e:
              print(str(e))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    a = git_operations()
    git_operations.git_push('')
    git_operations()
#    git_operations.git_clone('')