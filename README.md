# python-web
python 在web方向的应用， 也许不只是web 也许吧。

### django
  根据 django框架组织的一个web结构，用于做一个展示的平台。

### data
  帮大傻子处理数据的脚本。

  - python 读文件编码的问题可以说是很恶心了。

  - 错误编码
  ```
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3598: ordinal not in range(128)
  ```

  ```python
    # python2 的解决方法
    import sys
    reload(sys) 
    sys.setdefaultencoding('utf-8')
  ```

 ```python
    # python3 的解决方法, 但是这种方式我并没有生效
    import importlib
    importlib.reload(sys)

    # 我才用的解决办法
    with open('simple.train.dat', encoding='utf-8') as inf:
      lines = inf.readlines()
  ```

  
  贴一下解决方案的链接 (https://stackoverflow.com/questions/35028683/python3-unicodedecodeerror-with-readlines-method/41652865)
