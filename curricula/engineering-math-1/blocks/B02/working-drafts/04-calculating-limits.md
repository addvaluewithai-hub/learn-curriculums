# B02 Stage 01 provisional working draft D — إزاي نحسب النهاية من غير ما نقع في فخ صفر على صفر؟
**Stage:** B02 **Stage 02** — critically revised complete connected provisional draft; **no final ID, boundary, scenes/audio or academic approval**.
**Source:** `abd-el-salam-math-i-scan`, printed pp. 39–46 (PDF pp. 23–27).
**Prerequisites:** limit/nearby behavior (C); factors/fractions, basic trig and radians (brief bridges).
**Working objectives:** justify conditional limit laws and 0/0 forms, calculate limits by factoring or conjugates, distinguish two-sided finite vs divergent one-sided behavior, and apply radians-based trigonometric limits.
**Authored examples:** original explanations, worked examples and questions, not transcriptions.
**Legacy provenance:** Derived **verbatim in teaching/assessment body** from historical `curricula/engineering-math-1/working-drafts/04-calculating-limits.md` (previous curriculum-wide AI Stage 02 revision). Historical original is **frozen for audit**, while THIS B02-scoped copy is the sole active Stage 01 draft; no retroactive B02 gate approval is claimed. The current turn did not conduct a new Stage 02 critique.
**Verified source scope:** printed 39–46 / PDF 23–27. On 2026-10-10 the conversation-mounted original PDF was reopened; SHA-256 matches the source manifest. Its future private retrieval is still unresolved at the user's request.
**B01 prerequisite bridge:** B02 C limit meaning; B01 factorization and rational domain; radians bridge.
**Deliberately deferred:** continuity and differentiation.
**Teaching boundary:** Label D and order A→E are **provisional**; no stable B02 lesson ID or scene may be created until Stage 03 after a separate human gate.
**Active critique/rewrite evidence:** `../reviews/STAGE_02_CRITIQUE.md`; algebraic vs trigonometric limit boundaries remain undecided until Stage 03. Source pp. 41–46 were visually checked again; some textbook explanatory remarks are not rigorous substitutes for one-sided sign analysis.

## Complete connected spoken draft
دلوقتي عندنا سؤال واضح: لما إكس تقرب من رقم، إزاي أطلع قيمة الدالة اللي بتقرب لها؟ في مسائل كتير أول خطوة منطقية هي **Direct substitution**، يعني أجرب أحط الرقم في التعبير. لو $f(x)=x^2+2x$ وإكس بتقرب من ثلاثة، التعويض يديني تسعة زائد ستة، يعني خمسة عشر. في كثيرات الحدود، العمليات دي بتشتغل من غير مشاكل عند أي عدد حقيقي. لكن خلي في بالك إن ده وضع مناسب للتعويض، مش إذن إنك تتجاهل مقامات الأصفار أو دوال غير معرفة.

قوانين **Limit laws** بتقول، لما النهايات المعنية موجودة ومحددة، إن نهاية مجموع دالتين هي مجموع نهايتيهما، ونهاية حاصل الضرب هي حاصل ضرب النهايتين، والثابت نقدر نطلعه بره. وبالنسبة للكسر، نقدر نقسم نهايتي البسط والمقام **بشرط إن نهاية المقام مش صفر**. الشرط ده أساسي. لو نهايتا البسط والمقام صفر، ماينفعش أقول إن النهاية صفر أو إنها غير موجودة بمجرد ما شفت صفر على صفر؛ دي إشارة إن طريقة التعويض لوحدها مش كفاية.

صورة صفر على صفر مش رقم بنقدر نطلعه من الآلة. مثالين بسيطين هيورّونا ليه: نهاية $x/x$ عند اقتراب إكس من صفر تساوي واحد؛ لأن الكسر يساوي واحد عند كل إكس غير صفر. أما نهاية $x^2/x$ عند نفس النقطة فتساوي صفر؛ لأن الكسر بيساوي إكس بعيدًا عن الصفر. الاتنين بيدونا شكل صفر على صفر بالتعويض غير المسموح، لكن نهايتهم مختلفة. عشان كده السؤال الأول هو: هل نقدر نبسط التعبير على مدخلات قريبة **مسموح بها**؟

خلينا نشتغل على $g(x)=(x^2-9)/(x-3)$ لما إكس تقرب من ثلاثة. التعويض الأول يطلع صفر على صفر. نحلل البسط: إكس تربيع ناقص تسعة تساوي إكس ناقص ثلاثة في إكس زائد ثلاثة. طول ما إكس مش مساوية ثلاثة، العامل المشترك ممكن يتبسط، فيبقى التعبير إكس زائد ثلاثة. الآن لما إكس تقرب من ثلاثة، القيم تقرب من ستة. إحنا ماقلناش إن الدالة الأصلية معرفة عند ثلاثة؛ قلنا إن اللي بيحصل حول النقطة يسمح لنا نحسب النهاية.

ومش كل مسألة تبسيطها بتحليل كثيرات حدود. مثلًا لما يكون عندك $ (\sqrt{x+4}-2)/x $ وإكس بتقرب من صفر، التعويض يدي صورة صفر على صفر. الفكرة هنا نضرب البسط والمقام في **المرافق** $\sqrt{x+4}+2$. البسط يبقى إكس زائد أربعة ناقص أربعة، يعني إكس. نلغي إكس فقط لما تكون غير صفر في الطريق إلى الصفر، فيتبقى واحد على الجذر لإكس زائد أربعة زائد اتنين. الآن النهاية واحد على أربعة. لاحظ إن التبسيط بيحافظ على سلوك الدالة عند كل نقطة قريبة مسموح بها؛ مش بيعرفها قسرًا عند النقطة المحذوفة.

لكن في نهايات مينفعش نكتفي فيها بالتعويض والتبسيط. خذ واحد على إكس، لما إكس تقرب من صفر. من اليمين القيم موجبة وتكبر بلا حد، ومن الشمال سالبة ومقدارها يكبر بلا حد. إذن مفيش **نهاية حقيقية من الناحيتين** عند الصفر. قولنا «بتكبر بلا حد» وصف للسلوك، مش معناها إن ما لا نهاية عدد حقيقي نقدر نعوض بيه. لازم تفرق بين نهاية عددية موجودة، ونهاية غير موجودة من الناحيتين.

خلينا نثبت حاجة مهمة قبل تطبيق القانون المثلثي: الراديان هو وحدة قياس الزاوية اللي بنستخدمها في نهايات الـCalculus دي. الزاوية $\pi$ راديان تساوي مية وتمانين درجة؛ وبالتالي لو الآلة الحاسبة على درجات من غير تحويل، مش ينفع ناخد منها نفس الحد الأساسي كما هو. وجود شرط الراديان مش تنبيه شكلي، ده جزء من صحة القانون.

في الجزء الخاص بالدوال المثلثية، هنستخدم حقيقة أساسية: نهاية ساين إكس على إكس لما إكس تقرب من صفر تساوي واحد، **بشرط قياس الزاوية بالراديان**. خلي كلمة **radians** واضحة في ذهنك؛ لو بدلنا وحدة الزاوية من غير تحويل، النتيجة مش بنفس الصورة. ومن العلاقة بين الظل والساين والكوساين، بنستنتج إن نهاية تان إكس على إكس عند الصفر تساوي واحد برضه بالراديان.

ليه قانون تان إكس على إكس طلع بنفس النهاية؟ حوالين الصفر، كوساين إكس بيقرب من واحد ومش صفر، فنقدر نكتب تان إكس على إكس كأنها ساين إكس على إكس مضروبًا في واحد على كوساين إكس. أول عامل بيقرب من واحد، والتاني كمان، فيبقى حاصل الضرب واحد. مش معناها إننا عوضنا بصفر داخل الكسر؛ الحساب كله على قيم قريبة وغير مساوية للصفر.

خلينا نطبقها على $\sin(3x)/x$ لما إكس تقرب من صفر. نقسم ونضرب في ثلاثة: الناتج ثلاثة في ساين ثلاثة إكس على ثلاثة إكس. لما إكس تقرب من صفر، ثلاثة إكس كمان تقرب من صفر، والكسر المثلثي يقرب من واحد، فالنهاية ثلاثة. الحيلة هنا مش حفظ رقم ثلاثة؛ هي إننا نبني **نفس صورة القانون** ونراعي إن المعامل ظهر خارج الكسر.

وإحنا بنحل، هنفضل نسأل: هل التعبير معرف حوالين النقطة؟ هل نهاية المقام صفر؟ هل فيه عامل مشترك أو مرافق؟ هل نهايتا الجهتين متفقتان؟ وهل الزاوية بالراديان؟ الأسئلة دي اللي بتحول الحساب من تكديس خطوات إلى طريقة تفكير هندسية.

## Independent attempt Q-D1 — not spoken as heading
**Question spoken (English):** Evaluate $\lim_{x\to4}(x^2-16)/(x-4)$. Explain why direct substitution is insufficient.
**Question spoken (Arabic support):** احسب نهاية إكس تربيع ناقص ستة عشر على إكس ناقص أربعة لما إكس تقترب من أربعة، واشرح ليه التعويض المباشر مش كفاية.
**Attempt:** written; no factorization or numerical answer before attempt.

### Post-attempt feedback D1 — separate spoken text
**Model answer (English):** The limit is $8$. Factor $x^2-16=(x-4)(x+4)$ for $x\ne4$.
**Feedback spoken:** التعويض الأول يطلع صفر على صفر. نحلل فرق المربعين، ونبسط العامل إكس ناقص أربعة بعيد عن النقطة نفسها، فيبقى إكس زائد أربعة. ولما إكس تقرب من أربعة، التعبير يقرب من تمانية. الدالة الأصلية لسه مش معرفة عند أربعة.

## Independent attempt Q-D2 — not spoken as heading
**Question spoken (English):** In radians, find $\lim_{x\to0}\sin(5x)/(2x)$.
**Question spoken (Arabic support):** بالراديان، احسب نهاية ساين خمسة إكس على اتنين إكس لما إكس تقرب من صفر.
**Attempt:** written; keep transformation and answer concealed.

### Post-attempt feedback D2 — separate spoken text
**Model answer (English):** The limit is $\frac52$.
**Feedback spoken:** نخلي الكسر فيه ساين خمسة إكس على خمسة إكس، ونطلع معامل خمسة على اتنين بره. النهاية الأساسية جوه بتساوي واحد لما إكس تقرب من صفر بالراديان، فيبقى الجواب خمسة على اتنين. كتابة الوحدة مش تفصيلة زائدة هنا.

## Independent attempt Q-D3 — separate rationalization transfer
**Question spoken (English):** Evaluate $\displaystyle\lim_{x\to0}\frac{\sqrt{2x+9}-3}{x}$ by algebraic manipulation, and explain the restriction used when cancelling $x$.
**Question spoken (Arabic support):** احسب نهاية الجذر التربيعي لاتنين إكس زائد تسعة ناقص تلاتة، الكل على إكس، لما إكس تقرب من صفر. استخدم تبسيط جبري واشرح امتى ينفع نختصر إكس.
**Attempt:** written; reveal neither conjugate nor answer until after submission.

### Post-attempt feedback D3 — separate spoken text
**Model answer (English):** Multiply by the conjugate; for $x\ne0$, the expression becomes $\frac{2}{\sqrt{2x+9}+3}$, so the limit is $\frac13$.
**Feedback spoken:** الضرب في المرافق يخلي البسط اتنين إكس، فنقدر نختصر إكس مع المقام **لما إكس مش صفر**؛ والنهاية بتدرس القيم القريبة غير المساوية للصفر. اللي يتبقى اتنين على الجذر زائد تلاتة. عند الاقتراب من الصفر المقام يقرب من ستة، فالناتج تلت. ما قلناش إن الكسر الأصلي معرف عند إكس صفر.

## Independent attempt Q-D4 — separate one-sided rational-limit transfer
**Question spoken (English):** Describe the left-hand and right-hand behavior of $f(x)=\frac{1}{x-2}$ as $x$ approaches $2$. Does a finite two-sided limit exist?
**Question spoken (Arabic support):** اوصف سلوك واحد على إكس ناقص اتنين لما إكس تقرب من اتنين من الشمال واليمين. هل فيه نهاية حقيقية محددة من الناحيتين؟
**Attempt:** written; conceal signs and nonexistence statement until response.

### Post-attempt feedback D4 — separate spoken text
**Model answer (English):** From the left, $f(x)\to-\infty$; from the right, $f(x)\to+\infty$. No finite two-sided limit exists.
**Feedback spoken:** قبل اتنين مباشرة، المقام سالب وصغير جدًا، فالكسر قيمته سالبة ومقدارها بيكبر بلا حد. بعد اتنين المقام موجب وصغير جدًا، فتكون القيم موجبة وبتكبر بلا حد. الجهتين مش بيقربوا من نفس عدد حقيقي، وبالتالي مفيش نهاية حقيقية محددة من الناحيتين. علامة ما لا نهاية هنا بتوصف السلوك، مش قيمة نعوض بيها في الدالة.

## Closing spoken recap
لو النهايات عندك متاحة ومفيش مقام بيوصل للصفر، قوانين النهايات والتعويض غالبًا الطريق الأسرع. لو ظهرت صفر على صفر، فكر في تحليل أو مرافق بدل ما تعتبرها إجابة. ولو في اتجاهين مختلفين، افصل اليمين عن الشمال. والنهايات المثلثية الأساسية تعتمد على الراديان. الخطوة الجاية هي سؤال مختلف: هل قرب الدالة من نقطة بيتفق مع قيمتها عند النقطة؟ هنا بندخل على الاتصال.

## Rough visual ideas (editorial only)
An initially blocked “0/0” board transitions to factorization/cancellation; one-sided arrows near 0 for (1/x); radian unit-circle cue; feedback equations only after submissions.
