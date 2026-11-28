"""
QQuickWebView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickWebView to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem, QQuickWindowContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQml import QJSValue
  from . import QQuickWebViewLoadRequest, QQuickWebViewSettings
  from ..QtWebView import QWebViewLoadingInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QQuickWebViewLoadRequest = WAIT['QQuickWebViewLoadRequest']
  QUrl = WAIT['QUrl']
  QWebViewLoadingInfo = WAIT['QWebViewLoadingInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebView(QQuickWindowContainer):
  """
  The cute side of Qt's QQuickWebView: a plain Python object standing in
  front of one C++ QQuickWebView.

  It is built on the cute 'QQuickWindowContainer', as Qt's QQuickWebView is
  built on Qt's QQuickWindowContainer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebView that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'tr', 'httpUserAgent',
  'setHttpUserAgent', 'url', 'setUrl', 'loadProgress', 'title', 'canGoBack',
  'isLoading', 'canGoForward', 'settings', 'classBegin', 'goBack',
  'goForward', 'reload', 'stop', 'loadHtml', 'runJavaScript', 'setCookie',
  'deleteCookie', 'deleteAllCookies', 'titleChanged', 'urlChanged',
  'loadingChanged', 'loadProgressChanged', 'httpUserAgentChanged',
  'cookieAdded', 'cookieRemoved', 'onLoadingChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickWebView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWebView::~QQuickWebView()': the destructor: Python never
    removes a C++ QQuickWebView.
  - Qt's 'QWebView &QQuickWebView::webView() const': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  3 of the 38 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickWebView is created at the first use, not by
    'QQuickWebView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebView.
  - Qt tells when it has removed the C++ QQuickWebView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWebView that has no cute function yet,
    'nativeWindow', 'webView', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LoadStatus(CuteNum):
    """
    The enum 'QQuickWebView::LoadStatus' of Qt, with the 4 names Qt gives in
    it.
    """

    LoadStartedStatus = Kee[int](0)
    LoadStoppedStatus = Kee[int](1)
    LoadSucceededStatus = Kee[int](2)
    LoadFailedStatus = Kee[int](3)

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
    Calls Qt's 'QString QQuickWebView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#tr

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
    #  QString QQuickWebView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickWebView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebView'

  #  A C++ QQuickWebView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWebView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebView::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickWebView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def httpUserAgent(self) -> str:
    """
    Calls Qt's 'QString QQuickWebView::httpUserAgent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#httpUserAgent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebView::httpUserAgent() const
    return self.uglySide.call('ritual_ZNK13QQuickWebView13httpUserAgentEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebView::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebView::url() const
    address = self.uglySide.call('ritual_ZNK13QQuickWebView3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def loadProgress(self) -> int:
    """
    Calls Qt's 'int QQuickWebView::loadProgress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#loadProgress
    """
    #  int QQuickWebView::loadProgress() const
    return self.uglySide.call('ritual_ZNK13QQuickWebView12loadProgressEv')

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickWebView::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebView::title() const
    return self.uglySide.call('ritual_ZNK13QQuickWebView5titleEv')

  def canGoBack(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebView::canGoBack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#canGoBack
    """
    #  bool QQuickWebView::canGoBack() const
    return self.uglySide.call('ritual_ZNK13QQuickWebView9canGoBackEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebView::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#isLoading
    """
    #  bool QQuickWebView::isLoading() const
    return self.uglySide.call('ritual_ZNK13QQuickWebView9isLoadingEv')

  def canGoForward(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebView::canGoForward() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#canGoForward
    """
    #  bool QQuickWebView::canGoForward() const
    return self.uglySide.call('ritual_ZNK13QQuickWebView12canGoForwardEv')

  def settings(self) -> Optional[QQuickWebViewSettings]:
    """
    Calls Qt's 'QQuickWebViewSettings *QQuickWebView::settings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#settings

    Returns
    -------

    Optional[QQuickWebViewSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebViewSettings *QQuickWebView::settings() const
    address = self.uglySide.call('ritual_ZNK13QQuickWebView8settingsEv')
    from . import QQuickWebViewSettings
    return QQuickWebViewSettings._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHttpUserAgent(self, userAgent: str) -> None:
    """
    Calls Qt's 'void QQuickWebView::setHttpUserAgent(const QString
    &userAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebview.html#setHttpUserAgent

    Parameters
    ----------

    userAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebView::setHttpUserAgent(const QString &userAgent)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView16setHttpUserAgentERK7QString', userAgent,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickWebView::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickWebView::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(str, str, str)
  def setCookie(self, domain: str, name: str, value: str) -> None:
    """
    Calls Qt's 'void QQuickWebView::setCookie(const QString &domain, const
    QString &name, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#setCookie

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebView::setCookie(const QString &domain, const QString
    #      &name, const QString &value)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView9setCookieERK7QStringS2_S2_',
        domain, name, value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickWebView::QQuickWebView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#QQuickWebView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWebView::QQuickWebView(QQuickItem *parent)
    self._noteCreation(QQuickWebView, lambda: Rituals.call(
        'ritual_ZN13QQuickWebViewC1EP10QQuickItem', self._addressOf(parent),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#classBegin
    """
    #  void QQuickWebView::classBegin()
    ritual = 'ritual_ZN13QQuickWebView10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickWebView10classBeginEv'
    self.uglySide.call(ritual)

  def goBack(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::goBack()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#goBack
    """
    #  void QQuickWebView::goBack()
    self.uglySide.call('ritual_ZN13QQuickWebView6goBackEv')

  def goForward(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::goForward()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#goForward
    """
    #  void QQuickWebView::goForward()
    self.uglySide.call('ritual_ZN13QQuickWebView9goForwardEv')

  def reload(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#reload
    """
    #  void QQuickWebView::reload()
    self.uglySide.call('ritual_ZN13QQuickWebView6reloadEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#stop
    """
    #  void QQuickWebView::stop()
    self.uglySide.call('ritual_ZN13QQuickWebView4stopEv')

  @overload(str)
  @overload(str, QUrl)
  def loadHtml(self, html: str, baseUrl: Optional[QUrl] = None) -> None:
    """
    Calls Qt's 'void QQuickWebView::loadHtml(const QString &html, const QUrl
    &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#loadHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QQuickWebView::loadHtml(const QString &html, const QUrl &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN13QQuickWebView8loadHtmlERK7QStringRK4QUrl',
        html, self._valueOf(baseUrl),
    )

  @overload(str, QJSValue)
  def runJavaScript(self, script: str, callback: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickWebView::runJavaScript(const QString &script,
    const QJSValue &callback)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#runJavaScript

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebView::runJavaScript(const QString &script, const
    #      QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView13runJavaScriptERK7QStringRK8QJSValue',
        script, self._valueOf(callback),
    )

  @overload(str, str)
  def deleteCookie(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QQuickWebView::deleteCookie(const QString &domain, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#deleteCookie

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebView::deleteCookie(const QString &domain, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView12deleteCookieERK7QStringS2_', domain, name,
    )

  def deleteAllCookies(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::deleteAllCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebview.html#deleteAllCookies
    """
    #  void QQuickWebView::deleteAllCookies()
    self.uglySide.call('ritual_ZN13QQuickWebView16deleteAllCookiesEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::titleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#titleChanged
    """
    #  void QQuickWebView::titleChanged()
    self.uglySide.call('ritual_ZN13QQuickWebView12titleChangedEv')

  def urlChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::urlChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#urlChanged
    """
    #  void QQuickWebView::urlChanged()
    self.uglySide.call('ritual_ZN13QQuickWebView10urlChangedEv')

  @overload(QQuickWebViewLoadRequest)
  @overload(NoneType)
  def loadingChanged(
      self,
      loadRequest: Optional[QQuickWebViewLoadRequest],
  ) -> None:
    """
    Calls Qt's 'void QQuickWebView::loadingChanged(QQuickWebViewLoadRequest
    *loadRequest)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#loadingChanged

    Parameters
    ----------

    loadRequest : Optional[QQuickWebViewLoadRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWebView::loadingChanged(QQuickWebViewLoadRequest
    #      *loadRequest)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView14loadingChangedEP24QQuickWebViewLoadReque'
        'st',
        self._addressOf(loadRequest),
    )

  def loadProgressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::loadProgressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebview.html#loadProgressChanged
    """
    #  void QQuickWebView::loadProgressChanged()
    self.uglySide.call('ritual_ZN13QQuickWebView19loadProgressChangedEv')

  def httpUserAgentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebView::httpUserAgentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebview.html#httpUserAgentChanged
    """
    #  void QQuickWebView::httpUserAgentChanged()
    self.uglySide.call('ritual_ZN13QQuickWebView20httpUserAgentChangedEv')

  @overload(str, str)
  def cookieAdded(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QQuickWebView::cookieAdded(const QString &domain, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#cookieAdded

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebView::cookieAdded(const QString &domain, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView11cookieAddedERK7QStringS2_', domain, name,
    )

  @overload(str, str)
  def cookieRemoved(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QQuickWebView::cookieRemoved(const QString &domain,
    const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwebview.html#cookieRemoved

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebView::cookieRemoved(const QString &domain, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView13cookieRemovedERK7QStringS2_',
        domain, name,
    )

  @overload(QWebViewLoadingInfo)
  def onLoadingChanged(self, loadRequest: QWebViewLoadingInfo) -> None:
    """
    Calls Qt's 'void QQuickWebView::onLoadingChanged(const
    QWebViewLoadingInfo &loadRequest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebview.html#onLoadingChanged

    Parameters
    ----------

    loadRequest : QWebViewLoadingInfo
      Passed on as a value: Qt reads the C++ QWebViewLoadingInfo, which stays
      Python's own.
    """
    #  void QQuickWebView::onLoadingChanged(const QWebViewLoadingInfo
    #      &loadRequest)
    self.uglySide.call(
        'ritual_ZN13QQuickWebView16onLoadingChangedERK19QWebViewLoadingInfo',
        self._valueOf(loadRequest),
    )

  @staticmethod
  def nativeWindow(*__, **_) -> Never:
    """
    Qt's 'QWindow *QQuickWebView::nativeWindow()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickWebView.nativeWindow' has no cute function yet. Qt's "
        "'QWindow *QQuickWebView::nativeWindow()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def webView(*__, **_) -> Never:
    """
    Qt's 'QWebView &QQuickWebView::webView() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickWebView.webView' has no cute function yet. Qt's 'QWebView "
        "&QQuickWebView::webView() const': gives a type Python has no way "
        "to take yet.")
