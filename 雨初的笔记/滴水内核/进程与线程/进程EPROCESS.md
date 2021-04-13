+ `PsActiveProcessHead` 指向全局链表头，该变量未导出。

+ 当线程进入**0环**时，**FS:[0]指向`KPCR`**(**3环**时**FS:[0] -> TEB**)

+ 在零环获取当前进程的 `EPROCESS` 的方法如下

  ```c
  __asm
  {
      mov eax, fs:[0x124];
      mov eax, [eax + 0x220];
      mov pEprocess, eax;
  }
  ```

  首先通过 `fs:[0x124]` 找到指向 `KTHREAD` 的指针（在零环fs指向 `KPCR` 结构体）

  ![image-20210201174540485](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210201174700221.png)

  因为 `KTHREAD` 是 `ETHERAD`的第一个元素，而 `ETHREAD` 第 `0x220` 位是指向其所属进程的 `EPROCESS` 结构体的指针

  ![image-20210201174700221](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210201174700221.png)

  因此在获取指向 `KTHREAD` 的指针后 `[eax+0x220]` 即为当前进程 `EPROCESS` 的指针。

+ 

### 线程结构体

