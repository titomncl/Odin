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

## Change configuration

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

## Tree overview

```yaml
PROJECT_NAME:
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
        DAY#:
  DATA:
    FILM:
      EDITING:
        VERSION:
          <PROJECT_NAME>_EDIT_<VERSION>.ext
        PUBLISH:
          <PROJECT_NAME>_EDIT.ext
      <S###>:
        <P###>:
          ANIMATION:
            VERSION:
              <S###P###>_ANIM_<VERSION>.ext
            PUBLISH:
              <S###P###>_ANIM.ext
          LIGHTING:
            VERSION:
              <S###P###>_LIGHTING_<VERSION>.ext
            PUBLISH:
              <S###P###>_LIGHTING.ext
          COMPOSITING:
            CACHE:
            VERSION:
              <S###P###>_COMPO_<VERSION>.ext
            PUBLISH:
              <S###P###>_COMPO.ext
          FX:
            CACHE:
              <S###P###>_FX_CACHE.vdb
              <S###P###>_FX_CACHE.abc
              <S###P###>_FX_CACHE.bgeo.sc
            VERSION:
              <S###P###>_FX_<VERSION>.ext
            PUBLISH:
              <S###P###>_FX.ext
        PREVIZ:
          SCENES:
            VERSION:
          SOURCEIMAGES:
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
            <FX_NAME>.vdb
            <FX_NAME>.abc
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
                <SET_NAME>_SET_<VERSION>.hip
              PUBLISH:
                <SET_NAME>_SET.hip
          SHD:
            TEXTURES:
              VERSION:
                <VERSION>:
                  <SET_NAME>_<LAYER>_<COLORSPACE>.exr
              PUBLISH:
                <SET_NAME>_<LAYER>_<COLORSPACE>.exr
            SCENE:
              VERSION:
                <SET_NAME>_SHD_<VERSION>.spp
                <SET_NAME>_SHD_<VERSION>.sbs
                <SET_NAME>_SHD_<VERSION>.mra
              PUBLISH:
                <SET_NAME>_SHD.spp
                <SET_NAME>_SHD.sbs
                <SET_NAME>_SHD.mra
      FX:
        <FX_NAME>:
          CACHEFILES:
            <FX_NAME>.vdb
            <FX_NAME>.abc
            <FX_NAME>.bgeo.sc
          SCENES:
            VERSION:
              <FX_NAME>_FX_<VERSION>.hip
            PUBLISH:
              <FX_NAME>_FX.hip
      CHARA:
        <CHARA_NAME>:
          MOD:
            SCENE:
              VERSION:
                <CHARA_NAME>_MOD_<VERSION>.ma
                <CHARA_NAME>_MOD_<VERSION>.ztl
              PUBLISH:
                <CHARA_NAME>_MOD.ma
                <CHARA_NAME>_MOD.ztl
          SHD:
            TEXTURES:
              VERSION:
                <VERSION>:
                  <CHARA_NAME>_<LAYER>_<COLORSPACE>.exr
              PUBLISH:
                <CHARA_NAME>_<LAYER>_<COLORSPACE>.exr
            SCENE:
              VERSION:
                <CHARA_NAME>_SHD_<VERSION>.spp
                <CHARA_NAME>_SHD_<VERSION>.sbs
                <CHARA_NAME>_SHD_<VERSION>.mra
              PUBLISH:
                <CHARA_NAME>_SHD.spp
                <CHARA_NAME>_SHD.sbs
                <CHARA_NAME>_SHD.mra
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
                <PROPS_NAME>_MOD_<VERSION>.ma
                <PROPS_NAME>_MOD_<VERSION>.ztl
              PUBLISH:
                <PROPS_NAME>_MOD.ma
                <PROPS_NAME>_MOD.ztl
            SHD:
              TEXTURES:
                VERSION:
                  <VERSION>:
                    <PROPS_NAME>_<LAYER>_<COLORSPACE>.exr
                PUBLISH:
                  <PROPS_NAME>_<LAYER>_<COLORSPACE>.exr
              SCENE:
                VERSION:
                  <PROPS_NAME>_SHD_<VERSION>.spp
                  <PROPS_NAME>_SHD_<VERSION>.sbs
                  <PROPS_NAME>_SHD_<VERSION>.mra
                PUBLISH:
                  <PROPS_NAME>_SHD.spp
                  <PROPS_NAME>_SHD.sbs
                  <PROPS_NAME>_SHD.mra
            RIG:
              SCENE:
                VERSION:
                  <PROPS_NAME>_RIG_<VERSION>.ma
                PUBLISH:
                  <PROPS_NAME>_RIG.ma
  OUT:
    <S###>:
      <P###>:
        ANIMATION:
          <S###P###>_ANIM.abc
        LIGHTING:
          <S###P###>_LIGHTING.exr
        COMPOSITING:
          <S###P###>_COMPO.exr
        FX:
          <S###P###>_FX.vdb
          <S###P###>_FX.abc
    EDITING:
      VERSION:
        <PROJECT_NAME>_EDIT_<VERSION>.mp4
      PUBLISH:
        <PROJECT_NAME>_EDIT.mp4
    DAILIES:
    COMMUNICATION:
      PACKAGE_1:
      PACKAGE_2:
      PACKAGE_3:
      PACKAGE_4:
      PACKAGE_5:
  TMP:
```
