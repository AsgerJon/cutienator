"""
QMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ._qt import Qt
from ._q_byte_array import QByteArray
from ._q_meta_object__connection import Connection
from ._q_meta_object_call import Call

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaObject: a plain Python object standing in front
  of one C++ QMetaObject.

  C++ hands a QMetaObject around as a copy, so every C++ QMetaObject behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaObject that has a ritual and that Python can
  call so far, 29 names in all: 'className', 'superClass', 'inherits',
  'cast', 'tr', 'methodOffset', 'enumeratorOffset', 'propertyOffset',
  'classInfoOffset', 'constructorCount', 'methodCount', 'enumeratorCount',
  'propertyCount', 'classInfoCount', 'indexOfConstructor', 'indexOfMethod',
  'indexOfSignal', 'indexOfSlot', 'indexOfEnumerator', 'indexOfProperty',
  'indexOfClassInfo', 'constructor', 'method', 'checkConnectArgs',
  'normalizedSignature', 'normalizedType', 'disconnect', 'disconnectOne',
  'connectSlotsByName'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QObject *QMetaObject::cast(const QObject *obj) const': takes
    in Python what 'QObject *QMetaObject::cast(QObject *obj) const' takes.
  - Qt's 'QMetaType QMetaObject::metaType() const': gives 'QMetaType', which
    has no cute class yet.
  - Qt's 'QMetaEnum QMetaObject::enumerator(int index) const': gives
    'QMetaEnum', which has no cute class yet.
  - Qt's 'QMetaProperty QMetaObject::property(int index) const': gives
    'QMetaProperty', which has no cute class yet.
  - Qt's 'QMetaClassInfo QMetaObject::classInfo(int index) const': gives
    'QMetaClassInfo', which has no cute class yet.
  - Qt's 'QMetaProperty QMetaObject::userProperty() const': gives
    'QMetaProperty', which has no cute class yet.
  - Qt's 'Connection QMetaObject::connect(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index, int type, int
    *types)': takes a number to change where it is.
  - Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    Qt::ConnectionType a2, QGenericReturnArgument ret, QGenericArgument val0,
    QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
    QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
    QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)':
    names 'QGenericReturnArgument', which has no cute class yet.
  - Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    QGenericReturnArgument ret, QGenericArgument val0, QGenericArgument val1,
    QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
    QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
    QGenericArgument val8, QGenericArgument val9)': names
    'QGenericReturnArgument', which has no cute class yet.
  - Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    Qt::ConnectionType type, QGenericArgument val0, QGenericArgument val1,
    QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
    QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
    QGenericArgument val8, QGenericArgument val9)': names 'QGenericArgument',
    which has no cute class yet.
  - Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    QGenericArgument val0, QGenericArgument val1, QGenericArgument val2,
    QGenericArgument val3, QGenericArgument val4, QGenericArgument val5,
    QGenericArgument val6, QGenericArgument val7, QGenericArgument val8,
    QGenericArgument val9)': names 'QGenericArgument', which has no cute
    class yet.
  - Qt's 'QObject *QMetaObject::newInstance(QGenericArgument val0,
    QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
    QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
    QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)
    const': names 'QGenericArgument', which has no cute class yet.
  - Qt's 'QMetaObject::~QMetaObject()': the destructor: Python removes its
    C++ QMetaObject by it, and has no other use for it.

  What has no ritual
  ------------------

  24 of the 67 functions Qt declares: 15 a template; 5 takes or gives a type
  that cannot be passed yet; 4 private.

  What to expect
  --------------

  - The C++ QMetaObject is created at the first use, not by
    'QMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaObject back gives a copy the ritual made for
    Python, in a new cute QMetaObject.
  """

  #  The classes Qt writes inside QMetaObject.
  Connection = Connection

  #  The enums Qt writes inside QMetaObject, and the names Qt has for the
  #  combinations of its flags enums.
  Call = Call

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QMetaMethod = WAIT['QMetaMethod']
  QObject = WAIT['QObject']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def checkConnectArgs(signal: Optional[str], method: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QMetaObject::checkConnectArgs(const char *signal, const
    char *method)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#checkConnectArgs

    Parameters
    ----------

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QMetaObject::checkConnectArgs(const char *signal, const char
    #      *method)
    return Rituals.call(
        'ritual_ZN11QMetaObject16checkConnectArgsEPKcS1_',
        CuteMixin._bytesOf(signal), CuteMixin._bytesOf(method),
    )

  @staticmethod
  @overload(QMetaMethod, QMetaMethod)
  def checkConnectArgs(signal: QMetaMethod, method: QMetaMethod) -> bool:
    """
    Calls Qt's 'bool QMetaObject::checkConnectArgs(const QMetaMethod &signal,
    const QMetaMethod &method)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#checkConnectArgs

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    method : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool QMetaObject::checkConnectArgs(const QMetaMethod &signal, const
    #      QMetaMethod &method)
    return Rituals.call(
        'ritual_ZN11QMetaObject16checkConnectArgsERK11QMetaMethodS2_',
        CuteMixin._valueOf(signal), CuteMixin._valueOf(method),
    )

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def normalizedSignature(method: Optional[str]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaObject::normalizedSignature(const char
    *method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobject.html#normalizedSignature

    Parameters
    ----------

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaObject::normalizedSignature(const char *method)
    address = Rituals.call(
        'ritual_ZN11QMetaObject19normalizedSignatureEPKc',
        CuteMixin._bytesOf(method),
    )
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def normalizedType(type: Optional[str]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaObject::normalizedType(const char *type)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#normalizedType

    Parameters
    ----------

    type : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaObject::normalizedType(const char *type)
    address = Rituals.call(
        'ritual_ZN11QMetaObject14normalizedTypeEPKc',
        CuteMixin._bytesOf(type),
    )
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QObject, int, QObject, int)
  def disconnect(
      sender: QObject,
      signal_index: int,
      receiver: QObject,
      method_index: int,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::disconnect(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#disconnect

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    sender : QObject
      Passed on as the address of its C++ object.

    signal_index : int
      Passed on as it is.

    receiver : QObject
      Passed on as the address of its C++ object.

    method_index : int
      Passed on as it is.
    """
    #  bool QMetaObject::disconnect(const QObject *sender, int signal_index,
    #      const QObject *receiver, int method_index)
    return Rituals.call(
        'ritual_ZN11QMetaObject10disconnectEPK7QObjectiS2_i',
        CuteMixin._addressOf(sender), signal_index,
        CuteMixin._addressOf(receiver), method_index,
    )

  @staticmethod
  @overload(QObject, int, QObject, int)
  def disconnectOne(
      sender: QObject,
      signal_index: int,
      receiver: QObject,
      method_index: int,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::disconnectOne(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#disconnectOne

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    sender : QObject
      Passed on as the address of its C++ object.

    signal_index : int
      Passed on as it is.

    receiver : QObject
      Passed on as the address of its C++ object.

    method_index : int
      Passed on as it is.
    """
    #  bool QMetaObject::disconnectOne(const QObject *sender, int
    #      signal_index, const QObject *receiver, int method_index)
    return Rituals.call(
        'ritual_ZN11QMetaObject13disconnectOneEPK7QObjectiS2_i',
        CuteMixin._addressOf(sender), signal_index,
        CuteMixin._addressOf(receiver), method_index,
    )

  @staticmethod
  @overload(QObject)
  def connectSlotsByName(o: QObject) -> None:
    """
    Calls Qt's 'void QMetaObject::connectSlotsByName(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobject.html#connectSlotsByName

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    o : QObject
      Passed on as the address of its C++ object.
    """
    #  void QMetaObject::connectSlotsByName(QObject *o)
    Rituals.call(
        'ritual_ZN11QMetaObject18connectSlotsByNameEP7QObject',
        CuteMixin._addressOf(o),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaObject'

  #  Qt's '~QMetaObject()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaObject behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QMetaObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def className(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaObject::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#className

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaObject::className() const
    chars = self.uglySide.call('ritual_ZNK11QMetaObject9classNameEv')
    return None if chars is None else chars.decode()

  def superClass(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaObject::superClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#superClass

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaObject::superClass() const
    address = self.uglySide.call('ritual_ZNK11QMetaObject10superClassEv')
    return QMetaObject._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def inherits(self, metaObject: Optional[QMetaObject]) -> bool:
    """
    Calls Qt's 'bool QMetaObject::inherits(const QMetaObject *metaObject)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#inherits

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaObject::inherits(const QMetaObject *metaObject) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject8inheritsEPKS_', self._addressOf(metaObject),
    )

  @overload(QObject)
  def cast(self, obj: QObject) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMetaObject::cast(QObject *obj) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#cast

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    obj : QObject
      Passed on as the address of its C++ object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMetaObject::cast(QObject *obj) const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaObject4castEP7QObject', self._addressOf(obj),
    )
    return self.QObject._cuteAt(address)

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(self, s: Optional[str], c: Optional[str], n: int = -1) -> str:
    """
    Calls Qt's 'QString QMetaObject::tr(const char *s, const char *c, int n)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMetaObject::tr(const char *s, const char *c, int n) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject2trEPKcS1_i',
        self._bytesOf(s), self._bytesOf(c), n,
    )

  def methodOffset(self) -> int:
    """
    Calls Qt's 'int QMetaObject::methodOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#methodOffset
    """
    #  int QMetaObject::methodOffset() const
    return self.uglySide.call('ritual_ZNK11QMetaObject12methodOffsetEv')

  def enumeratorOffset(self) -> int:
    """
    Calls Qt's 'int QMetaObject::enumeratorOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#enumeratorOffset
    """
    #  int QMetaObject::enumeratorOffset() const
    return self.uglySide.call('ritual_ZNK11QMetaObject16enumeratorOffsetEv')

  def propertyOffset(self) -> int:
    """
    Calls Qt's 'int QMetaObject::propertyOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#propertyOffset
    """
    #  int QMetaObject::propertyOffset() const
    return self.uglySide.call('ritual_ZNK11QMetaObject14propertyOffsetEv')

  def classInfoOffset(self) -> int:
    """
    Calls Qt's 'int QMetaObject::classInfoOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#classInfoOffset
    """
    #  int QMetaObject::classInfoOffset() const
    return self.uglySide.call('ritual_ZNK11QMetaObject15classInfoOffsetEv')

  def constructorCount(self) -> int:
    """
    Calls Qt's 'int QMetaObject::constructorCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#constructorCount
    """
    #  int QMetaObject::constructorCount() const
    return self.uglySide.call('ritual_ZNK11QMetaObject16constructorCountEv')

  def methodCount(self) -> int:
    """
    Calls Qt's 'int QMetaObject::methodCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#methodCount
    """
    #  int QMetaObject::methodCount() const
    return self.uglySide.call('ritual_ZNK11QMetaObject11methodCountEv')

  def enumeratorCount(self) -> int:
    """
    Calls Qt's 'int QMetaObject::enumeratorCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#enumeratorCount
    """
    #  int QMetaObject::enumeratorCount() const
    return self.uglySide.call('ritual_ZNK11QMetaObject15enumeratorCountEv')

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QMetaObject::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#propertyCount
    """
    #  int QMetaObject::propertyCount() const
    return self.uglySide.call('ritual_ZNK11QMetaObject13propertyCountEv')

  def classInfoCount(self) -> int:
    """
    Calls Qt's 'int QMetaObject::classInfoCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#classInfoCount
    """
    #  int QMetaObject::classInfoCount() const
    return self.uglySide.call('ritual_ZNK11QMetaObject14classInfoCountEv')

  @overload(str)
  @overload(NoneType)
  def indexOfConstructor(self, constructor: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfConstructor(const char *constructor)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobject.html#indexOfConstructor

    Parameters
    ----------

    constructor : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfConstructor(const char *constructor) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject18indexOfConstructorEPKc',
        self._bytesOf(constructor),
    )

  @overload(str)
  @overload(NoneType)
  def indexOfMethod(self, method: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfMethod(const char *method) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#indexOfMethod

    Parameters
    ----------

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfMethod(const char *method) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject13indexOfMethodEPKc', self._bytesOf(method),
    )

  @overload(str)
  @overload(NoneType)
  def indexOfSignal(self, signal: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfSignal(const char *signal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#indexOfSignal

    Parameters
    ----------

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfSignal(const char *signal) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject13indexOfSignalEPKc', self._bytesOf(signal),
    )

  @overload(str)
  @overload(NoneType)
  def indexOfSlot(self, slot: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfSlot(const char *slot) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#indexOfSlot

    Parameters
    ----------

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfSlot(const char *slot) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject11indexOfSlotEPKc', self._bytesOf(slot),
    )

  @overload(str)
  @overload(NoneType)
  def indexOfEnumerator(self, name: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfEnumerator(const char *name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#indexOfEnumerator

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfEnumerator(const char *name) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject17indexOfEnumeratorEPKc',
        self._bytesOf(name),
    )

  @overload(str)
  @overload(NoneType)
  def indexOfProperty(self, name: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfProperty(const char *name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#indexOfProperty

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfProperty(const char *name) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject15indexOfPropertyEPKc', self._bytesOf(name),
    )

  @overload(str)
  @overload(NoneType)
  def indexOfClassInfo(self, name: Optional[str]) -> int:
    """
    Calls Qt's 'int QMetaObject::indexOfClassInfo(const char *name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#indexOfClassInfo

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QMetaObject::indexOfClassInfo(const char *name) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaObject16indexOfClassInfoEPKc', self._bytesOf(name),
    )

  @overload(int)
  def constructor(self, index: int) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QMetaObject::constructor(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#constructor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QMetaObject::constructor(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaObject11constructorEi', index,
    )
    return self.QMetaMethod._cuteOwning(address)

  @overload(int)
  def method(self, index: int) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QMetaObject::method(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#method

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QMetaObject::method(int index) const
    address = self.uglySide.call('ritual_ZNK11QMetaObject6methodEi', index)
    return self.QMetaMethod._cuteOwning(address)

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
