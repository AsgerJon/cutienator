"""
QSvgCssEasing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgCssEasing to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSvgCssValues, QSvgEasingInterface


class QSvgCssEasing(QSvgEasingInterface):
  """
  The cute side of Qt's QSvgCssEasing: a plain Python object standing in
  front of one C++ QSvgCssEasing.

  It is built on the cute 'QSvgEasingInterface', as Qt's QSvgCssEasing is
  built on Qt's QSvgEasingInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgCssEasing that has a ritual and that Python can
  call so far, 1 name in all: 'easingFunction'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgCssEasing::~QSvgCssEasing()': the destructor: Python never
    removes a C++ QSvgCssEasing.

  What to expect
  --------------

  - The C++ QSvgCssEasing is created at the first use, not by
    'QSvgCssEasing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgCssEasing.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgCssEasing'

  #  A C++ QSvgCssEasing Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgCssEasing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def easingFunction(self) -> QSvgCssValues.EasingFunction:
    """
    Calls Qt's 'QSvgCssValues::EasingFunction QSvgCssEasing::easingFunction()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcsseasing.html#easingFunction

    Returns
    -------

    QSvgCssValues.EasingFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgCssValues.EasingFunction(number)' gives.
    """
    #  QSvgCssValues::EasingFunction QSvgCssEasing::easingFunction() const
    return QSvgCssValues.EasingFunction(self.uglySide.call(
        'ritual_ZNK13QSvgCssEasing14easingFunctionEv',
    ))

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

  @overload(QSvgCssValues.EasingFunction)
  def __init__(self, easingFunction: QSvgCssValues.EasingFunction) -> None:
    """
    Notes what was given, for Qt's
    'QSvgCssEasing::QSvgCssEasing(QSvgCssValues::EasingFunction
    easingFunction)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcsseasing.html#QSvgCssEasing

    Parameters
    ----------

    easingFunction : QSvgCssValues.EasingFunction
      Passed on as its number.
    """
    #  QSvgCssEasing::QSvgCssEasing(QSvgCssValues::EasingFunction
    #      easingFunction)
    self._noteCreation(QSvgCssEasing, lambda: Rituals.call(
        'ritual_ZN13QSvgCssEasingC1EN13QSvgCssValues14EasingFunctionE',
        easingFunction.value,
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
