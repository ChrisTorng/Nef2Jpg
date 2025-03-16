import argparse
import os
import glob
from PIL import Image
import rawpy

def convert_nef_to_jpg(input_path):
    if os.path.isfile(input_path):
        convert_file(input_path)
    elif os.path.isdir(input_path):
        for nef_file in glob.glob(os.path.join(input_path, '*.nef')):
            convert_file(nef_file)
    else:
        print(f"無效的輸入路徑: {input_path}")

def convert_file(nef_file):
    try:
        with rawpy.imread(nef_file) as raw:
            rgb = raw.postprocess()
            img = Image.fromarray(rgb)
            width, height = img.size
            jpg_file = os.path.splitext(nef_file)[0] + '.jpg'
            img.save(jpg_file, 'JPEG')
            print(f"轉換成功: {nef_file} -> {jpg_file} ({width}x{height})")
    except Exception as e:
        print(f"轉換失敗: {nef_file}, 錯誤: {e}")

def main():
    parser = argparse.ArgumentParser(description='NEF 轉 JPG 自動轉檔程式')
    parser.add_argument('input', nargs='+', help='輸入檔案或資料夾')
    args = parser.parse_args()

    for input_path in args.input:
        convert_nef_to_jpg(input_path)

if __name__ == '__main__':
    main()
