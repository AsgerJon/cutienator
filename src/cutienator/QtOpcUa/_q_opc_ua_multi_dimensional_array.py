"""
QOpcUaMultiDimensionalArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuamultidimensionalarray.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QOpcUaMultiDimensionalArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaMultiDimensionalArray: a plain Python object
  standing in front of one C++ QOpcUaMultiDimensionalArray.

  C++ hands a QOpcUaMultiDimensionalArray around as a copy, so every C++
  QOpcUaMultiDimensionalArray behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaMultiDimensionalArray that has a ritual and
  that Python can call so far, 4 names in all: 'valueArray', 'setValueArray',
  'isValid', '__eq__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaMultiDimensionalArray
    &QOpcUaMultiDimensionalArray::operator=(const QOpcUaMultiDimensionalArray
    &rhs)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
    QVariantList &valueArray, const QList<quint32> &arrayDimensions)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
    QList<quint32> &arrayDimensions)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QOpcUaMultiDimensionalArray::~QOpcUaMultiDimensionalArray()': the
    destructor: Python removes its C++ QOpcUaMultiDimensionalArray by it, and
    has no other use for it.
  - Qt's 'QVariantList &QOpcUaMultiDimensionalArray::valueArrayRef()': gives
    a type Python has no way to take yet.
  - Qt's 'int QOpcUaMultiDimensionalArray::arrayIndex(const QList<quint32>
    &indices) const': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant QOpcUaMultiDimensionalArray::value(const QList<quint32>
    &indices) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QOpcUaMultiDimensionalArray::setValue(const QList<quint32>
    &indices, const QVariant &value)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QList<quint32> QOpcUaMultiDimensionalArray::arrayDimensions()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QOpcUaMultiDimensionalArray::setArrayDimensions(const
    QList<quint32> &arrayDimensions)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QVariant QOpcUaMultiDimensionalArray::operator QVariant() const':
    an operator Python has no name for.

  What to expect
  --------------

  - The C++ QOpcUaMultiDimensionalArray is created at the first use, not by
    'QOpcUaMultiDimensionalArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaMultiDimensionalArray back gives a copy the
    ritual made for Python, in a new cute QOpcUaMultiDimensionalArray.
  - Each name of Qt's QOpcUaMultiDimensionalArray that has no cute function
    yet, 'arrayDimensions', 'arrayIndex', 'setArrayDimensions', 'setValue',
    'value', 'valueArrayRef', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaMultiDimensionalArray'

  #  Qt's '~QOpcUaMultiDimensionalArray()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaMultiDimensionalArray behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QOpcUaMultiDimensionalArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valueArray(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QOpcUaMultiDimensionalArray::valueArray()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamultidimensionalarray.html#valueArray

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QOpcUaMultiDimensionalArray::valueArray() const
    address = self.uglySide.call(
        'ritual_ZNK27QOpcUaMultiDimensionalArray10valueArrayEv',
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaMultiDimensionalArray::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamultidimensionalarray.html#isValid
    """
    #  bool QOpcUaMultiDimensionalArray::isValid() const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaMultiDimensionalArray7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVariant])
  def setValueArray(self, valueArray: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaMultiDimensionalArray::setValueArray(const
    QVariantList &valueArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamultidimensionalarray.html#setValueArray

    Parameters
    ----------

    valueArray : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaMultiDimensionalArray::setValueArray(const QVariantList
    #      &valueArray)
    self.uglySide.call(
        'ritual_ZN27QOpcUaMultiDimensionalArray13setValueArrayERK5QListI8QV'
        'ariantE',
        self._valueOf(valueArray),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QOpcUaMultiDimensionalArray) -> bool:
    """
    Calls Qt's 'bool QOpcUaMultiDimensionalArray::operator==(const
    QOpcUaMultiDimensionalArray &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamultidimensionalarray.html#operator==

    Parameters
    ----------

    other : QOpcUaMultiDimensionalArray
      Passed on as a value: Qt reads the C++ QOpcUaMultiDimensionalArray,
      which stays Python's own.
    """
    #  bool QOpcUaMultiDimensionalArray::operator==(const
    #      QOpcUaMultiDimensionalArray &other) const
    return self.uglySide.call(
        'ritual_ZNK27QOpcUaMultiDimensionalArrayeqERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamultidimensionalarray.html
    """
    #  QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray()
    self._noteCreation(QOpcUaMultiDimensionalArray, lambda: Rituals.call(
        'ritual_ZN27QOpcUaMultiDimensionalArrayC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaMultiDimensionalArray) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
    QOpcUaMultiDimensionalArray &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamultidimensionalarray.html

    Parameters
    ----------

    other : QOpcUaMultiDimensionalArray
      Passed on as a value: Qt reads the C++ QOpcUaMultiDimensionalArray,
      which stays Python's own.
    """
    #  QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
    #      QOpcUaMultiDimensionalArray &other)
    self._noteCreation(QOpcUaMultiDimensionalArray, lambda: Rituals.call(
        'ritual_ZN27QOpcUaMultiDimensionalArrayC1ERKS_',
        self._valueOf(other),
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

  @staticmethod
  def arrayDimensions(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> QOpcUaMultiDimensionalArray::arrayDimensions()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaMultiDimensionalArray.arrayDimensions' has no cute function "
        "yet. Qt's 'QList<quint32> "
        "QOpcUaMultiDimensionalArray::arrayDimensions() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def arrayIndex(*__, **_) -> Never:
    """
    Qt's 'int QOpcUaMultiDimensionalArray::arrayIndex(const QList<quint32>
    &indices) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaMultiDimensionalArray.arrayIndex' has no cute function yet. "
        "Qt's 'int QOpcUaMultiDimensionalArray::arrayIndex(const "
        "QList<quint32> &indices) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setArrayDimensions(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaMultiDimensionalArray::setArrayDimensions(const
    QList<quint32> &arrayDimensions)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpcUaMultiDimensionalArray.setArrayDimensions' has no cute "
        "function yet. Qt's 'void "
        "QOpcUaMultiDimensionalArray::setArrayDimensions(const "
        "QList<quint32> &arrayDimensions)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setValue(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaMultiDimensionalArray::setValue(const QList<quint32>
    &indices, const QVariant &value)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QOpcUaMultiDimensionalArray.setValue' has no cute function yet. "
        "Qt's 'bool QOpcUaMultiDimensionalArray::setValue(const "
        "QList<quint32> &indices, const QVariant &value)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QVariant QOpcUaMultiDimensionalArray::value(const QList<quint32>
    &indices) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaMultiDimensionalArray.value' has no cute function yet. Qt's "
        "'QVariant QOpcUaMultiDimensionalArray::value(const QList<quint32> "
        "&indices) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def valueArrayRef(*__, **_) -> Never:
    """
    Qt's 'QVariantList &QOpcUaMultiDimensionalArray::valueArrayRef()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaMultiDimensionalArray.valueArrayRef' has no cute function "
        "yet. Qt's 'QVariantList "
        "&QOpcUaMultiDimensionalArray::valueArrayRef()': gives a type "
        "Python has no way to take yet.")
