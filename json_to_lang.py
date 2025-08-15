import json
import os

def json_to_lang(json_input, output_file=None):
    """
    将JSON格式数据转换为lang格式数据

    参数:
    json_input (str): JSON文件路径或JSON字符串
    output_file (str, optional): 输出文件路径，如果为None则返回字符串

    返回:
    str: 转换后的lang格式数据，如果指定了output_file则返回None
    """
    # 判断输入是文件路径还是JSON字符串
    if os.path.isfile(json_input):
        with open(json_input, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        try:
            data = json.loads(json_input)
        except json.JSONDecodeError:
            raise ValueError("无效的JSON字符串或文件路径")

    # 转换为lang格式
    lang_lines = []
    for key, value in data.items():
        lang_lines.append(f"{key}={value}")

    lang_content = '\n'.join(lang_lines)

    # 输出处理
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(lang_content)
        return None
    else:
        return lang_content

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='将JSON格式转换为lang格式')
    parser.add_argument('input', help='JSON文件路径或JSON字符串')
    parser.add_argument('-o', '--output', help='输出文件路径')
    parser.add_argument('-s', '--string', action='store_true', help='指定输入为JSON字符串')

    args = parser.parse_args()

    if args.string:
        input_data = args.input
    else:
        input_data = args.input

    result = json_to_lang(input_data, args.output)

    if result:
        print(result)