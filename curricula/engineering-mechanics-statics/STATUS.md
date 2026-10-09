# Engineering Mechanics — Statics | STATUS

- **التاريخ:** 2026-10-09؛ **المحرر:** ChatGPT، AI-assisted authoring؛ لا توجد موافقة بشرية مُسجلة.
- **الجمهور المؤكد:** طلاب **أولى هندسة** (تأكيد المستخدم في المحادثة).
- **المرحلة الحالية:** ثلاث **connected lesson drafts** جاهزة للمراجعة التحريرية الأولى؛ لم تتحول إلى scenes ولا lesson.json، فلا يجوز وصفها بأنها script-stage completed.
- **Branch:** curriculum/statics-ch01-working-drafts-20261009؛ **PR:** #4، Draft PR مفتوح للمراجعة.
- **الصوت والنشر والمعاينة:** لا TTS أو media أو timed cues أو release؛ preview SDK لم يصل بعد.

## الملفات الحالية

- course.json — تعريف المنهج وsource-access وlanguage policy.
- OUTLINE.md — خريطة مبدئية وفق مستوى أولى هندسة، ما زالت حدود الدروس غير معتمدة.
- references/SOURCE_REVIEW.md — محتوى 36 صفحة المصورة، locators وقيود الاستدلال ومشكلة جدول SI.
- drafts/CH01_WORKING_DRAFTS.md — **فهرس** للملفات الثلاثة؛ النسخة المجمعة القديمة في Git history فقط لتجنب مسودتين قابلتين للتحرير.
- drafts/LESSON_01_ENGINEERING_MECHANICS_MODELS.md — درس أول كامل؛ 3 independent questions + 3 feedback.
- drafts/LESSON_02_NEWTON_LAWS_WEIGHT.md — درس ثان كامل؛ 5 independent questions + 5 feedback.
- drafts/LESSON_03_UNITS_CONVERSIONS.md — درس ثالث كامل؛ 4 independent questions + 4 feedback.
- STATUS.md — هذا السجل.

## Coverage وقرار الحدود الأولي

1. L01: ماذا تدرس Mechanics وStatics/Dynamics، basic quantities، particle/rigid body/concentrated force. **Keep one** مع أجزاء فهم داخلية.
2. L02: Newton's first/second/third laws، gravitational attraction وmass/weight. **Keep with deliberate internal parts provisionally**؛ أعلى مخاطرة حمل معرفي في الجزء الخاص بالجاذبية/الوزن؛ اختبار طالب مبتدئ قد يبرر split قبل تثبيت IDs.
3. L03: SI/FPS، N من kg·m/s²، unit factors والتحويل والجمع المتسق. **Keep one**.
4. **12 سؤالًا مستقلًا و12 feedback بعد المحاولة**، مع English exam wording + Arabic conceptual support. أمثلة مؤلفة للتدريس وليست مسائل منقولة عن الكتاب.

## نزاهة المصدر والمراجعة

- PDF المصوّر (36 صفحة) في المحادثة، **ليس داخل GitHub**؛ access=reviewed-notes وليس available للمستودع. Chapter 1 PDF pp. 7–12 وChapter 2 جزئيًا؛ Chapters 3–7 فهرس فقط.
- صيغ Newton والجاذبية/الوزن ومعلومات الوحدات مستندة إلى النص المرئي. الأمثلة والأرقام التعليمية من إنشاء المؤلف؛ التفسيرات اللاحقة والافتراضات موضحة في المسودات.
- **عيب مصدر معلّق:** PDF p. 12 / printed p. 6، Energy/J formula «N/m» تختلف عن Work/J «N·m» في نفس الجدول؛ لم ننقل «N/m» كصيغة علمية صحيحة. يراجعها مدرس من الأصل قبل درس الطاقة.
- Source/science review، teaching/novice review، audio/listening/visual/runtime: **غير مختبرة بشريًا**؛ لا status = passed.

## الفحوص المنفذة فعليًا بعد الكتابة

- استرجاع source files السبعة من GitHub branch وتدقيق course.json.
- **9/9 فحوص بنيوية مخصصة نجحت**: JSON parses؛ مستوى أولى هندسة؛ كل ملف أقل من 300 سطر؛ وجود شرح متصل/خاتمة؛ توزيع 3+5+4 أسئلة؛ 3+5+4 feedback؛ الملف التجميعي أصبح فهرسًا فقط؛ source locators في كل درس؛ توثيق اختلاف جدول المصدر.
- لم تُشغّل npm test أو tools/quality.py أو cli.py validate: لا يوجد lesson.json/scenes، ولم نهيئ clone محلي للمستودع؛ هذه فحوص بنيوية للكتابة **لا تثبت** جودة العلم أو التدريس.

## ما التالي؟

1. تسليم المسودات للمراجع العلمي ومدرس أولى هندسة ومجموعة طلاب صغيرة إن أمكن؛ مراجعة مستوى المصطلحات ونطقها ومراجعة جميع الحسابات وتوثيق verdict للمصدر.
2. مراجعة انتقالات الأسئلة بدون answer leakage وتجربة الحمل المعرفي في L02؛ قرار keep/internal parts/split/merge مع سبب مدعّم بالملاحظة.
3. اعتماد حدود الدروس من مسؤول المنهج ثم إصدار IDs والترتيب ومراجع الأهداف في OUTLINE.
4. تحويل أول درس ثابت إلى lesson/scenes JSON، semantic units وstoryboards للمقاسين، ثم تشغيل checks الخاصة بمراحل الإنتاج. **لا TTS مدفوع ولا نشر تلقائي.**
