# B02 Stage 03 — Continuity, Removable Holes, Jumps and Piecewise Matching
**Stable lesson ID:** `em1-functions-continuity` | **B02 issued order:** 8 of 8 | **Arabic title:** الاتصال عند نقطة والثقوب والقفزات
**Source:** `abd-el-salam-math-i-scan`, printed theory pp. 47–50, Exercise (2) pp. 51–53; photographed PDF pp. 27–30 left; textbook Chapter 1 *Functions and Their Graphs*. Printed pp. 51–53, where cited, are an exercise bank, not continuity theory.
**Concept prerequisites:** B02 concepts of domain/function value, finite left/right limits and algebraic simplification; B01 absolute-value distance.
**Outcomes taught and independently assessed:** three conditions at an interior point; one-sided domain-endpoint continuity; removable holes versus jumps; piecewise parameters; sharp corner may be continuous.
**Boundary rationale:** KEEP E as one lesson with internal connected parts because the same three-part continuity criterion explains holes, jumps and piecewise repairs; small endpoint and corner bridges avoid requiring derivatives.
**Attribution:** all demonstrations and English exam questions are independent authored pedagogy; only topic and page locators are source-grounded. A source p.34 erratum about exponentials is not in this lesson.
**Production limit:** Stage 03 complete spoken editorial manuscript, not scene JSON, timestamped cues, paid audio, faculty certification or a published lesson. Editorial headings/questions/feedback boundaries are not spoken.

## Complete connected spoken script — student journey
فاكر لما حسبنا نهاية دالة عند نقطة لقينا إنها بتقرب من رقم، مع إن الدالة ممكن ما تكونش معرفة عند نفس النقطة؟ هنا يظهر السؤال اللي بيجمع كل اللي فات: هل المنحنى مكمل بعضه عند النقطة، ولا فيه فجوة أو قفزة؟ في الحساب بنسمي الفكرة دي **Continuity**، يعني اتصال الدالة عند نقطة.

تخيل إنك بترسم خط بقلم، وإنت ماشي قريب من إكس تساوي اتنين. لو الخط اللي جاي من الشمال والخط اللي جاي من اليمين بيوصلوا لنفس الارتفاع، والنقطة المرسومة فعلًا عند إكس تساوي اتنين موجودة على نفس الارتفاع، مفيش انقطاع عند النقطة دي. لكن لو النقطة ناقصة أو في ارتفاع مختلف، فالرسم عندها مش متصل. التشبيه البصري مفيد، لكن خلينا نحوله لثلاثة شروط واضحة؛ عشان الرسم ساعات مايبقاش كفاية في مسألة جبرية.

الرسم اللي نقدر نمشي عليه من غير ما نرفع القلم تشبيه سريع، لكن مش اختبارًا رياضيًا كافيًا؛ عشان نحكم بدقة لازم نتأكد من النهاية وقيمة الدالة. وهنناقش هنا الاتصال عند نقطة **داخل** مجال بنقدر نقترب منها من اليمين والشمال. لو النقطة آخر المجال، بنستخدم اتصالًا من الناحية المتاحة فقط، ودي ملاحظة للتمييز مش محور مسائلنا دلوقتي.

خلينا نشوف الطرف ده مرة واحدة من غير ما نحوله لفصل مستقل. $q(x)=\sqrt{x}$ على المجال $[0,\infty)$ عند الصفر، ماعندناش مدخلات حقيقية من شمال الصفر جوه المجال. لكن نقدر نقرب من اليمين، والجذر بيقرب من صفر، و$q(0)=0$؛ فالدالة متصلة عند بداية مجالها **من ناحية المجال**. أما لو النقطة في نص المجال وفيه اقتراب من الناحيتين، هنرجع لشروطنا التلاتة كاملة.

عشان الدالة (f) تكون **Continuous at $x=a$** لازم أول حاجة (f(a)) تكون معرفة؛ يعني قيمة الدالة عند النقطة موجودة. ثاني حاجة النهاية $\lim_{x\to a}f(x)$ تكون موجودة كعدد حقيقي واحد من الناحيتين. وثالث حاجة، وهي الأهم في الربط، إن النهاية تساوي قيمة الدالة: $\lim_{x\to a}f(x)=f(a)$. الشروط التلاتة مع بعض مطلوبة. لو واحد غاب، مانقولش الدالة متصلة عند النقطة، حتى لو الرسم من بعيد شكله شبه خط واحد.

خد الدالة $f(x)=x^2+1$. عند إكس تساوي واحد، قيمة الدالة اتنين، ولما إكس تقرب من واحد من الناحيتين، القيم بتقرب من اتنين برضه. عندنا الثلاثة شروط، فالدالة متصلة عند واحد. كتير من الدوال المألوفة، زي كثيرات الحدود، متصلة عند كل عدد حقيقي. والدالة الكسرية بتكون متصلة عند النقط اللي مقامها مش صفر؛ هنا دور المجال بيرجع يظهر.

وفيه فرق مهم قبل ما نمهد للمشتقة: الدالة ممكن تكون متصلة عند نقطة حتى لو الرسم عامل زاوية حادة. مثلًا $|x|$ عند الصفر قيمتها صفر ومن اليمين والشمال بتقرب من صفر، فهي متصلة. كون الرسم ناعم أو له ميل واحد موضوع تاني مش هنفترضه من الاتصال.

خلينا نشوف ثقب في الرسم. افترض إن $g(x)=(x^2-1)/(x-1)$ لكل إكس ما عدا واحد. قريب من الواحد نقدر نبسطها إلى إكس زائد واحد، فالنهاية عند واحد تساوي اتنين. لكن (g(1)) نفسها مش معرفة؛ إذن الدالة **غير متصلة** عند واحد بسبب قيمة ناقصة. لو عرّفنا قيمة جديدة عند واحد تساوي اتنين، يبقى ممكن نصلح الثقب في الدالة المعاد تعريفها. ده نموذج اسمه **removable discontinuity** أو انقطاع يمكن إصلاحه بإضافة قيمة مناسبة.

ومش كل انقطاع ثقب بسيط. لو النهاية من الشمال مختلفة عن النهاية من اليمين، فمفيش رقم واحد نحطه في النقطة يصلح المشكلة. مثلًا لو يسار الصفر القاعدة واي يساوي واحد، ويمين الصفر القاعدة واي يساوي ثلاثة، فالقيم بتقرب من واحد ناحية، وثلاثة الناحية التانية. هنا القفزة مش هتختفي بمجرد ما نحدد (f(0)) بأي قيمة. شرط اتفاق النهايتين جه قبل شرط مساواتهما بقيمة الدالة.

النوع اللي بيجمع الأفكار دي في الامتحان هو **Piecewise function**، يعني دالة بقواعد مختلفة حسب قيمة إكس. خلينا نكوّن دالة: لما إكس أقل من اتنين، $f(x)=x+1$. ولما إكس أكبر من اتنين، $f(x)=x^2-1$. وعند إكس تساوي اتنين بالضبط، $f(2)=k$؛ كي عدد مجهول. من الشمال، إكس زائد واحد تقرب من ثلاثة. ومن اليمين، إكس تربيع ناقص واحد تقرب من ثلاثة. كويس، النهاية من الناحيتين موجودة وتساوي ثلاثة. فلو عايزين الاتصال، لازم القيمة عند النقطة نفسها، يعني كي، تساوي ثلاثة. كده وصلنا من شكل الرسم لقيمة عددية مفهومة.

في مسائل الاتصال، أنصحك تحط ترتيب صغير على الورقة: القيمة عند النقطة، نهاية من الشمال، نهاية من اليمين، ثم المقارنة. ما تبدأش بحل المجهول قبل ما تتأكد إن الناحيتين متفقتان أصلًا. وفي الدرس القادم عن المشتقة هنحتاج نفهم اتصال الدالة وسلوكها القريب جدًا، فالاتصال هنا مش نهاية منفصلة، ده أساس للحساب التفاضلي.

## Independent attempt Q-E1 — not spoken as heading
**Question spoken (English):** A piecewise function is defined by $f(x)=x^2-2$ for $x<1$, $f(1)=a$, and $f(x)=3x-4$ for $x>1$. Find $a$ so the function is continuous at $x=1$.
**Question spoken (Arabic support):** الدالة إكس تربيع ناقص اتنين قبل الواحد، وقيمتها عند واحد هي إيه المجهولة، وبعد الواحد ثلاثة إكس ناقص أربعة. أوجد إيه عشان تكون متصلة عند واحد.
**Attempt:** written; withhold limits and parameter until after submission.

### Post-attempt feedback E1 — separate spoken text
**Model answer (English):** $a=-1$; both one-sided limits equal $-1$.
**Feedback spoken:** من الشمال نعوض في إكس تربيع ناقص اتنين لما إكس تقرب من واحد، فالنهاية سالب واحد. ومن اليمين ثلاثة في واحد ناقص أربعة برضه سالب واحد. إذن النهاية الكلية سالب واحد. عشان الاتصال لازم قيمة الدالة عند واحد، اللي رمزنا لها بإيه، تساوي سالب واحد.

## Independent attempt Q-E2 — not spoken as heading
**Question spoken (English):** Let $h(x)=(x^2-4)/(x-2)$ for $x\ne2$, and let $h(2)=5$. Is $h$ continuous at $x=2$? Explain using the limit and the function value.
**Question spoken (Arabic support):** لو الدالة بتساوي إكس تربيع ناقص أربعة على إكس ناقص اتنين بعيدًا عن اتنين، لكن قيمتها عند اتنين تساوي خمسة؛ هل هي متصلة عند اتنين؟ وضح السبب.
**Attempt:** written; no answer or factored equation before response.

### Post-attempt feedback E2 — separate spoken text
**Model answer (English):** No. The limit is $4$, while $h(2)=5$.
**Feedback spoken:** حوالين اتنين نحلل ونبسط، فالتعبير يمشي زي إكس زائد اتنين، وده بيقرب من أربعة. لكن القيمة اللي حددناها عند اتنين هي خمسة. النهاية موجودة، والقيمة موجودة، بس مش متساويين؛ الشرط الثالث فشل، فالدالة مش متصلة عند اتنين. لو غيرنا قيمة النقطة لأربعة هنصلح الانقطاع.

## Independent attempt Q-E3 — separate jump-discontinuity transfer
**Question spoken (English):** Suppose $g(x)=2x$ for $x<1$, $g(1)=k$, and $g(x)=x+4$ for $x>1$. Is there any real value of $k$ that makes $g$ continuous at $x=1$? Explain.
**Question spoken (Arabic support):** الدالة قبل الواحد اتنين إكس، وعند الواحد قيمتها كي المجهولة، وبعد الواحد إكس زائد أربعة. هل فيه قيمة حقيقية لكي تخلي الدالة متصلة عند واحد؟ اشرح.
**Attempt:** written; keep separate directional limits and reasoning concealed.

### Post-attempt feedback E3 — separate spoken text
**Model answer (English):** No such $k$ exists. The left-hand limit is $2$ and the right-hand limit is $5$, so the two-sided limit does not exist.
**Feedback spoken:** من الشمال النهاية اتنين، ومن اليمين النهاية خمسة. لأن الناحيتين مش متساويين، النهاية الكلية مش موجودة. مهما اخترنا كي، هنغيّر قيمة النقطة نفسها بس، ومش هنقدر نخلي النهايتين تتفقوا. دي قفزة، مش مجرد ثقب نصلحه بتغيير قيمة واحدة.

## Independent attempt Q-E4 — continuity without smoothness
**Question spoken (English):** Is $f(x)=|x-2|$ continuous at $x=2$ on $\mathbb R$? Check the value at the point and both one-sided limits.
**Question spoken (Arabic support):** هل القيمة المطلقة لإكس ناقص اتنين متصلة عند اتنين؟ افحص قيمة الدالة عند النقطة والنهاية من كل ناحية.
**Attempt:** written; do not pre-reveal the value or the two limits.

### Post-attempt feedback E4 — separate spoken text
**Model answer (English):** Yes. $f(2)=0$, $\lim_{x\to2^-}f(x)=0$ and $\lim_{x\to2^+}f(x)=0$; therefore $f$ is continuous at $2$.
**Feedback spoken:** عند اتنين القيمة المطلقة لصفر هي صفر. ولو قربنا من اتنين من أي ناحية، المسافة بتقرب من صفر. كده النهاية من الشمال والنهاية من اليمين واحد، وبتساوي قيمة الدالة عند اتنين. الزاوية الحادة في الرسم ما تمنعش الاتصال، لكن ممكن تأثر لاحقًا على المشتقة.

## Closing spoken recap
الاتصال مش مجرد رسمة ينفع نمشي عليها بقلم. عند نقطة داخل المجال لازم القيمة تكون معرفة، والنهاية من الناحيتين تكون موجودة، والاتنين يكونوا متساويين. الثقب ممكن يتصلح بتحديد قيمة مناسبة، لكن اختلاف اتجاهي الاقتراب مش هيتصلح بمجرد تغيير النقطة؛ وعند طرف المجال نفحص الاقتراب المسموح. والزاوية الحادة مش دليل انقطاع. كده عندنا الأساس اللي هنحتاجه لما يبدأ Block التفاضل بعدين.

## Rough visual proposals — NOT a Stage 04 storyboard
Point value vs approached height, open and filled point at a removable hole, distinct one-sided arrows at a jump, endpoint domain arrow; hide answers until attempt.
