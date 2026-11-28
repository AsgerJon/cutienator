"""
QQC2::QStyleOptionToolBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionToolBar to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionToolBar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionToolBar: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionToolBar.

  C++ hands a QQC2::QStyleOptionToolBar around as a copy, so every C++
  QQC2::QStyleOptionToolBar behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionToolBar yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionToolBar &QQC2::QStyleOptionToolBar::operator=(const
    QStyleOptionToolBar &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionToolBar::~QStyleOptionToolBar()': the destructor:
    Python removes its C++ QQC2::QStyleOptionToolBar by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionToolBar is created at the first use, not by
    'QQC2::QStyleOptionToolBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionToolBar back gives a copy the
    ritual made for Python, in a new cute QQC2::QStyleOptionToolBar.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionToolBar, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionToolBar::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](14)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionToolBar::StyleOptionVersion' of Qt, with the
    1 names Qt gives in it.
    """

    Version = Kee[int](1)

  class ToolBarFeature(CuteFlags):
    """
    The flags enum 'QQC2::QStyleOptionToolBar::ToolBarFeature' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QQC2::QStyleOptionToolBar::ToolBarFeatures'.
    """

    NULL = 0x0
    Movable = 0x1

  ToolBarFeatures = ToolBarFeature

  class ToolBarPosition(CuteNum):
    """
    The enum 'QQC2::QStyleOptionToolBar::ToolBarPosition' of Qt, with the 4
    names Qt gives in it.
    """

    Beginning = Kee[int](0)
    Middle = Kee[int](1)
    End = Kee[int](2)
    OnlyOne = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QStyleOptionToolBar'

  #  Qt's '~QQC2::QStyleOptionToolBar()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleOptionToolBar behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC219QStyleOptionToolBarD1Ev'

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
    'QQC2::QStyleOptionToolBar::QStyleOptionToolBar()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiontoolbar.html#QStyleOptionToolBar
    """
    #  QQC2::QStyleOptionToolBar::QStyleOptionToolBar()
    self._noteCreation(QStyleOptionToolBar, lambda: Rituals.call(
        'ritual_ZN4QQC219QStyleOptionToolBarC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionToolBar) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionToolBar::QStyleOptionToolBar(const QStyleOptionToolBar
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiontoolbar.html#QStyleOptionToolBar

    Parameters
    ----------

    other : QStyleOptionToolBar
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionToolBar, which
      stays Python's own.
    """
    #  QQC2::QStyleOptionToolBar::QStyleOptionToolBar(const
    #      QStyleOptionToolBar &other)
    self._noteCreation(QStyleOptionToolBar, lambda: Rituals.call(
        'ritual_ZN4QQC219QStyleOptionToolBarC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionToolBar::QStyleOptionToolBar(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptiontoolbar.html#QStyleOptionToolBar

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionToolBar::QStyleOptionToolBar(int version)
    self._noteCreation(QStyleOptionToolBar, lambda: Rituals.call(
        'ritual_ZN4QQC219QStyleOptionToolBarC1Ei', version,
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
