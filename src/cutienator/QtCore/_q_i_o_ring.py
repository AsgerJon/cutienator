"""
QIORing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qioring_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QIORing to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QIORing(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIORing: a plain Python object standing in front of
  one C++ QIORing.

  What exists
  -----------

  Every function of Qt's QIORing that has a ritual and that Python can call
  so far, 8 names in all: 'sharedInstance', 'ensureInitialized',
  'supportsOperation', 'submitRequests', 'submissionQueueSize',
  'completionQueueSize', 'initializeIORing', 'isResultFailure'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIORing::~QIORing()': the destructor: Python never removes a C++
    QIORing.
  - Qt's 'bool QIORing::waitForRequest(RequestHandle handle, QDeadlineTimer
    deadline)': names 'RequestHandleTag', which has no cute class yet.
  - Qt's 'QueuedRequestStatus
    QIORing::queueRequestInternal(GenericRequestType &request)': takes a type
    Python has no way to hand over yet.
  - Qt's 'ReadWriteStatus QIORing::handleReadCompletion(size_t value,
    QSpan<std::byte> *destinations, void *voidExtra, SetResultFn setResult)':
    names 'QSpan<std::byte>', which has no cute class yet.
  - Qt's 'ReadWriteStatus QIORing::handleWriteCompletion(size_t value, const
    QSpan<const std::byte> *sources, void *voidExtra, SetResultFn
    setResult)': names 'QSpan<const std::byte>', which has no cute class yet.
  - Qt's 'void QIORing::finalizeReadWriteCompletion(GenericRequestType
    *request, ReadWriteStatus rwstatus)': names
    'QIORing::GenericRequestType', which has no cute class yet.

  What has no ritual
  ------------------

  18 of the 33 functions Qt declares: 6 a template; 5 cannot be called and
  cannot be called through the meta-object and cannot be copied; 4 forbidden;
  3 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QIORing is created at the first use, not by 'QIORing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIORing.
  - Each name of Qt's QIORing that has no cute function yet,
    'completionReady', 'finalizeReadWriteCompletion',
    'finishRequestWithError', 'getVectoredOpAddressAndSize',
    'handleReadCompletion', 'handleWriteCompletion', 'invokeOnOp',
    'mapFileError', 'prepareRequest', 'prepareRequests', 'queueRequest',
    'queueRequestInternal', 'setFileErrorResult', 'verifyFd',
    'waitForCompletions', 'waitForRequest', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def sharedInstance() -> Optional[QIORing]:
    """
    Calls Qt's 'QIORing *QIORing::sharedInstance()'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#sharedInstance

    Returns
    -------

    Optional[QIORing]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIORing *QIORing::sharedInstance()
    address = Rituals.call('ritual_ZN7QIORing14sharedInstanceEv')
    return QIORing._cuteAt(address)

  @staticmethod
  @overload(QtPrivate.Operation)
  def supportsOperation(op: QtPrivate.Operation) -> bool:
    """
    Calls Qt's 'bool QIORing::supportsOperation(Operation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#supportsOperation

    Parameters
    ----------

    op : QtPrivate.Operation
      Passed on as its number.
    """
    #  bool QIORing::supportsOperation(Operation op)
    return Rituals.call(
        'ritual_ZN7QIORing17supportsOperationEN9QtPrivate9OperationE',
        op.value,
    )

  @staticmethod
  @overload(int)
  def isResultFailure(result: int) -> bool:
    """
    Calls Qt's 'bool QIORing::isResultFailure(NativeResultType result)'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#isResultFailure

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  bool QIORing::isResultFailure(NativeResultType result)
    return Rituals.call('ritual_ZN7QIORing15isResultFailureEi', result)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIORing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def submissionQueueSize(self) -> int:
    """
    Calls Qt's 'quint32 QIORing::submissionQueueSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#submissionQueueSize
    """
    #  quint32 QIORing::submissionQueueSize() const
    return self.uglySide.call('ritual_ZNK7QIORing19submissionQueueSizeEv')

  def completionQueueSize(self) -> int:
    """
    Calls Qt's 'quint32 QIORing::completionQueueSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#completionQueueSize
    """
    #  quint32 QIORing::completionQueueSize() const
    return self.uglySide.call('ritual_ZNK7QIORing19completionQueueSizeEv')

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
  @overload(int)
  @overload(int, int)
  def __init__(
      self,
      submissionQueueSize: int = 128,
      completionQueueSize: int = 256,
  ) -> None:
    """
    Notes what was given, for Qt's 'QIORing::QIORing(quint32
    submissionQueueSize, quint32 completionQueueSize)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#QIORing

    Parameters
    ----------

    submissionQueueSize : int
      Passed on as it is. May be left out, as in Qt: it is then 128.

    completionQueueSize : int
      Passed on as it is. May be left out, as in Qt: it is then 256.
    """
    #  QIORing::QIORing(quint32 submissionQueueSize, quint32
    #      completionQueueSize)
    self._noteCreation(QIORing, lambda: Rituals.call(
        'ritual_ZN7QIORingC1Ejj', submissionQueueSize, completionQueueSize,
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

  def ensureInitialized(self) -> bool:
    """
    Calls Qt's 'bool QIORing::ensureInitialized()'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#ensureInitialized
    """
    #  bool QIORing::ensureInitialized()
    return self.uglySide.call('ritual_ZN7QIORing17ensureInitializedEv')

  def submitRequests(self) -> None:
    """
    Calls Qt's 'void QIORing::submitRequests()'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#submitRequests
    """
    #  void QIORing::submitRequests()
    self.uglySide.call('ritual_ZN7QIORing14submitRequestsEv')

  def initializeIORing(self) -> bool:
    """
    Calls Qt's 'bool QIORing::initializeIORing()'.

    Qt's own words: https://doc.qt.io/qt-6/qioring.html#initializeIORing
    """
    #  bool QIORing::initializeIORing()
    return self.uglySide.call('ritual_ZN7QIORing16initializeIORingEv')

  @staticmethod
  def completionReady(*__, **_) -> Never:
    """
    Qt's 'void QIORing::completionReady()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QIORing.completionReady' has no cute function yet. Qt's 'void "
        "QIORing::completionReady()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def finalizeReadWriteCompletion(*__, **_) -> Never:
    """
    Qt's 'void QIORing::finalizeReadWriteCompletion(GenericRequestType
    *request, ReadWriteStatus rwstatus)': names
    'QIORing::GenericRequestType', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QIORing.finalizeReadWriteCompletion' has no cute function yet. "
        "Qt's 'void QIORing::finalizeReadWriteCompletion(GenericRequestType "
        "*request, ReadWriteStatus rwstatus)': names "
        "'QIORing::GenericRequestType', which has no cute class yet.")

  @staticmethod
  def finishRequestWithError(*__, **_) -> Never:
    """
    Qt's 'void QIORing::finishRequestWithError(GenericRequestType &req,
    QFileDevice::FileError error)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: no member named
    'HasResultMember' in namespace 'QtPrivate'.
    """
    raise NotImplementedError(
        "'QIORing.finishRequestWithError' has no cute function yet. Qt's "
        "'void QIORing::finishRequestWithError(GenericRequestType &req, "
        "QFileDevice::FileError error)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "no member named 'HasResultMember' in namespace 'QtPrivate'.")

  @staticmethod
  def getVectoredOpAddressAndSize(*__, **_) -> Never:
    """
    Qt's 'QIORing::getVectoredOpAddressAndSize': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QIORing.getVectoredOpAddressAndSize' has no cute function yet. "
        "Qt's 'QIORing::getVectoredOpAddressAndSize': a template: a pattern "
        "and no single function.")

  @staticmethod
  def handleReadCompletion(*__, **_) -> Never:
    """
    - Qt's 'ReadWriteStatus QIORing::handleReadCompletion(size_t value,
      QSpan<std::byte> *destinations, void *voidExtra, SetResultFn
      setResult)': names 'QSpan<std::byte>', which has no cute class yet.
    - Qt's 'QIORing::handleReadCompletion': a template: a pattern and no
      single function.
    """
    raise NotImplementedError(
        "'QIORing.handleReadCompletion' has no cute function yet. Qt's "
        "'ReadWriteStatus QIORing::handleReadCompletion(size_t value, "
        "QSpan<std::byte> *destinations, void *voidExtra, SetResultFn "
        "setResult)': names 'QSpan<std::byte>', which has no cute class "
        "yet. Qt's 'QIORing::handleReadCompletion': a template: a pattern "
        "and no single function.")

  @staticmethod
  def handleWriteCompletion(*__, **_) -> Never:
    """
    - Qt's 'ReadWriteStatus QIORing::handleWriteCompletion(size_t value,
      const QSpan<const std::byte> *sources, void *voidExtra, SetResultFn
      setResult)': names 'QSpan<const std::byte>', which has no cute class
      yet.
    - Qt's 'QIORing::handleWriteCompletion': a template: a pattern and no
      single function.
    """
    raise NotImplementedError(
        "'QIORing.handleWriteCompletion' has no cute function yet. Qt's "
        "'ReadWriteStatus QIORing::handleWriteCompletion(size_t value, "
        "const QSpan<const std::byte> *sources, void *voidExtra, "
        "SetResultFn setResult)': names 'QSpan<const std::byte>', which has "
        "no cute class yet. Qt's 'QIORing::handleWriteCompletion': a "
        "template: a pattern and no single function.")

  @staticmethod
  def invokeOnOp(*__, **_) -> Never:
    """
    Qt's 'QIORing::invokeOnOp': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QIORing.invokeOnOp' has no cute function yet. Qt's "
        "'QIORing::invokeOnOp': a template: a pattern and no single "
        "function.")

  @staticmethod
  def mapFileError(*__, **_) -> Never:
    """
    Qt's 'QFileDevice::FileError QIORing::mapFileError(NativeResultType
    result, QFileDevice::FileError defaultValue)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QIORing.mapFileError' has no cute function yet. Qt's "
        "'QFileDevice::FileError QIORing::mapFileError(NativeResultType "
        "result, QFileDevice::FileError defaultValue)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def prepareRequest(*__, **_) -> Never:
    """
    Qt's 'RequestPrepResult QIORing::prepareRequest(io_uring_sqe *sqe,
    GenericRequestType &request)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'maxReadWriteLen'.
    """
    raise NotImplementedError(
        "'QIORing.prepareRequest' has no cute function yet. Qt's "
        "'RequestPrepResult QIORing::prepareRequest(io_uring_sqe *sqe, "
        "GenericRequestType &request)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'maxReadWriteLen'.")

  @staticmethod
  def prepareRequests(*__, **_) -> Never:
    """
    Qt's 'void QIORing::prepareRequests()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QIORing.prepareRequests' has no cute function yet. Qt's 'void "
        "QIORing::prepareRequests()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def queueRequest(*__, **_) -> Never:
    """
    Qt's 'QIORing::queueRequest': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QIORing.queueRequest' has no cute function yet. Qt's "
        "'QIORing::queueRequest': a template: a pattern and no single "
        "function.")

  @staticmethod
  def queueRequestInternal(*__, **_) -> Never:
    """
    Qt's 'QueuedRequestStatus
    QIORing::queueRequestInternal(GenericRequestType &request)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QIORing.queueRequestInternal' has no cute function yet. Qt's "
        "'QueuedRequestStatus "
        "QIORing::queueRequestInternal(GenericRequestType &request)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def setFileErrorResult(*__, **_) -> Never:
    """
    - Qt's 'QIORing::setFileErrorResult': a template: a pattern and no single
      function.
    - Qt's 'void QIORing::setFileErrorResult(GenericRequestType &req,
      QFileDevice::FileError error)': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: no member
      named 'HasResultMember' in namespace 'QtPrivate'.
    """
    raise NotImplementedError(
        "'QIORing.setFileErrorResult' has no cute function yet. Qt's "
        "'QIORing::setFileErrorResult': a template: a pattern and no single "
        "function. Qt's 'void "
        "QIORing::setFileErrorResult(GenericRequestType &req, "
        "QFileDevice::FileError error)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "no member named 'HasResultMember' in namespace 'QtPrivate'.")

  @staticmethod
  def verifyFd(*__, **_) -> Never:
    """
    Qt's 'bool QIORing::verifyFd(GenericRequestType &req)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QIORing.verifyFd' has no cute function yet. Qt's 'bool "
        "QIORing::verifyFd(GenericRequestType &req)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def waitForCompletions(*__, **_) -> Never:
    """
    Qt's 'bool QIORing::waitForCompletions(QDeadlineTimer deadline)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QIORing.waitForCompletions' has no cute function yet. Qt's 'bool "
        "QIORing::waitForCompletions(QDeadlineTimer deadline)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def waitForRequest(*__, **_) -> Never:
    """
    Qt's 'bool QIORing::waitForRequest(RequestHandle handle, QDeadlineTimer
    deadline)': names 'RequestHandleTag', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QIORing.waitForRequest' has no cute function yet. Qt's 'bool "
        "QIORing::waitForRequest(RequestHandle handle, QDeadlineTimer "
        "deadline)': names 'RequestHandleTag', which has no cute class yet.")
