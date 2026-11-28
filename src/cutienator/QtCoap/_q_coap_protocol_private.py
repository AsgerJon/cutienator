"""
QCoapProtocolPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapprotocol_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapProtocolPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QCoapInternalReply, QCoapInternalRequest, QCoapProtocol
  from . import QCoapReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapInternalRequest = WAIT['QCoapInternalRequest']
  QCoapReply = WAIT['QCoapReply']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapProtocolPrivate(QObjectPrivate):
  """
  The cute side of Qt's QCoapProtocolPrivate: a plain Python object standing
  in front of one C++ QCoapProtocolPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QCoapProtocolPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapProtocolPrivate that has a ritual and that
  Python can call so far, 13 names in all: 'generateUniqueMessageId',
  'generateUniqueToken', 'onRequestAborted', 'isMessageIdRegistered',
  'isTokenRegistered', 'isRequestRegistered', 'requestForToken',
  'lastReplyForToken', 'findRequestByMessageId', 'findRequestByUserReply',
  'forgetExchange', 'forgetExchangeReplies', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPointer<QCoapReply> QCoapProtocolPrivate::userReplyForToken(const
    QCoapToken &token) const': gives a type Python has no way to take yet.
  - Qt's 'QList<QSharedPointer<QCoapInternalReply>>
    QCoapProtocolPrivate::repliesForToken(const QCoapToken &token) const':
    gives a type Python has no way to take yet.
  - Qt's 'void QCoapProtocolPrivate::registerExchange(const QCoapToken
    &token, QCoapReply *reply, QSharedPointer<QCoapInternalRequest>
    request)': takes a type Python has no way to hand over yet.
  - Qt's 'const QCoapProtocol *QCoapProtocolPrivate::q_func() const': takes
    in Python what 'QCoapProtocol *QCoapProtocolPrivate::q_func()' takes.

  What has no ritual
  ------------------

  13 of the 32 functions Qt declares: 6 leans on 'QCoapProtocol; 4 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 3 leans on 'QCoapInternalMessage.

  What to expect
  --------------

  - The C++ QCoapProtocolPrivate is created at the first use, not by
    'QCoapProtocolPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapProtocolPrivate.
  - Each name of Qt's QCoapProtocolPrivate that has no cute function yet,
    'addReply', 'decode', 'onConnectionError', 'onFrameReceived',
    'onLastMessageReceived', 'onMulticastRequestExpired', 'onRequestError',
    'onRequestMaxTransmissionSpanReached', 'onRequestTimeout',
    'registerExchange', 'repliesForToken', 'sendAcknowledgment',
    'sendRequest', 'sendReset', 'userReplyForToken', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapProtocolPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def generateUniqueMessageId(self) -> int:
    """
    Calls Qt's 'quint16 QCoapProtocolPrivate::generateUniqueMessageId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#generateUniqueMessageId
    """
    #  quint16 QCoapProtocolPrivate::generateUniqueMessageId() const
    return self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate23generateUniqueMessageIdEv',
    )

  def generateUniqueToken(self) -> QByteArray:
    """
    Calls Qt's 'QCoapToken QCoapProtocolPrivate::generateUniqueToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#generateUniqueToken

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QCoapToken QCoapProtocolPrivate::generateUniqueToken() const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate19generateUniqueTokenEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def isMessageIdRegistered(self, id: int) -> bool:
    """
    Calls Qt's 'bool QCoapProtocolPrivate::isMessageIdRegistered(quint16 id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#isMessageIdRegistered

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QCoapProtocolPrivate::isMessageIdRegistered(quint16 id) const
    return self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate21isMessageIdRegisteredEt', id,
    )

  @overload(QByteArray)
  def isTokenRegistered(self, token: QByteArray) -> bool:
    """
    Calls Qt's 'bool QCoapProtocolPrivate::isTokenRegistered(const QCoapToken
    &token) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#isTokenRegistered

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QCoapProtocolPrivate::isTokenRegistered(const QCoapToken &token)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate17isTokenRegisteredERK10QByteArray',
        self._valueOf(token),
    )

  @overload(QCoapInternalRequest)
  @overload(NoneType)
  def isRequestRegistered(
      self,
      request: Optional[QCoapInternalRequest],
  ) -> bool:
    """
    Calls Qt's 'bool QCoapProtocolPrivate::isRequestRegistered(const
    QCoapInternalRequest *request) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#isRequestRegistered

    Parameters
    ----------

    request : Optional[QCoapInternalRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoapProtocolPrivate::isRequestRegistered(const
    #      QCoapInternalRequest *request) const
    return self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate19isRequestRegisteredEPK20QCoapInt'
        'ernalRequest',
        self._addressOf(request),
    )

  @overload(QByteArray)
  def requestForToken(
      self,
      token: QByteArray,
  ) -> Optional[QCoapInternalRequest]:
    """
    Calls Qt's 'QCoapInternalRequest
    *QCoapProtocolPrivate::requestForToken(const QCoapToken &token) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#requestForToken

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QCoapInternalRequest]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalRequest *QCoapProtocolPrivate::requestForToken(const
    #      QCoapToken &token) const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate15requestForTokenERK10QByteArray',
        self._valueOf(token),
    )
    from . import QCoapInternalRequest
    return QCoapInternalRequest._cuteAt(address)

  @overload(QByteArray)
  def lastReplyForToken(
      self,
      token: QByteArray,
  ) -> Optional[QCoapInternalReply]:
    """
    Calls Qt's 'QCoapInternalReply
    *QCoapProtocolPrivate::lastReplyForToken(const QCoapToken &token) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#lastReplyForToken

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QCoapInternalReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalReply *QCoapProtocolPrivate::lastReplyForToken(const
    #      QCoapToken &token) const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate17lastReplyForTokenERK10QByteArray',
        self._valueOf(token),
    )
    from . import QCoapInternalReply
    return QCoapInternalReply._cuteAt(address)

  @overload(int)
  def findRequestByMessageId(
      self,
      messageId: int,
  ) -> Optional[QCoapInternalRequest]:
    """
    Calls Qt's 'QCoapInternalRequest
    *QCoapProtocolPrivate::findRequestByMessageId(quint16 messageId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#findRequestByMessageId

    Parameters
    ----------

    messageId : int
      Passed on as it is.

    Returns
    -------

    Optional[QCoapInternalRequest]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalRequest
    #      *QCoapProtocolPrivate::findRequestByMessageId(quint16 messageId)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate22findRequestByMessageIdEt',
        messageId,
    )
    from . import QCoapInternalRequest
    return QCoapInternalRequest._cuteAt(address)

  @overload(QCoapReply)
  @overload(NoneType)
  def findRequestByUserReply(
      self,
      reply: Optional[QCoapReply],
  ) -> Optional[QCoapInternalRequest]:
    """
    Calls Qt's 'QCoapInternalRequest
    *QCoapProtocolPrivate::findRequestByUserReply(const QCoapReply *reply)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#findRequestByUserReply

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCoapInternalRequest]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalRequest
    #      *QCoapProtocolPrivate::findRequestByUserReply(const QCoapReply
    #      *reply) const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapProtocolPrivate22findRequestByUserReplyEPK10QCoap'
        'Reply',
        self._addressOf(reply),
    )
    from . import QCoapInternalRequest
    return QCoapInternalRequest._cuteAt(address)

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
    Notes what was given, for Qt's
    'QCoapProtocolPrivate::QCoapProtocolPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#QCoapProtocolPrivate
    """
    #  QCoapProtocolPrivate::QCoapProtocolPrivate()
    self._noteCreation(QCoapProtocolPrivate, lambda: Rituals.call(
        'ritual_ZN20QCoapProtocolPrivateC1Ev',
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

  @overload(QByteArray)
  def onRequestAborted(self, token: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapProtocolPrivate::onRequestAborted(const QCoapToken
    &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#onRequestAborted

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapProtocolPrivate::onRequestAborted(const QCoapToken &token)
    self.uglySide.call(
        'ritual_ZN20QCoapProtocolPrivate16onRequestAbortedERK10QByteArray',
        self._valueOf(token),
    )

  @overload(QByteArray)
  def forgetExchange(self, token: QByteArray) -> bool:
    """
    Calls Qt's 'bool QCoapProtocolPrivate::forgetExchange(const QCoapToken
    &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#forgetExchange

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QCoapProtocolPrivate::forgetExchange(const QCoapToken &token)
    return self.uglySide.call(
        'ritual_ZN20QCoapProtocolPrivate14forgetExchangeERK10QByteArray',
        self._valueOf(token),
    )

  @overload(QCoapInternalRequest)
  @overload(NoneType)
  def forgetExchange(self, request: Optional[QCoapInternalRequest]) -> bool:
    """
    Calls Qt's 'bool QCoapProtocolPrivate::forgetExchange(const
    QCoapInternalRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#forgetExchange

    Parameters
    ----------

    request : Optional[QCoapInternalRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCoapProtocolPrivate::forgetExchange(const QCoapInternalRequest
    #      *request)
    return self.uglySide.call(
        'ritual_ZN20QCoapProtocolPrivate14forgetExchangeEPK20QCoapInternalR'
        'equest',
        self._addressOf(request),
    )

  @overload(QByteArray)
  def forgetExchangeReplies(self, token: QByteArray) -> bool:
    """
    Calls Qt's 'bool QCoapProtocolPrivate::forgetExchangeReplies(const
    QCoapToken &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocolprivate.html#forgetExchangeReplies

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QCoapProtocolPrivate::forgetExchangeReplies(const QCoapToken
    #      &token)
    return self.uglySide.call(
        'ritual_ZN20QCoapProtocolPrivate21forgetExchangeRepliesERK10QByteAr'
        'ray',
        self._valueOf(token),
    )

  def q_func(self) -> Optional[QCoapProtocol]:
    """
    Calls Qt's 'QCoapProtocol *QCoapProtocolPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocolprivate.html#q_func

    Returns
    -------

    Optional[QCoapProtocol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapProtocol *QCoapProtocolPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QCoapProtocolPrivate6q_funcEv')
    from . import QCoapProtocol
    return QCoapProtocol._cuteAt(address)

  @staticmethod
  def addReply(*__, **_) -> Never:
    """
    Qt's 'bool QCoapProtocolPrivate::addReply(const QCoapToken &token,
    QSharedPointer<QCoapInternalReply> reply)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'lcCoapProtocol'; did you mean 'QCoapProtocol'?.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.addReply' has no cute function yet. Qt's "
        "'bool QCoapProtocolPrivate::addReply(const QCoapToken &token, "
        "QSharedPointer<QCoapInternalReply> reply)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcCoapProtocol'; did you mean "
        "'QCoapProtocol'?.")

  @staticmethod
  def decode(*__, **_) -> Never:
    """
    Qt's 'QCoapInternalReply *QCoapProtocolPrivate::decode(const QByteArray
    &data, const QHostAddress &sender)': leans on
    'QCoapInternalMessage::addOption(QCoapOption::OptionName, QByteArray
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.decode' has no cute function yet. Qt's "
        "'QCoapInternalReply *QCoapProtocolPrivate::decode(const QByteArray "
        "&data, const QHostAddress &sender)': leans on "
        "'QCoapInternalMessage::addOption(QCoapOption::OptionName, "
        "QByteArray const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def onConnectionError(*__, **_) -> Never:
    """
    Qt's 'void
    QCoapProtocolPrivate::onConnectionError(QAbstractSocket::SocketError
    error)': leans on 'QCoapProtocol::error(QCoapReply*, QtCoap::Error)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onConnectionError' has no cute function yet. "
        "Qt's 'void "
        "QCoapProtocolPrivate::onConnectionError(QAbstractSocket::SocketErro"
        "r error)': leans on 'QCoapProtocol::error(QCoapReply*, "
        "QtCoap::Error)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def onFrameReceived(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::onFrameReceived(const QByteArray &data,
    const QHostAddress &sender)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: unknown type
    name 'lcCoapProtocol'; did you mean 'QCoapProtocol'?.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onFrameReceived' has no cute function yet. "
        "Qt's 'void QCoapProtocolPrivate::onFrameReceived(const QByteArray "
        "&data, const QHostAddress &sender)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: unknown type name 'lcCoapProtocol'; did you mean "
        "'QCoapProtocol'?.")

  @staticmethod
  def onLastMessageReceived(*__, **_) -> Never:
    """
    Qt's 'void
    QCoapProtocolPrivate::onLastMessageReceived(QCoapInternalRequest
    *request, const QHostAddress &sender)': leans on
    'QCoapProtocol::responseToMulticastReceived(QCoapReply*, QCoapMessage
    const&, QHostAddress const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onLastMessageReceived' has no cute function "
        "yet. Qt's 'void "
        "QCoapProtocolPrivate::onLastMessageReceived(QCoapInternalRequest "
        "*request, const QHostAddress &sender)': leans on "
        "'QCoapProtocol::responseToMulticastReceived(QCoapReply*, "
        "QCoapMessage const&, QHostAddress const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def onMulticastRequestExpired(*__, **_) -> Never:
    """
    Qt's 'void
    QCoapProtocolPrivate::onMulticastRequestExpired(QCoapInternalRequest
    *request)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'lcCoapProtocol';
    did you mean 'QCoapProtocol'?.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onMulticastRequestExpired' has no cute "
        "function yet. Qt's 'void "
        "QCoapProtocolPrivate::onMulticastRequestExpired(QCoapInternalReques"
        "t *request)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'lcCoapProtocol'; did you mean 'QCoapProtocol'?.")

  @staticmethod
  def onRequestError(*__, **_) -> Never:
    """
    - Qt's 'void QCoapProtocolPrivate::onRequestError(QCoapInternalRequest
      *request, QCoapInternalReply *reply)': leans on
      'QCoapProtocol::error(QCoapReply*, QtCoap::Error)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'void QCoapProtocolPrivate::onRequestError(QCoapInternalRequest
      *request, QtCoap::Error error, QCoapInternalReply *reply)': leans on
      'QCoapProtocol::error(QCoapReply*, QtCoap::Error)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onRequestError' has no cute function yet. "
        "Qt's 'void "
        "QCoapProtocolPrivate::onRequestError(QCoapInternalRequest "
        "*request, QCoapInternalReply *reply)': leans on "
        "'QCoapProtocol::error(QCoapReply*, QtCoap::Error)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken. Qt's 'void "
        "QCoapProtocolPrivate::onRequestError(QCoapInternalRequest "
        "*request, QtCoap::Error error, QCoapInternalReply *reply)': leans "
        "on 'QCoapProtocol::error(QCoapReply*, QtCoap::Error)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def onRequestMaxTransmissionSpanReached(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::onRequestMaxTransmissionSpanReached(
    QCoapInternalRequest *request)': leans on
    'QCoapProtocol::error(QCoapReply*, QtCoap::Error)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onRequestMaxTransmissionSpanReached' has no "
        "cute function yet. Qt's 'void "
        "QCoapProtocolPrivate::onRequestMaxTransmissionSpanReached(QCoapInte"
        "rnalRequest *request)': leans on "
        "'QCoapProtocol::error(QCoapReply*, QtCoap::Error)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def onRequestTimeout(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::onRequestTimeout(QCoapInternalRequest
    *request)': leans on 'QCoapProtocol::error(QCoapReply*, QtCoap::Error)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.onRequestTimeout' has no cute function yet. "
        "Qt's 'void "
        "QCoapProtocolPrivate::onRequestTimeout(QCoapInternalRequest "
        "*request)': leans on 'QCoapProtocol::error(QCoapReply*, "
        "QtCoap::Error)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def registerExchange(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::registerExchange(const QCoapToken
    &token, QCoapReply *reply, QSharedPointer<QCoapInternalRequest>
    request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.registerExchange' has no cute function yet. "
        "Qt's 'void QCoapProtocolPrivate::registerExchange(const QCoapToken "
        "&token, QCoapReply *reply, QSharedPointer<QCoapInternalRequest> "
        "request)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def repliesForToken(*__, **_) -> Never:
    """
    Qt's 'QList<QSharedPointer<QCoapInternalReply>>
    QCoapProtocolPrivate::repliesForToken(const QCoapToken &token) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.repliesForToken' has no cute function yet. "
        "Qt's 'QList<QSharedPointer<QCoapInternalReply>> "
        "QCoapProtocolPrivate::repliesForToken(const QCoapToken &token) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def sendAcknowledgment(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::sendAcknowledgment(QCoapInternalRequest
    *request) const': leans on
    'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePrivate&,
    QObject*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.sendAcknowledgment' has no cute function "
        "yet. Qt's 'void "
        "QCoapProtocolPrivate::sendAcknowledgment(QCoapInternalRequest "
        "*request) const': leans on "
        "'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePri"
        "vate&, QObject*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def sendRequest(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::sendRequest(QCoapInternalRequest
    *request, const QString &host) const': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: unknown
    type name 'lcCoapProtocol'; did you mean 'QCoapProtocol'?.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.sendRequest' has no cute function yet. Qt's "
        "'void QCoapProtocolPrivate::sendRequest(QCoapInternalRequest "
        "*request, const QString &host) const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'lcCoapProtocol'; did you mean "
        "'QCoapProtocol'?.")

  @staticmethod
  def sendReset(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocolPrivate::sendReset(QCoapInternalRequest *request)
    const': leans on
    'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePrivate&,
    QObject*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.sendReset' has no cute function yet. Qt's "
        "'void QCoapProtocolPrivate::sendReset(QCoapInternalRequest "
        "*request) const': leans on "
        "'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePri"
        "vate&, QObject*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def userReplyForToken(*__, **_) -> Never:
    """
    Qt's 'QPointer<QCoapReply> QCoapProtocolPrivate::userReplyForToken(const
    QCoapToken &token) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCoapProtocolPrivate.userReplyForToken' has no cute function yet. "
        "Qt's 'QPointer<QCoapReply> "
        "QCoapProtocolPrivate::userReplyForToken(const QCoapToken &token) "
        "const': gives a type Python has no way to take yet.")
