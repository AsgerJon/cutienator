"""
QQmlPointValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlPointValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QPoint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QQmlPointValueType(QPoint):
  """
  The cute side of Qt's QQmlPointValueType: a plain Python object standing in
  front of one C++ QQmlPointValueType.

  It is built on the cute 'QPoint', as Qt's QQmlPointValueType is built on
  Qt's QPoint, and has everything that class has.

  C++ hands a QQmlPointValueType around as a copy, so every C++
  QQmlPointValueType behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPointValueType that has a ritual and that Python
  can call so far, 5 names in all: 'toString', 'x', 'y', 'setX', 'setY'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlPointValueType::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlPointValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlPointValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQmlPointValueType::~QQmlPointValueType()': the destructor: Python
    removes its C++ QQmlPointValueType by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlPointValueType is created at the first use, not by
    'QQmlPointValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPointValueType back gives a copy the ritual made
    for Python, in a new cute QQmlPointValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPointValueType'

  #  Qt's '~QQmlPointValueType()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlPointValueType behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlPointValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlPointValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPointValueType::toString() const
    return self.uglySide.call('ritual_ZNK18QQmlPointValueType8toStringEv')

  def x(self) -> int:
    """
    Calls Qt's 'int QQmlPointValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointvaluetype.html#x
    """
    #  int QQmlPointValueType::x() const
    return self.uglySide.call('ritual_ZNK18QQmlPointValueType1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QQmlPointValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointvaluetype.html#y
    """
    #  int QQmlPointValueType::y() const
    return self.uglySide.call('ritual_ZNK18QQmlPointValueType1yEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setX(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlPointValueType::setX(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointvaluetype.html#setX

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlPointValueType::setX(int a0)
    self.uglySide.call('ritual_ZN18QQmlPointValueType4setXEi', a0)

  @overload(int)
  def setY(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlPointValueType::setY(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpointvaluetype.html#setY

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlPointValueType::setY(int a0)
    self.uglySide.call('ritual_ZN18QQmlPointValueType4setYEi', a0)

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
    'QQmlPointValueType::QQmlPointValueType()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpointvaluetype.html#QQmlPointValueType
    """
    #  QQmlPointValueType::QQmlPointValueType()
    self._noteCreation(QQmlPointValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlPointValueTypeC1Ev',
    ))

  @overload(QPoint)
  def __init__(self, point: QPoint) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPointValueType::QQmlPointValueType(const QPoint &point)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpointvaluetype.html#QQmlPointValueType

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QQmlPointValueType::QQmlPointValueType(const QPoint &point)
    self._noteCreation(QQmlPointValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlPointValueTypeC1ERK6QPoint', self._valueOf(point),
    ))

  @overload(QPointF)
  def __init__(self, point: QPointF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPointValueType::QQmlPointValueType(const QPointF &point)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpointvaluetype.html#QQmlPointValueType

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QQmlPointValueType::QQmlPointValueType(const QPointF &point)
    self._noteCreation(QQmlPointValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlPointValueTypeC1ERK7QPointF',
        self._valueOf(point, 'QPointF'),
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
