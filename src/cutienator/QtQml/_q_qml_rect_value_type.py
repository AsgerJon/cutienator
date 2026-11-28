"""
QQmlRectValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlRectValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QRect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QQmlRectValueType(QRect):
  """
  The cute side of Qt's QQmlRectValueType: a plain Python object standing in
  front of one C++ QQmlRectValueType.

  It is built on the cute 'QRect', as Qt's QQmlRectValueType is built on Qt's
  QRect, and has everything that class has.

  C++ hands a QQmlRectValueType around as a copy, so every C++
  QQmlRectValueType behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlRectValueType that has a ritual and that Python
  can call so far, 13 names in all: 'toString', 'x', 'y', 'setX', 'setY',
  'width', 'height', 'setWidth', 'setHeight', 'left', 'right', 'top',
  'bottom'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlRectValueType::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlRectValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlRectValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQmlRectValueType::~QQmlRectValueType()': the destructor: Python
    removes its C++ QQmlRectValueType by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlRectValueType is created at the first use, not by
    'QQmlRectValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlRectValueType back gives a copy the ritual made
    for Python, in a new cute QQmlRectValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlRectValueType'

  #  Qt's '~QQmlRectValueType()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlRectValueType behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQmlRectValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlRectValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlRectValueType::toString() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType8toStringEv')

  def x(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#x
    """
    #  int QQmlRectValueType::x() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#y
    """
    #  int QQmlRectValueType::y() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType1yEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#width
    """
    #  int QQmlRectValueType::width() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#height
    """
    #  int QQmlRectValueType::height() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType6heightEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#left
    """
    #  int QQmlRectValueType::left() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType4leftEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#right
    """
    #  int QQmlRectValueType::right() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType5rightEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#top
    """
    #  int QQmlRectValueType::top() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType3topEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QQmlRectValueType::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#bottom
    """
    #  int QQmlRectValueType::bottom() const
    return self.uglySide.call('ritual_ZNK17QQmlRectValueType6bottomEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setX(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlRectValueType::setX(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#setX

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlRectValueType::setX(int a0)
    self.uglySide.call('ritual_ZN17QQmlRectValueType4setXEi', a0)

  @overload(int)
  def setY(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlRectValueType::setY(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#setY

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlRectValueType::setY(int a0)
    self.uglySide.call('ritual_ZN17QQmlRectValueType4setYEi', a0)

  @overload(int)
  def setWidth(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlRectValueType::setWidth(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#setWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlRectValueType::setWidth(int a0)
    self.uglySide.call('ritual_ZN17QQmlRectValueType8setWidthEi', a0)

  @overload(int)
  def setHeight(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlRectValueType::setHeight(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlrectvaluetype.html#setHeight

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlRectValueType::setHeight(int a0)
    self.uglySide.call('ritual_ZN17QQmlRectValueType9setHeightEi', a0)

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
    Notes what was given, for Qt's 'QQmlRectValueType::QQmlRectValueType()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrectvaluetype.html#QQmlRectValueType
    """
    #  QQmlRectValueType::QQmlRectValueType()
    self._noteCreation(QQmlRectValueType, lambda: Rituals.call(
        'ritual_ZN17QQmlRectValueTypeC1Ev',
    ))

  @overload(QRect)
  def __init__(self, rect: QRect) -> None:
    """
    Notes what was given, for Qt's
    'QQmlRectValueType::QQmlRectValueType(const QRect &rect)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrectvaluetype.html#QQmlRectValueType

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QQmlRectValueType::QQmlRectValueType(const QRect &rect)
    self._noteCreation(QQmlRectValueType, lambda: Rituals.call(
        'ritual_ZN17QQmlRectValueTypeC1ERK5QRect', self._valueOf(rect),
    ))

  @overload(QRectF)
  def __init__(self, rect: QRectF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlRectValueType::QQmlRectValueType(const QRectF &rect)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlrectvaluetype.html#QQmlRectValueType

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QQmlRectValueType::QQmlRectValueType(const QRectF &rect)
    self._noteCreation(QQmlRectValueType, lambda: Rituals.call(
        'ritual_ZN17QQmlRectValueTypeC1ERK6QRectF', self._valueOf(rect),
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
