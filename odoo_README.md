# Build docker image using docker-compose
1. cd into project root
2. Run command `$ chmod +x odoo-docker/entrypoint.sh odoo-docker/wait-for-it.sh`
3. Run command `$ docker-compose build --no-cache`
    * [OPTIONAL] For custom build args: `$ docker-compose build --no-cache --build-arg APT_MIRROR=http://ubuntu.ntc.net.np`
4. Run command `$ ./bin/odoo start -i base -d odoo`

## \# Build docker image
1. cd into **odoo-docker** directory `$ cd odoo-docker`
2. Run command `$ chmod +x entrypoint.sh wait-for-it.sh`
3. Run command `$ docker build -t odoo_12:12.20191001 --no-cache --network host  --build-arg APT_MIRROR=http://ubuntu.ntc.net.np .`


## \# Debug using Visual Studio Code
1. cd into project
2. Run command `$ ./bin/odoo start --debug`
3. Open project in VSCode `$ code .`
4. Add following configuration to `.vscode/launch.json`

```json
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Remote Attach",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "172.17.0.1",
                "justMyCode": false,
                "pathMappings": [
                    {
                      "localRoot": "${workspaceFolder}/.vscode/odoo/odoo",
                      "remoteRoot": "/usr/lib/python3/dist-packages/odoo"
                    },
                    {
                      "localRoot": "${workspaceFolder}/addons",
                      "remoteRoot": "/mnt/extra-addons"
                    }
                ]
            }
        ]
    }
```
5. Download same version and relase of odoo as defined in docker image (ie. Dockerfile) from [nightly.odoo.com](http://nightly.odoo.com/) and extract it to `.vscode/odoo`

  `$ mkdir -p .vscode/odoo && wget -qO - "http://nightly.odoo.com/12.0/nightly/src/odoo_12.0.20191001.tar.gz" | tar -xvz -C .vscode/odoo --strip-components=1`

6. Open debug activity in VSCode `Ctrl + Shift + D`
7. From debug options choose `Python: Remote Attach` and hit `f5` function key from keybaord
8. To add break points in odoo source files:
    * Open search activity in VSCode `Ctrl + Shift + F`
    * Type search keywords
    * Type `.vscode` in `files to include` section. (Click at three dots ...[Toggle Search Detail] at right if this field not visible)
    * Choose file and add break points

## \# CLI Commands

* `$ ./bin/odoo start`
* `$ ./bin/odoo start --debug`
* `$ ./bin/odoo start --production`
* `$ ./bin/odoo start -u <module1,module2> -d <dbname>`
* `$ ./bin/odoo shell <dbname>`
* `$ ./bin/odoo login [-u <root|odoo>]`
* `$ ./bin/odoo backup <dbname> [/backup-directory-path]`
* `$ ./bin/odoo upgrade <dbname> addon1 [addons/addon2] [addons/addon3,addon4]`

## \# Deployment
* checkout to `dev` , `uat` or `production` branch and push
