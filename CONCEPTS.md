1. # GIT Commands:
   1. Create a repo with your project name in Github
   2. Initialize Git in Your Project Folder
      3. Command : git init
   4. Add Remote Repository (GitHub, GitLab, etc.)
      5. Command : git remote add origin https://github.com/username/repo.git , this Links your local repo to the remote repo.
   6. Verify if the remote repo is set properly
      7. Command : git remote -v
   8. Stage Files (Add to Staging Area)
      9. Commands : git add filename.txt     # Add a single file
      10. Commands : git add .               # Add all files in the project 
   11. Commit Changes to Local Repository
       12. Command : git commit -m "Initial commit" # Saves the staged changes with a message.
   13. Push Changes to Remote
       14. First push (set upstream branch): Command : git push -u origin main
           (If your branch is master instead of main, replace accordingly.)
       15. Subsequent pushes:
           Command : git push
   16. Pull Updates from Remote
       17. Command : git pull (Keeps your local copy in sync with the remote.)
   18. Git Status Check 
       19. Command : git status (Shows which files are staged, unstaged, or untracked.)
   20. View Commit history
       21. Commands : git log (Complete info)
       22. Commands : git log --oneline    # Short version
   23. Create and Switch Branches
       24.  git branch new-branch         # Create new branch
            git checkout new-branch       # Switch to it
            git checkout -b new-branch    # Create + switch in one command
------------------------------------------------
2. # Configuration Management System (hybrid configuration management mechanism) :
   1. We can set up config.yaml and .env files and manage our configs
   2. Steps : 
   3. ## Config YAML file: 
      1. Create a folder like configs and create config.yaml and .env files under it, you can use any name but these are recommended
      2. In config.yaml , create sections like default or common, sit, preprod etc as per you test requirements and add all your
         required configs in each section.
   4.  ## .env file:
      1. In .env file, add your secrets like user name , password, keys etc
   5. ## Config Loader:
      1. Create another folder like utilities and create python file to load the configs i.e config_loader.py (can be any name).
      2. So, in config_loader.py , Create a class as **Config** and define a __init__ method to fetch the paths of .env and config.yaml files
      3. Now, define function for each config.yaml and .env data using python decorator @property (so you can call your configs just like attributes without () - example config.env_url)
   6. ## Hook (Pytest Hook) 
      1. Using pytest file -> conftest.py(mandatory naming) to inject the config values into tests
      2. Pytest auto-discovers the file, no need of any importing
      3. In the file, use pytest_addoption hook using which you can create a new CLI argument that help you to choose env while running, action to store input, default env if not passed and help option
      4. @pytest.fixture scope = session helps calling it only once per session , not for every test
      5. config function then fetches the input CLI input and creates a Config object with env data
   7. ## Fetching the config data into Tests
      1. In the actual Test , we mention the python function like test_***(config), so when this function gets called, using config function from conftest.py hook, the config data will be fetched.

3. # Logging : 
   1. Configure Logging : To log all your test activities , add pytest_configure hook in the conftest.py file
   2. Tell what to log : Add pytest.ini file under the project root , so your tests will log success, failure and warning etc
   3. Because by defauly, the logging works only for warning and above only, success will be suppressed 

4. # Freeze Requirements.txt
   1. Everytime you install a new package , remember to update the requirements file using below command : 
   2.  pip freeze > requirements.txt
   3. This can be automatically done , but for now try manual for learning
   
