"""
QQmlRectFValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlRectFValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QRectF

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']


class QQmlRectFValueType(QRectF):
  """
  The cute side of Qt's QQmlRectFValueType: a plain Python object standing in
  front of one C++ QQmlRectFValueType.

  It is built on the cute 'QRectF', as Qt's QQmlRectFValueType is built on
  Qt's QRectF, and has everything that class has.

  C++ hands a QQmlRectFValueType around as a copy, so every C++
  QQmlRectFValueType behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlRectFValueType that has a ritual and that Python
  can call so far, 13 names in all: 'toString', 'x', 'y', 'setX', 'setY',
  'width', 'height', 'setWidth', 'setHeight', 'left', 'right', 'top',
  'bottom'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlRectFValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlRectFValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQmlRectFValueType::~QQmlRectFValueType()': the destructor: Python
    removes its C++ QQmlRectFValueType by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlRectFValueType is created at the first use, not by
    'QQmlRectFValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlRectFValueType back gives a copy the ritual made
    for Python, in a new cute QQmlRectFValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlRectFValueType'

  #  Qt's '~QQmlRectFValueType()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlRectFValueType behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlRectFValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlRectFValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlRectFValueType::toString() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType8toStringEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#x
    """
    #  qreal QQmlRectFValueType::x() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#y
    """
    #  qreal QQmlRectFValueType::y() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType1yEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#width
    """
    #  qreal QQmlRectFValueType::width() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#height
    """
    #  qreal QQmlRectFValueType::height() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType6heightEv')

  def left(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#left
    """
    #  qreal QQmlRectFValueType::left() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType4leftEv')

  def right(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#right
    """
    #  qreal QQmlRectFValueType::right() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType5rightEv')

  def top(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#top
    """
    #  qreal QQmlRectFValueType::top() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType3topEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'qreal QQmlRectFValueType::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#bottom
    """
    #  qreal QQmlRectFValueType::bottom() const
    return self.uglySide.call('ritual_ZNK18QQmlRectFValueType6bottomEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlRectFValueType::setX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlRectFValueType::setX(qreal a0)
    self.uglySide.call('ritual_ZN18QQmlRectFValueType4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlRectFValueType::setY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlRectFValueType::setY(qreal a0)
    self.uglySide.call('ritual_ZN18QQmlRectFValueType4setYEd', a0)

  @overload(float)
  def setWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlRectFValueType::setWidth(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#setWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlRectFValueType::setWidth(qreal a0)
    self.uglySide.call('ritual_ZN18QQmlRectFValueType8setWidthEd', a0)

  @overload(float)
  def setHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlRectFValueType::setHeight(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#setHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlRectFValueType::setHeight(qreal a0)
    self.uglySide.call('ritual_ZN18QQmlRectFValueType9setHeightEd', a0)

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
    'QQmlRectFValueType::QQmlRectFValueType()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#QQmlRectFValueType
    """
    #  QQmlRectFValueType::QQmlRectFValueType()
    self._noteCreation(QQmlRectFValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlRectFValueTypeC1Ev',
    ))

  @overload(QRectF)
  def __init__(self, rect: QRectF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlRectFValueType::QQmlRectFValueType(const QRectF &rect)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#QQmlRectFValueType

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QQmlRectFValueType::QQmlRectFValueType(const QRectF &rect)
    self._noteCreation(QQmlRectFValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlRectFValueTypeC1ERK6QRectF', self._valueOf(rect),
    ))

  @overload(QRect)
  def __init__(self, rect: QRect) -> None:
    """
    Notes what was given, for Qt's
    'QQmlRectFValueType::QQmlRectFValueType(const QRect &rect)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrectfvaluetype.html#QQmlRectFValueType

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QQmlRectFValueType::QQmlRectFValueType(const QRect &rect)
    self._noteCreation(QQmlRectFValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlRectFValueTypeC1ERK5QRect', self._valueOf(rect),
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
