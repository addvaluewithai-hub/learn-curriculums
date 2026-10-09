# Stage 03 final connected teaching script — Real Numbers, Order & Sets
**Stable lesson ID:** \`em1-prelim-real-sets\` | **B01 order:** 1 of 5 | **Title:** الأعداد الحقيقية وخط الأعداد والمجموعات
**Source:** \`abd-el-salam-math-i-scan\`, printed pp. 1–5, PDF pp. 4–6; inspected historically for Stage 01. Examples and questions here are *newly authored*, not copied book exercises.
**Prerequisites:** counting, four operations, fractions and the idea of a point on a line (established/quick bridge).
**Taught targets:** rational/irrational number classification; position/order on the real line; set elements, empty set, membership, union and intersection.
**Deferred:** interval notation and solving inequalities (next lesson); complex numbers (later/unneeded here).
**Editorial boundary:** one coherent lesson with two short learning parts, not two issued lessons. Each has its own consolidation. No scene/audio markup; headings and directions below are not spoken.

## Complete connected spoken script

تخيل إننا بنحاول نرسم خريطة لكل الأعداد اللي ممكن نقابلها في حسابات أولى هندسة. على خط الأعداد هتحط الصفر في النص، واحد واتنين ناحية اليمين، وسالب واحد وسالب اتنين ناحية الشمال. كل ما نمشي يمين، القيمة بتكبر. عشان كده سالب اتنين أكبر من سالب خمسة؛ لأن مكانه على الخط على يمينه. اسم الخط ده **Real Number Line**، وكل عدد حقيقي ليه نقطة بتمثله عليه، حتى لو مش عددًا صحيحًا.

إحنا مش بنجمع الأعداد في صندوق واحد وخلاص؛ بنرتبها في مجموعات على حسب طبيعتها. أعداد العد واحد واتنين وتلاتة اسمها **Natural Numbers**. في مراجع بتضيف الصفر وفي مراجع لأ، فلو السؤال اعتمد على الاصطلاح هنوضحه. الأعداد الصحيحة **Integers** بتضيف الصفر والسوالب، لكن مفيهاش كسر زي تلاتة على أربعة. لما نقدر نكتب العدد في صورة $\frac{p}{q}$، بحيث $p$ و$q$ عددان صحيحان و$q\ne0$، بنسميه **Rational Number** أو عدد نسبي. مثالنا سالب خمسة على اتنين، أو الصفر اللي نقدر نكتبه صفر على واحد.

خد بالك من الفخ ده: عدد عشري طويل مش لازم يكون غير نسبي. الواحد على تمانية يساوي صفر فاصلة مية خمسة وعشرين؛ التمثيل العشري هنا انتهى. والواحد على تلاتة فيه تكرار مستمر، لكنه برضه نسبي لأننا كتبناه ككسر. مقابل ده، **Irrational Number** زي $\sqrt{2}$ ماينفعش يساوي كسر عددين صحيحين. تمثيله العشري لا ينتهي بنمط دوري. والعدد غير النسبي لسه عدد حقيقي؛ موجود على خط الأعداد. أما $\sqrt{-1}$ فمش عددًا حقيقيًا، ومش هندخله هنا في تصنيف الأعداد الحقيقية.

تعال نبص على المقارنة. لما نقول $a<b$ فده معناه إن مكان $a$ على الشمال من $b$. علامة $a\le b$ بتسمح كمان بالمساواة. ولو أضفت نفس العدد للطرفين هيفضل الترتيب زي ما هو. ولو ضربت في عدد سالب، الاتجاه بيتعكس، لأن الضرب في سالب بيعكس أماكن الأعداد حول الصفر. هنستعمل القاعدة بدقة في درس المتباينات، لكن دلوقتي عايزك تربطها بمعنى الخط.

دلوقتي خلينا نجرب سؤال عن تصنيف الأعداد بعيدًا عن أمثلة الشرح. اكتب إجابتك وسبب مختصر قبل ما نفتح التفسير.

## Independent attempt EM1-RS-Q1 — question only
**English exam question:** Classify each as rational or irrational: $-\frac{9}{5}$, $\sqrt{7}$ and $0.375$. Explain briefly.
**Arabic spoken support:** صنف سالب تسعة على خمسة، وجذر سبعة، وصفر فاصلة تلاتة سبعة خمسة، واذكر السبب.
**Attempt direction (non-spoken):** allow written response; do not show answer until attempt is submitted.

### Post-attempt explanatory feedback EM1-RS-Q1 — separate
**English model answer:** $-\frac95$ is rational; $\sqrt7$ is irrational; $0.375=\frac38$ is rational.
**Egyptian Arabic spoken explanation:** سالب تسعة على خمسة مكتوب ككسر صحيحين، والجذر التربيعي لسبعة غير نسبي لأن سبعة مش مربعًا كاملًا لعدد صحيح، والصفر فاصلة تلاتة سبعة خمسة عشري منتهٍ ونقدر نكتبه تلاتة على تمانية. يبقى إحنا صنفنا بالخاصية الرياضية، مش بطول الرقم أو إشارته.

## Connected spoken continuation — sets and their operations

إحنا لسه بنتكلم عن أعداد، لكن ساعات السؤال مش عايز رقم واحد؛ عايز مجموعة أرقام تحقق وصف معين. هنا هنستخدم **Set**، يعني مجموعة. مثلًا $A=\{1,3,5\}$ فيها تلاتة عناصر. بنقول $3\in A$ لما تلاتة تنتمي للمجموعة، و$2\notin A$ لما اتنين مش فيها. ترتيب عناصر المجموعة مش مهم؛ $\{5,1,3\}$ هي نفس $A$. وكمان تكرار الرقم في الكتابة مش بيزود عدد العناصر.

هنعرف عمليتين هنستخدمهم طول السنة. **Union** أو الاتحاد $A\cup B$ معناه كل العناصر اللي في $A$ **أو** في $B$ أو فيهما معًا، من غير تكرار. و**Intersection** أو التقاطع $A\cap B$ معناه العناصر الموجودة في الاتنين **في نفس الوقت**. لو $A=\{1,3,5\}$ و$B=\{3,4,5\}$، الاتحاد هيضم واحد وتلاتة وأربعة وخمسة، لكن التقاطع هيضم تلاتة وخمسة بس. لما المجموعتين مايتقاطعوش، النتيجة اسمها **Empty Set** أو المجموعة الخالية، ورمزها $\varnothing$؛ مش هي المجموعة اللي فيها العدد صفر، دي مجموعة مفيهاش أي عنصر.

ولو العناصر كتير، نقدر نعرّف المجموعة بشرط بدل ما نعدها. مثال: $\{x\in\mathbb R:x>0\}$، وده معناه الأعداد الحقيقية الموجبة. علامة $\mathbb R$ بتحدد مجموعة الأعداد اللي بنختار منها، والشرط $x>0$ بيحدد مين اللي يدخل. هنحوّل نفس الفكرة لفترات لما نبدأ الدرس الجاي.

خلينا نختبر العمليات بمجموعات جديدة ونشوف الفرق بين «أو» و«و».

## Independent attempt EM1-RS-Q2 — question only
**English exam question:** Let $A=\{0,2,5,7\}$ and $B=\{1,2,6,7\}$. Find $A\cup B$, $A\cap B$, and decide whether $5\in B$.
**Arabic spoken support:** عندك مجموعتين إيه وبي؛ أوجد الاتحاد والتقاطع، وبعدين حدد هل خمسة عنصر في بي.
**Attempt direction (non-spoken):** no overlap coloring or model answer until attempt.

### Post-attempt explanatory feedback EM1-RS-Q2 — separate
**English model answer:** $A\cup B=\{0,1,2,5,6,7\}$; $A\cap B=\{2,7\}$; $5\notin B$.
**Egyptian Arabic spoken explanation:** الاتحاد بيجمع كل العناصر من المجموعتين من غير تكرار، والتقاطع بيحتفظ باتنين وسبعة لأنهم مشتركان. خمسة موجودة في إيه بس مش في بي. كلمة عنصر معناها موجود جوه المجموعة المطلوبة نفسها، مش أي مجموعة في السؤال.

## Final independent transfer — number order and empty set

لسه عندنا نقطة مشتركة بين جزئي الدرس: الخط بيرتب أعداد، والمجموعات بتوصف اختياراتنا منها. جرّب السؤال اللي جاي لوحدك، وخلّي بالك إن المجموعة الخالية مش هي الصفر.

## Independent attempt EM1-RS-Q3 — question only
**English exam question:** Arrange $-\sqrt{3}$, $-2$ and $0$ in increasing order. If $C=\{-1,2\}$ and $D=\{0,3\}$, find $C\cap D$.
**Arabic spoken support:** رتب سالب جذر تلاتة وسالب اتنين والصفر من الأصغر للأكبر، وأوجد تقاطع سي ودي.
**Attempt direction (non-spoken):** written; do not reveal approximations or set answer early.

### Post-attempt explanatory feedback EM1-RS-Q3 — separate
**English model answer:** $-2<-\sqrt3<0$; $C\cap D=\varnothing$.
**Egyptian Arabic spoken explanation:** جذر تلاتة حوالي واحد فاصلة سبعة تلاتة، فسالبه أكبر من سالب اتنين وأصغر من الصفر. والمجموعتين مش مشتركتين في أي عنصر، فالتقاطع هو المجموعة الخالية. الجمع بين الترتيب والتقاطع هنا بيفكرنا إن كل رمز لازم نربطه بمعناه.

## Closing spoken recap

النهارده عرفنا إن كل عدد حقيقي ليه مكان على خط الأعداد، وإن النسبي ينكتب ككسر من عددين صحيحين ومقام غير صفر، وإن غير النسبي برضه حقيقي لكنه مش كسر بالشكل ده. وعرفنا المجموعات، والاتحاد بمعنى «أو»، والتقاطع بمعنى «و». المرة الجاية هنحوّل المناطق اللي على خط الأعداد إلى **Intervals**، ونحل متباينات ونكتب إجابتها كمجموعات صحيحة بدل رقم واحد.

## Rough visual suggestions — NON production assets
Number line and irrational location; nested number-family labels; separate union and intersection Venn visuals; delayed answer display only after each independent attempt. No timings, scenes or visuals commissioned.
