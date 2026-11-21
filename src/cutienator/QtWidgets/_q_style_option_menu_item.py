"""
QStyleOptionMenuItem binding of the Qt C++
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


class QStyleOptionMenuItem(QStyleOption):
  """
  The cute side of Qt's QStyleOptionMenuItem: a plain Python object standing
  in front of one C++ QStyleOptionMenuItem.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionMenuItem is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionMenuItem around as a copy, so every C++
  QStyleOptionMenuItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionMenuItem yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionMenuItem::~QStyleOptionMenuItem()': the destructor:
    Python removes its C++ QStyleOptionMenuItem by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionMenuItem is created at the first use, not by
    'QStyleOptionMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionMenuItem back gives a copy the ritual
    made for Python, in a new cute QStyleOptionMenuItem.
  """

  #  The enums Qt writes inside QStyleOptionMenuItem, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CheckType(CuteNum):
    """
    The enum 'QStyleOptionMenuItem::CheckType' of Qt, with the 3 names Qt
    gives in it.
    """

    NotCheckable = Kee[int](0)
    Exclusive = Kee[int](1)
    NonExclusive = Kee[int](2)

  class MenuItemType(CuteNum):
    """
    The enum 'QStyleOptionMenuItem::MenuItemType' of Qt, with the 8 names Qt
    gives in it.
    """

    Normal = Kee[int](0)
    DefaultItem = Kee[int](1)
    Separator = Kee[int](2)
    SubMenu = Kee[int](3)
    Scroller = Kee[int](4)
    TearOff = Kee[int](5)
    Margin = Kee[int](6)
    EmptyArea = Kee[int](7)

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionMenuItem::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](4)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionMenuItem::StyleOptionVersion' of Qt, with the 1
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
  __qt_class__ = 'QStyleOptionMenuItem'

  #  Qt's '~QStyleOptionMenuItem()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionMenuItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QStyleOptionMenuItemD1Ev'

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
    'QStyleOptionMenuItem::QStyleOptionMenuItem()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionmenuitem.html#QStyleOptionMenuItem
    """
    #  QStyleOptionMenuItem::QStyleOptionMenuItem()
    self._noteCreation(QStyleOptionMenuItem, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionMenuItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionMenuItem) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionMenuItem::QStyleOptionMenuItem(const QStyleOptionMenuItem
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionmenuitem.html#QStyleOptionMenuItem

    Parameters
    ----------

    other : QStyleOptionMenuItem
      Passed on as a value: Qt reads the C++ QStyleOptionMenuItem, which
      stays Python's own.
    """
    #  QStyleOptionMenuItem::QStyleOptionMenuItem(const QStyleOptionMenuItem
    #      &other)
    self._noteCreation(QStyleOptionMenuItem, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionMenuItemC1ERKS_', self._valueOf(other),
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
