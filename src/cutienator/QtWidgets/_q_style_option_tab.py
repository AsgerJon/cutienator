"""
QStyleOptionTab binding of the Qt C++
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

from ..cute import CuteFlags, CuteNum
from ..occult import Rituals
from . import QStyleOption


class QStyleOptionTab(QStyleOption):
  """
  The cute side of Qt's QStyleOptionTab: a plain Python object standing in
  front of one C++ QStyleOptionTab.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionTab is built on
  Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionTab around as a copy, so every C++ QStyleOptionTab
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionTab yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionTab &QStyleOptionTab::operator=(const QStyleOptionTab
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QStyleOptionTab::~QStyleOptionTab()': the destructor: Python
    removes its C++ QStyleOptionTab by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStyleOptionTab is created at the first use, not by
    'QStyleOptionTab(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionTab back gives a copy the ritual made for
    Python, in a new cute QStyleOptionTab.
  """

  #  The enums Qt writes inside QStyleOptionTab, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CornerWidget(CuteFlags):
    """
    The flags enum 'QStyleOptionTab::CornerWidget' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QStyleOptionTab::CornerWidgets'.
    """

    NoCornerWidgets = 0x0
    LeftCornerWidget = 0x1
    RightCornerWidget = 0x2

  CornerWidgets = CornerWidget

  class SelectedPosition(CuteNum):
    """
    The enum 'QStyleOptionTab::SelectedPosition' of Qt, with the 3 names Qt
    gives in it.
    """

    NotAdjacent = Kee[int](0)
    NextIsSelected = Kee[int](1)
    PreviousIsSelected = Kee[int](2)

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionTab::StyleOptionType' of Qt, with the 1 names Qt
    gives in it.
    """

    Type = Kee[int](3)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionTab::StyleOptionVersion' of Qt, with the 1 names Qt
    gives in it.
    """

    Version = Kee[int](1)

  class TabFeature(CuteFlags):
    """
    The flags enum 'QStyleOptionTab::TabFeature' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QStyleOptionTab::TabFeatures'.
    """

    NULL = 0x0
    HasFrame = 0x1
    MinimumSizeHint = 0x2

  TabFeatures = TabFeature

  class TabPosition(CuteNum):
    """
    The enum 'QStyleOptionTab::TabPosition' of Qt, with the 5 names Qt gives
    in it.
    """

    Beginning = Kee[int](0)
    Middle = Kee[int](1)
    End = Kee[int](2)
    OnlyOneTab = Kee[int](3)
    Moving = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionTab'

  #  Qt's '~QStyleOptionTab()'. Naming it makes this a value class: Python
  #  owns every C++ QStyleOptionTab behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QStyleOptionTabD1Ev'

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
    Notes what was given, for Qt's 'QStyleOptionTab::QStyleOptionTab()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontab.html#QStyleOptionTab
    """
    #  QStyleOptionTab::QStyleOptionTab()
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN15QStyleOptionTabC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionTab) -> None:
    """
    Notes what was given, for Qt's 'QStyleOptionTab::QStyleOptionTab(const
    QStyleOptionTab &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontab.html#QStyleOptionTab

    Parameters
    ----------

    other : QStyleOptionTab
      Passed on as a value: Qt reads the C++ QStyleOptionTab, which stays
      Python's own.
    """
    #  QStyleOptionTab::QStyleOptionTab(const QStyleOptionTab &other)
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN15QStyleOptionTabC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's 'QStyleOptionTab::QStyleOptionTab(int
    version)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontab.html#QStyleOptionTab

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionTab::QStyleOptionTab(int version)
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN15QStyleOptionTabC1Ei', version,
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
