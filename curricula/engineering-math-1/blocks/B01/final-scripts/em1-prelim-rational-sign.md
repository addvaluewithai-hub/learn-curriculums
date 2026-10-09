# Stage 03 final connected teaching script — Rational Inequalities & Combined Conditions
**Stable lesson ID:** \`em1-prelim-rational-sign\` | **B01 order:** 5 of 5 | **Title:** المتباينات الكسرية وتقاطع الشروط
**Source:** \`abd-el-salam-math-i-scan\`, printed pp. 13–18, PDF pp. 10–12 (the photographed instruction spans polynomial/rational inequalities; precise split into two *student lessons* is pedagogical). Source pp. 19–20, PDF p. 13, are Exercises (1) and **not transcribed**.
**Prerequisites:** completed B01 sign chart lesson 4, sets/intervals from lessons 1–2 and linear inequality constraints; rational arithmetic with nonzero denominators (bridge).
**Taught targets:** distinguish numerator zeros from denominator exclusions; solve rational sign regions; retain exclusions after factor cancellation; intersect multiple conditions and express the final union of solution intervals.
**Deferred:** function-domain formalism and limit holes (B02), algebraic differentiation.
**Attribution:** all spoken worked numbers and English exam questions independently authored, not copied source examples. Not scene JSON or audio-ready clips.

## Complete connected spoken script — the denominator changes everything

فاكر جدول الإشارات اللي قسمنا بيه خط الأعداد عند جذور العوامل؟ دلوقتي هناخد نفس الطريقة، بس بدل حاصل ضرب كثيرات حدود، هيكون عندنا **كسر**. والكسر له قانون لازم نفتكره قبل أي رسم: المقام ماينفعش يساوي صفر. يعني لو طلع عندنا جذر للبسط، ممكن نضمّه أو نستبعده حسب علامة المتباينة. لكن لو لقيت قيمة تخلي **المقام** صفر، القيمة دي ممنوعة دائمًا؛ لأنها أصلًا مش ضمن الأعداد اللي التعبير معرف عندها.

خد المسألة $\frac{x+1}{x-2}\le0$. بسط الكسر يساوي صفر لما إكس تساوي سالب واحد. والمقام يساوي صفر لما إكس تساوي اتنين. هنرسم النقطتين على خط الأعداد، ونعلّم إن اتنين **ممنوعة**، حتى قبل ما نعرف الإشارة. كده عندنا تلات مناطق: أقل من سالب واحد، وبين سالب واحد واتنين، وأكبر من اتنين.

نجرب سالب اتنين في المنطقة الأولى: البسط سالب والمقام سالب، فالكسر موجب، وبالتالي مش مناسب للشرط أصغر من أو يساوي صفر. نجرب صفر في المنطقة الوسطى: البسط موجب والمقام سالب، فالكسر سالب، وده مناسب. ونجرب تلاتة بعد اتنين: البسط والمقام موجبان، فالناتج موجب، ومش مناسب. عند سالب واحد البسط صفر والمقام مش صفر، فالكسر صفر؛ السؤال يسمح بالمساواة، فنضم سالب واحد. أما اتنين فالمقام صفر، فنستبعدها. إذن الحل $[-1,2)$.

لو تعاملت مع اتنين زي سالب واحد من غير ما تبص مين في البسط ومين في المقام، ممكن تدخل نقطة ممنوعة في الحل. ودي غلطة بنحاول نمنعها من البداية: **Zero of the numerator** مش زي **Zero of the denominator**. ورغم إن القيمتين بيقسموا الخط لمناطق نختبرها، سبب ضم كل حد أو استبعاده مختلف تمامًا.

خلينا نعمل تطبيق على كسر جديد، ولازم تكتب فيه القيمة الممنوعة صراحةً.

## Independent attempt EM1-RA-Q1 — question only
**English exam question:** Solve $\frac{x-4}{x+3}>0$ over the real numbers. Identify every excluded denominator value.
**Arabic spoken support:** حل إكس ناقص أربعة على إكس زائد تلاتة أكبر من صفر، واكتب القيمة الممنوعة بسبب المقام.
**Attempt direction (non-spoken):** do not show the sign table, intervals, or exclusions until answer is submitted.

### Post-attempt explanatory feedback EM1-RA-Q1 — separate
**English model answer:** $(-\infty,-3)\cup(4,\infty)$; $x=-3$ is excluded because the denominator is zero. $x=4$ is not included because the inequality is strict.
**Egyptian Arabic spoken explanation:** المقام يساوي صفر عند سالب تلاتة، فهي نقطة ممنوعة. البسط يساوي صفر عند أربعة، لكن علامة أكبر من صفر لا تسمح بضمها. قبل سالب تلاتة البسط والمقام سالبين فالناتج موجب. بين سالب تلاتة وأربعة إشارتهم مختلفة فالناتج سالب. وبعد أربعة الاتنين موجبين. ناخد الفترتين الخارجيتين ونستبعد الحدين.

## Connected spoken continuation — cancellation doesn't restore missing values

فيه فخ تاني بيظهر في الكسور لما نختصر عاملًا مشتركًا. لو كتبت $\frac{(x-1)(x+3)}{x-1}$، ممكن تختصر إكس ناقص واحد وتقول التعبير بقى $x+3$. الجبر ده صحيح فقط **عند القيم اللي إكس فيها مش واحد**. لأن التعبير الأصلي عند واحد فيه قسمة على صفر ومش معرف. الاختصار ماينفعش يرجّع النقطة دي للمجال.

يعني لو حد طلب حل متباينة من النوع $\frac{(x-1)(x+3)}{x-1}>0$، لازم نقول أولًا إكس لا تساوي واحد. وبعيدًا عن الواحد، الكسر يساوي إكس زائد تلاتة. إذن نحل $x+3>0$ يعني $x>-3$، وبعدين نشيل الواحد من الحل لأنه ممنوع في الأصل. الناتج $(-3,1)\cup(1,\infty)$. لاحظ إن الواحد هنا مش محذوف لأنه بيخلي البسط صفر فقط؛ اتحذف عشان المقام الأصلي كان صفر.

السؤال اللي جاي هيقيس النقطة دي بأرقام مختلفة. ما تخليش بساطة التعبير بعد الاختصار تنسيك قيمة ممنوعة في الأصل.

## Independent attempt EM1-RA-Q2 — question only
**English exam question:** Solve $\frac{(x-2)(x+5)}{x-2}\ge0$ over the real numbers. Explain whether $x=2$ may be included after cancellation.
**Arabic spoken support:** حل الكسر إكس ناقص اتنين في إكس زائد خمسة على إكس ناقص اتنين أكبر من أو يساوي صفر. هل ينفع تضم اتنين بعد الاختصار؟
**Attempt direction (non-spoken):** never display the cancellation result/denominator hole or interval before answer.

### Post-attempt explanatory feedback EM1-RA-Q2 — separate
**English model answer:** The original expression requires $x\ne2$. For allowed $x$, it reduces to $x+5\ge0$. Solution $[-5,2)\cup(2,\infty)$. The point $x=2$ remains excluded.
**Egyptian Arabic spoken explanation:** الاختصار صح بس لما إكس مش اتنين. بعيدًا عن القيمة دي، المتباينة بتقول إكس زائد خمسة أكبر من أو يساوي صفر، فنختار إكس من سالب خمسة وطالع. لكن لازم نشيل اتنين، لأن المقام الأصلي عندها صفر. وإشارة أو يساوي سمحت بسالب خمسة، ما سمحتش بقسمة على صفر.

## Connected spoken continuation — simultaneous constraints

آخر خطوة هنجمع فيها الدروس مع بعضها: أحيانًا يكون عندنا شرطين لازم يحصلوا **في نفس الوقت**. لو اتقال $x^2-4\ge0$ **and** $x<3$، نحل كل شرط الأول. الشرط التربيعي يعني $(x-2)(x+2)\ge0$، وده يدينا $(-\infty,-2]\cup[2,\infty)$. الشرط الخطي التاني يدينا $(-\infty,3)$. كلمة **and** معناها تقاطع الحلين؛ ناخد الأرقام المشتركة بينهم: $(-\infty,-2]\cup[2,3)$. استخدمنا اتحادًا بين فرعي الحل النهائي، لكن **التقاطع** هو اللي طبّق شرط «و» الأساسي.

وهنا طريقة منظمة للامتحان: اكتب القيم الممنوعة من البداية لو فيه مقام، حدد أصفار البسط والعوامل، اعمل جدول الإشارات، حل كل شرط لوحده، ثم استخدم تقاطعًا لو السؤال قال **and** أو اتحادًا لو السؤال قال **or**. بعدين راجع الأقواس: هل القيمة ناتجها صفر؟ هل مسموح بالمساواة؟ وهل المقام معرف؟ ده سبب إننا بدأنا المنهج كله بخط الأعداد والفترات.

خلينا نختم بسؤال يجمع متباينة كسرية وشرطًا ثانيًا. حل كل جزء الأول، وبعدها خد المشترك.

## Independent attempt EM1-RA-Q3 — question only
**English exam question:** Solve both conditions: $\frac{x+2}{x-1}\le0$ and $x<0$. Give the final real solution set as intervals and state the excluded denominator point.
**Arabic spoken support:** حل الشرطين مع بعض: إكس زائد اتنين على إكس ناقص واحد أصغر من أو يساوي صفر، وإكس أقل من صفر. اكتب مجموعة الحل وحدد القيمة الممنوعة للمقام.
**Attempt direction (non-spoken):** hold denominator and sign-chart/interval result until submission.

### Post-attempt explanatory feedback EM1-RA-Q3 — separate
**English model answer:** $\frac{x+2}{x-1}\le0$ yields $[-2,1)$; intersecting with $(-\infty,0)$ gives $[-2,0)$. The excluded denominator point is $x=1$.
**Egyptian Arabic spoken explanation:** البسط صفر عند سالب اتنين، والمقام صفر عند واحد. الكسر موجب قبل سالب اتنين، وسالب بين سالب اتنين وواحد، وموجب بعد واحد. نضم سالب اتنين لأن الكسر صفر والشرط يسمح، ونستبعد واحد لأن المقام عنده صفر. فالشرط الأول حلّه من سالب اتنين شاملًا لحد أقل من واحد. الشرط التاني إكس أقل من صفر، وده يقطع جزءًا من الفترة الأولى. فالتقاطع هو من سالب اتنين شاملًا لحد أقل من صفر، يعني $[-2,0)$. واحد يفضل قيمة ممنوعة للمقام حتى لو أصلًا خارج التقاطع النهائي.

## Closing spoken recap

إحنا كده خلصنا التمهيدات اللي هنحتاجها قبل Functions. جدول الإشارات بيفسر فين الكسر موجب أو سالب، وصفر البسط ممكن يدخل الحل حسب علامة المتباينة، لكن صفر المقام ممنوع دايمًا. الاختصار ما بيرجعش نقطة ممنوعة، و«و» معناها تقاطع الشروط، بينما «أو» معناها اتحاد. دلوقتي لما نبدأ مجال الدالة في الـBlock التالي هنكون فاهمين ليه بنستبعد قيم من المجال، وإزاي نكتب باقي القيم كفترات بدل ما نحفظ أشكال الإجابات.

## Rough visual suggestions — NON production assets
Numerator zero vs forbidden denominator point, rational sign chart, a cancelled factor with a persistent open hole, two sets of solution bands for their intersection. Responses hidden prior to independent attempt.
