"""
QGrpcOperationContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcoperationcontext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QLatin1String, QMetaObject
  from ..QtCore import QMetaType
  from . import QGrpcCallOptions, QGrpcOperationContextPrivate, QGrpcStatus
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QGrpcStatus = WAIT['QGrpcStatus']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGrpcOperationContext(QObject):
  """
  The cute side of Qt's QGrpcOperationContext: a plain Python object standing
  in front of one C++ QGrpcOperationContext.

  It is built on the cute 'QObject', as Qt's QGrpcOperationContext is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcOperationContext that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'method',
  'service', 'descriptor', 'callOptions', 'responseMetaType',
  'setResponseMetaType', 'operationId', 'finished', 'messageReceived',
  'cancelRequested', 'writeMessageRequested', 'writesDoneRequested',
  'd_func', 'event'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGrpcOperationContext::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGrpcOperationContext::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGrpcOperationContext::QGrpcOperationContext(QtGrpc::RpcDescriptor
    description, const QGrpcCallOptions &options,
    std::shared_ptr<QAbstractProtobufSerializer> serializer, QGrpcOperation
    *parent, PrivateConstructor a4)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QGrpcOperationContext::~QGrpcOperationContext()': the destructor:
    Python never removes a C++ QGrpcOperationContext.
  - Qt's 'const QHash<QByteArray, QByteArray>
    &QGrpcOperationContext::serverMetadata() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QGrpcOperationContext::setServerMetadata(const
    QHash<QByteArray, QByteArray> &metadata)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QGrpcOperationContext::setServerMetadata(QHash<QByteArray,
    QByteArray> &&metadata)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperationContext::serverInitialMetadata() const': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QGrpcOperationContext::setServerInitialMetadata(QMultiHash<QByteArray,
    QByteArray> &&metadata)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperationContext::serverTrailingMetadata() const': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QGrpcOperationContext::setServerTrailingMetadata(QMultiHash<QByteArray,
    QByteArray> &&metadata)': takes a type Python has no way to hand over
    yet.
  - Qt's 'std::shared_ptr<const QAbstractProtobufSerializer>
    QGrpcOperationContext::serializer() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QGrpcOperationContext::serverInitialMetadataReceived(const
    QMultiHash<QByteArray, QByteArray> &metadata, QPrivateSignal a1)': takes
    a type Python has no way to hand over yet.
  - Qt's 'const QGrpcOperationContextPrivate *QGrpcOperationContext::d_func()
    const': takes in Python what 'QGrpcOperationContextPrivate
    *QGrpcOperationContext::d_func()' takes.
  - Qt's 'const QGrpcOperation &QGrpcOperationContext::operation() const':
    gives a type Python has no way to take yet.
  - Qt's 'QGrpcOperation &QGrpcOperationContext::operation()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  11 of the 43 functions Qt declares: 9 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QGrpcOperationContext is created at the first use, not by
    'QGrpcOperationContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcOperationContext.
  - Qt tells when it has removed the C++ QGrpcOperationContext. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGrpcOperationContext that has no cute function yet,
    '__init__', 'operation', 'serializer', 'serverInitialMetadata',
    'serverInitialMetadataReceived', 'serverMetadata',
    'serverTrailingMetadata', 'setServerInitialMetadata',
    'setServerMetadata', 'setServerTrailingMetadata', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QGrpcOperationContext::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationcontext.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGrpcOperationContext::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QGrpcOperationContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcOperationContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGrpcOperationContext::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGrpcOperationContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QGrpcOperationContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def method(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QGrpcOperationContext::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationcontext.html#method

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QGrpcOperationContext::method() const
    address = self.uglySide.call(
        'ritual_ZNK21QGrpcOperationContext6methodEv',
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def service(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QGrpcOperationContext::service() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationcontext.html#service

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QGrpcOperationContext::service() const
    address = self.uglySide.call(
        'ritual_ZNK21QGrpcOperationContext7serviceEv',
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def descriptor(self) -> QtGrpc.RpcDescriptor:
    """
    Calls Qt's 'QtGrpc::RpcDescriptor QGrpcOperationContext::descriptor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#descriptor

    Returns
    -------

    QtGrpc.RpcDescriptor
      A new cute QtGrpc::RpcDescriptor around the copy Qt gave back. Python
      owns it.
    """
    #  QtGrpc::RpcDescriptor QGrpcOperationContext::descriptor() const
    address = self.uglySide.call(
        'ritual_ZNK21QGrpcOperationContext10descriptorEv',
    )
    return QtGrpc.RpcDescriptor._cuteOwning(address)

  def callOptions(self) -> QGrpcCallOptions:
    """
    Calls Qt's 'const QGrpcCallOptions &QGrpcOperationContext::callOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#callOptions

    Returns
    -------

    QGrpcCallOptions
      A new cute QGrpcCallOptions around the copy Qt gave back. Python owns
      it.
    """
    #  const QGrpcCallOptions &QGrpcOperationContext::callOptions() const
    address = self.uglySide.call(
        'ritual_ZNKR21QGrpcOperationContext11callOptionsEv',
    )
    from . import QGrpcCallOptions
    return QGrpcCallOptions._cuteOwning(address)

  def responseMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QGrpcOperationContext::responseMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#responseMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QGrpcOperationContext::responseMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK21QGrpcOperationContext16responseMetaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def operationId(self) -> int:
    """
    Calls Qt's 'quint64 QGrpcOperationContext::operationId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#operationId
    """
    #  quint64 QGrpcOperationContext::operationId() const
    return self.uglySide.call(
        'ritual_ZNK21QGrpcOperationContext11operationIdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMetaType)
  def setResponseMetaType(self, metaType: QMetaType) -> None:
    """
    Calls Qt's 'void QGrpcOperationContext::setResponseMetaType(QMetaType
    metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#setResponseMetaType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QGrpcOperationContext::setResponseMetaType(QMetaType metaType)
    self.uglySide.call(
        'ritual_ZN21QGrpcOperationContext19setResponseMetaTypeE9QMetaType',
        self._valueOf(metaType),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGrpcOperationContext::QGrpcOperationContext(QtGrpc::RpcDescriptor
    description, const QGrpcCallOptions &options,
    std::shared_ptr<QAbstractProtobufSerializer> serializer, QGrpcOperation
    *parent, PrivateConstructor a4)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.__init__' has no cute function yet. Qt's "
        "'QGrpcOperationContext::QGrpcOperationContext(QtGrpc::RpcDescriptor"
        " description, const QGrpcCallOptions &options, "
        "std::shared_ptr<QAbstractProtobufSerializer> serializer, "
        "QGrpcOperation *parent, PrivateConstructor a4)': takes a type "
        "Python has no way to hand over yet.")

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

  @overload(QGrpcStatus)
  def finished(self, status: QGrpcStatus) -> None:
    """
    Calls Qt's 'void QGrpcOperationContext::finished(const QGrpcStatus
    &status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#finished

    Parameters
    ----------

    status : QGrpcStatus
      Passed on as a value: Qt reads the C++ QGrpcStatus, which stays
      Python's own.
    """
    #  void QGrpcOperationContext::finished(const QGrpcStatus &status)
    self.uglySide.call(
        'ritual_ZN21QGrpcOperationContext8finishedERK11QGrpcStatus',
        self._valueOf(status),
    )

  @overload(QByteArray)
  def messageReceived(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QGrpcOperationContext::messageReceived(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#messageReceived

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QGrpcOperationContext::messageReceived(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN21QGrpcOperationContext15messageReceivedERK10QByteArray',
        self._valueOf(data),
    )

  def cancelRequested(self) -> None:
    """
    Calls Qt's 'void QGrpcOperationContext::cancelRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#cancelRequested
    """
    #  void QGrpcOperationContext::cancelRequested()
    self.uglySide.call('ritual_ZN21QGrpcOperationContext15cancelRequestedEv')

  @overload(QByteArray)
  def writeMessageRequested(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QGrpcOperationContext::writeMessageRequested(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#writeMessageRequested

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QGrpcOperationContext::writeMessageRequested(const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN21QGrpcOperationContext21writeMessageRequestedERK10QByteA'
        'rray',
        self._valueOf(data),
    )

  def writesDoneRequested(self) -> None:
    """
    Calls Qt's 'void QGrpcOperationContext::writesDoneRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontext.html#writesDoneRequested
    """
    #  void QGrpcOperationContext::writesDoneRequested()
    self.uglySide.call(
        'ritual_ZN21QGrpcOperationContext19writesDoneRequestedEv',
    )

  def d_func(self) -> Optional[QGrpcOperationContextPrivate]:
    """
    Calls Qt's 'QGrpcOperationContextPrivate
    *QGrpcOperationContext::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationcontext.html#d_func

    Returns
    -------

    Optional[QGrpcOperationContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGrpcOperationContextPrivate *QGrpcOperationContext::d_func()
    address = self.uglySide.call('ritual_ZN21QGrpcOperationContext6d_funcEv')
    from . import QGrpcOperationContextPrivate
    return QGrpcOperationContextPrivate._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGrpcOperationContext::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationcontext.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGrpcOperationContext::event(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN21QGrpcOperationContext5eventEP6QEvent',
        self._addressOf(event),
    )

  @staticmethod
  def operation(*__, **_) -> Never:
    """
    - Qt's 'const QGrpcOperation &QGrpcOperationContext::operation() const':
      gives a type Python has no way to take yet.
    - Qt's 'QGrpcOperation &QGrpcOperationContext::operation()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.operation' has no cute function yet. Qt's "
        "'const QGrpcOperation &QGrpcOperationContext::operation() const': "
        "gives a type Python has no way to take yet. Qt's 'QGrpcOperation "
        "&QGrpcOperationContext::operation()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def serializer(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<const QAbstractProtobufSerializer>
    QGrpcOperationContext::serializer() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.serializer' has no cute function yet. Qt's "
        "'std::shared_ptr<const QAbstractProtobufSerializer> "
        "QGrpcOperationContext::serializer() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def serverInitialMetadata(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperationContext::serverInitialMetadata() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.serverInitialMetadata' has no cute function "
        "yet. Qt's 'const QMultiHash<QByteArray, QByteArray> "
        "&QGrpcOperationContext::serverInitialMetadata() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def serverInitialMetadataReceived(*__, **_) -> Never:
    """
    Qt's 'void QGrpcOperationContext::serverInitialMetadataReceived(const
    QMultiHash<QByteArray, QByteArray> &metadata, QPrivateSignal a1)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.serverInitialMetadataReceived' has no cute "
        "function yet. Qt's 'void "
        "QGrpcOperationContext::serverInitialMetadataReceived(const "
        "QMultiHash<QByteArray, QByteArray> &metadata, QPrivateSignal a1)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def serverMetadata(*__, **_) -> Never:
    """
    Qt's 'const QHash<QByteArray, QByteArray>
    &QGrpcOperationContext::serverMetadata() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.serverMetadata' has no cute function yet. "
        "Qt's 'const QHash<QByteArray, QByteArray> "
        "&QGrpcOperationContext::serverMetadata() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def serverTrailingMetadata(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperationContext::serverTrailingMetadata() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.serverTrailingMetadata' has no cute "
        "function yet. Qt's 'const QMultiHash<QByteArray, QByteArray> "
        "&QGrpcOperationContext::serverTrailingMetadata() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setServerInitialMetadata(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcOperationContext::setServerInitialMetadata(QMultiHash<QByteArray,
    QByteArray> &&metadata)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.setServerInitialMetadata' has no cute "
        "function yet. Qt's 'void "
        "QGrpcOperationContext::setServerInitialMetadata(QMultiHash<QByteArr"
        "ay, QByteArray> &&metadata)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setServerMetadata(*__, **_) -> Never:
    """
    - Qt's 'void QGrpcOperationContext::setServerMetadata(const
      QHash<QByteArray, QByteArray> &metadata)': takes a type Python has no
      way to hand over yet.
    - Qt's 'void QGrpcOperationContext::setServerMetadata(QHash<QByteArray,
      QByteArray> &&metadata)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.setServerMetadata' has no cute function "
        "yet. Qt's 'void QGrpcOperationContext::setServerMetadata(const "
        "QHash<QByteArray, QByteArray> &metadata)': takes a type Python has "
        "no way to hand over yet. Qt's 'void "
        "QGrpcOperationContext::setServerMetadata(QHash<QByteArray, "
        "QByteArray> &&metadata)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setServerTrailingMetadata(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcOperationContext::setServerTrailingMetadata(QMultiHash<QByteArray,
    QByteArray> &&metadata)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContext.setServerTrailingMetadata' has no cute "
        "function yet. Qt's 'void "
        "QGrpcOperationContext::setServerTrailingMetadata(QMultiHash<QByteAr"
        "ray, QByteArray> &&metadata)': takes a type Python has no way to "
        "hand over yet.")
