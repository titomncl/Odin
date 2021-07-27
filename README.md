<p align="center">
  <img src="https://img.shields.io/github/v/release/titomncl/odin?include_prereleases&style=for-the-badge">
  <img src="https://img.shields.io/github/license/titomncl/odin?style=for-the-badge">
  <img src="https://img.shields.io/github/downloads/titomncl/odin/total?style=for-the-badge">
  <img src="https://img.shields.io/github/languages/code-size/titomncl/odin?style=for-the-badge">
  <img src="https://img.shields.io/github/issues-raw/titomncl/odin?color=red&style=for-the-badge">
</p>

![repository-open-graph-odin](https://user-images.githubusercontent.com/70750510/126334220-9b6ddcad-235f-4f32-8caf-1eb290605f85.png)

## Introduction

Odin is a project manager for 3D production.
It can be used by freelance artist or school project.

It allows the user to:
- Create a project:
    - Add assets:
        + Characters
        + Props/Static
        + Sets/Environment
        + FX
    - Add sequences
    - Add shots relatives to a sequence
- Choose an existing project
- Run multiple software with a python environment


## Installation
* Download the latest release
* Unzip the file
* Put the Odin folder wherever you want
* Run `Odin.exe`

## First use

Before creating your first project, Odin need some information:
 - Path directory containing your projects
 - (Optional) Directory containing your scripts

| ℹ Note: You can cancel it, but another pop-up will ask you if you are sure to cancel. ℹ|
|---|


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

### Change the configuration
You can change the software launch path if it's absolutely necessary.

| ⚠️Be aware that any modification can result to unusable software launching feature⚠️|
|---|

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

| ℹ Make sure you keep the indent for each line and the space between `cwd:` (or `exe:`) and the path ℹ |
|---|
