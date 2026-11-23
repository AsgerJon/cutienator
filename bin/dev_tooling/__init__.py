"""
The 'dev_tooling' package creates parts of cutienator from Qt's own files.
It is not part of cutienator, and cutienator does not need it to run.

It has two sides. A generator writes, and a tester verifies what the
generator wrote.

What it does so far: it reads every header file of a part of Qt and
keeps all the contents of each; it makes the dependency tree of the
classes found there; it writes the ritual file of a class and verifies
that ritual file; it writes the Python file of an enum, and of a
namespace that holds enums, and verifies the numbers in those files by
asking the compiler; and it writes the Python file of a cute class from
the plan of its ritual file, and verifies that file.

  python -m dev_tooling WORK_FOLDER QtCore QtGui QtWidgets
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._header_file import HeaderFile
from ._header_reader import HeaderReader
from ._source_reader import SourceReader
from ._dependency_tree import DependencyTree
from ._ritual_generator import RitualGenerator
from ._ritual_tester import RitualTester
from ._enum_generator import EnumGenerator
from ._namespace_generator import NamespaceGenerator
from ._enum_tester import EnumTester
from ._class_generator import ClassGenerator
from ._class_tester import ClassTester

__all__ = (
    'HeaderFile',
    'HeaderReader', 'SourceReader',
    'DependencyTree',
    'RitualGenerator',
    'RitualTester',
    'EnumGenerator',
    'NamespaceGenerator',
    'EnumTester',
    'ClassGenerator',
    'ClassTester',
)
