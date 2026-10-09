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
    <div dir="rtl" style={{fontSize:portrait ? 24 : 29, fontWeight:700}}>المتباينات الكسرية وتقاطع الشروط</div>
    {phase === "feedback" ? <div style={panel}>
      {answered.map((p, i) => <p key={i} dir="auto" style={{fontSize:portrait ? 23 : 29,
        lineHeight:1.5, margin:"12px 0", overflowWrap:"anywhere"}}>{p.text}</p>)}
    </div> : question ? <div style={panel}>
      {prompted.map((p, i) => <p key={i} dir="auto" style={{fontSize:portrait ? 23 : 29,
        lineHeight:1.5, margin:"12px 0", overflowWrap:"anywhere"}}>{p.text}</p>)}
    </div> : <div style={{...panel, display:"flex",
      flexDirection:portrait ? "column" : "row", alignItems:"center", gap:23}}>
      <div style={{flex:1, minWidth:0, width:"100%"}}><svg viewBox="0 0 550 210" style={{width:"100%"}}><line x1="25" y1="100" x2="525" y2="100" stroke="#334155" strokeWidth="3"/><circle cx="205" cy="100" r="12" fill="#047857"/><circle cx="385" cy="100" r="13" fill="white" stroke="#dc2626" strokeWidth="4"/><text x="205" y="151" fontSize="21" textAnchor="middle">numerator = 0</text><text x="385" y="151" fontSize="21" textAnchor="middle">denominator = 0</text><text x="385" y="65" fontSize="21" textAnchor="middle" fill="#dc2626">excluded</text></svg></div>
      <div dir="rtl" style={{flex:1, minWidth:0, fontSize:portrait ? 25 : 30, lineHeight:1.6,
        fontWeight:600, textAlign:"right"}}>{ready ? params?.concept : " "}</div>
    </div>}
    <div dir="rtl" style={{fontSize:portrait ? 17 : 20, color:"#475569"}}>
      {phase==="feedback" ? "تفسير الإجابة بعد المحاولة" :
       question ? "السؤال — حاول بنفسك الأول" : "رسم متدرج متزامن مع الشرح"}
    </div>
  </AbsoluteFill>;
}
