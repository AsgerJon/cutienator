"""
The 'dev_tooling' package creates parts of cutienator from Qt's own files.
It is not part of cutienator, and cutienator does not need it to run.

It has two sides. A generator writes, and a tester verifies what the
generator wrote.

What it does so far: it reads every header file of a part of Qt and
keeps all the contents of each; it makes the dependency tree of the
classes found there; it writes the ritual file of a class; and it
verifies that ritual file.

  python -m dev_tooling WORK_FOLDER QtCore QtGui QtWidgets
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._header_file import HeaderFile
from ._qt_part import QtPart
from ._dependency_tree import DependencyTree
from ._ritual_generator import RitualGenerator
from ._ritual_tester import RitualTester

__all__ = (
    'HeaderFile',
    'QtPart',
    'DependencyTree',
    'RitualGenerator',
    'RitualTester',
)
