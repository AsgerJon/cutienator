"""
QNearFieldTargetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QNearFieldTargetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from . import QNearFieldTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QNdefMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNdefMessage = WAIT['QNdefMessage']
  QVariant = WAIT['QVariant']


class QNearFieldTargetPrivate(QObject):
  """
  The cute side of Qt's QNearFieldTargetPrivate: a plain Python object
  standing in front of one C++ QNearFieldTargetPrivate.

  It is built on the cute 'QObject', as Qt's QNearFieldTargetPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNearFieldTargetPrivate that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'uid', 'type',
  'accessMethods', 'disconnect', 'hasNdefMessage', 'readNdefMessages',
  'writeNdefMessages', 'maxCommandLength', 'sendCommand', 'requestResponse',
  'disconnected', 'ndefMessageRead', 'requestCompleted', 'error',
  'setResponseForRequest'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNearFieldTargetPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNearFieldTargetPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNearFieldTargetPrivate::~QNearFieldTargetPrivate()': the
    destructor: Python never removes a C++ QNearFieldTargetPrivate.

  What has no ritual
  ------------------

  6 of the 25 functions Qt declares: 4 leans on 'QNearFieldTargetPrivate; 2
  not a gap.

  What to expect
  --------------

  - The C++ QNearFieldTargetPrivate is created at the first use, not by
    'QNearFieldTargetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNearFieldTargetPrivate.
  - Qt tells when it has removed the C++ QNearFieldTargetPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNearFieldTargetPrivate that has no cute function yet,
    '__init__', 'reportError', 'waitForRequestCompleted', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNearFieldTargetPrivate'

  #  A C++ QNearFieldTargetPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNearFieldTargetPrivate'

  #  The functions Qt calls itself that QNearFieldTargetPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'writeNdefMessages': (
          'QNearFieldTarget::RequestId '
          'QNearFieldTargetPrivate::writeNdefMessages(const '
          'QList<QNdefMessage> &)',
      ),
  }

  #  The functions Qt calls itself that QNearFieldTargetPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'uid': (
          ('_ZNK23QNearFieldTargetPrivate3uidEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'type': (
          ('_ZNK23QNearFieldTargetPrivate4typeEv',
           ('int', 'enum', 'QtNfc:QNearFieldTarget.Type'),
           ()),
      ),
      'accessMethods': (
          ('_ZNK23QNearFieldTargetPrivate13accessMethodsEv',
           ('int', 'flags', 'QtNfc:QNearFieldTarget.AccessMethod'),
           ()),
      ),
      'disconnect': (
          ('_ZN23QNearFieldTargetPrivate10disconnectEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasNdefMessage': (
          ('_ZN23QNearFieldTargetPrivate14hasNdefMessageEv',
           ('bool', 'number', ''),
           ()),
      ),
      'readNdefMessages': (
          ('_ZN23QNearFieldTargetPrivate16readNdefMessagesEv',
           ('address', 'value', 'QtNfc:QNearFieldTarget.RequestId'),
           ()),
      ),
      'maxCommandLength': (
          ('_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv',
           ('int', 'number', ''),
           ()),
      ),
      'sendCommand': (
          ('_ZN23QNearFieldTargetPrivate11sendCommandERK10QByteArray',
           ('address', 'value', 'QtNfc:QNearFieldTarget.RequestId'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'setResponseForRequest': (
          ('_ZN23QNearFieldTargetPrivate21setResponseForRequestERKN16QNearF'
           'ieldTarget9RequestIdERK8QVariantb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNfc:QNearFieldTarget.RequestId'),
               ('address', 'value', 'QtCore:QVariant'),
               ('bool', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNearFieldTargetPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNearFieldTargetPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QNearFieldTargetPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def uid(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNearFieldTargetPrivate::uid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#uid

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNearFieldTargetPrivate::uid() const
    ritual = 'ritual_ZNK23QNearFieldTargetPrivate3uidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QNearFieldTargetPrivate3uidEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> QNearFieldTarget.Type:
    """
    Calls Qt's 'QNearFieldTarget::Type QNearFieldTargetPrivate::type()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#type

    Returns
    -------

    QNearFieldTarget.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNearFieldTarget.Type(number)' gives.
    """
    #  QNearFieldTarget::Type QNearFieldTargetPrivate::type() const
    ritual = 'ritual_ZNK23QNearFieldTargetPrivate4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QNearFieldTargetPrivate4typeEv'
    return QNearFieldTarget.Type(self.uglySide.call(ritual))

  def accessMethods(self) -> QNearFieldTarget.AccessMethods:
    """
    Calls Qt's 'QNearFieldTarget::AccessMethods
    QNearFieldTargetPrivate::accessMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#accessMethods

    Returns
    -------

    QNearFieldTarget.AccessMethods
      The value standing for the combination Qt gave back.
    """
    #  QNearFieldTarget::AccessMethods
    #      QNearFieldTargetPrivate::accessMethods() const
    ritual = 'ritual_ZNK23QNearFieldTargetPrivate13accessMethodsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QNearFieldTargetPrivate13accessMethodsEv'
    return QNearFieldTarget.AccessMethods(self.uglySide.call(ritual))

  def maxCommandLength(self) -> int:
    """
    Calls Qt's 'int QNearFieldTargetPrivate::maxCommandLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#maxCommandLength
    """
    #  int QNearFieldTargetPrivate::maxCommandLength() const
    ritual = 'ritual_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv'
    return self.uglySide.call(ritual)

  @overload(QNearFieldTarget.RequestId)
  def requestResponse(self, id: QNearFieldTarget.RequestId) -> QVariant:
    """
    Calls Qt's 'QVariant QNearFieldTargetPrivate::requestResponse(const
    QNearFieldTarget::RequestId &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#requestResponse

    Parameters
    ----------

    id : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNearFieldTargetPrivate::requestResponse(const
    #      QNearFieldTarget::RequestId &id) const
    address = self.uglySide.call(
        'ritual_ZNK23QNearFieldTargetPrivate15requestResponseERKN16QNearFie'
        'ldTarget9RequestIdE',
        self._valueOf(id),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNearFieldTarget.RequestId, QVariant)
  @overload(QNearFieldTarget.RequestId, QVariant, bool)
  def setResponseForRequest(
      self,
      id: QNearFieldTarget.RequestId,
      response: QVariant,
      emitRequestCompleted: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QNearFieldTargetPrivate::setResponseForRequest(const
    QNearFieldTarget::RequestId &id, const QVariant &response, bool
    emitRequestCompleted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#setResponseForRequest

    Parameters
    ----------

    id : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.

    response : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    emitRequestCompleted : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QNearFieldTargetPrivate::setResponseForRequest(const
    #      QNearFieldTarget::RequestId &id, const QVariant &response, bool
    #      emitRequestCompleted)
    self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate21setResponseForRequestERKN16QNe'
        'arFieldTarget9RequestIdERK8QVariantb',
        self._valueOf(id), self._valueOf(response), emitRequestCompleted,
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
    Qt's 'QNearFieldTargetPrivate::QNearFieldTargetPrivate(QObject *parent)':
    leans on 'QNearFieldTargetPrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNearFieldTargetPrivate.__init__' has no cute function yet. Qt's "
        "'QNearFieldTargetPrivate::QNearFieldTargetPrivate(QObject "
        "*parent)': leans on "
        "'QNearFieldTargetPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def disconnect(self) -> bool:
    """
    Calls Qt's 'bool QNearFieldTargetPrivate::disconnect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#disconnect
    """
    #  bool QNearFieldTargetPrivate::disconnect()
    ritual = 'ritual_ZN23QNearFieldTargetPrivate10disconnectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QNearFieldTargetPrivate10disconnectEv'
    return self.uglySide.call(ritual)

  def hasNdefMessage(self) -> bool:
    """
    Calls Qt's 'bool QNearFieldTargetPrivate::hasNdefMessage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#hasNdefMessage
    """
    #  bool QNearFieldTargetPrivate::hasNdefMessage()
    ritual = 'ritual_ZN23QNearFieldTargetPrivate14hasNdefMessageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QNearFieldTargetPrivate14hasNdefMessageEv'
    return self.uglySide.call(ritual)

  def readNdefMessages(self) -> QNearFieldTarget.RequestId:
    """
    Calls Qt's 'QNearFieldTarget::RequestId
    QNearFieldTargetPrivate::readNdefMessages()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#readNdefMessages

    Returns
    -------

    QNearFieldTarget.RequestId
      A new cute QNearFieldTarget::RequestId around the copy Qt gave back.
      Python owns it.
    """
    #  QNearFieldTarget::RequestId
    #      QNearFieldTargetPrivate::readNdefMessages()
    address = self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate16readNdefMessagesEv',
    )
    return QNearFieldTarget.RequestId._cuteOwning(address)

  @overload(QList[QNdefMessage])
  def writeNdefMessages(
      self,
      messages: QList[QNdefMessage],
  ) -> QNearFieldTarget.RequestId:
    """
    Calls Qt's 'QNearFieldTarget::RequestId
    QNearFieldTargetPrivate::writeNdefMessages(const QList<QNdefMessage>
    &messages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#writeNdefMessages

    Parameters
    ----------

    messages : QList[QNdefMessage]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QNearFieldTarget.RequestId
      A new cute QNearFieldTarget::RequestId around the copy Qt gave back.
      Python owns it.
    """
    #  QNearFieldTarget::RequestId
    #      QNearFieldTargetPrivate::writeNdefMessages(const
    #      QList<QNdefMessage> &messages)
    address = self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate17writeNdefMessagesERK5QListI12Q'
        'NdefMessageE',
        self._valueOf(messages),
    )
    return QNearFieldTarget.RequestId._cuteOwning(address)

  @overload(QByteArray)
  def sendCommand(self, command: QByteArray) -> QNearFieldTarget.RequestId:
    """
    Calls Qt's 'QNearFieldTarget::RequestId
    QNearFieldTargetPrivate::sendCommand(const QByteArray &command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#sendCommand

    Parameters
    ----------

    command : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QNearFieldTarget.RequestId
      A new cute QNearFieldTarget::RequestId around the copy Qt gave back.
      Python owns it.
    """
    #  QNearFieldTarget::RequestId QNearFieldTargetPrivate::sendCommand(const
    #      QByteArray &command)
    address = self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate11sendCommandERK10QByteArray',
        self._valueOf(command),
    )
    return QNearFieldTarget.RequestId._cuteOwning(address)

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QNearFieldTargetPrivate::disconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#disconnected
    """
    #  void QNearFieldTargetPrivate::disconnected()
    self.uglySide.call('ritual_ZN23QNearFieldTargetPrivate12disconnectedEv')

  @overload(QNdefMessage)
  def ndefMessageRead(self, message: QNdefMessage) -> None:
    """
    Calls Qt's 'void QNearFieldTargetPrivate::ndefMessageRead(const
    QNdefMessage &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#ndefMessageRead

    Parameters
    ----------

    message : QNdefMessage
      Passed on as a value: Qt reads the C++ QNdefMessage, which stays
      Python's own.
    """
    #  void QNearFieldTargetPrivate::ndefMessageRead(const QNdefMessage
    #      &message)
    self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate15ndefMessageReadERK12QNdefMessa'
        'ge',
        self._valueOf(message),
    )

  @overload(QNearFieldTarget.RequestId)
  def requestCompleted(self, id: QNearFieldTarget.RequestId) -> None:
    """
    Calls Qt's 'void QNearFieldTargetPrivate::requestCompleted(const
    QNearFieldTarget::RequestId &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#requestCompleted

    Parameters
    ----------

    id : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNearFieldTargetPrivate::requestCompleted(const
    #      QNearFieldTarget::RequestId &id)
    self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate16requestCompletedERKN16QNearFie'
        'ldTarget9RequestIdE',
        self._valueOf(id),
    )

  @overload(QNearFieldTarget.Error, QNearFieldTarget.RequestId)
  def error(
      self,
      error: QNearFieldTarget.Error,
      id: QNearFieldTarget.RequestId,
  ) -> None:
    """
    Calls Qt's 'void QNearFieldTargetPrivate::error(QNearFieldTarget::Error
    error, const QNearFieldTarget::RequestId &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtargetprivate.html#error

    Parameters
    ----------

    error : QNearFieldTarget.Error
      Passed on as its number.

    id : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNearFieldTargetPrivate::error(QNearFieldTarget::Error error,
    #      const QNearFieldTarget::RequestId &id)
    self.uglySide.call(
        'ritual_ZN23QNearFieldTargetPrivate5errorEN16QNearFieldTarget5Error'
        'ERKNS0_9RequestIdE',
        error.value, self._valueOf(id),
    )

  @staticmethod
  def reportError(*__, **_) -> Never:
    """
    Qt's 'void QNearFieldTargetPrivate::reportError(QNearFieldTarget::Error
    error, const QNearFieldTarget::RequestId &id)': leans on
    'QNearFieldTargetPrivate::error(QNearFieldTarget::Error,
    QNearFieldTarget::RequestId const&)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNearFieldTargetPrivate.reportError' has no cute function yet. "
        "Qt's 'void "
        "QNearFieldTargetPrivate::reportError(QNearFieldTarget::Error "
        "error, const QNearFieldTarget::RequestId &id)': leans on "
        "'QNearFieldTargetPrivate::error(QNearFieldTarget::Error, "
        "QNearFieldTarget::RequestId const&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def waitForRequestCompleted(*__, **_) -> Never:
    """
    Qt's 'bool QNearFieldTargetPrivate::waitForRequestCompleted(const
    QNearFieldTarget::RequestId &id, int msecs)': leans on
    'QNearFieldTargetPrivate::error(QNearFieldTarget::Error,
    QNearFieldTarget::RequestId const&)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNearFieldTargetPrivate.waitForRequestCompleted' has no cute "
        "function yet. Qt's 'bool "
        "QNearFieldTargetPrivate::waitForRequestCompleted(const "
        "QNearFieldTarget::RequestId &id, int msecs)': leans on "
        "'QNearFieldTargetPrivate::error(QNearFieldTarget::Error, "
        "QNearFieldTarget::RequestId const&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
