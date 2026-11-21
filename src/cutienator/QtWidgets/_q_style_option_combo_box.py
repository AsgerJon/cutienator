"""
QStyleOptionComboBox binding of the Qt C++
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
from . import QStyleOptionComboBoxStyleOptionType
from . import QStyleOptionComboBoxStyleOptionVersion, QStyleOptionComplex


class QStyleOptionComboBox(QStyleOptionComplex):
  """
  The cute side of Qt's QStyleOptionComboBox: a plain Python object standing
  in front of one C++ QStyleOptionComboBox.

  It is built on the cute 'QStyleOptionComplex', as Qt's QStyleOptionComboBox
  is built on Qt's QStyleOptionComplex, and has everything that class has.

  C++ hands a QStyleOptionComboBox around as a copy, so every C++
  QStyleOptionComboBox behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionComboBox yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionComboBox::~QStyleOptionComboBox()': the destructor:
    Python removes its C++ QStyleOptionComboBox by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionComboBox is created at the first use, not by
    'QStyleOptionComboBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionComboBox back gives a copy the ritual
    made for Python, in a new cute QStyleOptionComboBox.
  """

  #  The enums Qt writes inside QStyleOptionComboBox, and the names Qt has
  #  for the combinations of its flags enums.
  StyleOptionType = QStyleOptionComboBoxStyleOptionType
  StyleOptionVersion = QStyleOptionComboBoxStyleOptionVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionComboBox'

  #  Qt's '~QStyleOptionComboBox()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionComboBox behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QStyleOptionComboBoxD1Ev'

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
    'QStyleOptionComboBox::QStyleOptionComboBox()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptioncombobox.html#QStyleOptionComboBox
    """
    #  QStyleOptionComboBox::QStyleOptionComboBox()
    self._noteCreation(QStyleOptionComboBox, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionComboBoxC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionComboBox) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionComboBox::QStyleOptionComboBox(const QStyleOptionComboBox
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptioncombobox.html#QStyleOptionComboBox

    Parameters
    ----------

    other : QStyleOptionComboBox
      Passed on as a value: Qt reads the C++ QStyleOptionComboBox, which
      stays Python's own.
    """
    #  QStyleOptionComboBox::QStyleOptionComboBox(const QStyleOptionComboBox
    #      &other)
    self._noteCreation(QStyleOptionComboBox, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionComboBoxC1ERKS_', self._valueOf(other),
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
