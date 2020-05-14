# Ubuntu install
## Backup
[backup methods on official website](https://help.ubuntu.com/community/BackupYourSystem)
## SSH MotionPro client

- [ ] change Wi-Fi
- [ ] change log-in account
- [ ] change `"选项"-"虚拟网卡类型"`，and change back
- [ ] Windos Administrators bash `bcdedit.exe /set nointegritychecks on` , then reboot windows **NOT** in `secure boot`, which is in `'security' - 'secure boot'` in BIOS setting.
- [ ] Re-setup the "MotionPro" software in Windows.
- [ ] Using [Internet Exploerer](https://vpn.bjtu.edu.cn/prx/000/http/localhost/login/login.html) to access VPN



## 关闭图形界面   
执行以下命令，临时关闭Ubuntu桌面版的GUI环境：
```bash
sudo service lightdm stop
```
执行以下命令，临时开启Ubuntu桌面版的GUI环境：
```bash
sudo service lightdm start
```

## gcc和g++版本设置

系统gcc[参考网站](https://blog.csdn.net/gatieme/article/details/52871438)

直接anaconda其实就可以了