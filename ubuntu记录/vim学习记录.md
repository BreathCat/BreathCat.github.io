# vim学习记录

## vim function jump
[参考链接](https://youguanxinqing.xyz/archives/104/)

步骤:

1. put the [ptags.py](https://github.com/python/cpython/blob/master/Tools/scripts/ptags.py) file in your project directoty.

2. in the project directory, open terminal, run `find ./ -name "*.py" | xargs python3 ptags.py`

3. Then you get the **tag** file in your dir. After that, modify your vim config file. `vim ~/.vimrc` , add `set tags=./tags,tags;` (from [forum](https://stackoverflow.com/questions/8285232/vim-set-ctags-in-vimrc)), then you may `source ~/.vimrc`

4. 

   

   

