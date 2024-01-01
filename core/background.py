import winreg as Reg
import sys
from .config import Config

class ExtendsLoader:
    pass;

class Background:

    # register SubCommands

    def __init__(self,Basename:str=None) -> None:
        if Basename:
            self.Basename = Basename
        else:
            self.Basename = Config.Basename
            
        self.InstallPath = f"*\\shell\\{self.Basename}"

    def _is_installed(self) -> bool:
        return Background.keyExist(Reg.HKEY_CLASSES_ROOT,self.InstallPath);

    def installBySubCommands(self) -> bool:
        if self._is_installed():
            return False
        
    
    def _add_sub_key(self) -> bool:
        pass;

    @staticmethod
    def keyExist(keyType:int,keyPath:str) -> bool:
        try:
            key = Reg.OpenKey(keyType,keyPath);
            return True;
        except FileNotFoundError:
            return False;

    



    # 无限菜单：ExtendedSubCommandsKey 