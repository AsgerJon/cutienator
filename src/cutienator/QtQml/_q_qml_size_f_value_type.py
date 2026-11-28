"""
QQmlSizeFValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlSizeFValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSizeF

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QQmlSizeFValueType(QSizeF):
  """
  The cute side of Qt's QQmlSizeFValueType: a plain Python object standing in
  front of one C++ QQmlSizeFValueType.

  It is built on the cute 'QSizeF', as Qt's QQmlSizeFValueType is built on
  Qt's QSizeF, and has everything that class has.

  C++ hands a QQmlSizeFValueType around as a copy, so every C++
  QQmlSizeFValueType behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSizeFValueType that has a ritual and that Python
  can call so far, 5 names in all: 'toString', 'width', 'height', 'setWidth',
  'setHeight'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlSizeFValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlSizeFValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQmlSizeFValueType::~QQmlSizeFValueType()': the destructor: Python
    removes its C++ QQmlSizeFValueType by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlSizeFValueType is created at the first use, not by
    'QQmlSizeFValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSizeFValueType back gives a copy the ritual made
    for Python, in a new cute QQmlSizeFValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSizeFValueType'

  #  Qt's '~QQmlSizeFValueType()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSizeFValueType behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlSizeFValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlSizeFValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSizeFValueType::toString() const
    return self.uglySide.call('ritual_ZNK18QQmlSizeFValueType8toStringEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQmlSizeFValueType::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#width
    """
    #  qreal QQmlSizeFValueType::width() const
    return self.uglySide.call('ritual_ZNK18QQmlSizeFValueType5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQmlSizeFValueType::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#height
    """
    #  qreal QQmlSizeFValueType::height() const
    return self.uglySide.call('ritual_ZNK18QQmlSizeFValueType6heightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlSizeFValueType::setWidth(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#setWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlSizeFValueType::setWidth(qreal a0)
    self.uglySide.call('ritual_ZN18QQmlSizeFValueType8setWidthEd', a0)

  @overload(float)
  def setHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlSizeFValueType::setHeight(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#setHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlSizeFValueType::setHeight(qreal a0)
    self.uglySide.call('ritual_ZN18QQmlSizeFValueType9setHeightEd', a0)

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
    'QQmlSizeFValueType::QQmlSizeFValueType()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#QQmlSizeFValueType
    """
    #  QQmlSizeFValueType::QQmlSizeFValueType()
    self._noteCreation(QQmlSizeFValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlSizeFValueTypeC1Ev',
    ))

  @overload(QSizeF)
  def __init__(self, size: QSizeF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSizeFValueType::QQmlSizeFValueType(const QSizeF &size)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#QQmlSizeFValueType

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  QQmlSizeFValueType::QQmlSizeFValueType(const QSizeF &size)
    self._noteCreation(QQmlSizeFValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlSizeFValueTypeC1ERK6QSizeF', self._valueOf(size),
    ))

  @overload(QSize)
  def __init__(self, size: QSize) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSizeFValueType::QQmlSizeFValueType(const QSize &size)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsizefvaluetype.html#QQmlSizeFValueType

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QQmlSizeFValueType::QQmlSizeFValueType(const QSize &size)
    self._noteCreation(QQmlSizeFValueType, lambda: Rituals.call(
        'ritual_ZN18QQmlSizeFValueTypeC1ERK5QSize', self._valueOf(size),
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
