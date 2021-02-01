## 系统调用阶段测试——基于 SSDT HOOK 的 FindWindowA 监视器

+ `KeServiceDescriptorTableShadow` 未导出，可以通过特征码搜索（？交叉引用），或者更简单的方法是 `KeServiceDescriptorTableShadow - 0x40` 
+ 要通过devicecontrol来调用，因为调用的进程必须使用过gdi，否则没有挂页会导致蓝屏
+ 