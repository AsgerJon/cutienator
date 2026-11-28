"""
QStyleOptionComplex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QStyleOption


class QStyleOptionComplex(QStyleOption):
  """
  The cute side of Qt's QStyleOptionComplex: a plain Python object standing
  in front of one C++ QStyleOptionComplex.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionComplex is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionComplex around as a copy, so every C++
  QStyleOptionComplex behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionComplex yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionComplex &QStyleOptionComplex::operator=(const
    QStyleOptionComplex &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QStyleOptionComplex::~QStyleOptionComplex()': the destructor:
    Python removes its C++ QStyleOptionComplex by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QStyleOptionComplex is created at the first use, not by
    'QStyleOptionComplex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionComplex back gives a copy the ritual made
    for Python, in a new cute QStyleOptionComplex.
  """

  #  The enums Qt writes inside QStyleOptionComplex, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionComplex::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](983040)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionComplex::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
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
  __qt_class__ = 'QStyleOptionComplex'

  #  Qt's '~QStyleOptionComplex()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionComplex behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QStyleOptionComplexD1Ev'

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
    'QStyleOptionComplex::QStyleOptionComplex(int version, int type)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptioncomplex.html#QStyleOptionComplex

    Parameters
    ----------

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 983040.
    """
    #  QStyleOptionComplex::QStyleOptionComplex(int version, int type)
    self._noteCreation(QStyleOptionComplex, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionComplexC1Eii', version, type,
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionComplex) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionComplex::QStyleOptionComplex(const QStyleOptionComplex
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptioncomplex.html#QStyleOptionComplex

    Parameters
    ----------

    other : QStyleOptionComplex
      Passed on as a value: Qt reads the C++ QStyleOptionComplex, which stays
      Python's own.
    """
    #  QStyleOptionComplex::QStyleOptionComplex(const QStyleOptionComplex
    #      &other)
    self._noteCreation(QStyleOptionComplex, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionComplexC1ERKS_', self._valueOf(other),
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
