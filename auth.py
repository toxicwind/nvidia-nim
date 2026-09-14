"""Auth shim: vault surrogate on the author's box, else NVIDIA_API_KEY env.

Get a free key at https://build.nvidia.com and export NVIDIA_API_KEY.
"""
import os
import sys


class DynamicCredentialError(Exception):
    pass


def _load_vault():
    try:
        sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
        from dynamic_credentials import (
            add_surrogate_to_request as _add,
            read_response_body as _read,
        )
        return _add, _read
    except Exception:
        return None, None


_ADD, _READ = _load_vault()


def add_surrogate_to_request(req, cred, allowed_hosts=()):
    if _ADD is not None:
        return _ADD(req, cred, allowed_hosts=allowed_hosts)
    key = os.environ.get("NVIDIA_API_KEY")
    if not key:
        raise DynamicCredentialError(
            "no vault credential and NVIDIA_API_KEY is not set "
            "(get a free key at https://build.nvidia.com)"
        )
    req.add_header("Authorization", "Bearer " + key)


def read_response_body(response, chunk_size=65536):
    if _READ is not None:
        return _READ(response, chunk_size=chunk_size)
    chunks = []
    while True:
        c = response.read(chunk_size)
        if not c:
            break
        chunks.append(c)
    return b"".join(chunks)
