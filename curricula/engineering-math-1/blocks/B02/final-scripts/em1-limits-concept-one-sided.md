# B02 Stage 03 — Limits as Nearby Behavior and One-Sided Approach
**Stable lesson ID:** `em1-limits-concept-one-sided` | **B02 issued order:** 5 of 8 | **Arabic title:** معنى النهاية والنهايات من اليمين والشمال
**Source:** `abd-el-salam-math-i-scan`, printed pp. **37–40** (shared with monotonicity and next calculation pages); PDF images **22–23**. Page overlap is genuine; the new boundary is pedagogical, not a distinct source heading.
**Prerequisites:** B02 domain and graph-reading, intervals/ordered inputs and basic factoring; previous monotonicity lesson is context, not proof of any limit.
**Objectives:** distinguish limit of nearby values from value at the point; read separate left-/right-hand approaches, including missing or reassigned points; determine when a finite two-sided limit exists.
**Stage 02 source:** C, `../working-drafts/03-monotonicity-limits.md`, Q-C2/C3/C4 all retained as separate independent checks; lesson rewritten with its own starting motivation and recap.
**Boundary:** other half of SPLIT C; one unified question—what does the rule approach near a target input?—supports all examples and exams.
**Attribution:** examples/questions original pedagogy; no copyrighted book exercise is transcribed. No issued scenes, audio or media.

## Complete connected spoken script — get near without having to arrive

افترض إنك رايح باب وبتقرب منه خطوة صغيرة بعد خطوة أصغر. تقدر تقول إن المسافة الباقية بتقرب للصفر حتى لو ما وصلتش الباب فعلًا. في الدوال بنعمل حاجة شبه كده: لما المدخل إكس يقرب من رقم، نشوف قيمة الدالة بتقرب من كام. دي فكرة **Limit**، أو النهاية. التشبيه للتقريب بس؛ في الرياضيات هنراقب القيم المسموح بها **قرب** المدخل المقصود.

مثال لطيف: $f(x)=2x+3$. لو إكس قربت من واحد، الناتج قرب من خمسة، ونكتب $\lim_{x\to1}(2x+3)=5$. في الحالة دي الدالة متصلة، فالتعويض المباشر يدينا النهاية، لكن لازم نفتكر إن **النهاية سؤال عن القيم القريبة** مش عن رقم فِي الخانة بالضرورة. لو قيمة الدالة عند واحد اتغيرت من غير ما نغيّر القيم اللي حوالين واحد، ممكن النهاية تفضل خمسة.

خلينا ناخد المثال الأوضح: $r(x)=(x^2-4)/(x-2)$ لما إكس ما تساويش اتنين. عند اتنين الكسر الأصلي صفر على صفر، وده مش قيمة عددية نقدر نقول إنها النهاية. بس بعيدًا عن اتنين نحلل البسط $(x-2)(x+2)$ ونختصر العامل المشترك حيث المقام مش صفر. قرب اتنين، التعبير ماشي زي $x+2$، يعني القيم تقرب من أربعة. بالرغم إن $r(2)$ أصلًا مش معرفة، النهاية تساوي أربعة. ده خط فاصل بين **Function value** و**Limit**.

عشان تتأكد إنك مش بتستخدم التعويض من غير فهم، هنطبق معنى الاقتراب على قاعدة خطية جديدة. حاول الأول وبعدين شوف سبب الإجابة.

## Independent attempt Q-C2 — not spoken as heading
**Question spoken (English):** Evaluate $\lim_{x\to 2}(3x-2)$. Is the limit about inputs near two or only the value exactly at two?
**Question spoken (Arabic support):** احسب نهاية ثلاثة إكس ناقص اتنين لما إكس تقترب من اتنين، واشرح هل السؤال عن القيم القريبة ولا نقطة اتنين وحدها.
**Attempt:** written; keep answer hidden.

### Post-attempt feedback C2 — separate spoken text
**Model answer (English):** The limit is $4$; it describes nearby values as $x\to2$.
**Feedback spoken:** ناتج التعويض هنا أربعة، والدالة الخطية مفيهاش مشكلة حوالين اتنين، فالقيم القريبة فعلًا بتقرب من أربعة. معنى النهاية هو سلوك القيم القريبة، وإنها ساوت قيمة الدالة عند اتنين في المثال ده حاجة إضافية مش تعريف النهاية.

## Connected spoken continuation — left side, right side, and the missing point

نقدر نقرب من رقم زي الواحد بطريقتين. من الشمال بقيم أقل من الواحد، ودي **Left-hand limit**؛ ومن اليمين بقيم أكبر، ودي **Right-hand limit**. في النهاية المحددة بعدد حقيقي من الناحيتين، لازم الاتنين يقتربوا لنفس الرقم. لو الشمال بيقرب من اتنين واليمين من تلاتة، مفيش نهاية **واحدة من الناحيتين** عند النقطة، حتى لو حددنا قيمة الدالة هناك بعشرة.

الرسمة هنا مفيدة: ممكن يبقى عند إكس تساوي واحد دائرة **مفتوحة** عند ارتفاع اتنين، ودائرة مقفولة عند عشرة، لكن ده وحده ما يحددش النهاية من اليمين. لازم نمشي بالعين على مسار المنحنى من **كل جهة**. وماينفعش نسأل عن نهاية من جهة مفيش مدخلات من مجال الدالة قريبة فيها أصلًا؛ إحنا بنراقب قيمًا في المجال، مش بنخترع نقاط.

دلوقتي هتتعامل مع دالة **Piecewise** لها فرع قبل الواحد وفرع بعده، وقيمة معينة عند الواحد. هل الجهتين متفقتين؟

## Independent attempt Q-C3 — separate one-sided-transfer question
**Question spoken (English):** For $p(x)=x+1$ when $x<1$, $p(1)=10$, and $p(x)=4-x$ when $x>1$, find the left-hand and right-hand limits at $x=1$. Does the two-sided limit exist?
**Question spoken (Arabic support):** الدالة بتساوي إكس زائد واحد قبل الواحد، وقيمتها عند الواحد عشرة، وبعد الواحد بتساوي أربعة ناقص إكس. احسب النهاية من الشمال ومن اليمين، وهل النهاية من الجهتين موجودة؟
**Attempt:** written; conceal directional limits and final conclusion.

### Post-attempt feedback C3 — separate spoken text
**Model answer (English):** Left-hand limit $=2$, right-hand limit $=3$; the two-sided limit does not exist, even though $p(1)=10$.
**Feedback spoken:** لما نقرب من الواحد بقيم أصغر، نستخدم إكس زائد واحد فالقيم تقرب من اتنين. ولما نقرب من قيم أكبر، نستخدم أربعة ناقص إكس فالقيم تقرب من تلاتة. بما إن اتنين مش هي تلاتة، النهاية من الناحيتين مش موجودة كقيمة واحدة. الرقم عشرة هو قيمة الدالة عند النقطة، ومش بيغير سلوك الاقتراب.

## Connected spoken continuation — repairing a point does not change nearby behavior

قبل ما نخلص، خد قاعدة جديدة في ذهنك: لو قربنا من نقطة والدالة على كل المدخلات القريبة بتدي نفس السلوك، تغيير **قيمة النقطة نفسها** ما بيغيرش النهاية. مثال جديد: لو بعيدًا عن أربعة كان التعبير $(x^2-16)/(x-4)$، فبيساوي $x+4$ عند كل إكس غير أربعة؛ وبالتالي النهاية تمانية. لو صاحب المسألة كتب إن القيمة عند أربعة اتنين، هنقول ده تعريف جديد للنقطة فقط؛ النهاية لسه تمانية. السؤال التالي مش نفس المثال: لازم تفصل بين القيمة اللي حُددت للنقطة واللي الدالة بتميل له حواليها.

## Independent attempt Q-C4 — value assigned at a removable hole
**Question spoken (English):** For $x\ne3$ let $r(x)=\frac{x^2-9}{x-3}$, but define $r(3)=-7$. Find $\lim_{x\to3}r(x)$ and $r(3)$. Are they equal?
**Question spoken (Arabic support):** بعيدًا عن تلاتة الدالة إكس تربيع ناقص تسعة على إكس ناقص تلاتة، وعند تلاتة اتعرّفت قيمتها بسالب سبعة. احسب النهاية والقيمة عند تلاتة وقارن بينهم.
**Attempt:** written; do not show factorization or limit value before attempt.

### Post-attempt feedback C4 — separate spoken text
**Model answer (English):** The limit is $6$, while $r(3)=-7$; the two values are different.
**Feedback spoken:** لما إكس تبعد عن تلاتة نقدر نحلل فرق المربعين ونختصر العامل المشترك بشرط إكس ما تكونش تلاتة. ساعتها القيم القريبة ماشية زي إكس زائد تلاتة، فتقرب من ستة. لكن نقطة تلاتة نفسها قيمتها المحددة سالب سبعة. دي طريقة نشوف بيها إن النهاية عن الجوار مش عن قيمة النقطة وحدها.

## Closing spoken recap

النهارده عرفنا إن $\lim$ بتدرس القيم القريبة من المدخل المقصود، ومش شرط تكون الدالة معرفة أو مساوية للنهاية عند النقطة نفسها. النهاية من الشمال واليمين لازم تتفق لو عايزين نهاية عددية واحدة من الجهتين، ولازم أصلًا يبقى فيه مجال نقرب منه. في الدرس اللي بعده هنستخدم الفكرة دي لحساب نهايات فيها عوامل، أو جذر يحتاج مرافقًا، أو مقام يخلي السلوك مختلفًا حسب الاتجاه.

## Rough visual ideas — nonproduction

Approach arrows toward a hollow point, full vs hollow point at different heights, left/right colored trajectories that disagree; pre-attempt board contains only neutral axes and question text.
