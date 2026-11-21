"""
QStyleOptionToolButton binding of the Qt C++
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
from . import QStyleOptionComplex, QStyleOptionToolButtonStyleOptionType
from . import QStyleOptionToolButtonStyleOptionVersion
from . import QStyleOptionToolButtonToolButtonFeature


class QStyleOptionToolButton(QStyleOptionComplex):
  """
  The cute side of Qt's QStyleOptionToolButton: a plain Python object
  standing in front of one C++ QStyleOptionToolButton.

  It is built on the cute 'QStyleOptionComplex', as Qt's
  QStyleOptionToolButton is built on Qt's QStyleOptionComplex, and has
  everything that class has.

  C++ hands a QStyleOptionToolButton around as a copy, so every C++
  QStyleOptionToolButton behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionToolButton yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionToolButton::~QStyleOptionToolButton()': the destructor:
    Python removes its C++ QStyleOptionToolButton by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionToolButton is created at the first use, not by
    'QStyleOptionToolButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionToolButton back gives a copy the ritual
    made for Python, in a new cute QStyleOptionToolButton.
  """

  #  The enums Qt writes inside QStyleOptionToolButton, and the names Qt has
  #  for the combinations of its flags enums.
  StyleOptionType = QStyleOptionToolButtonStyleOptionType
  StyleOptionVersion = QStyleOptionToolButtonStyleOptionVersion
  ToolButtonFeature = QStyleOptionToolButtonToolButtonFeature
  ToolButtonFeatures = QStyleOptionToolButtonToolButtonFeature

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionToolButton'

  #  Qt's '~QStyleOptionToolButton()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionToolButton behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QStyleOptionToolButtonD1Ev'

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
    'QStyleOptionToolButton::QStyleOptionToolButton()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbutton.html#QStyleOptionToolButton
    """
    #  QStyleOptionToolButton::QStyleOptionToolButton()
    self._noteCreation(QStyleOptionToolButton, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionToolButtonC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionToolButton) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionToolButton::QStyleOptionToolButton(const
    QStyleOptionToolButton &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontoolbutton.html#QStyleOptionToolButton

    Parameters
    ----------

    other : QStyleOptionToolButton
      Passed on as a value: Qt reads the C++ QStyleOptionToolButton, which
      stays Python's own.
    """
    #  QStyleOptionToolButton::QStyleOptionToolButton(const
    #      QStyleOptionToolButton &other)
    self._noteCreation(QStyleOptionToolButton, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionToolButtonC1ERKS_', self._valueOf(other),
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
