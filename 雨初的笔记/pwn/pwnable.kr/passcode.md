+ 这道题在 `welcome` 和 `login` 之间没有多余的操作，所以调用 `login` 的时候， `ebp` 和 `welcome` 时候的 `ebp` 是一样的。而一旦进入到 `login` 就没有可以干的事情了，我们只有在调用 `welcome` 的时候往 `passcode1` 里面写入 `system` 的地址才行。没有开 `PIE` ，所以直接填地址就可以。
+ ![image-20201024152018951](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201024152018951.png)
+ 所以我们完全可以先找到 `fflush` 的got表项地址（程序没有开PIE，无需leak），把 `passcode1` 布局为该地址，并在调用到 `scanf(“%d”, passcode1)` 时输入程序代码中调用`system("/bin/cat flag");`处的地址即可。这样调用 `scanf` 的时候就会将 `system("/bin/cat flag")` 的地址写入到 `fflush` 的 `got` 表里面。
+ https://r00tk1ts.github.io/2018/03/05/passcode/
+ ![img](https://r00tk1ts.github.io/images/ctf/pwn/pwnable.kr/passcode_07.jpg)