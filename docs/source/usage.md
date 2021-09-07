# Usage

## First use

Before creating your first project, Odin needs some information:
 - A path to the directory that will contain your projects
 - (Optional) A directory that contain the scripts for the DCCs


When running Odin for the first time, a pop-up will ask you to specify a project path.

```{eval-rst}
.. note: You can cancel it, but another pop-up will ask you if you are sure to cancel.
```

Now the project path is specified, you can create as many projects as you want.

## Update Odin
If an update is available, a message box will show up asking you if you want to download the new version of Odin.
You can abort the update and say the software you don't want to be reminded about future updates.

You can tell Odin to check about new beta updates by checking the option in the `Update` tab.

> The preferences are in `odin/config/config_file.yaml` file created at the first use of Odin. 

## Tools for DCCs

Odin is capable of loading an environment for each DCCs that support Python scripting.
These scripts can be downloaded or created. For both of these situations, I recommend you to have a repository that 
follows the example bellow:

*Example:*
```yaml
- 📂 <dev-tools-folder>: the folder that contains the repositories
  - 📦 <project_name>: Root folder of the repository
    - 📂<project_name>: Package folder that contains your scripts
      - __init__.py: Required file
      - <your_file>.py: Python script that should follow PEP8, black and flake8 conformations
    - 📂docs: optional
    - 📄 .gitignore:
    - 📄 README.md: Documentation of your repository
```

To specify the tools' path containing the repositories, you need to open Odin. 
Go into the `Config` tab, click on `Set tools path...` and specify the folder that contains your tools.

```{eval-rst}
.. tip:: If you work in a production, the configuration should be set by the dev department.
```

```{eval-rst}
.. _change_config:
```

## Change configuration

Odin provide a configuration file containing the path of each software it can launch.

Here is the list:

* Maya 2019
* ZBrush 2020.1.1 FL
* Houdini 18.5.596
* Substance Designer & Painter (Allegorithmic)
* Mari 4.6v3
* Photoshop 2021
* NukeX 12.2v4
* Guerilla Render
* Resolve

Some software has its version in the path. You can change it to follow the version you have on your computer by editing
the `software_config.yaml` file.

```{eval-rst}
.. warning:: Be aware that any modification can result to unusable software launching feature 
```

To do so:
* Go inside the Odin folder
* In `odin/config`, open the file `software_config.yaml` with a text editor (Notepad++ preferably)
* Replace the cwd and exe path by seeing the example bellow

```{eval-rst}
.. tip:: The cwd is the path folder that contain all the files needed for the software to work properly.
        The exe is the executable file path of the software. 
```

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

## Tree overview

```yaml
<PROJECT_NAME>:
  IN:
    PREPROD:
      STORYBOARD:
      DESIGN:
      SCENARIO:
      REFS:
    FILMING:
      CONFO:
        EXR:
        PROXY:
      DOCS:
      PHOTOS:
        HDRI:
        MAKING_OF:
      RUSH:
        PREVIZ:
        <DAY##>:
  DATA:
    FILM:
      EDITING:
        VERSION:
          <PROJECT_NAME>_EDIT_<VERSION>.<ext>
        PUBLISH:
          <PROJECT_NAME>_EDIT.<ext>
      SEQ:
        <S###>:
          <P###>:
            ANIMATION:
              VERSION:
                <S###P###>_ANIM_<VERSION>.<ext>
              PUBLISH:
                <S###P###>_ANIM.<ext>
            LIGHTING:
              VERSION:
                <S###P###>_LIGHTING_<VERSION>.<ext>
              PUBLISH:
                <S###P###>_LIGHTING.<ext>
            COMPOSITING:
              CACHE:
              VERSION:
                <S###P###>_COMPO_<VERSION>.<ext>
              PUBLISH:
                <S###P###>_COMPO.<ext>
            FX:
              CACHE:
                <S###P###>_FX_CACHE.<ext>
              VERSION:
                <S###P###>_FX_<VERSION>.<ext>
              PUBLISH:
                <S###P###>_FX.<ext>
          PREVIZ:
            SCENES:
              VERSION:
                <S###P###>_PREVIZ.<ext>
            MEDIA:
    LIB:
      PUBLISH:
        SET:
          <SET_NAME>:
            MOD:
              HD:
                <SET_NAME>_HD.obj
              LD:
                <SET_NAME>_LD.obj
            SHD:
              <SET_NAME>_<LAYER>_<COLORSPACE>.exr
        FX:
          <FX_NAME>:
            <FX_NAME>.<ext>
        CHARA:
          <CHARA_NAME>:
            MOD:
              HD:
                <CHARA_NAME>_HD.obj
              LD:
                <CHARA_NAME>_LD.obj
            SHD:
              <CHARA_NAME>_<LAYER>_<COLORSPACE.exr
            RIG:
              <CHARA_NAME>_RIG.ma
        PROPS:
          <PROPS_NAME>:
            MOD:
              HD:
                <PROPS_NAME>_HD.obj
              LD:
                <PROPS_NAME>_LD.obj
            SHD:
              <PROPS_NAME>_<LAYER>_<COLORSPACE>.exr
            RIG:
              <PROPS_NAME>_RIG.ma
      SET:
        <SET_NAME>:
          MOD:
            SCENE:
              VERSION:
                <SET_NAME>_SET_<VERSION>.<ext>
              PUBLISH:
                <SET_NAME>_SET.<ext>
          SHD:
            TEXTURES:
              VERSION:
                <VERSION>:
                  <SET_NAME>_<LAYER>_<COLORSPACE>.<ext>
              PUBLISH:
                <SET_NAME>_<LAYER>_<COLORSPACE>.<ext>
            SCENE:
              VERSION:
                <SET_NAME>_SHD_<VERSION>.<ext>
              PUBLISH:
                <SET_NAME>_SHD.<ext>
      FX:
        <FX_NAME>:
          CACHEFILES:
            <FX_NAME>.<ext>
          SCENES:
            VERSION:
              <FX_NAME>_FX_<VERSION>.<ext>
            PUBLISH:
              <FX_NAME>_FX.<ext>
      CHARA:
        <CHARA_NAME>:
          MOD:
            SCENE:
              VERSION:
                <CHARA_NAME>_MOD_<VERSION>.<ext>
              PUBLISH:
                <CHARA_NAME>_MOD.<ext>
          SHD:
            TEXTURES:
              VERSION:
                <VERSION>:
                  <CHARA_NAME>_<LAYER>_<COLORSPACE>.<ext>
              PUBLISH:
                <CHARA_NAME>_<LAYER>_<COLORSPACE>.<ext>
            SCENE:
              VERSION:
                <CHARA_NAME>_SHD_<VERSION>.<ext>
              PUBLISH:
                <CHARA_NAME>_SHD.<ext>
          RIG:
            SCENE:
              VERSION:
                <CHARA_NAME>_RIG_<VERSION>.ma
              PUBLISH:
                <CHARA_NAME>_RIG.ma
      PROPS:
        <PROPS_NAME>:
          MOD:
            SCENE:
              VERSION:
                <PROPS_NAME>_MOD_<VERSION>.<ext>
              PUBLISH:
                <PROPS_NAME>_MOD.<ext>
          SHD:
            TEXTURES:
              VERSION:
                <VERSION>:
                  <PROPS_NAME>_<LAYER>_<COLORSPACE>.<ext>
              PUBLISH:
                <PROPS_NAME>_<LAYER>_<COLORSPACE>.<ext>
            SCENE:
              VERSION:
                <PROPS_NAME>_SHD_<VERSION>.<ext>
              PUBLISH:
                <PROPS_NAME>_SHD.<ext>
          RIG:
            SCENE:
              VERSION:
                <PROPS_NAME>_RIG_<VERSION>.ma
              PUBLISH:
                <PROPS_NAME>_RIG.ma
  OUT:
    SEQ:
      <S###>:
        <P###>:
          ANIMATION:
            <S###P###>_ANIM.abc
          LIGHTING:
            <S###P###>_LIGHTING.exr
          COMPOSITING:
            <S###P###>_COMPO.exr
          FX:
            <S###P###>_FX.<ext>
    AUDIO:
      VERSION:
        <PROJECT_NAME>_AUDIO_<VERSION>.<ext>
      PUBLISH:
        <PROJECT_NAME>_AUDIO.<ext>
    EDITING:
      VERSION:
        <PROJECT_NAME>_EDIT_<VERSION>.<ext>
      PUBLISH:
        <PROJECT_NAME>_EDIT.<ext>
    DAILIES:
    COMMUNICATION:
      PACKAGE_1:
      PACKAGE_2:
      PACKAGE_3:
      PACKAGE_4:
      PACKAGE_5:
  TMP:
```
