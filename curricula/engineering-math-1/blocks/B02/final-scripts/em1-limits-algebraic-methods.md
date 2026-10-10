# B02 Stage 03 — Algebraic Limits, Cancellation, Rationalization and Directional Behavior
**Stable lesson ID:** \`em1-limits-algebraic-methods\` | **B02 issued order:** 6 of 8 | **Arabic title:** حساب النهايات الجبرية والمرافق والاتجاهات
**Source:** \`abd-el-salam-math-i-scan\`, printed pp. **39–45** (limit laws, algebraic worked approaches) / PDF images **23–26**. Trigonometric limit identities on the overlapping later spread are treated in the next student lesson, not falsely claimed as a clean printed section break.
**Prerequisites:** nearby/one-sided limits from preceding B02 lesson; B01 factorization, nonzero denominator, sign analysis, principal square root and interval notation.
**Objectives:** use valid limit laws with denominator conditions; distinguish \`0/0\` from a result; compute finite limits by factoring or conjugates on neighboring admissible inputs; interpret opposing unbounded one-sided signs without assigning infinity as a real value.
**Stage 02 source:** D \`../working-drafts/04-calculating-limits.md\`, independent D1 (factor), D3 (conjugate), D4 (one-sided divergence). All kept as written-attempt questions with separate feedback.
**Boundary:** SPLIT D: algebraic neighborhood transformation and denominator sign reasoning form a coherent prerequisite for the distinct radians and trig identities taught next. No mechanical transcript slicing.
**Attribution:** numbers/problems and spoken demonstrations are authored pedagogy, not reproduced book exercises; source p. 42 shorthand about denominator zero does not override actual mathematical conditions. No Stage 04 scenes/audio/teacher approval.

## Complete connected spoken script — when substitution stalls

إحنا فهمنا إن النهاية مش لازم تساوي قيمة الدالة عند نقطة. لكن في الامتحان هنسأل السؤال الأصعب: **أحسبها إزاي؟** هنستخدم تلات حاجات نعرفها من قبل: التعويض لما ينفع، والتحليل أو المرافق لما يظهر صفر على صفر، والتفكير في الإشارة من اليمين والشمال لما المقام يقرب من صفر.

ابدأ بـ$\lim_{x\to2}(x^2+3)$. الدالة كثيرة حدود ومفيش فيها مقام أو جذر يعطل التعويض، فتقرب من سبعة. القوانين اللي بنسميها **Limit laws** بتقول لما نهايات الطرفين موجودة ومحددة، نقدر نجمع النهايات ونضربها في ثابت، ونضرب نهايتين مع بعض. وفي القسمة فيه شرط إضافي: **نهاية المقام لازم ما تكونش صفر** قبل ما نقسم نهاية البسط على نهاية المقام. ماينفعش نخترع قسمة على صفر باسم قانون نهايات.

لو جربت $\lim_{x\to3}(x^2-9)/(x-3)$، التعويض يدينا صورة $0/0$. دي اسمها **Indeterminate form**، يعني التعويض فشل يحدد لنا النهاية، مش إن النهاية صفر أو غير موجودة. نحلل فرق المربعين، $(x-3)(x+3)$، ونختصر العامل المشترك **فقط عند إكس مش تلاتة**. القيم المسموح بيها جنب تلاتة ماشية زي $x+3$، فبتقرب من ستة. إحنا ما عرّفناش الكسر الأصلي عند تلاتة، إنما حسبنا سلوكه حواليها.

ليه لازم ما نحكمش من شكل $0/0$؟ لأن $\lim_{x\to0} x/x$ تساوي واحد بعيدًا عن الصفر، بينما $\lim_{x\to0} x^2/x$ تساوي صفر؛ نفس شكل التعويض المتعطل لكن سلوك الدالتين مختلف. المطلوب تفحص التعبير المسموح حوالين النقطة. خلينا نجرب مسألة تحليل جديدة من غير ما أوريك عواملها.

## Independent attempt Q-D1 — not spoken as heading
**Question spoken (English):** Evaluate $\lim_{x\to4}(x^2-16)/(x-4)$. Explain why direct substitution is insufficient.
**Question spoken (Arabic support):** احسب نهاية إكس تربيع ناقص ستة عشر على إكس ناقص أربعة لما إكس تقترب من أربعة، واشرح ليه التعويض المباشر مش كفاية.
**Attempt:** written; no factorization or numerical answer before attempt.

### Post-attempt feedback D1 — separate spoken text
**Model answer (English):** The limit is $8$. Factor $x^2-16=(x-4)(x+4)$ for $x\ne4$.
**Feedback spoken:** التعويض الأول يطلع صفر على صفر. نحلل فرق المربعين، ونبسط العامل إكس ناقص أربعة بعيد عن النقطة نفسها، فيبقى إكس زائد أربعة. ولما إكس تقرب من أربعة، التعبير يقرب من تمانية. الدالة الأصلية لسه مش معرفة عند أربعة.

## Connected spoken continuation — the conjugate is another algebraic bridge

مش كل بسط بيتحلل كفرق مربعين واضح. لو عندنا $\lim_{x\to0}(\sqrt{x+4}-2)/x$، التعويض برضه يطلع صفر على صفر. نضرب البسط والمقام في **المرافق** $\sqrt{x+4}+2$. فوق نحصل على $(x+4)-4=x$، وبعيدًا عن إكس صفر نختصرها، فالتعبير يبقى $1/(\sqrt{x+4}+2)$. لما إكس تقرب من صفر، المقام يقرب من أربعة، والنهاية ربع. لاحظ إننا ضربنا في مقدار مناسب عشان نبسط الفرق بين جذر وعدد؛ ما قالش إن التعبير القديم معرف عند الصفر.

حاول أنت دلوقتي تستخدم المرافق في مثال فيه معامل جديد تحت الجذر، وفسر شرط الاختصار.

## Independent attempt Q-D3 — separate rationalization transfer
**Question spoken (English):** Evaluate $\displaystyle\lim_{x\to0}\frac{\sqrt{2x+9}-3}{x}$ by algebraic manipulation, and explain the restriction used when cancelling $x$.
**Question spoken (Arabic support):** احسب نهاية الجذر التربيعي لاتنين إكس زائد تسعة ناقص تلاتة، الكل على إكس، لما إكس تقرب من صفر. استخدم تبسيط جبري واشرح امتى ينفع نختصر إكس.
**Attempt:** written; reveal neither conjugate nor answer until after submission.

### Post-attempt feedback D3 — separate spoken text
**Model answer (English):** Multiply by the conjugate; for $x\ne0$, the expression becomes $\frac{2}{\sqrt{2x+9}+3}$, so the limit is $\frac13$.
**Feedback spoken:** الضرب في المرافق يخلي البسط اتنين إكس، فنقدر نختصر إكس مع المقام **لما إكس مش صفر**؛ والنهاية بتدرس القيم القريبة غير المساوية للصفر. اللي يتبقى اتنين على الجذر زائد تلاتة. عند الاقتراب من الصفر المقام يقرب من ستة، فالناتج تلت. ما قلناش إن الكسر الأصلي معرف عند إكس صفر.

## Connected spoken continuation — denominator approaching zero is a different situation

في حالة تالتة، التبسيط مش هيديك نهاية حقيقية محددة. مثلًا $1/x$ لما إكس تقرب من صفر: من اليمين إكس موجبة وصغيرة جدًا، فالناتج موجب وكبير بلا حد. من الشمال إكس سالبة وصغيرة جدًا في المقدار، فالناتج سالب ومقداره يكبر بلا حد. بنرمز للسلوك ده بموجب أو سالب ما لا نهاية، لكن **ما لا نهاية مش عدد حقيقي بنعوّض بيه**. عشان كده ماينفعش نقول إن فيه نهاية حقيقية واحدة من الجهتين.

لو البسط والمقام قربوا من غير ما المقام يثبت بعيدًا عن صفر، لازم نحلل سلوك الإشارة والقيمة بدل استخدام قانون القسمة آليًا. مثلًا عند $1/(x-2)$، يمين اتنين المقام موجب وشمال اتنين سالب، فالاتجاهين مختلفين. ده بيفسّر ليه بعض مسائل النهايات محتاجة Left-hand وRight-hand limit مش مجرد عملية تعويض.

اختبر نفسك في موقف فيه النقطة الممنوعة متحركة بعيدًا عن الصفر، واكتب تفسير كل اتجاه.

## Independent attempt Q-D4 — separate one-sided rational-limit transfer
**Question spoken (English):** Describe the left-hand and right-hand behavior of $f(x)=\frac{1}{x-2}$ as $x$ approaches $2$. Does a finite two-sided limit exist?
**Question spoken (Arabic support):** اوصف سلوك واحد على إكس ناقص اتنين لما إكس تقرب من اتنين من الشمال واليمين. هل فيه نهاية حقيقية محددة من الناحيتين؟
**Attempt:** written; conceal signs and nonexistence statement until response.

### Post-attempt feedback D4 — separate spoken text
**Model answer (English):** From the left, $f(x)\to-\infty$; from the right, $f(x)\to+\infty$. No finite two-sided limit exists.
**Feedback spoken:** قبل اتنين مباشرة، المقام سالب وصغير جدًا، فالكسر قيمته سالبة ومقدارها بيكبر بلا حد. بعد اتنين المقام موجب وصغير جدًا، فتكون القيم موجبة وبتكبر بلا حد. الجهتين مش بيقربوا من نفس عدد حقيقي، وبالتالي مفيش نهاية حقيقية محددة من الناحيتين. علامة ما لا نهاية هنا بتوصف السلوك، مش قيمة نعوض بيها في الدالة.

## Closing spoken recap

بقى عندنا مسار قرار: هل التعبير منتظم عند النقطة؟ التعويض غالبًا ينفع. لو ظهر $0/0$، ده إنذار نفحص تحليلًا أو مرافقًا، مع الاختصار **على المدخلات القريبة المسموح بها فقط**. لو المقام بيقرب من صفر ومفيش إلغاء يزيل المشكلة، نشوف الإشارة من الجهتين ونرفض فكرة إن ما لا نهاية قيمة تعويض. الدرس الجاي هنستعمل نفس معنى النهاية، لكن مع قانون خاص بالدوال المثلثية **بوحدة الراديان**.

## Rough visual proposals — not scene assets

Substitution cards show \`0/0\` as unresolved; algebraic factor cancellation with a persistent missing point; conjugate paired rectangles; separate left/right signed number lines. Questions reveal solution only post-attempt.
