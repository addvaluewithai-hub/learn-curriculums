# Chapter 1 — فهرس مسودات الدروس الثلاثة

**الجمهور:** طلاب أولى هندسة (تأكيد المستخدم).  
**المرحلة:** ثلاث مسودات شرح متصلة، غير مقسّمة إلى scenes وغير معتمدة بعد.  
**المرجع:** ملف Engineering Mechanics [Statics] المصور، PDF pp. 7–12 / printed pp. 1–6.

| ترتيب العمل (غير صادر كـ stable ID) | الملف المعتمد حاليًا للمراجعة | الصفحات | الأسئلة المستقلة |
|---|---|---|---:|
| الأول — مدخل الميكانيكا والنماذج | [LESSON_01_ENGINEERING_MECHANICS_MODELS.md](LESSON_01_ENGINEERING_MECHANICS_MODELS.md) | PDF pp. 7–9 | 3 |
| الثاني — قوانين نيوتن والجاذبية والوزن | [LESSON_02_NEWTON_LAWS_WEIGHT.md](LESSON_02_NEWTON_LAWS_WEIGHT.md) | PDF pp. 9–11 | 5 |
| الثالث — الوحدات والتحويلات | [LESSON_03_UNITS_CONVERSIONS.md](LESSON_03_UNITS_CONVERSIONS.md) | PDF pp. 11–12 | 4 |

كل ملف درس فيه: هدف واضح، جسور مفاهيمية، **نص مصري متصل مكتمل**، أمثلة مؤلفة للشرح، أسئلة English with Arabic support قبل المحاولة، feedback إنجليزي/عربي بعد المحاولة، خاتمة، نقد تعليمي/علمي، وإشارات المصدر.

## ترتيب الدروس والحمل المعرفي

- **Lesson 1:** keep as one with short conceptual parts: mechanics → quantities → idealizations.
- **Lesson 2:** **provisional internal parts**, with a possible future split before gravitation/weight. اختبر فهم طلاب أولى هندسة للثلاثة قوانين قبل تثبيت القرار؛ الإطالة وحدها لا تفرض split.
- **Lesson 3:** keep as one: معنى نظام الوحدات → التحويل → فحص الاتساق.
- العلاقة بينهم صريحة؛ الوحدات الأساسية تُقدَّم بالقدر الكافي قبل صيغ Newton ثم تُعمَّق في Lesson 3.

## نزاهة المراجعة

- الملفات الثلاثة هي **مصدر المسودات الحالي الوحيد**. مسودات C1-A/B/C المجمّعة السابقة محفوظة في Git history فقط حتى لا ننشئ نسختين مستقلتين قابلتين للتحرير من كلام الدرس.
- مصدر النص فعليًا Chapter 1 في ملف PDF؛ الأمثلة والتمارين المصاغة جديدة وليست مقتطفات منه.
- رُصد عدم اتساق ظاهر في جدول وحدات **Energy** بـ PDF p. 12: «N/m» في صف مقابل «J = N·m» في صف Work. التوثيق في الدرس الثالث وSOURCE_REVIEW؛ يحتاج مدرسًا للتأكد من طبعة المصدر. لا يُدرّس الشكل المختلف عليه للطلبة.
- **إجمالي الأسئلة:** 12 سؤالًا مستقلًا و12 feedback clips مخططة (وليست ملفات صوتية). لا تقييم بشري، لا \`passed\`، لا audio أو storyboard نهائي.
- تُثبَّت الدروس وIDs/الـOUTLINE بعد مراجعة الحدود؛ لا تنشئ \`lesson.json\` أو scenes قبلها.

## المرحلة التالية

Review by Statics instructor + first-year student → accept/revise lesson boundaries and detailed text → issue stable lesson IDs/order → scene decomposition, storyboards (16:9 and 9:16), structural validation → later listening pilot with explicit authorization.
