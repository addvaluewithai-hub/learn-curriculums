import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

type BoardParams = {title?:string;mode?:string;anchors?:string[]};
const textStyle: React.CSSProperties = {lineHeight:1.45,overflowWrap:"anywhere"};
function Container({kind}:{kind:"solid"|"liquid"|"gas"}) {
  const color = kind==="solid"?"#98bdfa":kind==="liquid"?"#69d8d3":"#f3ce7c";
  return <div style={{border:"3px solid #8fbceb",borderTop:0,borderRadius:"0 0 14px 14px",
    width:96,height:108,padding:10,display:"flex",flexWrap:"wrap",gap:5,
    alignContent:kind==="gas"?"space-around":"end",justifyContent:"space-around"}}>
    {Array.from({length:9},(_,i)=><span key={i} style={{width:kind==="gas"?11:14,height:kind==="gas"?11:14,
      borderRadius:kind==="solid"?3:99,background:color}}/>)}
  </div>;
}
const names=["Solid","Liquid","Gas"] as const;
export default function MatterBoard(props:VisualProps) {
  const {spec,recording,frame,fps,layout,phase,question,answer}=props;
  const params=spec.params as BoardParams;
  const portrait=layout==="portrait";
  const anchors=params.anchors??[];
  const shown=(n:number)=>!!anchors[n]&&cueIsVisible(recording,anchors[n],frame,fps);
  const parts=question?visibleQuestionParts(question,recording,frame,fps):[];
  const answers=answer?.parts?.filter(p=>frame*1000/fps>=p.atMs)??[];
  const box:React.CSSProperties={padding:portrait?16:22,background:"#1f354d",borderRadius:14};
  const font=portrait?20:24;
  const mode=params.mode??"states";
  return <AbsoluteFill style={{background:"#0f2135",color:"#f3f8ff",fontFamily:"Tahoma, Arial, sans-serif",
    padding:portrait?24:40,overflow:"hidden"}}>
    <div style={{fontSize:16,color:"#a7cce9"}}>First-Year Engineering · Chemistry</div>
    {phase==="question-reading"||phase==="feedback"?
      <div style={{marginTop:32,display:"grid",gap:16}}>
        {(phase==="feedback"?answers:parts).map((p,i)=><div key={i} dir={p.language==="ar"?"rtl":"ltr"}
          style={{...box,...textStyle,fontSize:font}}>{p.text}</div>)}
      </div>:
      <div style={{display:"grid",gap:portrait?18:26,marginTop:24}}>
        <div style={{fontSize:font+2,fontWeight:700}}>{params.title??"States of Matter"}</div>
        {mode==="states"&&shown(0)?<div style={{display:"flex",justifyContent:"space-around",gap:10}}>
          {names.map(n=><div key={n} style={{display:"grid",justifyItems:"center",gap:12}}>
            <Container kind={n.toLowerCase() as "solid"|"liquid"|"gas"}/><b>{n}</b></div>)}</div>:null}
        {mode==="states"&&shown(1)?<div style={{...box,fontSize:portrait?18:23}}>
          Shape and Volume are different · Compressibility is greatest for a gas (in this comparison)
        </div>:null}
        {mode==="phase-arrows"&&shown(0)?<div style={{...box,display:"grid",gap:portrait?12:18,fontSize:font}}>
          {shown(0)?<div>Solid ⇄ Liquid <span style={{color:"#7be2ce"}}>Melting / Freezing</span></div>:null}
          {shown(1)?<div>Liquid ⇄ Gas <span style={{color:"#7be2ce"}}>Vaporization / Condensation</span></div>:null}
          {shown(2)?<div>Solid ⇄ Gas <span style={{color:"#7be2ce"}}>Sublimation / Deposition</span></div>:null}
        </div>:null}
        {mode==="recap"&&shown(0)?<div style={{...box,fontSize:font,display:"grid",gap:15}}>
          <div>Shape · Volume · Compressibility</div><div>Direction decides phase-change name</div>
          <div style={{color:"#f5d891"}}>Next → Boyle: P versus V at constant T</div>
        </div>:null}
      </div>}
  </AbsoluteFill>;
}
