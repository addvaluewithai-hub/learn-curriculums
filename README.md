# Learn Curriculums — ورشة إنتاج المناهج

ابدأ كتابة المنهج والاسكربتات والـstoryboards وإنتاج الصوت والتوقيتات الآن.
**المعاينة والمحرّك لم يُضافا بعد.** `preview-sdk` فولدر مستقل لدمج الحزمة المشتركة لاحقًا.
لا حسابات، لا قاعدة بيانات، لا حفظ طالب، ولا نشر تلقائي من هنا.

## البداية

المطلوب: Python 3.11+ فقط. npm اختصار للأوامر؛ لا packages تحتاج تثبيتًا حاليًا.
إرسال الصوت يحتاج صلاحية GitHub على gemini-tts؛ gh أو connector مأذون يرسل الـpayload.

```bash
python3 tools/cli.py course-new --id biology-basics --title "أساسيات الأحياء"
python3 tools/cli.py lesson-new --course biology-basics --id bio-cells --order 1 --title "الخلية"
python3 tools/cli.py validate
```

املأ course.json بالمصادر وسياسة اللغة، وOUTLINE.md بتسلسل الأهداف. **قبل تأليف المشاهد بشكل نهائي** اعمل خريطة للمفاهيم والمتطلبات السابقة، واكتب شرح متصل، وانقده من منظور الطالب والدقة العلمية والإنجليزي، وصلّح فجوات الفهم. فكر في الرسوم خلال التأليف، لكن ثبّت المشاهد والـsemantic units بعد مراجعة النص.
راجع [منهجية التدريس](instructions/teaching.md) و[العقد](instructions/contract.md). الفحص الافتراضي يسمح بمسودة؛ `script` يفحص اكتمال البنية ولا يعتمد جودة التدريس. بعد التقسيم، نصوص المشاهد هي المصدر التشغيلي؛ بلاش نسختين مستقلتين من الكلام.

```bash
npm run validate -- --course biology-basics --lesson bio-cells --stage script
npm run audio:prepare -- --course biology-basics --lesson bio-cells --clip N01 --take t01
```

الأمر الثاني يكتب ملف طلب فقط. استخدم المسار الذي يعيده:

```bash
npm run audio:dispatch -- --job curricula/biology-basics/lessons/bio-cells/jobs/JOB_ID.json
```

ده dry-run. إضافة --send تبدأ طلبًا مدفوعًا بعد مراجعة الـpilot وسياسة الفريق.
راجع [الصوت والاستلام](instructions/audio.md)؛ لا تعيد نفس الطلب لأنه ما زال queued.

## التنظيم والملكية

| المسار | المسؤولية | صاحبه |
|---|---|---|
| curricula | كل منهج ومصادره ودروسه ومكوناته | فريق المنهج |
| instructions | الشرح والبورد والصوت والعقد والتسليم | مسؤول طريقة الإنتاج |
| .agents/skills | Skill واحدة تقرأ التعليمات | مسؤول طريقة الإنتاج |
| tools | إنشاء وفحص وصوت وتصدير | مسؤول أدوات الإنتاج |
| preview-sdk | مكان المعاينة لاحقًا؛ README فقط الآن | مسؤول المحرّك |
| tests | اختبارات الأدوات وحالات الفشل | مسؤول الأدوات |
| dist | حزم تسليم مولدة لا تعدل يدويًا | أدوات الإنتاج |

لا مناهج حقيقية نُسخت من Learn في هذه الدفعة، ولا أمثلة وهمية داخل الفهرس الحقيقي.
يتكرر نفس تنظيم الدرس: metadata، scenes، media، jobs، review وSTATUS؛ لا أسماء دروس داخل الأدوات.
التسجيلات والأصول تبقى تحت الدرس الذي يملكها.

## بداية العمل مع الـAI

> اقرأ AGENTS.md وSkill produce-learn-lesson. حدد الدرس من OUTLINE بمعرّفه الثابت، وابنِ Concept Map وخطة فهم؛ اكتب Master Draft متصلًا، واعمل نقدًا علميًا وتعليميًا ولغويًا وأصلح العيوب. بعد كده قسّم النص المستقر إلى scenes وstoryboards بالمقاسين، وافصل السؤال عن الإجابة والـFeedback. شغّل الفحوص المناسبة ومنها `--stage script`، وسجّل ما اتنفذ بالفعل والحدود في STATUS، وافتح PR، من غير توليد صوت مدفوع.

لو أداة AI لا تكتشف Skills تلقائيًا، اقرأ `.agents/skills/produce-learn-lesson/SKILL.md` مباشرة.
لا نفترض أن «3» يعني نفس القانون أو ID في كل منهج.

## مراجعة وتسليم

```bash
npm test
npm run check
npm run validate
npm run export -- --course biology-basics --stage script
```

النتيجة تحت dist/handoff: source كامل وhandoff.json بالملفات والـhashes والمرحلة.
media يفحص التسجيلات، وtimed يفحص كمان anchors المرتبطة بالكلمات.
**دي مش حزمة جاهزة للنشر على الطالب:** ينقصها بناء المحرّك والمعاينة والتحقق والاستيراد المعتمد.
نجاح tests لا يثبت صحة المحتوى أو النطق. نجاح `validate --stage script` مش اعتماد تربوي أو علمي؛ المراجعات تحتاج أدلة منفصلة.
الشغل الجماعي: branch/PR لكل درس، ومعرف وترتيب متفق عليهما؛ تغييرات الخطة والمصادر لمسؤول المنهج.
CI يفحص تضارب الهويات والترتيب. STATUS القديم ليس قفلًا دائمًا.
الكود اليدوي والتعليمات تحت 300 سطر؛ timestamps/تسجيلات المصنع مخرجات لا تختصر يدويًا لهذا الحد.
