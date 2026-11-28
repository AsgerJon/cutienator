"""
QDBusMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusmessage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QDBusError

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QDBusMessage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMessage: a plain Python object standing in front
  of one C++ QDBusMessage.

  C++ hands a QDBusMessage around as a copy, so every C++ QDBusMessage behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusMessage that has a ritual and that Python can
  call so far, 23 names in all: 'createSignal', 'createTargetedSignal',
  'createMethodCall', 'createError', 'createReply', 'createErrorReply',
  'service', 'path', 'interface', 'member', 'errorName', 'errorMessage',
  'type', 'signature', 'isReplyRequired', 'setDelayedReply',
  'isDelayedReply', 'setAutoStartService', 'autoStartService',
  'setInteractiveAuthorizationAllowed', 'isInteractiveAuthorizationAllowed',
  'setArguments', 'arguments'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusMessage::QDBusMessage(QDBusMessage &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDBusMessage &QDBusMessage::operator=(QDBusMessage &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusMessage &QDBusMessage::operator=(const QDBusMessage &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusMessage::~QDBusMessage()': the destructor: Python removes its
    C++ QDBusMessage by it, and has no other use for it.
  - Qt's 'void QDBusMessage::swap(QDBusMessage &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QDBusMessage &QDBusMessage::operator<<(const QVariant &arg)': gives
    a type Python has no way to take yet.
  - Qt's 'QDBusMessage::QDBusMessage(QDBusMessagePrivate &dd)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDBusMessage is created at the first use, not by
    'QDBusMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusMessage back gives a copy the ritual made for
    Python, in a new cute QDBusMessage.
  - Each name of Qt's QDBusMessage that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QDBusMessage, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class MessageType(CuteNum):
    """
    The enum 'QDBusMessage::MessageType' of Qt, with the 5 names Qt gives in
    it.
    """

    InvalidMessage = Kee[int](0)
    MethodCallMessage = Kee[int](1)
    ReplyMessage = Kee[int](2)
    ErrorMessage = Kee[int](3)
    SignalMessage = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str, str)
  def createSignal(path: str, interface: str, name: str) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createSignal(const QString &path,
    const QString &interface, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createSignal

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createSignal(const QString &path, const
    #      QString &interface, const QString &name)
    address = Rituals.call(
        'ritual_ZN12QDBusMessage12createSignalERK7QStringS2_S2_',
        path, interface, name,
    )
    return QDBusMessage._cuteOwning(address)

  @staticmethod
  @overload(str, str, str, str)
  def createTargetedSignal(
      service: str,
      path: str,
      interface: str,
      name: str,
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createTargetedSignal(const QString
    &service, const QString &path, const QString &interface, const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmessage.html#createTargetedSignal

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createTargetedSignal(const QString
    #      &service, const QString &path, const QString &interface, const
    #      QString &name)
    address = Rituals.call(
        'ritual_ZN12QDBusMessage20createTargetedSignalERK7QStringS2_S2_S2_',
        service, path, interface, name,
    )
    return QDBusMessage._cuteOwning(address)

  @staticmethod
  @overload(str, str, str, str)
  def createMethodCall(
      destination: str,
      path: str,
      interface: str,
      method: str,
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createMethodCall(const QString
    &destination, const QString &path, const QString &interface, const
    QString &method)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createMethodCall

    Parameters
    ----------

    destination : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    method : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createMethodCall(const QString
    #      &destination, const QString &path, const QString &interface, const
    #      QString &method)
    address = Rituals.call(
        'ritual_ZN12QDBusMessage16createMethodCallERK7QStringS2_S2_S2_',
        destination, path, interface, method,
    )
    return QDBusMessage._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def createError(name: str, msg: str) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createError(const QString &name,
    const QString &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createError

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createError(const QString &name, const
    #      QString &msg)
    address = Rituals.call(
        'ritual_ZN12QDBusMessage11createErrorERK7QStringS2_', name, msg,
    )
    return QDBusMessage._cuteOwning(address)

  @staticmethod
  @overload(QDBusError)
  def createError(err: QDBusError) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createError(const QDBusError
    &err)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createError

    Parameters
    ----------

    err : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createError(const QDBusError &err)
    address = Rituals.call(
        'ritual_ZN12QDBusMessage11createErrorERK10QDBusError',
        CuteMixin._valueOf(err),
    )
    return QDBusMessage._cuteOwning(address)

  @staticmethod
  @overload(QDBusError.ErrorType, str)
  def createError(type: QDBusError.ErrorType, msg: str) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createError(QDBusError::ErrorType
    type, const QString &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createError

    Parameters
    ----------

    type : QDBusError.ErrorType
      Passed on as its number.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createError(QDBusError::ErrorType type,
    #      const QString &msg)
    address = Rituals.call(
        'ritual_ZN12QDBusMessage11createErrorEN10QDBusError9ErrorTypeERK7QS'
        'tring',
        type.value, msg,
    )
    return QDBusMessage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMessage'

  #  Qt's '~QDBusMessage()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusMessage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QDBusMessageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVariant])
  def createReply(self, arguments: QList[QVariant]) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createReply(const QList<QVariant>
    &arguments) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createReply

    Parameters
    ----------

    arguments : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createReply(const QList<QVariant>
    #      &arguments) const
    address = self.uglySide.call(
        'ritual_ZNK12QDBusMessage11createReplyERK5QListI8QVariantE',
        self._valueOf(arguments),
    )
    return QDBusMessage._cuteOwning(address)

  @overload(QVariant)
  def createReply(self, argument: QVariant) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createReply(const QVariant
    &argument) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createReply

    Parameters
    ----------

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createReply(const QVariant &argument) const
    address = self.uglySide.call(
        'ritual_ZNK12QDBusMessage11createReplyERK8QVariant',
        self._valueOf(argument),
    )
    return QDBusMessage._cuteOwning(address)

  @overload(str, str)
  def createErrorReply(self, name: str, msg: str) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createErrorReply(const QString
    &name, const QString &msg) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createErrorReply

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createErrorReply(const QString &name, const
    #      QString &msg) const
    address = self.uglySide.call(
        'ritual_ZNK12QDBusMessage16createErrorReplyERK7QStringS2_',
        name, msg,
    )
    return QDBusMessage._cuteOwning(address)

  @overload(QDBusError)
  def createErrorReply(self, err: QDBusError) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusMessage::createErrorReply(const QDBusError
    &err) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createErrorReply

    Parameters
    ----------

    err : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createErrorReply(const QDBusError &err)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QDBusMessage16createErrorReplyERK10QDBusError',
        self._valueOf(err),
    )
    return QDBusMessage._cuteOwning(address)

  @overload(QDBusError.ErrorType, str)
  def createErrorReply(
      self,
      type: QDBusError.ErrorType,
      msg: str,
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage
    QDBusMessage::createErrorReply(QDBusError::ErrorType type, const QString
    &msg) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#createErrorReply

    Parameters
    ----------

    type : QDBusError.ErrorType
      Passed on as its number.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusMessage::createErrorReply(QDBusError::ErrorType
    #      type, const QString &msg) const
    address = self.uglySide.call(
        'ritual_ZNK12QDBusMessage16createErrorReplyEN10QDBusError9ErrorType'
        'ERK7QString',
        type.value, msg,
    )
    return QDBusMessage._cuteOwning(address)

  def service(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::service() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#service

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::service() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage7serviceEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::path() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage4pathEv')

  def interface(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::interface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#interface

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::interface() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage9interfaceEv')

  def member(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::member() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#member

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::member() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage6memberEv')

  def errorName(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::errorName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#errorName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::errorName() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage9errorNameEv')

  def errorMessage(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::errorMessage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#errorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::errorMessage() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage12errorMessageEv')

  def type(self) -> MessageType:
    """
    Calls Qt's 'MessageType QDBusMessage::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#type

    Returns
    -------

    MessageType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MessageType(number)'
      gives.
    """
    #  MessageType QDBusMessage::type() const
    return QDBusMessage.MessageType(self.uglySide.call(
        'ritual_ZNK12QDBusMessage4typeEv',
    ))

  def signature(self) -> str:
    """
    Calls Qt's 'QString QDBusMessage::signature() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#signature

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusMessage::signature() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage9signatureEv')

  def isReplyRequired(self) -> bool:
    """
    Calls Qt's 'bool QDBusMessage::isReplyRequired() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#isReplyRequired
    """
    #  bool QDBusMessage::isReplyRequired() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage15isReplyRequiredEv')

  def isDelayedReply(self) -> bool:
    """
    Calls Qt's 'bool QDBusMessage::isDelayedReply() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#isDelayedReply
    """
    #  bool QDBusMessage::isDelayedReply() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage14isDelayedReplyEv')

  def autoStartService(self) -> bool:
    """
    Calls Qt's 'bool QDBusMessage::autoStartService() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#autoStartService
    """
    #  bool QDBusMessage::autoStartService() const
    return self.uglySide.call('ritual_ZNK12QDBusMessage16autoStartServiceEv')

  def isInteractiveAuthorizationAllowed(self) -> bool:
    """
    Calls Qt's 'bool QDBusMessage::isInteractiveAuthorizationAllowed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmessage.html
    """
    #  bool QDBusMessage::isInteractiveAuthorizationAllowed() const
    return self.uglySide.call(
        'ritual_ZNK12QDBusMessage33isInteractiveAuthorizationAllowedEv',
    )

  def arguments(self) -> QList[QVariant]:
    """
    Calls Qt's 'QList<QVariant> QDBusMessage::arguments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#arguments

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVariant> QDBusMessage::arguments() const
    address = self.uglySide.call('ritual_ZNK12QDBusMessage9argumentsEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDelayedReply(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusMessage::setDelayedReply(bool enable) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#setDelayedReply

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusMessage::setDelayedReply(bool enable) const
    self.uglySide.call('ritual_ZNK12QDBusMessage15setDelayedReplyEb', enable)

  @overload(bool)
  def setAutoStartService(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusMessage::setAutoStartService(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmessage.html#setAutoStartService

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusMessage::setAutoStartService(bool enable)
    self.uglySide.call(
        'ritual_ZN12QDBusMessage19setAutoStartServiceEb', enable,
    )

  @overload(bool)
  def setInteractiveAuthorizationAllowed(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusMessage::setInteractiveAuthorizationAllowed(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmessage.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusMessage::setInteractiveAuthorizationAllowed(bool enable)
    self.uglySide.call(
        'ritual_ZN12QDBusMessage34setInteractiveAuthorizationAllowedEb',
        enable,
    )

  @overload(QList[QVariant])
  def setArguments(self, arguments: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QDBusMessage::setArguments(const QList<QVariant>
    &arguments)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#setArguments

    Parameters
    ----------

    arguments : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusMessage::setArguments(const QList<QVariant> &arguments)
    self.uglySide.call(
        'ritual_ZN12QDBusMessage12setArgumentsERK5QListI8QVariantE',
        self._valueOf(arguments),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDBusMessage::QDBusMessage()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#QDBusMessage
    """
    #  QDBusMessage::QDBusMessage()
    self._noteCreation(QDBusMessage, lambda: Rituals.call(
        'ritual_ZN12QDBusMessageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDBusMessage) -> None:
    """
    Notes what was given, for Qt's 'QDBusMessage::QDBusMessage(const
    QDBusMessage &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessage.html#QDBusMessage

    Parameters
    ----------

    other : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  QDBusMessage::QDBusMessage(const QDBusMessage &other)
    self._noteCreation(QDBusMessage, lambda: Rituals.call(
        'ritual_ZN12QDBusMessageC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusMessage::swap(QDBusMessage &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusMessage.swap' has no cute function yet. Qt's 'void "
        "QDBusMessage::swap(QDBusMessage &other)': takes a type Python has "
        "no way to hand over yet.")
