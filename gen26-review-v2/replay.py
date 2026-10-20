"""Rejouer l'entrée avec la connexion Codex existante ; aucune identité de sortie garantie."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    content = (ROOT / "model/input.txt").read_bytes()
    expected = (ROOT / "model/input.sha256").read_text().strip()
    if hashlib.sha256(content).hexdigest() != expected:
        raise ValueError("Entrée modifiée : arrêt avant appel modèle")
    if args.check_only:
        print("PASS: empreinte de l'entrée ; aucun appel modèle")
        return
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    version = subprocess.check_output(["codex", "--version"], text=True).strip()
    with tempfile.TemporaryDirectory(prefix="gen26-inference-") as cwd:
        cmd = [
            "codex", "exec", "--ignore-user-config", "--skip-git-repo-check",
            "--ephemeral", "--sandbox", "read-only", "--json",
            "-c", "project_doc_max_bytes=0", "-c", "features.shell_tool=false",
            "-c", "features.memories=false", "-c", "features.multi_agent=false",
            "-c", 'web_search="disabled"', "-C", cwd,
            "-o", str(out / "output.txt"), "-"
        ]
        receipt = {
            "command": cmd, "cli_version": version,
            "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "input_sha256": expected, "requested_model": "CLI default, no override",
            "snapshot": None, "cost": None,
            "isolation": "new empty cwd; server context not exposed"
        }
        start = time.monotonic()
        try:
            result = subprocess.run(cmd, input=content, capture_output=True, timeout=150)
            stdout, stderr = result.stdout, result.stderr
            receipt["returncode"] = result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout, stderr = exc.stdout or b"", exc.stderr or b""
            receipt["error"] = "timeout 150 seconds"
        receipt["wall_seconds"] = time.monotonic() - start
        (out / "events.jsonl").write_bytes(stdout)
        (out / "stderr.txt").write_bytes(stderr)
        (out / "execution.json").write_text(json.dumps(receipt, indent=2) + "\n")
    if receipt.get("returncode") != 0:
        raise SystemExit("Échec conservé ; aucune génération réussie revendiquée")

if __name__ == "__main__":
    main()
