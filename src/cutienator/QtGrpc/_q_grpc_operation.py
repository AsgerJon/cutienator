"""
QGrpcOperation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcoperation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QLatin1String, QMetaObject, QMetaType
  from ..QtProtobuf import QProtobufMessage
  from . import QGrpcOperationPrivate, QGrpcStatus
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QGrpcStatus = WAIT['QGrpcStatus']
  QProtobufMessage = WAIT['QProtobufMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGrpcOperation(QObject):
  """
  The cute side of Qt's QGrpcOperation: a plain Python object standing in
  front of one C++ QGrpcOperation.

  It is built on the cute 'QObject', as Qt's QGrpcOperation is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcOperation that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'read', 'method',
  'isFinished', 'responseMetaType', 'finished', 'cancel', 'writesDone',
  'd_func', 'event'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGrpcOperation::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QGrpcOperation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGrpcOperation::~QGrpcOperation()': the destructor: Python never
    removes a C++ QGrpcOperation.
  - Qt's 'const QHash<QByteArray, QByteArray> &QGrpcOperation::metadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperation::serverInitialMetadata() const': gives a type Python has
    no way to take yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperation::serverTrailingMetadata() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QGrpcOperation::serverInitialMetadataReceived(const
    QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QGrpcOperation::QGrpcOperation(QtGrpc::RpcDescriptor descriptor,
    const QGrpcCallOptions &options, std::weak_ptr<QAbstractGrpcChannel>
    &&channel)': takes a type Python has no way to hand over yet.
  - Qt's 'const QGrpcOperationContext &QGrpcOperation::context() const':
    gives a type Python has no way to take yet.
  - Qt's 'QGrpcOperationContext &QGrpcOperation::context()': gives a type
    Python has no way to take yet.
  - Qt's 'void QGrpcOperation::writeMessage(const QProtobufMessage
    &message)': takes a type Python has no way to hand over yet.
  - Qt's 'const QGrpcOperationPrivate *QGrpcOperation::d_func() const': takes
    in Python what 'QGrpcOperationPrivate *QGrpcOperation::d_func()' takes.

  What has no ritual
  ------------------

  11 of the 34 functions Qt declares: 8 forbidden; 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QGrpcOperation is created at the first use, not by
    'QGrpcOperation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcOperation.
  - Qt tells when it has removed the C++ QGrpcOperation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGrpcOperation that has no cute function yet,
    '__init__', 'context', 'metadata', 'serverInitialMetadata',
    'serverInitialMetadataReceived', 'serverTrailingMetadata',
    'writeMessage', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QGrpcOperation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#tr

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
    #  QString QGrpcOperation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QGrpcOperation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcOperation'

  #  A C++ QGrpcOperation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGrpcOperation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGrpcOperation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGrpcOperation::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QGrpcOperation10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QProtobufMessage)
  @overload(NoneType)
  def read(self, message: Optional[QProtobufMessage]) -> bool:
    """
    Calls Qt's 'bool QGrpcOperation::read(QProtobufMessage *message) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#read

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGrpcOperation::read(QProtobufMessage *message) const
    return self.uglySide.call(
        'ritual_ZNK14QGrpcOperation4readEP16QProtobufMessage',
        self._addressOf(message),
    )

  def method(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QGrpcOperation::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#method

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QGrpcOperation::method() const
    address = self.uglySide.call('ritual_ZNK14QGrpcOperation6methodEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QGrpcOperation::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#isFinished
    """
    #  bool QGrpcOperation::isFinished() const
    return self.uglySide.call('ritual_ZNK14QGrpcOperation10isFinishedEv')

  def responseMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QGrpcOperation::responseMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperation.html#responseMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QGrpcOperation::responseMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK14QGrpcOperation16responseMetaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGrpcOperation::QGrpcOperation(QtGrpc::RpcDescriptor descriptor,
    const QGrpcCallOptions &options, std::weak_ptr<QAbstractGrpcChannel>
    &&channel)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.__init__' has no cute function yet. Qt's "
        "'QGrpcOperation::QGrpcOperation(QtGrpc::RpcDescriptor descriptor, "
        "const QGrpcCallOptions &options, "
        "std::weak_ptr<QAbstractGrpcChannel> &&channel)': takes a type "
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
    Calls Qt's 'void QGrpcOperation::finished(const QGrpcStatus &status)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#finished

    Parameters
    ----------

    status : QGrpcStatus
      Passed on as a value: Qt reads the C++ QGrpcStatus, which stays
      Python's own.
    """
    #  void QGrpcOperation::finished(const QGrpcStatus &status)
    self.uglySide.call(
        'ritual_ZN14QGrpcOperation8finishedERK11QGrpcStatus',
        self._valueOf(status),
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QGrpcOperation::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#cancel
    """
    #  void QGrpcOperation::cancel()
    self.uglySide.call('ritual_ZN14QGrpcOperation6cancelEv')

  def writesDone(self) -> None:
    """
    Calls Qt's 'void QGrpcOperation::writesDone()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#writesDone
    """
    #  void QGrpcOperation::writesDone()
    self.uglySide.call('ritual_ZN14QGrpcOperation10writesDoneEv')

  def d_func(self) -> Optional[QGrpcOperationPrivate]:
    """
    Calls Qt's 'QGrpcOperationPrivate *QGrpcOperation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#d_func

    Returns
    -------

    Optional[QGrpcOperationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGrpcOperationPrivate *QGrpcOperation::d_func()
    address = self.uglySide.call('ritual_ZN14QGrpcOperation6d_funcEv')
    from . import QGrpcOperationPrivate
    return QGrpcOperationPrivate._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGrpcOperation::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperation.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGrpcOperation::event(QEvent *event)
    ritual = 'ritual_ZN14QGrpcOperation5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QGrpcOperation5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def context(*__, **_) -> Never:
    """
    - Qt's 'const QGrpcOperationContext &QGrpcOperation::context() const':
      gives a type Python has no way to take yet.
    - Qt's 'QGrpcOperationContext &QGrpcOperation::context()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.context' has no cute function yet. Qt's 'const "
        "QGrpcOperationContext &QGrpcOperation::context() const': gives a "
        "type Python has no way to take yet. Qt's 'QGrpcOperationContext "
        "&QGrpcOperation::context()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def metadata(*__, **_) -> Never:
    """
    Qt's 'const QHash<QByteArray, QByteArray> &QGrpcOperation::metadata()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.metadata' has no cute function yet. Qt's 'const "
        "QHash<QByteArray, QByteArray> &QGrpcOperation::metadata() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def serverInitialMetadata(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperation::serverInitialMetadata() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.serverInitialMetadata' has no cute function yet. "
        "Qt's 'const QMultiHash<QByteArray, QByteArray> "
        "&QGrpcOperation::serverInitialMetadata() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def serverInitialMetadataReceived(*__, **_) -> Never:
    """
    Qt's 'void QGrpcOperation::serverInitialMetadataReceived(const
    QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.serverInitialMetadataReceived' has no cute "
        "function yet. Qt's 'void "
        "QGrpcOperation::serverInitialMetadataReceived(const "
        "QMultiHash<QByteArray, QByteArray> &metadata)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def serverTrailingMetadata(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcOperation::serverTrailingMetadata() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.serverTrailingMetadata' has no cute function yet. "
        "Qt's 'const QMultiHash<QByteArray, QByteArray> "
        "&QGrpcOperation::serverTrailingMetadata() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def writeMessage(*__, **_) -> Never:
    """
    Qt's 'void QGrpcOperation::writeMessage(const QProtobufMessage
    &message)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperation.writeMessage' has no cute function yet. Qt's 'void "
        "QGrpcOperation::writeMessage(const QProtobufMessage &message)': "
        "takes a type Python has no way to hand over yet.")
