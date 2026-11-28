"""
QWebView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebView/qwebview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QWindow
from . import QWebViewFactory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QUrl
  from ..QtGui import QScreen
  from . import QWebViewLoadingInfo, QWebViewSettings
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QScreen = WAIT['QScreen']
  QUrl = WAIT['QUrl']
  QWebViewLoadingInfo = WAIT['QWebViewLoadingInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebView(QWindow):
  """
  The cute side of Qt's QWebView: a plain Python object standing in front of
  one C++ QWebView.

  It is built on the cute 'QWindow', as Qt's QWebView is built on Qt's
  QWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebView that has a ritual and that Python can call
  so far, 28 names in all: 'metaObject', 'tr', 'httpUserAgentString', 'url',
  'canGoBack', 'canGoForward', 'title', 'loadProgress', 'isLoading',
  'settings', 'setHttpUserAgentString', 'setUrl', 'goBack', 'goForward',
  'reload', 'stop', 'loadHtml', 'setCookie', 'deleteCookie',
  'deleteAllCookies', 'titleChanged', 'urlChanged', 'loadingChanged',
  'loadProgressChanged', 'httpUserAgentStringChanged', 'cookieAdded',
  'cookieRemoved', 'event'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebView::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QWebView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWebView::~QWebView()': the destructor: Python never removes a C++
    QWebView.
  - Qt's 'void QWebView::runJavaScript(const QString &script, const
    std::function<void (const QVariant &)> &resultCallback)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebView is created at the first use, not by 'QWebView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebView.
  - Qt tells when it has removed the C++ QWebView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QWebView that has no cute function yet,
    'runJavaScript', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QWebView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#tr

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
    #  QString QWebView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QWebView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebView'

  #  A C++ QWebView Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebView::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QWebView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def httpUserAgentString(self) -> str:
    """
    Calls Qt's 'QString QWebView::httpUserAgentString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#httpUserAgentString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebView::httpUserAgentString() const
    return self.uglySide.call('ritual_ZNK8QWebView19httpUserAgentStringEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebView::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebView::url() const
    address = self.uglySide.call('ritual_ZNK8QWebView3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def canGoBack(self) -> bool:
    """
    Calls Qt's 'bool QWebView::canGoBack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#canGoBack
    """
    #  bool QWebView::canGoBack() const
    return self.uglySide.call('ritual_ZNK8QWebView9canGoBackEv')

  def canGoForward(self) -> bool:
    """
    Calls Qt's 'bool QWebView::canGoForward() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#canGoForward
    """
    #  bool QWebView::canGoForward() const
    return self.uglySide.call('ritual_ZNK8QWebView12canGoForwardEv')

  def title(self) -> str:
    """
    Calls Qt's 'QString QWebView::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebView::title() const
    return self.uglySide.call('ritual_ZNK8QWebView5titleEv')

  def loadProgress(self) -> int:
    """
    Calls Qt's 'int QWebView::loadProgress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#loadProgress
    """
    #  int QWebView::loadProgress() const
    return self.uglySide.call('ritual_ZNK8QWebView12loadProgressEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QWebView::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#isLoading
    """
    #  bool QWebView::isLoading() const
    return self.uglySide.call('ritual_ZNK8QWebView9isLoadingEv')

  def settings(self) -> Optional[QWebViewSettings]:
    """
    Calls Qt's 'QWebViewSettings *QWebView::settings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#settings

    Returns
    -------

    Optional[QWebViewSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebViewSettings *QWebView::settings() const
    address = self.uglySide.call('ritual_ZNK8QWebView8settingsEv')
    from . import QWebViewSettings
    return QWebViewSettings._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHttpUserAgentString(self, httpUserAgent: str) -> None:
    """
    Calls Qt's 'void QWebView::setHttpUserAgentString(const QString
    &httpUserAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebview.html#setHttpUserAgentString

    Parameters
    ----------

    httpUserAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::setHttpUserAgentString(const QString &httpUserAgent)
    self.uglySide.call(
        'ritual_ZN8QWebView22setHttpUserAgentStringERK7QString',
        httpUserAgent,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebView::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebView::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN8QWebView6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(str, str, str)
  def setCookie(self, domain: str, name: str, value: str) -> None:
    """
    Calls Qt's 'void QWebView::setCookie(const QString &domain, const QString
    &name, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#setCookie

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::setCookie(const QString &domain, const QString &name,
    #      const QString &value)
    self.uglySide.call(
        'ritual_ZN8QWebView9setCookieERK7QStringS2_S2_', domain, name, value,
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
  @overload(QScreen)
  @overload(NoneType)
  def __init__(self, screen: Optional[QScreen] = None) -> None:
    """
    Notes what was given, for Qt's 'QWebView::QWebView(QScreen *screen)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#QWebView

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebView::QWebView(QScreen *screen)
    self._noteCreation(QWebView, lambda: Rituals.call(
        'ritual_ZN8QWebViewC1EP7QScreen', self._addressOf(screen),
    ))

  @overload(QWindow)
  def __init__(self, parent: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's 'QWebView::QWebView(QWindow *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#QWebView

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebView::QWebView(QWindow *parent)
    self._noteCreation(QWebView, lambda: Rituals.call(
        'ritual_ZN8QWebViewC1EP7QWindow', self._addressOf(parent),
    ))

  @overload(QWebViewFactory.Hint)
  def __init__(self, a0: QWebViewFactory.Hint) -> None:
    """
    Notes what was given, for Qt's 'QWebView::QWebView(QWebViewFactory::Hint
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#QWebView

    Parameters
    ----------

    a0 : QWebViewFactory.Hint
      Passed on as its number.
    """
    #  QWebView::QWebView(QWebViewFactory::Hint a0)
    self._noteCreation(QWebView, lambda: Rituals.call(
        'ritual_ZN8QWebViewC1EN15QWebViewFactory4HintE', a0.value,
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

  def goBack(self) -> None:
    """
    Calls Qt's 'void QWebView::goBack()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#goBack
    """
    #  void QWebView::goBack()
    self.uglySide.call('ritual_ZN8QWebView6goBackEv')

  def goForward(self) -> None:
    """
    Calls Qt's 'void QWebView::goForward()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#goForward
    """
    #  void QWebView::goForward()
    self.uglySide.call('ritual_ZN8QWebView9goForwardEv')

  def reload(self) -> None:
    """
    Calls Qt's 'void QWebView::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#reload
    """
    #  void QWebView::reload()
    self.uglySide.call('ritual_ZN8QWebView6reloadEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QWebView::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#stop
    """
    #  void QWebView::stop()
    self.uglySide.call('ritual_ZN8QWebView4stopEv')

  @overload(str)
  @overload(str, QUrl)
  def loadHtml(self, html: str, baseUrl: Optional[QUrl] = None) -> None:
    """
    Calls Qt's 'void QWebView::loadHtml(const QString &html, const QUrl
    &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#loadHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebView::loadHtml(const QString &html, const QUrl &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN8QWebView8loadHtmlERK7QStringRK4QUrl',
        html, self._valueOf(baseUrl),
    )

  @overload(str, str)
  def deleteCookie(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QWebView::deleteCookie(const QString &domain, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#deleteCookie

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::deleteCookie(const QString &domain, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN8QWebView12deleteCookieERK7QStringS2_', domain, name,
    )

  def deleteAllCookies(self) -> None:
    """
    Calls Qt's 'void QWebView::deleteAllCookies()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#deleteAllCookies
    """
    #  void QWebView::deleteAllCookies()
    self.uglySide.call('ritual_ZN8QWebView16deleteAllCookiesEv')

  @overload(str)
  def titleChanged(self, title: str) -> None:
    """
    Calls Qt's 'void QWebView::titleChanged(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#titleChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::titleChanged(const QString &title)
    self.uglySide.call('ritual_ZN8QWebView12titleChangedERK7QString', title)

  @overload(QUrl)
  def urlChanged(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebView::urlChanged(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#urlChanged

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebView::urlChanged(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN8QWebView10urlChangedERK4QUrl', self._valueOf(url),
    )

  @overload(QWebViewLoadingInfo)
  def loadingChanged(self, loadingInfo: QWebViewLoadingInfo) -> None:
    """
    Calls Qt's 'void QWebView::loadingChanged(const QWebViewLoadingInfo
    &loadingInfo)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#loadingChanged

    Parameters
    ----------

    loadingInfo : QWebViewLoadingInfo
      Passed on as a value: Qt reads the C++ QWebViewLoadingInfo, which stays
      Python's own.
    """
    #  void QWebView::loadingChanged(const QWebViewLoadingInfo &loadingInfo)
    self.uglySide.call(
        'ritual_ZN8QWebView14loadingChangedERK19QWebViewLoadingInfo',
        self._valueOf(loadingInfo),
    )

  @overload(int)
  def loadProgressChanged(self, loadProgress: int) -> None:
    """
    Calls Qt's 'void QWebView::loadProgressChanged(int loadProgress)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#loadProgressChanged

    Parameters
    ----------

    loadProgress : int
      Passed on as it is.
    """
    #  void QWebView::loadProgressChanged(int loadProgress)
    self.uglySide.call(
        'ritual_ZN8QWebView19loadProgressChangedEi', loadProgress,
    )

  @overload(str)
  def httpUserAgentStringChanged(self, userAgent: str) -> None:
    """
    Calls Qt's 'void QWebView::httpUserAgentStringChanged(const QString
    &userAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebview.html#httpUserAgentStringChanged

    Parameters
    ----------

    userAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::httpUserAgentStringChanged(const QString &userAgent)
    self.uglySide.call(
        'ritual_ZN8QWebView26httpUserAgentStringChangedERK7QString',
        userAgent,
    )

  @overload(str, str)
  def cookieAdded(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QWebView::cookieAdded(const QString &domain, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#cookieAdded

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::cookieAdded(const QString &domain, const QString &name)
    self.uglySide.call(
        'ritual_ZN8QWebView11cookieAddedERK7QStringS2_', domain, name,
    )

  @overload(str, str)
  def cookieRemoved(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QWebView::cookieRemoved(const QString &domain, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#cookieRemoved

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebView::cookieRemoved(const QString &domain, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN8QWebView13cookieRemovedERK7QStringS2_', domain, name,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWebView::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebview.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWebView::event(QEvent *a0)
    ritual = 'ritual_ZN8QWebView5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QWebView5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def runJavaScript(*__, **_) -> Never:
    """
    Qt's 'void QWebView::runJavaScript(const QString &script, const
    std::function<void (const QVariant &)> &resultCallback)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebView.runJavaScript' has no cute function yet. Qt's 'void "
        "QWebView::runJavaScript(const QString &script, const "
        "std::function<void (const QVariant &)> &resultCallback)': takes a "
        "type Python has no way to hand over yet.")
