## 📘 Script Description – `srt_pinyin.py`

### 🧩 **What does this script do?**

I made this Python script enhances a Chinese `.srt` subtitle file by automatically adding **Pinyin** (phonetic transcription) and **Arabic translation** under each line that contains Chinese characters.

It reads the `.srt` file line by line, identifies Chinese text, then:

* Extracts **Pinyin** using the `pypinyin` library.
* Fetches an **Arabic translation** using the Google Translate API (via the `googletrans` package).
* Appends both lines (Pinyin and translation) underneath the original subtitle.

The processed result is saved as a new `.srt` file with the same subtitle numbering and timing structure, but now enriched for language learning.
---
### 🛠️ **How it works – Step-by-step**

1. **File Reading:**

   * Loads an `.srt` file using UTF-8 encoding and reads it line-by-line.
   * Each subtitle block (number → timecode → one or more text lines) is processed in sequence.

2. **Chinese Detection:**

   * Each line is checked using a regular expression to detect Chinese characters: `[\u4e00-\u9fff]`.

3. **Pinyin Generation:**

   * For detected Chinese lines, the script uses `pypinyin.pinyin()` with `Style.TONE` to get tone-marked pinyin.
   * The result is flattened into a readable Pinyin sentence and inserted below the original line.

4. **Translation to Arabic:**

   * Each Chinese line is translated using `googletrans.Translator()` with source language `'zh-cn'` and destination `'ar'`.
   * Translations are added directly below the Pinyin.

5. **Output Writing:**

   * The enhanced subtitles are saved to a new `.srt` file.
   * The script maintains blank lines and index structure to keep the SRT format valid.

6. **Rate Limiting:**

   * A `time.sleep(0.4)` is added between API calls to avoid being rate-limited or blocked by Google Translate.

---

### 🎯 **Who is this for?**

This script is especially useful for:

* **Chinese language learners** who want to follow native media with both pronunciation (Pinyin) and understanding (Arabic meaning).
* **Subtitle creators** who want to enhance their `.srt` files with additional linguistic support.
* **Educators and language content developers** who produce learning materials based on Chinese media.

---

### 💡 Example:

Original `.srt` block:

```
15
00:01:24,180 --> 00:01:27,000
我想吃火锅
```

Enhanced block after processing:

```
15
00:01:24,180 --> 00:01:27,000
我想吃火锅
wǒ xiǎng chī huǒ guō
أريد أن آكل الهوت بوت
```

---

### 📦 Dependencies:

Make sure to install the following packages before running the script:

```bash
pip install pypinyin googletrans==4.0.0-rc1
```

---

### 📝 Notes:

* This script assumes basic `.srt` formatting: subtitle index, timing, and one or more text lines per block.
* The Google Translate API via `googletrans` is unofficial and may be unstable or blocked in some regions.
* It can be easily extended to support other languages or output formats.

---
## 📘 وصف السكربت – `srt_pinyin.py`

### 🧩 **ما وظيفة هذا السكربت؟**

يقوم هذا السكربت المكتوب بلغة Python بتحسين ملفات الترجمة الصينية بصيغة `.srt` عن طريق إضافة:

* **الـPinyin** (النطق الصوتي بالحروف اللاتينية للكلمات الصينية).
* **الترجمة إلى اللغة العربية**.

لكل سطر يحتوي على نص صيني، يتم إدراج سطرين تحته:

1. سطر يوضح طريقة نطق الجملة بالصينية (Pinyin مع النغمات).
2. سطر يوضح معناها باللغة العربية.

يتم حفظ النتيجة في ملف `.srt` جديد مع الحفاظ على البنية الأصلية للملف (ترقيم الجمل، التوقيتات، والفواصل).

---

### 🛠️ **طريقة عمل السكربت – خطوة بخطوة**

1. **قراءة ملف الترجمة:**

   * يتم تحميل ملف `.srt` باستخدام ترميز `UTF-8`.
   * تتم قراءة الملف سطرًا بسطر، مع الحفاظ على الترقيم والفواصل.

2. **التعرف على النص الصيني:**

   * يستخدم السكربت تعبيرًا منتظمًا لاكتشاف وجود أحرف صينية في أي سطر: `[\\u4e00-\\u9fff]`.

3. **إنتاج الـPinyin:**

   * يتم استخدام مكتبة `pypinyin` لإنتاج النطق الكامل للجملة بالصينية مع النغمات (`Style.TONE`).
   * يتم تنسيق الناتج في سطر واحد سهل القراءة ويوضع أسفل الجملة الصينية.

4. **الترجمة إلى اللغة العربية:**

   * يتم استخدام مكتبة `googletrans` (غير رسمية) للحصول على الترجمة من الصينية إلى العربية.
   * يتم إدراج الترجمة أسفل سطر الـPinyin مباشرة.

5. **كتابة الملف الناتج:**

   * يتم حفظ الجمل المعالجة في ملف جديد بنفس تنسيق `.srt`.
   * يحافظ السكربت على الفواصل بين الجمل والترقيم الأساسي.

6. **تجنب الحظر من Google Translate:**

   * يتم استخدام `time.sleep(0.4)` لتقليل سرعة الطلبات وتفادي الحظر المؤقت من Google.

---

### 🎯 **لمن هذا السكربت مفيد؟**

هذا السكربت موجه لـ:

* 📘 **دارسي اللغة الصينية** الذين يرغبون في ربط النطق بالمعنى والنص الأصلي.
* 🎥 **محرري الترجمة** الذين يريدون تحسين ملفات `.srt` بمعلومات إضافية تعليمية.
* 🧑‍🏫 **المدرسين وصناع المحتوى التعليمي** الذين يعتمدون على مقاطع الفيديو لتعليم اللغة.

---

### 💡 مثال على النتيجة:

الملف الأصلي:

```
15
00:01:24,180 --> 00:01:27,000
我想吃火锅
```

بعد المعالجة:

```
15
00:01:24,180 --> 00:01:27,000
我想吃火锅
wǒ xiǎng chī huǒ guō
أريد أن آكل الهوت بوت
```

---

### 📦 المتطلبات:

قبل تشغيل السكربت، تأكد من تثبيت المكتبات التالية:

```bash
pip install pypinyin googletrans==4.0.0-rc1
```

---

### 📝 ملاحظات إضافية:

* يفترض السكربت تنسيقًا أساسيًا لملف `.srt` (ترقيم، توقيت، نص).
* مكتبة `googletrans` تعتمد على واجهة Google Translate غير الرسمية وقد تكون غير مستقرة أو محجوبة في بعض المناطق.
* يمكن تعديل السكربت بسهولة ليدعم لغات ترجمة أخرى أو تنسيقات ملفات مختلفة.

---

هل تحب أدمج الوصف الإنجليزي والعربي في ملف `README.md` جاهز وأرسله لك بصيغة قابلة للرفع؟


هل تحب دلوقتي أجهزه لك كملف `README.md`؟ وبعدها نضيف النسخة العربية تحته؟
