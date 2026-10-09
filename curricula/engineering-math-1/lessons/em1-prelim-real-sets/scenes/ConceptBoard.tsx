import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

// Source-controlled Stage 04 board draft; audio/cue and SDK playback untested.
export default function ConceptBoard(props: VisualProps) {
  const {frame, fps, recording, layout, question, answer, phase} = props;
  const portrait = layout === "portrait";
  const params = (props as unknown as {spec?: {params?: {concept?: string}}}).spec?.params;
  const ready = !question && phase !== "feedback" && cueIsVisible(recording, "U01", frame, fps);
  const reading = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const prompted = question && phase !== "question-reading"
    ? [{text: question.english}, {text: question.title}] : reading;
  const answered = answer?.parts?.filter(part => frame * 1000 / fps >= part.atMs) ?? [];
  const panel = {background: "#fff", borderRadius: 20, padding: portrait ? 21 : 29,
    boxShadow: "0 3px 16px #00000012", boxSizing: "border-box" as const, width:"100%"};
  return <AbsoluteFill style={{background:"#f1f5f9", padding:portrait ? 22 : 32,
    display:"flex", flexDirection:"column", justifyContent:"center", gap:portrait ? 16 : 20,
    color:"#0f172a", fontFamily:"sans-serif", overflow:"hidden"}}>
    <div dir="rtl" style={{fontSize:portrait ? 24 : 29, fontWeight:700}}>الأعداد الحقيقية وخط الأعداد والمجموعات</div>
    {phase === "feedback" ? <div style={panel}>
      {answered.map((p, i) => <p key={i} dir="auto" style={{fontSize:portrait ? 23 : 29,
        lineHeight:1.5, margin:"12px 0", overflowWrap:"anywhere"}}>{p.text}</p>)}
    </div> : question ? <div style={panel}>
      {prompted.map((p, i) => <p key={i} dir="auto" style={{fontSize:portrait ? 23 : 29,
        lineHeight:1.5, margin:"12px 0", overflowWrap:"anywhere"}}>{p.text}</p>)}
    </div> : <div style={{...panel, display:"flex",
      flexDirection:portrait ? "column" : "row", alignItems:"center", gap:23}}>
      <div style={{flex:1, minWidth:0, width:"100%"}}><svg viewBox="0 0 550 210" style={{width:"100%"}}><line x1="20" y1="65" x2="520" y2="65" stroke="#334155" strokeWidth="4"/>{[-2,-1,0,1,2].map((n,i)=><g key={n}><line x1={120+i*80} x2={120+i*80} y1="53" y2="77" stroke="#334155" strokeWidth="3"/><text x={120+i*80} y="104" fontSize="20" textAnchor="middle">{n}</text></g>)}<circle cx="230" cy="158" r="48" fill="#dbeafe" stroke="#2563eb" strokeWidth="3"/><circle cx="295" cy="158" r="48" fill="#d1fae5" stroke="#047857" strokeWidth="3"/><text x="210" y="163" fontSize="21">A</text><text x="313" y="163" fontSize="21">B</text></svg></div>
      <div dir="rtl" style={{flex:1, minWidth:0, fontSize:portrait ? 25 : 30, lineHeight:1.6,
        fontWeight:600, textAlign:"right"}}>{ready ? params?.concept : " "}</div>
    </div>}
    <div dir="rtl" style={{fontSize:portrait ? 17 : 20, color:"#475569"}}>
      {phase==="feedback" ? "تفسير الإجابة بعد المحاولة" :
       question ? "السؤال — حاول بنفسك الأول" : "رسم متدرج متزامن مع الشرح"}
    </div>
  </AbsoluteFill>;
}
