"""
QMetaEnum binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QMetaObject, QMetaType


class QMetaEnum(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaEnum: a plain Python object standing in front of
  one C++ QMetaEnum.

  C++ hands a QMetaEnum around as a copy, so every C++ QMetaEnum behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaEnum that has a ritual and that Python can call
  so far, 14 names in all: 'name', 'enumName', 'metaType', 'isFlag',
  'isScoped', 'is64Bit', 'keyCount', 'key', 'value', 'scope', 'valueToKey',
  'valueToKeys', 'enclosingMetaObject', 'isValid'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QMetaEnum::keyToValue(const char *key, bool *ok) const': takes
    a number to change where it is.
  - Qt's 'int QMetaEnum::keysToValue(const char *keys, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'QMetaEnum::~QMetaEnum()': the destructor: Python removes its C++
    QMetaEnum by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 24 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 2 a template; 1 private.

  What to expect
  --------------

  - The C++ QMetaEnum is created at the first use, not by 'QMetaEnum(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaEnum back gives a copy the ritual made for
    Python, in a new cute QMetaEnum.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaEnum'

  #  Qt's '~QMetaEnum()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaEnum behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QMetaEnumD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaEnum::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#name

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaEnum::name() const
    chars = self.uglySide.call('ritual_ZNK9QMetaEnum4nameEv')
    return None if chars is None else chars.decode()

  def enumName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaEnum::enumName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#enumName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaEnum::enumName() const
    chars = self.uglySide.call('ritual_ZNK9QMetaEnum8enumNameEv')
    return None if chars is None else chars.decode()

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaEnum::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaEnum::metaType() const
    address = self.uglySide.call('ritual_ZNK9QMetaEnum8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def isFlag(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnum::isFlag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#isFlag
    """
    #  bool QMetaEnum::isFlag() const
    return self.uglySide.call('ritual_ZNK9QMetaEnum6isFlagEv')

  def isScoped(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnum::isScoped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#isScoped
    """
    #  bool QMetaEnum::isScoped() const
    return self.uglySide.call('ritual_ZNK9QMetaEnum8isScopedEv')

  def is64Bit(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnum::is64Bit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#is64Bit
    """
    #  bool QMetaEnum::is64Bit() const
    return self.uglySide.call('ritual_ZNK9QMetaEnum7is64BitEv')

  def keyCount(self) -> int:
    """
    Calls Qt's 'int QMetaEnum::keyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#keyCount
    """
    #  int QMetaEnum::keyCount() const
    return self.uglySide.call('ritual_ZNK9QMetaEnum8keyCountEv')

  @overload(int)
  def key(self, index: int) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaEnum::key(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#key

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaEnum::key(int index) const
    chars = self.uglySide.call('ritual_ZNK9QMetaEnum3keyEi', index)
    return None if chars is None else chars.decode()

  @overload(int)
  def value(self, index: int) -> int:
    """
    Calls Qt's 'int QMetaEnum::value(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QMetaEnum::value(int index) const
    return self.uglySide.call('ritual_ZNK9QMetaEnum5valueEi', index)

  def scope(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaEnum::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#scope

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaEnum::scope() const
    chars = self.uglySide.call('ritual_ZNK9QMetaEnum5scopeEv')
    return None if chars is None else chars.decode()

  @overload(int)
  def valueToKey(self, value: int) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaEnum::valueToKey(quint64 value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#valueToKey

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaEnum::valueToKey(quint64 value) const
    chars = self.uglySide.call('ritual_ZNK9QMetaEnum10valueToKeyEy', value)
    return None if chars is None else chars.decode()

  @overload(int)
  def valueToKeys(self, value: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaEnum::valueToKeys(quint64 value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#valueToKeys

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaEnum::valueToKeys(quint64 value) const
    address = self.uglySide.call(
        'ritual_ZNK9QMetaEnum11valueToKeysEy', value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def enclosingMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaEnum::enclosingMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#enclosingMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaEnum::enclosingMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9QMetaEnum19enclosingMetaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnum::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#isValid
    """
    #  bool QMetaEnum::isValid() const
    return self.uglySide.call('ritual_ZNK9QMetaEnum7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QMetaEnum::QMetaEnum()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenum.html#QMetaEnum
    """
    #  QMetaEnum::QMetaEnum()
    self._noteCreation(QMetaEnum, lambda: Rituals.call(
        'ritual_ZN9QMetaEnumC1Ev',
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
