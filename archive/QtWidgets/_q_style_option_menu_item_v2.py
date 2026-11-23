"""
QStyleOptionMenuItemV2 binding of the Qt C++
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
from . import QStyleOptionMenuItem


class QStyleOptionMenuItemV2(QStyleOptionMenuItem):
  """
  The cute side of Qt's QStyleOptionMenuItemV2: a plain Python object
  standing in front of one C++ QStyleOptionMenuItemV2.

  It is built on the cute 'QStyleOptionMenuItem', as Qt's
  QStyleOptionMenuItemV2 is built on Qt's QStyleOptionMenuItem, and has
  everything that class has.

  C++ hands a QStyleOptionMenuItemV2 around as a copy, so every C++
  QStyleOptionMenuItemV2 behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionMenuItemV2 yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionMenuItemV2::~QStyleOptionMenuItemV2()': the destructor:
    Python removes its C++ QStyleOptionMenuItemV2 by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOptionMenuItemV2 is created at the first use, not by
    'QStyleOptionMenuItemV2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionMenuItemV2 back gives a copy the ritual
    made for Python, in a new cute QStyleOptionMenuItemV2.
  """

  #  The enums Qt writes inside QStyleOptionMenuItemV2, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionMenuItemV2::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionMenuItemV2'

  #  Qt's '~QStyleOptionMenuItemV2()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionMenuItemV2 behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QStyleOptionMenuItemV2D1Ev'

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
    'QStyleOptionMenuItemV2::QStyleOptionMenuItemV2()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionmenuitemv2.html#QStyleOptionMenuItemV2
    """
    #  QStyleOptionMenuItemV2::QStyleOptionMenuItemV2()
    self._noteCreation(QStyleOptionMenuItemV2, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionMenuItemV2C1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionMenuItemV2) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionMenuItemV2::QStyleOptionMenuItemV2(const
    QStyleOptionMenuItemV2 &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionmenuitemv2.html#QStyleOptionMenuItemV2

    Parameters
    ----------

    other : QStyleOptionMenuItemV2
      Passed on as a value: Qt reads the C++ QStyleOptionMenuItemV2, which
      stays Python's own.
    """
    #  QStyleOptionMenuItemV2::QStyleOptionMenuItemV2(const
    #      QStyleOptionMenuItemV2 &other)
    self._noteCreation(QStyleOptionMenuItemV2, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionMenuItemV2C1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionMenuItemV2::QStyleOptionMenuItemV2(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionmenuitemv2.html#QStyleOptionMenuItemV2

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionMenuItemV2::QStyleOptionMenuItemV2(int version)
    self._noteCreation(QStyleOptionMenuItemV2, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionMenuItemV2C1Ei', version,
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
