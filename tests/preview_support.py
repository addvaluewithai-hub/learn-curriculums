"""Synthetic timed WAV fixture only; not speech or a published curriculum."""
import wave
from support import ProductionCase
from audio import prepare, collect
from common import clips_for, read_json, write_json
from media import tokens

BOARD = '''import {AbsoluteFill} from 'remotion';
import {cueIsVisible, visibleQuestionParts, type VisualProps} from '@learn/lesson-runtime';
export default function Probe({frame, fps, recording, phase, question, answer, layout}: VisualProps) {
  const parts = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  return <AbsoluteFill data-board-phase={phase} style={{background:'#fafbf4', padding:40, justifyContent:'center', gap:24, fontSize:layout === 'portrait' ? 30 : 36}}>
    {phase === 'question-reading' ? parts.map((p, i) => <p key={i} data-safe-element="part" dir={p.language === 'ar' ? 'rtl' : 'ltr'}>{p.text}</p>) :
     phase === 'feedback' ? answer?.parts?.filter(p => frame * 1000 / fps >= p.atMs).map((p,i) => <p key={i} data-safe-element="answer" dir={p.language === 'ar' ? 'rtl' : 'ltr'}>{p.text}</p>) :
     <><p data-safe-element="first">Two counters</p>{cueIsVisible(recording,'U2',frame,fps) ? <p data-safe-element="second">Three counters</p> : null}</>}
  </AbsoluteFill>;
}
'''


class PreviewCase(ProductionCase):
    def setUp(self):
        super().setUp()
        (self.folder / "scenes/Probe.tsx").write_text(BOARD)
        spec = {**self.teaching["visual"], "renderer": "counting-probe", "module": "scenes/Probe.tsx"}
        self.teaching["visual"] = spec
        self.question["visual"] = spec
        self.question["question"]["feedback"]["visual"] = spec
        self.question["question"]["feedback"]["units"].append({"id": "UFA", "text": "خمس قطع.", "visualIntent": "Reveal Arabic answer with its audio"})
        self.teaching["narration"]["units"].append({"id": "U2", "text": "سؤال قصير دلوقتي.", "visualIntent": "Synthetic cue for second group"})
        self.question["narration"]["units"].append({"id": "UA", "text": "كام قطعة؟", "visualIntent": "Show Arabic support"})
        self.save_scenes()

    def deliver_all(self):
        for clip in clips_for([self.teaching, self.question]):
            job = prepare(self.root, "counting", "counting-add", clip["id"], "probe")
            payload = read_json(job)["client_payload"]
            audio = self.root / "fixture.wav"
            with wave.open(str(audio), "wb") as handle:
                handle.setnchannels(1)
                handle.setsampwidth(2)
                handle.setframerate(8000)
                handle.writeframes(b"\0\0" * 24000)
            words = [{"text": value, "start_ms": index * 200, "end_ms": (index + 1) * 200}
                     for index, value in enumerate(clip["script"].split())]
            duration = words[-1]["end_ms"]
            transcript = {"schema_version": 1, "type": "word_timestamps", "alignment_mode": "synthetic-test-only",
                          "source_text": clip["script"], "recognized_text": clip["script"], "duration_ms": duration,
                          "word_count": len(words), "words": words}
            result = {"id": payload["job_id"], "status": "completed", "audio_url": "https://example.test/probe.wav",
                      "transcript_url": "https://example.test/probe.json", "metadata": payload["request"]["metadata"],
                      "transcript": {"status": "completed", "word_count": len(words), "duration_ms": duration}}
            write_json(self.root / "result.json", result)
            write_json(self.root / "transcript.json", transcript)
            collect(self.root, str(job.relative_to(self.root)), self.root / "result.json", audio, self.root / "transcript.json")
            receipt = read_json(self.folder / f"media/{clip['id']}/receipt.json")
            cues = []
            for unit in clip["units"]:
                count = len(unit["text"].split())
                first = next(i for i in range(len(words)) if tokens(" ".join(w["text"] for w in words[i:i+count])) == tokens(unit["text"]))
                cues.append({"unitId": unit["id"], "wordStart": first, "wordEnd": first + count - 1, "atMs": words[first]["start_ms"]})
            write_json(self.folder / f"media/{clip['id']}/timing.json", {
                "audioHash": receipt["audioHash"], "scriptHash": receipt["scriptHash"], "transcriptHash": receipt["transcriptHash"],
                "method": "word-anchors-reviewed", "reviewer": "synthetic fixture generator",
                "evidence": "Fabricated test-only anchors, not real listening review", "cues": cues,
            })
