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
    <div dir="rtl" style={{fontSize:portrait?23:30,fontWeight:700}}>الدالة والمجال والمدى والاختبار الرأسي</div>
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
        <><circle cx="125" cy="116" r="80" fill="#eff6ff" stroke="#2563eb" strokeWidth="3"/><circle cx="426" cy="116" r="80" fill="#ecfdf5" stroke="#059669" strokeWidth="3"/>{[-1,0,1].map((x,i)=><g key={x}><circle cx="121" cy={72+i*45} r="9" fill="#2563eb"/><text x="95" y={78+i*45} fontSize="20">{x}</text></g>)}{show1&&<path d="M138 72 Q270 29 408 72 M138 116 Q270 116 408 116 M138 162 Q270 207 408 72" stroke="#2563eb" strokeWidth="3" fill="none"/>}{show2&&<><circle cx="426" cy="72" r="9" fill="#059669"/><circle cx="426" cy="116" r="9" fill="#059669"/></>}{show3&&<text x="271" y="224" textAnchor="middle" fontSize="18">one output per input</text>}</>
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
