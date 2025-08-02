import re
from pypinyin import pinyin, Style
from googletrans import Translator
import time

translator = Translator()

def get_translation(text, target_lang='ar'):
    try:
        result = translator.translate(text, src='zh-cn', dest=target_lang)
        return result.text
    except Exception as e:
        print(f"ترجمة خطأ: {text} -> {e}")
        return ''

input_filename = "唐探1900.srt"
output_filename = "唐探1900_pinyin_arabic.srt"

with open(input_filename, 'r', encoding='utf-8') as f:
    srt_lines = f.readlines()

output_lines = []
i = 0
while i < len(srt_lines):
    output_lines.append(srt_lines[i].rstrip('\n'))  # رقم الترجمة أو التوقيت
    i += 1
    if i < len(srt_lines):
        output_lines.append(srt_lines[i].rstrip('\n'))  # التوقيت أو السطر الصيني
        i += 1
    if i < len(srt_lines):
        line = srt_lines[i].rstrip('\n')
        output_lines.append(line)
        # لو فيه صيني في السطر، أضف تحته Pinyin + الترجمة العربية
        if re.search('[\u4e00-\u9fff]', line):
            # Pinyin
            py = pinyin(line, style=Style.TONE, strict=False)
            py_line = ' '.join([word[0] for word in py])
            output_lines.append(py_line)
            # ترجمة عربية
            translation = get_translation(line, 'ar')
            output_lines.append(translation)
            time.sleep(0.4)  # تجنب بلوك جوجل ترانزليت
        i += 1
    # في بعض الأحيان فيه سطر إضافي (ترجمة إنجليزي)، هنتعامل معاه ببساطة
    while i < len(srt_lines) and srt_lines[i].strip() != "" and not srt_lines[i].strip().isdigit() and not "-->" in srt_lines[i]:
        line = srt_lines[i].rstrip('\n')
        output_lines.append(line)
        if re.search('[\u4e00-\u9fff]', line):
            py = pinyin(line, style=Style.TONE, strict=False)
            py_line = ' '.join([word[0] for word in py])
            output_lines.append(py_line)
            translation = get_translation(line, 'ar')
            output_lines.append(translation)
            time.sleep(0.4)
        i += 1
    if i < len(srt_lines):
        output_lines.append('')  # سطر فاضي بين الجمل
        i += 1

with open(output_filename, 'w', encoding='utf-8') as f:
    for l in output_lines:
        f.write(l + '\n')

print("مبروك، تمت إضافة البينين والترجمة العربية بنجاح!")

