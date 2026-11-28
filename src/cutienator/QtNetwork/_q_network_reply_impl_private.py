"""
QNetworkReplyImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyimpl_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkReplyImplPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QNetworkReply, QNetworkReplyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QAbstractNetworkCache, QNetworkReplyImpl, QSslError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslError = WAIT['QSslError']
  QUrl = WAIT['QUrl']


class QNetworkReplyImplPrivate(QNetworkReplyPrivate):
  """
  The cute side of Qt's QNetworkReplyImplPrivate: a plain Python object
  standing in front of one C++ QNetworkReplyImplPrivate.

  It is built on the cute 'QNetworkReplyPrivate', as Qt's
  QNetworkReplyImplPrivate is built on Qt's QNetworkReplyPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyImplPrivate that has a ritual and that
  Python can call so far, 20 names in all: '_q_bufferOutgoingData',
  '_q_bufferOutgoingDataFinished', 'pauseNotificationHandling',
  'resumeNotificationHandling', 'backendNotify', 'createCache',
  'completeCacheSave', 'setCachingEnabled', 'isCachingEnabled',
  'nextDownstreamBlockSize', 'initCacheSaveDevice', 'finished', 'error',
  'metaDataChanged', 'redirectionRequested', 'encrypted', 'sslErrors',
  'readFromBackend', 'networkCache', 'q_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QNetworkReplyImplPrivate::setDownloadBuffer(QSharedPointer<char> sp,
    qint64 size)': takes a type Python has no way to hand over yet.
  - Qt's 'char *QNetworkReplyImplPrivate::getDownloadBuffer(qint64 size)':
    gives 'char', which has no cute class yet.
  - Qt's 'const QNetworkReplyImpl *QNetworkReplyImplPrivate::q_func() const':
    takes in Python what 'QNetworkReplyImpl
    *QNetworkReplyImplPrivate::q_func()' takes.

  What has no ritual
  ------------------

  11 of the 35 functions Qt declares: 10 leans on 'QNetworkReplyPrivate; 1
  cannot be called and cannot be called through the meta-object and cannot be
  copied.

  What to expect
  --------------

  - The C++ QNetworkReplyImplPrivate is created at the first use, not by
    'QNetworkReplyImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyImplPrivate.
  - Each name of Qt's QNetworkReplyImplPrivate that has no cute function yet,
    '_q_copyReadChannelFinished', '_q_copyReadyRead', '_q_startOperation',
    'appendDownstreamData', 'appendDownstreamDataDownloadBuffer',
    'appendDownstreamDataSignalEmissions', 'consume', 'emitUploadProgress',
    'getDownloadBuffer', 'handleNotifications', 'setDownloadBuffer', 'setup',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QNetworkReplyImplPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InternalNotifications(CuteNum):
    """
    The enum 'QNetworkReplyImplPrivate::InternalNotifications' of Qt, with
    the 1 names Qt gives in it.
    """

    NotifyDownstreamReadyWrite = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkReplyImplPrivate'

  #  A C++ QNetworkReplyImplPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyImplPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCachingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyImplPrivate::isCachingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#isCachingEnabled
    """
    #  bool QNetworkReplyImplPrivate::isCachingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QNetworkReplyImplPrivate16isCachingEnabledEv',
    )

  def nextDownstreamBlockSize(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyImplPrivate::nextDownstreamBlockSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html
    """
    #  qint64 QNetworkReplyImplPrivate::nextDownstreamBlockSize() const
    return self.uglySide.call(
        'ritual_ZNK24QNetworkReplyImplPrivate23nextDownstreamBlockSizeEv',
    )

  def networkCache(self) -> Optional[QAbstractNetworkCache]:
    """
    Calls Qt's 'QAbstractNetworkCache
    *QNetworkReplyImplPrivate::networkCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#networkCache

    Returns
    -------

    Optional[QAbstractNetworkCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractNetworkCache *QNetworkReplyImplPrivate::networkCache() const
    address = self.uglySide.call(
        'ritual_ZNK24QNetworkReplyImplPrivate12networkCacheEv',
    )
    from . import QAbstractNetworkCache
    return QAbstractNetworkCache._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCachingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::setCachingEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#setCachingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QNetworkReplyImplPrivate::setCachingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate17setCachingEnabledEb', enable,
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
    Notes what was given, for Qt's
    'QNetworkReplyImplPrivate::QNetworkReplyImplPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html
    """
    #  QNetworkReplyImplPrivate::QNetworkReplyImplPrivate()
    self._noteCreation(QNetworkReplyImplPrivate, lambda: Rituals.call(
        'ritual_ZN24QNetworkReplyImplPrivateC1Ev',
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

  def _q_bufferOutgoingData(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::_q_bufferOutgoingData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html
    """
    #  void QNetworkReplyImplPrivate::_q_bufferOutgoingData()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate21_q_bufferOutgoingDataEv',
    )

  def _q_bufferOutgoingDataFinished(self) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyImplPrivate::_q_bufferOutgoingDataFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html
    """
    #  void QNetworkReplyImplPrivate::_q_bufferOutgoingDataFinished()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate29_q_bufferOutgoingDataFinished'
        'Ev',
    )

  def pauseNotificationHandling(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::pauseNotificationHandling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html
    """
    #  void QNetworkReplyImplPrivate::pauseNotificationHandling()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate25pauseNotificationHandlingEv',
    )

  def resumeNotificationHandling(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::resumeNotificationHandling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html
    """
    #  void QNetworkReplyImplPrivate::resumeNotificationHandling()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate26resumeNotificationHandlingEv',
    )

  @overload(InternalNotifications)
  def backendNotify(self, notification: InternalNotifications) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyImplPrivate::backendNotify(InternalNotifications
    notification)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#backendNotify

    Parameters
    ----------

    notification : InternalNotifications
      Passed on as its number.
    """
    #  void QNetworkReplyImplPrivate::backendNotify(InternalNotifications
    #      notification)
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate13backendNotifyENS_21InternalNo'
        'tificationsE',
        notification.value,
    )

  def createCache(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::createCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#createCache
    """
    #  void QNetworkReplyImplPrivate::createCache()
    self.uglySide.call('ritual_ZN24QNetworkReplyImplPrivate11createCacheEv')

  def completeCacheSave(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::completeCacheSave()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#completeCacheSave
    """
    #  void QNetworkReplyImplPrivate::completeCacheSave()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate17completeCacheSaveEv',
    )

  def initCacheSaveDevice(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::initCacheSaveDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#initCacheSaveDevice
    """
    #  void QNetworkReplyImplPrivate::initCacheSaveDevice()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate19initCacheSaveDeviceEv',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#finished
    """
    #  void QNetworkReplyImplPrivate::finished()
    self.uglySide.call('ritual_ZN24QNetworkReplyImplPrivate8finishedEv')

  @overload(QNetworkReply.NetworkError, str)
  def error(
      self,
      code: QNetworkReply.NetworkError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyImplPrivate::error(QNetworkReply::NetworkError code, const
    QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#error

    Parameters
    ----------

    code : QNetworkReply.NetworkError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkReplyImplPrivate::error(QNetworkReply::NetworkError code,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate5errorEN13QNetworkReply12Networ'
        'kErrorERK7QString',
        code.value, errorString,
    )

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::metaDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#metaDataChanged
    """
    #  void QNetworkReplyImplPrivate::metaDataChanged()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate15metaDataChangedEv',
    )

  @overload(QUrl)
  def redirectionRequested(self, target: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::redirectionRequested(const
    QUrl &target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#redirectionRequested

    Parameters
    ----------

    target : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkReplyImplPrivate::redirectionRequested(const QUrl
    #      &target)
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate20redirectionRequestedERK4QUrl',
        self._valueOf(target),
    )

  def encrypted(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::encrypted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#encrypted
    """
    #  void QNetworkReplyImplPrivate::encrypted()
    self.uglySide.call('ritual_ZN24QNetworkReplyImplPrivate9encryptedEv')

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::sslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkReplyImplPrivate::sslErrors(const QList<QSslError>
    #      &errors)
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate9sslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  def readFromBackend(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImplPrivate::readFromBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#readFromBackend
    """
    #  void QNetworkReplyImplPrivate::readFromBackend()
    self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate15readFromBackendEv',
    )

  def q_func(self) -> Optional[QNetworkReplyImpl]:
    """
    Calls Qt's 'QNetworkReplyImpl *QNetworkReplyImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimplprivate.html#q_func

    Returns
    -------

    Optional[QNetworkReplyImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyImpl *QNetworkReplyImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QNetworkReplyImplPrivate6q_funcEv',
    )
    from . import QNetworkReplyImpl
    return QNetworkReplyImpl._cuteAt(address)

  @staticmethod
  def _q_copyReadChannelFinished(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyImplPrivate::_q_copyReadChannelFinished()': leans
    on 'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate._q_copyReadChannelFinished' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyImplPrivate::_q_copyReadChannelFinished()': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def _q_copyReadyRead(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyImplPrivate::_q_copyReadyRead()': leans on
    'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate._q_copyReadyRead' has no cute function "
        "yet. Qt's 'void QNetworkReplyImplPrivate::_q_copyReadyRead()': "
        "leans on 'QNetworkReplyPrivate::progressSignalInterval', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def _q_startOperation(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyImplPrivate::_q_startOperation()': leans on
    'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate._q_startOperation' has no cute function "
        "yet. Qt's 'void QNetworkReplyImplPrivate::_q_startOperation()': "
        "leans on 'QNetworkReplyPrivate::progressSignalInterval', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def appendDownstreamData(*__, **_) -> Never:
    """
    - Qt's 'void
      QNetworkReplyImplPrivate::appendDownstreamData(QByteDataBuffer &data)':
      leans on 'QNetworkReplyPrivate::progressSignalInterval', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'void QNetworkReplyImplPrivate::appendDownstreamData(QIODevice
      *data)': leans on 'QNetworkReplyPrivate::progressSignalInterval', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.appendDownstreamData' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyImplPrivate::appendDownstreamData(QByteDataBuffer "
        "&data)': leans on 'QNetworkReplyPrivate::progressSignalInterval', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's 'void "
        "QNetworkReplyImplPrivate::appendDownstreamData(QIODevice *data)': "
        "leans on 'QNetworkReplyPrivate::progressSignalInterval', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def appendDownstreamDataDownloadBuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReplyImplPrivate::appendDownstreamDataDownloadBuffer(qint64 a0,
    qint64 a1)': leans on 'QNetworkReplyPrivate::progressSignalInterval',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.appendDownstreamDataDownloadBuffer' has "
        "no cute function yet. Qt's 'void "
        "QNetworkReplyImplPrivate::appendDownstreamDataDownloadBuffer(qint64"
        " a0, qint64 a1)': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def appendDownstreamDataSignalEmissions(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReplyImplPrivate::appendDownstreamDataSignalEmissions()': leans
    on 'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.appendDownstreamDataSignalEmissions' has "
        "no cute function yet. Qt's 'void "
        "QNetworkReplyImplPrivate::appendDownstreamDataSignalEmissions()': "
        "leans on 'QNetworkReplyPrivate::progressSignalInterval', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def consume(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyImplPrivate::consume(qint64 count)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.consume' has no cute function yet. Qt's "
        "'void QNetworkReplyImplPrivate::consume(qint64 count)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def emitUploadProgress(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyImplPrivate::emitUploadProgress(qint64 bytesSent,
    qint64 bytesTotal)': leans on
    'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.emitUploadProgress' has no cute function "
        "yet. Qt's 'void "
        "QNetworkReplyImplPrivate::emitUploadProgress(qint64 bytesSent, "
        "qint64 bytesTotal)': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getDownloadBuffer(*__, **_) -> Never:
    """
    Qt's 'char *QNetworkReplyImplPrivate::getDownloadBuffer(qint64 size)':
    gives 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.getDownloadBuffer' has no cute function "
        "yet. Qt's 'char "
        "*QNetworkReplyImplPrivate::getDownloadBuffer(qint64 size)': gives "
        "'char', which has no cute class yet.")

  @staticmethod
  def handleNotifications(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyImplPrivate::handleNotifications()': leans on
    'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.handleNotifications' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyImplPrivate::handleNotifications()': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setDownloadBuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReplyImplPrivate::setDownloadBuffer(QSharedPointer<char> sp,
    qint64 size)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.setDownloadBuffer' has no cute function "
        "yet. Qt's 'void "
        "QNetworkReplyImplPrivate::setDownloadBuffer(QSharedPointer<char> "
        "sp, qint64 size)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def setup(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReplyImplPrivate::setup(QNetworkAccessManager::Operation op,
    const QNetworkRequest &request, QIODevice *outgoingData)': leans on
    'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImplPrivate.setup' has no cute function yet. Qt's "
        "'void "
        "QNetworkReplyImplPrivate::setup(QNetworkAccessManager::Operation "
        "op, const QNetworkRequest &request, QIODevice *outgoingData)': "
        "leans on 'QNetworkReplyPrivate::progressSignalInterval', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
