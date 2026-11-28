"""
QNetworkReplyHttpImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyhttpimpl_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkReplyHttpImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QNetworkReplyHttpImplPrivate, QSslConfiguration, QSslError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']


class QNetworkReplyHttpImpl(QNetworkReply):
  """
  The cute side of Qt's QNetworkReplyHttpImpl: a plain Python object standing
  in front of one C++ QNetworkReplyHttpImpl.

  It is built on the cute 'QNetworkReply', as Qt's QNetworkReplyHttpImpl is
  built on Qt's QNetworkReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyHttpImpl that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'close', 'abort',
  'bytesAvailable', 'isSequential', 'size', 'setReadBufferSize',
  'canReadLine', 'd_func', 'ignoreSslErrors',
  'ignoreSslErrorsImplementation', 'setSslConfigurationImplementation',
  'startHttpRequest', 'abortHttpRequest', 'readBufferSizeChanged',
  'readBufferFreed', 'startHttpRequestSynchronously', 'haveUploadData'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkReplyHttpImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkReplyHttpImpl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkReplyHttpImpl::~QNetworkReplyHttpImpl()': the destructor:
    Python never removes a C++ QNetworkReplyHttpImpl.
  - Qt's 'qint64 QNetworkReplyHttpImpl::readData(char *a0, qint64 a1)': names
    'char', which has no cute class yet.
  - Qt's 'const QNetworkReplyHttpImplPrivate *QNetworkReplyHttpImpl::d_func()
    const': takes in Python what 'QNetworkReplyHttpImplPrivate
    *QNetworkReplyHttpImpl::d_func()' takes.
  - Qt's 'void
    QNetworkReplyHttpImpl::sslConfigurationImplementation(QSslConfiguration
    &configuration) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 29 functions Qt declares: 3 leans on 'QNetworkReplyHttpImpl; 2 not
  a gap.

  What to expect
  --------------

  - The C++ QNetworkReplyHttpImpl is created at the first use, not by
    'QNetworkReplyHttpImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyHttpImpl.
  - Qt tells when it has removed the C++ QNetworkReplyHttpImpl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkReplyHttpImpl that has no cute function yet,
    '__init__', 'abortImpl', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkReplyHttpImpl'

  #  A C++ QNetworkReplyHttpImpl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyHttpImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkReplyHttpImpl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkReplyHttpImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkReplyHttpImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyHttpImpl::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#bytesAvailable
    """
    #  qint64 QNetworkReplyHttpImpl::bytesAvailable() const
    ritual = 'ritual_ZNK21QNetworkReplyHttpImpl14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyHttpImpl14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyHttpImpl::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#isSequential
    """
    #  bool QNetworkReplyHttpImpl::isSequential() const
    ritual = 'ritual_ZNK21QNetworkReplyHttpImpl12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyHttpImpl12isSequentialEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyHttpImpl::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#size
    """
    #  qint64 QNetworkReplyHttpImpl::size() const
    ritual = 'ritual_ZNK21QNetworkReplyHttpImpl4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyHttpImpl4sizeEv'
    return self.uglySide.call(ritual)

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyHttpImpl::canReadLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#canReadLine
    """
    #  bool QNetworkReplyHttpImpl::canReadLine() const
    ritual = 'ritual_ZNK21QNetworkReplyHttpImpl11canReadLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkReplyHttpImpl11canReadLineEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::setReadBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImpl::setReadBufferSize(qint64 size)
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl17setReadBufferSizeEx', size,
    )

  @overload(QSslConfiguration)
  def setSslConfigurationImplementation(
      self,
      configuration: QSslConfiguration,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImpl::setSslConfigurationImplementation(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkReplyHttpImpl::setSslConfigurationImplementation(const
    #      QSslConfiguration &configuration)
    ritual = (
        'ritual_ZN21QNetworkReplyHttpImpl33setSslConfigurationImplementatio'
        'nERK17QSslConfiguration')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QNetworkReplyHttpImpl33setSslConfigurationImpleme'
          'ntationERK17QSslConfiguration')
    self.uglySide.call(ritual, self._valueOf(configuration))

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
    Qt's 'QNetworkReplyHttpImpl::QNetworkReplyHttpImpl(QNetworkAccessManager
    *const a0, const QNetworkRequest &a1, QNetworkAccessManager::Operation
    &a2, QIODevice *outgoingData)': leans on
    'QNetworkReplyHttpImpl::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImpl.__init__' has no cute function yet. Qt's "
        "'QNetworkReplyHttpImpl::QNetworkReplyHttpImpl(QNetworkAccessManager"
        " *const a0, const QNetworkRequest &a1, "
        "QNetworkAccessManager::Operation &a2, QIODevice *outgoingData)': "
        "leans on 'QNetworkReplyHttpImpl::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#close
    """
    #  void QNetworkReplyHttpImpl::close()
    self.uglySide.call('ritual_ZN21QNetworkReplyHttpImpl5closeEv')

  def abort(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#abort
    """
    #  void QNetworkReplyHttpImpl::abort()
    self.uglySide.call('ritual_ZN21QNetworkReplyHttpImpl5abortEv')

  def d_func(self) -> Optional[QNetworkReplyHttpImplPrivate]:
    """
    Calls Qt's 'QNetworkReplyHttpImplPrivate
    *QNetworkReplyHttpImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#d_func

    Returns
    -------

    Optional[QNetworkReplyHttpImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyHttpImplPrivate *QNetworkReplyHttpImpl::d_func()
    address = self.uglySide.call('ritual_ZN21QNetworkReplyHttpImpl6d_funcEv')
    from . import QNetworkReplyHttpImplPrivate
    return QNetworkReplyHttpImplPrivate._cuteAt(address)

  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::ignoreSslErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#ignoreSslErrors
    """
    #  void QNetworkReplyHttpImpl::ignoreSslErrors()
    ritual = 'ritual_ZN21QNetworkReplyHttpImpl15ignoreSslErrorsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkReplyHttpImpl15ignoreSslErrorsEv'
    self.uglySide.call(ritual)

  @overload(QList[QSslError])
  def ignoreSslErrorsImplementation(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImpl::ignoreSslErrorsImplementation(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkReplyHttpImpl::ignoreSslErrorsImplementation(const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl29ignoreSslErrorsImplementationERK'
        '5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  def startHttpRequest(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::startHttpRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#startHttpRequest
    """
    #  void QNetworkReplyHttpImpl::startHttpRequest()
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl16startHttpRequestEv',
    )

  def abortHttpRequest(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::abortHttpRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#abortHttpRequest
    """
    #  void QNetworkReplyHttpImpl::abortHttpRequest()
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl16abortHttpRequestEv',
    )

  @overload(int)
  def readBufferSizeChanged(self, size: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::readBufferSizeChanged(qint64
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#readBufferSizeChanged

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImpl::readBufferSizeChanged(qint64 size)
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl21readBufferSizeChangedEx', size,
    )

  @overload(int)
  def readBufferFreed(self, size: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::readBufferFreed(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#readBufferFreed

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImpl::readBufferFreed(qint64 size)
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl15readBufferFreedEx', size,
    )

  def startHttpRequestSynchronously(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::startHttpRequestSynchronously()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html
    """
    #  void QNetworkReplyHttpImpl::startHttpRequestSynchronously()
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl29startHttpRequestSynchronouslyEv',
    )

  @overload(int, QByteArray, bool, int)
  def haveUploadData(
      self,
      pos: int,
      dataArray: QByteArray,
      dataAtEnd: bool,
      dataSize: int,
  ) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImpl::haveUploadData(const qint64 pos,
    const QByteArray &dataArray, bool dataAtEnd, qint64 dataSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimpl.html#haveUploadData

    Parameters
    ----------

    pos : int
      Passed on as it is.

    dataArray : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    dataAtEnd : bool
      Passed on as it is.

    dataSize : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImpl::haveUploadData(const qint64 pos, const
    #      QByteArray &dataArray, bool dataAtEnd, qint64 dataSize)
    self.uglySide.call(
        'ritual_ZN21QNetworkReplyHttpImpl14haveUploadDataExRK10QByteArraybx',
        pos, self._valueOf(dataArray), dataAtEnd, dataSize,
    )

  @staticmethod
  def abortImpl(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImpl::abortImpl(QNetworkReply::NetworkError
    error)': leans on 'QNetworkReplyHttpImpl::abortHttpRequest()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImpl.abortImpl' has no cute function yet. Qt's "
        "'void QNetworkReplyHttpImpl::abortImpl(QNetworkReply::NetworkError "
        "error)': leans on 'QNetworkReplyHttpImpl::abortHttpRequest()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
