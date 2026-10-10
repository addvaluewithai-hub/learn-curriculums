# B02 Stage 01 provisional working draft E — الاتصال: هل قيمة الدالة بتطابق اللي الرسم بيقرب له؟
**Stage:** B02 **Stage 01** — complete connected provisional draft; **not** Stage 02 sign-off, final boundary, stable ID or production scenes.
**Source:** `abd-el-salam-math-i-scan`, printed pp. 47–53 (PDF pp. 28–30, left page only at PDF 30).
**Prerequisites:** function value/domain (A), graph/limits and one-sided approach (C–D).
**Working objectives:** explain pointwise continuity; detect holes/jumps; solve for a piecewise parameter that produces continuity.
**Authored examples:** all narrated examples and questions are newly written.
**Legacy provenance:** Derived **verbatim in teaching/assessment body** from historical `curricula/engineering-math-1/working-drafts/05-continuity.md` (previous curriculum-wide AI Stage 02 revision). Historical original is **frozen for audit**, while THIS B02-scoped copy is the sole active Stage 01 draft; no retroactive B02 gate approval is claimed. The current turn did not conduct a new Stage 02 critique.
**Verified source scope:** printed 47–50 with practice 51–53 / PDF 27–30 left. On 2026-10-10 the conversation-mounted original PDF was reopened; SHA-256 matches the source manifest. Its future private retrieval is still unresolved at the user's request.
**B01 prerequisite bridge:** B02 A values/domain and C–D one-sided/two-sided limit concept.
**Deliberately deferred:** derivatives in B03.
**Teaching boundary:** Label E and order A→E are **provisional**; no stable B02 lesson ID or scene may be created until Stage 03 after a separate human gate.

## Complete connected spoken draft
فاكر لما حسبنا نهاية دالة عند نقطة لقينا إنها بتقرب من رقم، مع إن الدالة ممكن ما تكونش معرفة عند نفس النقطة؟ هنا يظهر السؤال اللي بيجمع كل اللي فات: هل المنحنى مكمل بعضه عند النقطة، ولا فيه فجوة أو قفزة؟ في الحساب بنسمي الفكرة دي **Continuity**، يعني اتصال الدالة عند نقطة.

تخيل إنك بترسم خط بقلم، وإنت ماشي قريب من إكس تساوي اتنين. لو الخط اللي جاي من الشمال والخط اللي جاي من اليمين بيوصلوا لنفس الارتفاع، والنقطة المرسومة فعلًا عند إكس تساوي اتنين موجودة على نفس الارتفاع، مفيش انقطاع عند النقطة دي. لكن لو النقطة ناقصة أو في ارتفاع مختلف، فالرسم عندها مش متصل. التشبيه البصري مفيد، لكن خلينا نحوله لثلاثة شروط واضحة؛ عشان الرسم ساعات مايبقاش كفاية في مسألة جبرية.

الرسم اللي نقدر نمشي عليه من غير ما نرفع القلم تشبيه سريع، لكن مش اختبارًا رياضيًا كافيًا؛ عشان نحكم بدقة لازم نتأكد من النهاية وقيمة الدالة. وهنناقش هنا الاتصال عند نقطة **داخل** مجال بنقدر نقترب منها من اليمين والشمال. لو النقطة آخر المجال، بنستخدم اتصالًا من الناحية المتاحة فقط، ودي ملاحظة للتمييز مش محور مسائلنا دلوقتي.

عشان الدالة (f) تكون **Continuous at $x=a$** لازم أول حاجة (f(a)) تكون معرفة؛ يعني قيمة الدالة عند النقطة موجودة. ثاني حاجة النهاية $\lim_{x\to a}f(x)$ تكون موجودة كعدد حقيقي واحد من الناحيتين. وثالث حاجة، وهي الأهم في الربط، إن النهاية تساوي قيمة الدالة: $\lim_{x\to a}f(x)=f(a)$. الشروط التلاتة مع بعض مطلوبة. لو واحد غاب، مانقولش الدالة متصلة عند النقطة، حتى لو الرسم من بعيد شكله شبه خط واحد.

خد الدالة $f(x)=x^2+1$. عند إكس تساوي واحد، قيمة الدالة اتنين، ولما إكس تقرب من واحد من الناحيتين، القيم بتقرب من اتنين برضه. عندنا الثلاثة شروط، فالدالة متصلة عند واحد. كتير من الدوال المألوفة، زي كثيرات الحدود، متصلة عند كل عدد حقيقي. والدالة الكسرية بتكون متصلة عند النقط اللي مقامها مش صفر؛ هنا دور المجال بيرجع يظهر.

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

## Closing spoken recap
نقدر دلوقتي نقول إن الدالة متصلة عند نقطة لما قيمتها موجودة، ونهايتها من الجهتين موجودة، والاتنين متساويين. الثقب ممكن يتصلح لو النهاية واحدة وعرفنا النقطة بالقيمة المناسبة. أما القفزة بين نهايتين مختلفتين فلا تصلحها قيمة مفردة عند النقطة. كده أنهينا مسار الفصل الأول من الدوال إلى النهايات والاتصال، وجاهزين نبني عليه مفهوم المشتقة في الفصل التالي.

## Rough visual ideas (editorial only)
Show a filled dot vs open circle, a jump with two heights, and left/right traces meeting at a piecewise boundary; answer number only after attempt.
