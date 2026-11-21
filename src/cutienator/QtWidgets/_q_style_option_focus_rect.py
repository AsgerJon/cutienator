"""
QStyleOptionFocusRect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QStyleOption, QStyleOptionFocusRectStyleOptionType
from . import QStyleOptionFocusRectStyleOptionVersion


class QStyleOptionFocusRect(QStyleOption):
  """
  The cute side of Qt's QStyleOptionFocusRect: a plain Python object standing
  in front of one C++ QStyleOptionFocusRect.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionFocusRect is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionFocusRect around as a copy, so every C++
  QStyleOptionFocusRect behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionFocusRect yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionFocusRect::~QStyleOptionFocusRect()': the destructor:
    Python removes its C++ QStyleOptionFocusRect by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionFocusRect is created at the first use, not by
    'QStyleOptionFocusRect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionFocusRect back gives a copy the ritual
    made for Python, in a new cute QStyleOptionFocusRect.
  """

  #  The enums Qt writes inside QStyleOptionFocusRect, and the names Qt has
  #  for the combinations of its flags enums.
  StyleOptionType = QStyleOptionFocusRectStyleOptionType
  StyleOptionVersion = QStyleOptionFocusRectStyleOptionVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionFocusRect'

  #  Qt's '~QStyleOptionFocusRect()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionFocusRect behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QStyleOptionFocusRectD1Ev'

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
    'QStyleOptionFocusRect::QStyleOptionFocusRect()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionfocusrect.html#QStyleOptionFocusRect
    """
    #  QStyleOptionFocusRect::QStyleOptionFocusRect()
    self._noteCreation(QStyleOptionFocusRect, lambda: Rituals.call(
        'ritual_ZN21QStyleOptionFocusRectC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionFocusRect) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionFocusRect::QStyleOptionFocusRect(const QStyleOptionFocusRect
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionfocusrect.html#QStyleOptionFocusRect

    Parameters
    ----------

    other : QStyleOptionFocusRect
      Passed on as a value: Qt reads the C++ QStyleOptionFocusRect, which
      stays Python's own.
    """
    #  QStyleOptionFocusRect::QStyleOptionFocusRect(const
    #      QStyleOptionFocusRect &other)
    self._noteCreation(QStyleOptionFocusRect, lambda: Rituals.call(
        'ritual_ZN21QStyleOptionFocusRectC1ERKS_', self._valueOf(other),
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
