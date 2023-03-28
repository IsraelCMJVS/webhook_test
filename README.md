Autor : Israel Cortes Mayorga <br />
Javanes Solutions <br />
Version 1.0 <br />
 ## Requisitos: 
    Python version 3.8 o superior
    instalar modulo "requests" de python (via pip3)
    git -ultima version
#
 # SCRIPT PARA ACTUALIZAR LOS WEBHOOKS EN PROYECTOS DE GITLAB
 CUENTA CON MODULOS OPCIONALES PARA ENLISTAR Y AGREGAR NUEVOS HOOKS (COMENTADOS) <br />
 Este script hace peticiones a la API de Gitlab para obtener informacion acerca de los webhooks almacenados en los proyectos <br /> 
 Trabaja mediate un archivo de variables tipo json llamado "vars.json" donde obtiene los datos para hacer las peticione. <br /> 
 Se debe modificar estas variables como se muestra a continuación: <br />
 ## Vars info:
       -listhook_api: Endpoint para obtener una lista de los hooks en un proyecto. Este mismo funciona para agregar nuevos hooks.
                     "https://gitms.bcpl.mx/api/v4/projects/$PROJECTID/hooks"
                        $PROJECTID = ID del proyecto a consultar.       
       -edithook_api: Endpoint para actualizar un hook existente por otro.
                     "https://gitms.bcpl.mx/api/v4/projects/$PROJECTID/hooks/$HOOKID"
                        $PROJECTID = ID del proyecto a modificar.
                        $HOOKID = ID del webhook que sera reemplazado (si no se tiene, se puede consultar con el modulo LISTHOOK)
       -gitlab_token: "PERSONAL ACCESS TOKEN DE GITLAB" 
       -hook_url: La URL del webhook que reemplazara al anterior.
       -addhook_url: La URL del webhook que sera agregado como nuevo.
Una vez modificado el archivo de variables, ejecutar el comando "python webhook.py" para correr el script. <br />
