## 系统调用阶段测试——基于 SSDT HOOK 的 FindWindowA 监视器

+ `KeServiceDescriptorTableShadow` 未导出，可以通过特征码搜索（？交叉引用），或者更简单的方法是 `KeServiceDescriptorTableShadow - 0x40` 

+ 要通过devicecontrol来调用，因为调用的进程必须使用过gdi，否则没有挂页会导致蓝屏

+ ![image-20210202163211486](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210202163211486.png)

  调用 `Messagebox` 之后会变成一个 `gui` 线程（or进程？上课好像说的是进程），然后 `e0` 指向的地方会变成有 `shadow` 那个？

