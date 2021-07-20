<p align="center">
  <img src="https://img.shields.io/github/v/release/titomncl/odin?style=for-the-badge">
  <img src="https://img.shields.io/github/license/titomncl/odin?style=for-the-badge">
  <img src="https://img.shields.io/github/downloads/titomncl/odin/total?style=for-the-badge">
  <img src="https://img.shields.io/github/languages/code-size/titomncl/odin?style=for-the-badge">
  <img src="https://img.shields.io/github/issues-raw/titomncl/odin?color=red&style=for-the-badge">
</p>

![repository-open-graph-odin](https://user-images.githubusercontent.com/70750510/126334220-9b6ddcad-235f-4f32-8caf-1eb290605f85.png)

## How to install:
* Download the latest release
* Unzip the file
* Put the Odin folder wherever you want
* Run Odin.exe

## First use:
When running Odin for the first time, a file dialog while pop-up. You'll need to specify the root path that will contain the projects.
You are now able to create a new project.
Now your project is created, you can set your project. A new pop-up shows up to ask you the path to the folder that contains the scripts used by the DCCs.
> I recommend to have a directory that contains repositories with the names of your DCCs.
#### Example:
```yaml
- 📂 <dev-tools-folder>: the folder that contains the repositories
  - 📦 <project_name>: Root folder of the repository
    - 📂<project_name>: Package folder that contains your scripts
    - 📂docs: optional
    - 📄 .gitignore:
    - 📄 README.md: Documentation of your repository
```

### Change the software launch path:
You can change the software launch path if it's absolutely necessary.

**⚠️Be aware that any modification can result to unusable software launching feature⚠️**

* Go inside the Odin folder
* Inside the 'config' folder, open the file `software_config.yaml` with a text editor
* Replace the cwd and exe path:
> The cwd is the path folder that contain all the files needed for the software to work properly.
> The exe is the executable file path of the software.
###### Base:
```yaml
houdini:
  cwd: C:\Program Files\Side Effects Software\Houdini 18.5.596
  exe: C:\Program Files\Side Effects Software\Houdini 18.5.596\bin\houdini.exe
```
###### Edited:
```yaml
houdini:
  cwd: D:\DCC\Houdini\Houdini 18.0.432
  exe: D:\DCC\Houdini\Houdini 18.0.432\bin\houdini.exe
```
**Make sure you keep the indent for each line and the space between *cwd:* and the path**
