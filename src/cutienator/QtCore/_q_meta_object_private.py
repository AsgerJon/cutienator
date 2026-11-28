"""
QMetaObjectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMetaObjectPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArrayView, QMetaMethod, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QMetaMethod = WAIT['QMetaMethod']
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaObjectPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaObjectPrivate: a plain Python object standing in
  front of one C++ QMetaObjectPrivate.

  C++ hands a QMetaObjectPrivate around as a copy, so every C++
  QMetaObjectPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaObjectPrivate that has a ritual and that Python
  can call so far, 8 names in all: 'get', 'originalClone',
  'indexOfEnumerator', 'signal', 'signalOffset', 'absoluteSignalCount',
  'signalIndex', 'firstMethod'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QMetaObjectPrivate::checkConnectArgs(QSpan<const
    QArgumentType> signalTypes, QSpan<const QArgumentType> methodTypes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QByteArrayView
    QMetaObjectPrivate::parameterTypeNamesFromSignature(QByteArrayView
    signature, QVarLengthArray<QByteArrayView, 10> &typeNames)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QMetaObjectPrivate::memberIndexes(const QObject *obj, const
    QMetaMethod &member, int *signalIndex, int *methodIndex)': takes a number
    to change where it is.
  - Qt's 'QMetaObjectPrivate::~QMetaObjectPrivate()': the destructor: Python
    removes its C++ QMetaObjectPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  15 of the 27 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 6 leans on
  'QMetaObjectPrivate; 1 the compiler refuses its ritual as it would be
  written here; 1 leans on 'qMetaTypeTypeInternal(QByteArrayView)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QMetaObjectPrivate is created at the first use, not by
    'QMetaObjectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaObjectPrivate back gives a copy the ritual made
    for Python, in a new cute QMetaObjectPrivate.
  - Each name of Qt's QMetaObjectPrivate that has no cute function yet,
    'checkConnectArgs', 'connect', 'decodeMethodSignature', 'disconnect',
    'disconnectHelper', 'indexOfConstructor', 'indexOfMethod',
    'indexOfMethodRelative', 'indexOfSignal', 'indexOfSignalRelative',
    'indexOfSlot', 'indexOfSlotRelative', 'memberIndexes', 'methodMatch',
    'normalizedSignature', 'parameterTypeNamesFromSignature', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMetaObjectPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DisconnectType(CuteNum):
    """
    The enum 'QMetaObjectPrivate::DisconnectType' of Qt, with the 2 names Qt
    gives in it.
    """

    DisconnectAll = Kee[int](0)
    DisconnectOne = Kee[int](1)

  class Which(CuteNum, scoped=True):
    """
    The enum 'QMetaObjectPrivate::Which' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Name = Kee[int](0)
    Alias = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def get(metaobject: Optional[QMetaObject]) -> Optional[QMetaObjectPrivate]:
    """
    Calls Qt's 'const QMetaObjectPrivate *QMetaObjectPrivate::get(const
    QMetaObject *metaobject)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectprivate.html#get

    Parameters
    ----------

    metaobject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObjectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObjectPrivate *QMetaObjectPrivate::get(const QMetaObject
    #      *metaobject)
    address = Rituals.call(
        'ritual_ZN18QMetaObjectPrivate3getEPK11QMetaObject',
        CuteMixin._addressOf(metaobject, 'QMetaObject'),
    )
    return QMetaObjectPrivate._cuteAt(address)

  @staticmethod
  @overload(QMetaObject, int)
  @overload(NoneType, int)
  def originalClone(
      obj: Optional[QMetaObject],
      local_method_index: int,
  ) -> int:
    """
    Calls Qt's 'int QMetaObjectPrivate::originalClone(const QMetaObject *obj,
    int local_method_index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectprivate.html#originalClone

    Parameters
    ----------

    obj : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    local_method_index : int
      Passed on as it is.
    """
    #  int QMetaObjectPrivate::originalClone(const QMetaObject *obj, int
    #      local_method_index)
    return Rituals.call(
        'ritual_ZN18QMetaObjectPrivate13originalCloneEPK11QMetaObjecti',
        CuteMixin._addressOf(obj, 'QMetaObject'), local_method_index,
    )

  @staticmethod
  @overload(QMetaObject, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def indexOfEnumerator(
      m: Optional[QMetaObject],
      name: QByteArrayView,
  ) -> int:
    """
    Calls Qt's 'int QMetaObjectPrivate::indexOfEnumerator(const QMetaObject
    *m, QByteArrayView name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectprivate.html#indexOfEnumerator

    Parameters
    ----------

    m : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  int QMetaObjectPrivate::indexOfEnumerator(const QMetaObject *m,
    #      QByteArrayView name)
    return Rituals.call(
        'ritual_ZN18QMetaObjectPrivate17indexOfEnumeratorEPK11QMetaObject14'
        'QByteArrayView',
        CuteMixin._addressOf(m, 'QMetaObject'), CuteMixin._valueOf(name),
    )

  @staticmethod
  @overload(QMetaObject, int)
  @overload(NoneType, int)
  def signal(m: Optional[QMetaObject], signal_index: int) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QMetaObjectPrivate::signal(const QMetaObject *m,
    int signal_index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectprivate.html#signal

    Parameters
    ----------

    m : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal_index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QMetaObjectPrivate::signal(const QMetaObject *m, int
    #      signal_index)
    address = Rituals.call(
        'ritual_ZN18QMetaObjectPrivate6signalEPK11QMetaObjecti',
        CuteMixin._addressOf(m, 'QMetaObject'), signal_index,
    )
    from . import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def signalOffset(m: Optional[QMetaObject]) -> int:
    """
    Calls Qt's 'int QMetaObjectPrivate::signalOffset(const QMetaObject *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectprivate.html#signalOffset

    Parameters
    ----------

    m : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QMetaObjectPrivate::signalOffset(const QMetaObject *m)
    return Rituals.call(
        'ritual_ZN18QMetaObjectPrivate12signalOffsetEPK11QMetaObject',
        CuteMixin._addressOf(m, 'QMetaObject'),
    )

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def absoluteSignalCount(m: Optional[QMetaObject]) -> int:
    """
    Calls Qt's 'int QMetaObjectPrivate::absoluteSignalCount(const QMetaObject
    *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectprivate.html#absoluteSignalCount

    Parameters
    ----------

    m : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QMetaObjectPrivate::absoluteSignalCount(const QMetaObject *m)
    return Rituals.call(
        'ritual_ZN18QMetaObjectPrivate19absoluteSignalCountEPK11QMetaObject',
        CuteMixin._addressOf(m, 'QMetaObject'),
    )

  @staticmethod
  @overload(QMetaMethod)
  def signalIndex(m: QMetaMethod) -> int:
    """
    Calls Qt's 'int QMetaObjectPrivate::signalIndex(const QMetaMethod &m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectprivate.html#signalIndex

    Parameters
    ----------

    m : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  int QMetaObjectPrivate::signalIndex(const QMetaMethod &m)
    return Rituals.call(
        'ritual_ZN18QMetaObjectPrivate11signalIndexERK11QMetaMethod',
        CuteMixin._valueOf(m),
    )

  @staticmethod
  @overload(QMetaObject, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def firstMethod(
      baseObject: Optional[QMetaObject],
      name: QByteArrayView,
  ) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QMetaObjectPrivate::firstMethod(const QMetaObject
    *baseObject, QByteArrayView name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectprivate.html#firstMethod

    Parameters
    ----------

    baseObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QMetaObjectPrivate::firstMethod(const QMetaObject
    #      *baseObject, QByteArrayView name)
    address = Rituals.call(
        'ritual_ZN18QMetaObjectPrivate11firstMethodEPK11QMetaObject14QByteA'
        'rrayView',
        CuteMixin._addressOf(baseObject, 'QMetaObject'),
        CuteMixin._valueOf(name),
    )
    from . import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaObjectPrivate'

  #  Qt's '~QMetaObjectPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaObjectPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMetaObjectPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def checkConnectArgs(*__, **_) -> Never:
    """
    - Qt's 'bool QMetaObjectPrivate::checkConnectArgs(QSpan<const
      QArgumentType> signalTypes, QSpan<const QArgumentType> methodTypes)':
      takes a type Python has no way to hand over yet.
    - Qt's 'bool QMetaObjectPrivate::checkConnectArgs(const
      QMetaMethodPrivate *signal, const QMetaMethodPrivate *method)': the
      compiler refuses its ritual as it would be written here: function
      'QMetaObjectPrivate::checkConnectArgs' is used but not defined in this
      translation unit, and cannot be defined in any other translation unit
      because its type does not have linkage.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.checkConnectArgs' has no cute function yet. "
        "Qt's 'bool QMetaObjectPrivate::checkConnectArgs(QSpan<const "
        "QArgumentType> signalTypes, QSpan<const QArgumentType> "
        "methodTypes)': takes a type Python has no way to hand over yet. "
        "Qt's 'bool QMetaObjectPrivate::checkConnectArgs(const "
        "QMetaMethodPrivate *signal, const QMetaMethodPrivate *method)': "
        "the compiler refuses its ritual as it would be written here: "
        "function 'QMetaObjectPrivate::checkConnectArgs' is used but not "
        "defined in this translation unit, and cannot be defined in any "
        "other translation unit because its type does not have linkage.")

  @staticmethod
  def connect(*__, **_) -> Never:
    """
    Qt's 'QObjectPrivate::Connection *QMetaObjectPrivate::connect(const
    QObject *sender, int signal_index, const QMetaObject *smeta, const
    QObject *receiver, int method_index_relative, const QMetaObject *rmeta,
    int type, int *types)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'signalSlotLock'.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.connect' has no cute function yet. Qt's "
        "'QObjectPrivate::Connection *QMetaObjectPrivate::connect(const "
        "QObject *sender, int signal_index, const QMetaObject *smeta, const "
        "QObject *receiver, int method_index_relative, const QMetaObject "
        "*rmeta, int type, int *types)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'signalSlotLock'.")

  @staticmethod
  def decodeMethodSignature(*__, **_) -> Never:
    """
    Qt's 'QByteArrayView
    QMetaObjectPrivate::decodeMethodSignature(QByteArrayView signature,
    QArgumentTypeArray &types)': leans on
    'qMetaTypeTypeInternal(QByteArrayView)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.decodeMethodSignature' has no cute function "
        "yet. Qt's 'QByteArrayView "
        "QMetaObjectPrivate::decodeMethodSignature(QByteArrayView "
        "signature, QArgumentTypeArray &types)': leans on "
        "'qMetaTypeTypeInternal(QByteArrayView)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def disconnect(*__, **_) -> Never:
    """
    Qt's 'bool QMetaObjectPrivate::disconnect(const QObject *sender, int
    signal_index, const QMetaObject *smeta, const QObject *receiver, int
    method_index, void **slot, DisconnectType a6)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'signalSlotLock'.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.disconnect' has no cute function yet. Qt's "
        "'bool QMetaObjectPrivate::disconnect(const QObject *sender, int "
        "signal_index, const QMetaObject *smeta, const QObject *receiver, "
        "int method_index, void **slot, DisconnectType a6)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'signalSlotLock'."
    )

  @staticmethod
  def disconnectHelper(*__, **_) -> Never:
    """
    Qt's 'bool
    QMetaObjectPrivate::disconnectHelper(QObjectPrivate::ConnectionData
    *connections, int signalIndex, const QObject *receiver, int method_index,
    void **slot, QBasicMutex *senderMutex, DisconnectType a6)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'signalSlotLock'.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.disconnectHelper' has no cute function yet. "
        "Qt's 'bool "
        "QMetaObjectPrivate::disconnectHelper(QObjectPrivate::ConnectionData"
        " *connections, int signalIndex, const QObject *receiver, int "
        "method_index, void **slot, QBasicMutex *senderMutex, "
        "DisconnectType a6)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'signalSlotLock'.")

  @staticmethod
  def indexOfConstructor(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfConstructor(const QMetaObject *m,
    QByteArrayView name, QSpan<const QArgumentType> types)': leans on
    'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod const&,
    QByteArrayView, QSpan<QArgumentType const, 18446744073709551615ul>)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfConstructor' has no cute function yet. "
        "Qt's 'int QMetaObjectPrivate::indexOfConstructor(const QMetaObject "
        "*m, QByteArrayView name, QSpan<const QArgumentType> types)': leans "
        "on 'QMetaObjectPrivate::methodMatch(QMetaObject const*, "
        "QMetaMethod const&, QByteArrayView, QSpan<QArgumentType const, "
        "18446744073709551615ul>)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def indexOfMethod(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfMethod(const QMetaObject *m,
    QByteArrayView name, QSpan<const QArgumentType> types)': leans on
    'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod const&,
    QByteArrayView, QSpan<QArgumentType const, 18446744073709551615ul>)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfMethod' has no cute function yet. Qt's "
        "'int QMetaObjectPrivate::indexOfMethod(const QMetaObject *m, "
        "QByteArrayView name, QSpan<const QArgumentType> types)': leans on "
        "'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod "
        "const&, QByteArrayView, QSpan<QArgumentType const, "
        "18446744073709551615ul>)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def indexOfMethodRelative(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfMethodRelative(const QMetaObject
    **baseObject, QByteArrayView name, QSpan<const QArgumentType> types,
    QMetaMethod::MethodType what)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'priv'.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfMethodRelative' has no cute function "
        "yet. Qt's 'int QMetaObjectPrivate::indexOfMethodRelative(const "
        "QMetaObject **baseObject, QByteArrayView name, QSpan<const "
        "QArgumentType> types, QMetaMethod::MethodType what)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'priv'.")

  @staticmethod
  def indexOfSignal(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfSignal(const QMetaObject *m,
    QByteArrayView name, QSpan<const QArgumentType> types)': leans on
    'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod const&,
    QByteArrayView, QSpan<QArgumentType const, 18446744073709551615ul>)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfSignal' has no cute function yet. Qt's "
        "'int QMetaObjectPrivate::indexOfSignal(const QMetaObject *m, "
        "QByteArrayView name, QSpan<const QArgumentType> types)': leans on "
        "'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod "
        "const&, QByteArrayView, QSpan<QArgumentType const, "
        "18446744073709551615ul>)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def indexOfSignalRelative(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfSignalRelative(const QMetaObject
    **baseObject, QByteArrayView name, QSpan<const QArgumentType> types)':
    leans on 'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod
    const&, QByteArrayView, QSpan<QArgumentType const,
    18446744073709551615ul>)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfSignalRelative' has no cute function "
        "yet. Qt's 'int QMetaObjectPrivate::indexOfSignalRelative(const "
        "QMetaObject **baseObject, QByteArrayView name, QSpan<const "
        "QArgumentType> types)': leans on "
        "'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod "
        "const&, QByteArrayView, QSpan<QArgumentType const, "
        "18446744073709551615ul>)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def indexOfSlot(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfSlot(const QMetaObject *m,
    QByteArrayView name, QSpan<const QArgumentType> types)': leans on
    'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod const&,
    QByteArrayView, QSpan<QArgumentType const, 18446744073709551615ul>)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfSlot' has no cute function yet. Qt's "
        "'int QMetaObjectPrivate::indexOfSlot(const QMetaObject *m, "
        "QByteArrayView name, QSpan<const QArgumentType> types)': leans on "
        "'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod "
        "const&, QByteArrayView, QSpan<QArgumentType const, "
        "18446744073709551615ul>)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def indexOfSlotRelative(*__, **_) -> Never:
    """
    Qt's 'int QMetaObjectPrivate::indexOfSlotRelative(const QMetaObject **m,
    QByteArrayView name, QSpan<const QArgumentType> types)': leans on
    'QMetaObjectPrivate::methodMatch(QMetaObject const*, QMetaMethod const&,
    QByteArrayView, QSpan<QArgumentType const, 18446744073709551615ul>)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.indexOfSlotRelative' has no cute function yet. "
        "Qt's 'int QMetaObjectPrivate::indexOfSlotRelative(const "
        "QMetaObject **m, QByteArrayView name, QSpan<const QArgumentType> "
        "types)': leans on 'QMetaObjectPrivate::methodMatch(QMetaObject "
        "const*, QMetaMethod const&, QByteArrayView, QSpan<QArgumentType "
        "const, 18446744073709551615ul>)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def memberIndexes(*__, **_) -> Never:
    """
    Qt's 'void QMetaObjectPrivate::memberIndexes(const QObject *obj, const
    QMetaMethod &member, int *signalIndex, int *methodIndex)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.memberIndexes' has no cute function yet. Qt's "
        "'void QMetaObjectPrivate::memberIndexes(const QObject *obj, const "
        "QMetaMethod &member, int *signalIndex, int *methodIndex)': takes a "
        "number to change where it is.")

  @staticmethod
  def methodMatch(*__, **_) -> Never:
    """
    Qt's 'bool QMetaObjectPrivate::methodMatch(const QMetaObject *m, const
    QMetaMethod &method, QByteArrayView name, QSpan<const QArgumentType>
    types)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: incomplete type '(anonymous
    namespace)::QMetaMethodPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.methodMatch' has no cute function yet. Qt's "
        "'bool QMetaObjectPrivate::methodMatch(const QMetaObject *m, const "
        "QMetaMethod &method, QByteArrayView name, QSpan<const "
        "QArgumentType> types)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: "
        "incomplete type '(anonymous namespace)::QMetaMethodPrivate' named "
        "in nested name specifier.")

  @staticmethod
  def normalizedSignature(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMetaObjectPrivate::normalizedSignature(QByteArrayView
    method)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'trimSpacesFromLeft'.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.normalizedSignature' has no cute function yet. "
        "Qt's 'QByteArray "
        "QMetaObjectPrivate::normalizedSignature(QByteArrayView method)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'trimSpacesFromLeft'.")

  @staticmethod
  def parameterTypeNamesFromSignature(*__, **_) -> Never:
    """
    Qt's 'QByteArrayView
    QMetaObjectPrivate::parameterTypeNamesFromSignature(QByteArrayView
    signature, QVarLengthArray<QByteArrayView, 10> &typeNames)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMetaObjectPrivate.parameterTypeNamesFromSignature' has no cute "
        "function yet. Qt's 'QByteArrayView "
        "QMetaObjectPrivate::parameterTypeNamesFromSignature(QByteArrayView "
        "signature, QVarLengthArray<QByteArrayView, 10> &typeNames)': takes "
        "a type Python has no way to hand over yet.")
