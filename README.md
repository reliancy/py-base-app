Reliancy Base App Template for Python
==============================

This is reliancy base app template for python. It reflects a structure which has been proven over time.

A python project folder must allow us to document, develop and test our code with ease. 
It also needs to fit nicely in the ecosystem of github and visual studio code.

Immediately after cloining this project you should run python -m venv .venv inside the folder to create a virtual environment
specific to this project. Thereafter issue source .venv/Scripts/activate to activate virtual environment. As shell we recommend Bash such as git bash and we shall reference commands and paths that work with bash. Check Makefile and manage.py for possible implemeation of these init steps as an init or deps task.



Structure
--------
<pre>
root  - working directory of the project
  ├── /src/ - code sources including entrypoint and modules
  ├── /doc/ - documentation
  ├── /var/ - variable or runtime data
  ├── /test/ - test facility and good entry point for development
  ├── .gitignore - files and patterns not to be included in git repo
  ├── LICENCE.txt - licence info for completeness
  ├── requirements.txt - file with list of python dependencies via pip3 freeze > requirements.txt
  ├── README.md - markdown file to describe the project and how to apply it
  ├── setup.py - needed to publish to pypy repository
  ├── manage.py - used to manage project, not so much as runtime entry point which should be in src
  └── Makefile recipe for tasks such as build, deps, install etc.
  </pre>

  ### Code Sources
  Source folder should include entry point and various modules. The entry point or just before it is called should set up search path so that relative includes can find modules in src or build or dist or lib folder wherever they might be deployed in final build step. For python that is probably src folder.

  ### Documentation 
  Documentaton folder is there for API documentation, user manuals etc.
    
  ### Setup Folder
  Often but not always you might need a setup folder for things like Dockerfile recipes. 

  ### Log Folder
  Often but not always you might need a log folder. Not always because in dockerized environments you leave it up to docker to manage stdout/stderr logging. 
  
  ### Configuration Folder
  Soon after you try anything more serious you will find that you need a folder where parameters and configurations are saved. You will often need different settings for development and for production and for testing. This folder is not with sources because in cases your sources are built and deposited as libraries and executables.

  ### Runtime Data Folder
  Soon after you try anything more serious you will find that you need a folder where results are saved, even if temporarily. This folder should not go into git repository and often must be initialized for first run.

  Inside your code please look out for following main folders:
  * conf folder
  * data folder which is often same as 
  * work folder
  * base folder which is the root of the project
  
  You will save yourself a lot of trouble by defining these folders early in your code.

  ### Makefile
  You might have a laungage specific build system but do not underestimate the power of good old make. Thru Makefile you can encode often executed tasks and make your life easier. If for example manage.py implemnts various verbs/action over your project then thru Makefile you can composite these verbs into meaninful sentences.

  
