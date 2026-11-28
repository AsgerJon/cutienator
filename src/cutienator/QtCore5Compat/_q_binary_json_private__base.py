"""
QBinaryJsonPrivate::Base binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::Base to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Base(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::Base: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::Base.

  C++ hands a QBinaryJsonPrivate::Base around as a copy, so every C++
  QBinaryJsonPrivate::Base behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::Base that has a ritual and that
  Python can call so far, 7 names in all: 'setIsObject', 'isObject',
  'setIsArray', 'isArray', 'setLength', 'length', 'reserveSpace'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'offset *QBinaryJsonPrivate::Base::table()': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
  - Qt's 'const offset *QBinaryJsonPrivate::Base::table() const': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
  - Qt's 'QBinaryJsonPrivate::Base::~Base()': the destructor: Python removes
    its C++ QBinaryJsonPrivate::Base by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::Base is created at the first use, not by
    'QBinaryJsonPrivate::Base(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::Base back gives a copy the ritual
    made for Python, in a new cute QBinaryJsonPrivate::Base.
  - Each name of Qt's QBinaryJsonPrivate::Base that has no cute function yet,
    'table', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::Base'

  #  Qt's '~QBinaryJsonPrivate::Base()'. Naming it makes this a value class:
  #  Python owns every C++ QBinaryJsonPrivate::Base behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate4BaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isObject(self) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Base::isObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#isObject
    """
    #  bool QBinaryJsonPrivate::Base::isObject() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate4Base8isObjectEv',
    )

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Base::isArray() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#isArray
    """
    #  bool QBinaryJsonPrivate::Base::isArray() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate4Base7isArrayEv',
    )

  def length(self) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Base::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#length
    """
    #  uint QBinaryJsonPrivate::Base::length() const
    return self.uglySide.call('ritual_ZNK18QBinaryJsonPrivate4Base6lengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setIsObject(self) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Base::setIsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#setIsObject
    """
    #  void QBinaryJsonPrivate::Base::setIsObject()
    self.uglySide.call('ritual_ZN18QBinaryJsonPrivate4Base11setIsObjectEv')

  def setIsArray(self) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Base::setIsArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#setIsArray
    """
    #  void QBinaryJsonPrivate::Base::setIsArray()
    self.uglySide.call('ritual_ZN18QBinaryJsonPrivate4Base10setIsArrayEv')

  @overload(int)
  def setLength(self, length: int) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Base::setLength(uint length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#setLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QBinaryJsonPrivate::Base::setLength(uint length)
    self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate4Base9setLengthEj', length,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(int, int, int, bool)
  def reserveSpace(
      self,
      dataSize: int,
      posInTable: int,
      numItems: int,
      replace: bool,
  ) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Base::reserveSpace(uint dataSize,
    uint posInTable, uint numItems, bool replace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-base.html#reserveSpace

    Parameters
    ----------

    dataSize : int
      Passed on as it is.

    posInTable : int
      Passed on as it is.

    numItems : int
      Passed on as it is.

    replace : bool
      Passed on as it is.
    """
    #  uint QBinaryJsonPrivate::Base::reserveSpace(uint dataSize, uint
    #      posInTable, uint numItems, bool replace)
    return self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate4Base12reserveSpaceEjjjb',
        dataSize, posInTable, numItems, replace,
    )

  @staticmethod
  def table(*__, **_) -> Never:
    """
    - Qt's 'offset *QBinaryJsonPrivate::Base::table()': gives
      'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
      cute class yet.
    - Qt's 'const offset *QBinaryJsonPrivate::Base::table() const': gives
      'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
      cute class yet.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Base.table' has no cute function yet. Qt's "
        "'offset *QBinaryJsonPrivate::Base::table()': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet. Qt's 'const offset "
        "*QBinaryJsonPrivate::Base::table() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")
