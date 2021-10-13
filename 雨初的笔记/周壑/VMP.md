+ x32dbg里面按 `h` 再选择寄存器可以高亮寄存器。

### 去混淆

+ 在去VMP的混淆的时候主要思想是找两次连续写同一个寄存器的操作。因为如果两次连续写同一个寄存器的话那么前一次指令是无效的混淆指令，那么我们可以丢弃这个指令。而VMP中很少有对内存操作的混淆指令，因此其实可以忽略对内存操作的指令的混淆，而认为对于内存进行操作的指令都是有效的。

+ 特殊地， `pop eax` ， `push eax` 这样的指令也应该认为是有效的，因为他们也进行了内存的修改，而对于内存存在修改的指令应该笼统认为是有效的指令。

+ 对于一个寄存器，因为VMP中存在对 `al, ah, ax` 之类的寄存器的读写，因此还要对一个寄存器进行进一步的细分。具体应该细分成这样

  ![image-20211010091455033](C:\Users\22112\AppData\Roaming\Typora\typora-user-images\image-20211010091455033.png)

+ ![image-20211010093015520](C:\Users\22112\AppData\Roaming\Typora\typora-user-images\image-20211010093015520.png)

+ 对于TMD加壳的时候，如果是使用TMD的SDK来加壳，且不手动把函数设置为裸函数并自己提升堆栈，那么函数入口的 `push ebp` `mov ebp, esp` 是可以看到的。这样我们就可以分析出不同的函数，然后根据不同函数的返回值来尝试爆破。

  ![image-20211010100322834](C:\Users\22112\AppData\Roaming\Typora\typora-user-images\image-20211010100322834.png)

+ 可以通过一些方法不写 `jcc` 。

  ![image-20211010195759198](C:\Users\22112\AppData\Roaming\Typora\typora-user-images\image-20211010195759198.png)

### 测试

+ ![image-20211013134210003](https://cdn.jsdelivr.net/gh/smallzhong/new_new_picgo_picbed@main/image-20211013134210003.png)

  首先关掉增量链接和优化
  
  ![image-20211013134041556](https://raw.githubusercontent.com/smallzhong/new_new_picgo_picbed/main/image-20211013134041556.png)
  
  

