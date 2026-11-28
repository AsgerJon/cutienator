"""
QQC2::QStyleOptionComplex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionComplex to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionComplex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionComplex: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionComplex.

  C++ hands a QQC2::QStyleOptionComplex around as a copy, so every C++
  QQC2::QStyleOptionComplex behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionComplex yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionComplex &QQC2::QStyleOptionComplex::operator=(const
    QStyleOptionComplex &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionComplex::~QStyleOptionComplex()': the destructor:
    Python removes its C++ QQC2::QStyleOptionComplex by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionComplex is created at the first use, not by
    'QQC2::QStyleOptionComplex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionComplex back gives a copy the
    ritual made for Python, in a new cute QQC2::QStyleOptionComplex.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionComplex, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionComplex::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](983040)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionComplex::StyleOptionVersion' of Qt, with the
    1 names Qt gives in it.
    """

    Version = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QStyleOptionComplex'

  #  Qt's '~QQC2::QStyleOptionComplex()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleOptionComplex behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC219QStyleOptionComplexD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(int)
  @overload(int, int)
  def __init__(self, version: int = 1, type: int = 983040) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionComplex::QStyleOptionComplex(int version, int type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptioncomplex.html#QStyleOptionComplex

    Parameters
    ----------

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 983040.
    """
    #  QQC2::QStyleOptionComplex::QStyleOptionComplex(int version, int type)
    self._noteCreation(QStyleOptionComplex, lambda: Rituals.call(
        'ritual_ZN4QQC219QStyleOptionComplexC1Eii', version, type,
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionComplex) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionComplex::QStyleOptionComplex(const QStyleOptionComplex
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptioncomplex.html#QStyleOptionComplex

    Parameters
    ----------

    other : QStyleOptionComplex
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionComplex, which
      stays Python's own.
    """
    #  QQC2::QStyleOptionComplex::QStyleOptionComplex(const
    #      QStyleOptionComplex &other)
    self._noteCreation(QStyleOptionComplex, lambda: Rituals.call(
        'ritual_ZN4QQC219QStyleOptionComplexC1ERKS0_', self._valueOf(other),
    ))

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
