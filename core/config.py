import sys,os
class Config:
    DefaultInterpreter = sys.executable
    Basename = "pycontextmenu"
    # base folder
    Plugins = "plugins"
    Template = "template"
    Icon = "icon"
    Cwd = os.getcwd();