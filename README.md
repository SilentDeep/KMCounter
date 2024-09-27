# KMCounter

KMCounter 是一个用于记录和显示键盘和鼠标点击次数的程序，并通过柱状图和热图展示。本软件基于 Python、Flask、Plotly 等开发。

目前仅针对 macOS 的键盘进行了设计，Windows 键盘映射可能存在缺陷。

目前未将程序打包为 app 或 exe，需要使用者有一定 Python 基础。

## 界面展示
![界面展示](./assets/PixelSnap%202024-09-27%20at%2022.26.37@2x.png)

## 功能

- 记录各键盘按键和鼠标点击次数
- 用柱状图展示点击次数随时间变化情况
- 根据时间范围过滤并用热力图可视化点击次数

## 安装

1. 克隆此仓库：
    ```bash
    git clone https://github.com/SilentDeep/KMCounter.git
    cd KMCounter
    ```

2. 创建并激活虚拟环境（可选）：
    ```bash
    conda create -n KMCounter python=3.9 -y
    conda activate KMCounter
    ```

3. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 使用

1. 运行主程序：（先 `cd` 到 `KMCounter` 文件夹）
    ```bash
    python main.py
    ```

2. 打开浏览器并访问 `http://127.0.0.1:5000` 查看应用程序。

## 贡献

欢迎提交 issue 和 pull request 来改进此项目。

## 许可证

此项目使用 GNU General Public License v3.0 许可证。详情请参阅 [LICENSE](./LICENSE) 文件。

## Todo List
有空来填坑：
- [ ] 屏幕鼠标点击位置热力图
- [ ] 增加 Windows 键盘
- [ ] 某些特殊键未计入
