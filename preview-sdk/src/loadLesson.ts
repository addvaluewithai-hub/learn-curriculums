import type {
  LessonPackage,
  RendererRegistry,
  VisualProps,
} from "@learn/lesson-runtime";
import { validateLessonPackage } from "@learn/lesson-runtime/core";
import type { ComponentType } from "react";
import { moduleLoaders } from "../.generated/modules";

export type Entry = {
  key: string;
  curriculumId: string;
  lessonId: string;
  title?: string;
  order?: number;
  ready: boolean;
  blocker?: string;
  packageUrl?: string;
  renderers?: string[];
};
type Module = { default: ComponentType<VisualProps> };
const loaders = moduleLoaders as Record<string, () => Promise<Module>>;

export async function loadLesson(entry: Entry, signal: AbortSignal) {
  if (!entry.ready || !entry.packageUrl)
    throw new Error(entry.blocker || "الدرس مش جاهز للمعاينة.");
  const [response, modules] = await Promise.all([
    fetch(entry.packageUrl, { signal }),
    Promise.all(
      (entry.renderers ?? []).map(async (renderer) => {
        const loader = loaders[`${entry.key}:${renderer}`];
        if (!loader) throw new Error(`Missing local renderer: ${renderer}`);
        const module = await loader();
        if (typeof module.default !== "function")
          throw new Error(`${renderer}: default-export a React component.`);
        return [renderer, module.default] as const;
      }),
    ),
  ]);
  if (!response.ok) throw new Error("تعذّر تحميل بيانات الدرس.");
  const payload = await response.json();
  const registry: RendererRegistry = Object.fromEntries(modules);
  const lesson: LessonPackage = validateLessonPackage(
    payload.lesson,
    new Set(Object.keys(registry)),
  );
  return { lesson, registry, provenance: payload.provenance };
}
