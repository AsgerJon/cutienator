"""
QWebViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebView/6.12.0/QtWebView/private/qwebview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QWebViewPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from ..QtGui import QWindow
  from . import QWebViewSettingsPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebViewPrivate(QObject):
  """
  The cute side of Qt's QWebViewPrivate: a plain Python object standing in
  front of one C++ QWebViewPrivate.

  It is built on the cute 'QObject', as Qt's QWebViewPrivate is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebViewPrivate that has a ritual and that Python
  can call so far, 20 names in all: 'initialize', 'settings',
  'httpUserAgent', 'setHttpUserAgent', 'setUrl', 'canGoBack', 'canGoForward',
  'title', 'url', 'loadProgress', 'isLoading', 'goBack', 'goForward', 'stop',
  'reload', 'loadHtml', 'setCookie', 'deleteCookie', 'deleteAllCookies',
  'nativeWindow'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QWebViewPrivate::runJavaScript(const QString &script, const
    std::function<void (const QVariant &)> &resultCallback)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 22 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QWebViewPrivate is created at the first use, not by
    'QWebViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebViewPrivate.
  - Qt tells when it has removed the C++ QWebViewPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebViewPrivate that has no cute function yet,
    '__init__', 'runJavaScript', holds a function that raises
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
  __qt_class__ = 'QWebViewPrivate'

  #  A C++ QWebViewPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebViewPrivate'

  #  The functions Qt calls itself that QWebViewPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'runJavaScript': (
          'void QWebViewPrivate::runJavaScript(const QString &, const '
          'std::function<void (const QVariant &)> &)',
      ),
  }

  #  The functions Qt calls itself that QWebViewPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN15QWebViewPrivate10initializeEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'settings': (
          ('_ZNK15QWebViewPrivate8settingsEv',
           ('address', 'address', 'QtWebView:QWebViewSettingsPrivate'),
           ()),
      ),
      'httpUserAgent': (
          ('_ZNK15QWebViewPrivate13httpUserAgentEv',
           ('address', 'text', ''),
           ()),
      ),
      'setHttpUserAgent': (
          ('_ZN15QWebViewPrivate16setHttpUserAgentERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setUrl': (
          ('_ZN15QWebViewPrivate6setUrlERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'canGoBack': (
          ('_ZNK15QWebViewPrivate9canGoBackEv',
           ('bool', 'number', ''),
           ()),
      ),
      'canGoForward': (
          ('_ZNK15QWebViewPrivate12canGoForwardEv',
           ('bool', 'number', ''),
           ()),
      ),
      'title': (
          ('_ZNK15QWebViewPrivate5titleEv',
           ('address', 'text', ''),
           ()),
      ),
      'url': (
          ('_ZNK15QWebViewPrivate3urlEv',
           ('address', 'value', 'QtCore:QUrl'),
           ()),
      ),
      'loadProgress': (
          ('_ZNK15QWebViewPrivate12loadProgressEv',
           ('int', 'number', ''),
           ()),
      ),
      'isLoading': (
          ('_ZNK15QWebViewPrivate9isLoadingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'goBack': (
          ('_ZN15QWebViewPrivate6goBackEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'goForward': (
          ('_ZN15QWebViewPrivate9goForwardEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN15QWebViewPrivate4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reload': (
          ('_ZN15QWebViewPrivate6reloadEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'loadHtml': (
          ('_ZN15QWebViewPrivate8loadHtmlERK7QStringRK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'setCookie': (
          ('_ZN15QWebViewPrivate9setCookieERK7QStringS2_S2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'deleteCookie': (
          ('_ZN15QWebViewPrivate12deleteCookieERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'deleteAllCookies': (
          ('_ZN15QWebViewPrivate16deleteAllCookiesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'nativeWindow': (
          ('_ZNK15QWebViewPrivate12nativeWindowEv',
           ('address', 'address', 'QtGui:QWindow'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def settings(self) -> Optional[QWebViewSettingsPrivate]:
    """
    Calls Qt's 'QWebViewSettingsPrivate *QWebViewPrivate::settings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#settings

    Returns
    -------

    Optional[QWebViewSettingsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebViewSettingsPrivate *QWebViewPrivate::settings() const
    address = self.uglySide.call('ritual_ZNK15QWebViewPrivate8settingsEv')
    from . import QWebViewSettingsPrivate
    return QWebViewSettingsPrivate._cuteAt(address)

  def httpUserAgent(self) -> str:
    """
    Calls Qt's 'QString QWebViewPrivate::httpUserAgent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#httpUserAgent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebViewPrivate::httpUserAgent() const
    return self.uglySide.call('ritual_ZNK15QWebViewPrivate13httpUserAgentEv')

  def canGoBack(self) -> bool:
    """
    Calls Qt's 'bool QWebViewPrivate::canGoBack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#canGoBack
    """
    #  bool QWebViewPrivate::canGoBack() const
    return self.uglySide.call('ritual_ZNK15QWebViewPrivate9canGoBackEv')

  def canGoForward(self) -> bool:
    """
    Calls Qt's 'bool QWebViewPrivate::canGoForward() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#canGoForward
    """
    #  bool QWebViewPrivate::canGoForward() const
    return self.uglySide.call('ritual_ZNK15QWebViewPrivate12canGoForwardEv')

  def title(self) -> str:
    """
    Calls Qt's 'QString QWebViewPrivate::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebViewPrivate::title() const
    return self.uglySide.call('ritual_ZNK15QWebViewPrivate5titleEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebViewPrivate::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebViewPrivate::url() const
    address = self.uglySide.call('ritual_ZNK15QWebViewPrivate3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def loadProgress(self) -> int:
    """
    Calls Qt's 'int QWebViewPrivate::loadProgress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#loadProgress
    """
    #  int QWebViewPrivate::loadProgress() const
    return self.uglySide.call('ritual_ZNK15QWebViewPrivate12loadProgressEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QWebViewPrivate::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#isLoading
    """
    #  bool QWebViewPrivate::isLoading() const
    return self.uglySide.call('ritual_ZNK15QWebViewPrivate9isLoadingEv')

  def nativeWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWebViewPrivate::nativeWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#nativeWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWebViewPrivate::nativeWindow() const
    address = self.uglySide.call(
        'ritual_ZNK15QWebViewPrivate12nativeWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHttpUserAgent(self, httpUserAgent: str) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::setHttpUserAgent(const QString
    &httpUserAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewprivate.html#setHttpUserAgent

    Parameters
    ----------

    httpUserAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebViewPrivate::setHttpUserAgent(const QString &httpUserAgent)
    self.uglySide.call(
        'ritual_ZN15QWebViewPrivate16setHttpUserAgentERK7QString',
        httpUserAgent,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebViewPrivate::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN15QWebViewPrivate6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(str, str, str)
  def setCookie(self, domain: str, name: str, value: str) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::setCookie(const QString &domain, const
    QString &name, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#setCookie

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebViewPrivate::setCookie(const QString &domain, const QString
    #      &name, const QString &value)
    self.uglySide.call(
        'ritual_ZN15QWebViewPrivate9setCookieERK7QStringS2_S2_',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebViewPrivate::QWebViewPrivate(QWebView *view)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QWebViewPrivate.__init__' has no cute function yet. Qt's "
        "'QWebViewPrivate::QWebViewPrivate(QWebView *view)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(QObject)
  @overload(NoneType)
  def initialize(self, context: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::initialize(QObject *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#initialize

    Parameters
    ----------

    context : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebViewPrivate::initialize(QObject *context)
    self.uglySide.call(
        'ritual_ZN15QWebViewPrivate10initializeEP7QObject',
        self._addressOf(context, 'QObject'),
    )

  def goBack(self) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::goBack()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#goBack
    """
    #  void QWebViewPrivate::goBack()
    self.uglySide.call('ritual_ZN15QWebViewPrivate6goBackEv')

  def goForward(self) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::goForward()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#goForward
    """
    #  void QWebViewPrivate::goForward()
    self.uglySide.call('ritual_ZN15QWebViewPrivate9goForwardEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#stop
    """
    #  void QWebViewPrivate::stop()
    self.uglySide.call('ritual_ZN15QWebViewPrivate4stopEv')

  def reload(self) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#reload
    """
    #  void QWebViewPrivate::reload()
    self.uglySide.call('ritual_ZN15QWebViewPrivate6reloadEv')

  @overload(str, QUrl)
  def loadHtml(self, html: str, baseUrl: QUrl) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::loadHtml(const QString &html, const
    QUrl &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#loadHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebViewPrivate::loadHtml(const QString &html, const QUrl
    #      &baseUrl)
    self.uglySide.call(
        'ritual_ZN15QWebViewPrivate8loadHtmlERK7QStringRK4QUrl',
        html, self._valueOf(baseUrl),
    )

  @overload(str, str)
  def deleteCookie(self, domain: str, name: str) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::deleteCookie(const QString &domain,
    const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewprivate.html#deleteCookie

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebViewPrivate::deleteCookie(const QString &domain, const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN15QWebViewPrivate12deleteCookieERK7QStringS2_',
        domain, name,
    )

  def deleteAllCookies(self) -> None:
    """
    Calls Qt's 'void QWebViewPrivate::deleteAllCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewprivate.html#deleteAllCookies
    """
    #  void QWebViewPrivate::deleteAllCookies()
    self.uglySide.call('ritual_ZN15QWebViewPrivate16deleteAllCookiesEv')

  @staticmethod
  def runJavaScript(*__, **_) -> Never:
    """
    Qt's 'void QWebViewPrivate::runJavaScript(const QString &script, const
    std::function<void (const QVariant &)> &resultCallback)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebViewPrivate.runJavaScript' has no cute function yet. Qt's "
        "'void QWebViewPrivate::runJavaScript(const QString &script, const "
        "std::function<void (const QVariant &)> &resultCallback)': takes a "
        "type Python has no way to hand over yet.")
