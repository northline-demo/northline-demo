import os
import pathlib

_HERE = pathlib.Path(__file__).resolve().parent.parent


def deployed_version() -> dict:
    """Read the release stamp written by the deploy job.

    This is the answer to 'show me the commit running in production
    right now' -- it comes from the artefact CI built, not from a
    human's memory.
    """
    stamp = _HERE / "RELEASE"
    if not stamp.exists():
        return {"commit": "unknown", "release": "unknown", "deployed_at": "unknown"}
    data = {}
    for line in stamp.read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            data[k.strip().lower()] = v.strip()
    return {
        "commit": data.get("commit", "unknown"),
        "release": data.get("release", "unknown"),
        "deployed_at": data.get("deployed_at", "unknown"),
        "deployed_by": data.get("deployed_by", "unknown"),
        "host": os.uname().nodename,
    }
