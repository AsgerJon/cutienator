"""
QStyleOptionToolBox binding of the Qt C++
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


class QStyleOptionToolBox(QStyleOption):
  """
  The cute side of Qt's QStyleOptionToolBox: a plain Python object standing
  in front of one C++ QStyleOptionToolBox.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionToolBox is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionToolBox around as a copy, so every C++
  QStyleOptionToolBox behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionToolBox yet. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionToolBox &QStyleOptionToolBox::operator=(const
    QStyleOptionToolBox &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QStyleOptionToolBox::~QStyleOptionToolBox()': the destructor:
    Python removes its C++ QStyleOptionToolBox by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QStyleOptionToolBox is created at the first use, not by
    'QStyleOptionToolBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionToolBox back gives a copy the ritual made
    for Python, in a new cute QStyleOptionToolBox.
  """

  #  The enums Qt writes inside QStyleOptionToolBox, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SelectedPosition(CuteNum):
    """
    The enum 'QStyleOptionToolBox::SelectedPosition' of Qt, with the 3 names
    Qt gives in it.
    """

    NotAdjacent = Kee[int](0)
    NextIsSelected = Kee[int](1)
    PreviousIsSelected = Kee[int](2)

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionToolBox::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](7)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionToolBox::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](1)

  class TabPosition(CuteNum):
    """
    The enum 'QStyleOptionToolBox::TabPosition' of Qt, with the 4 names Qt
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
  __qt_class__ = 'QStyleOptionToolBox'

  #  Qt's '~QStyleOptionToolBox()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionToolBox behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QStyleOptionToolBoxD1Ev'

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
    'QStyleOptionToolBox::QStyleOptionToolBox()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbox.html#QStyleOptionToolBox
    """
    #  QStyleOptionToolBox::QStyleOptionToolBox()
    self._noteCreation(QStyleOptionToolBox, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionToolBoxC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionToolBox) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionToolBox::QStyleOptionToolBox(const QStyleOptionToolBox
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbox.html#QStyleOptionToolBox

    Parameters
    ----------

    other : QStyleOptionToolBox
      Passed on as a value: Qt reads the C++ QStyleOptionToolBox, which stays
      Python's own.
    """
    #  QStyleOptionToolBox::QStyleOptionToolBox(const QStyleOptionToolBox
    #      &other)
    self._noteCreation(QStyleOptionToolBox, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionToolBoxC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionToolBox::QStyleOptionToolBox(int version)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbox.html#QStyleOptionToolBox

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionToolBox::QStyleOptionToolBox(int version)
    self._noteCreation(QStyleOptionToolBox, lambda: Rituals.call(
        'ritual_ZN19QStyleOptionToolBoxC1Ei', version,
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
