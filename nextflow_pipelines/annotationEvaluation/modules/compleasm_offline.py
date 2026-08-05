#!/usr/bin/env python3
"""Run compleasm with its offline fallback repaired.

compleasm 0.2.9 declares its own `class URLError(OSError)`, which shadows
`urllib.error.URLError` in the module namespace. Its `except URLError` guards
therefore never catch a real connection failure, so the documented
"cannot reach <url>, using cached file_versions.tsv" path is unreachable and
compleasm aborts on hosts without internet access. Rebinding the module-level
name restores that fallback, which is what lets `-L <library>` work on compute
nodes. All arguments are passed through to compleasm unchanged.
"""
import sys
import urllib.error

import compleasm

compleasm.URLError = urllib.error.URLError

if __name__ == "__main__":
    sys.exit(compleasm.main())
