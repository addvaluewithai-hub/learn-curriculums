import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { mkdir } from "node:fs/promises";
import { chromium } from "playwright";

const url = "http://127.0.0.1:5176";
const server = spawn(
  process.execPath,
  [
    "node_modules/vite/bin/vite.js",
    "preview",
    "--host",
    "127.0.0.1",
    "--port",
    "5176",
    "--strictPort",
  ],
  { stdio: ["ignore", "pipe", "pipe"] },
);
let logs = "";
server.stdout.on("data", (chunk) => {
  logs += chunk;
});
server.stderr.on("data", (chunk) => {
  logs += chunk;
});
let browser;
async function poll(check, label) {
  const end = Date.now() + 15000;
  while (Date.now() < end) {
    if (await check()) return;
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
  throw new Error(`Timed out: ${label}`);
}
async function bounds(page) {
  const escaped = await page.evaluate(() => {
    const stage = document
      .querySelector(".lesson-stage")
      .getBoundingClientRect();
    return [...document.querySelectorAll("[data-safe-element]")]
      .filter((node) => {
        const b = node.getBoundingClientRect();
        return (
          b.left < stage.left - 2 ||
          b.right > stage.right + 2 ||
          b.top < stage.top - 2 ||
          b.bottom > stage.bottom + 2
        );
      })
      .map((node) => node.textContent);
  });
  assert.deepEqual(escaped, []);
  assert.equal(
    await page.evaluate(
      () => document.documentElement.scrollWidth > innerWidth,
    ),
    false,
  );
}

try {
  await poll(async () => {
    if (server.exitCode != null) throw new Error(logs);
    try {
      return (await fetch(url)).ok;
    } catch {
      return false;
    }
  }, "built preview server");
  browser = await chromium.launch({ headless: true });
  await mkdir("test-results", { recursive: true });
  const page = await browser.newPage({
    viewport: { width: 1280, height: 1000 },
  });
  const errors = [];
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(url);
  await page.locator('.lesson-preview[data-scene="S01"]').waitFor();
  assert.equal(
    await page.getByText("Three counters", { exact: true }).count(),
    0,
  );
  await page.getByRole("button", { name: "ابدأ الشرح", exact: true }).click();
  await page.getByText("Three counters", { exact: true }).waitFor();
  await page.getByRole("button", { name: "إيقاف مؤقت", exact: true }).click();
  const seek = page.getByLabel("موضع التشغيل");
  const paused = await seek.inputValue();
  await new Promise((resolve) => setTimeout(resolve, 300));
  assert.equal(await seek.inputValue(), paused);
  await bounds(page);
  await page.screenshot({
    path: "test-results/preview-desktop.png",
    fullPage: true,
  });
  await page.getByRole("button", { name: "كمّل الشرح", exact: true }).click();
  await page.locator('[data-board-phase="question-reading"]').waitFor();
  await page.getByText("How many counters?", { exact: true }).waitFor();
  assert.equal(
    await page.locator(".lesson-preview").getAttribute("data-mode"),
    "narration",
  );
  assert.equal(
    await page.getByText("Five counters.", { exact: true }).count(),
    0,
  );
  await page.locator('.lesson-preview[data-mode="attempt"]').waitFor();
  await page.getByRole("textbox").fill("Five counters");
  await page.getByRole("button", { name: "اسمع التعقيب ونكمل" }).click();
  await page.locator('.lesson-preview[data-mode="feedback"]').waitFor();
  await page.getByText("Five counters.", { exact: true }).waitFor();
  await page.getByText("خمس قطع.", { exact: true }).waitFor();
  await page.locator('.lesson-preview[data-mode="complete"]').waitFor();
  assert.deepEqual(errors, []);
  await page.close();
  const mobile = await browser.newPage({
    viewport: { width: 320, height: 844 },
  });
  await mobile.goto(url);
  await mobile.locator('.lesson-preview[data-layout="portrait"]').waitFor();
  const ratio = await mobile
    .locator(".lesson-stage")
    .evaluate((node) => node.clientWidth / node.clientHeight);
  assert.ok(Math.abs(ratio - 9 / 16) < 0.01);
  await mobile.getByLabel("موضع التشغيل").focus();
  await mobile.getByLabel("موضع التشغيل").press("End");
  await mobile.getByText("Three counters", { exact: true }).waitFor();
  await bounds(mobile);
  await mobile.getByRole("button", { name: "2. Try", exact: true }).click();
  await mobile.getByRole("button", { name: "ابدأ الشرح", exact: true }).click();
  await mobile.getByText("كام قطعة؟", { exact: true }).waitFor();
  await bounds(mobile);
  await mobile.screenshot({
    path: "test-results/preview-mobile.png",
    fullPage: true,
  });
  console.log(
    "Factory preview: installed SDK, source adapter, custom teaching/question/feedback, progressive cues, automatic completion and 9:16 safe bounds passed. Synthetic WAV/anchors only.",
  );
} finally {
  await browser?.close();
  server.kill();
}
