### time库的使用

#### time库是python中处理时间的标准库

- 计算机时间的表达
- 提供获取系统时间并格式化输出功能
- 提供系统级精确计时功能，用于程序性能分析

`import time</br>time.<b>()`

#### time库的三类函数

1. 时间获取：`time() ctime() gmtime()`
2. 时间格式：`strtime() strptime()`
3. 程序计时：`sleep() perf_counter()`

|函数|描述|
|:---:|:---:|
|time()|获取当前的时间戳，计算机内部时间值，浮点数|
|ctime()|获取当前时间并以易读方式表示，返回字符串</br>`>>>time.ctime()</br>'Fri Jan 26 12:11:16 2018'|
|gmtime()|获取当前时间，表示为**计算机可处理**的时间格式</br>`time.struct_time(tm_year=2018, tm_mon=1, tm_mday=26, tm_hour=4, tm_min=11, tm_sec=16, tm_wday=4, tm_yday=26, tmisdst=0)`|

#### 时间处理

|函数|描述|
|:---:|:---:|
|strftime(tpl, ts)|tpl是格式化模板字符串，用来定义输出效果；ts是计算机内部时间类型变量</br> `>>>t = time.gmtime()</br>>>>time.strftime("%Y-%m-%f %H-:%M:%S", t)</br>'2018-01-26 12:55:20`|
|strptime(str, tpl)|str是字符串形式的时间值</br>tpl是格式化模板字符串，用来定义输入效果</br>>>>timeStr = '2018-01-26 12:55:20'</br>>>>time.strptime(timeStr, "%Y-%m-%f %H-:%M:%S")|


|格式化字符|日期、时间说明|值范围和实例|
|:---:|:---:|:---:|
|%Y|年份|1900|
|%m|月份|01~12|
|%B|月份名称|April|
|%b|月份简称|Apr|
|%d|日期|01~31|
|%A|星期|Wednesday|
|%a|星期缩写|Wed|
|%H|小时（24小时）|00~23|
|%I|小时（12小时）|01~~12|
|%p|上/下午|AM, PM|


#### 程序计时

- 测量时间：perf_counter()
- 产生时间：sleep()

|函数|描述|
|:---:|:---:|
|perf_counter()|返回一个CPU级别的时间计数值，单位为秒，连续调用差值才有意义</br>`>>>start = time.per_counter()</br>111.1212123231</br>end = time.perf_counter()</br>324234</br>end - start</br>234234233`|
|sleep(s)|s是拟休眠的时间，单位是秒，可以是浮点数</br>`>>>def wait:</br>time.sleep(3.3)</br>>>>wait()  #调用这个函数，并程序将等待3.3秒后再退出`|
