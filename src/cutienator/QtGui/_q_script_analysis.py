"""
QScriptAnalysis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QScriptAnalysis to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class QScriptAnalysis(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScriptAnalysis: a plain Python object standing in
  front of one C++ QScriptAnalysis.

  C++ hands a QScriptAnalysis around as a copy, so every C++ QScriptAnalysis
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScriptAnalysis that has a ritual and that Python
  can call so far, 1 name in all: '__eq__'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScriptAnalysis::~QScriptAnalysis()': the destructor: Python
    removes its C++ QScriptAnalysis by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScriptAnalysis is created at the first use, not by
    'QScriptAnalysis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScriptAnalysis back gives a copy the ritual made for
    Python, in a new cute QScriptAnalysis.
  """

  #  The enums Qt writes inside QScriptAnalysis, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BidiFlags(CuteNum):
    """
    The enum 'QScriptAnalysis::BidiFlags' of Qt, with the 4 names Qt gives in
    it.
    """

    BidiBN = Kee[int](1)
    BidiMaybeResetToParagraphLevel = Kee[int](2)
    BidiResetToParagraphLevel = Kee[int](4)
    BidiMirrored = Kee[int](8)

  class Flags(CuteNum):
    """
    The enum 'QScriptAnalysis::Flags' of Qt, with the 11 names Qt gives in
    it.
    """

    NULL = Kee[int](0)
    Lowercase = Kee[int](1)
    Uppercase = Kee[int](2)
    SmallCaps = Kee[int](3)
    LineOrParagraphSeparator = Kee[int](4)
    Space = Kee[int](5)
    SpaceTabOrObject = Kee[int](5)
    Nbsp = Kee[int](6)
    Tab = Kee[int](7)
    TabOrObject = Kee[int](7)
    Object = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScriptAnalysis'

  #  Qt's '~QScriptAnalysis()'. Naming it makes this a value class: Python
  #  owns every C++ QScriptAnalysis behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QScriptAnalysisD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QScriptAnalysis) -> bool:
    """
    Calls Qt's 'bool QScriptAnalysis::operator==(const QScriptAnalysis
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscriptanalysis.html#operator==

    Parameters
    ----------

    other : QScriptAnalysis
      Passed on as a value: Qt reads the C++ QScriptAnalysis, which stays
      Python's own.
    """
    #  bool QScriptAnalysis::operator==(const QScriptAnalysis &other) const
    return self.uglySide.call(
        'ritual_ZNK15QScriptAnalysiseqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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
