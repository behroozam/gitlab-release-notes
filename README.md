# GitLab Release-Notes checker 

The giltab release-notes checker is a simple cli for gitlab-ci to prevent deploy project without release-notes.

### How Release-Notes checker works

The giltab release-notes checker gets enviroment variabeles and configs from `config.py`.
in `config.py` we have `PRIVATE_TOKEN` and `GITLAB_URL` that most set by user in `config.py`.
`CI_PROJECT_ID` and `CI_COMMIT_TAG` is sets automaticly by gitlab-runner to enviroment varibale.

giltab release-notes checks current tag in gitlab-runner match with the tag in release page and  print release notes to pipline output. 

### installation 

get your `PRIVATE_TOKEN` from your gitlab personal access token page 

``` pip3 install -r requirements.txt ```

``` mv config.py.example config.py``` 

change values of config.py 

``` python3 release-notes.py ```

### how to use 

clone the project in your /opt gitlab-runner linux directory  

``` cd /opt && git clone https://github.com/behroozam/gitlab-release-notes ```

link the project to /usr/bin/

``` ln -s /opt/release-note/release-notes.py /usr/bin/release-notes ```

and finaly using `.gitlab-ci.yaml` example in repository. 

### In The End
if you using this tool please consider giving it a star! ⭐
