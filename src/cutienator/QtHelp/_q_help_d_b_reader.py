"""
QHelpDBReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/6.12.0/QtHelp/private/qhelpdbreader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHelpDBReader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant, QVersionNumber


class QHelpDBReader(QObject):
  """
  The cute side of Qt's QHelpDBReader: a plain Python object standing in
  front of one C++ QHelpDBReader.

  It is built on the cute 'QObject', as Qt's QHelpDBReader is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpDBReader that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'namespaceName',
  'virtualFolder', 'version', 'fileData', 'customFilters',
  'filterAttributes', 'metaData', 'versionHeuristic', 'quote'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpDBReader::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QHelpDBReader::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpDBReader::~QHelpDBReader()': the destructor: Python never
    removes a C++ QHelpDBReader.
  - Qt's 'QList<QStringList> QHelpDBReader::filterAttributeSets() const':
    gives a type Python has no way to take yet.
  - Qt's 'QMultiMap<QString, QByteArray> QHelpDBReader::filesData(const
    QStringList &filterAttributes, const QString &extensionFilter) const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  9 of the 24 functions Qt declares: 5 leans on 'QHelpDBReader; 2 not a gap;
  2 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QHelpDBReader is created at the first use, not by
    'QHelpDBReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpDBReader.
  - Qt tells when it has removed the C++ QHelpDBReader. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHelpDBReader that has no cute function yet,
    '__init__', 'filesData', 'filterAttributeSets', 'indexTable', 'init',
    'initDB', 'qtVersionHeuristic', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QHelpDBReader, each a class in here as in
  #  C++.

  class ContentsItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpDBReader::ContentsItem: a plain Python object
    standing in front of one C++ QHelpDBReader::ContentsItem.

    C++ hands a QHelpDBReader::ContentsItem around as a copy, so every C++
    QHelpDBReader::ContentsItem behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QHelpDBReader::ContentsItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpDBReader::ContentsItem::~ContentsItem()': the destructor:
      Python removes its C++ QHelpDBReader::ContentsItem by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QHelpDBReader::ContentsItem is created at the first use, not by
      'QHelpDBReader::ContentsItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpDBReader::ContentsItem back gives a copy the
      ritual made for Python, in a new cute QHelpDBReader::ContentsItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpDBReader::ContentsItem'

    #  Qt's '~QHelpDBReader::ContentsItem()'. Naming it makes this a value
    #  class: Python owns every C++ QHelpDBReader::ContentsItem behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QHelpDBReader12ContentsItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class FileItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpDBReader::FileItem: a plain Python object
    standing in front of one C++ QHelpDBReader::FileItem.

    C++ hands a QHelpDBReader::FileItem around as a copy, so every C++
    QHelpDBReader::FileItem behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QHelpDBReader::FileItem yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpDBReader::FileItem::~FileItem()': the destructor: Python
      removes its C++ QHelpDBReader::FileItem by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QHelpDBReader::FileItem is created at the first use, not by
      'QHelpDBReader::FileItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpDBReader::FileItem back gives a copy the
      ritual made for Python, in a new cute QHelpDBReader::FileItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpDBReader::FileItem'

    #  Qt's '~QHelpDBReader::FileItem()'. Naming it makes this a value class:
    #  Python owns every C++ QHelpDBReader::FileItem behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QHelpDBReader8FileItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class IndexItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpDBReader::IndexItem: a plain Python object
    standing in front of one C++ QHelpDBReader::IndexItem.

    C++ hands a QHelpDBReader::IndexItem around as a copy, so every C++
    QHelpDBReader::IndexItem behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QHelpDBReader::IndexItem yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpDBReader::IndexItem::~IndexItem()': the destructor: Python
      removes its C++ QHelpDBReader::IndexItem by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QHelpDBReader::IndexItem is created at the first use, not by
      'QHelpDBReader::IndexItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpDBReader::IndexItem back gives a copy the
      ritual made for Python, in a new cute QHelpDBReader::IndexItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpDBReader::IndexItem'

    #  Qt's '~QHelpDBReader::IndexItem()'. Naming it makes this a value
    #  class: Python owns every C++ QHelpDBReader::IndexItem behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QHelpDBReader9IndexItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class IndexTable(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpDBReader::IndexTable: a plain Python object
    standing in front of one C++ QHelpDBReader::IndexTable.

    C++ hands a QHelpDBReader::IndexTable around as a copy, so every C++
    QHelpDBReader::IndexTable behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QHelpDBReader::IndexTable yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpDBReader::IndexTable::~IndexTable()': the destructor: Python
      removes its C++ QHelpDBReader::IndexTable by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QHelpDBReader::IndexTable is created at the first use, not by
      'QHelpDBReader::IndexTable(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpDBReader::IndexTable back gives a copy the
      ritual made for Python, in a new cute QHelpDBReader::IndexTable.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpDBReader::IndexTable'

    #  Qt's '~QHelpDBReader::IndexTable()'. Naming it makes this a value
    #  class: Python owns every C++ QHelpDBReader::IndexTable behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QHelpDBReader10IndexTableD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def versionHeuristic(namespaceName: str) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QHelpDBReader::versionHeuristic(const QString
    &namespaceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpdbreader.html#versionHeuristic

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QHelpDBReader::versionHeuristic(const QString
    #      &namespaceName)
    address = Rituals.call(
        'ritual_ZN13QHelpDBReader16versionHeuristicERK7QString',
        namespaceName,
    )
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpDBReader'

  #  A C++ QHelpDBReader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpDBReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpDBReader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpDBReader::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QHelpDBReader10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def namespaceName(self) -> str:
    """
    Calls Qt's 'QString QHelpDBReader::namespaceName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#namespaceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpDBReader::namespaceName() const
    return self.uglySide.call('ritual_ZNK13QHelpDBReader13namespaceNameEv')

  def virtualFolder(self) -> str:
    """
    Calls Qt's 'QString QHelpDBReader::virtualFolder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#virtualFolder

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpDBReader::virtualFolder() const
    return self.uglySide.call('ritual_ZNK13QHelpDBReader13virtualFolderEv')

  def version(self) -> str:
    """
    Calls Qt's 'QString QHelpDBReader::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#version

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpDBReader::version() const
    return self.uglySide.call('ritual_ZNK13QHelpDBReader7versionEv')

  @overload(str, str)
  def fileData(self, virtualFolder: str, filePath: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHelpDBReader::fileData(const QString
    &virtualFolder, const QString &filePath) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#fileData

    Parameters
    ----------

    virtualFolder : str
      Passed on as it is: a QString is made of it for the call.

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHelpDBReader::fileData(const QString &virtualFolder, const
    #      QString &filePath) const
    address = self.uglySide.call(
        'ritual_ZNK13QHelpDBReader8fileDataERK7QStringS2_',
        virtualFolder, filePath,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def customFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpDBReader::customFilters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#customFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpDBReader::customFilters() const
    address = self.uglySide.call(
        'ritual_ZNK13QHelpDBReader13customFiltersEv',
    )
    return QStringList._cuteOwning(address)

  @overload()
  @overload(str)
  def filterAttributes(self, filterName: str = '') -> QStringList:
    """
    Calls Qt's 'QStringList QHelpDBReader::filterAttributes(const QString
    &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpdbreader.html#filterAttributes

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpDBReader::filterAttributes(const QString &filterName)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QHelpDBReader16filterAttributesERK7QString', filterName,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def metaData(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QHelpDBReader::metaData(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#metaData

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHelpDBReader::metaData(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK13QHelpDBReader8metaDataERK7QString', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def quote(self, string: str) -> str:
    """
    Calls Qt's 'QString QHelpDBReader::quote(const QString &string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpdbreader.html#quote

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpDBReader::quote(const QString &string) const
    return self.uglySide.call(
        'ritual_ZNK13QHelpDBReader5quoteERK7QString', string,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QHelpDBReader::QHelpDBReader(const QString &dbName)': leans on
      'QHelpDBReader::qt_metacall(QMetaObject::Call, int, void**)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'QHelpDBReader::QHelpDBReader(const QString &dbName, const QString
      &uniqueId, QObject *parent)': leans on
      'QHelpDBReader::qt_metacall(QMetaObject::Call, int, void**)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QHelpDBReader.__init__' has no cute function yet. Qt's "
        "'QHelpDBReader::QHelpDBReader(const QString &dbName)': leans on "
        "'QHelpDBReader::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's "
        "'QHelpDBReader::QHelpDBReader(const QString &dbName, const QString "
        "&uniqueId, QObject *parent)': leans on "
        "'QHelpDBReader::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def filesData(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QString, QByteArray> QHelpDBReader::filesData(const
    QStringList &filterAttributes, const QString &extensionFilter) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpDBReader.filesData' has no cute function yet. Qt's "
        "'QMultiMap<QString, QByteArray> QHelpDBReader::filesData(const "
        "QStringList &filterAttributes, const QString &extensionFilter) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def filterAttributeSets(*__, **_) -> Never:
    """
    Qt's 'QList<QStringList> QHelpDBReader::filterAttributeSets() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpDBReader.filterAttributeSets' has no cute function yet. Qt's "
        "'QList<QStringList> QHelpDBReader::filterAttributeSets() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def indexTable(*__, **_) -> Never:
    """
    Qt's 'IndexTable QHelpDBReader::indexTable() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isAttributeUsed'.
    """
    raise NotImplementedError(
        "'QHelpDBReader.indexTable' has no cute function yet. Qt's "
        "'IndexTable QHelpDBReader::indexTable() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'isAttributeUsed'.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'bool QHelpDBReader::init()': leans on
    'QHelpDBReader::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpDBReader.init' has no cute function yet. Qt's 'bool "
        "QHelpDBReader::init()': leans on "
        "'QHelpDBReader::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def initDB(*__, **_) -> Never:
    """
    Qt's 'bool QHelpDBReader::initDB()': leans on
    'QHelpDBReader::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpDBReader.initDB' has no cute function yet. Qt's 'bool "
        "QHelpDBReader::initDB()': leans on "
        "'QHelpDBReader::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def qtVersionHeuristic(*__, **_) -> Never:
    """
    Qt's 'QString QHelpDBReader::qtVersionHeuristic() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'VersionData'.
    """
    raise NotImplementedError(
        "'QHelpDBReader.qtVersionHeuristic' has no cute function yet. Qt's "
        "'QString QHelpDBReader::qtVersionHeuristic() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'VersionData'.")
