"""
QWebEngineProfile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineprofile.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QWebEnginePermission

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from ..QtNetwork import QSslCertificate
  from . import QWebEngineClientCertificateStore, QWebEngineClientHints
  from . import QWebEngineCookieStore, QWebEngineDownloadRequest
  from . import QWebEngineExtensionManager, QWebEngineScriptCollection
  from . import QWebEngineSettings, QWebEngineUrlRequestInterceptor
  from . import QWebEngineUrlSchemeHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']
  QWebEngineDownloadRequest = WAIT['QWebEngineDownloadRequest']
  QWebEngineUrlRequestInterceptor = WAIT['QWebEngineUrlRequestInterceptor']
  QWebEngineUrlSchemeHandler = WAIT['QWebEngineUrlSchemeHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineProfile(QObject):
  """
  The cute side of Qt's QWebEngineProfile: a plain Python object standing in
  front of one C++ QWebEngineProfile.

  It is built on the cute 'QObject', as Qt's QWebEngineProfile is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineProfile that has a ritual and that Python
  can call so far, 52 names in all: 'metaObject', 'tr', 'storageName',
  'isOffTheRecord', 'persistentStoragePath', 'setPersistentStoragePath',
  'cachePath', 'setCachePath', 'httpUserAgent', 'setHttpUserAgent',
  'httpCacheType', 'setHttpCacheType', 'setHttpAcceptLanguage',
  'httpAcceptLanguage', 'persistentCookiesPolicy',
  'setPersistentCookiesPolicy', 'persistentPermissionsPolicy',
  'setPersistentPermissionsPolicy', 'httpCacheMaximumSize',
  'setHttpCacheMaximumSize', 'cookieStore', 'setUrlRequestInterceptor',
  'clearAllVisitedLinks', 'clearVisitedLinks', 'visitedLinksContainsUrl',
  'settings', 'scripts', 'clientHints', 'urlSchemeHandler',
  'installUrlSchemeHandler', 'removeUrlScheme', 'removeUrlSchemeHandler',
  'removeAllUrlSchemeHandlers', 'clearHttpCache', 'setSpellCheckLanguages',
  'spellCheckLanguages', 'setSpellCheckEnabled', 'isSpellCheckEnabled',
  'downloadPath', 'setDownloadPath', 'isPushServiceEnabled',
  'setPushServiceEnabled', 'clientCertificateStore',
  'additionalTrustedCertificates', 'queryPermission', 'listAllPermissions',
  'listPermissionsForOrigin', 'listPermissionsForPermissionType',
  'extensionManager', 'defaultProfile', 'downloadRequested',
  'clearHttpCacheCompleted'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineProfile::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWebEngineProfile::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineProfile::~QWebEngineProfile()': the destructor: Python
    never removes a C++ QWebEngineProfile.
  - Qt's 'void QWebEngineProfile::setNotificationPresenter(std::function<void
    (std::unique_ptr<QWebEngineNotification>)> notificationPresenter)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QWebEngineProfile::requestIconForPageURL(const QUrl &url, int
    desiredSizeInPixel, std::function<void (const QIcon &, const QUrl &,
    const QUrl &)> iconAvailableCallback) const': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QWebEngineProfile::requestIconForIconURL(const QUrl &url, int
    desiredSizeInPixel, std::function<void (const QIcon &, const QUrl &)>
    iconAvailableCallback) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QWebEngineProfile::setCryptoModulePasswordFunction(std::function<std::
    string (std::string, std::string, bool)> passwordFunction)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QWebEngineProfilePrivate *QWebEngineProfile::d_func()': gives
    'QWebEngineProfilePrivate', which has no cute class yet.
  - Qt's 'const QWebEngineProfilePrivate *QWebEngineProfile::d_func() const':
    gives 'QWebEngineProfilePrivate', which has no cute class yet.
  - Qt's 'QWebEngineProfile::QWebEngineProfile(QWebEngineProfilePrivate *a0,
    QObject *parent)': names 'QWebEngineProfilePrivate', which has no cute
    class yet.
  - Qt's 'std::function<void (std::unique_ptr<QWebEngineNotification>)>
    QWebEngineProfile::notificationPresenter()': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  4 of the 69 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineProfile is created at the first use, not by
    'QWebEngineProfile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineProfile.
  - Qt tells when it has removed the C++ QWebEngineProfile. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineProfile that has no cute function yet,
    'notificationPresenter', 'requestIconForIconURL',
    'requestIconForPageURL', 'setCryptoModulePasswordFunction',
    'setNotificationPresenter', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineProfile, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HttpCacheType(CuteNum):
    """
    The enum 'QWebEngineProfile::HttpCacheType' of Qt, with the 3 names Qt
    gives in it.
    """

    MemoryHttpCache = Kee[int](0)
    DiskHttpCache = Kee[int](1)
    NoCache = Kee[int](2)

  class PersistentCookiesPolicy(CuteNum):
    """
    The enum 'QWebEngineProfile::PersistentCookiesPolicy' of Qt, with the 4
    names Qt gives in it.
    """

    NoPersistentCookies = Kee[int](0)
    AllowPersistentCookies = Kee[int](1)
    ForcePersistentCookies = Kee[int](2)
    OnlyPersistentCookies = Kee[int](3)

  class PersistentPermissionsPolicy(CuteNum, scoped=True):
    """
    The enum 'QWebEngineProfile::PersistentPermissionsPolicy' of Qt, with the
    3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    AskEveryTime = Kee[int](0)
    StoreInMemory = Kee[int](1)
    StoreOnDisk = Kee[int](2)

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
    Calls Qt's 'QString QWebEngineProfile::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#tr

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
    #  QString QWebEngineProfile::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QWebEngineProfile2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultProfile() -> Optional[QWebEngineProfile]:
    """
    Calls Qt's 'QWebEngineProfile *QWebEngineProfile::defaultProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#defaultProfile

    Returns
    -------

    Optional[QWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineProfile *QWebEngineProfile::defaultProfile()
    address = Rituals.call('ritual_ZN17QWebEngineProfile14defaultProfileEv')
    return QWebEngineProfile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineProfile'

  #  A C++ QWebEngineProfile Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineProfile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineProfile::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineProfile::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def storageName(self) -> str:
    """
    Calls Qt's 'QString QWebEngineProfile::storageName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#storageName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineProfile::storageName() const
    return self.uglySide.call('ritual_ZNK17QWebEngineProfile11storageNameEv')

  def isOffTheRecord(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineProfile::isOffTheRecord() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#isOffTheRecord
    """
    #  bool QWebEngineProfile::isOffTheRecord() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile14isOffTheRecordEv',
    )

  def persistentStoragePath(self) -> str:
    """
    Calls Qt's 'QString QWebEngineProfile::persistentStoragePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#persistentStoragePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineProfile::persistentStoragePath() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile21persistentStoragePathEv',
    )

  def cachePath(self) -> str:
    """
    Calls Qt's 'QString QWebEngineProfile::cachePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#cachePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineProfile::cachePath() const
    return self.uglySide.call('ritual_ZNK17QWebEngineProfile9cachePathEv')

  def httpUserAgent(self) -> str:
    """
    Calls Qt's 'QString QWebEngineProfile::httpUserAgent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#httpUserAgent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineProfile::httpUserAgent() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile13httpUserAgentEv',
    )

  def httpCacheType(self) -> HttpCacheType:
    """
    Calls Qt's 'HttpCacheType QWebEngineProfile::httpCacheType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#httpCacheType

    Returns
    -------

    HttpCacheType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HttpCacheType(number)'
      gives.
    """
    #  HttpCacheType QWebEngineProfile::httpCacheType() const
    return QWebEngineProfile.HttpCacheType(self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile13httpCacheTypeEv',
    ))

  def httpAcceptLanguage(self) -> str:
    """
    Calls Qt's 'QString QWebEngineProfile::httpAcceptLanguage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#httpAcceptLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineProfile::httpAcceptLanguage() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile18httpAcceptLanguageEv',
    )

  def persistentCookiesPolicy(self) -> PersistentCookiesPolicy:
    """
    Calls Qt's 'PersistentCookiesPolicy
    QWebEngineProfile::persistentCookiesPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#persistentCookiesPolicy

    Returns
    -------

    PersistentCookiesPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PersistentCookiesPolicy(number)' gives.
    """
    #  PersistentCookiesPolicy QWebEngineProfile::persistentCookiesPolicy()
    #      const
    return QWebEngineProfile.PersistentCookiesPolicy(self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile23persistentCookiesPolicyEv',
    ))

  def persistentPermissionsPolicy(self) -> PersistentPermissionsPolicy:
    """
    Calls Qt's 'PersistentPermissionsPolicy
    QWebEngineProfile::persistentPermissionsPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#persistentPermissionsPolicy

    Returns
    -------

    PersistentPermissionsPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PersistentPermissionsPolicy(number)' gives.
    """
    #  PersistentPermissionsPolicy
    #      QWebEngineProfile::persistentPermissionsPolicy() const
    return QWebEngineProfile.PersistentPermissionsPolicy(self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile27persistentPermissionsPolicyEv',
    ))

  def httpCacheMaximumSize(self) -> int:
    """
    Calls Qt's 'int QWebEngineProfile::httpCacheMaximumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#httpCacheMaximumSize
    """
    #  int QWebEngineProfile::httpCacheMaximumSize() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile20httpCacheMaximumSizeEv',
    )

  @overload(QUrl)
  def visitedLinksContainsUrl(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QWebEngineProfile::visitedLinksContainsUrl(const QUrl
    &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#visitedLinksContainsUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QWebEngineProfile::visitedLinksContainsUrl(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile23visitedLinksContainsUrlERK4QUrl',
        self._valueOf(url),
    )

  def settings(self) -> Optional[QWebEngineSettings]:
    """
    Calls Qt's 'QWebEngineSettings *QWebEngineProfile::settings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#settings

    Returns
    -------

    Optional[QWebEngineSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineSettings *QWebEngineProfile::settings() const
    address = self.uglySide.call('ritual_ZNK17QWebEngineProfile8settingsEv')
    from . import QWebEngineSettings
    return QWebEngineSettings._cuteAt(address)

  def scripts(self) -> Optional[QWebEngineScriptCollection]:
    """
    Calls Qt's 'QWebEngineScriptCollection *QWebEngineProfile::scripts()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#scripts

    Returns
    -------

    Optional[QWebEngineScriptCollection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineScriptCollection *QWebEngineProfile::scripts() const
    address = self.uglySide.call('ritual_ZNK17QWebEngineProfile7scriptsEv')
    from . import QWebEngineScriptCollection
    return QWebEngineScriptCollection._cuteAt(address)

  def clientHints(self) -> Optional[QWebEngineClientHints]:
    """
    Calls Qt's 'QWebEngineClientHints *QWebEngineProfile::clientHints()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#clientHints

    Returns
    -------

    Optional[QWebEngineClientHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineClientHints *QWebEngineProfile::clientHints() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile11clientHintsEv',
    )
    from . import QWebEngineClientHints
    return QWebEngineClientHints._cuteAt(address)

  @overload(QByteArray)
  def urlSchemeHandler(
      self,
      a0: QByteArray,
  ) -> Optional[QWebEngineUrlSchemeHandler]:
    """
    Calls Qt's 'const QWebEngineUrlSchemeHandler
    *QWebEngineProfile::urlSchemeHandler(const QByteArray &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#urlSchemeHandler

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QWebEngineUrlSchemeHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWebEngineUrlSchemeHandler
    #      *QWebEngineProfile::urlSchemeHandler(const QByteArray &a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile16urlSchemeHandlerERK10QByteArray',
        self._valueOf(a0),
    )
    from . import QWebEngineUrlSchemeHandler
    return QWebEngineUrlSchemeHandler._cuteAt(address)

  def spellCheckLanguages(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebEngineProfile::spellCheckLanguages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#spellCheckLanguages

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebEngineProfile::spellCheckLanguages() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile19spellCheckLanguagesEv',
    )
    return QStringList._cuteOwning(address)

  def isSpellCheckEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineProfile::isSpellCheckEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#isSpellCheckEnabled
    """
    #  bool QWebEngineProfile::isSpellCheckEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile19isSpellCheckEnabledEv',
    )

  def downloadPath(self) -> str:
    """
    Calls Qt's 'QString QWebEngineProfile::downloadPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#downloadPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineProfile::downloadPath() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile12downloadPathEv',
    )

  def isPushServiceEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineProfile::isPushServiceEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#isPushServiceEnabled
    """
    #  bool QWebEngineProfile::isPushServiceEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile20isPushServiceEnabledEv',
    )

  def additionalTrustedCertificates(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QWebEngineProfile::additionalTrustedCertificates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate>
    #      QWebEngineProfile::additionalTrustedCertificates() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile29additionalTrustedCertificatesEv',
    )
    from ..QtNetwork import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  @overload(QUrl, QWebEnginePermission.PermissionType)
  def queryPermission(
      self,
      securityOrigin: QUrl,
      permissionType: QWebEnginePermission.PermissionType,
  ) -> QWebEnginePermission:
    """
    Calls Qt's 'QWebEnginePermission QWebEngineProfile::queryPermission(const
    QUrl &securityOrigin, QWebEnginePermission::PermissionType
    permissionType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#queryPermission

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    permissionType : QWebEnginePermission.PermissionType
      Passed on as its number.

    Returns
    -------

    QWebEnginePermission
      A new cute QWebEnginePermission around the copy Qt gave back. Python
      owns it.
    """
    #  QWebEnginePermission QWebEngineProfile::queryPermission(const QUrl
    #      &securityOrigin, QWebEnginePermission::PermissionType
    #      permissionType) const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile15queryPermissionERK4QUrlN20QWebEngin'
        'ePermission14PermissionTypeE',
        self._valueOf(securityOrigin), permissionType.value,
    )
    return QWebEnginePermission._cuteOwning(address)

  def listAllPermissions(self) -> QList[QWebEnginePermission]:
    """
    Calls Qt's 'QList<QWebEnginePermission>
    QWebEngineProfile::listAllPermissions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#listAllPermissions

    Returns
    -------

    QList[QWebEnginePermission]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEnginePermission> QWebEngineProfile::listAllPermissions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile18listAllPermissionsEv',
    )
    return QList[QWebEnginePermission]._cuteOwning(address)

  @overload(QUrl)
  def listPermissionsForOrigin(
      self,
      securityOrigin: QUrl,
  ) -> QList[QWebEnginePermission]:
    """
    Calls Qt's 'QList<QWebEnginePermission>
    QWebEngineProfile::listPermissionsForOrigin(const QUrl &securityOrigin)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#listPermissionsForOrigin

    Parameters
    ----------

    securityOrigin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QList[QWebEnginePermission]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEnginePermission>
    #      QWebEngineProfile::listPermissionsForOrigin(const QUrl
    #      &securityOrigin) const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile24listPermissionsForOriginERK4QUrl',
        self._valueOf(securityOrigin),
    )
    return QList[QWebEnginePermission]._cuteOwning(address)

  @overload(QWebEnginePermission.PermissionType)
  def listPermissionsForPermissionType(
      self,
      permissionType: QWebEnginePermission.PermissionType,
  ) -> QList[QWebEnginePermission]:
    """
    Calls Qt's 'QList<QWebEnginePermission>
    QWebEngineProfile::listPermissionsForPermissionType(
    QWebEnginePermission::PermissionType permissionType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html

    Parameters
    ----------

    permissionType : QWebEnginePermission.PermissionType
      Passed on as its number.

    Returns
    -------

    QList[QWebEnginePermission]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEnginePermission>
    #      QWebEngineProfile::listPermissionsForPermissionType(
    #      QWebEnginePermission::PermissionType permissionType) const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile32listPermissionsForPermissionTypeEN2'
        '0QWebEnginePermission14PermissionTypeE',
        permissionType.value,
    )
    return QList[QWebEnginePermission]._cuteOwning(address)

  def extensionManager(self) -> Optional[QWebEngineExtensionManager]:
    """
    Calls Qt's 'QWebEngineExtensionManager
    *QWebEngineProfile::extensionManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#extensionManager

    Returns
    -------

    Optional[QWebEngineExtensionManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineExtensionManager *QWebEngineProfile::extensionManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QWebEngineProfile16extensionManagerEv',
    )
    from . import QWebEngineExtensionManager
    return QWebEngineExtensionManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPersistentStoragePath(self, path: str) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setPersistentStoragePath(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setPersistentStoragePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineProfile::setPersistentStoragePath(const QString &path)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile24setPersistentStoragePathERK7QString',
        path,
    )

  @overload(str)
  def setCachePath(self, path: str) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setCachePath(const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setCachePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineProfile::setCachePath(const QString &path)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile12setCachePathERK7QString', path,
    )

  @overload(str)
  def setHttpUserAgent(self, userAgent: str) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setHttpUserAgent(const QString
    &userAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpUserAgent

    Parameters
    ----------

    userAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineProfile::setHttpUserAgent(const QString &userAgent)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile16setHttpUserAgentERK7QString',
        userAgent,
    )

  @overload(HttpCacheType)
  def setHttpCacheType(self, a0: HttpCacheType) -> None:
    """
    Calls Qt's 'void
    QWebEngineProfile::setHttpCacheType(QWebEngineProfile::HttpCacheType
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpCacheType

    Parameters
    ----------

    a0 : HttpCacheType
      Passed on as its number.
    """
    #  void QWebEngineProfile::setHttpCacheType(QWebEngineProfile::
    #      HttpCacheType a0)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile16setHttpCacheTypeENS_13HttpCacheTypeE',
        a0.value,
    )

  @overload(str)
  def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setHttpAcceptLanguage(const QString
    &httpAcceptLanguage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpAcceptLanguage

    Parameters
    ----------

    httpAcceptLanguage : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineProfile::setHttpAcceptLanguage(const QString
    #      &httpAcceptLanguage)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile21setHttpAcceptLanguageERK7QString',
        httpAcceptLanguage,
    )

  @overload(PersistentCookiesPolicy)
  def setPersistentCookiesPolicy(self, a0: PersistentCookiesPolicy) -> None:
    """
    Calls Qt's 'void
    QWebEngineProfile::setPersistentCookiesPolicy(QWebEngineProfile::
    PersistentCookiesPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setPersistentCookiesPolicy

    Parameters
    ----------

    a0 : PersistentCookiesPolicy
      Passed on as its number.
    """
    #  void QWebEngineProfile::setPersistentCookiesPolicy(QWebEngineProfile::
    #      PersistentCookiesPolicy a0)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile26setPersistentCookiesPolicyENS_23Pers'
        'istentCookiesPolicyE',
        a0.value,
    )

  @overload(PersistentPermissionsPolicy)
  def setPersistentPermissionsPolicy(
      self,
      a0: PersistentPermissionsPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QWebEngineProfile::setPersistentPermissionsPolicy(QWebEngineProfile::
    PersistentPermissionsPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html

    Parameters
    ----------

    a0 : PersistentPermissionsPolicy
      Passed on as its number.
    """
    #  void QWebEngineProfile::setPersistentPermissionsPolicy(
    #      QWebEngineProfile::PersistentPermissionsPolicy a0)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile30setPersistentPermissionsPolicyENS_27'
        'PersistentPermissionsPolicyE',
        a0.value,
    )

  @overload(int)
  def setHttpCacheMaximumSize(self, maxSize: int) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setHttpCacheMaximumSize(int
    maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setHttpCacheMaximumSize

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  void QWebEngineProfile::setHttpCacheMaximumSize(int maxSize)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile23setHttpCacheMaximumSizeEi', maxSize,
    )

  @overload(QWebEngineUrlRequestInterceptor)
  @overload(NoneType)
  def setUrlRequestInterceptor(
      self,
      interceptor: Optional[QWebEngineUrlRequestInterceptor],
  ) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setUrlRequestInterceptor(
    QWebEngineUrlRequestInterceptor *interceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setUrlRequestInterceptor

    Parameters
    ----------

    interceptor : Optional[QWebEngineUrlRequestInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineProfile::setUrlRequestInterceptor(
    #      QWebEngineUrlRequestInterceptor *interceptor)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile24setUrlRequestInterceptorEP31QWebEngi'
        'neUrlRequestInterceptor',
        self._addressOf(interceptor),
    )

  @overload(QStringList)
  def setSpellCheckLanguages(self, languages: QStringList) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setSpellCheckLanguages(const
    QStringList &languages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setSpellCheckLanguages

    Parameters
    ----------

    languages : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebEngineProfile::setSpellCheckLanguages(const QStringList
    #      &languages)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile22setSpellCheckLanguagesERK5QListI7QSt'
        'ringE',
        self._valueOf(languages),
    )

  @overload(bool)
  def setSpellCheckEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setSpellCheckEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setSpellCheckEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWebEngineProfile::setSpellCheckEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile20setSpellCheckEnabledEb', enabled,
    )

  @overload(str)
  def setDownloadPath(self, path: str) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setDownloadPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setDownloadPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineProfile::setDownloadPath(const QString &path)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile15setDownloadPathERK7QString', path,
    )

  @overload(bool)
  def setPushServiceEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::setPushServiceEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#setPushServiceEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWebEngineProfile::setPushServiceEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile21setPushServiceEnabledEb', enabled,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineProfile::QWebEngineProfile(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#QWebEngineProfile

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineProfile::QWebEngineProfile(QObject *parent)
    self._noteCreation(QWebEngineProfile, lambda: Rituals.call(
        'ritual_ZN17QWebEngineProfileC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, name: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineProfile::QWebEngineProfile(const QString &name, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#QWebEngineProfile

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineProfile::QWebEngineProfile(const QString &name, QObject
    #      *parent)
    self._noteCreation(QWebEngineProfile, lambda: Rituals.call(
        'ritual_ZN17QWebEngineProfileC1ERK7QStringP7QObject',
        name, self._addressOf(parent, 'QObject'),
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

  def cookieStore(self) -> Optional[QWebEngineCookieStore]:
    """
    Calls Qt's 'QWebEngineCookieStore *QWebEngineProfile::cookieStore()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineprofile.html#cookieStore

    Returns
    -------

    Optional[QWebEngineCookieStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineCookieStore *QWebEngineProfile::cookieStore()
    address = self.uglySide.call(
        'ritual_ZN17QWebEngineProfile11cookieStoreEv',
    )
    from . import QWebEngineCookieStore
    return QWebEngineCookieStore._cuteAt(address)

  def clearAllVisitedLinks(self) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::clearAllVisitedLinks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#clearAllVisitedLinks
    """
    #  void QWebEngineProfile::clearAllVisitedLinks()
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile20clearAllVisitedLinksEv',
    )

  @overload(QList[QUrl])
  def clearVisitedLinks(self, urls: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::clearVisitedLinks(const QList<QUrl>
    &urls)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#clearVisitedLinks

    Parameters
    ----------

    urls : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebEngineProfile::clearVisitedLinks(const QList<QUrl> &urls)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile17clearVisitedLinksERK5QListI4QUrlE',
        self._valueOf(urls),
    )

  @overload(QByteArray, QWebEngineUrlSchemeHandler)
  @overload(QByteArray, NoneType)
  def installUrlSchemeHandler(
      self,
      scheme: QByteArray,
      a1: Optional[QWebEngineUrlSchemeHandler],
  ) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::installUrlSchemeHandler(const
    QByteArray &scheme, QWebEngineUrlSchemeHandler *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#installUrlSchemeHandler

    Parameters
    ----------

    scheme : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : Optional[QWebEngineUrlSchemeHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineProfile::installUrlSchemeHandler(const QByteArray
    #      &scheme, QWebEngineUrlSchemeHandler *a1)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile23installUrlSchemeHandlerERK10QByteArr'
        'ayP26QWebEngineUrlSchemeHandler',
        self._valueOf(scheme), self._addressOf(a1),
    )

  @overload(QByteArray)
  def removeUrlScheme(self, scheme: QByteArray) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::removeUrlScheme(const QByteArray
    &scheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#removeUrlScheme

    Parameters
    ----------

    scheme : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebEngineProfile::removeUrlScheme(const QByteArray &scheme)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile15removeUrlSchemeERK10QByteArray',
        self._valueOf(scheme),
    )

  @overload(QWebEngineUrlSchemeHandler)
  @overload(NoneType)
  def removeUrlSchemeHandler(
      self,
      a0: Optional[QWebEngineUrlSchemeHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QWebEngineProfile::removeUrlSchemeHandler(QWebEngineUrlSchemeHandler
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#removeUrlSchemeHandler

    Parameters
    ----------

    a0 : Optional[QWebEngineUrlSchemeHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineProfile::removeUrlSchemeHandler(
    #      QWebEngineUrlSchemeHandler *a0)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile22removeUrlSchemeHandlerEP26QWebEngine'
        'UrlSchemeHandler',
        self._addressOf(a0),
    )

  def removeAllUrlSchemeHandlers(self) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::removeAllUrlSchemeHandlers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#removeAllUrlSchemeHandlers
    """
    #  void QWebEngineProfile::removeAllUrlSchemeHandlers()
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile26removeAllUrlSchemeHandlersEv',
    )

  def clearHttpCache(self) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::clearHttpCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#clearHttpCache
    """
    #  void QWebEngineProfile::clearHttpCache()
    self.uglySide.call('ritual_ZN17QWebEngineProfile14clearHttpCacheEv')

  def clientCertificateStore(
      self,
  ) -> Optional[QWebEngineClientCertificateStore]:
    """
    Calls Qt's 'QWebEngineClientCertificateStore
    *QWebEngineProfile::clientCertificateStore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#clientCertificateStore

    Returns
    -------

    Optional[QWebEngineClientCertificateStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineClientCertificateStore
    #      *QWebEngineProfile::clientCertificateStore()
    address = self.uglySide.call(
        'ritual_ZN17QWebEngineProfile22clientCertificateStoreEv',
    )
    from . import QWebEngineClientCertificateStore
    return QWebEngineClientCertificateStore._cuteAt(address)

  @overload(QWebEngineDownloadRequest)
  @overload(NoneType)
  def downloadRequested(
      self,
      download: Optional[QWebEngineDownloadRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QWebEngineProfile::downloadRequested(QWebEngineDownloadRequest
    *download)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#downloadRequested

    Parameters
    ----------

    download : Optional[QWebEngineDownloadRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineProfile::downloadRequested(QWebEngineDownloadRequest
    #      *download)
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile17downloadRequestedEP25QWebEngineDownl'
        'oadRequest',
        self._addressOf(download),
    )

  def clearHttpCacheCompleted(self) -> None:
    """
    Calls Qt's 'void QWebEngineProfile::clearHttpCacheCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineprofile.html#clearHttpCacheCompleted
    """
    #  void QWebEngineProfile::clearHttpCacheCompleted()
    self.uglySide.call(
        'ritual_ZN17QWebEngineProfile23clearHttpCacheCompletedEv',
    )

  @staticmethod
  def notificationPresenter(*__, **_) -> Never:
    """
    Qt's 'std::function<void (std::unique_ptr<QWebEngineNotification>)>
    QWebEngineProfile::notificationPresenter()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfile.notificationPresenter' has no cute function "
        "yet. Qt's 'std::function<void "
        "(std::unique_ptr<QWebEngineNotification>)> "
        "QWebEngineProfile::notificationPresenter()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def requestIconForIconURL(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineProfile::requestIconForIconURL(const QUrl &url, int
    desiredSizeInPixel, std::function<void (const QIcon &, const QUrl &)>
    iconAvailableCallback) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfile.requestIconForIconURL' has no cute function "
        "yet. Qt's 'void QWebEngineProfile::requestIconForIconURL(const "
        "QUrl &url, int desiredSizeInPixel, std::function<void (const QIcon "
        "&, const QUrl &)> iconAvailableCallback) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def requestIconForPageURL(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineProfile::requestIconForPageURL(const QUrl &url, int
    desiredSizeInPixel, std::function<void (const QIcon &, const QUrl &,
    const QUrl &)> iconAvailableCallback) const': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfile.requestIconForPageURL' has no cute function "
        "yet. Qt's 'void QWebEngineProfile::requestIconForPageURL(const "
        "QUrl &url, int desiredSizeInPixel, std::function<void (const QIcon "
        "&, const QUrl &, const QUrl &)> iconAvailableCallback) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setCryptoModulePasswordFunction(*__, **_) -> Never:
    """
    Qt's 'void
    QWebEngineProfile::setCryptoModulePasswordFunction(std::function<std::
    string (std::string, std::string, bool)> passwordFunction)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfile.setCryptoModulePasswordFunction' has no cute "
        "function yet. Qt's 'void "
        "QWebEngineProfile::setCryptoModulePasswordFunction(std::function<st"
        "d::string (std::string, std::string, bool)> passwordFunction)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setNotificationPresenter(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineProfile::setNotificationPresenter(std::function<void
    (std::unique_ptr<QWebEngineNotification>)> notificationPresenter)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineProfile.setNotificationPresenter' has no cute function "
        "yet. Qt's 'void "
        "QWebEngineProfile::setNotificationPresenter(std::function<void "
        "(std::unique_ptr<QWebEngineNotification>)> "
        "notificationPresenter)': takes a type Python has no way to hand "
        "over yet.")
