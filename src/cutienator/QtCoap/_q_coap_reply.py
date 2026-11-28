"""
QCoapReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QIODevice
from . import QtCoap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from . import QCoapMessage, QCoapReplyPrivate, QCoapRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapMessage = WAIT['QCoapMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapReply(QIODevice):
  """
  The cute side of Qt's QCoapReply: a plain Python object standing in front
  of one C++ QCoapReply.

  It is built on the cute 'QIODevice', as Qt's QCoapReply is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapReply that has a ritual and that Python can
  call so far, 19 names in all: 'metaObject', 'tr', 'responseCode',
  'message', 'request', 'url', 'method', 'errorReceived', 'isRunning',
  'isFinished', 'isAborted', 'isSuccessful', 'abortRequest', 'finished',
  'notified', 'error', 'aborted', 'writeData', 'd_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCoapReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCoapReply::~QCoapReply()': the destructor: Python never removes a
    C++ QCoapReply.
  - Qt's 'qint64 QCoapReply::readData(char *data, qint64 maxSize)': names
    'char', which has no cute class yet.
  - Qt's 'const QCoapReplyPrivate *QCoapReply::d_func() const': takes in
    Python what 'QCoapReplyPrivate *QCoapReply::d_func()' takes.
  - Qt's 'QCoapReply::QCoapReply(QCoapReplyPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCoapReply is created at the first use, not by 'QCoapReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapReply.
  - Qt tells when it has removed the C++ QCoapReply. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QCoapReply that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QCoapReply::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#tr

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
    #  QString QCoapReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QCoapReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapReply'

  #  A C++ QCoapReply Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QCoapReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def responseCode(self) -> QtCoap.ResponseCode:
    """
    Calls Qt's 'QtCoap::ResponseCode QCoapReply::responseCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#responseCode

    Returns
    -------

    QtCoap.ResponseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCoap.ResponseCode(number)' gives.
    """
    #  QtCoap::ResponseCode QCoapReply::responseCode() const
    return QtCoap.ResponseCode(self.uglySide.call(
        'ritual_ZNK10QCoapReply12responseCodeEv',
    ))

  def message(self) -> QCoapMessage:
    """
    Calls Qt's 'QCoapMessage QCoapReply::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#message

    Returns
    -------

    QCoapMessage
      A new cute QCoapMessage around the copy Qt gave back. Python owns it.
    """
    #  QCoapMessage QCoapReply::message() const
    address = self.uglySide.call('ritual_ZNK10QCoapReply7messageEv')
    from . import QCoapMessage
    return QCoapMessage._cuteOwning(address)

  def request(self) -> QCoapRequest:
    """
    Calls Qt's 'QCoapRequest QCoapReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#request

    Returns
    -------

    QCoapRequest
      A new cute QCoapRequest around the copy Qt gave back. Python owns it.
    """
    #  QCoapRequest QCoapReply::request() const
    address = self.uglySide.call('ritual_ZNK10QCoapReply7requestEv')
    from . import QCoapRequest
    return QCoapRequest._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QCoapReply::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QCoapReply::url() const
    address = self.uglySide.call('ritual_ZNK10QCoapReply3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def method(self) -> QtCoap.Method:
    """
    Calls Qt's 'QtCoap::Method QCoapReply::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#method

    Returns
    -------

    QtCoap.Method
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtCoap.Method(number)'
      gives.
    """
    #  QtCoap::Method QCoapReply::method() const
    return QtCoap.Method(self.uglySide.call(
        'ritual_ZNK10QCoapReply6methodEv',
    ))

  def errorReceived(self) -> QtCoap.Error:
    """
    Calls Qt's 'QtCoap::Error QCoapReply::errorReceived() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#errorReceived

    Returns
    -------

    QtCoap.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtCoap.Error(number)'
      gives.
    """
    #  QtCoap::Error QCoapReply::errorReceived() const
    return QtCoap.Error(self.uglySide.call(
        'ritual_ZNK10QCoapReply13errorReceivedEv',
    ))

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QCoapReply::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#isRunning
    """
    #  bool QCoapReply::isRunning() const
    return self.uglySide.call('ritual_ZNK10QCoapReply9isRunningEv')

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QCoapReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#isFinished
    """
    #  bool QCoapReply::isFinished() const
    return self.uglySide.call('ritual_ZNK10QCoapReply10isFinishedEv')

  def isAborted(self) -> bool:
    """
    Calls Qt's 'bool QCoapReply::isAborted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#isAborted
    """
    #  bool QCoapReply::isAborted() const
    return self.uglySide.call('ritual_ZNK10QCoapReply9isAbortedEv')

  def isSuccessful(self) -> bool:
    """
    Calls Qt's 'bool QCoapReply::isSuccessful() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#isSuccessful
    """
    #  bool QCoapReply::isSuccessful() const
    return self.uglySide.call('ritual_ZNK10QCoapReply12isSuccessfulEv')

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
    Qt's 'QCoapReply::QCoapReply(QCoapReplyPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapReply.__init__' has no cute function yet. Qt's "
        "'QCoapReply::QCoapReply(QCoapReplyPrivate &dd, QObject *parent)': "
        "takes a type Python has no way to hand over yet.")

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

  def abortRequest(self) -> None:
    """
    Calls Qt's 'void QCoapReply::abortRequest()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#abortRequest
    """
    #  void QCoapReply::abortRequest()
    self.uglySide.call('ritual_ZN10QCoapReply12abortRequestEv')

  @overload(THIS)
  @overload(NoneType)
  def finished(self, reply: Optional[QCoapReply]) -> None:
    """
    Calls Qt's 'void QCoapReply::finished(QCoapReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#finished

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapReply::finished(QCoapReply *reply)
    self.uglySide.call(
        'ritual_ZN10QCoapReply8finishedEPS_', self._addressOf(reply),
    )

  @overload(THIS, QCoapMessage)
  @overload(NoneType, QCoapMessage)
  def notified(
      self,
      reply: Optional[QCoapReply],
      message: QCoapMessage,
  ) -> None:
    """
    Calls Qt's 'void QCoapReply::notified(QCoapReply *reply, const
    QCoapMessage &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#notified

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    message : QCoapMessage
      Passed on as a value: Qt reads the C++ QCoapMessage, which stays
      Python's own.
    """
    #  void QCoapReply::notified(QCoapReply *reply, const QCoapMessage
    #      &message)
    self.uglySide.call(
        'ritual_ZN10QCoapReply8notifiedEPS_RK12QCoapMessage',
        self._addressOf(reply), self._valueOf(message),
    )

  @overload(THIS, QtCoap.Error)
  @overload(NoneType, QtCoap.Error)
  def error(self, reply: Optional[QCoapReply], error: QtCoap.Error) -> None:
    """
    Calls Qt's 'void QCoapReply::error(QCoapReply *reply, QtCoap::Error
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#error

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QtCoap.Error
      Passed on as its number.
    """
    #  void QCoapReply::error(QCoapReply *reply, QtCoap::Error error)
    self.uglySide.call(
        'ritual_ZN10QCoapReply5errorEPS_N6QtCoap5ErrorE',
        self._addressOf(reply), error.value,
    )

  @overload(QByteArray)
  def aborted(self, token: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapReply::aborted(const QCoapToken &token)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#aborted

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapReply::aborted(const QCoapToken &token)
    self.uglySide.call(
        'ritual_ZN10QCoapReply7abortedERK10QByteArray', self._valueOf(token),
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QCoapReply::writeData(const char *data, qint64
    maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QCoapReply::writeData(const char *data, qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN10QCoapReply9writeDataEPKcx', self._bytesOf(data), maxSize,
    )

  def d_func(self) -> Optional[QCoapReplyPrivate]:
    """
    Calls Qt's 'QCoapReplyPrivate *QCoapReply::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapreply.html#d_func

    Returns
    -------

    Optional[QCoapReplyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapReplyPrivate *QCoapReply::d_func()
    address = self.uglySide.call('ritual_ZN10QCoapReply6d_funcEv')
    from . import QCoapReplyPrivate
    return QCoapReplyPrivate._cuteAt(address)
