# pyxlsx

通过pyxlsx.py脚本给Excel文件建立目录，并建立跳转使用的超链接。此脚本目前支持xls及xlsx格式文件。其中，如果文件类型是xls则会被程序转化为xlsx格式文件。

可以通过在Windows终端中输入如下命令执行脚本：

```powershell
# 确认好系统里已安装Python。用[python]命令运行pyxlsx.py脚本，并输入参数p
python pyxlsx.py -p [文件所在路径]
# 范例 python pyxlsx.py -p C:\Users\zhhon\Desktop\abc.xlsx
```

为Windows10+平台开发的桌面版应用放在dist文件夹内。进入建立目录的页签，通过打开按钮指定需要建立目录的excel文件，点击建立目录。

建立目录的逻辑：

* 默认会在当前excel文件中新建一个叫做“目录”的sheet，并将所有sheet的超链接按次序，从上到下置入目录sheet的第一列。
* 为了让链接良好闭环，会默认在所有sheet的[A3]单元格建立返回目录的超链接
* 如果检测到已存在“目录”sheet，则会覆盖此sheet

![1656471552311](image/README/1656471552311.png)
