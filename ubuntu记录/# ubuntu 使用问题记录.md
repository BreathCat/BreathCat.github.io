# ubuntu 使用问题记录

## zsh can not use conda

Solution: 

```bash
vim ~/.zshrc
```
add one line :
`export PATH=/home/li/anaconda3/bin:$PATH`

```bash
source ~/.zshrc
conda init zsh
```

## zsh "home" button doesn't work

Solution:

 [weibisite solution](https://conanblog.me/blog/2012/08/20/resolve-zsh-home-and-end-key-problem/)

Coding solution:

`vim ~/.zshrc`, and add the following code

```bash
bindkey "^[[H" beginning-of-line  # Home键                   
bindkey "^[[F" end-of-line  # End键                         
bindkey "^[[A" forward-word  # 方 向 上 键
bindkey "^[[B" backward-word  # 方 向 下 键   
```

## tmux default shell 'bash' →'zsh'

`vim ~/.tmux.conf ` , add 

```bash
set -g default-shell /bin/zsh 
set -g default-command /bin/zsh
```

## tmux using mouse to page up/down

`cd ~/.tmux_conf`, add

```bash
set -g mouse on
```
## Terminus directory background color is unclear

Modify the the terminus `color scheme` the ` color 4 ` to be  `#8FBC8F`