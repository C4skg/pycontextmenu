class ScriptLoader:
    @staticmethod
    def loader(**kwargs) -> bool:
        '''
        在这里实现你需要的功能
        '''
        ScriptLoader.myFunction(kwargs.get('path'),kwargs.get('filename'),kwargs.get('type'));
        return True;

    @staticmethod
    def myFunction(path:str,filename:str):
        print("Hello World!");
        input();