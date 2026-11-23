"""
QStyleOptionTabBarBase binding of the Qt C++
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


class QStyleOptionTabBarBase(QStyleOption):
  """
  The cute side of Qt's QStyleOptionTabBarBase: a plain Python object
  standing in front of one C++ QStyleOptionTabBarBase.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionTabBarBase is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionTabBarBase around as a copy, so every C++
  QStyleOptionTabBarBase behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionTabBarBase yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionTabBarBase::~QStyleOptionTabBarBase()': the destructor:
    Python removes its C++ QStyleOptionTabBarBase by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOptionTabBarBase is created at the first use, not by
    'QStyleOptionTabBarBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionTabBarBase back gives a copy the ritual
    made for Python, in a new cute QStyleOptionTabBarBase.
  """

  #  The enums Qt writes inside QStyleOptionTabBarBase, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionTabBarBase::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](12)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionTabBarBase::StyleOptionVersion' of Qt, with the 1
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
  __qt_class__ = 'QStyleOptionTabBarBase'

  #  Qt's '~QStyleOptionTabBarBase()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionTabBarBase behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QStyleOptionTabBarBaseD1Ev'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTabBarBase::QStyleOptionTabBarBase()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontabbarbase.html#QStyleOptionTabBarBase
    """
    #  QStyleOptionTabBarBase::QStyleOptionTabBarBase()
    self._noteCreation(QStyleOptionTabBarBase, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionTabBarBaseC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionTabBarBase) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTabBarBase::QStyleOptionTabBarBase(const
    QStyleOptionTabBarBase &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontabbarbase.html#QStyleOptionTabBarBase

    Parameters
    ----------

    other : QStyleOptionTabBarBase
      Passed on as a value: Qt reads the C++ QStyleOptionTabBarBase, which
      stays Python's own.
    """
    #  QStyleOptionTabBarBase::QStyleOptionTabBarBase(const
    #      QStyleOptionTabBarBase &other)
    self._noteCreation(QStyleOptionTabBarBase, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionTabBarBaseC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTabBarBase::QStyleOptionTabBarBase(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontabbarbase.html#QStyleOptionTabBarBase

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionTabBarBase::QStyleOptionTabBarBase(int version)
    self._noteCreation(QStyleOptionTabBarBase, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionTabBarBaseC1Ei', version,
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
