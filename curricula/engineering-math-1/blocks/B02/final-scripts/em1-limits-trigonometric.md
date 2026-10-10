# B02 Stage 03 — Trigonometric Limits in Radians
**Stable lesson ID:** \`em1-limits-trigonometric\` | **B02 issued order:** 7 of 8 | **Arabic title:** النهايات المثلثية وقانون الساين بالراديان
**Source:** \`abd-el-salam-math-i-scan\`, printed pp. **44–46** (end of B02 limit methods; overlap pp. 44–45 with algebraic methods), PDF images **25–27**. Exact photographed source division is not one-to-one with student lessons.
**Prerequisites:** limit meaning and valid product law; radian angle measure (\`pi radians=180 degrees\` bridge); $\sin,\cos,\tan$ definitions and tangent denominator from preceding B02 trig-family lesson.
**Objectives:** correctly use $\lim_{u\to0}\sin(u)/u=1$ in radians; convert scaled sine limits by factor matching; derive tangent limit from sine and cosine; solve comparative trig-limit examples with conditions.
**Stage 02 source:** D \`../working-drafts/04-calculating-limits.md\`, independent Q-D2 plus new Q-D5 and Q-D6 for tangent and mixed sine/tangent transfer.
**Boundary:** other half of SPLIT D. Angle units and trig identities are a distinct new conceptual precondition, so this is a fully connected lesson, not a cut paragraph.
**Attribution:** worked examples/assessments independently authored; no verbatim textbook exercise reproduction. This is Stage 03 script only; no timed visuals/TTS.
 
## Complete connected spoken script — a limit depends on angle units

إحنا حسبنا نهايات بالدوال الجبرية، لكن لما تدخل دالة **Sine** في المسألة، التحليل والمرافق مش دايمًا هيخلّصونا. هنا هنحتاج قانون أساسي له شرط واضح: الزاوية تكون **بالراديان**. لو فاكر الدائرة اللي رسمنا عليها ساين وكوساين، الراديان طريقة لقياس طول القوس مقارنةً بنصف القطر. $\pi$ راديان تساوي مية وتمانين درجة. القانون الأساسي في التفاضل بيعتمد على المقياس ده، مش مجرد اختيار شكل كتابة.

القانون هو $\lim_{x\to0}\sin x/x=1$ لما إكس مقاسة بالراديان. عند إكس صفر الكسر نفسه صفر على صفر ومش معرف، لكن عند زوايا قريبة من الصفر **بالراديان** النسبة بين ساين الزاوية والزاوية نفسها بتقرب من واحد. دي نهاية وليس قيمة تعويض. لو الآلة الحاسبة في وضع درجات واستخدمتها كأنها راديان، هتطلع نسبة مختلفة؛ فلازم تحول وحدات الزوايا الأول أو تلتزم بالراديان من البداية.

خلينا نحسب $\lim_{x\to0}\sin(3x)/x$. جوه ساين عندنا **تلاتة إكس**، لكن المقام إكس فقط. عشان نستخدم القانون، نعمل الصورة اللي احنا حافظين معناها: $3\,\sin(3x)/(3x)$. لما إكس تقرب من صفر، تلاتة إكس برضه تقرب من صفر، والنسبة الأساسية تقرب من واحد، فالنهاية تلاتة. الرقم بره مش بياتي من الحفظ؛ بيطلع من موازنة المعامل جوه الزاوية.

نجرب قانون ساين في مسألة مختلفة زي امتحان الهندسة: فيه معامل فوق وتحت ولازم تراعي الراديان.

## Independent attempt Q-D2 — not spoken as heading
**Question spoken (English):** In radians, find $\lim_{x\to0}\sin(5x)/(2x)$.
**Question spoken (Arabic support):** بالراديان، احسب نهاية ساين خمسة إكس على اتنين إكس لما إكس تقرب من صفر.
**Attempt:** written; keep transformation and answer concealed.

### Post-attempt feedback D2 — separate spoken text
**Model answer (English):** The limit is $\frac52$.
**Feedback spoken:** نخلي الكسر فيه ساين خمسة إكس على خمسة إكس، ونطلع معامل خمسة على اتنين بره. النهاية الأساسية جوه بتساوي واحد لما إكس تقرب من صفر بالراديان، فيبقى الجواب خمسة على اتنين. كتابة الوحدة مش تفصيلة زائدة هنا.

## Connected spoken continuation — tangent from sine and cosine

طيب $\tan x/x$ نهايتها كام؟ نعرف من درس العائلات إن $\tan x=\sin x/\cos x$ بشرط كوساين ما تكونش صفر. قرب الصفر، كوساين إكس بيقرب من واحد، فالمقام مش صفر في منطقة صغيرة حوالين الصفر. نقدر نكتب
$\tan x/x=(\sin x/x)\,(1/\cos x)$.
أول جزء يقرب من واحد بقانون الساين بالراديان، والتاني يقرب من واحد؛ فالنهاية تساوي واحد. مرة تانية، ما قلناش إننا عوضنا إكس بصفر داخل الكسر غير المعرف.

لو الزاوية جوه التان بقت $4x$، نعمل زي الساين بالضبط: $\tan(4x)/(3x)=(4/3)\,[\tan(4x)/(4x)]$. النسبة جوه تقرب من واحد، فيبقى الناتج أربعة على تلاتة. خد بالك إن المقام لازم يطابق **كل الزاوية**، مش مجرد حرف إكس.

دلوقتي هتطبق الفكرة على معامل جديد في التان بنفسك.

## Independent attempt Q-D5 — new tangent-limit transfer
**Question spoken (English):** In radians, evaluate $\lim_{x\to0}\frac{\tan(6x)}{5x}$. State which basic limit law you use.
**Question spoken (Arabic support):** بالراديان، احسب نهاية تان ستة إكس على خمسة إكس عند الصفر، واذكر قانون النهاية الأساسي اللي استخدمته.
**Attempt:** written; do not reveal the factor or numerical result before submission.

### Post-attempt feedback D5 — delayed reasoning
**Model answer (English):** $\frac65$, since $\frac{\tan(6x)}{5x}=\frac65\,\frac{\tan(6x)}{6x}\to\frac65$ in radians.
**Feedback spoken:** عشان المقام يبقى نفس الزاوية اللي جوه التان، نضرب في ستة على ستة بشكل صحيح ونطلع ستة على خمسة بره. الجزء تان ستة إكس على ستة إكس نهايته واحد بالراديان. إذن النتيجة ستة على خمسة، بشرط إننا بنقرب بصفر من قيم غير صفر وداخل مجال التان.

## Connected spoken continuation — combining two trigonometric terms

آخر خطوة هتجمع بين ساين وتان. مثلًا $\sin(2x)/\tan(3x)$ لما إكس تقرب من صفر، ماينفعش نعوض مباشرة لأن البسط والمقام بيقربوا من صفر. نكتبها في صورة
$[\sin(2x)/(2x)]\,[(3x)/\tan(3x)]\,(2/3)$.
النسبة الأولى تقرب من واحد، والنسبة التانية مقلوب نسبة التان الأساسية اللي بتقرب من واحد، فالنهاية اتنين على تلاتة. مش محتاج تحفظ قانونًا جديدًا لكل معامل؛ نفس النهايتين الأساسيتين هم اللي بيشتغلوا.

هنشوف دلوقتي سؤال فيه معاملات تانية، وانت حوّله لنفس الصور القياسية بنفسك.

## Independent attempt Q-D6 — new sine-to-tangent transfer
**Question spoken (English):** In radians, evaluate $\lim_{x\to0}\frac{\sin(4x)}{\tan(7x)}$, and identify both standard trigonometric limit ratios.
**Question spoken (Arabic support):** بالراديان، احسب نهاية ساين أربعة إكس على تان سبعة إكس عند الصفر، واذكر نسبتي النهاية الأساسيتين.
**Attempt:** written; conceal coefficient matching and answer before learner attempt.

### Post-attempt feedback D6 — delayed reasoning
**Model answer (English):** $\frac47$; use $\sin(4x)/(4x)\to1$ and $\tan(7x)/(7x)\to1$ in radians.
**Feedback spoken:** بنخلّي ساين أربعة إكس على أربعة إكس، وسبعة إكس على تان سبعة إكس، ونطلع أربعة على سبعة بره. كل جزء قياسي بيقرب لواحد بالراديان، فالناتج أربعة على سبعة. المشكلة ما كانتش إن صفر على صفر له قيمة، لكن إننا نقدر نعيد كتابة السلوك عند المدخلات القريبة المسموح بها.

## Closing spoken recap

النهارده ربطنا وحدة **Radian** بصحة قانون ساين إكس على إكس، وشفنا إزاي نطابق المعامل جوه الزاوية مع المقام، واشتقينا قانون التان من الساين والكوساين بدل حفظه من غير سبب. واتدربنا على ساين فوق تان باستخدام نفس القواعد. السؤال اللي جاي في الفصل هو: هل نهاية الدالة عند نقطة بتساوي قيمتها عند النقطة؟ يعني هل الدالة **متصلة** هناك؟

## Rough visual proposals — not scene assets

Small-angle radian arc, highlighted numerator angle vs denominator factor, neutral unit circle and ratio reformulation. No displayed model answer during written attempt.
