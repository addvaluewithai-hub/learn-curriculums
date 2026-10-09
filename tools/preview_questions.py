"""Use explicit reviewed full-clause units for bilingual question disclosure."""
from common import require
from media import tokens


def reading_parts(question, clip, timing):
    parts = []
    for field, language in (("english", "en"), ("arabic", "ar")):
        value = question.get(field)
        require(isinstance(value, str) and value.strip(), f"Preview requires {field} question text")
        explicit = question.get("readingUnitIds", {}).get(field)
        matches = [u for u in clip["units"] if tokens(u["text"]) == tokens(value)
                   and (not explicit or u["id"] == explicit)]
        require(len(matches) == 1,
                f"Question {question['id']}: add one full {field} question unit or set readingUnitIds; never guess onset")
        cue = next(c for c in timing["cues"] if c["unitId"] == matches[0]["id"])
        parts.append({"text": value, "language": language, "atMs": cue["atMs"]})
    return sorted(parts, key=lambda part: part["atMs"])


def adapt_question(question, clip, timing, visual, feedback_visual):
    options = question.get("options", [])
    english_options = question.get("englishOptions", options)
    require(isinstance(english_options, list) and len(english_options) == len(options), "Option translations must match")
    result = {
        "id": question["id"], "english": question["english"], "title": question["arabic"],
        "options": options, "englishOptions": english_options, "correct": question.get("correctIndex", 0),
        "explanation": question["answer"]["arabic"], "answerReasoning": question["answer"]["reasoning"],
        "englishAnswer": question["answer"]["english"], "feedbackId": question["feedback"]["id"],
        "hint": "", "attempt": question["attempt"], "readingParts": reading_parts(question, clip, timing),
        "writtenLabel": question.get("writtenLabel", "اكتب إجابتك بالإنجليزي"),
        "writtenPlaceholder": question.get("writtenPlaceholder", "Your answer…"),
        "readingVisual": visual,
    }
    if feedback_visual:
        result["feedbackVisual"] = feedback_visual
    return result
