+ ![](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110131043288.png)

+ ![image-20210110131321378](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110131321378.png)

+ **transmate** 是国产的

  ![ ](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110131355733.png)

+ core of translation technology是什么？

  ![image-20210110150730101](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110150730101.png)

+ ![image-20210110132137967](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110132137967.png)

+ 这又应该选什么？

  ![image-20210110132252326](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110132252326.png)

+ ![image-20210110150600843](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110150600843.png)

+ ![image-20210110150624571](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110150624571.png)

+ ![image-20210110150710258](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110150710258.png)

+ ![image-20210110150827278](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110150827278.png)

+ **methodology** == **方法学,方法论，一套方法**

+ ![image-20210110151434676](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110151434676.png)

+ ![image-20210110151658170](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110151658170.png)



### 网课

+ ![image-20210110134901284](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110134901284.png)

+ ![image-20210110135118485](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110135118485.png)

+ **bilingual corpora** 才是对翻译有价值的语料库![image-20210110135917111](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110135917111.png)

+ 非译元素是蓝色的，有匹配的术语是粉色的，标识符是紫色的。

+ ![image-20210110140311010](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110140311010.png)

+ ![image-20210110140511391](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110140511391.png)

+ ![image-20210110140904613](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110140904613.png)

+ ![image-20210110141304600](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110141304600.png)

+ ![image-20210110141533124](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110141533124.png)

  句珠对是要进行避免的。

+ **上下文匹配**是最精准的

  ![image-20210110141948056](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110141948056.png)

+ ![image-20210110142143566](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210110142143566.png)

+  



### trados(overall)

+ trados只能建记忆库，不能建术语库。建术语库要用 `multiterm` 。

+ 记忆库的文件是 `sdltb` ， `tb` 是 `term base` 的意思。
+ 翻译完成之后要进行验证 



## 对比：

+ 原因可以

1. 语序混乱

2. 词义不准确

3. 孤立地进行句法分析

+ 思考：

1. 机器翻译可能会将词群连接成一个结构混乱的句子，而人工翻译就可以使句子更加流畅。

2. 句子传递给我们的不单单是单词、单句，用翻译软件(机器翻译)直接翻译段落可能无法形象的使用某个词或句子(机器多数是按照字面意思翻译)。而人工翻译与之相比就更加灵活(能够考虑到情景、双关等)。

3. 但是机器翻译也有其的优势：高速、不断扩充的资料库和低成本。
   + 在未来将会有不可小视的作用和发展，在现阶段机器翻译只能作为一种辅助工具，快速解决原文中较简单的表达和固定文本的翻译。
   + 但是我们可以将二者结合起来，相辅相成，既能节省翻译的时间，又能做出高标准的译文。



## 流程

+ 首先生成术语库，导入
+ 通过abbyy aligner将给的语料进行对齐，并导出为tmx



+ 建一个项目

+ 新建翻译记忆库，选择英到中
+ 导入tmx，如果客户给了tmx，直接导入，如果只有两个doc之类的，就用abbyy对齐了之后再导入
+ 把tmx导入到翻译记忆库中
+  通过multiterm或者glossary转换excel生成一个sdltb术语库（用户友好名、字段等）
+ 在sdl tardos里面创建一个项目，项目的文件导入待译的文件和参考的文件。
+ 往项目中导入sdltm术语库
+ 在项目中进行翻译，注意各种要点，如非译元素、非完全匹配等，对翻译的内容进行修改。
+ 进行审校
+ 进行外部审校，导出为word，和外部的专家团队进行外部审校
+ 对翻译的项目进行校对，设置各种校对的标准
+ 导出为文件包