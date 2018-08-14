import os


if __name__ == '__main__':
    print("""\033[1;31;40m
                                             
                                                                                                                       
     I$    $$$$$$   $        \$    $$$$$  
    $$$        z$  m$        $$    $b  $$ 
  $$ $"        $   $j       $%$    $    $ 
     $       l$    $        $ $$   $   M$ 
     $      '$     $       $  ]$   $$$$v  
     $      $      $       $   $  u$   $$ 
    O$     $      o$      $$$$$$  $0    $ 
    $     $       $$     %$    $  $    $% 
 $$$$$$@ $$$$$$$  $$$$$$ $     $  $$$$$$  
                                          
                                                                                                                                                                   
    \033[0m""")
    print('\033[1;31;40minit machine...\033[0m')
    files = os.listdir()
    os.mkdir('hotload')
    for i in files:
        if not i == 'main.py' and not i == 'boot.py':
            os.rename(i, '/hotload/%s' % i)
    main_code = """
import network
import json
import sys


if __name__ == '__main__':
    # 添加ezlab包路径  add module ezlab to path 
    sys.path.append('hotload')
    from tools import load_config
    # 是否开启热加载    hotloader mode or not
    if load_config():
        from hotload_server import hotloader
        hotloader().Start()
    else:
        # your own code goes here
        pass
"""
    with open('main.py', 'w') as f:
        f.write(main_code)

    print('\033[1;31;40minit done,please reboot the machine.\033[0m')
