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
    <div dir="rtl" style={{fontSize:portrait ? 24 : 29, fontWeight:700}}>المتباينات التربيعية وجدول إشارات كثيرات الحدود</div>
    {phase === "feedback" ? <div style={panel}>
      {answered.map((p, i) => <p key={i} dir="auto" style={{fontSize:portrait ? 23 : 29,
        lineHeight:1.5, margin:"12px 0", overflowWrap:"anywhere"}}>{p.text}</p>)}
    </div> : question ? <div style={panel}>
      {prompted.map((p, i) => <p key={i} dir="auto" style={{fontSize:portrait ? 23 : 29,
        lineHeight:1.5, margin:"12px 0", overflowWrap:"anywhere"}}>{p.text}</p>)}
    </div> : <div style={{...panel, display:"flex",
      flexDirection:portrait ? "column" : "row", alignItems:"center", gap:23}}>
      <div style={{flex:1, minWidth:0, width:"100%"}}><svg viewBox="0 0 550 210" style={{width:"100%"}}><line x1="25" y1="105" x2="525" y2="105" stroke="#334155" strokeWidth="3"/><line x1="208" y1="65" x2="208" y2="145" stroke="#d97706" strokeDasharray="8 7" strokeWidth="3"/><line x1="374" y1="65" x2="374" y2="145" stroke="#d97706" strokeDasharray="8 7" strokeWidth="3"/>{[120,291,457].map(x=><g key={x}><rect x={x-46} y="157" width="92" height="45" rx="9" fill="#e2e8f0"/><text x={x} y="185" textAnchor="middle" fontSize="26">?</text></g>)}<text x="208" y="50" textAnchor="middle" fontSize="23">r₁</text><text x="374" y="50" textAnchor="middle" fontSize="23">r₂</text></svg></div>
      <div dir="rtl" style={{flex:1, minWidth:0, fontSize:portrait ? 25 : 30, lineHeight:1.6,
        fontWeight:600, textAlign:"right"}}>{ready ? params?.concept : " "}</div>
    </div>}
    <div dir="rtl" style={{fontSize:portrait ? 17 : 20, color:"#475569"}}>
      {phase==="feedback" ? "تفسير الإجابة بعد المحاولة" :
       question ? "السؤال — حاول بنفسك الأول" : "رسم متدرج متزامن مع الشرح"}
    </div>
  </AbsoluteFill>;
}
