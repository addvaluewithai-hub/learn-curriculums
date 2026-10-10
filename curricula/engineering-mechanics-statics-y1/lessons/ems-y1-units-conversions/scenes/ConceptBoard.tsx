import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

// Author-created diagram board; layout and cues are deterministic from SDK frame.
// Stage 04: implementation prepared, but audio-linked preview remains untested.
type Params = {mode?: string;topic?: string;focus?: string;primaryUnitId?: string};
type WithSpec = VisualProps & {spec?: {params?: Params}};
const labels: Record<string,[string,string]> = {
  motion:["EQUILIBRIUM","ACCELERATION"],forces:["SUPPORT ↑","GRAVITY ↓"],
  model:["REAL BODY","SIMPLIFIED MODEL"],particle:["SENSOR","PARTICLE"],
  rigid:["DIMENSIONS","RIGID BODY"],contact:["CONTACT PATCH","POINT FORCE"],
  balanced:["FORCE LEFT","FORCE RIGHT"],acceleration:["NET FORCE","a = ΣF / m"],
  interaction:["BODY A","BODY B"],gravity:["MASS 1","MASS 2"],
  weight:["MASS: kg","WEIGHT: N"],fps:["SI: kg / N","FPS: slug / lbf"],
  dimensions:["kg × m/s²","N"],length:["ft","m"],forceunit:["lbf","N"],
  question:["QUESTION","WRITE YOUR ANSWER"]
};
function Sketch({mode}:{mode:string}) {
  const color="#91e5ec";
  const isForces=["forces","balanced","weight","motion","acceleration","interaction"].includes(mode);
  const isDistance=mode==="gravity";
  const isIdeal=["particle","rigid","contact","model"].includes(mode);
  const arrow=(x1:number,y1:number,x2:number,y2:number)=>
    <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth="5"
      strokeLinecap="round" markerEnd="url(#statics-arrow)"/>;
  return <svg viewBox="0 0 660 260" role="img" aria-label="Simplified engineering concept diagram"
    style={{width:"100%",maxHeight:"100%"}}>
    <defs><marker id="statics-arrow" markerWidth="9" markerHeight="9" refX="7" refY="3"
      orient="auto"><path d="M0 0 L7 3 L0 6" fill="none" stroke={color} strokeWidth="1.5"/></marker></defs>
    {isForces&&<>
      <rect x="256" y="96" width="147" height="79" rx="15" fill="#27536b" stroke={color} strokeWidth="3"/>
      {["forces","balanced","weight"].includes(mode)&&<>{arrow(330,93,330,22)}{arrow(330,178,330,248)}</>}
      {["motion","acceleration"].includes(mode)&&arrow(409,135,554,135)}
      {mode==="interaction"&&<><rect x="64" y="103" width="111" height="66" rx="14"
        fill="#27536b" stroke={color} strokeWidth="3"/>{arrow(181,132,253,132)}{arrow(246,160,182,160)}</>}
    </>}
    {isDistance&&<>
      <circle cx="123" cy="130" r="49" fill="#176a84" stroke={color} strokeWidth="3"/>
      <circle cx="540" cy="130" r="35" fill="#176a84" stroke={color} strokeWidth="3"/>
      {arrow(184,131,285,131)}{arrow(481,131,380,131)}
      <path d="M175 194 H506" stroke={color} strokeWidth="2" strokeDasharray="7 8"/>
      <text x="336" y="223" fill="#d6ebfc" textAnchor="middle" fontSize="28">r</text>
    </>}
    {isIdeal&&<>
      <rect x="80" y="91" width="178" height="100" rx="18" fill="#27536b" stroke={color} strokeWidth="3"/>
      {arrow(282,139,398,139)}
      {mode==="particle"?<circle cx="488" cy="140" r="18" fill={color}/>:
       <rect x="420" y="108" width="131" height="65" rx="10" fill="#39708e" stroke={color} strokeWidth="3"/>}
      {mode==="contact"&&arrow(487,29,487,99)}
    </>}
    {!isForces&&!isDistance&&!isIdeal&&<>
      <rect x="68" y="90" width="188" height="90" rx="20" fill="#27536b" stroke={color} strokeWidth="3"/>
      {arrow(282,136,397,136)}
      <rect x="423" y="90" width="169" height="90" rx="20" fill="#27536b" stroke={color} strokeWidth="3"/>
    </>}
  </svg>;
}
export default function ConceptBoard(props: VisualProps) {
  const {frame,fps,recording,layout,phase,question,answer}=props;
  const p=(props as WithSpec).spec?.params??{};
  const portrait=layout==="portrait";
  const mode=String(p.mode??"model");
  const visible=!!p.primaryUnitId&&cueIsVisible(recording,String(p.primaryUnitId),frame,fps);
  const words=labels[mode]??labels.model;
  const reading=question?visibleQuestionParts(question,recording,frame,fps):[];
  const answerParts=phase==="feedback"?(answer?.parts?.filter(v=>frame*1000/fps>=v.atMs)??[]):[];
  const questionActive=Boolean(question)&&phase!=="feedback";
  const part=(v:{text:string;language?:string},i:number)=><div key={i}
    dir={v.language==="ar"?"rtl":"ltr"} style={{background:"#204b65",borderRadius:16,
      padding:portrait?14:23,fontSize:portrait?19:25,lineHeight:1.5,overflowWrap:"anywhere"}}>{v.text}</div>;
  return <AbsoluteFill style={{background:"#071e30",color:"#f5fbff",fontFamily:"system-ui,sans-serif",
    boxSizing:"border-box",padding:portrait?20:34,display:"flex",flexDirection:"column",gap:portrait?14:22}}>
    <div style={{color:"#b4d2df",fontSize:portrait?16:23,fontWeight:700,overflowWrap:"anywhere"}}>
      {String(p.topic??"Engineering Mechanics")}
    </div>
    {questionActive?<div style={{display:"flex",flex:1,flexDirection:"column",justifyContent:"center",gap:14}}>
      <div style={{fontSize:portrait?15:19,color:"#91e5ec"}}>Read → think → write your answer</div>
      {reading.map(part)}
      <div style={{fontSize:portrait?13:17,color:"#b4d2df"}}>Feedback is hidden until submission</div>
    </div>:phase==="feedback"?<div style={{display:"flex",flex:1,flexDirection:"column",justifyContent:"center",gap:14}}>
      <div style={{fontSize:portrait?17:22,color:"#91e5ec"}}>Feedback after submission</div>
      {answerParts.map(part)}
    </div>:<>
      <div style={{display:"flex",flex:1,flexDirection:"column",minHeight:0,justifyContent:"center"}}>
        <Sketch mode={mode}/>
        <div style={{display:"flex",flexDirection:portrait?"column":"row",gap:portrait?8:20,
          justifyContent:"center",marginTop:portrait?8:13}}>
          {words.map((v,i)=><div key={i} style={{flex:1,minWidth:0,textAlign:"center",borderRadius:12,
            background:"#204b65",padding:portrait?11:19,fontSize:portrait?17:23,
            fontWeight:700,overflowWrap:"anywhere"}}>{v}</div>)}
        </div>
      </div>
      <div style={{padding:portrait?15:22,background:"#11364d",borderRadius:14,
        minHeight:portrait?80:86,display:"flex",alignItems:"center",justifyContent:"center",
        fontSize:portrait?19:25,textAlign:"center",fontWeight:650,overflowWrap:"anywhere",
        opacity:visible?1:0.2}}>
        {visible?String(p.focus??"Key idea"):"· · ·"}
      </div>
    </>}
  </AbsoluteFill>;
}
