# Stage 03 final connected teaching script — Absolute Value as Distance
**Stable lesson ID:** `em1-prelim-absolute-value` | **B01 order:** 3 of 5 | **Title:** القيمة المطلقة ومعادلاتها ومتبايناتها
**Source:** `abd-el-salam-math-i-scan`, printed pp. 9–12, PDF pp. 8–9. Classroom examples and questions independently authored.
**Prerequisites:** sign of real numbers, real-line distance, open/closed interval notation and linear inequalities (B01 lessons 1–2).
**Taught targets:** explain $\lvert x-a\rvert$ as real-line distance and piecewise magnitude; solve simple absolute-value equations, inside/outside inequalities and handle zero/negative thresholds; verify triangle inequality numerically.
**Deferred:** absolute values within more advanced rational/polynomial expressions; differentiation.
**Teaching boundary:** keep one lesson, with connected distance → equality → inequality → properties internal learning turns. No production scene cuts, stable audio clips or timing.

## Complete connected spoken script — discover the distance meaning

عايزك تتخيل إن فيه نقطة اسمها الصفر على خط الأعداد، وإنت واقف عندها. لو مشيت أربعة خطوات ناحية اليمين، بُعدك عن الصفر أربعة. ولو مشيت أربعة ناحية الشمال، برضه بُعدك أربعة. الاتجاه مختلف، لكن **المسافة** نفسها مش سالبة. ده معنى **Absolute Value** أو القيمة المطلقة: $|4|=4$ و$|-4|=4$، والصفر قيمته المطلقة صفر.

لو $x$ عدد حقيقي موجب أو صفر، هتلاقي $|x|=x$. ولو $x$ سالب، $|x|=-x$؛ وخد بالك إن التعبير $-x$ هنا بيطلع موجب لأن إكس نفسها سالبة. يعني لو إكس بسالب ستة، سالب إكس تساوي موجب ستة. ده سبب إن القيمة المطلقة ما ينفعش تساوي عددًا سالبًا. وفيه كتابة مفيدة: $|x|=\sqrt{x^2}$ مع استخدام الجذر التربيعي الرئيسي غير السالب. ما ينفعش نكتب بدلها إن $\sqrt{x^2}=x$ لكل الأعداد من غير شرط، لأن ده هيغلط عند السالب.

ونقدر نقيس المسافة مش بس عن الصفر. التعبير $|x-a|$ معناه المسافة بين موضع إكس والنقطة إيه. مثلًا $|x-4|=3$ بيقول إن إكس بعيدة عن أربعة بمسافة تلاتة. على الخط فيه نقطتان: واحد ناحية الشمال، وسبعة ناحية اليمين. الجبر بيترجم ده لفرعين: $x-4=3$ **أو** $x-4=-3$. وبالتالي $x=7$ أو $x=1$. الفرعين بديلان مش شرط يحصلوا معًا.

دلوقتي جرّب معادلة مختلفة؛ هدف السؤال إنك تفتكر ليه لازم نفحص الفرعين.

## Independent attempt EM1-AV-Q1 — question only
**English exam question:** Solve $|3x+1|=8$ over the real numbers.
**Arabic spoken support:** حل معادلة القيمة المطلقة لتلاتة إكس زائد واحد تساوي تمانية على الأعداد الحقيقية.
**Attempt direction (non-spoken):** hide both branches and final roots until response.

### Post-attempt explanatory feedback EM1-AV-Q1 — separate
**English model answer:** $3x+1=8$ or $3x+1=-8$; hence $x=\frac73$ or $x=-3$.
**Egyptian Arabic spoken explanation:** اللي جوه القيمة المطلقة ممكن يكون موجب تمانية أو سالب تمانية، لأن الاتنين بعدهم عن الصفر تمانية. نحل الفرع الأول فنلاقي سبعة على تلاتة، والتاني فنلاقي سالب تلاتة. جرب كل قيمة في المعادلة الأصلية، هتلاقي القيمة المطلقة فعلًا تساوي تمانية.

## Connected spoken continuation — inside and outside regions

خلينا نبدل علامة المساواة بعلامة مقارنة. لو طلبنا $|x-4|<3$، إحنا عايزين الأعداد اللي تبعد عن أربعة بأقل من تلاتة. يعني المنطقة اللي **بين** واحد وسبعة، ومن غير الطرفين: $1<x<7$. ونقدر نطلعها جبريًا: $-3<x-4<3$، وبعد إضافة أربعة للأجزاء كلها نوصل لنفس الحل. أما لو المسافة **أكبر** من تلاتة، يعني $|x-4|>3$، هنختار بره المنطقة: $x<1$ **أو** $x>7$. وده معناه اتحاد فترتين بعيدتين.

في الحالات دي كنا بنقارن المسافة بعدد **موجب**. لازم نقف عند الشرط ده: هل $|x-4|=-2$ ممكن تحصل؟ لأ، لأن المسافة مش سالبة. وهل $|x-4|<-2$ ممكن؟ برضه لأ. لكن $|x-4|\ge0$ صحيحة لكل إكس حقيقية. قبل فتح الفرعين، شوف الحد اللي على الناحية التانية وهل يسمح بحلول أصلاً.

خلينا نحل متباينة فيها معامل لإكس: $|2x-6|\le4$. معناها إن المقدار جوه القيمة المطلقة محصور بين سالب أربعة وموجب أربعة، فبنكتب $-4\le2x-6\le4$. نضيف ستة للأطراف التلاتة: $2\le2x\le10$. وبالقسمة على اتنين: $1\le x\le5$. هنضم الواحد والخمسة لأن العلامة بتسمح بالمساواة. لو جربت إكس تساوي خمسة، المقدار جوه القيمة المطلقة أربعة بالضبط، يعني الحد فعلاً داخل الحل.

الاختبار الجاي بيخليك تستخدم المعنى ده على حالة متباينة مختلفة. حل الأول وبعدين اقرأ تفسير الطرفين.

## Independent attempt EM1-AV-Q2 — question only
**English exam question:** Solve $|2x-3|\le7$ and express the real solution set in interval notation.
**Arabic spoken support:** حل القيمة المطلقة لاتنين إكس ناقص تلاتة أصغر من أو تساوي سبعة، واكتب الحل في صورة فترة.
**Attempt direction (non-spoken):** don't reveal inequality transformation or endpoint inclusion before attempt.

### Post-attempt explanatory feedback EM1-AV-Q2 — separate
**English model answer:** $-7\le2x-3\le7$, so $-4\le2x\le10$ and $-2\le x\le5$; solution $[-2,5]$.
**Egyptian Arabic spoken explanation:** نكتب اللي جوه القيمة المطلقة بين سالب سبعة وموجب سبعة، ونضيف تلاتة للأطراف، وبعدها نقسم على اتنين الموجب. الناتج من سالب اتنين لحد خمسة، والطرفان داخلان. طريقة الفترات هنا مبنية على المسافة، مش قاعدة محفوظة من غير سبب.

## Connected spoken continuation — useful properties and a misconception

من خواص القيمة المطلقة إن $|ab|=|a||b|$؛ مقدار حاصل الضرب يساوي حاصل ضرب المقدارين. وفيه خاصية اسمها **Triangle Inequality** أو متباينة المثلث: $|a+b|\le|a|+|b|$. ليه مش مساواة دايمًا؟ تخيل حركة خمسة خطوات يمين وبعدين تلاتة شمال؛ بعدك النهائي عن البداية اتنين، لكن مجموع المسافتين اللي مشيتهما تمانية. فـ **مقدار المحصلة مايزيدش عن مجموع المقدارين**.

فيه طلبة بتسمع كلمة متباينة المثلث فتفتكر لازم مجموع الأطوال يساوي المسافة النهائية. لكن المساواة بتحصل بس في بعض الحالات، زي الحركتين في نفس الاتجاه على الخط. السؤال اللي جاي هيقارن قيمتين ويأكد معنى علامة أصغر من أو يساوي.

## Independent attempt EM1-AV-Q3 — question only
**English exam question:** Let $a=-6$ and $b=2$. Compute $|a+b|$ and $|a|+|b|$. Does the triangle inequality hold, and is it an equality for these values?
**Arabic spoken support:** لو إيه سالب ستة وبي اتنين، احسب القيمة المطلقة لمجموعهم ومجموع القيمتين المطلقـتين. تحقق من متباينة المثلث، وهل حصلت مساواة؟
**Attempt direction (non-spoken):** model calculations shown only as feedback.

### Post-attempt explanatory feedback EM1-AV-Q3 — separate
**English model answer:** $|a+b|=|-4|=4$, while $|a|+|b|=6+2=8$. Thus $4\le8$ holds; equality does not hold.
**Egyptian Arabic spoken explanation:** سالب ستة زائد اتنين يساوي سالب أربعة، ومقداره أربعة. لكن لو أخدنا مقدار كل واحدة لوحدها يبقى ستة زائد اتنين تمانية. أربعة أقل من تمانية، فمتباينة المثلث صحيحة من غير ما تتحول لمساواة. لو كتبت مساواة دايمًا هتخالف معنى المسافة.

## Closing spoken recap

النهارده القيمة المطلقة بقت بالنسبة لنا **مسافة**: ما بتطلعش سالب، والمعادلة مع حد موجب ممكن تدينا موضعين على الخط، والمتباينة بأقل من بتختار **الداخل**، وبأكبر من بتختار **الخارج**. اتأكدنا كمان إن شرط الحد الموجب مهم، وإن متباينة المثلث علامة أصغر من أو يساوي، مش مساواة دائمًا. المرة الجاية هنشتغل على إشارات حاصل ضرب عوامل، وبدل ما نسأل عن المسافة هنسأل: حاصل الضرب موجب فين وسالب فين؟

## Rough visual suggestions — NON production assets
Point-to-point distance arrows, two roots for one equal distance, inside/outside shading, zero-threshold example and two opposed moves for triangle inequality. Attempts remain answer-free until feedback.
