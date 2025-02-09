# Poetry Available Commands

---
## Essential Commands
**add :**
   Adds a new dependency to pyproject.toml and installs it.
   - poetry add <package>
   To add as a dev dependency:
   - poetry add <package> --dev

**build :** 
   Builds a package, as a tarball and a wheel by default.
   - poetry build

**config :** 
   Manages configuration settings.
   - poetry config
   To list all Poetry configurations.
   - poetry config --list

**init :**
   Creates a basic pyproject.toml file in the current directory.
   - poetry init

**install:**
   Installs the project dependencies.
   - poetry install

**new:**
   Creates a new Python project at <path>.
   - poetry new <project_name>

**remove :**
   Removes a package from the project dependencies.
   - poetry remove <package>

**run :**
   Runs a command in the appropriate environment.
   - poetry run <command>

**sync:**
   Update the project's environment according to the lockfile.
   - poetry lock && poetry install

---
## Other Commands:
**about :**
   Shows information about Poetry. 
   - poetry about

**check :**
   Validates the content of the pyproject.toml file and its consistency with the poetry.lock file
   - poetry check

**help :** 
   Displays help for a command.
   - poetry help
   For specific command help
   - poetry help <command>

**list :**
   Lists commands.
   - poetry list

**lock :**
   Locks the project dependencies.
   - poetry lock

**publish :**
   Publishes a package to a remote repository.
   - poetry publish

**update:**
   Update the dependencies as according to the pyproject.toml file.
   - poetry update

**version :**
   Shows the version of the project or bumps it when a valid bump rule is provided.
   - poetry version
   To update version 
   - poetry version <new_version>  

**search :**
   Searches for packages on remote repositories.
   - poetry search <package>

**show :**
   Shows information about packages.
   - poetry show
   To see all dependencies & their versions.
   - poetry show --tree

**self update :**
   Update Poetry itself to the latest version.
   - poetry self update

---
### Quick  Examples:

**1. Add a dependency:**   poetry add requests
**2. Remove a package:**   poetry remove numpy
**3. Update all dependencies:**  poetry update
**4. Build a package:**    poetry build
**5. Export dependencies:**poetry export -f requirements.txt --output requirements.txt
**6. Publish to PyPI :**   poetry publish --build