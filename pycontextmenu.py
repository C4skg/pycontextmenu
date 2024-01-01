# from core.background
from core.task import SubTask
from core.args import ServiceHelper

def start():
    helper = ServiceHelper('pycontextmenu');
    helper.showArgs();
    args = helper.parse_args();
    if args.help:
        helper.print_help();

    elif args.change:
        SubTask._change(args.change);

    elif args.create:
        pass;
    elif args.list:
        pass;
    elif args.add:
        if not args.name:
            raise EOFError("the arguments name is null");
        pass;
    else:
        pass;

if __name__ == '__main__':
    start();    
    
    