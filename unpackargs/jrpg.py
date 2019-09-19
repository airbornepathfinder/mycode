#!/usr/bin/env python3

import os
import fnmatch

def find(pattern, path, dontlook):
    """search through filesystem based on given path location"""

    result = []
    for root, dirs, files in os.walk(path, topdown=True):
            if root in dontlook:
                dirs[:] = []
                files[:] = []
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
    return result

