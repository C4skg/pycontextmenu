from .background import Background

class SubTask:

    @staticmethod
    def _change(command:str) -> bool:
        # return type bool; 
        # it means the status has been changed
        Back = Background();
        status = Back._is_installed();
        if command == 'install':
            if status:
                return False;
            
            return Back.installBySubCommands()
        
        elif command == 'uninstall':
            pass;