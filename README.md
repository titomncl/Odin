<p align="center">
  <img src="https://img.shields.io/github/v/release/titomncl/odin?style=flat-square">
  <img src='https://readthedocs.org/projects/odin-project-manager/badge/?version=latest&style=flat-square' alt='Documentation Status' />
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square">
  <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336">
  <img src="https://img.shields.io/github/license/titomncl/odin?style=flat-square">
  <img src="https://img.shields.io/github/downloads/titomncl/odin/total?style=flat-square">
  <img src="https://img.shields.io/github/languages/code-size/titomncl/odin?style=flat-square">
  <img src="https://img.shields.io/github/issues-raw/titomncl/odin?color=red&style=flat-square">
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


Now the project path is specified, you can create as many projects as you want.


### Update Odin
If an update is available, a message box will show up telling you if you want to download the new version of Odin.
You can abort the update and say the soft you don't want to be reminded about future updates.

You can tell Odin to check about new beta updates by checking the option in the `Update` tab.
 

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
