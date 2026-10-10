# STATUS — Physics I (Curriculum control)

- **آخر تحديث:** 2026-10-10
- **جمهور المنهج (تأكيد المستخدم):** **طلبة سنة أولى هندسة**، مع شرح مصري ومصطلحات/أسئلة امتحان بالإنجليزية؛ تفاصيل الكلية وخطة الامتحان غير معروفة.
- **Stage 00:** مكتمل، مصدر + خريطة كورس + اختيار B01.
- **Stage 01:** **مكتمل لـ B01 وحده**: قراءة مطبوع ص121–133؛ خريطة مفاهيم ومتطلبات؛ 3 مسودات مترابطة بنصوص وأمثلة وأسئلة مستقلة وإجابات مؤجلة، ليست دروسًا/مشاهد نهائية.
- **Stage 02:** **لم يبدأ**؛ ينتظر أمر الإنسان «كمل/next» للتقييم والتحرير العلمي/التربوي.
- **الـBlock النشط:** B01 — Solids and Elasticity. **B02:** مبدئي فقط؛ B03–B06 تتطلب صفحات غير مرفوعة.
- **نقطة الاستئناف:** B01 Stage 02 فقط، ثم توقف. تعديل/تعليق المستخدم يعيد مراجعة المرحلة الحالية بدل التقدم.
- **الفرع:** curriculum/physics-1-stage00-20261010 | **Draft PR:** #10. لا دمج إلى main ولا إصدار طلابي.

## Source access and scope
- **الموجود فعلًا:** S01 PDF ص5–11 = كتاب مطبوع ص121–133؛ S02 PDF ص1 = نسخة أوضح من المطبوع 124–125. فصول 1–7 والموائع غير موجودة إلا في الفهرس.
- **التحقق من مصدر B01:** عُرضت الصفحات الأصلية فعلًا في Stage 01. القيم غير الواضحة في التمارين المطبوعة 130–133 لم تُختلق؛ كل الأمثلة والأرقام في المسودات مؤلفة ومعلنة كذلك.
- **بصمات الأصلين:** محسوبة فعلًا من ملفات PDF المرفوعة؛ موثقة في SOURCE_MANIFEST. **لا يُفترض** إثبات تطابق البايتات مع كل تنزيل لاحق من Drive.
- **حفظ المصدر:** الأصول كانت متاحة عبر Google Drive connector خلال Stage 00، لكن metadata أظهرت مشاركة anyone-with-link مع صلاحية writer؛ يُطلب تشديد الصلاحيات والتحقق من استرجاع مستقبلي. لا روابط/صور كتب داخل المستودع العام.
- **الحقوق:** إعادة توزيع المسح ضوئيًا غير مرخّصة على حد علمنا؛ لن تُنشر نسخ الصفحات في GitHub.

## Deliverables — B01 Stage 01
- blocks/B01/CONCEPT_MAP.md
- blocks/B01/drafts/WORKING-01-solid-structure-and-deformation.md
- blocks/B01/drafts/WORKING-02-tensile-young-hooke.md
- blocks/B01/drafts/WORKING-03-shear-bulk-and-engineering-transfer.md
- OUTLINE.md وcourse.json وreferences/SOURCE_COVERAGE.md وblocks/B01/STATUS.md محدثة.
- **لا توجد:** stable lesson IDs، lessons/*.json، scenes/*.json، jobs/media/timing، معاينة SDK أو أي نشر.

## Actual sanity checks and remaining review
- تمت مراجعة الصيغ العددية الأساسية بالأمثلة المؤلفة (Stress/strain, Young/k, Shear, Bulk) حسابيًا؛ لا يمثّل ذلك تدقيقًا علميًا مستقلًا.
- Source/teaching human review: **untested**؛ audio/timing/visual/runtime: **untested**.
- Stage script validation غير قابل للتشغيل بعد: لا دروس نهائية ولا scenes (عن قصد).
- المطلوب في Stage 02: مراجعة علمية وتربوية دقيقة، وخاصة التمييز بين stiffness/strength؛ تفسير منحنى stress–strain؛ دقة رمز/إشارة Bulk؛ الشرح المسموع الطبيعي وعلاقة عدد الأهداف بعبء التعلم.

**Awaiting human:** «كمل» = B01 Stage 02 critique/rewrite ثم STOP؛ أو تعليقات على مسودات Stage 01 لإصلاحها قبل أي انتقال.
