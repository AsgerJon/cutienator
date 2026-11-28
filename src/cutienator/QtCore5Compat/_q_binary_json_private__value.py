"""
QBinaryJsonPrivate::Value binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::Value to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QBinaryJsonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonValue

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Value(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::Value: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::Value.

  C++ hands a QBinaryJsonPrivate::Value around as a copy, so every C++
  QBinaryJsonPrivate::Value behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::Value that has a ritual and that
  Python can call so far, 18 names in all: 'intValue', 'data', 'usedStorage',
  'toBoolean', 'toDouble', 'toString', 'asString', 'asLatin1String', 'base',
  'toScalarJsonValue', 'setIsLatinKey', 'isLatinKey', 'setIsLatinOrIntValue',
  'isLatinOrIntValue', 'setType', 'type', 'setValue', 'value'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'uint QBinaryJsonPrivate::Value::requiredStorage(const
    QBinaryJsonValue &v, bool *compressed)': takes a type Python has no way
    to hand over yet.
  - Qt's 'uint QBinaryJsonPrivate::Value::valueToStore(const QBinaryJsonValue
    &v, uint offset)': takes a type Python has no way to hand over yet.
  - Qt's 'QBinaryJsonPrivate::Value::~Value()': the destructor: Python
    removes its C++ QBinaryJsonPrivate::Value by it, and has no other use for
    it.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::Value is created at the first use, not by
    'QBinaryJsonPrivate::Value(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::Value back gives a copy the
    ritual made for Python, in a new cute QBinaryJsonPrivate::Value.
  - Each name of Qt's QBinaryJsonPrivate::Value that has no cute function
    yet, 'copyData', 'isValidHelper', 'requiredStorage', 'valueToStore',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::Value'

  #  Qt's '~QBinaryJsonPrivate::Value()'. Naming it makes this a value class:
  #  Python owns every C++ QBinaryJsonPrivate::Value behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate5ValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def intValue(self) -> int:
    """
    Calls Qt's 'int QBinaryJsonPrivate::Value::intValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#intValue
    """
    #  int QBinaryJsonPrivate::Value::intValue() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value8intValueEv',
    )

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def data(self, b: Optional[QBinaryJsonPrivate.Base]) -> Optional[str]:
    """
    Calls Qt's 'const char *QBinaryJsonPrivate::Value::data(const Base *b)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#data

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QBinaryJsonPrivate::Value::data(const Base *b) const
    chars = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value4dataEPKNS_4BaseE',
        self._addressOf(b),
    )
    return None if chars is None else chars.decode()

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def usedStorage(self, b: Optional[QBinaryJsonPrivate.Base]) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Value::usedStorage(const Base *b)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#usedStorage

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  uint QBinaryJsonPrivate::Value::usedStorage(const Base *b) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value11usedStorageEPKNS_4BaseE',
        self._addressOf(b),
    )

  def toBoolean(self) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Value::toBoolean() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#toBoolean
    """
    #  bool QBinaryJsonPrivate::Value::toBoolean() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value9toBooleanEv',
    )

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def toDouble(self, b: Optional[QBinaryJsonPrivate.Base]) -> float:
    """
    Calls Qt's 'double QBinaryJsonPrivate::Value::toDouble(const Base *b)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#toDouble

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QBinaryJsonPrivate::Value::toDouble(const Base *b) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value8toDoubleEPKNS_4BaseE',
        self._addressOf(b),
    )

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def toString(self, b: Optional[QBinaryJsonPrivate.Base]) -> str:
    """
    Calls Qt's 'QString QBinaryJsonPrivate::Value::toString(const Base *b)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#toString

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBinaryJsonPrivate::Value::toString(const Base *b) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value8toStringEPKNS_4BaseE',
        self._addressOf(b),
    )

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def asString(
      self,
      b: Optional[QBinaryJsonPrivate.Base],
  ) -> QBinaryJsonPrivate.String:
    """
    Calls Qt's 'String QBinaryJsonPrivate::Value::asString(const Base *b)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#asString

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QBinaryJsonPrivate.String
      A new cute QBinaryJsonPrivate::String around the copy Qt gave back.
      Python owns it.
    """
    #  String QBinaryJsonPrivate::Value::asString(const Base *b) const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value8asStringEPKNS_4BaseE',
        self._addressOf(b),
    )
    return QBinaryJsonPrivate.String._cuteOwning(address)

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def asLatin1String(
      self,
      b: Optional[QBinaryJsonPrivate.Base],
  ) -> QBinaryJsonPrivate.Latin1String:
    """
    Calls Qt's 'Latin1String QBinaryJsonPrivate::Value::asLatin1String(const
    Base *b) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#asLatin1String

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QBinaryJsonPrivate.Latin1String
      A new cute QBinaryJsonPrivate::Latin1String around the copy Qt gave
      back. Python owns it.
    """
    #  Latin1String QBinaryJsonPrivate::Value::asLatin1String(const Base *b)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value14asLatin1StringEPKNS_4BaseE',
        self._addressOf(b),
    )
    return QBinaryJsonPrivate.Latin1String._cuteOwning(address)

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def base(
      self,
      b: Optional[QBinaryJsonPrivate.Base],
  ) -> Optional[QBinaryJsonPrivate.Base]:
    """
    Calls Qt's 'const Base *QBinaryJsonPrivate::Value::base(const Base *b)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#base

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBinaryJsonPrivate.Base]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Base *QBinaryJsonPrivate::Value::base(const Base *b) const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value4baseEPKNS_4BaseE',
        self._addressOf(b),
    )
    return QBinaryJsonPrivate.Base._cuteAt(address)

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def toScalarJsonValue(
      self,
      b: Optional[QBinaryJsonPrivate.Base],
  ) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QBinaryJsonPrivate::Value::toScalarJsonValue(const
    Base *b) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#toScalarJsonValue

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QBinaryJsonPrivate::Value::toScalarJsonValue(const Base *b)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value17toScalarJsonValueEPKNS_4Base'
        'E',
        self._addressOf(b),
    )
    from ..QtCore import QJsonValue
    return QJsonValue._cuteOwning(address)

  def isLatinKey(self) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Value::isLatinKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#isLatinKey
    """
    #  bool QBinaryJsonPrivate::Value::isLatinKey() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value10isLatinKeyEv',
    )

  def isLatinOrIntValue(self) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Value::isLatinOrIntValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#isLatinOrIntValue
    """
    #  bool QBinaryJsonPrivate::Value::isLatinOrIntValue() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Value17isLatinOrIntValueEv',
    )

  def type(self) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Value::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#type
    """
    #  uint QBinaryJsonPrivate::Value::type() const
    return self.uglySide.call('ritual_ZNK18QBinaryJsonPrivate5Value4typeEv')

  def value(self) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Value::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#value
    """
    #  uint QBinaryJsonPrivate::Value::value() const
    return self.uglySide.call('ritual_ZNK18QBinaryJsonPrivate5Value5valueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsLatinKey(self, isLatinKey: bool) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Value::setIsLatinKey(bool
    isLatinKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#setIsLatinKey

    Parameters
    ----------

    isLatinKey : bool
      Passed on as it is.
    """
    #  void QBinaryJsonPrivate::Value::setIsLatinKey(bool isLatinKey)
    self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate5Value13setIsLatinKeyEb', isLatinKey,
    )

  @overload(bool)
  def setIsLatinOrIntValue(self, v: bool) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Value::setIsLatinOrIntValue(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#setIsLatinOrIntValue

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QBinaryJsonPrivate::Value::setIsLatinOrIntValue(bool v)
    self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate5Value20setIsLatinOrIntValueEb', v,
    )

  @overload(int)
  def setType(self, type: int) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Value::setType(uint type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#setType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QBinaryJsonPrivate::Value::setType(uint type)
    self.uglySide.call('ritual_ZN18QBinaryJsonPrivate5Value7setTypeEj', type)

  @overload(int)
  def setValue(self, value: int) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::Value::setValue(uint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-value.html#setValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QBinaryJsonPrivate::Value::setValue(uint value)
    self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate5Value8setValueEj', value,
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

  @staticmethod
  def copyData(*__, **_) -> Never:
    """
    Qt's 'void QBinaryJsonPrivate::Value::copyData(const QBinaryJsonValue &v,
    char *dest, bool compressed)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'emptyArray'.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Value.copyData' has no cute function yet. Qt's "
        "'void QBinaryJsonPrivate::Value::copyData(const QBinaryJsonValue "
        "&v, char *dest, bool compressed)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'emptyArray'.")

  @staticmethod
  def isValidHelper(*__, **_) -> Never:
    """
    Qt's 'bool QBinaryJsonPrivate::Value::isValidHelper(const Base *b,
    IsValidStack &stack) const': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'isValidValueOffset'.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Value.isValidHelper' has no cute function yet. "
        "Qt's 'bool QBinaryJsonPrivate::Value::isValidHelper(const Base *b, "
        "IsValidStack &stack) const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'isValidValueOffset'.")

  @staticmethod
  def requiredStorage(*__, **_) -> Never:
    """
    Qt's 'uint QBinaryJsonPrivate::Value::requiredStorage(const
    QBinaryJsonValue &v, bool *compressed)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Value.requiredStorage' has no cute function "
        "yet. Qt's 'uint QBinaryJsonPrivate::Value::requiredStorage(const "
        "QBinaryJsonValue &v, bool *compressed)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def valueToStore(*__, **_) -> Never:
    """
    Qt's 'uint QBinaryJsonPrivate::Value::valueToStore(const QBinaryJsonValue
    &v, uint offset)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Value.valueToStore' has no cute function yet. "
        "Qt's 'uint QBinaryJsonPrivate::Value::valueToStore(const "
        "QBinaryJsonValue &v, uint offset)': takes a type Python has no way "
        "to hand over yet.")
