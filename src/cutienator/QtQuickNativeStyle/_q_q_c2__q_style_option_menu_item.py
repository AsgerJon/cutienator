"""
QQC2::QStyleOptionMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionMenuItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionMenuItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionMenuItem: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionMenuItem.

  C++ hands a QQC2::QStyleOptionMenuItem around as a copy, so every C++
  QQC2::QStyleOptionMenuItem behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionMenuItem yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionMenuItem &QQC2::QStyleOptionMenuItem::operator=(const
    QStyleOptionMenuItem &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionMenuItem::~QStyleOptionMenuItem()': the
    destructor: Python removes its C++ QQC2::QStyleOptionMenuItem by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionMenuItem is created at the first use, not by
    'QQC2::QStyleOptionMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionMenuItem back gives a copy the
    ritual made for Python, in a new cute QQC2::QStyleOptionMenuItem.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionMenuItem, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class CheckType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionMenuItem::CheckType' of Qt, with the 3 names
    Qt gives in it.
    """

    NotCheckable = Kee[int](0)
    Exclusive = Kee[int](1)
    NonExclusive = Kee[int](2)

  class MenuItemType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionMenuItem::MenuItemType' of Qt, with the 8
    names Qt gives in it.
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
    The enum 'QQC2::QStyleOptionMenuItem::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](4)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionMenuItem::StyleOptionVersion' of Qt, with the
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
  __qt_class__ = 'QQC2::QStyleOptionMenuItem'

  #  Qt's '~QQC2::QStyleOptionMenuItem()'. Naming it makes this a value
  #  class: Python owns every C++ QQC2::QStyleOptionMenuItem behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC220QStyleOptionMenuItemD1Ev'

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
    'QQC2::QStyleOptionMenuItem::QStyleOptionMenuItem()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionmenuitem.html
    """
    #  QQC2::QStyleOptionMenuItem::QStyleOptionMenuItem()
    self._noteCreation(QStyleOptionMenuItem, lambda: Rituals.call(
        'ritual_ZN4QQC220QStyleOptionMenuItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionMenuItem) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionMenuItem::QStyleOptionMenuItem(const
    QStyleOptionMenuItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionmenuitem.html

    Parameters
    ----------

    other : QStyleOptionMenuItem
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionMenuItem,
      which stays Python's own.
    """
    #  QQC2::QStyleOptionMenuItem::QStyleOptionMenuItem(const
    #      QStyleOptionMenuItem &other)
    self._noteCreation(QStyleOptionMenuItem, lambda: Rituals.call(
        'ritual_ZN4QQC220QStyleOptionMenuItemC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionMenuItem::QStyleOptionMenuItem(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionmenuitem.html

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionMenuItem::QStyleOptionMenuItem(int version)
    self._noteCreation(QStyleOptionMenuItem, lambda: Rituals.call(
        'ritual_ZN4QQC220QStyleOptionMenuItemC1Ei', version,
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
