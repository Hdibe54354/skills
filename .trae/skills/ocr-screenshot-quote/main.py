import pytesseract
from PIL import Image
import argparse
import sys

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='chi_sim+eng')
        return text.strip()
    except Exception as e:
        return f"OCR识别失败: {str(e)}"

def format_for_feishu(quote_text, thought_text):
    formatted = f"> 引用内容\n>\n> {quote_text}\n>\n> ——\n>\n> 想法内容\n>\n> {thought_text}"
    return formatted

def main():
    parser = argparse.ArgumentParser(description='OCR截图文字提取并按飞书格式输出')
    parser.add_argument('image_path', help='截图图片路径')
    parser.add_argument('--thought', '-t', help='用户的想法文字')
    
    args = parser.parse_args()
    
    quote_text = extract_text_from_image(args.image_path)
    
    if args.thought:
        result = format_for_feishu(quote_text, args.thought)
    else:
        result = f"> 引用内容\n>\n> {quote_text}"
    
    print(result)
    return result

if __name__ == '__main__':
    main()