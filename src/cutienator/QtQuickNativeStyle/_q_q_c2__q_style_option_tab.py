"""
QQC2::QStyleOptionTab binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionTab to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionTab(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionTab: a plain Python object standing
  in front of one C++ QQC2::QStyleOptionTab.

  C++ hands a QQC2::QStyleOptionTab around as a copy, so every C++
  QQC2::QStyleOptionTab behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionTab yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionTab &QQC2::QStyleOptionTab::operator=(const
    QStyleOptionTab &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionTab::~QStyleOptionTab()': the destructor: Python
    removes its C++ QQC2::QStyleOptionTab by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionTab is created at the first use, not by
    'QQC2::QStyleOptionTab(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionTab back gives a copy the ritual
    made for Python, in a new cute QQC2::QStyleOptionTab.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionTab, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CornerWidget(CuteFlags):
    """
    The flags enum 'QQC2::QStyleOptionTab::CornerWidget' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QQC2::QStyleOptionTab::CornerWidgets'.
    """

    NoCornerWidgets = 0x0
    LeftCornerWidget = 0x1
    RightCornerWidget = 0x2

  CornerWidgets = CornerWidget

  class SelectedPosition(CuteNum):
    """
    The enum 'QQC2::QStyleOptionTab::SelectedPosition' of Qt, with the 3
    names Qt gives in it.
    """

    NotAdjacent = Kee[int](0)
    NextIsSelected = Kee[int](1)
    PreviousIsSelected = Kee[int](2)

  class Shape(CuteNum):
    """
    The enum 'QQC2::QStyleOptionTab::Shape' of Qt, with the 8 names Qt gives
    in it.
    """

    RoundedNorth = Kee[int](0)
    RoundedSouth = Kee[int](1)
    RoundedWest = Kee[int](2)
    RoundedEast = Kee[int](3)
    TriangularNorth = Kee[int](4)
    TriangularSouth = Kee[int](5)
    TriangularWest = Kee[int](6)
    TriangularEast = Kee[int](7)

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionTab::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](3)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionTab::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](3)

  class TabFeature(CuteFlags):
    """
    The flags enum 'QQC2::QStyleOptionTab::TabFeature' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QQC2::QStyleOptionTab::TabFeatures'.
    """

    NULL = 0x0
    HasFrame = 0x1

  TabFeatures = TabFeature

  class TabPosition(CuteNum):
    """
    The enum 'QQC2::QStyleOptionTab::TabPosition' of Qt, with the 4 names Qt
    gives in it.
    """

    Beginning = Kee[int](0)
    Middle = Kee[int](1)
    End = Kee[int](2)
    OnlyOneTab = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QStyleOptionTab'

  #  Qt's '~QQC2::QStyleOptionTab()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleOptionTab behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC215QStyleOptionTabD1Ev'

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
    'QQC2::QStyleOptionTab::QStyleOptionTab()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiontab.html#QStyleOptionTab
    """
    #  QQC2::QStyleOptionTab::QStyleOptionTab()
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN4QQC215QStyleOptionTabC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionTab) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionTab::QStyleOptionTab(const QStyleOptionTab &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiontab.html#QStyleOptionTab

    Parameters
    ----------

    other : QStyleOptionTab
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionTab, which
      stays Python's own.
    """
    #  QQC2::QStyleOptionTab::QStyleOptionTab(const QStyleOptionTab &other)
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN4QQC215QStyleOptionTabC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionTab::QStyleOptionTab(int version)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiontab.html#QStyleOptionTab

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionTab::QStyleOptionTab(int version)
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN4QQC215QStyleOptionTabC1Ei', version,
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
