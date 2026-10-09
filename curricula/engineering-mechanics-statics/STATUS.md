# Engineering Mechanics — Statics | STATUS

- **التاريخ:** 2026-10-09.
- **المحرر:** ChatGPT (AI-assisted preliminary authoring)؛ لا مراجع بشري مسجل.
- **المرحلة الحقيقية:** curriculum setup + provisional outline + connected Chapter 1 working drafts + editorial self-critique. **ليست script stage ولا audio**.
- **الفرع:** `curriculum/statics-ch01-working-drafts-20261009`.
- **النشر / runtime:** لم يحدث نشر، SDK المعاينة غير موجود بالمشروع، ولم يُشغّل صوت أو TTS.

## الملفات في هذا الفرع

- `course.json`: تعريف المنهج وسياسة اللغة وحدود الوصول للمصدر.
- `OUTLINE.md`: تخطيط أولي بثلاث وحدات عمل في الفصل الأول، وباقي الفصول وفق حدود ما هو متاح.
- `references/SOURCE_REVIEW.md`: خريطة صفحات الملف المصوّر مقابل صفحات الكتاب، حدود الاستدلال ومخاطر النقل.
- `drafts/CH01_WORKING_DRAFTS.md`: ثلاثة نصوص شرح متصلة أصلية، تطبيقات موجهة، ستة أسئلة مستقلة مع feedback مفصول، whole-draft critique وقرار حدود مبدئي.
- `STATUS.md`: هذا السجل.

## حدود المصادر

- PDF المرفق في المحادثة (36 صفحة) راجعناه بصريًا؛ **الملف غير محفوظ في GitHub** لحين التحقق من حقوق التوزيع وطريقة توفيره للمراجع.
- Chapter 1 متن متاح (PDF pp. 7–12)، Chapter 2 متاح جزئيًا (PDF pp. 14–36)، Chapters 3–7 فهرس فقط.
- وصف source `reviewed-notes` متعمد، ولا يعني وصولًا دائمًا للكتاب.
- جميع الأمثلة الحسابية وأمثلة النقل مولّدة من فريق التأليف وليست حلولًا مقتبسة من الكتاب.

## فحوص ومراجعات

- معاينة مرئية للمصدر: تمت للصفحات اللازمة لمسودات Chapter 1؛ يلزم تدقيقها مع مدرس.
- AI editorial critique: مكتوب في نهاية مسودات CH01، **لا يُعد اعتمادًا علميًا أو بشريًا**.
- JSON/format and file-length checks: ستُسجل نتيجتها في PR بعد القراءة من الفرع.
- `npm test` / `npm run check` / `cli.py validate --stage script`: **لم تُشغّل** في هذه المرحلة؛ لا توجد `lesson.json` أو مشاهد كي يُطبّق عليها script validation. البيئة المحلية لا تستطيع استنساخ GitHub؛ يجري تحرير الملفات مباشرة عبر GitHub connector.
- source review: awaiting human evidence؛ teaching review: awaiting novice/instructor feedback؛ audio/timing/visual/runtime: untested.

## القرار المبدئي وحدوده

- C1-A: درس واحد بأجزاء داخلية قصيرة.
- C1-B: درس واحد بثلاث نقاط توقف، **مرشح للتقسيم بعد اختبار حمله المعرفي**.
- C1-C: درس واحد.
- لا stable lesson IDs، ولا approved lesson order، ولا scenes أو review.json مع passed statuses حتى يعتمد المسؤول هذا التقسيم.

## الخطوة التنفيذية التالية

1. مراجعة مدرس Statics للنصوص والمعادلات والأسئلة؛ مراجعة طالب مبتدئ للانتقالات والحمل المعرفي، خصوصًا C1-B.
2. تسجيل قرارات keep / internal-parts / split وسببها، مع تحديث الافتتاحيات/التقييمات لو تغير التقسيم.
3. تثبيت IDs والأهداف والترتيب في OUTLINE مع مسؤول المنهج.
4. تحويل أول درس معتمد إلى scenes وstoryboards بالمقاسين، ثم تشغيل draft/script validations. بعد مراجعة حقيقية فقط يجوز بحث pilot صوت؛ **لا طلب مدفوع الآن**.
