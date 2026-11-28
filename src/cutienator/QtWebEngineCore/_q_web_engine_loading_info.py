"""
QWebEngineLoadingInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineloadinginfo.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl


class QWebEngineLoadingInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineLoadingInfo: a plain Python object standing
  in front of one C++ QWebEngineLoadingInfo.

  C++ hands a QWebEngineLoadingInfo around as a copy, so every C++
  QWebEngineLoadingInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineLoadingInfo that has a ritual and that
  Python can call so far, 7 names in all: 'url', 'isErrorPage', 'status',
  'errorString', 'errorDomain', 'errorCode', 'isDownload'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineLoadingInfo &QWebEngineLoadingInfo::operator=(const
    QWebEngineLoadingInfo &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QWebEngineLoadingInfo::QWebEngineLoadingInfo(QWebEngineLoadingInfo
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineLoadingInfo
    &QWebEngineLoadingInfo::operator=(QWebEngineLoadingInfo &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineLoadingInfo::~QWebEngineLoadingInfo()': the destructor:
    Python removes its C++ QWebEngineLoadingInfo by it, and has no other use
    for it.
  - Qt's 'QMultiMap<QByteArray, QByteArray>
    QWebEngineLoadingInfo::responseHeaders() const': gives a type Python has
    no way to take yet.
  - Qt's 'QWebEngineLoadingInfo::QWebEngineLoadingInfo(const QUrl &url,
    LoadStatus status, bool isErrorPage, const QString &errorString, int
    errorCode, ErrorDomain errorDomain, const QMultiMap<QByteArray,
    QByteArray> &responseHeaders, bool isDownload)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 20 functions Qt declares: 3 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QWebEngineLoadingInfo is created at the first use, not by
    'QWebEngineLoadingInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineLoadingInfo back gives a copy the ritual
    made for Python, in a new cute QWebEngineLoadingInfo.
  - Each name of Qt's QWebEngineLoadingInfo that has no cute function yet,
    'd_func', 'responseHeaders', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineLoadingInfo, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ErrorDomain(CuteNum):
    """
    The enum 'QWebEngineLoadingInfo::ErrorDomain' of Qt, with the 8 names Qt
    gives in it.
    """

    NoErrorDomain = Kee[int](0)
    InternalErrorDomain = Kee[int](1)
    ConnectionErrorDomain = Kee[int](2)
    CertificateErrorDomain = Kee[int](3)
    HttpErrorDomain = Kee[int](4)
    FtpErrorDomain = Kee[int](5)
    DnsErrorDomain = Kee[int](6)
    HttpStatusCodeDomain = Kee[int](7)

  class LoadStatus(CuteNum):
    """
    The enum 'QWebEngineLoadingInfo::LoadStatus' of Qt, with the 4 names Qt
    gives in it.
    """

    LoadStartedStatus = Kee[int](0)
    LoadStoppedStatus = Kee[int](1)
    LoadSucceededStatus = Kee[int](2)
    LoadFailedStatus = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineLoadingInfo'

  #  Qt's '~QWebEngineLoadingInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineLoadingInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QWebEngineLoadingInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineLoadingInfo::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineloadinginfo.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineLoadingInfo::url() const
    address = self.uglySide.call('ritual_ZNK21QWebEngineLoadingInfo3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isErrorPage(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineLoadingInfo::isErrorPage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#isErrorPage
    """
    #  bool QWebEngineLoadingInfo::isErrorPage() const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineLoadingInfo11isErrorPageEv',
    )

  def status(self) -> LoadStatus:
    """
    Calls Qt's 'LoadStatus QWebEngineLoadingInfo::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineloadinginfo.html#status

    Returns
    -------

    LoadStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LoadStatus(number)'
      gives.
    """
    #  LoadStatus QWebEngineLoadingInfo::status() const
    return QWebEngineLoadingInfo.LoadStatus(self.uglySide.call(
        'ritual_ZNK21QWebEngineLoadingInfo6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebEngineLoadingInfo::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineLoadingInfo::errorString() const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineLoadingInfo11errorStringEv',
    )

  def errorDomain(self) -> ErrorDomain:
    """
    Calls Qt's 'ErrorDomain QWebEngineLoadingInfo::errorDomain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#errorDomain

    Returns
    -------

    ErrorDomain
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorDomain(number)'
      gives.
    """
    #  ErrorDomain QWebEngineLoadingInfo::errorDomain() const
    return QWebEngineLoadingInfo.ErrorDomain(self.uglySide.call(
        'ritual_ZNK21QWebEngineLoadingInfo11errorDomainEv',
    ))

  def errorCode(self) -> int:
    """
    Calls Qt's 'int QWebEngineLoadingInfo::errorCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#errorCode
    """
    #  int QWebEngineLoadingInfo::errorCode() const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineLoadingInfo9errorCodeEv',
    )

  def isDownload(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineLoadingInfo::isDownload() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#isDownload
    """
    #  bool QWebEngineLoadingInfo::isDownload() const
    return self.uglySide.call(
        'ritual_ZNK21QWebEngineLoadingInfo10isDownloadEv',
    )

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
    'QWebEngineLoadingInfo::QWebEngineLoadingInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#QWebEngineLoadingInfo
    """
    #  QWebEngineLoadingInfo::QWebEngineLoadingInfo()
    self._noteCreation(QWebEngineLoadingInfo, lambda: Rituals.call(
        'ritual_ZN21QWebEngineLoadingInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineLoadingInfo) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineLoadingInfo::QWebEngineLoadingInfo(const QWebEngineLoadingInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineloadinginfo.html#QWebEngineLoadingInfo

    Parameters
    ----------

    other : QWebEngineLoadingInfo
      Passed on as a value: Qt reads the C++ QWebEngineLoadingInfo, which
      stays Python's own.
    """
    #  QWebEngineLoadingInfo::QWebEngineLoadingInfo(const
    #      QWebEngineLoadingInfo &other)
    self._noteCreation(QWebEngineLoadingInfo, lambda: Rituals.call(
        'ritual_ZN21QWebEngineLoadingInfoC1ERKS_', self._valueOf(other),
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
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWebEngineLoadingInfoPrivate *QWebEngineLoadingInfo::d_func()':
      the compiler refuses its ritual as it would be written here: unknown
      type name 'QWebEngineLoadingInfoPrivate'; did you mean
      'QWebEngineLoadingInfo::QWebEngineLoadingInfoPrivate'?.
    - Qt's 'const QWebEngineLoadingInfoPrivate
      *QWebEngineLoadingInfo::d_func() const': the compiler refuses its
      ritual as it would be written here: unknown type name
      'QWebEngineLoadingInfoPrivate'; did you mean
      'QWebEngineLoadingInfo::QWebEngineLoadingInfoPrivate'?.
    """
    raise NotImplementedError(
        "'QWebEngineLoadingInfo.d_func' has no cute function yet. Qt's "
        "'QWebEngineLoadingInfoPrivate *QWebEngineLoadingInfo::d_func()': "
        "the compiler refuses its ritual as it would be written here: "
        "unknown type name 'QWebEngineLoadingInfoPrivate'; did you mean "
        "'QWebEngineLoadingInfo::QWebEngineLoadingInfoPrivate'?. Qt's "
        "'const QWebEngineLoadingInfoPrivate "
        "*QWebEngineLoadingInfo::d_func() const': the compiler refuses its "
        "ritual as it would be written here: unknown type name "
        "'QWebEngineLoadingInfoPrivate'; did you mean "
        "'QWebEngineLoadingInfo::QWebEngineLoadingInfoPrivate'?.")

  @staticmethod
  def responseHeaders(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QByteArray, QByteArray>
    QWebEngineLoadingInfo::responseHeaders() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineLoadingInfo.responseHeaders' has no cute function yet. "
        "Qt's 'QMultiMap<QByteArray, QByteArray> "
        "QWebEngineLoadingInfo::responseHeaders() const': gives a type "
        "Python has no way to take yet.")
