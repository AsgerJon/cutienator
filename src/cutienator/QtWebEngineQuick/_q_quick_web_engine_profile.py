"""
QQuickWebEngineProfile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/qquickwebengineprofile.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from ..QtWebEngineCore import QWebEnginePermission

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from ..QtWebEngineCore import QWebEngineClientCertificateStore
  from ..QtWebEngineCore import QWebEngineClientHints, QWebEngineCookieStore
  from ..QtWebEngineCore import QWebEngineExtensionManager
  from ..QtWebEngineCore import QWebEngineNotification
  from ..QtWebEngineCore import QWebEngineUrlRequestInterceptor
  from ..QtWebEngineCore import QWebEngineUrlSchemeHandler
  from . import QQuickWebEngineDownloadRequest
  from . import QQuickWebEngineScriptCollection, QQuickWebEngineSettings
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQuickWebEngineDownloadRequest = WAIT['QQuickWebEngineDownloadRequest']
  QUrl = WAIT['QUrl']
  QWebEngineNotification = WAIT['QWebEngineNotification']
  QWebEngineUrlRequestInterceptor = WAIT['QWebEngineUrlRequestInterceptor']
  QWebEngineUrlSchemeHandler = WAIT['QWebEngineUrlSchemeHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineProfile(QObject):
  """
  The cute side of Qt's QQuickWebEngineProfile: a plain Python object
  standing in front of one C++ QQuickWebEngineProfile.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineProfile is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineProfile that has a ritual and that
  Python can call so far, 66 names in all: 'metaObject', 'tr', 'storageName',
  'setStorageName', 'isOffTheRecord', 'setOffTheRecord',
  'persistentStoragePath', 'setPersistentStoragePath', 'cachePath',
  'setCachePath', 'httpUserAgent', 'setHttpUserAgent', 'httpCacheType',
  'setHttpCacheType', 'persistentCookiesPolicy',
  'setPersistentCookiesPolicy', 'persistentPermissionsPolicy',
  'setPersistentPermissionsPolicy', 'httpCacheMaximumSize',
  'setHttpCacheMaximumSize', 'httpAcceptLanguage', 'setHttpAcceptLanguage',
  'cookieStore', 'setUrlRequestInterceptor', 'urlSchemeHandler',
  'installUrlSchemeHandler', 'removeUrlScheme', 'removeUrlSchemeHandler',
  'removeAllUrlSchemeHandlers', 'clearHttpCache', 'setSpellCheckLanguages',
  'spellCheckLanguages', 'setSpellCheckEnabled', 'isSpellCheckEnabled',
  'userScripts', 'downloadPath', 'setDownloadPath', 'isPushServiceEnabled',
  'setPushServiceEnabled', 'clientCertificateStore', 'clientHints',
  'extensionManager', 'queryPermission', 'listAllPermissions',
  'listPermissionsForOrigin', 'listPermissionsForPermissionType',
  'defaultProfile', 'storageNameChanged', 'offTheRecordChanged',
  'persistentStoragePathChanged', 'cachePathChanged', 'httpUserAgentChanged',
  'httpCacheTypeChanged', 'persistentCookiesPolicyChanged',
  'httpCacheMaximumSizeChanged', 'httpAcceptLanguageChanged',
  'spellCheckLanguagesChanged', 'spellCheckEnabledChanged',
  'downloadPathChanged', 'pushServiceEnabledChanged',
  'clearHttpCacheCompleted', 'persistentPermissionsPolicyChanged',
  'downloadRequested', 'downloadFinished', 'presentNotification', 'settings'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineProfile::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWebEngineProfile::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWebEngineProfile::~QQuickWebEngineProfile()': the destructor:
    Python never removes a C++ QQuickWebEngineProfile.
  - Qt's 'QQuickWebEngineProfilePrivate *QQuickWebEngineProfile::d_func()':
    gives 'QQuickWebEngineProfilePrivate', which has no cute class yet.
  - Qt's 'const QQuickWebEngineProfilePrivate
    *QQuickWebEngineProfile::d_func() const': gives
    'QQuickWebEngineProfilePrivate', which has no cute class yet.
  - Qt's 'QQuickWebEngineProfile::QQuickWebEngineProfile(
    QQuickWebEngineProfilePrivate *a0, QObject *parent)': names
    'QQuickWebEngineProfilePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 76 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineProfile is created at the first use, not by
    'QQuickWebEngineProfile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineProfile.
  - Qt tells when it has removed the C++ QQuickWebEngineProfile. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWebEngineProfile, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class HttpCacheType(CuteNum):
    """
    The enum 'QQuickWebEngineProfile::HttpCacheType' of Qt, with the 3 names
    Qt gives in it.
    """

    MemoryHttpCache = Kee[int](0)
    DiskHttpCache = Kee[int](1)
    NoCache = Kee[int](2)

  class PersistentCookiesPolicy(CuteNum):
    """
    The enum 'QQuickWebEngineProfile::PersistentCookiesPolicy' of Qt, with
    the 4 names Qt gives in it.
    """

    NoPersistentCookies = Kee[int](0)
    AllowPersistentCookies = Kee[int](1)
    ForcePersistentCookies = Kee[int](2)
    OnlyPersistentCookies = Kee[int](3)

  class PersistentPermissionsPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineProfile::PersistentPermissionsPolicy' of Qt,
    with the 3 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
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
    Calls Qt's 'QString QQuickWebEngineProfile::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebengineprofile.html#tr

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
    #  QString QQuickWebEngineProfile::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickWebEngineProfile2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultProfile() -> Optional[QQuickWebEngineProfile]:
    """
    Calls Qt's 'QQuickWebEngineProfile
    *QQuickWebEngineProfile::defaultProfile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#defaultProfile

    Returns
    -------

    Optional[QQuickWebEngineProfile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineProfile *QQuickWebEngineProfile::defaultProfile()
    address = Rituals.call(
        'ritual_ZN22QQuickWebEngineProfile14defaultProfileEv',
    )
    return QQuickWebEngineProfile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineProfile'

  #  A C++ QQuickWebEngineProfile Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineProfile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebEngineProfile::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineProfile::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def storageName(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfile::storageName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#storageName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfile::storageName() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile11storageNameEv',
    )

  def isOffTheRecord(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineProfile::isOffTheRecord() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#isOffTheRecord
    """
    #  bool QQuickWebEngineProfile::isOffTheRecord() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile14isOffTheRecordEv',
    )

  def persistentStoragePath(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfile::persistentStoragePath()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#persistentStoragePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfile::persistentStoragePath() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile21persistentStoragePathEv',
    )

  def cachePath(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfile::cachePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#cachePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfile::cachePath() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile9cachePathEv',
    )

  def httpUserAgent(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfile::httpUserAgent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpUserAgent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfile::httpUserAgent() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile13httpUserAgentEv',
    )

  def httpCacheType(self) -> HttpCacheType:
    """
    Calls Qt's 'HttpCacheType QQuickWebEngineProfile::httpCacheType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheType

    Returns
    -------

    HttpCacheType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HttpCacheType(number)'
      gives.
    """
    #  HttpCacheType QQuickWebEngineProfile::httpCacheType() const
    return QQuickWebEngineProfile.HttpCacheType(self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile13httpCacheTypeEv',
    ))

  def persistentCookiesPolicy(self) -> PersistentCookiesPolicy:
    """
    Calls Qt's 'PersistentCookiesPolicy
    QQuickWebEngineProfile::persistentCookiesPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Returns
    -------

    PersistentCookiesPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PersistentCookiesPolicy(number)' gives.
    """
    #  PersistentCookiesPolicy
    #      QQuickWebEngineProfile::persistentCookiesPolicy() const
    return QQuickWebEngineProfile.PersistentCookiesPolicy(self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile23persistentCookiesPolicyEv',
    ))

  def persistentPermissionsPolicy(self) -> PersistentPermissionsPolicy:
    """
    Calls Qt's 'PersistentPermissionsPolicy
    QQuickWebEngineProfile::persistentPermissionsPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Returns
    -------

    PersistentPermissionsPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PersistentPermissionsPolicy(number)' gives.
    """
    #  PersistentPermissionsPolicy
    #      QQuickWebEngineProfile::persistentPermissionsPolicy() const
    return QQuickWebEngineProfile.PersistentPermissionsPolicy(
        self.uglySide.call(
            'ritual_ZNK22QQuickWebEngineProfile27persistentPermissionsPolic'
            'yEv',
        ))

  def httpCacheMaximumSize(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineProfile::httpCacheMaximumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheMaximumSize
    """
    #  int QQuickWebEngineProfile::httpCacheMaximumSize() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile20httpCacheMaximumSizeEv',
    )

  def httpAcceptLanguage(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfile::httpAcceptLanguage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpAcceptLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfile::httpAcceptLanguage() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile18httpAcceptLanguageEv',
    )

  def cookieStore(self) -> Optional[QWebEngineCookieStore]:
    """
    Calls Qt's 'QWebEngineCookieStore *QQuickWebEngineProfile::cookieStore()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#cookieStore

    Returns
    -------

    Optional[QWebEngineCookieStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineCookieStore *QQuickWebEngineProfile::cookieStore() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile11cookieStoreEv',
    )
    from ..QtWebEngineCore import QWebEngineCookieStore
    return QWebEngineCookieStore._cuteAt(address)

  @overload(QByteArray)
  def urlSchemeHandler(
      self,
      a0: QByteArray,
  ) -> Optional[QWebEngineUrlSchemeHandler]:
    """
    Calls Qt's 'const QWebEngineUrlSchemeHandler
    *QQuickWebEngineProfile::urlSchemeHandler(const QByteArray &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#urlSchemeHandler

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
    #      *QQuickWebEngineProfile::urlSchemeHandler(const QByteArray &a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile16urlSchemeHandlerERK10QByteArra'
        'y',
        self._valueOf(a0),
    )
    from ..QtWebEngineCore import QWebEngineUrlSchemeHandler
    return QWebEngineUrlSchemeHandler._cuteAt(address)

  def spellCheckLanguages(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickWebEngineProfile::spellCheckLanguages()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#spellCheckLanguages

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickWebEngineProfile::spellCheckLanguages() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile19spellCheckLanguagesEv',
    )
    return QStringList._cuteOwning(address)

  def isSpellCheckEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineProfile::isSpellCheckEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#isSpellCheckEnabled
    """
    #  bool QQuickWebEngineProfile::isSpellCheckEnabled() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile19isSpellCheckEnabledEv',
    )

  def userScripts(self) -> Optional[QQuickWebEngineScriptCollection]:
    """
    Calls Qt's 'QQuickWebEngineScriptCollection
    *QQuickWebEngineProfile::userScripts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#userScripts

    Returns
    -------

    Optional[QQuickWebEngineScriptCollection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineScriptCollection *QQuickWebEngineProfile::userScripts()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile11userScriptsEv',
    )
    from . import QQuickWebEngineScriptCollection
    return QQuickWebEngineScriptCollection._cuteAt(address)

  def downloadPath(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineProfile::downloadPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineProfile::downloadPath() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile12downloadPathEv',
    )

  def isPushServiceEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineProfile::isPushServiceEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#isPushServiceEnabled
    """
    #  bool QQuickWebEngineProfile::isPushServiceEnabled() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile20isPushServiceEnabledEv',
    )

  def clientHints(self) -> Optional[QWebEngineClientHints]:
    """
    Calls Qt's 'QWebEngineClientHints *QQuickWebEngineProfile::clientHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#clientHints

    Returns
    -------

    Optional[QWebEngineClientHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineClientHints *QQuickWebEngineProfile::clientHints() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile11clientHintsEv',
    )
    from ..QtWebEngineCore import QWebEngineClientHints
    return QWebEngineClientHints._cuteAt(address)

  @overload(QUrl, QWebEnginePermission.PermissionType)
  def queryPermission(
      self,
      securityOrigin: QUrl,
      permissionType: QWebEnginePermission.PermissionType,
  ) -> QWebEnginePermission:
    """
    Calls Qt's 'QWebEnginePermission
    QQuickWebEngineProfile::queryPermission(const QUrl &securityOrigin,
    QWebEnginePermission::PermissionType permissionType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#queryPermission

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
    #  QWebEnginePermission QQuickWebEngineProfile::queryPermission(const
    #      QUrl &securityOrigin, QWebEnginePermission::PermissionType
    #      permissionType) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile15queryPermissionERK4QUrlN20QWeb'
        'EnginePermission14PermissionTypeE',
        self._valueOf(securityOrigin), permissionType.value,
    )
    return QWebEnginePermission._cuteOwning(address)

  def listAllPermissions(self) -> QList[QWebEnginePermission]:
    """
    Calls Qt's 'QList<QWebEnginePermission>
    QQuickWebEngineProfile::listAllPermissions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#listAllPermissions

    Returns
    -------

    QList[QWebEnginePermission]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEnginePermission>
    #      QQuickWebEngineProfile::listAllPermissions() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile18listAllPermissionsEv',
    )
    return QList[QWebEnginePermission]._cuteOwning(address)

  @overload(QUrl)
  def listPermissionsForOrigin(
      self,
      securityOrigin: QUrl,
  ) -> QList[QWebEnginePermission]:
    """
    Calls Qt's 'QList<QWebEnginePermission>
    QQuickWebEngineProfile::listPermissionsForOrigin(const QUrl
    &securityOrigin) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

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
    #      QQuickWebEngineProfile::listPermissionsForOrigin(const QUrl
    #      &securityOrigin) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile24listPermissionsForOriginERK4QU'
        'rl',
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
    QQuickWebEngineProfile::listPermissionsForPermissionType(
    QWebEnginePermission::PermissionType permissionType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

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
    #      QQuickWebEngineProfile::listPermissionsForPermissionType(
    #      QWebEnginePermission::PermissionType permissionType) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile32listPermissionsForPermissionTy'
        'peEN20QWebEnginePermission14PermissionTypeE',
        permissionType.value,
    )
    return QList[QWebEnginePermission]._cuteOwning(address)

  def settings(self) -> Optional[QQuickWebEngineSettings]:
    """
    Calls Qt's 'QQuickWebEngineSettings *QQuickWebEngineProfile::settings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#settings

    Returns
    -------

    Optional[QQuickWebEngineSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineSettings *QQuickWebEngineProfile::settings() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWebEngineProfile8settingsEv',
    )
    from . import QQuickWebEngineSettings
    return QQuickWebEngineSettings._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStorageName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setStorageName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setStorageName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfile::setStorageName(const QString &name)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile14setStorageNameERK7QString', name,
    )

  @overload(bool)
  def setOffTheRecord(self, offTheRecord: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setOffTheRecord(bool
    offTheRecord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setOffTheRecord

    Parameters
    ----------

    offTheRecord : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineProfile::setOffTheRecord(bool offTheRecord)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile15setOffTheRecordEb', offTheRecord,
    )

  @overload(str)
  def setPersistentStoragePath(self, path: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setPersistentStoragePath(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfile::setPersistentStoragePath(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile24setPersistentStoragePathERK7QSt'
        'ring',
        path,
    )

  @overload(str)
  def setCachePath(self, path: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setCachePath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setCachePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfile::setCachePath(const QString &path)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile12setCachePathERK7QString', path,
    )

  @overload(str)
  def setHttpUserAgent(self, userAgent: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setHttpUserAgent(const QString
    &userAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setHttpUserAgent

    Parameters
    ----------

    userAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfile::setHttpUserAgent(const QString
    #      &userAgent)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile16setHttpUserAgentERK7QString',
        userAgent,
    )

  @overload(HttpCacheType)
  def setHttpCacheType(self, a0: HttpCacheType) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfile::setHttpCacheType(QQuickWebEngineProfile::
    HttpCacheType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setHttpCacheType

    Parameters
    ----------

    a0 : HttpCacheType
      Passed on as its number.
    """
    #  void QQuickWebEngineProfile::setHttpCacheType(QQuickWebEngineProfile::
    #      HttpCacheType a0)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile16setHttpCacheTypeENS_13HttpCache'
        'TypeE',
        a0.value,
    )

  @overload(PersistentCookiesPolicy)
  def setPersistentCookiesPolicy(self, a0: PersistentCookiesPolicy) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setPersistentCookiesPolicy(
    QQuickWebEngineProfile::PersistentCookiesPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Parameters
    ----------

    a0 : PersistentCookiesPolicy
      Passed on as its number.
    """
    #  void QQuickWebEngineProfile::setPersistentCookiesPolicy(
    #      QQuickWebEngineProfile::PersistentCookiesPolicy a0)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile26setPersistentCookiesPolicyENS_2'
        '3PersistentCookiesPolicyE',
        a0.value,
    )

  @overload(PersistentPermissionsPolicy)
  def setPersistentPermissionsPolicy(
      self,
      a0: PersistentPermissionsPolicy,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setPersistentPermissionsPolicy(
    QQuickWebEngineProfile::PersistentPermissionsPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Parameters
    ----------

    a0 : PersistentPermissionsPolicy
      Passed on as its number.
    """
    #  void QQuickWebEngineProfile::setPersistentPermissionsPolicy(
    #      QQuickWebEngineProfile::PersistentPermissionsPolicy a0)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile30setPersistentPermissionsPolicyE'
        'NS_27PersistentPermissionsPolicyE',
        a0.value,
    )

  @overload(int)
  def setHttpCacheMaximumSize(self, maxSize: int) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setHttpCacheMaximumSize(int
    maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  void QQuickWebEngineProfile::setHttpCacheMaximumSize(int maxSize)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile23setHttpCacheMaximumSizeEi',
        maxSize,
    )

  @overload(str)
  def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setHttpAcceptLanguage(const
    QString &httpAcceptLanguage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setHttpAcceptLanguage

    Parameters
    ----------

    httpAcceptLanguage : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfile::setHttpAcceptLanguage(const QString
    #      &httpAcceptLanguage)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile21setHttpAcceptLanguageERK7QStrin'
        'g',
        httpAcceptLanguage,
    )

  @overload(QWebEngineUrlRequestInterceptor)
  @overload(NoneType)
  def setUrlRequestInterceptor(
      self,
      interceptor: Optional[QWebEngineUrlRequestInterceptor],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setUrlRequestInterceptor(
    QWebEngineUrlRequestInterceptor *interceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Parameters
    ----------

    interceptor : Optional[QWebEngineUrlRequestInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineProfile::setUrlRequestInterceptor(
    #      QWebEngineUrlRequestInterceptor *interceptor)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile24setUrlRequestInterceptorEP31QWe'
        'bEngineUrlRequestInterceptor',
        self._addressOf(interceptor),
    )

  @overload(QStringList)
  def setSpellCheckLanguages(self, languages: QStringList) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setSpellCheckLanguages(const
    QStringList &languages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setSpellCheckLanguages

    Parameters
    ----------

    languages : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickWebEngineProfile::setSpellCheckLanguages(const QStringList
    #      &languages)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile22setSpellCheckLanguagesERK5QList'
        'I7QStringE',
        self._valueOf(languages),
    )

  @overload(bool)
  def setSpellCheckEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setSpellCheckEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setSpellCheckEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineProfile::setSpellCheckEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile20setSpellCheckEnabledEb', enabled,
    )

  @overload(str)
  def setDownloadPath(self, path: str) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setDownloadPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setDownloadPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineProfile::setDownloadPath(const QString &path)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile15setDownloadPathERK7QString',
        path,
    )

  @overload(bool)
  def setPushServiceEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::setPushServiceEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#setPushServiceEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineProfile::setPushServiceEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile21setPushServiceEnabledEb', enable,
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
    'QQuickWebEngineProfile::QQuickWebEngineProfile(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#QQuickWebEngineProfile

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebEngineProfile::QQuickWebEngineProfile(QObject *parent)
    self._noteCreation(QQuickWebEngineProfile, lambda: Rituals.call(
        'ritual_ZN22QQuickWebEngineProfileC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      storageName: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineProfile::QQuickWebEngineProfile(const QString
    &storageName, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#QQuickWebEngineProfile

    Parameters
    ----------

    storageName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebEngineProfile::QQuickWebEngineProfile(const QString
    #      &storageName, QObject *parent)
    self._noteCreation(QQuickWebEngineProfile, lambda: Rituals.call(
        'ritual_ZN22QQuickWebEngineProfileC1ERK7QStringP7QObject',
        storageName, self._addressOf(parent, 'QObject'),
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

  @overload(QByteArray, QWebEngineUrlSchemeHandler)
  @overload(QByteArray, NoneType)
  def installUrlSchemeHandler(
      self,
      scheme: QByteArray,
      a1: Optional[QWebEngineUrlSchemeHandler],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::installUrlSchemeHandler(const
    QByteArray &scheme, QWebEngineUrlSchemeHandler *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html

    Parameters
    ----------

    scheme : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : Optional[QWebEngineUrlSchemeHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineProfile::installUrlSchemeHandler(const QByteArray
    #      &scheme, QWebEngineUrlSchemeHandler *a1)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile23installUrlSchemeHandlerERK10QBy'
        'teArrayP26QWebEngineUrlSchemeHandler',
        self._valueOf(scheme), self._addressOf(a1),
    )

  @overload(QByteArray)
  def removeUrlScheme(self, scheme: QByteArray) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::removeUrlScheme(const QByteArray
    &scheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#removeUrlScheme

    Parameters
    ----------

    scheme : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickWebEngineProfile::removeUrlScheme(const QByteArray &scheme)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile15removeUrlSchemeERK10QByteArray',
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
    QQuickWebEngineProfile::removeUrlSchemeHandler(QWebEngineUrlSchemeHandler
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#removeUrlSchemeHandler

    Parameters
    ----------

    a0 : Optional[QWebEngineUrlSchemeHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineProfile::removeUrlSchemeHandler(
    #      QWebEngineUrlSchemeHandler *a0)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile22removeUrlSchemeHandlerEP26QWebE'
        'ngineUrlSchemeHandler',
        self._addressOf(a0),
    )

  def removeAllUrlSchemeHandlers(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::removeAllUrlSchemeHandlers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::removeAllUrlSchemeHandlers()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile26removeAllUrlSchemeHandlersEv',
    )

  def clearHttpCache(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::clearHttpCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#clearHttpCache
    """
    #  void QQuickWebEngineProfile::clearHttpCache()
    self.uglySide.call('ritual_ZN22QQuickWebEngineProfile14clearHttpCacheEv')

  def clientCertificateStore(
      self,
  ) -> Optional[QWebEngineClientCertificateStore]:
    """
    Calls Qt's 'QWebEngineClientCertificateStore
    *QQuickWebEngineProfile::clientCertificateStore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#clientCertificateStore

    Returns
    -------

    Optional[QWebEngineClientCertificateStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineClientCertificateStore
    #      *QQuickWebEngineProfile::clientCertificateStore()
    address = self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile22clientCertificateStoreEv',
    )
    from ..QtWebEngineCore import QWebEngineClientCertificateStore
    return QWebEngineClientCertificateStore._cuteAt(address)

  def extensionManager(self) -> Optional[QWebEngineExtensionManager]:
    """
    Calls Qt's 'QWebEngineExtensionManager
    *QQuickWebEngineProfile::extensionManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#extensionManager

    Returns
    -------

    Optional[QWebEngineExtensionManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineExtensionManager *QQuickWebEngineProfile::extensionManager()
    address = self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile16extensionManagerEv',
    )
    from ..QtWebEngineCore import QWebEngineExtensionManager
    return QWebEngineExtensionManager._cuteAt(address)

  def storageNameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::storageNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#storageNameChanged
    """
    #  void QQuickWebEngineProfile::storageNameChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile18storageNameChangedEv',
    )

  def offTheRecordChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::offTheRecordChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#offTheRecordChanged
    """
    #  void QQuickWebEngineProfile::offTheRecordChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile19offTheRecordChangedEv',
    )

  def persistentStoragePathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::persistentStoragePathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::persistentStoragePathChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile28persistentStoragePathChangedEv',
    )

  def cachePathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::cachePathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#cachePathChanged
    """
    #  void QQuickWebEngineProfile::cachePathChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile16cachePathChangedEv',
    )

  def httpUserAgentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::httpUserAgentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpUserAgentChanged
    """
    #  void QQuickWebEngineProfile::httpUserAgentChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile20httpUserAgentChangedEv',
    )

  def httpCacheTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::httpCacheTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#httpCacheTypeChanged
    """
    #  void QQuickWebEngineProfile::httpCacheTypeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile20httpCacheTypeChangedEv',
    )

  def persistentCookiesPolicyChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfile::persistentCookiesPolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::persistentCookiesPolicyChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile30persistentCookiesPolicyChangedE'
        'v',
    )

  def httpCacheMaximumSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::httpCacheMaximumSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::httpCacheMaximumSizeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile27httpCacheMaximumSizeChangedEv',
    )

  def httpAcceptLanguageChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::httpAcceptLanguageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::httpAcceptLanguageChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile25httpAcceptLanguageChangedEv',
    )

  def spellCheckLanguagesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::spellCheckLanguagesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::spellCheckLanguagesChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile26spellCheckLanguagesChangedEv',
    )

  def spellCheckEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::spellCheckEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::spellCheckEnabledChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile24spellCheckEnabledChangedEv',
    )

  def downloadPathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::downloadPathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadPathChanged
    """
    #  void QQuickWebEngineProfile::downloadPathChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile19downloadPathChangedEv',
    )

  def pushServiceEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::pushServiceEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::pushServiceEnabledChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile25pushServiceEnabledChangedEv',
    )

  def clearHttpCacheCompleted(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineProfile::clearHttpCacheCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::clearHttpCacheCompleted()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile23clearHttpCacheCompletedEv',
    )

  def persistentPermissionsPolicyChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfile::persistentPermissionsPolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html
    """
    #  void QQuickWebEngineProfile::persistentPermissionsPolicyChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile34persistentPermissionsPolicyChan'
        'gedEv',
    )

  @overload(QQuickWebEngineDownloadRequest)
  @overload(NoneType)
  def downloadRequested(
      self,
      download: Optional[QQuickWebEngineDownloadRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfile::downloadRequested(QQuickWebEngineDownloadRequest
    *download)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadRequested

    Parameters
    ----------

    download : Optional[QQuickWebEngineDownloadRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineProfile::downloadRequested(
    #      QQuickWebEngineDownloadRequest *download)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile17downloadRequestedEP30QQuickWebE'
        'ngineDownloadRequest',
        self._addressOf(download),
    )

  @overload(QQuickWebEngineDownloadRequest)
  @overload(NoneType)
  def downloadFinished(
      self,
      download: Optional[QQuickWebEngineDownloadRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfile::downloadFinished(QQuickWebEngineDownloadRequest
    *download)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#downloadFinished

    Parameters
    ----------

    download : Optional[QQuickWebEngineDownloadRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebEngineProfile::downloadFinished(
    #      QQuickWebEngineDownloadRequest *download)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile16downloadFinishedEP30QQuickWebEn'
        'gineDownloadRequest',
        self._addressOf(download),
    )

  @overload(QWebEngineNotification)
  @overload(NoneType)
  def presentNotification(
      self,
      notification: Optional[QWebEngineNotification],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineProfile::presentNotification(QWebEngineNotification
    *notification)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineprofile.html#presentNotification

    Parameters
    ----------

    notification : Optional[QWebEngineNotification]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickWebEngineProfile::presentNotification(QWebEngineNotification
    #      *notification)
    self.uglySide.call(
        'ritual_ZN22QQuickWebEngineProfile19presentNotificationEP22QWebEngi'
        'neNotification',
        self._addressOf(notification),
    )
