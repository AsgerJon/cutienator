"""
QDateTimeAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qdatetimeaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDateTimeAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractAxisPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QDateTimeAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QDateTimeAxisPrivate(QAbstractAxisPrivate):
  """
  The cute side of Qt's QDateTimeAxisPrivate: a plain Python object standing
  in front of one C++ QDateTimeAxisPrivate.

  It is built on the cute 'QAbstractAxisPrivate', as Qt's
  QDateTimeAxisPrivate is built on Qt's QAbstractAxisPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDateTimeAxisPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'setMin', 'setMax', 'setRange',
  'min', 'max', 'calculateVisualRange', 'q_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTimeAxisPrivate::~QDateTimeAxisPrivate()': the destructor:
    Python never removes a C++ QDateTimeAxisPrivate.
  - Qt's 'const QDateTimeAxis *QDateTimeAxisPrivate::q_func() const': takes
    in Python what 'QDateTimeAxis *QDateTimeAxisPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QDateTimeAxisPrivate is created at the first use, not by
    'QDateTimeAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDateTimeAxisPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTimeAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QDateTimeAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDateTimeAxisPrivate'

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

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QDateTimeAxisPrivate::setMin(const QVariant &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDateTimeAxisPrivate::setMin(const QVariant &min)
    ritual = 'ritual_ZN20QDateTimeAxisPrivate6setMinERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeAxisPrivate6setMinERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(min))

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QDateTimeAxisPrivate::setMax(const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDateTimeAxisPrivate::setMax(const QVariant &max)
    ritual = 'ritual_ZN20QDateTimeAxisPrivate6setMaxERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeAxisPrivate6setMaxERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(max))

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QDateTimeAxisPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDateTimeAxisPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    ritual = 'ritual_ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_'
    self.uglySide.call(ritual, self._valueOf(min), self._valueOf(max))

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QDateTimeAxisPrivate::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
    ritual = 'ritual_ZN20QDateTimeAxisPrivate8setRangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeAxisPrivate8setRangeEdd'
    self.uglySide.call(ritual, min, max)

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
    'QDateTimeAxisPrivate::QDateTimeAxisPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#QDateTimeAxisPrivate
    """
    #  QDateTimeAxisPrivate::QDateTimeAxisPrivate()
    self._noteCreation(QDateTimeAxisPrivate, lambda: Rituals.call(
        'ritual_ZN20QDateTimeAxisPrivateC1Ev',
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

  def min(self) -> float:
    """
    Calls Qt's 'qreal QDateTimeAxisPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#min
    """
    #  qreal QDateTimeAxisPrivate::min()
    ritual = 'ritual_ZN20QDateTimeAxisPrivate3minEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeAxisPrivate3minEv'
    return self.uglySide.call(ritual)

  def max(self) -> float:
    """
    Calls Qt's 'qreal QDateTimeAxisPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#max
    """
    #  qreal QDateTimeAxisPrivate::max()
    ritual = 'ritual_ZN20QDateTimeAxisPrivate3maxEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeAxisPrivate3maxEv'
    return self.uglySide.call(ritual)

  def calculateVisualRange(self) -> None:
    """
    Calls Qt's 'void QDateTimeAxisPrivate::calculateVisualRange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#calculateVisualRange
    """
    #  void QDateTimeAxisPrivate::calculateVisualRange()
    self.uglySide.call(
        'ritual_ZN20QDateTimeAxisPrivate20calculateVisualRangeEv',
    )

  def q_func(self) -> Optional[QDateTimeAxis]:
    """
    Calls Qt's 'QDateTimeAxis *QDateTimeAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxisprivate.html#q_func

    Returns
    -------

    Optional[QDateTimeAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDateTimeAxis *QDateTimeAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QDateTimeAxisPrivate6q_funcEv')
    from . import QDateTimeAxis
    return QDateTimeAxis._cuteAt(address)
