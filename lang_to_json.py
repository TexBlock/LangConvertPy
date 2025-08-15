import json
import os

def lang_to_json(lang_input, output_file=None):
    """
    将lang格式数据转换为JSON格式数据

    参数:
    lang_input (str): lang文件路径或lang字符串
    output_file (str, optional): 输出文件路径，如果为None则返回字符串

    返回:
    str: 转换后的JSON格式数据，如果指定了output_file则返回None
    """
    # 判断输入是文件路径还是lang字符串
    if os.path.isfile(lang_input):
        with open(lang_input, 'r', encoding='utf-8') as f:
            lang_content = f.read()
    else:
        lang_content = lang_input

    # 解析lang格式
    data = {}
    lines = lang_content.strip().split('\n')
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)  # 只分割第一个等号
            data[key.strip()] = value.strip()

    # 转换为JSON格式
    json_content = json.dumps(data, ensure_ascii=False, indent=2)

    # 输出处理
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_content)
        return None
    else:
        return json_content

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='将lang格式转换为JSON格式')
    parser.add_argument('input', help='lang文件路径或lang字符串')
    parser.add_argument('-o', '--output', help='输出文件路径')
    parser.add_argument('-s', '--string', action='store_true', help='指定输入为lang字符串')

    args = parser.parse_args()

    if args.string:
        input_data = args.input
    else:
        input_data = args.input

    result = lang_to_json(input_data, args.output)

    if result:
        print(result)