"""
QMimeGlobPatternList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeGlobPatternList to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMimeGlobPatternList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeGlobPatternList: a plain Python object standing
  in front of one C++ QMimeGlobPatternList.

  C++ hands a QMimeGlobPatternList around as a copy, so every C++
  QMimeGlobPatternList behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMimeGlobPatternList that has a ritual and that
  Python can call so far, 2 names in all: 'hasPattern', 'removeMimeType'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMimeGlobPatternList::match(QMimeGlobMatchResult &result,
    const QString &fileName, const AddMatchFilterFunc &filterFunc) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMimeGlobPatternList::~QMimeGlobPatternList()': the destructor:
    Python removes its C++ QMimeGlobPatternList by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMimeGlobPatternList is created at the first use, not by
    'QMimeGlobPatternList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMimeGlobPatternList back gives a copy the ritual
    made for Python, in a new cute QMimeGlobPatternList.
  - Each name of Qt's QMimeGlobPatternList that has no cute function yet,
    'match', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeGlobPatternList'

  #  Qt's '~QMimeGlobPatternList()'. Naming it makes this a value class:
  #  Python owns every C++ QMimeGlobPatternList behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QMimeGlobPatternListD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def hasPattern(self, mimeType: str, pattern: str) -> bool:
    """
    Calls Qt's 'bool QMimeGlobPatternList::hasPattern(QStringView mimeType,
    QStringView pattern) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeglobpatternlist.html#hasPattern

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeGlobPatternList::hasPattern(QStringView mimeType,
    #      QStringView pattern) const
    return self.uglySide.call(
        'ritual_ZNK20QMimeGlobPatternList10hasPatternE11QStringViewS0_',
        mimeType, pattern,
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

  @overload(str)
  def removeMimeType(self, mimeType: str) -> None:
    """
    Calls Qt's 'void QMimeGlobPatternList::removeMimeType(QStringView
    mimeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeglobpatternlist.html#removeMimeType

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeGlobPatternList::removeMimeType(QStringView mimeType)
    self.uglySide.call(
        'ritual_ZN20QMimeGlobPatternList14removeMimeTypeE11QStringView',
        mimeType,
    )

  @staticmethod
  def match(*__, **_) -> Never:
    """
    Qt's 'void QMimeGlobPatternList::match(QMimeGlobMatchResult &result,
    const QString &fileName, const AddMatchFilterFunc &filterFunc) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeGlobPatternList.match' has no cute function yet. Qt's 'void "
        "QMimeGlobPatternList::match(QMimeGlobMatchResult &result, const "
        "QString &fileName, const AddMatchFilterFunc &filterFunc) const': "
        "takes a type Python has no way to hand over yet.")
