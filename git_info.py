import subprocess # import the subprocess module
import os # import the os module

def git_info(git_dir):
    try:
        os.chdir(git_dir) # change the working directory to the git repository directory
    except FileNotFoundError:
        print("The specified path does not exist. Please enter a valid path to your local git repository.")
        return

    active_branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True).stdout.strip().decode()
    # Run the git command to get the name of the active branch and store it in the variable active_branch.
    # The "capture_output=True" option captures the output of the command and stores it in the "stdout" attribute of the returned object.
    # The .strip() method is used to remove any leading or trailing white spaces.
    # The .decode() method is used to convert the output from bytes to a string.

    modified = subprocess.run(["git", "status", "--porcelain"], capture_output=True).stdout.strip().decode()
    # Run the git command to check if there are any modified files in the repository and store the result in the variable modified.
    # The "--porcelain" option is used to make the output of the command machine-readable.
    last_week = subprocess.run(["git", "log", "-1", "--since='1 week ago'", "--pretty=format:'%cd'", "--date=local"], capture_output=True).stdout.strip().decode()
    # Run the git command to check the date of the latest commit and store it in the variable last_week
    # The "-1" option is used to limit the number of commits to 1
    # The "--since='1 week ago'" option is used to limit the commits to those made in the last week
    # The "--pretty=format:'%cd'" option is used to format the output to show only the commit date
    # The "--date=local" option is used to show the date in the local time zone

    Rufus = subprocess.run(["git", "log", "-1", "--pretty=format:'%an'"], capture_output=True).stdout.strip().decode()
    # Run the git command to check the author of the latest commit and store it in the variable Rufus
    # The "-1" option is used to limit the number of commits to 1
    # The "--pretty=format:'%an'" option is used to format the output to show only the author's name
    
    print(f"active branch: {bool(active_branch)}")
    # Print the boolean value of whether the repository is on an active branch or not.
    # If active_branch is not an empty string, it means the repository is on an active branch, so the value is True, else False.
    
    print(f"local changes: {bool(modified)}")
    # Print the boolean value of whether there are any local changes in the repository or not.
    # If modified is not an empty string, it means there are local changes, so the value is True, else False.
    
    print(f"recent commit: {bool(last_week)}")
    # Print the boolean value of whether the repository has a commit in the last week or not.
    # If last_week is not an empty string, it means there is a recent commit, so the value is True, else False.
    
    print(f"blame Rufus: {Rufus == 'Rufus'}")
    # Print the boolean value of whether the repository's recent commit was authored by Rufus or not.
    # If Rufus is equal to 'Rufus', it means the recent commit was authored by Rufus, so the value is True, else False.

git_info("path_to_your_local_git_repo")
