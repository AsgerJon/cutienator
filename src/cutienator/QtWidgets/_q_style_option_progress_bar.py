"""
QStyleOptionProgressBar binding of the Qt C++
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
from . import QStyleOption, QStyleOptionProgressBarStyleOptionType
from . import QStyleOptionProgressBarStyleOptionVersion


class QStyleOptionProgressBar(QStyleOption):
  """
  The cute side of Qt's QStyleOptionProgressBar: a plain Python object
  standing in front of one C++ QStyleOptionProgressBar.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionProgressBar is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionProgressBar around as a copy, so every C++
  QStyleOptionProgressBar behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionProgressBar yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionProgressBar::~QStyleOptionProgressBar()': the
    destructor: Python removes its C++ QStyleOptionProgressBar by it, and has
    no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionProgressBar is created at the first use, not by
    'QStyleOptionProgressBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionProgressBar back gives a copy the ritual
    made for Python, in a new cute QStyleOptionProgressBar.
  """

  #  The enums Qt writes inside QStyleOptionProgressBar, and the names Qt has
  #  for the combinations of its flags enums.
  StyleOptionType = QStyleOptionProgressBarStyleOptionType
  StyleOptionVersion = QStyleOptionProgressBarStyleOptionVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionProgressBar'

  #  Qt's '~QStyleOptionProgressBar()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionProgressBar behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QStyleOptionProgressBarD1Ev'

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
    'QStyleOptionProgressBar::QStyleOptionProgressBar()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionprogressbar.html
    """
    #  QStyleOptionProgressBar::QStyleOptionProgressBar()
    self._noteCreation(QStyleOptionProgressBar, lambda: Rituals.call(
        'ritual_ZN23QStyleOptionProgressBarC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionProgressBar) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionProgressBar::QStyleOptionProgressBar(const
    QStyleOptionProgressBar &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionprogressbar.html

    Parameters
    ----------

    other : QStyleOptionProgressBar
      Passed on as a value: Qt reads the C++ QStyleOptionProgressBar, which
      stays Python's own.
    """
    #  QStyleOptionProgressBar::QStyleOptionProgressBar(const
    #      QStyleOptionProgressBar &other)
    self._noteCreation(QStyleOptionProgressBar, lambda: Rituals.call(
        'ritual_ZN23QStyleOptionProgressBarC1ERKS_', self._valueOf(other),
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
