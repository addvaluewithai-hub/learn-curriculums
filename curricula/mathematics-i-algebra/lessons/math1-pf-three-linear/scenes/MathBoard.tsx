import React from 'react';
import { AbsoluteFill } from 'remotion';
import { cueIsVisible, type VisualProps } from '@learn/lesson-runtime';

// Stage 04 editable visual component; unrendered until media/timing review.
// Storyboards in scenes/*.json define the independent responsive intention.
const panels = [
  { cue: "S01-U01", label: "ثلاثة عوامل", formula: "x³+x²−6x", note: "ابدأ من: في الدرس السابق شفت إن عندنا عاملين خطيين مختلفين، فكتبنا كسرين بمجهولين A" },
  { cue: "S01-U02", label: "ثلاثة عوامل", formula: "x(x−2)(x+3)", note: "ثم راجع: النهارده ما هنغيرش المنهج، لكن هنزود عاملًا خطيًا ثالثًا" },
  { cue: "S02-U01", label: "الصورة العامة", formula: "A/x + B/(x−2) + C/(x+3)", note: "ابدأ من: دلوقتي المقام فيه ثلاثة عوامل خطية مختلفة: إكس، وإكس ناقص اتنين، وإكس زائد" },
  { cue: "S02-U02", label: "الصورة العامة", formula: "x+1=A(x−2)(x+3)+Bx(x+3)+Cx(x−2)", note: "ثم راجع: إذن نكتب الصورة: A على إكس، زائد B على إكس ناقص اتنين، زائد" },
  { cue: "S03-U01", label: "فك الأقواس", formula: "(x−2)(x+3)=x²+x−6", note: "ابدأ من: الخطوة الجديدة هنرتب فيها الحدود حسب قوة إكس. افتكر فك الأقواس: (x-2)(x+3)=x^2+x-6، و" },
  { cue: "S03-U02", label: "فك الأقواس", formula: "(A+B+C)x²+(A+3B−2C)x−6A", note: "ثم راجع: افتكر فك الأقواس: (x-2)(x+3)=x^2+x-6، و x(x+3)=x^2+3x، و x(x-2)=x^2-2x" },
  { cue: "S04-U01", label: "مطابقة المعاملات", formula: "A+B+C=0", note: "ابدأ من: يبقى المعادلات عندنا: A زائد B زائد C تساوي صفر. وA زائد تلاتة" },
  { cue: "S04-U02", label: "مطابقة المعاملات", formula: "A+3B−2C=1 ; −6A=1", note: "ثم راجع: وA زائد تلاتة B ناقص اتنين C تساوي واحد" },
  { cue: "S05-U01", label: "الحل الصحيح", formula: "A=−1/6 ; B=3/10 ; C=−2/15", note: "ابدأ من: يبقى الناتج الكامل: سالب واحد على ستة إكس، زائد تلاتة على عشرة في" },
  { cue: "S05-U02", label: "الحل الصحيح", formula: "Check the signs before summing", note: "ثم راجع: بالصيغة الرياضية الواضحة: سالب واحد على ستة مضروبًا في واحد على إكس، زائد" },
  { cue: "S06-U01", label: "طريقة تحقق أخرى", formula: "x=0 → A=−1/6", note: "ابدأ من: طيب نقدر نراجع المعاملات بطريقة مختلفة؟ أيوه، وده تأكيد مش طريقة سحرية. ارجع" },
  { cue: "S06-U02", label: "طريقة تحقق أخرى", formula: "x=2 → B=3/10 ; x=−3 → C=−2/15", note: "ثم راجع: أيوه، وده تأكيد مش طريقة سحرية" },
  { cue: "S09-U01", label: "مهارتان متكاملتان", formula: "Compare coefficients", note: "ابدأ من: من البداية للنهاية المسألة فيها نفس المنطق اللي اتعلمته: تصنيف Proper، تحليل المقام،" },
  { cue: "S09-U02", label: "مهارتان متكاملتان", formula: "Check using the polynomial identity", note: "ثم راجع: الجديد النهارده إننا تعلّمنا Comparing Coefficients بثلاثة عوامل مختلفة، وشوفنا إزاي نربط المعاملات" },
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
