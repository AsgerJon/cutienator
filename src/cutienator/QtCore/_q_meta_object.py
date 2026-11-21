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
from . import Qt, QMetaObjectCall, QMetaObjectConnection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QGenericArgument, QGenericReturnArgument
  from . import QMetaEnum, QMetaMethod, QMetaProperty, QMetaType, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGenericArgument = WAIT['QGenericArgument']
  QGenericReturnArgument = WAIT['QGenericReturnArgument']
  QMetaMethod = WAIT['QMetaMethod']
  QObject = WAIT['QObject']

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
  call so far, 35 names in all: 'className', 'superClass', 'inherits',
  'cast', 'tr', 'metaType', 'methodOffset', 'enumeratorOffset',
  'propertyOffset', 'classInfoOffset', 'constructorCount', 'methodCount',
  'enumeratorCount', 'propertyCount', 'classInfoCount', 'indexOfConstructor',
  'indexOfMethod', 'indexOfSignal', 'indexOfSlot', 'indexOfEnumerator',
  'indexOfProperty', 'indexOfClassInfo', 'constructor', 'method',
  'enumerator', 'property', 'userProperty', 'checkConnectArgs',
  'normalizedSignature', 'normalizedType', 'disconnect', 'disconnectOne',
  'connectSlotsByName', 'invokeMethod', 'newInstance'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QObject *QMetaObject::cast(const QObject *obj) const': takes
    in Python what 'QObject *QMetaObject::cast(QObject *obj) const' takes.
  - Qt's 'QMetaClassInfo QMetaObject::classInfo(int index) const': gives
    'QMetaClassInfo', which has no cute class yet.
  - Qt's 'Connection QMetaObject::connect(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index, int type, int
    *types)': takes a number to change where it is.
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
  Connection = QMetaObjectConnection

  #  The enums Qt writes inside QMetaObject, and the names Qt has for the
  #  combinations of its flags enums.
  Call = QMetaObjectCall

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
    from . import QByteArray
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
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QObject, int, QObject, int)
  @overload(QObject, int, NoneType, int)
  @overload(NoneType, int, QObject, int)
  @overload(NoneType, int, NoneType, int)
  def disconnect(
      sender: Optional[QObject],
      signal_index: int,
      receiver: Optional[QObject],
      method_index: int,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::disconnect(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#disconnect

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal_index : int
      Passed on as it is.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
  @overload(QObject, int, NoneType, int)
  @overload(NoneType, int, QObject, int)
  @overload(NoneType, int, NoneType, int)
  def disconnectOne(
      sender: Optional[QObject],
      signal_index: int,
      receiver: Optional[QObject],
      method_index: int,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::disconnectOne(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#disconnectOne

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal_index : int
      Passed on as it is.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
  @overload(NoneType)
  def connectSlotsByName(o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMetaObject::connectSlotsByName(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobject.html#connectSlotsByName

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObject::connectSlotsByName(QObject *o)
    Rituals.call(
        'ritual_ZN11QMetaObject18connectSlotsByNameEP7QObject',
        CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(
      QObject, str, Qt.ConnectionType, QGenericReturnArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument,
  )
  @overload(
      QObject, NoneType, Qt.ConnectionType, QGenericReturnArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, str, Qt.ConnectionType, QGenericReturnArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, NoneType, Qt.ConnectionType, QGenericReturnArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument,
  )
  def invokeMethod(
      obj: Optional[QObject],
      member: Optional[str],
      a2: Qt.ConnectionType,
      ret: QGenericReturnArgument,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char
    *member, Qt::ConnectionType a2, QGenericReturnArgument ret,
    QGenericArgument val0, QGenericArgument val1, QGenericArgument val2,
    QGenericArgument val3, QGenericArgument val4, QGenericArgument val5,
    QGenericArgument val6, QGenericArgument val7, QGenericArgument val8,
    QGenericArgument val9)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#invokeMethod

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a2 : Qt.ConnectionType
      Passed on as its number.

    ret : QGenericReturnArgument
      Passed on as a value: Qt reads the C++ QGenericReturnArgument, which
      stays Python's own.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    #      Qt::ConnectionType a2, QGenericReturnArgument ret,
    #      QGenericArgument val0, QGenericArgument val1, QGenericArgument
    #      val2, QGenericArgument val3, QGenericArgument val4,
    #      QGenericArgument val5, QGenericArgument val6, QGenericArgument
    #      val7, QGenericArgument val8, QGenericArgument val9)
    return Rituals.call(
        'ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKcN2Qt14ConnectionT'
        'ypeE22QGenericReturnArgument16QGenericArgumentS7_S7_S7_S7_S7_S7_S7'
        '_S7_S7_',
        CuteMixin._addressOf(obj), CuteMixin._bytesOf(member), a2.value,
        CuteMixin._valueOf(ret), CuteMixin._valueOf(val0),
        CuteMixin._valueOf(val1), CuteMixin._valueOf(val2),
        CuteMixin._valueOf(val3), CuteMixin._valueOf(val4),
        CuteMixin._valueOf(val5), CuteMixin._valueOf(val6),
        CuteMixin._valueOf(val7), CuteMixin._valueOf(val8),
        CuteMixin._valueOf(val9),
    )

  @staticmethod
  @overload(
      QObject, str, QGenericReturnArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  @overload(
      QObject, NoneType, QGenericReturnArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  @overload(
      NoneType, str, QGenericReturnArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  @overload(
      NoneType, NoneType, QGenericReturnArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  def invokeMethod(
      obj: Optional[QObject],
      member: Optional[str],
      ret: QGenericReturnArgument,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char
    *member, QGenericReturnArgument ret, QGenericArgument val0,
    QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
    QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
    QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#invokeMethod

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    ret : QGenericReturnArgument
      Passed on as a value: Qt reads the C++ QGenericReturnArgument, which
      stays Python's own.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    #      QGenericReturnArgument ret, QGenericArgument val0,
    #      QGenericArgument val1, QGenericArgument val2, QGenericArgument
    #      val3, QGenericArgument val4, QGenericArgument val5,
    #      QGenericArgument val6, QGenericArgument val7, QGenericArgument
    #      val8, QGenericArgument val9)
    return Rituals.call(
        'ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKc22QGenericReturnA'
        'rgument16QGenericArgumentS5_S5_S5_S5_S5_S5_S5_S5_S5_',
        CuteMixin._addressOf(obj), CuteMixin._bytesOf(member),
        CuteMixin._valueOf(ret), CuteMixin._valueOf(val0),
        CuteMixin._valueOf(val1), CuteMixin._valueOf(val2),
        CuteMixin._valueOf(val3), CuteMixin._valueOf(val4),
        CuteMixin._valueOf(val5), CuteMixin._valueOf(val6),
        CuteMixin._valueOf(val7), CuteMixin._valueOf(val8),
        CuteMixin._valueOf(val9),
    )

  @staticmethod
  @overload(
      QObject, str, Qt.ConnectionType, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      QObject, NoneType, Qt.ConnectionType, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  @overload(
      NoneType, str, Qt.ConnectionType, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, NoneType, Qt.ConnectionType, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  def invokeMethod(
      obj: Optional[QObject],
      member: Optional[str],
      type: Qt.ConnectionType,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char
    *member, Qt::ConnectionType type, QGenericArgument val0, QGenericArgument
    val1, QGenericArgument val2, QGenericArgument val3, QGenericArgument
    val4, QGenericArgument val5, QGenericArgument val6, QGenericArgument
    val7, QGenericArgument val8, QGenericArgument val9)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#invokeMethod

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    #      Qt::ConnectionType type, QGenericArgument val0, QGenericArgument
    #      val1, QGenericArgument val2, QGenericArgument val3,
    #      QGenericArgument val4, QGenericArgument val5, QGenericArgument
    #      val6, QGenericArgument val7, QGenericArgument val8,
    #      QGenericArgument val9)
    return Rituals.call(
        'ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKcN2Qt14ConnectionT'
        'ypeE16QGenericArgumentS6_S6_S6_S6_S6_S6_S6_S6_S6_',
        CuteMixin._addressOf(obj), CuteMixin._bytesOf(member), type.value,
        CuteMixin._valueOf(val0), CuteMixin._valueOf(val1),
        CuteMixin._valueOf(val2), CuteMixin._valueOf(val3),
        CuteMixin._valueOf(val4), CuteMixin._valueOf(val5),
        CuteMixin._valueOf(val6), CuteMixin._valueOf(val7),
        CuteMixin._valueOf(val8), CuteMixin._valueOf(val9),
    )

  @staticmethod
  @overload(
      QObject, str, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      QObject, NoneType, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, str, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, NoneType, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  def invokeMethod(
      obj: Optional[QObject],
      member: Optional[str],
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaObject::invokeMethod(QObject *obj, const char
    *member, QGenericArgument val0, QGenericArgument val1, QGenericArgument
    val2, QGenericArgument val3, QGenericArgument val4, QGenericArgument
    val5, QGenericArgument val6, QGenericArgument val7, QGenericArgument
    val8, QGenericArgument val9)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#invokeMethod

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
    #      QGenericArgument val0, QGenericArgument val1, QGenericArgument
    #      val2, QGenericArgument val3, QGenericArgument val4,
    #      QGenericArgument val5, QGenericArgument val6, QGenericArgument
    #      val7, QGenericArgument val8, QGenericArgument val9)
    return Rituals.call(
        'ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKc16QGenericArgumen'
        'tS4_S4_S4_S4_S4_S4_S4_S4_S4_',
        CuteMixin._addressOf(obj), CuteMixin._bytesOf(member),
        CuteMixin._valueOf(val0), CuteMixin._valueOf(val1),
        CuteMixin._valueOf(val2), CuteMixin._valueOf(val3),
        CuteMixin._valueOf(val4), CuteMixin._valueOf(val5),
        CuteMixin._valueOf(val6), CuteMixin._valueOf(val7),
        CuteMixin._valueOf(val8), CuteMixin._valueOf(val9),
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
  @overload(NoneType)
  def cast(self, obj: Optional[QObject]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMetaObject::cast(QObject *obj) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#cast

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
    from . import QObject
    return QObject._cuteAt(address)

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

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaObject::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaObject::metaType() const
    address = self.uglySide.call('ritual_ZNK11QMetaObject8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

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
    from . import QMetaMethod
    return QMetaMethod._cuteOwning(address)

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
    from . import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  @overload(int)
  def enumerator(self, index: int) -> QMetaEnum:
    """
    Calls Qt's 'QMetaEnum QMetaObject::enumerator(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#enumerator

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaEnum
      A new cute QMetaEnum around the copy Qt gave back. Python owns it.
    """
    #  QMetaEnum QMetaObject::enumerator(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaObject10enumeratorEi', index,
    )
    from . import QMetaEnum
    return QMetaEnum._cuteOwning(address)

  @overload(int)
  def property(self, index: int) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QMetaObject::property(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QMetaObject::property(int index) const
    address = self.uglySide.call('ritual_ZNK11QMetaObject8propertyEi', index)
    from . import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  def userProperty(self) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QMetaObject::userProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#userProperty

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QMetaObject::userProperty() const
    address = self.uglySide.call('ritual_ZNK11QMetaObject12userPropertyEv')
    from . import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  @overload(
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument,
  )
  def newInstance(
      self,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QMetaObject::newInstance(QGenericArgument val0,
    QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
    QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
    QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobject.html#newInstance

    Parameters
    ----------

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QMetaObject::newInstance(QGenericArgument val0,
    #      QGenericArgument val1, QGenericArgument val2, QGenericArgument
    #      val3, QGenericArgument val4, QGenericArgument val5,
    #      QGenericArgument val6, QGenericArgument val7, QGenericArgument
    #      val8, QGenericArgument val9) const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaObject11newInstanceE16QGenericArgumentS0_S0_S0_S0'
        '_S0_S0_S0_S0_S0_',
        self._valueOf(val0), self._valueOf(val1), self._valueOf(val2),
        self._valueOf(val3), self._valueOf(val4), self._valueOf(val5),
        self._valueOf(val6), self._valueOf(val7), self._valueOf(val8),
        self._valueOf(val9),
    )
    from . import QObject
    return QObject._cuteAt(address)

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
