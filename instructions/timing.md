# AI-authored board timing

Timing is one authoring task inside the authorized Stage 06. The AI reads the
canonical scene script, visual intentions and delivered word-timestamps file,
then writes `media/<clipId>/timing.json` directly. Do not delegate the visual
decisions to phrase matching, word counts, an automatic cue generator or the human.
Do not introduce a separate human approval gate for every cue.

## Author the cues

1. Open the selected receipt and its actual transcript; follow `alignment.json`
   when a separately corrected transcript has already been selected.
2. Read the complete scene and its question/feedback boundaries. Decide which
   existing visual unit should appear/change at each meaningful spoken idea.
3. Inspect surrounding timestamped words and choose the intended occurrence.
   English/transliterated terms and Arabic spelling may differ from the script;
   use context, not exact text equality. Write the selected inclusive word indices
   and copy `atMs` from the first selected word's `start_ms`.
4. Record a short `reason` linking the spoken idea to the visual change. Keep the
   existing script, units, recording and original ASR intact.
5. Prepare the pinned SDK preview and inspect gradual disclosure, English/Arabic
   question onset, post-attempt feedback, backward seek and both layouts. Adjust
   the selected anchors/components within the same task; do not stop merely
   because a text-search helper found no exact phrase.

For example, source `Statics` and observed `ستاتيكس` can refer to the same utterance.
Select that actual timed word with its surrounding context; explain the relation.
For repeated terms use the scene's intended occurrence, not automatically the first.
Question/feedback clauses use their true spoken onsets, not a later recognizable term.

If the word file genuinely provides no evidence for a required onset, inspect
the same audio or supported alignment output. Resolve only the ambiguous cue;
never interpolate/guess missing times, invent a corrected transcript, or claim
listening happened when it did not. Record a precise unresolved blocker if actual
audio/alignment access cannot resolve it. Human help is optional for that ambiguity,
not a requirement for every correctly supported cue.

## File contract

Use `method: "semantic-word-anchors"` and an honest `author`, such as `ai:codex`.
Copy the current `audioHash`, `scriptHash` and selected `transcriptHash` from the
verified files. `reviewer`/human approval is not required for this authoring method.

```json
{
  "audioHash": "COPY_SELECTED_RECEIPT_HASH",
  "scriptHash": "COPY_CURRENT_SCRIPT_HASH",
  "transcriptHash": "COPY_SELECTED_TRANSCRIPT_HASH",
  "method": "semantic-word-anchors",
  "author": "ai:codex",
  "cues": [
    {
      "unitId": "U01",
      "wordStart": 12,
      "wordEnd": 13,
      "atMs": 3240,
      "reason": "The observed term introduces the idea represented by this label."
    }
  ]
}
```

This is an illustrative shape, not reusable times/hashes for a real recording.
Legacy `word-anchors-reviewed`/`multi-pass-reviewed` files remain supported.

## Technical checks and review

`validate --stage timed` checks selected recording/script/transcript identity,
unique complete unit IDs, valid word indices, finite in-recording times, actual
word-start binding and provenance fields. It neither matches script phrases to ASR
nor chooses cues, scores meaning or decides whether the diagram teaches well.
These checks run as ordinary preparation/build checks, not an extra authoring gate.

Writing cues does not mark `review.json` passed. Keep independent scientific,
listening and actual preview review evidence separate. Optional ASR candidate
tools are search aids only; their suggestions need an author decision, not mandatory
human approval. Source exports remain handoffs, not student releases.
