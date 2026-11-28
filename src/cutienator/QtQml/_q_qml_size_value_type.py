"""
QQmlSizeValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlSizeValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSize

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']


class QQmlSizeValueType(QSize):
  """
  The cute side of Qt's QQmlSizeValueType: a plain Python object standing in
  front of one C++ QQmlSizeValueType.

  It is built on the cute 'QSize', as Qt's QQmlSizeValueType is built on Qt's
  QSize, and has everything that class has.

  C++ hands a QQmlSizeValueType around as a copy, so every C++
  QQmlSizeValueType behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSizeValueType that has a ritual and that Python
  can call so far, 5 names in all: 'toString', 'width', 'height', 'setWidth',
  'setHeight'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlSizeValueType::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlSizeValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlSizeValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'QQmlSizeValueType::~QQmlSizeValueType()': the destructor: Python
    removes its C++ QQmlSizeValueType by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlSizeValueType is created at the first use, not by
    'QQmlSizeValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSizeValueType back gives a copy the ritual made
    for Python, in a new cute QQmlSizeValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSizeValueType'

  #  Qt's '~QQmlSizeValueType()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSizeValueType behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQmlSizeValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlSizeValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizevaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSizeValueType::toString() const
    return self.uglySide.call('ritual_ZNK17QQmlSizeValueType8toStringEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QQmlSizeValueType::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizevaluetype.html#width
    """
    #  int QQmlSizeValueType::width() const
    return self.uglySide.call('ritual_ZNK17QQmlSizeValueType5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QQmlSizeValueType::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizevaluetype.html#height
    """
    #  int QQmlSizeValueType::height() const
    return self.uglySide.call('ritual_ZNK17QQmlSizeValueType6heightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWidth(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlSizeValueType::setWidth(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizevaluetype.html#setWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlSizeValueType::setWidth(int a0)
    self.uglySide.call('ritual_ZN17QQmlSizeValueType8setWidthEi', a0)

  @overload(int)
  def setHeight(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlSizeValueType::setHeight(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsizevaluetype.html#setHeight

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlSizeValueType::setHeight(int a0)
    self.uglySide.call('ritual_ZN17QQmlSizeValueType9setHeightEi', a0)

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
    Notes what was given, for Qt's 'QQmlSizeValueType::QQmlSizeValueType()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsizevaluetype.html#QQmlSizeValueType
    """
    #  QQmlSizeValueType::QQmlSizeValueType()
    self._noteCreation(QQmlSizeValueType, lambda: Rituals.call(
        'ritual_ZN17QQmlSizeValueTypeC1Ev',
    ))

  @overload(QSize)
  def __init__(self, size: QSize) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSizeValueType::QQmlSizeValueType(const QSize &size)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsizevaluetype.html#QQmlSizeValueType

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QQmlSizeValueType::QQmlSizeValueType(const QSize &size)
    self._noteCreation(QQmlSizeValueType, lambda: Rituals.call(
        'ritual_ZN17QQmlSizeValueTypeC1ERK5QSize', self._valueOf(size),
    ))

  @overload(QSizeF)
  def __init__(self, size: QSizeF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSizeValueType::QQmlSizeValueType(const QSizeF &size)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsizevaluetype.html#QQmlSizeValueType

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  QQmlSizeValueType::QQmlSizeValueType(const QSizeF &size)
    self._noteCreation(QQmlSizeValueType, lambda: Rituals.call(
        'ritual_ZN17QQmlSizeValueTypeC1ERK6QSizeF', self._valueOf(size),
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
