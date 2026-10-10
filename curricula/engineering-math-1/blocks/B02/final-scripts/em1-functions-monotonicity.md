# B02 Stage 03 — Increasing, Decreasing and Intervals of Monotonicity
**Stable lesson ID:** \`em1-functions-monotonicity\` | **B02 issued order:** 4 of 8 | **Arabic title:** التزايد والتناقص على فترات
**Source:** \`abd-el-salam-math-i-scan\`, printed pp. **35–37** within chapter graph-behavior/limit transition; PDF image pp. **21–22**. This is a learner-centered division, not a claim of a clean printed subsection boundary.
**Prerequisites:** Cartesian graphs and B02 function families; B01 number-line order, intervals and positive/negative comparisons. No derivative is assumed.
**Objectives:** define strict increasing/decreasing relative to two ordered inputs in an interval; read sign of change left-to-right on common graphs; identify restricted intervals instead of making false whole-domain claims.
**Stage 02 source:** provisional C \`../working-drafts/03-monotonicity-limits.md\`, independent Q-C1, plus new original Q-C5 and Q-C6 assessing linear/rational behavior.
**Boundary:** SPLIT C into graph monotonicity here vs value-approach/one-sided limits next. This lesson is coherent without needing the formal limit concept; separate checks target comparison across entire intervals.
**Attribution:** examples and assessments are authored learning checks, not copied textbook exercises. This Markdown is Stage 03 editorial narration only.

## Complete connected spoken script — reading the drawing from left to right

تخيل طريق فيه طلعة وبعدها نزلة. لو بتتحرك من الشمال لليمين، هتقدر تقول إمتى ارتفاعك بيزيد وإمتى بينقص. الرسم البياني للدالة نفس الفكرة، لكن لازم نتفق إن الاتجاه اللي بنتبعه هو **زيادة إكس**. لو واي بتزيد مع كل زيادة لإكس، بنقول الدالة **Increasing** على الجزء ده؛ ولو واي بتقل بنقول **Decreasing**. وصفنا سلوك الدالة على **فترة**، مش شكل المنحنى كله بكلمة واحدة.

خلينا نفهم كلمة «على فترة» بشكل أدق. لو اخترت أي مدخلين $x_1<x_2$ من نفس الفترة، وكانت دائمًا $f(x_1)<f(x_2)$، يبقى الدالة متزايدة **بصرامة** أو Strictly Increasing فيها. لو بدل كده $f(x_1)>f(x_2)$ بنسميها Strictly Decreasing. مش كفاية تلاقي نقطتين وترسم سهم؛ لازم الحكم يفضل صحيح لاختيار أي نقطتين في الفترة. وده غير الحالة اللي تسمح بتساوي النواتج، اللي بنسميها Non-decreasing أو Non-increasing؛ دلوقتي تركيزنا على التزايد والتناقص الصارم.

بص على $f(x)=x^2$. لما نتحرك من إكس سالب تلاتة لسالب واحد، الناتج يقل من تسعة لواحد. وقبل الصفر كل ما إكس تقرب من الصفر من ناحية السالب، قيمة التربيع تقل. وبعد الصفر بيحصل العكس: تربيع الأعداد الموجبة بيكبر مع زيادة إكس. إذن الدالة متناقصة على $(-\infty,0)$ ومتزايدة على $(0,\infty)$. عند الصفر نفسها أقل قيمة؛ اخترنا الفترتين المفتوحتين لوصف فرعين صارمين ومش لازم نزعم إنها متزايدة على كل الأعداد الحقيقية.

لو حرّكنا نفس المنحنى للشمال في $(x+1)^2$، النقطة اللي بتقسم السلوك هتبقى سالب واحد. خلينا نختبر الجزء ده بسؤال جديد قبل ما نشوف الخطوط والكسور.

## Independent attempt Q-C1 — not spoken as heading
**Question spoken (English):** For $f(x)=(x+1)^2$, state the intervals where the function is decreasing and increasing.
**Question spoken (Arabic support):** لدالة إكس زائد واحد الكل تربيع، اكتب الفترات اللي فيها الدالة بتتناقص وبتتزايد وإنت ماشي من الشمال لليمين.
**Attempt:** written; don't expose vertex or interval answers before submission.

### Post-attempt feedback C1 — separate spoken text
**Model answer (English):** Decreasing on $(-\infty,-1)$ and increasing on $(-1,\infty)$.
**Feedback spoken:** دي نفس فكرة منحنى التربيع لكن القاع اتحرك لليسار عند إكس تساوي سالب واحد. قبل القاع، لما إكس تزيد قيمة الدالة بتقل؛ وبعد القاع بتزيد. عشان كده حد الفصل هو سالب واحد مش صفر.

## Connected spoken continuation — the sign of slope without calculus

هل لازم يكون فيه منحنى عشان نقول متزايد ومتناقص؟ لأ. لو $g(x)=3x+2$، خد أي مدخلين $x_1<x_2$. الفرق في النتيجتين $g(x_2)-g(x_1)=3(x_2-x_1)$؛ لأن الفرق بين المدخلين موجب، والضرب في تلاتة موجب يفضل موجب. إذن $g$ متزايدة على كل الأعداد الحقيقية. لو الميل سالب، زي $-2x+7$، نفس الفرق يطلع سالب، فالدالة متناقصة. ما احتجناش مشتقة عشان نفهم ده.

دلوقتي هتجرّب مستقيمًا مختلفًا عن اللي حسبناه، وهتربط الحكم بمقارنة نواتج فعلية.

## Independent attempt Q-C5 — independent linear-monotonicity transfer (new)
**Question spoken (English):** For $g(x)=-2x+7$, determine whether it is strictly increasing or decreasing on $\mathbb R$. Calculate $g(-1)$ and $g(3)$ to support your claim.
**Question spoken (Arabic support):** لدالة سالب اتنين إكس زائد سبعة، هل هي متزايدة ولا متناقصة على كل الأعداد الحقيقية؟ احسب عند سالب واحد وتلاتة عشان تفسر الاتجاه.
**Attempt:** written; keep both output values and final direction hidden before submission.

### Post-attempt feedback C5 — separate reasoning
**Model answer (English):** Strictly decreasing on $\mathbb R$; $g(-1)=9$ and $g(3)=1$.
**Feedback spoken:** عند سالب واحد، سالب اتنين في سالب واحد زائد سبعة يساوي تسعة. وعند تلاتة، سالب ستة زائد سبعة يساوي واحد. المدخل زاد لكن الناتج قل. وبشكل عام فرق الناتجين سالب اتنين في فرق المدخلين، فكل ما إكس تزيد، الناتج يقل على الفترة كلها؛ مش بس عند النقطتين دول.

## Connected spoken continuation — domain matters

آخر شكل هنراجعه هو الكسر $h(x)=1/x$. المجال هنا مش كل الأعداد: إكس تساوي صفر ممنوعة. على الجزء **الموجب فقط**، لو زودت إكس من واحد لاتنين، الناتج يقل من واحد لنص. ولو زودت المدخل أكثر من نص لواحد، الناتج يقل من اتنين لواحد. الفكرة العامة إن مقلوب العدد الموجب بيقل لما العدد نفسه يزيد، عشان كده الدالة متناقصة على $(0,\infty)$. وعلى الجزء السالب كمان هي متناقصة، لكن ماينفعش نقول متناقصة على **المجال كله كقطعة واحدة** باختيار نقطتين عبر الصفر: المجال فيه فجوة وحكم المقارنة ممكن يتغير عبر الفجوة.

جرّب بنفسك مسألة بتطلب منك توضح ليه الفترة المحددة مهمة، مش بس تقرأ الشكل من بعيد.

## Independent attempt Q-C6 — reciprocal interval transfer (new)
**Question spoken (English):** On the interval $(0,\infty)$, is $h(x)=1/x$ strictly increasing or strictly decreasing? Compare $h(1/2)$ and $h(2)$, and explain why $x=0$ is excluded.
**Question spoken (Arabic support):** على الفترة الموجبة فقط، واحد على إكس متزايدة ولا متناقصة؟ قارن الناتج عند نص وعند اتنين، واشرح ليه الصفر مش في المجال.
**Attempt:** written; do not show sample outputs or interval conclusion before submission.

### Post-attempt feedback C6 — separate reasoning
**Model answer (English):** Strictly decreasing on $(0,\infty)$; $h(1/2)=2$, $h(2)=1/2$, and $x=0$ is excluded since the denominator would vanish.
**Feedback spoken:** عند نص الناتج اتنين، وعند اتنين الناتج نص؛ المدخل زاد والناتج قل. والأهم إن لكل مدخلين موجبين مرتبّين، مقلوب الأصغر أكبر من مقلوب الأكبر، فالتناقص على الفترة كلها. الصفر ممنوع لأنه مقام، وعشان كده ماينفعش نرسم سلوك الدالة كأن الخط بيعدّي عليه.

## Closing spoken recap

تعلمنا وصف الرسم من الشمال لليمين بدل الكلام عن شكله كله: Increasing أو Decreasing لازم تتحدد على فترة وبمقارنة أي مدخلين من جواها. القطع المكافئ ممكن يتناقص ثم يتزايد، والخط المستقيم اتجاهه مرتبط بميله، والكسر يحتاج الانتباه لفترات مجاله. الدرس اللي جاي هنغير السؤال: بدل ما نسأل إكس بتزيد وواي بتعمل إيه، هنسأل واي **بتقرب من كام** لما إكس تقرب من نقطة؛ ودي فكرة النهاية.

## Rough visual proposals — not scene assets

Dot moving left-to-right on parabola and linear graph, open gap on reciprocal line, independent interval bands. No pre-attempt highlighting of correct increasing/decreasing bands.
