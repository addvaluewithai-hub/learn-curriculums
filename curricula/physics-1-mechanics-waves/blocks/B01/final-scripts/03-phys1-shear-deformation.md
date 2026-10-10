# B01 — Final connected script 03 | Shear: القص وتشوه الأوجه

- **Issued lesson ID:** phys1-shear-deformation
- **Curriculum order:** 803 | **English title:** Shear Deformation and Shear Modulus
- **Stage:** 03, complete continuous editorial script for a distinct student lesson; scenes not created.
- **Source locators:** phys1-main-scan PDF p.7 = printed 125 (moduli overview), PDF p.9 = printed 128 (shear diagram), PDF pp.10–11 = printed 130–133 (types of engineering exercises only).
- **Objectives:** O1 recognize tangential force and simple shear instead of axial elongation; O2 explain shear stress and engineering strain under simple-shear assumptions; O3 solve for shear modulus S/G and apply it independently.
- **Prerequisites:** Lessons phys1-solid-structure-stress-strain and phys1-young-axial-stiffness; force, area, SI units; recall stress/strain. Young's detailed computations are not required to solve shear.
- **Authored teaching extensions:** uniform simple-shear approximation, theta relationship, values and scenarios; not verbatim printed exercises.
- **Non-spoken:** headings and Attempt/Feedback boundaries mark editorial function, no scenes/clip IDs yet.

## نص الشرح المتصل

تخيل إن قدامك بلوك مطاطي فوق ترابيزة. لو شديته رأسيًا على امتداد طوله، إحنا عارفين إننا نراقب زيادة الطول ونفكر في Young's Modulus. لكن دلوقتي بدل ما نشده لفوق، هنثبت القاعدة وندفع الوجه العلوي على جنب بقوة أفقية. تخيل إن الحافة اللي فوق اتحركت يمين، والحافة اللي تحت فضلت مكانها. كده الجسم مش بيتطول بمحوره بنفس الفكرة القديمة؛ شكله نفسه بيميل. التغير ده بنسميه Shear deformation، أو تشوه القص.

ليه الفرق ده مهم في الهندسة؟ لأنك هتقابل أجزاء بتتحمل قوى موازية لأسطحها، ومش هتعرف تحلها صح بقانون الاستطالة الطولية. قبل ما تكتب قانون، لازم تسأل: اتجاه القوة إيه بالنسبة للوجه اللي بتأثر عليه؟ في شد القضيب، القوة محورية على مساحة مقطع عمودية عليها. إنما في القص، قوة Tangential أو مماسية، يعني **موازية** للسطح المؤثر عليه. وده بيفسر ليه أبعاد جديدة هتدخل في حساب الاستجابة.

خلي الرسم في بالك: بلوك ارتفاعه h، وجهه السفلي مثبت بفعل رد مناسب، ووجهه العلوي مساحته A. أثرنا عليه بقوة موازية F. علشان نقيس متوسط Shear stress بنستخدم مقدار القوة الموازية مقسومًا على مساحة الوجه: τ = F/A. الوحدة زي أي إجهاد هي Newton per square metre، أو Pascal. ده إجهاد قص **متوسط في الحالة المبسطة**، ومش هنعتبر إن توزيعه متساوٍ محليًا في أي جسم حقيقي مهما كان شكله.

الجزء الجديد بقى هو Shear strain. احنا مش بنقيس تغير طول قضيب؛ بنقيس مقدار إزاحة الوجه العلوي بالنسبة للسفلي. لو الوجه اللي فوق اتحرك مسافة Δx والارتفاع الأصلي للبلوك h، في **نموذج قص بسيط منتظم تقريبًا** نكتب انفعال القص الهندسي γ = Δx/h. النسبة من غير وحدة. لو تخيلنا زاوية الميل θ، هندسيًا في النموذج ده tanθ = Δx/h، ولما زاوية الميل صغيرة ومقاسة بالراديان، θ تقارب γ. عشان كده تلاقي أحيانًا علاقة بالزاوية بدل الأطوال. بس متخلطش التقريب الصغير مع تشوهات كبيرة أو قص غير منتظم.

ودلوقتي عايزين نوصل Stress إلى Strain. زي ما في الشد كان عندنا Young's Modulus، في القص عندنا Shear Modulus، والكتاب بيستعمل الرمز S، بينما بعض المراجع الهندسية بتستعمل G. في المجال المرن الخطي نكتب τ = S γ. وبالتالي S = τ/γ، وفي بلوك القص البسيط S = (F/A)/(Δx/h). ولاحظ وحدة S: Stress بالباسكال وStrain من غير وحدة، فالمعامل بالباسكال. لو S أكبر وتحت نفس إجهاد القص وفي نفس ظروف الاختبار، انفعال القص أصغر؛ دي مقاومة القص المرنة وليست تلقائيًا إجهاد الكسر.

تعال نمسك مثال من تأليفنا خطوة خطوة. بلوك ارتفاعه 0.10 متر ومساحة الوجه العلوي 0.020 متر مربع. قوة أفقية مقدارها 60 نيوتن تسببت في إزاحة جانبية صغيرة للوجه العلوي مقدارها 0.20 ملّيمتر، وافترض قصًا بسيطًا شبه منتظم في المجال المرن. أول خطوة: تحويل 0.20 ملّيمتر إلى 0.00020 متر. تاني خطوة: Shear stress = 60 ÷ 0.020 = 3000 Pascal. تالت خطوة: Shear strain = 0.00020 ÷ 0.10 = 0.002 بلا وحدة. وأخيرًا S = 3000 ÷ 0.002 = 1.5 × 10⁶ باسكال.

دلوقتي عايزك تتأكد من معنى كل طول، لأن ده مكان خطأ متكرر. الارتفاع h هو المسافة بين الوجه اللي بيتحرك والوجه المثبت، مش طول أي ضلع في الصورة. وΔx هي الحركة الجانبية **النسبية** بين الوجهين، مش الاستطالة المحورية. لو استخدمت ΔL/L0 بالصدفة من مسألة Young، هتبقى غيرت نوع التشوه قبل ما تبدأ الحل. الرسم هنا ضروري علشان تعرف اتجاه الحمل وتحدد الأبعاد الصح.

سؤال قصير قبل التطبيق: لو زوّدنا مساحة الوجه للضعف مع ثبات القوة والارتفاع ومعامل المادة، إيه اللي يحصل للإجهاد والإزاحة في النموذج البسيط؟ الإجهاد F/A هيقل للنصف. والانفعال τ/S هيقل للنصف، ومع ثبات h، الإزاحة الجانبية Δx تقل للنصف. ده مش قانون إضافي؛ ده قراءة واعية للعلاقات. ولو زوّدنا الارتفاع مع ثبات الإجهاد ومعامل المادة، نفس γ ممكن يقابله Δx أكبر؛ الأبعاد الهندسية مهمة زي ما شفنا في القضيب الطولي.

قبل السؤال النهائي، نحدد شروطنا علشان أي حد يسمع يقدر يعرف متى يصح القانون: بنفترض بلوك تقريبي الأوجه مستوية، قاعدة مثبتة، قوة موازية للوجه، التشوه صغير، وتوزيع القص منتظم على نحو يسمح بوصف متوسط، وسلوك مرن خطي. مسائل تانية فيها التواء أو انحناء محتاجة علاقات إضافية؛ مش هنرمي عليها S = Fh/(AΔx) لمجرد وجود قوة.

## [Attempt 01 — سؤال مستقل حسابي]

**English exam question:** A block has height 0.15 m and a top-face area of 0.030 m². Its bottom face is fixed. A tangential force of 90 N shifts the top face sideways by 0.30 mm. Assuming uniform, small, linear-elastic simple shear, calculate the average shear stress, engineering shear strain and shear modulus.

بالعربي: بلوك ارتفاعه 0.15 متر، مساحة وجهه العلوي 0.030 متر مربع، وقوة قص أفقية 90 نيوتن. السطح العلوي اتحرك 0.30 ملّيمتر. احسب إجهاد القص، انفعال القص، ومعامل القص. اكتب الرسم واتجاه القوة وبيانات الوحدات قبل ما تسمع الإجابة.

## [Feedback 01 — بعد المحاولة فقط]

**English model answer:** τ = 90/0.030 = 3000 Pa. γ = 0.00030/0.15 = 0.002. S = τ/γ = 1.5 × 10⁶ Pa.

بدأنا بتحديد إن الحمل موازي للوجه، مش شد محوري. الإجهاد 3000 باسكال، والانفعال 0.002 بدون وحدة، ومعامل القص مليون ونص باسكال. اتحقق إنك حولت 0.30 ملّيمتر إلى 0.00030 متر، واستخدمت الارتفاع 0.15 متر في المقام.

## [Attempt 02 — سؤال انتقال مفاهيمي]

**English exam question:** Two blocks of the same material and height are subjected to equal tangential forces. Block B has twice the loaded-face area of block A. Compare their average shear stresses and their sideways displacements in the same linear simple-shear approximation.

بالعربي: بلوكين نفس المادة ونفس الارتفاع ونفس القوة المماسية، لكن مساحة الوجه في B ضعف A. قارن إجهاد القص والإزاحة الجانبية للسطحين. جاوب بالتفسير قبل ما تطلع نسب.

## [Feedback 02 — بعد المحاولة فقط]

**English model answer:** Block B has half the average shear stress of A, half the shear strain and half the sideways displacement.

بما إن τ = F/A، المساحة الأكبر بنص الإجهاد عند نفس القوة. ولأن المادة نفسها وS ثابت في الفرض، γ = τ/S تنخفض للنصف. الارتفاع نفسه h، فـΔx = γ h ينخفض للنصف برضه. ده اختبار فهم لمساحة الوجه وتأثيرها بدل حفظ رقم واحد.

## خاتمة وربط

بدأنا بحركة وجه فوق بالنسبة لوجه تحت، وميزنا القوة الموازية للوجه عن قوة الشد المحورية. بعدها عرفنا Shear stress وShear strain ومعامل القص S، وحسبنا مثالًا وحلينا حالة جديدة بنفس المنطق. وبكده بقيت تعرف تختار بين استطالة طولية وبين إزاحة جانبية من شكل الحمل. في الدرس اللي جاي هنتحول لتأثير تالت: ضغط ييجي من كل الاتجاهات ويغير الحجم، مش مجرد طول أو ميل؛ وده Bulk Modulus.

## Editor-only coverage / review
- O1 → opening and load-direction classification, Attempt 02; O2 → derivation, worked and Attempts 01/02; O3 → formula and independent Attempt 01.
- Source printed p.128 supports simple shear depiction. Numeric values and angle explanation are authored.
- θ≈γ requires small angular shear; γ=Δx/h is the engineering ratio in the assumed uniform simple-shear geometry. Source scientific review still untested; no scenes or audio.
