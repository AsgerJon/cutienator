"""
QQmlEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QJSEngine, QQmlAbstractUrlInterceptor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QMetaProperty, QUrl
  from . import QQmlContext, QQmlEnginePrivate, QQmlError
  from . import QQmlImageProviderBase, QQmlIncubationController
  from . import QQmlNetworkAccessManagerFactory
  from ..QtNetwork import QNetworkAccessManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMetaProperty = WAIT['QMetaProperty']
  QQmlContext = WAIT['QQmlContext']
  QQmlError = WAIT['QQmlError']
  QQmlImageProviderBase = WAIT['QQmlImageProviderBase']
  QQmlIncubationController = WAIT['QQmlIncubationController']
  QQmlNetworkAccessManagerFactory = WAIT['QQmlNetworkAccessManagerFactory']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlEngine(QJSEngine):
  """
  The cute side of Qt's QQmlEngine: a plain Python object standing in front
  of one C++ QQmlEngine.

  It is built on the cute 'QJSEngine', as Qt's QQmlEngine is built on Qt's
  QJSEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlEngine that has a ritual and that Python can
  call so far, 46 names in all: 'metaObject', 'tr', 'rootContext',
  'clearComponentCache', 'trimComponentCache', 'clearSingletons',
  'importPathList', 'setImportPathList', 'addImportPath', 'pluginPathList',
  'setPluginPathList', 'addPluginPath', 'addNamedBundle',
  'setNetworkAccessManagerFactory', 'networkAccessManagerFactory',
  'networkAccessManager', 'setUrlInterceptor', 'urlInterceptor',
  'addUrlInterceptor', 'removeUrlInterceptor', 'urlInterceptors',
  'interceptUrl', 'addImageProvider', 'imageProvider', 'removeImageProvider',
  'setIncubationController', 'incubationController', 'setOfflineStoragePath',
  'offlineStoragePath', 'offlineStorageDatabaseFilePath', 'baseUrl',
  'setBaseUrl', 'outputWarningsToStandardError',
  'setOutputWarningsToStandardError',
  'markCurrentFunctionAsTranslationBinding', 'setExternalSingletonInstance',
  'captureProperty', 'retranslate', 'offlineStoragePathChanged',
  'contextForObject', 'setContextForObject', 'event', 'quit', 'exit',
  'warnings', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlEngine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlEngine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlEngine::~QQmlEngine()': the destructor: Python never removes a
    C++ QQmlEngine.
  - Qt's 'bool QQmlEngine::importPlugin(const QString &filePath, const
    QString &uri, QList<QQmlError> *errors)': names 'QList<QQmlError>', which
    has no cute class yet.
  - Qt's 'QQmlEngine::QQmlEngine(QQmlEnginePrivate &dd, QObject *p)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QQmlEnginePrivate *QQmlEngine::d_func() const': takes in
    Python what 'QQmlEnginePrivate *QQmlEngine::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 59 functions Qt declares: 2 not a gap; 2 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlEngine is created at the first use, not by 'QQmlEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlEngine.
  - Qt tells when it has removed the C++ QQmlEngine. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQmlEngine that has no cute function yet,
    'importPlugin', 'singletonInstance', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlEngine::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#tr

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
    #  QString QQmlEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQmlEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def contextForObject(a0: Optional[QObject]) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlEngine::contextForObject(const QObject
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#contextForObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlEngine::contextForObject(const QObject *a0)
    address = Rituals.call(
        'ritual_ZN10QQmlEngine16contextForObjectEPK7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  @staticmethod
  @overload(QObject, QQmlContext)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlContext)
  @overload(NoneType, NoneType)
  def setContextForObject(
      a0: Optional[QObject],
      a1: Optional[QQmlContext],
  ) -> None:
    """
    Calls Qt's 'void QQmlEngine::setContextForObject(QObject *a0, QQmlContext
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#setContextForObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::setContextForObject(QObject *a0, QQmlContext *a1)
    Rituals.call(
        'ritual_ZN10QQmlEngine19setContextForObjectEP7QObjectP11QQmlContext',
        CuteMixin._addressOf(a0, 'QObject'), CuteMixin._addressOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEngine'

  #  A C++ QQmlEngine Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlEngine::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rootContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlEngine::rootContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#rootContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlEngine::rootContext() const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine11rootContextEv')
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  def importPathList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlEngine::importPathList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#importPathList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlEngine::importPathList() const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine14importPathListEv')
    return QStringList._cuteOwning(address)

  def pluginPathList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlEngine::pluginPathList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#pluginPathList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlEngine::pluginPathList() const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine14pluginPathListEv')
    return QStringList._cuteOwning(address)

  def networkAccessManagerFactory(
      self,
  ) -> Optional[QQmlNetworkAccessManagerFactory]:
    """
    Calls Qt's 'QQmlNetworkAccessManagerFactory
    *QQmlEngine::networkAccessManagerFactory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#networkAccessManagerFactory

    Returns
    -------

    Optional[QQmlNetworkAccessManagerFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlNetworkAccessManagerFactory
    #      *QQmlEngine::networkAccessManagerFactory() const
    address = self.uglySide.call(
        'ritual_ZNK10QQmlEngine27networkAccessManagerFactoryEv',
    )
    from . import QQmlNetworkAccessManagerFactory
    return QQmlNetworkAccessManagerFactory._cuteAt(address)

  def networkAccessManager(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager *QQmlEngine::networkAccessManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#networkAccessManager

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QQmlEngine::networkAccessManager() const
    address = self.uglySide.call(
        'ritual_ZNK10QQmlEngine20networkAccessManagerEv',
    )
    from ..QtNetwork import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

  def urlInterceptor(self) -> Optional[QQmlAbstractUrlInterceptor]:
    """
    Calls Qt's 'QQmlAbstractUrlInterceptor *QQmlEngine::urlInterceptor()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#urlInterceptor

    Returns
    -------

    Optional[QQmlAbstractUrlInterceptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractUrlInterceptor *QQmlEngine::urlInterceptor() const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine14urlInterceptorEv')
    return QQmlAbstractUrlInterceptor._cuteAt(address)

  def urlInterceptors(self) -> QList[QQmlAbstractUrlInterceptor]:
    """
    Calls Qt's 'QList<QQmlAbstractUrlInterceptor *>
    QQmlEngine::urlInterceptors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#urlInterceptors

    Returns
    -------

    QList[QQmlAbstractUrlInterceptor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlAbstractUrlInterceptor *> QQmlEngine::urlInterceptors()
    #      const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine15urlInterceptorsEv')
    return QList[QQmlAbstractUrlInterceptor]._cuteOwning(address)

  @overload(QUrl, QQmlAbstractUrlInterceptor.DataType)
  def interceptUrl(
      self,
      url: QUrl,
      type: QQmlAbstractUrlInterceptor.DataType,
  ) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlEngine::interceptUrl(const QUrl &url,
    QQmlAbstractUrlInterceptor::DataType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#interceptUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : QQmlAbstractUrlInterceptor.DataType
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlEngine::interceptUrl(const QUrl &url,
    #      QQmlAbstractUrlInterceptor::DataType type) const
    address = self.uglySide.call(
        'ritual_ZNK10QQmlEngine12interceptUrlERK4QUrlN26QQmlAbstractUrlInte'
        'rceptor8DataTypeE',
        self._valueOf(url), type.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(str)
  def imageProvider(self, id: str) -> Optional[QQmlImageProviderBase]:
    """
    Calls Qt's 'QQmlImageProviderBase *QQmlEngine::imageProvider(const
    QString &id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#imageProvider

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQmlImageProviderBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlImageProviderBase *QQmlEngine::imageProvider(const QString &id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QQmlEngine13imageProviderERK7QString', id,
    )
    from . import QQmlImageProviderBase
    return QQmlImageProviderBase._cuteAt(address)

  def incubationController(self) -> Optional[QQmlIncubationController]:
    """
    Calls Qt's 'QQmlIncubationController *QQmlEngine::incubationController()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#incubationController

    Returns
    -------

    Optional[QQmlIncubationController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlIncubationController *QQmlEngine::incubationController() const
    address = self.uglySide.call(
        'ritual_ZNK10QQmlEngine20incubationControllerEv',
    )
    from . import QQmlIncubationController
    return QQmlIncubationController._cuteAt(address)

  def offlineStoragePath(self) -> str:
    """
    Calls Qt's 'QString QQmlEngine::offlineStoragePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#offlineStoragePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlEngine::offlineStoragePath() const
    return self.uglySide.call('ritual_ZNK10QQmlEngine18offlineStoragePathEv')

  @overload(str)
  def offlineStorageDatabaseFilePath(self, databaseName: str) -> str:
    """
    Calls Qt's 'QString QQmlEngine::offlineStorageDatabaseFilePath(const
    QString &databaseName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#offlineStorageDatabaseFilePath

    Parameters
    ----------

    databaseName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlEngine::offlineStorageDatabaseFilePath(const QString
    #      &databaseName) const
    return self.uglySide.call(
        'ritual_ZNK10QQmlEngine30offlineStorageDatabaseFilePathERK7QString',
        databaseName,
    )

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlEngine::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlEngine::baseUrl() const
    address = self.uglySide.call('ritual_ZNK10QQmlEngine7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def outputWarningsToStandardError(self) -> bool:
    """
    Calls Qt's 'bool QQmlEngine::outputWarningsToStandardError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#outputWarningsToStandardError
    """
    #  bool QQmlEngine::outputWarningsToStandardError() const
    return self.uglySide.call(
        'ritual_ZNK10QQmlEngine29outputWarningsToStandardErrorEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setImportPathList(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QQmlEngine::setImportPathList(const QStringList
    &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#setImportPathList

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlEngine::setImportPathList(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine17setImportPathListERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(QStringList)
  def setPluginPathList(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QQmlEngine::setPluginPathList(const QStringList
    &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#setPluginPathList

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlEngine::setPluginPathList(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine17setPluginPathListERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(QQmlNetworkAccessManagerFactory)
  @overload(NoneType)
  def setNetworkAccessManagerFactory(
      self,
      a0: Optional[QQmlNetworkAccessManagerFactory],
  ) -> None:
    """
    Calls Qt's 'void QQmlEngine::setNetworkAccessManagerFactory(
    QQmlNetworkAccessManagerFactory *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#setNetworkAccessManagerFactory

    Parameters
    ----------

    a0 : Optional[QQmlNetworkAccessManagerFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::setNetworkAccessManagerFactory(
    #      QQmlNetworkAccessManagerFactory *a0)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine30setNetworkAccessManagerFactoryEP31QQmlNetwo'
        'rkAccessManagerFactory',
        self._addressOf(a0),
    )

  @overload(QQmlAbstractUrlInterceptor)
  @overload(NoneType)
  def setUrlInterceptor(
      self,
      urlInterceptor: Optional[QQmlAbstractUrlInterceptor],
  ) -> None:
    """
    Calls Qt's 'void QQmlEngine::setUrlInterceptor(QQmlAbstractUrlInterceptor
    *urlInterceptor)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#setUrlInterceptor

    Parameters
    ----------

    urlInterceptor : Optional[QQmlAbstractUrlInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::setUrlInterceptor(QQmlAbstractUrlInterceptor
    #      *urlInterceptor)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine17setUrlInterceptorEP26QQmlAbstractUrlInterce'
        'ptor',
        self._addressOf(urlInterceptor),
    )

  @overload(QQmlIncubationController)
  @overload(NoneType)
  def setIncubationController(
      self,
      a0: Optional[QQmlIncubationController],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlEngine::setIncubationController(QQmlIncubationController *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#setIncubationController

    Parameters
    ----------

    a0 : Optional[QQmlIncubationController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::setIncubationController(QQmlIncubationController *a0)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine23setIncubationControllerEP24QQmlIncubationCo'
        'ntroller',
        self._addressOf(a0),
    )

  @overload(str)
  def setOfflineStoragePath(self, dir: str) -> None:
    """
    Calls Qt's 'void QQmlEngine::setOfflineStoragePath(const QString &dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#setOfflineStoragePath

    Parameters
    ----------

    dir : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlEngine::setOfflineStoragePath(const QString &dir)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine21setOfflineStoragePathERK7QString', dir,
    )

  @overload(QUrl)
  def setBaseUrl(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQmlEngine::setBaseUrl(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#setBaseUrl

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlEngine::setBaseUrl(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine10setBaseUrlERK4QUrl', self._valueOf(a0),
    )

  @overload(bool)
  def setOutputWarningsToStandardError(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlEngine::setOutputWarningsToStandardError(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#setOutputWarningsToStandardError

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlEngine::setOutputWarningsToStandardError(bool a0)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine32setOutputWarningsToStandardErrorEb', a0,
    )

  @overload(str, str, QObject)
  @overload(str, str, NoneType)
  def setExternalSingletonInstance(
      self,
      moduleName: str,
      typeName: str,
      instance: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlEngine::setExternalSingletonInstance(QAnyStringView
    moduleName, QAnyStringView typeName, QObject *instance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#setExternalSingletonInstance

    Parameters
    ----------

    moduleName : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlEngine::setExternalSingletonInstance(QAnyStringView
    #      moduleName, QAnyStringView typeName, QObject *instance)
    return self.uglySide.call(
        'ritual_ZN10QQmlEngine28setExternalSingletonInstanceE14QAnyStringVi'
        'ewS0_P7QObject',
        moduleName, typeName, self._addressOf(instance, 'QObject'),
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
  def __init__(self, p: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlEngine::QQmlEngine(QObject *p)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#QQmlEngine

    Parameters
    ----------

    p : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlEngine::QQmlEngine(QObject *p)
    self._noteCreation(QQmlEngine, lambda: Rituals.call(
        'ritual_ZN10QQmlEngineC1EP7QObject', self._addressOf(p, 'QObject'),
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

  def clearComponentCache(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::clearComponentCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#clearComponentCache
    """
    #  void QQmlEngine::clearComponentCache()
    self.uglySide.call('ritual_ZN10QQmlEngine19clearComponentCacheEv')

  def trimComponentCache(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::trimComponentCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#trimComponentCache
    """
    #  void QQmlEngine::trimComponentCache()
    self.uglySide.call('ritual_ZN10QQmlEngine18trimComponentCacheEv')

  def clearSingletons(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::clearSingletons()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#clearSingletons
    """
    #  void QQmlEngine::clearSingletons()
    self.uglySide.call('ritual_ZN10QQmlEngine15clearSingletonsEv')

  @overload(str)
  def addImportPath(self, dir: str) -> None:
    """
    Calls Qt's 'void QQmlEngine::addImportPath(const QString &dir)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#addImportPath

    Parameters
    ----------

    dir : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlEngine::addImportPath(const QString &dir)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine13addImportPathERK7QString', dir,
    )

  @overload(str)
  def addPluginPath(self, dir: str) -> None:
    """
    Calls Qt's 'void QQmlEngine::addPluginPath(const QString &dir)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#addPluginPath

    Parameters
    ----------

    dir : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlEngine::addPluginPath(const QString &dir)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine13addPluginPathERK7QString', dir,
    )

  @overload(str, str)
  def addNamedBundle(self, a0: str, a1: str) -> bool:
    """
    Calls Qt's 'bool QQmlEngine::addNamedBundle(const QString &a0, const
    QString &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#addNamedBundle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlEngine::addNamedBundle(const QString &a0, const QString &a1)
    return self.uglySide.call(
        'ritual_ZN10QQmlEngine14addNamedBundleERK7QStringS2_', a0, a1,
    )

  @overload(QQmlAbstractUrlInterceptor)
  @overload(NoneType)
  def addUrlInterceptor(
      self,
      urlInterceptor: Optional[QQmlAbstractUrlInterceptor],
  ) -> None:
    """
    Calls Qt's 'void QQmlEngine::addUrlInterceptor(QQmlAbstractUrlInterceptor
    *urlInterceptor)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#addUrlInterceptor

    Parameters
    ----------

    urlInterceptor : Optional[QQmlAbstractUrlInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::addUrlInterceptor(QQmlAbstractUrlInterceptor
    #      *urlInterceptor)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine17addUrlInterceptorEP26QQmlAbstractUrlInterce'
        'ptor',
        self._addressOf(urlInterceptor),
    )

  @overload(QQmlAbstractUrlInterceptor)
  @overload(NoneType)
  def removeUrlInterceptor(
      self,
      urlInterceptor: Optional[QQmlAbstractUrlInterceptor],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlEngine::removeUrlInterceptor(QQmlAbstractUrlInterceptor
    *urlInterceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#removeUrlInterceptor

    Parameters
    ----------

    urlInterceptor : Optional[QQmlAbstractUrlInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::removeUrlInterceptor(QQmlAbstractUrlInterceptor
    #      *urlInterceptor)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine20removeUrlInterceptorEP26QQmlAbstractUrlInte'
        'rceptor',
        self._addressOf(urlInterceptor),
    )

  @overload(str, QQmlImageProviderBase)
  @overload(str, NoneType)
  def addImageProvider(
      self,
      id: str,
      a1: Optional[QQmlImageProviderBase],
  ) -> None:
    """
    Calls Qt's 'void QQmlEngine::addImageProvider(const QString &id,
    QQmlImageProviderBase *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#addImageProvider

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QQmlImageProviderBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlEngine::addImageProvider(const QString &id,
    #      QQmlImageProviderBase *a1)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine16addImageProviderERK7QStringP21QQmlImageProv'
        'iderBase',
        id, self._addressOf(a1),
    )

  @overload(str)
  def removeImageProvider(self, id: str) -> None:
    """
    Calls Qt's 'void QQmlEngine::removeImageProvider(const QString &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#removeImageProvider

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlEngine::removeImageProvider(const QString &id)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine19removeImageProviderERK7QString', id,
    )

  def markCurrentFunctionAsTranslationBinding(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::markCurrentFunctionAsTranslationBinding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html
    """
    #  void QQmlEngine::markCurrentFunctionAsTranslationBinding()
    self.uglySide.call(
        'ritual_ZN10QQmlEngine39markCurrentFunctionAsTranslationBindingEv',
    )

  @overload(QObject, QMetaProperty)
  @overload(NoneType, QMetaProperty)
  def captureProperty(
      self,
      object: Optional[QObject],
      property: QMetaProperty,
  ) -> None:
    """
    Calls Qt's 'void QQmlEngine::captureProperty(QObject *object, const
    QMetaProperty &property) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#captureProperty

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlEngine::captureProperty(QObject *object, const QMetaProperty
    #      &property) const
    self.uglySide.call(
        'ritual_ZNK10QQmlEngine15capturePropertyEP7QObjectRK13QMetaProperty',
        self._addressOf(object, 'QObject'), self._valueOf(property),
    )

  def retranslate(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::retranslate()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#retranslate
    """
    #  void QQmlEngine::retranslate()
    self.uglySide.call('ritual_ZN10QQmlEngine11retranslateEv')

  def offlineStoragePathChanged(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::offlineStoragePathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlengine.html#offlineStoragePathChanged
    """
    #  void QQmlEngine::offlineStoragePathChanged()
    self.uglySide.call('ritual_ZN10QQmlEngine25offlineStoragePathChangedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQmlEngine::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlEngine::event(QEvent *a0)
    ritual = 'ritual_ZN10QQmlEngine5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQmlEngine5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def quit(self) -> None:
    """
    Calls Qt's 'void QQmlEngine::quit()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#quit
    """
    #  void QQmlEngine::quit()
    self.uglySide.call('ritual_ZN10QQmlEngine4quitEv')

  @overload(int)
  def exit(self, retCode: int) -> None:
    """
    Calls Qt's 'void QQmlEngine::exit(int retCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#exit

    Parameters
    ----------

    retCode : int
      Passed on as it is.
    """
    #  void QQmlEngine::exit(int retCode)
    self.uglySide.call('ritual_ZN10QQmlEngine4exitEi', retCode)

  @overload(QList[QQmlError])
  def warnings(self, warnings: QList[QQmlError]) -> None:
    """
    Calls Qt's 'void QQmlEngine::warnings(const QList<QQmlError> &warnings)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#warnings

    Parameters
    ----------

    warnings : QList[QQmlError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlEngine::warnings(const QList<QQmlError> &warnings)
    self.uglySide.call(
        'ritual_ZN10QQmlEngine8warningsERK5QListI9QQmlErrorE',
        self._valueOf(warnings),
    )

  def d_func(self) -> Optional[QQmlEnginePrivate]:
    """
    Calls Qt's 'QQmlEnginePrivate *QQmlEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlengine.html#d_func

    Returns
    -------

    Optional[QQmlEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEnginePrivate *QQmlEngine::d_func()
    address = self.uglySide.call('ritual_ZN10QQmlEngine6d_funcEv')
    from . import QQmlEnginePrivate
    return QQmlEnginePrivate._cuteAt(address)

  @staticmethod
  def importPlugin(*__, **_) -> Never:
    """
    Qt's 'bool QQmlEngine::importPlugin(const QString &filePath, const
    QString &uri, QList<QQmlError> *errors)': names 'QList<QQmlError>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlEngine.importPlugin' has no cute function yet. Qt's 'bool "
        "QQmlEngine::importPlugin(const QString &filePath, const QString "
        "&uri, QList<QQmlError> *errors)': names 'QList<QQmlError>', which "
        "has no cute class yet.")

  @staticmethod
  def singletonInstance(*__, **_) -> Never:
    """
    Qt's 'QQmlEngine::singletonInstance': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlEngine.singletonInstance' has no cute function yet. Qt's "
        "'QQmlEngine::singletonInstance': a template: a pattern and no "
        "single function.")
