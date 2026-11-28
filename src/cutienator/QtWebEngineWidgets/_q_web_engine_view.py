"""
QWebEngineView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineWidgets/qwebengineview.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget
from ..QtWebEngineCore import QWebEnginePage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject, QSize, QUrl
  from ..QtGui import QAction, QCloseEvent, QContextMenuEvent
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QHideEvent, QIcon, QPageLayout, QPageRanges
  from ..QtGui import QShowEvent
  from ..QtWidgets import QMenu
  from ..QtWebEngineCore import QWebEngineContextMenuRequest, QWebEngineFrame
  from ..QtWebEngineCore import QWebEngineHistory, QWebEngineHttpRequest
  from ..QtWebEngineCore import QWebEngineProfile, QWebEngineSettings
  from ..QtPrintSupport import QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCloseEvent = WAIT['QCloseEvent']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QIcon = WAIT['QIcon']
  QPageLayout = WAIT['QPageLayout']
  QPageRanges = WAIT['QPageRanges']
  QPrinter = WAIT['QPrinter']
  QShowEvent = WAIT['QShowEvent']
  QUrl = WAIT['QUrl']
  QWebEngineFrame = WAIT['QWebEngineFrame']
  QWebEngineHttpRequest = WAIT['QWebEngineHttpRequest']
  QWebEngineProfile = WAIT['QWebEngineProfile']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineView(QWidget):
  """
  The cute side of Qt's QWebEngineView: a plain Python object standing in
  front of one C++ QWebEngineView.

  It is built on the cute 'QWidget', as Qt's QWebEngineView is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineView that has a ritual and that Python can
  call so far, 53 names in all: 'metaObject', 'tr', 'forPage', 'page',
  'setPage', 'load', 'setHtml', 'setContent', 'history', 'title', 'setUrl',
  'url', 'iconUrl', 'icon', 'hasSelection', 'selectedText', 'pageAction',
  'triggerPageAction', 'zoomFactor', 'setZoomFactor', 'sizeHint', 'settings',
  'createStandardContextMenu', 'lastContextMenuRequest', 'printToPdf',
  'print', 'stop', 'back', 'forward', 'reload', 'loadStarted',
  'loadProgress', 'loadFinished', 'titleChanged', 'selectionChanged',
  'urlChanged', 'iconUrlChanged', 'iconChanged', 'renderProcessTerminated',
  'pdfPrintingFinished', 'printRequested', 'printRequestedByFrame',
  'printFinished', 'createWindow', 'contextMenuEvent', 'event', 'showEvent',
  'hideEvent', 'closeEvent', 'dragEnterEvent', 'dragLeaveEvent',
  'dragMoveEvent', 'dropEvent'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWebEngineView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineView::~QWebEngineView()': the destructor: Python never
    removes a C++ QWebEngineView.
  - Qt's 'void QWebEngineView::findText(const QString &subString,
    QWebEnginePage::FindFlags options, const std::function<void (const
    QWebEngineFindTextResult &)> &resultCallback)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QWebEngineView::printToPdf(const std::function<void (const
    QByteArray &)> &resultCallback, const QPageLayout &layout, const
    QPageRanges &ranges)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineViewPrivate *QWebEngineView::d_func()': gives
    'QWebEngineViewPrivate', which has no cute class yet.
  - Qt's 'const QWebEngineViewPrivate *QWebEngineView::d_func() const': gives
    'QWebEngineViewPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 68 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineView is created at the first use, not by
    'QWebEngineView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineView.
  - Qt tells when it has removed the C++ QWebEngineView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineView that has no cute function yet,
    'findText', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QWebEngineView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#tr

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
    #  QString QWebEngineView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWebEngineView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QWebEnginePage)
  @overload(NoneType)
  def forPage(page: Optional[QWebEnginePage]) -> Optional[QWebEngineView]:
    """
    Calls Qt's 'QWebEngineView *QWebEngineView::forPage(const QWebEnginePage
    *page)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#forPage

    Parameters
    ----------

    page : Optional[QWebEnginePage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWebEngineView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineView *QWebEngineView::forPage(const QWebEnginePage *page)
    address = Rituals.call(
        'ritual_ZN14QWebEngineView7forPageEPK14QWebEnginePage',
        CuteMixin._addressOf(page),
    )
    return QWebEngineView._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineView'

  #  A C++ QWebEngineView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineView'

  #  The functions Qt calls itself that QWebEngineView is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createWindow': (
          ('_ZN14QWebEngineView12createWindowEN14QWebEnginePage13WebWindowT'
           'ypeE',
           ('address', 'address', 'QtWebEngineWidgets:QWebEngineView'),
           (
               ('int', 'enum',
                'QtWebEngineCore:QWebEnginePage.WebWindowType'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def page(self) -> Optional[QWebEnginePage]:
    """
    Calls Qt's 'QWebEnginePage *QWebEngineView::page() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#page

    Returns
    -------

    Optional[QWebEnginePage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEnginePage *QWebEngineView::page() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView4pageEv')
    return QWebEnginePage._cuteAt(address)

  def history(self) -> Optional[QWebEngineHistory]:
    """
    Calls Qt's 'QWebEngineHistory *QWebEngineView::history() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#history

    Returns
    -------

    Optional[QWebEngineHistory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistory *QWebEngineView::history() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView7historyEv')
    from ..QtWebEngineCore import QWebEngineHistory
    return QWebEngineHistory._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QWebEngineView::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineView::title() const
    return self.uglySide.call('ritual_ZNK14QWebEngineView5titleEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineView::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineView::url() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def iconUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineView::iconUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#iconUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineView::iconUrl() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView7iconUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QWebEngineView::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QWebEngineView::icon() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineView::hasSelection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#hasSelection
    """
    #  bool QWebEngineView::hasSelection() const
    return self.uglySide.call('ritual_ZNK14QWebEngineView12hasSelectionEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QWebEngineView::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineView::selectedText() const
    return self.uglySide.call('ritual_ZNK14QWebEngineView12selectedTextEv')

  @overload(QWebEnginePage.WebAction)
  def pageAction(
      self,
      action: QWebEnginePage.WebAction,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QWebEngineView::pageAction(QWebEnginePage::WebAction
    action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#pageAction

    Parameters
    ----------

    action : QWebEnginePage.WebAction
      Passed on as its number.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QWebEngineView::pageAction(QWebEnginePage::WebAction action)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEngineView10pageActionEN14QWebEnginePage9WebAction'
        'E',
        action.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'qreal QWebEngineView::zoomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#zoomFactor
    """
    #  qreal QWebEngineView::zoomFactor() const
    return self.uglySide.call('ritual_ZNK14QWebEngineView10zoomFactorEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWebEngineView::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWebEngineView::sizeHint() const
    ritual = 'ritual_ZNK14QWebEngineView8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QWebEngineView8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def settings(self) -> Optional[QWebEngineSettings]:
    """
    Calls Qt's 'QWebEngineSettings *QWebEngineView::settings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#settings

    Returns
    -------

    Optional[QWebEngineSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineSettings *QWebEngineView::settings() const
    address = self.uglySide.call('ritual_ZNK14QWebEngineView8settingsEv')
    from ..QtWebEngineCore import QWebEngineSettings
    return QWebEngineSettings._cuteAt(address)

  def lastContextMenuRequest(self) -> Optional[QWebEngineContextMenuRequest]:
    """
    Calls Qt's 'QWebEngineContextMenuRequest
    *QWebEngineView::lastContextMenuRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#lastContextMenuRequest

    Returns
    -------

    Optional[QWebEngineContextMenuRequest]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineContextMenuRequest *QWebEngineView::lastContextMenuRequest()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QWebEngineView22lastContextMenuRequestEv',
    )
    from ..QtWebEngineCore import QWebEngineContextMenuRequest
    return QWebEngineContextMenuRequest._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWebEnginePage)
  @overload(NoneType)
  def setPage(self, page: Optional[QWebEnginePage]) -> None:
    """
    Calls Qt's 'void QWebEngineView::setPage(QWebEnginePage *page)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#setPage

    Parameters
    ----------

    page : Optional[QWebEnginePage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::setPage(QWebEnginePage *page)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView7setPageEP14QWebEnginePage',
        self._addressOf(page),
    )

  @overload(str)
  @overload(str, QUrl)
  def setHtml(self, html: str, baseUrl: Optional[QUrl] = None) -> None:
    """
    Calls Qt's 'void QWebEngineView::setHtml(const QString &html, const QUrl
    &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#setHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebEngineView::setHtml(const QString &html, const QUrl &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN14QWebEngineView7setHtmlERK7QStringRK4QUrl',
        html, self._valueOf(baseUrl),
    )

  @overload(QByteArray)
  @overload(QByteArray, str)
  @overload(QByteArray, str, QUrl)
  def setContent(
      self,
      data: QByteArray,
      mimeType: str = '',
      baseUrl: Optional[QUrl] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineView::setContent(const QByteArray &data, const
    QString &mimeType, const QUrl &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#setContent

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mimeType : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    baseUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebEngineView::setContent(const QByteArray &data, const QString
    #      &mimeType, const QUrl &baseUrl)
    if baseUrl is None:
      from ..QtCore import QUrl
      baseUrl = QUrl()
    self.uglySide.call(
        'ritual_ZN14QWebEngineView10setContentERK10QByteArrayRK7QStringRK4Q'
        'Url',
        self._valueOf(data), mimeType, self._valueOf(baseUrl),
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineView::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineView::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(float)
  def setZoomFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QWebEngineView::setZoomFactor(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#setZoomFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QWebEngineView::setZoomFactor(qreal factor)
    self.uglySide.call('ritual_ZN14QWebEngineView13setZoomFactorEd', factor)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QWebEngineView::QWebEngineView(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#QWebEngineView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineView::QWebEngineView(QWidget *parent)
    self._noteCreation(QWebEngineView, lambda: Rituals.call(
        'ritual_ZN14QWebEngineViewC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QWebEngineProfile)
  @overload(QWebEngineProfile, QWidget)
  @overload(QWebEngineProfile, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      profile: Optional[QWebEngineProfile],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineView::QWebEngineView(QWebEngineProfile *profile, QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#QWebEngineView

    Parameters
    ----------

    profile : Optional[QWebEngineProfile]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineView::QWebEngineView(QWebEngineProfile *profile, QWidget
    #      *parent)
    self._noteCreation(QWebEngineView, lambda: Rituals.call(
        'ritual_ZN14QWebEngineViewC1EP17QWebEngineProfileP7QWidget',
        self._addressOf(profile), self._addressOf(parent),
    ))

  @overload(QWebEnginePage)
  @overload(QWebEnginePage, QWidget)
  @overload(QWebEnginePage, NoneType)
  def __init__(
      self,
      page: Optional[QWebEnginePage],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineView::QWebEngineView(QWebEnginePage *page, QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#QWebEngineView

    Parameters
    ----------

    page : Optional[QWebEnginePage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineView::QWebEngineView(QWebEnginePage *page, QWidget *parent)
    self._noteCreation(QWebEngineView, lambda: Rituals.call(
        'ritual_ZN14QWebEngineViewC1EP14QWebEnginePageP7QWidget',
        self._addressOf(page), self._addressOf(parent),
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

  @overload(QUrl)
  def load(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineView::load(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#load

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineView::load(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView4loadERK4QUrl', self._valueOf(url),
    )

  @overload(QWebEngineHttpRequest)
  def load(self, request: QWebEngineHttpRequest) -> None:
    """
    Calls Qt's 'void QWebEngineView::load(const QWebEngineHttpRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#load

    Parameters
    ----------

    request : QWebEngineHttpRequest
      Passed on as a value: Qt reads the C++ QWebEngineHttpRequest, which
      stays Python's own.
    """
    #  void QWebEngineView::load(const QWebEngineHttpRequest &request)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView4loadERK21QWebEngineHttpRequest',
        self._valueOf(request),
    )

  @overload(QWebEnginePage.WebAction)
  @overload(QWebEnginePage.WebAction, bool)
  def triggerPageAction(
      self,
      action: QWebEnginePage.WebAction,
      checked: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QWebEngineView::triggerPageAction(QWebEnginePage::WebAction action, bool
    checked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#triggerPageAction

    Parameters
    ----------

    action : QWebEnginePage.WebAction
      Passed on as its number.

    checked : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWebEngineView::triggerPageAction(QWebEnginePage::WebAction
    #      action, bool checked)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView17triggerPageActionEN14QWebEnginePage9Web'
        'ActionEb',
        action.value, checked,
    )

  def createStandardContextMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QWebEngineView::createStandardContextMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#createStandardContextMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QWebEngineView::createStandardContextMenu()
    address = self.uglySide.call(
        'ritual_ZN14QWebEngineView25createStandardContextMenuEv',
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  @overload(str, QPageLayout)
  @overload(str, QPageLayout, QPageRanges)
  def printToPdf(
      self,
      filePath: str,
      layout: QPageLayout,
      ranges: Optional[QPageRanges] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineView::printToPdf(const QString &filePath,
    const QPageLayout &layout, const QPageRanges &ranges)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#printToPdf

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    layout : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.

    ranges : Optional[QPageRanges]
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own. May be left out, as in Qt: a new 'QPageRanges()' is then
      passed on.
    """
    #  void QWebEngineView::printToPdf(const QString &filePath, const
    #      QPageLayout &layout, const QPageRanges &ranges)
    if ranges is None:
      from ..QtGui import QPageRanges
      ranges = QPageRanges()
    self.uglySide.call(
        'ritual_ZN14QWebEngineView10printToPdfERK7QStringRK11QPageLayoutRK1'
        '1QPageRanges',
        filePath, self._valueOf(layout), self._valueOf(ranges),
    )

  @overload(QPrinter)
  @overload(NoneType)
  def print(self, printer: Optional[QPrinter]) -> None:
    """
    Calls Qt's 'void QWebEngineView::print(QPrinter *printer)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#print

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::print(QPrinter *printer)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView5printEP8QPrinter',
        self._addressOf(printer),
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#stop
    """
    #  void QWebEngineView::stop()
    self.uglySide.call('ritual_ZN14QWebEngineView4stopEv')

  def back(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::back()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#back
    """
    #  void QWebEngineView::back()
    self.uglySide.call('ritual_ZN14QWebEngineView4backEv')

  def forward(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::forward()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#forward
    """
    #  void QWebEngineView::forward()
    self.uglySide.call('ritual_ZN14QWebEngineView7forwardEv')

  def reload(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#reload
    """
    #  void QWebEngineView::reload()
    self.uglySide.call('ritual_ZN14QWebEngineView6reloadEv')

  def loadStarted(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::loadStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#loadStarted
    """
    #  void QWebEngineView::loadStarted()
    self.uglySide.call('ritual_ZN14QWebEngineView11loadStartedEv')

  @overload(int)
  def loadProgress(self, progress: int) -> None:
    """
    Calls Qt's 'void QWebEngineView::loadProgress(int progress)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#loadProgress

    Parameters
    ----------

    progress : int
      Passed on as it is.
    """
    #  void QWebEngineView::loadProgress(int progress)
    self.uglySide.call('ritual_ZN14QWebEngineView12loadProgressEi', progress)

  @overload(bool)
  def loadFinished(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWebEngineView::loadFinished(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#loadFinished

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWebEngineView::loadFinished(bool a0)
    self.uglySide.call('ritual_ZN14QWebEngineView12loadFinishedEb', a0)

  @overload(str)
  def titleChanged(self, title: str) -> None:
    """
    Calls Qt's 'void QWebEngineView::titleChanged(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#titleChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebEngineView::titleChanged(const QString &title)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView12titleChangedERK7QString', title,
    )

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#selectionChanged
    """
    #  void QWebEngineView::selectionChanged()
    self.uglySide.call('ritual_ZN14QWebEngineView16selectionChangedEv')

  @overload(QUrl)
  def urlChanged(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineView::urlChanged(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#urlChanged

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineView::urlChanged(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView10urlChangedERK4QUrl', self._valueOf(a0),
    )

  @overload(QUrl)
  def iconUrlChanged(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineView::iconUrlChanged(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#iconUrlChanged

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineView::iconUrlChanged(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView14iconUrlChangedERK4QUrl',
        self._valueOf(a0),
    )

  @overload(QIcon)
  def iconChanged(self, a0: QIcon) -> None:
    """
    Calls Qt's 'void QWebEngineView::iconChanged(const QIcon &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#iconChanged

    Parameters
    ----------

    a0 : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QWebEngineView::iconChanged(const QIcon &a0)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView11iconChangedERK5QIcon', self._valueOf(a0),
    )

  @overload(QWebEnginePage.RenderProcessTerminationStatus, int)
  def renderProcessTerminated(
      self,
      terminationStatus: QWebEnginePage.RenderProcessTerminationStatus,
      exitCode: int,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineView::renderProcessTerminated(QWebEnginePage::
    RenderProcessTerminationStatus terminationStatus, int exitCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#renderProcessTerminated

    Parameters
    ----------

    terminationStatus : QWebEnginePage.RenderProcessTerminationStatus
      Passed on as its number.

    exitCode : int
      Passed on as it is.
    """
    #  void QWebEngineView::renderProcessTerminated(QWebEnginePage::
    #      RenderProcessTerminationStatus terminationStatus, int exitCode)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView23renderProcessTerminatedEN14QWebEnginePa'
        'ge30RenderProcessTerminationStatusEi',
        terminationStatus.value, exitCode,
    )

  @overload(str, bool)
  def pdfPrintingFinished(self, filePath: str, success: bool) -> None:
    """
    Calls Qt's 'void QWebEngineView::pdfPrintingFinished(const QString
    &filePath, bool success)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#pdfPrintingFinished

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    success : bool
      Passed on as it is.
    """
    #  void QWebEngineView::pdfPrintingFinished(const QString &filePath, bool
    #      success)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView19pdfPrintingFinishedERK7QStringb',
        filePath, success,
    )

  def printRequested(self) -> None:
    """
    Calls Qt's 'void QWebEngineView::printRequested()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#printRequested
    """
    #  void QWebEngineView::printRequested()
    self.uglySide.call('ritual_ZN14QWebEngineView14printRequestedEv')

  @overload(QWebEngineFrame)
  def printRequestedByFrame(self, frame: QWebEngineFrame) -> None:
    """
    Calls Qt's 'void QWebEngineView::printRequestedByFrame(QWebEngineFrame
    frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#printRequestedByFrame

    Parameters
    ----------

    frame : QWebEngineFrame
      Passed on as a value: Qt reads the C++ QWebEngineFrame, which stays
      Python's own.
    """
    #  void QWebEngineView::printRequestedByFrame(QWebEngineFrame frame)
    self.uglySide.call(
        'ritual_ZN14QWebEngineView21printRequestedByFrameE15QWebEngineFrame',
        self._valueOf(frame),
    )

  @overload(bool)
  def printFinished(self, success: bool) -> None:
    """
    Calls Qt's 'void QWebEngineView::printFinished(bool success)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#printFinished

    Parameters
    ----------

    success : bool
      Passed on as it is.
    """
    #  void QWebEngineView::printFinished(bool success)
    self.uglySide.call('ritual_ZN14QWebEngineView13printFinishedEb', success)

  @overload(QWebEnginePage.WebWindowType)
  def createWindow(
      self,
      type: QWebEnginePage.WebWindowType,
  ) -> Optional[QWebEngineView]:
    """
    Calls Qt's 'QWebEngineView
    *QWebEngineView::createWindow(QWebEnginePage::WebWindowType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#createWindow

    Parameters
    ----------

    type : QWebEnginePage.WebWindowType
      Passed on as its number.

    Returns
    -------

    Optional[QWebEngineView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineView
    #      *QWebEngineView::createWindow(QWebEnginePage::WebWindowType type)
    ritual = (
        'ritual_ZN14QWebEngineView12createWindowEN14QWebEnginePage13WebWind'
        'owTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEngineView12createWindowEN14QWebEnginePage13W'
          'ebWindowTypeE')
    address = self.uglySide.call(ritual, type.value)
    return QWebEngineView._cuteAt(address)

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, a0: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::contextMenuEvent(QContextMenuEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineview.html#contextMenuEvent

    Parameters
    ----------

    a0 : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::contextMenuEvent(QContextMenuEvent *a0)
    ritual = (
        'ritual_ZN14QWebEngineView16contextMenuEventEP17QContextMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEngineView16contextMenuEventEP17QContextMenuE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWebEngineView::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWebEngineView::event(QEvent *a0)
    ritual = 'ritual_ZN14QWebEngineView5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEngineView5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::showEvent(QShowEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::showEvent(QShowEvent *a0)
    ritual = 'ritual_ZN14QWebEngineView9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEngineView9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::hideEvent(QHideEvent *a0)
    ritual = 'ritual_ZN14QWebEngineView9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEngineView9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, a0: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::closeEvent(QCloseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#closeEvent

    Parameters
    ----------

    a0 : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::closeEvent(QCloseEvent *a0)
    ritual = 'ritual_ZN14QWebEngineView10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEngineView10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, e: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::dragEnterEvent(QDragEnterEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#dragEnterEvent

    Parameters
    ----------

    e : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::dragEnterEvent(QDragEnterEvent *e)
    ritual = 'ritual_ZN14QWebEngineView14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEngineView14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#dragLeaveEvent

    Parameters
    ----------

    e : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::dragLeaveEvent(QDragLeaveEvent *e)
    ritual = 'ritual_ZN14QWebEngineView14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEngineView14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, e: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::dragMoveEvent(QDragMoveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::dragMoveEvent(QDragMoveEvent *e)
    ritual = 'ritual_ZN14QWebEngineView13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWebEngineView13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, e: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineView::dropEvent(QDropEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineview.html#dropEvent

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineView::dropEvent(QDropEvent *e)
    ritual = 'ritual_ZN14QWebEngineView9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QWebEngineView9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def findText(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineView::findText(const QString &subString,
    QWebEnginePage::FindFlags options, const std::function<void (const
    QWebEngineFindTextResult &)> &resultCallback)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineView.findText' has no cute function yet. Qt's 'void "
        "QWebEngineView::findText(const QString &subString, "
        "QWebEnginePage::FindFlags options, const std::function<void (const "
        "QWebEngineFindTextResult &)> &resultCallback)': takes a type "
        "Python has no way to hand over yet.")
