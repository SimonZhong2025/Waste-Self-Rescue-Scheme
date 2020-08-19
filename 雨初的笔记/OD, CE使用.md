+ OD中 `ctrl + G` 跳转到某一指定地址。
+ OD中命令 `dd xxxxx` 是 **data DWORD** 的意思，以DWORD为单位查看数据。如果是 `db xxxx` 就是 `data BYTE` 以字节为单位查看数据。
+ `ctrl + f9` 执行完这个函数并断在 `retn` 那里。 `f8` 下一步（返回），这样可以回到调用这个函数的那个  `call` 的下一行。