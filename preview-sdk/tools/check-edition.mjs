import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { runtimeVersion } from '@learn/lesson-runtime/core';

const read = async path => JSON.parse(await readFile(new URL(path, import.meta.url), 'utf8'));
const [sdk, config, lock] = await Promise.all([read('../sdk-version.json'), read('../package.json'), read('../package-lock.json')]);
const installed = lock.packages['node_modules/@learn/lesson-runtime'];
assert.equal(runtimeVersion, sdk.version, 'Installed runtime differs from SDK metadata');
assert.equal(config.dependencies['@learn/lesson-runtime'], sdk.url, 'SDK dependency URL differs from metadata');
assert.equal(installed.resolved, sdk.url, 'SDK lock must pin the same immutable tarball');
assert.equal(installed.integrity, sdk.integrity, 'SDK integrity differs from metadata');
assert.match(sdk.sha256, /^[a-f0-9]{64}$/);
assert.match(sdk.url, /^https:\/\/raw\.githubusercontent\.com\/addvaluewithai-hub\/new-learn\/[a-f0-9]{40}\/distributions\/learn-lesson-runtime-[0-9.]+\.tgz$/);
console.log(`Pinned SDK ${runtimeVersion}: installed version, immutable URL and lock integrity match.`);
