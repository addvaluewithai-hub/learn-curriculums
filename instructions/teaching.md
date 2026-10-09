# Teaching contract

## 1. Source, learner, and concept readiness

- Follow [human stage gates](stage-gates.md) and the [curriculum planning workflow](curriculum-planning.md): source analysis → provisional lesson map → connected working drafts **(Stage 01, stop)** → critique and rewrite **(Stage 02, stop)** → boundary decision/final scripts **(Stage 03, stop)** → scenes **(Stage 04)**. An original textbook section need not become one student lesson.

- Resolve audience, level, stable lesson ID/order, objectives, prerequisites, actual source availability and course language policy before authoring.
- Inspect original sources when available; cite exact locators. Old page-reviewed notes alone do not prove current access to the original. Preserve source wording/conditions, limits, units, and source inconsistencies; independently check numerical/scientific answers.
- Separate source-grounded facts from **original teaching analogies**. Label additional claims not in the source and verify them independently or flag for specialist review; never present invented examples as printed textbook exercises.
- For every objective, map prerequisite concepts in the order they become necessary. Mark each as **established**, **brief bridge needed**, **new concept taught here**, or **reserved for a later lesson**.
- Do not assume that a common expert word is familiar to a novice. Explain essential terms at first need using observation/experience; give only the minimal bridge needed now, not an accidental full lesson on a future topic. Record genuinely uncertain prerequisites.

## 2. Design the teaching journey first

- Plan a meaningful opening/problem → familiar example → observation → reason → contextual definition → guided application → independent attempt → explanatory feedback → recap.
- These are instructional responsibilities, **not required separate screens**. Plan rough visual beats during the learning architecture; a diagram can reveal an unclear explanation and prompt rewriting before scene implementation.
- Identify likely misconceptions and correct them with justified conditions. Avoid shortcuts that become false when the conditions change.
- Map **each** objective to teaching and a truly independent assessment, ideally using a new but comparable scenario rather than only repeating the demonstrated example. Label same-example guided checks as practice, not proof of transfer.
- Introduce every checkpoint naturally (“دلوقتي خلينا نجرب سؤال قصير عشان نتأكد إن الفكرة واضحة.” is one example); vary transitions and avoid abrupt isolated exam sentences.

## 3. Write a continuous working script before scene JSON

- Draft the **complete coherent spoken teaching journey** for each provisional lesson as one connected working narrative; test whether transitions and examples carry understanding. Natural paragraphs, editorial headings and question/attempt boundaries are allowed: 'continuous' means no forced production scenes, not an unstructured wall of words. A master draft is an **editorial method**, not a new runtime schema or required extra deliverable.
- Do not wait until the entire curriculum has been drafted. Work in source-grounded chapters or manageable neighboring-lesson blocks, then reconsider each proposed boundary before locking production scripts.
- Mark question/learner-attempt/feedback boundaries clearly in working material. Write questions and feedback separately: the model answer may **never** appear in question audio, spoken options as hints, or pre-attempt visuals.
- Keep directions, timestamps and headings outside spoken text; TTS must receive speech only.
- Think visually while drafting; defer final scene structure, word-anchored semantic units and responsive storyboards until the narrative has passed critique.
- **After decomposition, scenes/*.json narration and question.feedback scripts are the canonical words.** Never keep an independently edited master script alongside them. Any continuous reading copy must be regenerated from canonical clips, preserve speech verbatim and show non-spoken question/attempt/feedback boundaries.
- Compare the decomposed clips with the reviewed working draft for missing conditions, transitions, English terms, assessments and feedback. Revisit critique if wording or meaning changes.
- For **script-only** requests, return only the requested script. Do not synthesize audio, scaffold scenes, or create visual artifacts unless asked.

## 4. Natural bilingual comprehension

- Obey the course language policy: default Egyptian Arabic explanation, English technical vocabulary and exam questions/model answers with Arabic support. Do not impose subject-specific jargon across curricula.
- **Build the meaning before or around the English term.** Introduce a relatable action or observation and attach the English label after the learner has a usable concept. Never abandon an essential English phrase untranslated in meaning, and never force literal word-by-word translations.
- A *method example* (not mandatory copy): “لما تزق الباب أو تشده، إنت كده بتأثر عليه بقوة. التأثير اللي بنسميه Force ممكن يغيّر حركة الجسم أو شكله حسب الظروف.” Scientifically verify each example's nuance for its actual topic.
- For exam questions, voice the English wording clearly, then support comprehension in natural Arabic within the question clip; reveal clauses with their spoken onset. Keep answers hidden until submission.
- Feedback is a **separate** clip with a useful English model answer, an accessible Arabic explanation **and the reasoning**. Avoid long English-only boilerplate, mechanical repetitive translation and false personalized praise about an unseen answer.
- Introduce glossary words as needed, not in a front-loaded wall of definitions. Reuse technical English when it helps student recognition.

## 5. Treat length and cognitive load as design trade-offs

- Do not target a fixed duration, word count, or number of scenes. Preserve essential causal bridges and practice; trim padding and repeated examples that do not add new understanding.
- A long coherent lesson can contain brief conceptual segments and attempts. If several distinct groups of unfamiliar concepts each demand their own explanation, misconception, application and checkpoint, evaluate a lesson split or explicit internal learning parts instead of simply shortening the script.
- Decide **split vs internal chunks vs keep** from prerequisite dependencies, conceptual unity, fatigue risk and independent assessment opportunities; one textbook heading and a long transcript alone are neither sufficient nor necessary evidence.
- Duration estimates are not measured audio; use actual delivered WAV duration for playback.
- Don't cut a necessary explanation just to meet an arbitrary time quota; don't expand every assumed prerequisite into a full adjacent lesson.

## 6. Critique, rewrite and show evidence

This is **Stage 02 after a separate human `next`**, not an automatic continuation of Stage 01. Before formal scene decomposition, review the **whole connected narrative**:
1. **Novice gaps:** Which essential term or step occurs before it can be understood? Cite the specific passage and the smallest adequate bridge.
2. **Source/science:** Which claim lacks source evidence, overgeneralizes, loses a condition/unit or gives an unverified answer? Name the locator or uncertainty.
3. **Teaching/transfer:** Is each objective taught and checked independently in a non-identical context? Are likely misconceptions actually addressed?
4. **Bilingual/read-aloud:** Is English meaningful in context, is Egyptian Arabic natural, and would a human speak this sentence? Remove mechanical translation and pointless repetition.
5. **Visual/interaction:** Is a helpful diagram missing? Is an answer inadvertently disclosed before a valid attempt? Is recorded feedback explanatory rather than falsely personalized?
6. **Cognitive load / boundary:** Does this draft introduce multiple independently teachable concept clusters or too many new demands between attempts? Should it stay intact, gain short internal parts, split, merge or move a bridge to a neighboring lesson? Explain the decision without a fixed minute/word cap.

- Fix substantive findings, then reconsider the provisional lesson boundaries **before** converting drafts to scenes. If the map changes, rewrite each resulting lesson as a coherent teaching journey with its own meaningful opening, teaching/application, attempts, feedback and recap: never cut a long transcript mechanically into unrelated pieces.
- Re-check specific passages and boundary decisions. Record findings, revisions, unresolved issues and actual review scope in STATUS.md or the lesson PR; don't invent issues or claim a quality score proves success.
- AI self-critique is **editorial work**, not an independent scientific or learner test. Do not mark review.json `passed` without real reviewer/evidence bound to the current source hash.
- Follow [subject-specific notes](subject-notes/chemistry-density.md) only for relevant subject matter; generic instructions must not force chemistry rules onto statics or other curricula.

## 7. Teaching quality gate before audio batch

Show objective/scene/passage evidence for the following questions:
- **Concept readiness:** are critical terms taught or bridged at first use, with future lessons kept in scope?
- **Scientific and source fidelity:** are original examples labeled, quantities/conditions accurate, uncertainties disclosed?
- **Coherence:** can the learner follow one connected arc from the problem to the explanation and recap?
- **Language:** can a learner understand the English vocabulary/questions without literal-translation overload?
- **Assessment:** is every objective independently tested and its model answer concealed before attempt?
- **Efficiency and load:** does each example/paragraph add understanding? Are novel concept clusters spaced with explanation and application? Was a defensible keep/chunk/split/merge boundary decision recorded?
- **Production fidelity:** are reviewed words, independent feedback, exact anchors and two responsive storyboards retained during splitting?

The structural `validate --stage script` is necessary but **does not prove** educational/scientific quality. For source/teaching checks, provide real human reviewer/evidence before marking `passed`; otherwise leave `untested` and record blockers. Follow [audio guidance](audio.md) for a bilingual/value pilot before any authorized batch. Script-only requests never trigger synthesis.
