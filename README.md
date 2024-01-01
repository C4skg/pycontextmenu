# pycontextmenu
 一个 windows 桌面右键菜单脚本丰富工具

## 工具自带脚本工具
|功能描述|支持详情|
|-------|-------|
|文件 `md5 \| sha1` 值计算|<div align="center"><img width="50px" src="icon/file.png" /></div>|
|文件数据头检测| <div align="center"><img width="50px" src="icon/file.png" /></div>|
|强制解除占用|<div align="center"><img width="50px" src="icon/file.png" /><img width="50px" src="icon/folder.png" /></div>|

## 自定义功能
### 1. 创建模板
```bash
python3 pycontextmenu.py create myscript.py
```
随后就会在该目录下生成带有以下代码的 `myscript.py` 文件

```python
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
```
### 2. 加入菜单
在编程结束后，使用如下命令将自定义的脚本加入右键菜单中
```bash
python3 pycontextmenu.py -add myscript.py -name "打印 Hello World"
```
### 3. 测试
随后测试右键菜单中是否出现该自定义的脚本即可