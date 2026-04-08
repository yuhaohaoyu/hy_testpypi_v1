## URLS:

- source: https://github.com/yuhaohaoyu/hy_testpypi_v1

- PyPi package v1: https://pypi.org/project/hy-testpypi-v1/
- PyPi package v2: https://pypi.org/project/hy-testpypi-v2/


## Build

```
ln -s v1/pyproject.toml .
python3 -m build --wheel
rm pyproject.toml
ln -s v2/pyproject.toml .
python3 -m build --wheel
```


## Upload
```
twine upload dist/hy_testpypi_v1-0.1.0-py3-none-any.whl 
Uploading distributions to https://upload.pypi.org/legacy/
Uploading hy_testpypi_v1-0.1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.0/7.0 kB • 00:00 • ?

View at:
https://pypi.org/project/hy-testpypi-v1/0.1.0/

twine upload dist/hy_testpypi_v2-0.1.0-py3-none-any.whl 
Uploading distributions to https://upload.pypi.org/legacy/
Uploading hy_testpypi_v2-0.1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.0/7.0 kB • 00:00 • ?

View at:
https://pypi.org/project/hy-testpypi-v2/0.1.0/
```

## Test

### Test code

```
cat main.py 
# main.py
from testpypi import mymodule

# Accessing the function using dot notation
message = mymodule.greeting("Jonathan")
print(message)  # Output: Hello, Jonathan!

# Accessing the variable
print(mymodule.person["name"])  # Output: Alice
```

### testpypi module not installed

```
(mac-py-a) yuhibmmac2025@mac tests % python3 main.py              
Traceback (most recent call last):
  File "/Users/yuhibmmac2025/Work/perfcount/issues-here-there/TESTS-aiu/hy_testpypi_v1/tests/main.py", line 2, in <module>
    from testpypi import mymodule
ModuleNotFoundError: No module named 'testpypi'

(mac-py-a) yuhibmmac2025@mac tests % ls -otd ~/Work/mac-py-a/lib/python3.13/site-packages/* | head -5
drwxr-xr-x   10 yuhibmmac2025     320 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine-6.2.0.dist-info
drwxr-xr-x   17 yuhibmmac2025     544 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine
drwxr-xr-x    9 yuhibmmac2025     288 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/keyring-25.7.0.dist-info
drwxr-xr-x   20 yuhibmmac2025     640 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/keyring
drwxr-xr-x    7 yuhibmmac2025     224 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/rich-14.3.3.dist-info
```

### install hy_testpypi_v1 from pypi

```
pip install hy-testpypi-v1                                    
Collecting hy-testpypi-v1
  Downloading hy_testpypi_v1-0.1.0-py3-none-any.whl.metadata (126 bytes)
Downloading hy_testpypi_v1-0.1.0-py3-none-any.whl (5.5 kB)
Installing collected packages: hy-testpypi-v1
Successfully installed hy-testpypi-v1-0.1.0

(mac-py-a) yuhibmmac2025@mac tests % python3 main.py                                                 
Byebye, Jonathan!
Spyre

(mac-py-a) yuhibmmac2025@mac tests % ls -otd ~/Work/mac-py-a/lib/python3.13/site-packages/* | head -5
drwxr-xr-x    9 yuhibmmac2025     288 Apr  8 14:54 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/hy_testpypi_v1-0.1.0.dist-info
drwxr-xr-x    4 yuhibmmac2025     128 Apr  8 14:54 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/testpypi
drwxr-xr-x   10 yuhibmmac2025     320 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine-6.2.0.dist-info
drwxr-xr-x   17 yuhibmmac2025     544 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine
```

### uninstall hy_testpypi_v1 

```
pip3 uninstall hy_testpypi_v1                                   
Found existing installation: hy_testpypi_v1 0.1.0
Uninstalling hy_testpypi_v1-0.1.0:
  Would remove:
    /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/hy_testpypi_v1-0.1.0.dist-info/*
    /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/testpypi/mymodule.py
Proceed (Y/n)? 
  Successfully uninstalled hy_testpypi_v1-0.1.0

(mac-py-a) yuhibmmac2025@mac tests % ls -otd ~/Work/mac-py-a/lib/python3.13/site-packages/* | head -5
drwxr-xr-x   10 yuhibmmac2025     320 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine-6.2.0.dist-info
drwxr-xr-x   17 yuhibmmac2025     544 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine
drwxr-xr-x    9 yuhibmmac2025     288 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/keyring-25.7.0.dist-info
drwxr-xr-x   20 yuhibmmac2025     640 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/keyring

(mac-py-a) yuhibmmac2025@mac tests % python3 main.py                                                 
Traceback (most recent call last):
  File "/Users/yuhibmmac2025/Work/perfcount/issues-here-there/TESTS-aiu/hy_testpypi_v1/tests/main.py", line 2, in <module>
    from testpypi import mymodule
ModuleNotFoundError: No module named 'testpypi'
```


### install hy_testpypi_v2 from pypi

pip install hy-testpypi-v2                                      
Collecting hy-testpypi-v2
  Using cached hy_testpypi_v2-0.1.0-py3-none-any.whl.metadata (126 bytes)
Using cached hy_testpypi_v2-0.1.0-py3-none-any.whl (5.5 kB)
Installing collected packages: hy-testpypi-v2
Successfully installed hy-testpypi-v2-0.1.0

(mac-py-a) yuhibmmac2025@mac tests % ls -otd ~/Work/mac-py-a/lib/python3.13/site-packages/* | head -5
drwxr-xr-x    9 yuhibmmac2025     288 Apr  8 14:55 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/hy_testpypi_v2-0.1.0.dist-info
drwxr-xr-x    4 yuhibmmac2025     128 Apr  8 14:55 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/testpypi
drwxr-xr-x   10 yuhibmmac2025     320 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine-6.2.0.dist-info
drwxr-xr-x   17 yuhibmmac2025     544 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine

(mac-py-a) yuhibmmac2025@mac tests % python3 main.py                                                 
Byebye, Jonathan!
Spyre

### uninstall hy_testpypi_v2 

(mac-py-a) yuhibmmac2025@mac tests % pip3 uninstall hy_testpypi_v2                                   
Found existing installation: hy_testpypi_v2 0.1.0
Uninstalling hy_testpypi_v2-0.1.0:
  Would remove:
    /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/hy_testpypi_v2-0.1.0.dist-info/*
    /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/testpypi/mymodule.py
Proceed (Y/n)? 
  Successfully uninstalled hy_testpypi_v2-0.1.0

(mac-py-a) yuhibmmac2025@mac tests % python3 main.py              
Traceback (most recent call last):
  File "/Users/yuhibmmac2025/Work/perfcount/issues-here-there/TESTS-aiu/hy_testpypi_v1/tests/main.py", line 2, in <module>
    from testpypi import mymodule
ModuleNotFoundError: No module named 'testpypi'

(mac-py-a) yuhibmmac2025@mac tests % ls -otd ~/Work/mac-py-a/lib/python3.13/site-packages/* | head -5
drwxr-xr-x   10 yuhibmmac2025     320 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine-6.2.0.dist-info
drwxr-xr-x   17 yuhibmmac2025     544 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/twine
drwxr-xr-x    9 yuhibmmac2025     288 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/keyring-25.7.0.dist-info
drwxr-xr-x   20 yuhibmmac2025     640 Apr  8 14:13 /Users/yuhibmmac2025/Work/mac-py-a/lib/python3.13/site-packages/keyring

