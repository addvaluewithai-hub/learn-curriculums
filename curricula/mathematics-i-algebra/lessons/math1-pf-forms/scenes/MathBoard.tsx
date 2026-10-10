import React from 'react';
import { AbsoluteFill } from 'remotion';
import { cueIsVisible, type VisualProps } from '@learn/lesson-runtime';

// Stage 04 editable visual component; unrendered until media/timing review.
// Storyboards in scenes/*.json define the independent responsive intention.
const panels = [
  { cue: "S01-U01", label: "ابدأ بالمقام", formula: "Proper fraction → factor Q(x)", note: "ابدأ من: في الدرس السابق فهمنا إن نفس الكسر ممكن نكتبه مجموع كسور أبسط من" },
  { cue: "S01-U02", label: "ابدأ بالمقام", formula: "Choose the general form before coefficients", note: "ثم راجع: لكن فيه سؤال منطقي: هنقرر كم كسر نكتب، وكل كسر مقامه إيه" },
  { cue: "S02-U01", label: "عوامل خطية مختلفة", formula: "(x−1)(x+4)", note: "ابدأ من: ابدأ بأبسط حالة: عندك مقام (x-1)(x+4). فيه عاملان خطيان مختلفان؛ خطي يعني أعلى" },
  { cue: "S02-U02", label: "عوامل خطية مختلفة", formula: "A/(x−1) + B/(x+4)", note: "ثم راجع: فيه عاملان خطيان مختلفان؛ خطي يعني أعلى درجة فيه واحد" },
  { cue: "S03-U01", label: "عامل خطي مكرر", formula: "(x−2)²", note: "ابدأ من: لكن لو عامل واحد متكرر، الصورة بتختلف. خذ (x-2)^2 في المقام. مينفعش نكتفي" },
  { cue: "S03-U02", label: "عامل خطي مكرر", formula: "A/(x−2) + B/(x−2)²", note: "ثم راجع: خذ (x-2)^2 في المقام" },
  { cue: "S04-U01", label: "تربيعي غير قابل للتحليل", formula: "x²+1 (over real numbers)", note: "ابدأ من: طيب إيه اللي يحصل لو المقام فيه إكس تربيع زائد واحد؟ العامل ده" },
  { cue: "S04-U02", label: "تربيعي غير قابل للتحليل", formula: "(Ax+B)/(x²+1)", note: "ثم راجع: العامل ده quadratic، درجته اتنين" },
  { cue: "S05-U01", label: "تكرار التربيعي", formula: "(x²+1)²", note: "ابدأ من: ولو عامل تربيعي غير قابل للتحليل متكرر، بنعمل نفس قاعدة كل قوة لها" },
  { cue: "S05-U02", label: "تحليل المقام ورسم صورة الكسور", note: "ثم راجع: يعني لو المقام فيه (x^2+1)^2، هنكتب \\frac{Ax+B}{x^2+1}+\\frac{Cx+D}{(x^2+1)^2}" },
  { cue: "S06-U01", label: "تحليل المقام ورسم صورة الكسور", note: "ابدأ من: تعالى نطبّق توجيهيًا على مثال من إعدادنا: \\frac{2x+3}{(x-1)(x+4)^2}. أولًا Proper لأن البسط درجة" },
  { cue: "S06-U02", label: "قالب مختلط للتدريب", formula: "A/(x−1)+B/(x+4)+C/(x+4)²", note: "ثم راجع: أولًا Proper لأن البسط درجة واحد والمقام درجة تلاتة" },
  { cue: "S09-U01", label: "لخص القالب", formula: "Linear → constant numerator", note: "ابدأ من: الدرس ده خلّاك تعرف تكتب شكل الحل قبل ما تحسبه. دي مهارة مستقلة؛" },
  { cue: "S09-U02", label: "لخص القالب", formula: "Irreducible quadratic → linear numerator", note: "ثم راجع: دي مهارة مستقلة؛ مش لازم تخلص كل الحسابات عشان تعرف إنك فاهم قاعدة" },
];

export default function MathBoard(props: VisualProps) {
  const { recording, frame, fps, layout, phase } = props;
  const portrait = layout === 'portrait';
  // This component is used for teaching only. Questions use the SDK question board.
  const visible = phase === 'feedback' || phase === 'question-reading'
    ? []
    : panels.filter((p) => cueIsVisible(recording, p.cue, frame, fps));
  const active = visible.length ? visible[visible.length - 1] : null;
  return (
    <AbsoluteFill style={{ backgroundColor: '#0e1826', color: 'white', padding: portrait ? 22 : 48, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: portrait ? 18 : 28, overflow: 'hidden', fontFamily: 'sans-serif' }}>
      <div style={{fontSize: portrait ? 17 : 24, opacity: .8, letterSpacing: 1}}>Mathematics I · Partial Fractions</div>
      <div style={{height: 3, width: portrait ? '45%' : '25%', backgroundColor: '#67e8f9'}} />
      <div style={{display: 'grid', gridTemplateColumns: portrait ? '1fr' : '1fr 1fr', gap: 18, alignItems: 'center'}}>
        <div style={{fontSize: portrait ? 31 : 45, fontWeight: 700, lineHeight: 1.3, overflowWrap: 'anywhere'}} dir="rtl">
          {active?.label || 'تابع الفكرة خطوة بخطوة'}
        </div>
        <div style={{fontSize: portrait ? 19 : 27, lineHeight: 1.5, padding: portrait ? 16 : 28, backgroundColor: '#17283d', borderRadius: 18, border: '1px solid #37506a'}} dir="rtl">
          {active?.note || 'العناصر تظهر مع الشرح المسموع'}
        </div>
      </div>
      <div style={{ direction: 'ltr', textAlign: 'center', padding: portrait ? 14 : 24, borderRadius: 14, background: '#102f3e', border: '1px solid #1d7f96', fontFamily: 'monospace', fontSize: portrait ? 17 : 29, lineHeight: 1.45, overflowWrap: 'anywhere' }}>{active?.formula || 'P(x) / Q(x)'}</div>
      <div style={{fontSize: portrait ? 14 : 17, opacity: .66}} dir="rtl">كشف تدريجي مرتبط بوحدات المعنى؛ العرض الفعلي والتوقيتات ينتظران مراجعة التسجيل.</div>
    </AbsoluteFill>
  );
}
