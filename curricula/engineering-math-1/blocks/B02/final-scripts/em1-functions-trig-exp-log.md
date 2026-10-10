# B02 Stage 03 — Trigonometric, Exponential and Logarithmic Functions
**Stable lesson ID:** `em1-functions-trig-exp-log` | **B02 issued order:** 3 of 8 | **Arabic title:** الدوال المثلثية والأسية واللوغاريتمية
**Source:** `abd-el-salam-math-i-scan`, printed pp. **30–35** / PDF image pp. **18–21**, overlapping the algebraic family pages. Source printed **p. 34** appears to reverse domain/range for real $a^x$; this teaching script follows independently verified mathematics, explicitly **NOT** that printed erroneous pair.
**Prerequisites:** input-output, domain/range and denominator restrictions; brief radian/angle-circle bridge; B02 preceding algebraic graphs.
**Objectives:** classify and read sine/cosine/tangent including forbidden tangent angles; classify real exponentials $a^x$ with $a>0$ (and the special $a=1$ case); interpret $\log_a x$ with $a>0,a\ne1$ and positive arguments.
**Stage 02 source:** provisional B, `../working-drafts/02-function-families.md`; independently assessed questions B2, B4 and B5. 
**Boundary decision:** separate from algebraic families because periodicity, radians, exponent in place of x, and positive log input each need their own explanatory bridges and assessments; one connected family-and-domain goal unifies this lesson.
**Attribution:** demonstration graphs/numbers and questions are original teaching, not copied book exercises. This Stage 03 editorial script is not audio, scene JSON or human math approval.

## Complete connected spoken script — when the input plays a different role

إحنا عرفنا الرسومات اللي بتطلع من جمع وضرب وقسمة إكس. لكن لو بدل إكس ما بقتش بتحدد مكانًا على خط بس، وبقت زاوية في دائرة، أو موجودة في **الأس** نفسه، هيطلع عندنا شكل جديد. هنقارن ثلاث عائلات من ناحية القاعدة والمجال والمدى والسلوك؛ ده هيخلّي استخدامها في النهايات بعدين أوضح.

ابدأ بتخيل نقطة بتلف على دائرة نصف قطرها واحد. لو قسنا ارتفاعها عن المركز، الارتفاع يطلع وينزل ويتكرر بعد دورة. ده شكل دالة **Sine**، أو $y=\sin x$. ولو قسنا الإسقاط الأفقي هنوصل لفكرة **Cosine**، أو $y=\cos x$. الاتنين يقبلوا كل زاوية حقيقية؛ والمدى من سالب واحد لواحد شاملًا. في حساب التفاضل بنستخدم عادة **Radian**: دورة كاملة $2\pi$ راديان، ونص دورة $\pi$ راديان يساوي مية وتمانين درجة. فالدوال دي **Periodic** يعني شكل النواتج بيتكرر بعد طول معين من الزاوية.

الظل، أو **Tangent**، مختلف: $\tan x=\sin x/\cos x$. لو كوساين إكس يساوي صفر، المقام صفر وبالتالي المدخل ده ممنوع. وده بيحصل عند $x=\pi/2+k\pi$ لأي عدد صحيح $k$. رسمة التان فروع منفصلة بدل موجة متصلة في كل المدخلات. لاحظ إننا ما حفظناش القيم الممنوعة عشوائيًا؛ اشتقينا السبب من مقام الكسر، زي اللي اتعلمناه في B01. لما نشوف $\tan(2x)$، القيم الممنوعة تتغير لأن الزاوية جوه الدالة بقت اتنين إكس.

خلينا ناخد نوع تاني: $y=2^x$. ده اسمه **Exponential function**، أو دالة أسية، لأن إكس في الأس. جرب إكس صفر يطلع واحد، وواحد يطلع اتنين، وسالب واحد يطلع نص. يعني كل مدخل حقيقي ممكن، والناتج موجب دائمًا، من غير ما يساوي صفر. ولما الأساس أكبر من واحد زي اتنين، الدالة بتزيد؛ ولو الأساس بين صفر وواحد، زي $(1/2)^x$، بتقل. في الحالة العامة لما $a>0$ و$a\ne1$، المجال $\mathbb R$ والمدى $(0,\infty)$. استثناء صغير: $1^x=1$ ثابتة ومداها $\{1\}$، فمش بنفس مدى الحالة غير الثابتة.

اللي بيسأل سؤالًا عكسيًا هو **Logarithm**. لو قلنا $\log_2 8=3$، معناها «اتنين أس كام عشان تطلع تمانية؟» وبما إن أي أس حقيقي لأساس موجب يطلع قيمة موجبة، مدخل اللوغاريتم لازم يكون **أكبر من صفر**. للدالة $\log_a x$، نطلب $a>0$ والأساس مختلف عن واحد، و$x>0$، والمدى كل الأعداد الحقيقية. الفرق بين مجال الأسية ومجال اللوغاريتم أساسي، ومش هنخلطه بمجرد إن رسم الاتنين بيطلع بشكل منحني.

دلوقتي نجرب أول مسألة مستقلة: لو دخلنا تركيبًا فيه لوغاريتم وتغييرًا في مدخله، هل هتقدر تحدد العائلة والمجال؟

## Independent attempt Q-B2 — heading not spoken
**Question spoken (English):** Which family contains $h(x)=\log_3(x-2)$? State its real domain.
**Question spoken (Arabic support):** الدالة لوغاريتم أساس ثلاثة لإكس ناقص اتنين، تنتمي لأي عائلة؟ وما مجالها الحقيقي؟
**Attempt:** written; do not display a number line before attempt.

### Post-attempt feedback B2 — separate spoken text
**Model answer (English):** Logarithmic; domain $x>2$, or $(2,\infty)$.
**Feedback spoken:** دي دالة لوغاريتمية. أي حاجة داخل اللوغاريتم لازم تكون أكبر من صفر، يعني إكس ناقص اتنين أكبر من صفر، وبالتالي إكس أكبر من اتنين. مش بنسمح بالصفر هنا، حتى لو هو مسموح جوه الجذر التربيعي في بعض الدوال.

## Connected spoken continuation — transfer across the three families

قبل السؤال التاني، خلينا نقارن بطريقة عملية: كوساين إكس ياخد أي عدد حقيقي ويطلع قيمة محصورة بين سالب واحد وواحد. خمسة أس إكس يقبل أي عدد حقيقي برضه، لكن الناتج دايمًا موجب وممكن يكبر بلا حد مع زيادة إكس. أما لوغاريتم إكس فمدخله لازم يكون موجب، رغم إن الناتج ممكن يكون سالب أو صفر أو موجب. التمييز ده هيساعدك لما تقرأ سؤال إنجليزي بيطلب **Domain** أو **Range**؛ ما تجاوبش بالاسم بدل المجموعة الفعلية.

## Independent attempt Q-B4 — separate family/domain-range transfer
**Question spoken (English):** Classify $f(x)=\sin x$ and $g(x)=3^x$. For real $x$, state the domain of $f$ and the range of $g$.
**Question spoken (Arabic support):** صنّف ساين إكس وتلاتة أس إكس، وبعدها اكتب مجال ساين إكس ومدى تلاتة أس إكس لما إكس عدد حقيقي.
**Attempt:** written; do not expose the families or domain/range until response.

### Post-attempt feedback B4 — separate spoken text
**Model answer (English):** $f$ is trigonometric with domain $\mathbb R$; $g$ is exponential with range $(0,\infty)$.
**Feedback spoken:** ساين إكس دالة مثلثية وتقبل أي زاوية حقيقية بوحدة متفقة. تلاتة أس إكس دالة أسية، ومهما كانت إكس موجبة أو سالبة الناتج يفضل موجب، ومش بيساوي صفر. لذلك مدى الدالة الأسية هنا كل الأعداد الموجبة فقط. السؤال بيختبر إنك تربط العائلة بالمجال والمدى، مش الاسم وحده.

## Connected spoken continuation — angle transformations and restrictions

نرجع الآن لدالة التان ونزود معاملًا جوه الزاوية. مثلًا لو $\tan(3x)$، المنع مش عند إكس تساوي باي على اتنين مباشرة؛ بنحل $3x=\pi/2+k\pi$. يبقى القيم الممنوعة $\pi/6+k\pi/3$. لا تخلط بين تغيير الرسم الأفقي وبين تغيير قوانين القسمة: إحنا لسه بنستبعد أصفار الكوساين *في الزاوية الكاملة*. جرّب بنفسك معاملًا مختلفًا، وخلي الإجابة مؤجلة لما تخلص الحل.

## Independent attempt Q-B5 — unseen tangent-domain assessment
**Question spoken (English):** In radians, find all excluded real values of $x$ in $h(x)=\tan(2x)$, and explain why they are excluded.
**Question spoken (Arabic support):** بالراديان، حدد كل قيم إكس الممنوعة من مجال تان اتنين إكس، واشرح ليه القيم دي ممنوعة.
**Attempt:** written; do not show denominator zeros or exclusions before student attempt.

### Post-attempt feedback B5 — separate spoken text
**Model answer (English):** Exclude $x=\frac\pi4+\frac{k\pi}{2}$, $k\in\mathbb Z$, because $\cos(2x)=0$.
**Feedback spoken:** تان اتنين إكس هو ساين اتنين إكس على كوساين اتنين إكس. عشان المقام مايبقاش صفر، لازم نستبعد لما اتنين إكس تساوي باي على اتنين زائد كي باي. نقسم على اتنين فنطلع إكس تساوي باي على أربعة زائد كي باي على اتنين، لكل كي عدد صحيح. تفسير المجال أهم من حفظ نقاط فاضية في رسم التان.

## Closing spoken recap

خد معاك أربع علامات تميّز: الدالة المثلثية تربط مدخل الزاوية بدورة أو بفروع للظل؛ الأسية فيها إكس في الأس ونواتجها موجبة مع أساس موجب مناسب؛ اللوغاريتم بيطلب مدخلًا موجبًا؛ وتغيير الزاوية جوه التان بيغير قيم المقام الممنوعة. مصدرنا المطبوع عند صفحة 34 فيه سطر غير متسق مع رسم الأسية، فهنا استخدمنا القاعدة الرياضية الصحيحة بوضوح. دلوقتي نقدر نرجع للرسوم ونسأل: بتزيد فين وبتقل فين؟

## Rough visual suggestions — nonproduction

Unit-circle height → sine and cosine bands; one tangent branch with forbidden radian lines; $2^x$ vs $\log_2 x$ aligned axis, positive output and input shading; hide each exam answer until the attempt.
