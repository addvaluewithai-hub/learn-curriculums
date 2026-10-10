import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

// Stage 04 authored source only; source-specific playback and font/device QA untested.
export default function ConceptBoard(props: VisualProps) {
  const {frame, fps, recording, layout, question, answer, phase} = props;
  const portrait = layout === "portrait";
  const focus = (props as unknown as {spec?:{params?:{focus?:string}}}).spec?.params?.focus;
  const show1 = cueIsVisible(recording, "U01", frame, fps);
  const show2 = cueIsVisible(recording, "U02", frame, fps);
  const show3 = cueIsVisible(recording, "U03", frame, fps);
  const qparts = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const asked = question && phase !== "question-reading" ?
    [{text:question.english},{text:question.title}]:qparts;
  const feedback = phase === "feedback" ? answer?.parts?.filter(part =>
    frame * 1000 / fps >= part.atMs) ?? [] : [];
  const card = {width:"100%", boxSizing:"border-box" as const,
    background:"white", borderRadius:18, padding:portrait?18:28};
  return <AbsoluteFill style={{background:"#f8fafc", padding:portrait?18:30,
    display:"flex", flexDirection:"column", justifyContent:"center", gap:portrait?12:18,
    color:"#0f172a", fontFamily:"sans-serif", overflow:"hidden"}}>
    <div dir="rtl" style={{fontSize:portrait?23:30,fontWeight:700}}>الدوال المثلثية والأسية واللوغاريتمية</div>
    {phase==="feedback" ? <div style={card}>
      {feedback.map((p,i)=><p key={i} dir="auto" style={{fontSize:portrait?22:27,
        overflowWrap:"anywhere",lineHeight:1.5}}>{p.text}</p>)}
    </div> : question ? <div style={card}>
      {asked.map((p,i)=><p key={i} dir="auto" style={{fontSize:portrait?22:27,
        overflowWrap:"anywhere",lineHeight:1.5}}>{p.text}</p>)}
    </div> : <div style={{...card,display:"flex",alignItems:"center",
      flexDirection:portrait?"column":"row",gap:portrait?8:22}}>
      <svg viewBox="0 0 560 230" role="img" aria-label="Mathematics concept sketch"
        style={{width:"100%",flex:1,minWidth:0,maxHeight:portrait?158:240}}>
        <><path d="M24 118 H535 M25 18 V212" stroke="#64748b" strokeWidth="3"/>{show1&&<path d="M30 114 C63 37 108 37 148 114 S232 194 274 114 S356 37 397 114 S471 194 530 114" fill="none" stroke="#2563eb" strokeWidth="4"/>}{show2&&<path d="M30 190 C138 187 212 166 299 132 S424 75 521 28" fill="none" stroke="#059669" strokeWidth="4"/>}{show3&&<path d="M278 19 V218" stroke="#dc2626" strokeWidth="3" strokeDasharray="7 7"/>}</>
      </svg>
      <div dir="rtl" style={{flex:1,minWidth:0,width:"100%",fontSize:portrait?20:26,
        lineHeight:1.48,overflowWrap:"anywhere",fontWeight:600}}>
        {show1?focus:" "}
      </div>
    </div>}
    <div dir="rtl" style={{fontSize:portrait?16:19,color:"#475569"}}>
      {phase==="feedback"?"تفسير الإجابة بعد المحاولة":
        question?"السؤال ومحاولة مستقلة قبل الحل":"الرسم يتدرج مع وحدات النطق بعد مراجعة التوقيت"}
    </div>
  </AbsoluteFill>;
}
