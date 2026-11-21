"""
QStyleOptionSlider binding of the Qt C++
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
from . import QStyleOptionComplex, QStyleOptionSliderStyleOptionType
from . import QStyleOptionSliderStyleOptionVersion


class QStyleOptionSlider(QStyleOptionComplex):
  """
  The cute side of Qt's QStyleOptionSlider: a plain Python object standing in
  front of one C++ QStyleOptionSlider.

  It is built on the cute 'QStyleOptionComplex', as Qt's QStyleOptionSlider
  is built on Qt's QStyleOptionComplex, and has everything that class has.

  C++ hands a QStyleOptionSlider around as a copy, so every C++
  QStyleOptionSlider behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionSlider yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionSlider::~QStyleOptionSlider()': the destructor: Python
    removes its C++ QStyleOptionSlider by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionSlider is created at the first use, not by
    'QStyleOptionSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionSlider back gives a copy the ritual made
    for Python, in a new cute QStyleOptionSlider.
  """

  #  The enums Qt writes inside QStyleOptionSlider, and the names Qt has for
  #  the combinations of its flags enums.
  StyleOptionType = QStyleOptionSliderStyleOptionType
  StyleOptionVersion = QStyleOptionSliderStyleOptionVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionSlider'

  #  Qt's '~QStyleOptionSlider()'. Naming it makes this a value class: Python
  #  owns every C++ QStyleOptionSlider behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QStyleOptionSliderD1Ev'

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
    'QStyleOptionSlider::QStyleOptionSlider()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionslider.html#QStyleOptionSlider
    """
    #  QStyleOptionSlider::QStyleOptionSlider()
    self._noteCreation(QStyleOptionSlider, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionSliderC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionSlider) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionSlider::QStyleOptionSlider(const QStyleOptionSlider
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionslider.html#QStyleOptionSlider

    Parameters
    ----------

    other : QStyleOptionSlider
      Passed on as a value: Qt reads the C++ QStyleOptionSlider, which stays
      Python's own.
    """
    #  QStyleOptionSlider::QStyleOptionSlider(const QStyleOptionSlider
    #      &other)
    self._noteCreation(QStyleOptionSlider, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionSliderC1ERKS_', self._valueOf(other),
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
