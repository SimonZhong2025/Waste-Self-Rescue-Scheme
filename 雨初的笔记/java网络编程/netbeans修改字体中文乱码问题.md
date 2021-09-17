netbeans 默认编辑器的字体实在太不好看，在工具→选项→字体和颜色，修改字体后，中文现实乱码。

下面以修改为CONSOLA为例，如何解决乱码问题。

在jdk的安装目录下，C:\Program Files\Java\jdk1.8.0_281\jre\lib找到fontconfig.properties.src，复制并重命名为fontconfig.properties。

打开后，找到 Component Font Mappings 表示字体映射，可以看到几种字体映射集合，常见的有serif、sansserif、monospaced、dialog、dialoginput等，实际上在netbeans ide中也只有这几种字体能够正常显示中文，因为他们集合了英文、中文以及字符。

在文件末尾添加如下内容：

```properties
filename.Consolas=CONSOLA.TTF
filename.Consolas_Bold=CONSOLAB.TTF
filename.Consolas_Italic=CONSOLAI.TTF
filename.Consolas_Bold_Italic=CONSOLAZ.TTF
```

​    好了，现在修改上面提到的映射字体，选择你喜欢的一组，比如DialogInput，下面对其进行修改：

​    在fontconfig.properties中找到

```properties
dialoginput.plain.alphabetic=Courier New
dialoginput.bold.alphabetic=Courier New Bold
dialoginput.italic.alphabetic=Courier New Italic
dialoginput.bolditalic.alphabetic=Courier New Bold Italic
```

​    修改为

```properties
dialoginput.plain.alphabetic=Consolas
dialoginput.bold.alphabetic=Consolas Bold
dialoginput.italic.alphabetic=ConsolasItalic
dialoginput.bolditalic.alphabetic=Consolas Bold Italic
```



    保存

​    现在打开netbeans ide，工具→选项→编辑器。选择默认字体为DialogInput，则可以看到编辑器正常显示中文，英文则显示为Consolas字体。