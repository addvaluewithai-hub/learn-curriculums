"""Generate a temporary, clearly synthetic browser acceptance fixture."""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))
from preview_support import PreviewCase
from preview import prepare_preview

case = PreviewCase()
case.setUp()
try:
    case.deliver_all()
    source = ROOT / "preview-sdk/test-results/probe-root"
    if source.exists():
        shutil.rmtree(source)
    shutil.copytree(case.root, source)
    print(prepare_preview(source))
finally:
    case.doCleanups()
