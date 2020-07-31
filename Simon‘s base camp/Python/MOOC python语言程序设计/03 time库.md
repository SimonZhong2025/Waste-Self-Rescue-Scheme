### time库的使用

##### time库是python中处理时间的标准库

- 计算机时间的表达
- 提供获取系统时间并格式化输出功能
- 提供系统级精确计时功能，用于程序性能分析

`import time</br>time.<b>()`

##### time库的三类函数

1. 时间获取：`time() ctime() gmtime()`
2. 时间格式：`strtime() strptime()`
3. 程序计时：`sleep() perf_counter()`

|函数|描述|
|:---:|:---:|
|time()|获取当前的时间戳，计算机内部时间值，浮点数|
|ctime()|获取当前时间并以易读方式表示，返回字符串</br>`>>>time.ctime()</br>'Fri Jan 26 12:11:16 2018'|
|gmtime()|获取当前时间，表示为计算机可处理的时间格式</br>`time.struct_time(tm_year=2018, tm_mon=1, tm_mday=26, tm_hour=4, tm_min=11, tm_sec=16, tm_wday=4, tm_yday=26, tmisdst=0)`|

