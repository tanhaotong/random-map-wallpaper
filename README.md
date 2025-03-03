<h1 align="center">Random Map Wallpaper</h1>

<p align="center">一个自动生成随机地图壁纸的Python工具</p>

## 简介
这个工具会随机生成陆地上的经纬度坐标，然后使用Mapbox API获取该位置的地图图像作为壁纸。每次运行，您都能获得一张来自世界各地的独特地图壁纸。

## 特性
- 使用Mapbox API生成精美地图
- 地图样式可个性化定制（默认样式由[Madison Draper](https://www.mapbox.com/blog/designing-the-mineral-map-style)提供）
- 避免生成单调的海洋图片（使用[Natural Earth Data](http://www.naturalearthdata.com)提供的数据）
- 可设置为每日自动更新壁纸

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 首先在`map.py`文件中填入您的Mapbox令牌：
   ```python
   token = "your_mapbox_token_here"  # 填入您自己的Mapbox令牌
   ```

2. 运行程序：
   ```python
   python map.py
   ```

## 设置每日自动更新壁纸

### 方法1：使用Windows任务计划程序

1. 按下 "Win" + "R" 组合键
2. 输入 `taskschd.msc` 并点击确定
   ![任务计划程序](image.png)

3. 在右侧操作面板，点击"创建基本任务"
   - 输入任务名称（如"每日壁纸更新"）
   - 选择"每天"并设置时间
   - 在"操作"中选择"启动程序"

4. 在"程序或脚本"中，输入Python解释器路径：
   ```
   C:\Path\To\Python\python.exe
   ```

5. 在"添加参数"中，输入脚本路径：
   ```
   "D:\Path\To\random-map-wallpaper\map.py"
   ```

6. 在"起始于"中，输入脚本所在文件夹：
   ```
   D:\Path\To\random-map-wallpaper
   ```

7. 完成后，右键点击创建的任务，选择"属性"
   - 在"常规"选项卡中勾选"使用最高权限运行"
   - 保存更改

### 方法2：导入预设任务

1. 按下 "Win" + "R" 组合键，输入 `taskschd.msc`
   ![image.png](https://s2.loli.net/2025/03/03/yrbMpHlLUdjoBkN.png)

2. 在任务计划程序中，点击右侧"操作"面板中的"导入任务"
   ![image-2.png](https://s2.loli.net/2025/03/03/BYXU1L3wcKDk7yF.png)

3. 选择项目目录中的 `new-wallpaper.xml` 文件

4. 导入后，右键点击导入的任务，选择"属性"，修改操作选项卡中的路径为您的实际路径
   ![修改路径]![image-1.png](https://s2.loli.net/2025/03/03/aj9FkQzGJPOyqgE.png)
