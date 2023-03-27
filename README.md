Author : Israel Cortes Mayorga <br />
 Javanes Solutions <br />
 Version 1.0 <br />
 ## Requeriments: 
    Python version 3.8>
    install "requests" python module (via pip3)
    git -latest version
#
 # AUTOMATED SCRIPT TO UPDATE WEBHOOKS AT GITLAB PROJECTS (OPTIONAL MODULES TO LIST & ADD NEW HOOKS)
 This script works with a vars file named "vars.json" to get neccessary info and send the API requests, 
 please modify these vars with yours as the structure below: <br />
 ## Vars info:
       -listhook_api: Endpoint used to list the hooks in an specific project.
                     "https://gitms.bcpl.mx/api/v4/projects/$PROJECTID/hooks"       
       -edithook_api: Endpoint used to update or add hooks in an specific project.
                     "https://gitms.bcpl.mx/api/v4/projects/$PROJECTID/hooks/$HOOKID"
                        $PROJECTID = ID of the project to modify (int)
                        $HOOKID = ID of the webhook to be replaced (int)
       -gitlab_token: "PERSONAL ACCESS TOKEN (¿?)" 
       -hook_url: The updated webhook URL that will replace the previous one.
       -addhook_url: The new webhook URL to be added.
Once modified and saved the vars just run the command "python webhook.py" on your terminal to execute the script.<br />
