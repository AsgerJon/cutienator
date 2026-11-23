"""
QStyleOptionTitleBar binding of the Qt C++
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
from . import QStyleOptionComplex


class QStyleOptionTitleBar(QStyleOptionComplex):
  """
  The cute side of Qt's QStyleOptionTitleBar: a plain Python object standing
  in front of one C++ QStyleOptionTitleBar.

  It is built on the cute 'QStyleOptionComplex', as Qt's QStyleOptionTitleBar
  is built on Qt's QStyleOptionComplex, and has everything that class has.

  C++ hands a QStyleOptionTitleBar around as a copy, so every C++
  QStyleOptionTitleBar behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionTitleBar yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionTitleBar::~QStyleOptionTitleBar()': the destructor:
    Python removes its C++ QStyleOptionTitleBar by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOptionTitleBar is created at the first use, not by
    'QStyleOptionTitleBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionTitleBar back gives a copy the ritual
    made for Python, in a new cute QStyleOptionTitleBar.
  """

  #  The enums Qt writes inside QStyleOptionTitleBar, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionTitleBar::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](983045)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionTitleBar::StyleOptionVersion' of Qt, with the 1
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
  __qt_class__ = 'QStyleOptionTitleBar'

  #  Qt's '~QStyleOptionTitleBar()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionTitleBar behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QStyleOptionTitleBarD1Ev'

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
    'QStyleOptionTitleBar::QStyleOptionTitleBar()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontitlebar.html#QStyleOptionTitleBar
    """
    #  QStyleOptionTitleBar::QStyleOptionTitleBar()
    self._noteCreation(QStyleOptionTitleBar, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionTitleBarC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionTitleBar) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTitleBar::QStyleOptionTitleBar(const QStyleOptionTitleBar
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontitlebar.html#QStyleOptionTitleBar

    Parameters
    ----------

    other : QStyleOptionTitleBar
      Passed on as a value: Qt reads the C++ QStyleOptionTitleBar, which
      stays Python's own.
    """
    #  QStyleOptionTitleBar::QStyleOptionTitleBar(const QStyleOptionTitleBar
    #      &other)
    self._noteCreation(QStyleOptionTitleBar, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionTitleBarC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTitleBar::QStyleOptionTitleBar(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontitlebar.html#QStyleOptionTitleBar

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionTitleBar::QStyleOptionTitleBar(int version)
    self._noteCreation(QStyleOptionTitleBar, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionTitleBarC1Ei', version,
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
