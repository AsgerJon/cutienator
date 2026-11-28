"""
QWebEngineDownloadRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginedownloadrequest.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QWebEnginePage

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineDownloadRequest(QObject):
  """
  The cute side of Qt's QWebEngineDownloadRequest: a plain Python object
  standing in front of one C++ QWebEngineDownloadRequest.

  It is built on the cute 'QObject', as Qt's QWebEngineDownloadRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineDownloadRequest that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'tr', 'id', 'state',
  'totalBytes', 'receivedBytes', 'url', 'mimeType', 'isFinished', 'isPaused',
  'savePageFormat', 'setSavePageFormat', 'interruptReason',
  'interruptReasonString', 'isSavePageDownload', 'suggestedFileName',
  'downloadDirectory', 'setDownloadDirectory', 'downloadFileName',
  'setDownloadFileName', 'page', 'accept', 'cancel', 'pause', 'resume',
  'stateChanged', 'savePageFormatChanged', 'receivedBytesChanged',
  'totalBytesChanged', 'interruptReasonChanged', 'isFinishedChanged',
  'isPausedChanged', 'downloadDirectoryChanged', 'downloadFileNameChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineDownloadRequest::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWebEngineDownloadRequest::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineDownloadRequest::~QWebEngineDownloadRequest()': the
    destructor: Python never removes a C++ QWebEngineDownloadRequest.
  - Qt's 'QWebEngineDownloadRequestPrivate
    *QWebEngineDownloadRequest::d_func()': gives
    'QWebEngineDownloadRequestPrivate', which has no cute class yet.
  - Qt's 'const QWebEngineDownloadRequestPrivate
    *QWebEngineDownloadRequest::d_func() const': gives
    'QWebEngineDownloadRequestPrivate', which has no cute class yet.
  - Qt's 'QWebEngineDownloadRequest::QWebEngineDownloadRequest(
    QWebEngineDownloadRequestPrivate *a0, QObject *parent)': names
    'QWebEngineDownloadRequestPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 44 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineDownloadRequest is created at the first use, not by
    'QWebEngineDownloadRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineDownloadRequest.
  - Qt tells when it has removed the C++ QWebEngineDownloadRequest. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineDownloadRequest that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineDownloadRequest, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DownloadInterruptReason(CuteNum):
    """
    The enum 'QWebEngineDownloadRequest::DownloadInterruptReason' of Qt, with
    the 24 names Qt gives in it.
    """

    NoReason = Kee[int](0)
    FileFailed = Kee[int](1)
    FileAccessDenied = Kee[int](2)
    FileNoSpace = Kee[int](3)
    FileNameTooLong = Kee[int](5)
    FileTooLarge = Kee[int](6)
    FileVirusInfected = Kee[int](7)
    FileTransientError = Kee[int](10)
    FileBlocked = Kee[int](11)
    FileSecurityCheckFailed = Kee[int](12)
    FileTooShort = Kee[int](13)
    FileHashMismatch = Kee[int](14)
    NetworkFailed = Kee[int](20)
    NetworkTimeout = Kee[int](21)
    NetworkDisconnected = Kee[int](22)
    NetworkServerDown = Kee[int](23)
    NetworkInvalidRequest = Kee[int](24)
    ServerFailed = Kee[int](30)
    ServerBadContent = Kee[int](33)
    ServerUnauthorized = Kee[int](34)
    ServerCertProblem = Kee[int](35)
    ServerForbidden = Kee[int](36)
    ServerUnreachable = Kee[int](37)
    UserCanceled = Kee[int](40)

  class DownloadState(CuteNum):
    """
    The enum 'QWebEngineDownloadRequest::DownloadState' of Qt, with the 5
    names Qt gives in it.
    """

    DownloadRequested = Kee[int](0)
    DownloadInProgress = Kee[int](1)
    DownloadCompleted = Kee[int](2)
    DownloadCancelled = Kee[int](3)
    DownloadInterrupted = Kee[int](4)

  class SavePageFormat(CuteNum):
    """
    The enum 'QWebEngineDownloadRequest::SavePageFormat' of Qt, with the 4
    names Qt gives in it.
    """

    UnknownSaveFormat = Kee[int](-1)
    SingleHtmlSaveFormat = Kee[int](0)
    CompleteHtmlSaveFormat = Kee[int](1)
    MimeHtmlSaveFormat = Kee[int](2)

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
    Calls Qt's 'QString QWebEngineDownloadRequest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#tr

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
    #  QString QWebEngineDownloadRequest::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QWebEngineDownloadRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineDownloadRequest'

  #  A C++ QWebEngineDownloadRequest Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineDownloadRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineDownloadRequest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineDownloadRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def id(self) -> int:
    """
    Calls Qt's 'quint32 QWebEngineDownloadRequest::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#id
    """
    #  quint32 QWebEngineDownloadRequest::id() const
    return self.uglySide.call('ritual_ZNK25QWebEngineDownloadRequest2idEv')

  def state(self) -> DownloadState:
    """
    Calls Qt's 'DownloadState QWebEngineDownloadRequest::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#state

    Returns
    -------

    DownloadState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DownloadState(number)'
      gives.
    """
    #  DownloadState QWebEngineDownloadRequest::state() const
    return QWebEngineDownloadRequest.DownloadState(self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest5stateEv',
    ))

  def totalBytes(self) -> int:
    """
    Calls Qt's 'qint64 QWebEngineDownloadRequest::totalBytes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#totalBytes
    """
    #  qint64 QWebEngineDownloadRequest::totalBytes() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest10totalBytesEv',
    )

  def receivedBytes(self) -> int:
    """
    Calls Qt's 'qint64 QWebEngineDownloadRequest::receivedBytes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#receivedBytes
    """
    #  qint64 QWebEngineDownloadRequest::receivedBytes() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest13receivedBytesEv',
    )

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineDownloadRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineDownloadRequest::url() const
    address = self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def mimeType(self) -> str:
    """
    Calls Qt's 'QString QWebEngineDownloadRequest::mimeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#mimeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineDownloadRequest::mimeType() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest8mimeTypeEv',
    )

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineDownloadRequest::isFinished() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#isFinished
    """
    #  bool QWebEngineDownloadRequest::isFinished() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest10isFinishedEv',
    )

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineDownloadRequest::isPaused() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#isPaused
    """
    #  bool QWebEngineDownloadRequest::isPaused() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest8isPausedEv',
    )

  def savePageFormat(self) -> SavePageFormat:
    """
    Calls Qt's 'SavePageFormat QWebEngineDownloadRequest::savePageFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#savePageFormat

    Returns
    -------

    SavePageFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SavePageFormat(number)'
      gives.
    """
    #  SavePageFormat QWebEngineDownloadRequest::savePageFormat() const
    return QWebEngineDownloadRequest.SavePageFormat(self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest14savePageFormatEv',
    ))

  def interruptReason(self) -> DownloadInterruptReason:
    """
    Calls Qt's 'DownloadInterruptReason
    QWebEngineDownloadRequest::interruptReason() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#interruptReason

    Returns
    -------

    DownloadInterruptReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'DownloadInterruptReason(number)' gives.
    """
    #  DownloadInterruptReason QWebEngineDownloadRequest::interruptReason()
    #      const
    return QWebEngineDownloadRequest.DownloadInterruptReason(
        self.uglySide.call(
            'ritual_ZNK25QWebEngineDownloadRequest15interruptReasonEv',
        ))

  def interruptReasonString(self) -> str:
    """
    Calls Qt's 'QString QWebEngineDownloadRequest::interruptReasonString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineDownloadRequest::interruptReasonString() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest21interruptReasonStringEv',
    )

  def isSavePageDownload(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineDownloadRequest::isSavePageDownload() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#isSavePageDownload
    """
    #  bool QWebEngineDownloadRequest::isSavePageDownload() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest18isSavePageDownloadEv',
    )

  def suggestedFileName(self) -> str:
    """
    Calls Qt's 'QString QWebEngineDownloadRequest::suggestedFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#suggestedFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineDownloadRequest::suggestedFileName() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest17suggestedFileNameEv',
    )

  def downloadDirectory(self) -> str:
    """
    Calls Qt's 'QString QWebEngineDownloadRequest::downloadDirectory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#downloadDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineDownloadRequest::downloadDirectory() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest17downloadDirectoryEv',
    )

  def downloadFileName(self) -> str:
    """
    Calls Qt's 'QString QWebEngineDownloadRequest::downloadFileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#downloadFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineDownloadRequest::downloadFileName() const
    return self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest16downloadFileNameEv',
    )

  def page(self) -> Optional[QWebEnginePage]:
    """
    Calls Qt's 'QWebEnginePage *QWebEngineDownloadRequest::page() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#page

    Returns
    -------

    Optional[QWebEnginePage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEnginePage *QWebEngineDownloadRequest::page() const
    address = self.uglySide.call(
        'ritual_ZNK25QWebEngineDownloadRequest4pageEv',
    )
    from . import QWebEnginePage
    return QWebEnginePage._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SavePageFormat)
  def setSavePageFormat(self, format: SavePageFormat) -> None:
    """
    Calls Qt's 'void
    QWebEngineDownloadRequest::setSavePageFormat(SavePageFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#setSavePageFormat

    Parameters
    ----------

    format : SavePageFormat
      Passed on as its number.
    """
    #  void QWebEngineDownloadRequest::setSavePageFormat(SavePageFormat
    #      format)
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest17setSavePageFormatENS_14SaveP'
        'ageFormatE',
        format.value,
    )

  @overload(str)
  def setDownloadDirectory(self, directory: str) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::setDownloadDirectory(const
    QString &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineDownloadRequest::setDownloadDirectory(const QString
    #      &directory)
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest20setDownloadDirectoryERK7QStr'
        'ing',
        directory,
    )

  @overload(str)
  def setDownloadFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::setDownloadFileName(const
    QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#setDownloadFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineDownloadRequest::setDownloadFileName(const QString
    #      &fileName)
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest19setDownloadFileNameERK7QStri'
        'ng',
        fileName,
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
    Qt's 'QWebEngineDownloadRequest::QWebEngineDownloadRequest(
    QWebEngineDownloadRequestPrivate *a0, QObject *parent)': names
    'QWebEngineDownloadRequestPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineDownloadRequest.__init__' has no cute function yet. "
        "Qt's "
        "'QWebEngineDownloadRequest::QWebEngineDownloadRequest(QWebEngineDow"
        "nloadRequestPrivate *a0, QObject *parent)': names "
        "'QWebEngineDownloadRequestPrivate', which has no cute class yet.")

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

  def accept(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#accept
    """
    #  void QWebEngineDownloadRequest::accept()
    self.uglySide.call('ritual_ZN25QWebEngineDownloadRequest6acceptEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#cancel
    """
    #  void QWebEngineDownloadRequest::cancel()
    self.uglySide.call('ritual_ZN25QWebEngineDownloadRequest6cancelEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::pause()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#pause
    """
    #  void QWebEngineDownloadRequest::pause()
    self.uglySide.call('ritual_ZN25QWebEngineDownloadRequest5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::resume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#resume
    """
    #  void QWebEngineDownloadRequest::resume()
    self.uglySide.call('ritual_ZN25QWebEngineDownloadRequest6resumeEv')

  @overload(DownloadState)
  def stateChanged(self, state: DownloadState) -> None:
    """
    Calls Qt's 'void
    QWebEngineDownloadRequest::stateChanged(QWebEngineDownloadRequest::
    DownloadState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#stateChanged

    Parameters
    ----------

    state : DownloadState
      Passed on as its number.
    """
    #  void QWebEngineDownloadRequest::stateChanged(
    #      QWebEngineDownloadRequest::DownloadState state)
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest12stateChangedENS_13DownloadSt'
        'ateE',
        state.value,
    )

  def savePageFormatChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::savePageFormatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html
    """
    #  void QWebEngineDownloadRequest::savePageFormatChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest21savePageFormatChangedEv',
    )

  def receivedBytesChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::receivedBytesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html
    """
    #  void QWebEngineDownloadRequest::receivedBytesChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest20receivedBytesChangedEv',
    )

  def totalBytesChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::totalBytesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#totalBytesChanged
    """
    #  void QWebEngineDownloadRequest::totalBytesChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest17totalBytesChangedEv',
    )

  def interruptReasonChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::interruptReasonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html
    """
    #  void QWebEngineDownloadRequest::interruptReasonChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest22interruptReasonChangedEv',
    )

  def isFinishedChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::isFinishedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#isFinishedChanged
    """
    #  void QWebEngineDownloadRequest::isFinishedChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest17isFinishedChangedEv',
    )

  def isPausedChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::isPausedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html#isPausedChanged
    """
    #  void QWebEngineDownloadRequest::isPausedChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest15isPausedChangedEv',
    )

  def downloadDirectoryChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::downloadDirectoryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html
    """
    #  void QWebEngineDownloadRequest::downloadDirectoryChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest24downloadDirectoryChangedEv',
    )

  def downloadFileNameChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineDownloadRequest::downloadFileNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginedownloadrequest.html
    """
    #  void QWebEngineDownloadRequest::downloadFileNameChanged()
    self.uglySide.call(
        'ritual_ZN25QWebEngineDownloadRequest23downloadFileNameChangedEv',
    )
