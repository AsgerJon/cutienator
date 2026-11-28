"""
QQmlPropertyIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlPropertyIndex to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QQmlPropertyIndex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyIndex: a plain Python object standing in
  front of one C++ QQmlPropertyIndex.

  C++ hands a QQmlPropertyIndex around as a copy, so every C++
  QQmlPropertyIndex behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyIndex that has a ritual and that Python
  can call so far, 10 names in all: 'fromEncoded', 'isValid', 'coreIndex',
  'valueTypeIndex', 'hasValueTypeIndex', 'toEncoded', 'intValue', '__eq__',
  '__ne__', 'encode'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPropertyIndex::~QQmlPropertyIndex()': the destructor: Python
    removes its C++ QQmlPropertyIndex by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlPropertyIndex is created at the first use, not by
    'QQmlPropertyIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyIndex back gives a copy the ritual made
    for Python, in a new cute QQmlPropertyIndex.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def fromEncoded(encodedIndex: int) -> QQmlPropertyIndex:
    """
    Calls Qt's 'QQmlPropertyIndex QQmlPropertyIndex::fromEncoded(qint32
    encodedIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#fromEncoded

    Parameters
    ----------

    encodedIndex : int
      Passed on as it is.

    Returns
    -------

    QQmlPropertyIndex
      A new cute QQmlPropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyIndex QQmlPropertyIndex::fromEncoded(qint32 encodedIndex)
    address = Rituals.call(
        'ritual_ZN17QQmlPropertyIndex11fromEncodedEi', encodedIndex,
    )
    return QQmlPropertyIndex._cuteOwning(address)

  @staticmethod
  @overload(int, int)
  def encode(coreIndex: int, valueTypeIndex: int) -> int:
    """
    Calls Qt's 'qint32 QQmlPropertyIndex::encode(int coreIndex, int
    valueTypeIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#encode

    Parameters
    ----------

    coreIndex : int
      Passed on as it is.

    valueTypeIndex : int
      Passed on as it is.
    """
    #  qint32 QQmlPropertyIndex::encode(int coreIndex, int valueTypeIndex)
    return Rituals.call(
        'ritual_ZN17QQmlPropertyIndex6encodeEii', coreIndex, valueTypeIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyIndex'

  #  Qt's '~QQmlPropertyIndex()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlPropertyIndex behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQmlPropertyIndexD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyIndex::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#isValid
    """
    #  bool QQmlPropertyIndex::isValid() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyIndex7isValidEv')

  def coreIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyIndex::coreIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#coreIndex
    """
    #  int QQmlPropertyIndex::coreIndex() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyIndex9coreIndexEv')

  def valueTypeIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyIndex::valueTypeIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyindex.html#valueTypeIndex
    """
    #  int QQmlPropertyIndex::valueTypeIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyIndex14valueTypeIndexEv',
    )

  def hasValueTypeIndex(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyIndex::hasValueTypeIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyindex.html#hasValueTypeIndex
    """
    #  bool QQmlPropertyIndex::hasValueTypeIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyIndex17hasValueTypeIndexEv',
    )

  def toEncoded(self) -> int:
    """
    Calls Qt's 'qint32 QQmlPropertyIndex::toEncoded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#toEncoded
    """
    #  qint32 QQmlPropertyIndex::toEncoded() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyIndex9toEncodedEv')

  def intValue(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyIndex::intValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#intValue
    """
    #  int QQmlPropertyIndex::intValue() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyIndex8intValueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QQmlPropertyIndex) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyIndex::operator==(const QQmlPropertyIndex
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#operator==

    Parameters
    ----------

    other : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.
    """
    #  bool QQmlPropertyIndex::operator==(const QQmlPropertyIndex &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyIndexeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QQmlPropertyIndex) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyIndex::operator!=(const QQmlPropertyIndex
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyindex.html#operator!=

    Parameters
    ----------

    other : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.
    """
    #  bool QQmlPropertyIndex::operator!=(const QQmlPropertyIndex &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyIndexneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QQmlPropertyIndex::QQmlPropertyIndex()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyindex.html#QQmlPropertyIndex
    """
    #  QQmlPropertyIndex::QQmlPropertyIndex()
    self._noteCreation(QQmlPropertyIndex, lambda: Rituals.call(
        'ritual_ZN17QQmlPropertyIndexC1Ev',
    ))

  @overload(int)
  def __init__(self, coreIndex: int) -> None:
    """
    Notes what was given, for Qt's 'QQmlPropertyIndex::QQmlPropertyIndex(int
    coreIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyindex.html#QQmlPropertyIndex

    Parameters
    ----------

    coreIndex : int
      Passed on as it is.
    """
    #  QQmlPropertyIndex::QQmlPropertyIndex(int coreIndex)
    self._noteCreation(QQmlPropertyIndex, lambda: Rituals.call(
        'ritual_ZN17QQmlPropertyIndexC1Ei', coreIndex,
    ))

  @overload(int, int)
  def __init__(self, coreIndex: int, valueTypeIndex: int) -> None:
    """
    Notes what was given, for Qt's 'QQmlPropertyIndex::QQmlPropertyIndex(int
    coreIndex, int valueTypeIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyindex.html#QQmlPropertyIndex

    Parameters
    ----------

    coreIndex : int
      Passed on as it is.

    valueTypeIndex : int
      Passed on as it is.
    """
    #  QQmlPropertyIndex::QQmlPropertyIndex(int coreIndex, int
    #      valueTypeIndex)
    self._noteCreation(QQmlPropertyIndex, lambda: Rituals.call(
        'ritual_ZN17QQmlPropertyIndexC1Eii', coreIndex, valueTypeIndex,
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
