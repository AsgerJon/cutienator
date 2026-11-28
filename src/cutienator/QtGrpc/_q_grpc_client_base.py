"""
QGrpcClientBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcclientbase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QLatin1String, QMetaObject, QMetaType
  from . import QGrpcOperation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QGrpcOperation = WAIT['QGrpcOperation']
  QLatin1String = WAIT['QLatin1String']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGrpcClientBase(QObject):
  """
  The cute side of Qt's QGrpcClientBase: a plain Python object standing in
  front of one C++ QGrpcClientBase.

  It is built on the cute 'QObject', as Qt's QGrpcClientBase is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcClientBase that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'channelChanged',
  'setOperationResponseMetaType', 'event'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGrpcClientBase::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGrpcClientBase::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGrpcClientBase::~QGrpcClientBase()': the destructor: Python never
    removes a C++ QGrpcClientBase.
  - Qt's 'bool
    QGrpcClientBase::attachChannel(std::shared_ptr<QAbstractGrpcChannel>
    channel)': takes a type Python has no way to hand over yet.
  - Qt's 'std::shared_ptr<QAbstractGrpcChannel> QGrpcClientBase::channel()
    const': gives a type Python has no way to take yet.
  - Qt's 'std::unique_ptr<QGrpcCallReply>
    QGrpcClientBase::call(QLatin1StringView method, const QProtobufMessage
    &arg, const QGrpcCallOptions &options)': takes a type Python has no way
    to hand over yet.
  - Qt's 'std::unique_ptr<QGrpcServerStream>
    QGrpcClientBase::serverStream(QLatin1StringView method, const
    QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::unique_ptr<QGrpcClientStream>
    QGrpcClientBase::clientStream(QLatin1StringView method, const
    QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::unique_ptr<QGrpcBidiStream>
    QGrpcClientBase::bidiStream(QLatin1StringView method, const
    QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QGrpcClientBasePrivate *QGrpcClientBase::d_func()': gives
    'QGrpcClientBasePrivate', which has no cute class yet.
  - Qt's 'const QGrpcClientBasePrivate *QGrpcClientBase::d_func() const':
    gives 'QGrpcClientBasePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 23 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QGrpcClientBase is created at the first use, not by
    'QGrpcClientBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcClientBase.
  - Qt tells when it has removed the C++ QGrpcClientBase. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGrpcClientBase that has no cute function yet,
    'attachChannel', 'bidiStream', 'call', 'channel', 'clientStream',
    'serverStream', holds a function that raises 'NotImplementedError', and
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
    Calls Qt's 'QString QGrpcClientBase::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcclientbase.html#tr

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
    #  QString QGrpcClientBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGrpcClientBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QGrpcOperation, QMetaType)
  @overload(NoneType, QMetaType)
  def setOperationResponseMetaType(
      operation: Optional[QGrpcOperation],
      responseMetaType: QMetaType,
  ) -> None:
    """
    Calls Qt's 'void
    QGrpcClientBase::setOperationResponseMetaType(QGrpcOperation *operation,
    QMetaType responseMetaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcclientbase.html#setOperationResponseMetaType

    Parameters
    ----------

    operation : Optional[QGrpcOperation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    responseMetaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QGrpcClientBase::setOperationResponseMetaType(QGrpcOperation
    #      *operation, QMetaType responseMetaType)
    Rituals.call(
        'ritual_ZN15QGrpcClientBase28setOperationResponseMetaTypeEP14QGrpcO'
        'peration9QMetaType',
        CuteMixin._addressOf(operation),
        CuteMixin._valueOf(responseMetaType),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcClientBase'

  #  A C++ QGrpcClientBase Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGrpcClientBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGrpcClientBase::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcclientbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGrpcClientBase::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGrpcClientBase10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QLatin1String)
  @overload(QLatin1String, QObject)
  @overload(QLatin1String, NoneType)
  def __init__(
      self,
      service: QLatin1String,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcClientBase::QGrpcClientBase(QLatin1StringView service, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcclientbase.html#QGrpcClientBase

    Parameters
    ----------

    service : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGrpcClientBase::QGrpcClientBase(QLatin1StringView service, QObject
    #      *parent)
    self._noteCreation(QGrpcClientBase, lambda: Rituals.call(
        'ritual_ZN15QGrpcClientBaseC1E13QLatin1StringP7QObject',
        self._valueOf(service), self._addressOf(parent, 'QObject'),
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

  def channelChanged(self) -> None:
    """
    Calls Qt's 'void QGrpcClientBase::channelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcclientbase.html#channelChanged
    """
    #  void QGrpcClientBase::channelChanged()
    self.uglySide.call('ritual_ZN15QGrpcClientBase14channelChangedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGrpcClientBase::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcclientbase.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGrpcClientBase::event(QEvent *event)
    ritual = 'ritual_ZN15QGrpcClientBase5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGrpcClientBase5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def attachChannel(*__, **_) -> Never:
    """
    Qt's 'bool
    QGrpcClientBase::attachChannel(std::shared_ptr<QAbstractGrpcChannel>
    channel)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcClientBase.attachChannel' has no cute function yet. Qt's "
        "'bool "
        "QGrpcClientBase::attachChannel(std::shared_ptr<QAbstractGrpcChannel"
        "> channel)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def bidiStream(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QGrpcBidiStream>
    QGrpcClientBase::bidiStream(QLatin1StringView method, const
    QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcClientBase.bidiStream' has no cute function yet. Qt's "
        "'std::unique_ptr<QGrpcBidiStream> "
        "QGrpcClientBase::bidiStream(QLatin1StringView method, const "
        "QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def call(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QGrpcCallReply>
    QGrpcClientBase::call(QLatin1StringView method, const QProtobufMessage
    &arg, const QGrpcCallOptions &options)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcClientBase.call' has no cute function yet. Qt's "
        "'std::unique_ptr<QGrpcCallReply> "
        "QGrpcClientBase::call(QLatin1StringView method, const "
        "QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def channel(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QAbstractGrpcChannel> QGrpcClientBase::channel()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcClientBase.channel' has no cute function yet. Qt's "
        "'std::shared_ptr<QAbstractGrpcChannel> QGrpcClientBase::channel() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def clientStream(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QGrpcClientStream>
    QGrpcClientBase::clientStream(QLatin1StringView method, const
    QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcClientBase.clientStream' has no cute function yet. Qt's "
        "'std::unique_ptr<QGrpcClientStream> "
        "QGrpcClientBase::clientStream(QLatin1StringView method, const "
        "QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def serverStream(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QGrpcServerStream>
    QGrpcClientBase::serverStream(QLatin1StringView method, const
    QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcClientBase.serverStream' has no cute function yet. Qt's "
        "'std::unique_ptr<QGrpcServerStream> "
        "QGrpcClientBase::serverStream(QLatin1StringView method, const "
        "QProtobufMessage &arg, const QGrpcCallOptions &options)': takes a "
        "type Python has no way to hand over yet.")
