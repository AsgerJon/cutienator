"""
QStyleOptionToolBar binding of the Qt C++
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


class QStyleOptionToolBar(QStyleOption):
  """
  The cute side of Qt's QStyleOptionToolBar: a plain Python object standing
  in front of one C++ QStyleOptionToolBar.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionToolBar is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionToolBar around as a copy, so every C++
  QStyleOptionToolBar behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionToolBar yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionToolBar::~QStyleOptionToolBar()': the destructor:
    Python removes its C++ QStyleOptionToolBar by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionToolBar is created at the first use, not by
    'QStyleOptionToolBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionToolBar back gives a copy the ritual made
    for Python, in a new cute QStyleOptionToolBar.
  """

  #  The enums Qt writes inside QStyleOptionToolBar, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionToolBar::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](14)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionToolBar::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](1)

  class ToolBarFeature(CuteFlags):
    """
    The flags enum 'QStyleOptionToolBar::ToolBarFeature' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QStyleOptionToolBar::ToolBarFeatures'.
    """

    NULL = 0x0
    Movable = 0x1

  ToolBarFeatures = ToolBarFeature

  class ToolBarPosition(CuteNum):
    """
    The enum 'QStyleOptionToolBar::ToolBarPosition' of Qt, with the 4 names
    Qt gives in it.
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
  __qt_class__ = 'QStyleOptionToolBar'

  #  Qt's '~QStyleOptionToolBar()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionToolBar behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QStyleOptionToolBarD1Ev'

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
    'QStyleOptionToolBar::QStyleOptionToolBar()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbar.html#QStyleOptionToolBar
    """
    #  QStyleOptionToolBar::QStyleOptionToolBar()
    self._noteCreation(QStyleOptionToolBar, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionToolBarC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionToolBar) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionToolBar::QStyleOptionToolBar(const QStyleOptionToolBar
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbar.html#QStyleOptionToolBar

    Parameters
    ----------

    other : QStyleOptionToolBar
      Passed on as a value: Qt reads the C++ QStyleOptionToolBar, which stays
      Python's own.
    """
    #  QStyleOptionToolBar::QStyleOptionToolBar(const QStyleOptionToolBar
    #      &other)
    self._noteCreation(QStyleOptionToolBar, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionToolBarC1ERKS_', self._valueOf(other),
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
