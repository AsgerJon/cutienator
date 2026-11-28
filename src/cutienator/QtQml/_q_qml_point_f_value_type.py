"""
QQmlPointFValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlPointFValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QPointF

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QQmlPointFValueType(QPointF):
  """
  The cute side of Qt's QQmlPointFValueType: a plain Python object standing
  in front of one C++ QQmlPointFValueType.

  It is built on the cute 'QPointF', as Qt's QQmlPointFValueType is built on
  Qt's QPointF, and has everything that class has.

  C++ hands a QQmlPointFValueType around as a copy, so every C++
  QQmlPointFValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPointFValueType that has a ritual and that
  Python can call so far, 5 names in all: 'toString', 'x', 'y', 'setX',
  'setY'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlPointFValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlPointFValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQmlPointFValueType::~QQmlPointFValueType()': the destructor:
    Python removes its C++ QQmlPointFValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlPointFValueType is created at the first use, not by
    'QQmlPointFValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPointFValueType back gives a copy the ritual made
    for Python, in a new cute QQmlPointFValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPointFValueType'

  #  Qt's '~QQmlPointFValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlPointFValueType behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlPointFValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlPointFValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPointFValueType::toString() const
    return self.uglySide.call('ritual_ZNK19QQmlPointFValueType8toStringEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQmlPointFValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#x
    """
    #  qreal QQmlPointFValueType::x() const
    return self.uglySide.call('ritual_ZNK19QQmlPointFValueType1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQmlPointFValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#y
    """
    #  qreal QQmlPointFValueType::y() const
    return self.uglySide.call('ritual_ZNK19QQmlPointFValueType1yEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlPointFValueType::setX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlPointFValueType::setX(qreal a0)
    self.uglySide.call('ritual_ZN19QQmlPointFValueType4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlPointFValueType::setY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlPointFValueType::setY(qreal a0)
    self.uglySide.call('ritual_ZN19QQmlPointFValueType4setYEd', a0)

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
    'QQmlPointFValueType::QQmlPointFValueType()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#QQmlPointFValueType
    """
    #  QQmlPointFValueType::QQmlPointFValueType()
    self._noteCreation(QQmlPointFValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlPointFValueTypeC1Ev',
    ))

  @overload(QPointF)
  def __init__(self, point: QPointF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPointFValueType::QQmlPointFValueType(const QPointF &point)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#QQmlPointFValueType

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QQmlPointFValueType::QQmlPointFValueType(const QPointF &point)
    self._noteCreation(QQmlPointFValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlPointFValueTypeC1ERK7QPointF',
        self._valueOf(point, 'QPointF'),
    ))

  @overload(QPoint)
  def __init__(self, point: QPoint) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPointFValueType::QQmlPointFValueType(const QPoint &point)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpointfvaluetype.html#QQmlPointFValueType

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QQmlPointFValueType::QQmlPointFValueType(const QPoint &point)
    self._noteCreation(QQmlPointFValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlPointFValueTypeC1ERK6QPoint', self._valueOf(point),
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
