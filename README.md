# OCR截图引用技能

一个用于从截图中提取文字并按照飞书格式输出引用和想法的技能。

## 功能

- 使用OCR技术从截图中提取文字
- 将提取的文字作为"引用"部分
- 用户可添加自己的"想法"
- 按照飞书格式输出，可直接复制粘贴

## 技能文件

- `ocr-screenshot-quote/SKILL.md` - 技能定义文件
- `ocr-screenshot-quote/main.py` - OCR处理代码
- `ocr-screenshot-quote/requirements.txt` - 依赖列表
- `ocr-screenshot-quote/examples/` - 示例输入输出

## 安装依赖

```bash
pip install -r ocr-screenshot-quote/requirements.txt
```

## 使用方法

### 在 Trae 中使用

1. 在 Trae 中导入 `SKILL.md` 文件
2. 发送截图并输入想法，如：
   ```
   [发送截图]
   我的想法：这段内容很有意思。
   ```

### 命令行使用

```bash
python ocr-screenshot-quote/main.py /path/to/screenshot.png -t "我的想法"
```

## 输出格式

```
> 引用内容
> 
> （从截图中提取的文字）
> 
> ——
> 
> 想法内容
> 
> （用户提供的想法）
```

## 注意事项

- 需要安装 Tesseract OCR 引擎
- 支持中英文混合识别