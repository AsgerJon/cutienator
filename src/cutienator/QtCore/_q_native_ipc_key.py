"""
QNativeIpcKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtipccommon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QNativeIpcKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeIpcKey: a plain Python object standing in
  front of one C++ QNativeIpcKey.

  C++ hands a QNativeIpcKey around as a copy, so every C++ QNativeIpcKey
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNativeIpcKey that has a ritual and that Python can
  call so far, 11 names in all: 'legacyDefaultTypeForOs', 'isEmpty',
  'isValid', 'type', 'setType', 'nativeKey', 'setNativeKey', 'toString',
  'fromString', '__eq__', '__ne__'. It can be made from Python, in 4 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeIpcKey::~QNativeIpcKey()': the destructor: Python removes
    its C++ QNativeIpcKey by it, and has no other use for it.

  What has no ritual
  ------------------

  15 of the 31 functions Qt declares: 9 private; 4 takes or gives a type that
  cannot be passed yet; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QNativeIpcKey is created at the first use, not by
    'QNativeIpcKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNativeIpcKey back gives a copy the ritual made for
    Python, in a new cute QNativeIpcKey.
  """

  #  The enums Qt writes inside QNativeIpcKey, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QNativeIpcKey::Type' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    SystemV = Kee[int](81)
    PosixRealtime = Kee[int](256)
    Windows = Kee[int](257)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def legacyDefaultTypeForOs() -> Type:
    """
    Calls Qt's 'Type QNativeIpcKey::legacyDefaultTypeForOs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeipckey.html#legacyDefaultTypeForOs

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QNativeIpcKey::legacyDefaultTypeForOs()
    return QNativeIpcKey.Type(Rituals.call(
        'ritual_ZN13QNativeIpcKey22legacyDefaultTypeForOsEv',
    ))

  @staticmethod
  @overload(str)
  def fromString(string: str) -> QNativeIpcKey:
    """
    Calls Qt's 'QNativeIpcKey QNativeIpcKey::fromString(const QString
    &string)'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QNativeIpcKey
      A new cute QNativeIpcKey around the copy Qt gave back. Python owns it.
    """
    #  QNativeIpcKey QNativeIpcKey::fromString(const QString &string)
    address = Rituals.call(
        'ritual_ZN13QNativeIpcKey10fromStringERK7QString', string,
    )
    return QNativeIpcKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeIpcKey'

  #  Qt's '~QNativeIpcKey()'. Naming it makes this a value class: Python owns
  #  every C++ QNativeIpcKey behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QNativeIpcKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QNativeIpcKey::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#isEmpty
    """
    #  bool QNativeIpcKey::isEmpty() const
    return self.uglySide.call('ritual_ZNK13QNativeIpcKey7isEmptyEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QNativeIpcKey::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#isValid
    """
    #  bool QNativeIpcKey::isValid() const
    return self.uglySide.call('ritual_ZNK13QNativeIpcKey7isValidEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QNativeIpcKey::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QNativeIpcKey::type() const
    return QNativeIpcKey.Type(self.uglySide.call(
        'ritual_ZNK13QNativeIpcKey4typeEv',
    ))

  def nativeKey(self) -> str:
    """
    Calls Qt's 'QString QNativeIpcKey::nativeKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#nativeKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNativeIpcKey::nativeKey() const
    return self.uglySide.call('ritual_ZNK13QNativeIpcKey9nativeKeyEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QNativeIpcKey::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNativeIpcKey::toString() const
    return self.uglySide.call('ritual_ZNK13QNativeIpcKey8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def setType(self, type: Type) -> None:
    """
    Calls Qt's 'void QNativeIpcKey::setType(Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#setType

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void QNativeIpcKey::setType(Type type)
    self.uglySide.call(
        'ritual_ZN13QNativeIpcKey7setTypeENS_4TypeE', type.value,
    )

  @overload(str)
  def setNativeKey(self, newKey: str) -> None:
    """
    Calls Qt's 'void QNativeIpcKey::setNativeKey(const QString &newKey)'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#setNativeKey

    Parameters
    ----------

    newKey : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNativeIpcKey::setNativeKey(const QString &newKey)
    self.uglySide.call(
        'ritual_ZN13QNativeIpcKey12setNativeKeyERK7QString', newKey,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QNativeIpcKey) -> bool:
    """
    Calls Qt's 'bool operator==(const QNativeIpcKey &lhs, const QNativeIpcKey
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#operator==

    Parameters
    ----------

    rhs : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.
    """
    #  bool operator==(const QNativeIpcKey &lhs, const QNativeIpcKey &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QNativeIpcKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QNativeIpcKey) -> bool:
    """
    Calls Qt's 'bool operator!=(const QNativeIpcKey &lhs, const QNativeIpcKey
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#operator!=

    Parameters
    ----------

    rhs : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.
    """
    #  bool operator!=(const QNativeIpcKey &lhs, const QNativeIpcKey &rhs)
    return Rituals.call(
        'ritual_ZneRK13QNativeIpcKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's 'QNativeIpcKey::QNativeIpcKey()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#QNativeIpcKey
    """
    #  QNativeIpcKey::QNativeIpcKey()
    self._noteCreation(QNativeIpcKey, lambda: Rituals.call(
        'ritual_ZN13QNativeIpcKeyC1Ev',
    ))

  @overload(Type)
  def __init__(self, type: Type) -> None:
    """
    Notes what was given, for Qt's 'QNativeIpcKey::QNativeIpcKey(Type type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#QNativeIpcKey

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  QNativeIpcKey::QNativeIpcKey(Type type)
    self._noteCreation(QNativeIpcKey, lambda: Rituals.call(
        'ritual_ZN13QNativeIpcKeyC1ENS_4TypeE', type.value,
    ))

  @overload(str, Type)
  def __init__(self, k: str, type: Type) -> None:
    """
    Notes what was given, for Qt's 'QNativeIpcKey::QNativeIpcKey(const
    QString &k, Type type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#QNativeIpcKey

    Parameters
    ----------

    k : str
      Passed on as it is: a QString is made of it for the call.

    type : Type
      Passed on as its number.
    """
    #  QNativeIpcKey::QNativeIpcKey(const QString &k, Type type)
    self._noteCreation(QNativeIpcKey, lambda: Rituals.call(
        'ritual_ZN13QNativeIpcKeyC1ERK7QStringNS_4TypeE', k, type.value,
    ))

  @overload(THIS)
  def __init__(self, other: QNativeIpcKey) -> None:
    """
    Notes what was given, for Qt's 'QNativeIpcKey::QNativeIpcKey(const
    QNativeIpcKey &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnativeipckey.html#QNativeIpcKey

    Parameters
    ----------

    other : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.
    """
    #  QNativeIpcKey::QNativeIpcKey(const QNativeIpcKey &other)
    self._noteCreation(QNativeIpcKey, lambda: Rituals.call(
        'ritual_ZN13QNativeIpcKeyC1ERKS_', self._valueOf(other),
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
