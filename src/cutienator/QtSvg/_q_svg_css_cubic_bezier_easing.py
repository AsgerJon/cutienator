"""
QSvgCssCubicBezierEasing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgCssCubicBezierEasing to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgCssValues, QSvgCssEasing

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QSvgCssCubicBezierEasing(QSvgCssEasing):
  """
  The cute side of Qt's QSvgCssCubicBezierEasing: a plain Python object
  standing in front of one C++ QSvgCssCubicBezierEasing.

  It is built on the cute 'QSvgCssEasing', as Qt's QSvgCssCubicBezierEasing
  is built on Qt's QSvgCssEasing, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgCssCubicBezierEasing that has a ritual and that
  Python can call so far, 3 names in all: 'progress', 'c1', 'c2'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgCssCubicBezierEasing::~QSvgCssCubicBezierEasing()': the
    destructor: Python never removes a C++ QSvgCssCubicBezierEasing.

  What to expect
  --------------

  - The C++ QSvgCssCubicBezierEasing is created at the first use, not by
    'QSvgCssCubicBezierEasing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgCssCubicBezierEasing.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgCssCubicBezierEasing'

  #  A C++ QSvgCssCubicBezierEasing Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgCssCubicBezierEasing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def progress(self, t: float) -> float:
    """
    Calls Qt's 'qreal QSvgCssCubicBezierEasing::progress(qreal t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcsscubicbeziereasing.html#progress

    Parameters
    ----------

    t : float
      Passed on as it is.
    """
    #  qreal QSvgCssCubicBezierEasing::progress(qreal t) const
    ritual = 'ritual_ZNK24QSvgCssCubicBezierEasing8progressEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSvgCssCubicBezierEasing8progressEd'
    return self.uglySide.call(ritual, t)

  def c1(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgCssCubicBezierEasing::c1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcsscubicbeziereasing.html#c1

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgCssCubicBezierEasing::c1() const
    address = self.uglySide.call('ritual_ZNK24QSvgCssCubicBezierEasing2c1Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def c2(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgCssCubicBezierEasing::c2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcsscubicbeziereasing.html#c2

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgCssCubicBezierEasing::c2() const
    address = self.uglySide.call('ritual_ZNK24QSvgCssCubicBezierEasing2c2Ev')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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

  @overload(QSvgCssValues.EasingFunction, QPointF, QPointF)
  def __init__(
      self,
      easingFunction: QSvgCssValues.EasingFunction,
      c1: QPointF,
      c2: QPointF,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSvgCssCubicBezierEasing::QSvgCssCubicBezierEasing(QSvgCssValues::
    EasingFunction easingFunction, QPointF c1, QPointF c2)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcsscubicbeziereasing.html

    Parameters
    ----------

    easingFunction : QSvgCssValues.EasingFunction
      Passed on as its number.

    c1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    c2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QSvgCssCubicBezierEasing::QSvgCssCubicBezierEasing(
    #      QSvgCssValues::EasingFunction easingFunction, QPointF c1, QPointF
    #      c2)
    self._noteCreation(QSvgCssCubicBezierEasing, lambda: Rituals.call(
        'ritual_ZN24QSvgCssCubicBezierEasingC1EN13QSvgCssValues14EasingFunc'
        'tionE7QPointFS2_',
        easingFunction.value, self._valueOf(c1, 'QPointF'), self._valueOf(c2,
        'QPointF'),
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
