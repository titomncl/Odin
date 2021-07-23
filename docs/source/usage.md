# Usage

## First use

Before creating your first project, Odin need some information:
 - Path directory containing your projects
 - (Optional) Directory containing your scripts


When running Odin for the first time, a pop-up will ask you to specify a project path.

```{eval-rst}
.. note: You can cancel it, but another pop-up will ask you if you are sure to cancel.
```

Now the project path is set, you can create as many projects as you want.

You can specify a path to a directory that contain the scripts you want to use in the DCCs software.
If you work in a production, it may be set by the Pipeline-TD.

> I recommend having a directory that contains repositories with the names of your DCCs.

*Example:*
```yaml
- 📂 <dev-tools-folder>: the folder that contains the repositories
  - 📦 <project_name>: Root folder of the repository
    - 📂<project_name>: Package folder that contains your scripts
    - 📂docs: optional
    - 📄 .gitignore:
    - 📄 README.md: Documentation of your repository
```

```{eval-rst}
.. _change_config:
```

## Change the configuration

You can change the software launch path if it's absolutely necessary.

```{eval-rst}
.. warning:: Be aware that any modification can result to unusable software launching feature 
```

* Go inside the Odin folder
* Inside the 'config' folder, open the file `software_config.yaml` with a text editor
* Replace the cwd and exe path:
> The cwd is the path folder that contain all the files needed for the software to work properly.
> The exe is the executable file path of the software.

*Base:*
```yaml
houdini:
  cwd: C:\Program Files\Side Effects Software\Houdini 18.5.596
  exe: C:\Program Files\Side Effects Software\Houdini 18.5.596\bin\houdini.exe
```

*Edited:*
```yaml
houdini:
  cwd: D:\DCC\Houdini\Houdini 18.0.432
  exe: D:\DCC\Houdini\Houdini 18.0.432\bin\houdini.exe
```
```{eval-rst}
.. note:: Make sure you keep the indent for each line and the space between `cwd:` (or `exe:`) and the path 
```
