"""
QTextBrowser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtextbrowser.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtGui import QTextDocument
from . import QTextEdit, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QUrl, QVariant
  from ..QtGui import QFocusEvent, QKeyEvent, QMouseEvent, QPaintEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextBrowser(QTextEdit):
  """
  The cute side of Qt's QTextBrowser: a plain Python object standing in front
  of one C++ QTextBrowser.

  It is built on the cute 'QTextEdit', as Qt's QTextBrowser is built on Qt's
  QTextEdit, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextBrowser that has a ritual and that Python can
  call so far, 32 names in all: 'metaObject', 'tr', 'source', 'sourceType',
  'searchPaths', 'setSearchPaths', 'loadResource', 'isBackwardAvailable',
  'isForwardAvailable', 'clearHistory', 'historyTitle', 'historyUrl',
  'backwardHistoryCount', 'forwardHistoryCount', 'openExternalLinks',
  'setOpenExternalLinks', 'openLinks', 'setOpenLinks', 'setSource',
  'backward', 'forward', 'home', 'reload', 'event', 'keyPressEvent',
  'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'focusOutEvent',
  'focusNextPrevChild', 'paintEvent', 'doSetSource'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextBrowser::~QTextBrowser()': the destructor: Python never
    removes a C++ QTextBrowser.

  What has no ritual
  ------------------

  14 of the 48 functions Qt declares: 6 a signal; 3 private; 2 takes or gives
  a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTextBrowser is created at the first use, not by
    'QTextBrowser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextBrowser.
  - Qt tells when it has removed the C++ QTextBrowser. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QTextBrowser::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#tr

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
    #  QString QTextBrowser::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QTextBrowser2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBrowser'

  #  A C++ QTextBrowser Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextBrowser'

  #  The functions Qt calls itself that QTextBrowser is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'backward': (
          ('_ZN12QTextBrowser8backwardEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'forward': (
          ('_ZN12QTextBrowser7forwardEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'home': (
          ('_ZN12QTextBrowser4homeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reload': (
          ('_ZN12QTextBrowser6reloadEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'doSetSource': (
          ('_ZN12QTextBrowser11doSetSourceERK4QUrlN13QTextDocument12Resourc'
           'eTypeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('int', 'enum', 'QtGui:QTextDocument.ResourceType'),
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
    Calls Qt's 'const QMetaObject *QTextBrowser::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextBrowser::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QTextBrowser10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QTextBrowser::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QTextBrowser::source() const
    address = self.uglySide.call('ritual_ZNK12QTextBrowser6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceType(self) -> QTextDocument.ResourceType:
    """
    Calls Qt's 'QTextDocument::ResourceType QTextBrowser::sourceType()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#sourceType

    Returns
    -------

    QTextDocument.ResourceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextDocument.ResourceType(number)' gives.
    """
    #  QTextDocument::ResourceType QTextBrowser::sourceType() const
    return QTextDocument.ResourceType(self.uglySide.call(
        'ritual_ZNK12QTextBrowser10sourceTypeEv',
    ))

  def searchPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QTextBrowser::searchPaths() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#searchPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTextBrowser::searchPaths() const
    address = self.uglySide.call('ritual_ZNK12QTextBrowser11searchPathsEv')
    return QStringList._cuteOwning(address)

  def isBackwardAvailable(self) -> bool:
    """
    Calls Qt's 'bool QTextBrowser::isBackwardAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#isBackwardAvailable
    """
    #  bool QTextBrowser::isBackwardAvailable() const
    return self.uglySide.call(
        'ritual_ZNK12QTextBrowser19isBackwardAvailableEv',
    )

  def isForwardAvailable(self) -> bool:
    """
    Calls Qt's 'bool QTextBrowser::isForwardAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#isForwardAvailable
    """
    #  bool QTextBrowser::isForwardAvailable() const
    return self.uglySide.call(
        'ritual_ZNK12QTextBrowser18isForwardAvailableEv',
    )

  @overload(int)
  def historyTitle(self, a0: int) -> str:
    """
    Calls Qt's 'QString QTextBrowser::historyTitle(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#historyTitle

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextBrowser::historyTitle(int a0) const
    return self.uglySide.call('ritual_ZNK12QTextBrowser12historyTitleEi', a0)

  @overload(int)
  def historyUrl(self, a0: int) -> QUrl:
    """
    Calls Qt's 'QUrl QTextBrowser::historyUrl(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#historyUrl

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QTextBrowser::historyUrl(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK12QTextBrowser10historyUrlEi', a0,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def backwardHistoryCount(self) -> int:
    """
    Calls Qt's 'int QTextBrowser::backwardHistoryCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#backwardHistoryCount
    """
    #  int QTextBrowser::backwardHistoryCount() const
    return self.uglySide.call(
        'ritual_ZNK12QTextBrowser20backwardHistoryCountEv',
    )

  def forwardHistoryCount(self) -> int:
    """
    Calls Qt's 'int QTextBrowser::forwardHistoryCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#forwardHistoryCount
    """
    #  int QTextBrowser::forwardHistoryCount() const
    return self.uglySide.call(
        'ritual_ZNK12QTextBrowser19forwardHistoryCountEv',
    )

  def openExternalLinks(self) -> bool:
    """
    Calls Qt's 'bool QTextBrowser::openExternalLinks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#openExternalLinks
    """
    #  bool QTextBrowser::openExternalLinks() const
    return self.uglySide.call(
        'ritual_ZNK12QTextBrowser17openExternalLinksEv',
    )

  def openLinks(self) -> bool:
    """
    Calls Qt's 'bool QTextBrowser::openLinks() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#openLinks
    """
    #  bool QTextBrowser::openLinks() const
    return self.uglySide.call('ritual_ZNK12QTextBrowser9openLinksEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setSearchPaths(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QTextBrowser::setSearchPaths(const QStringList &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#setSearchPaths

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTextBrowser::setSearchPaths(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN12QTextBrowser14setSearchPathsERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(bool)
  def setOpenExternalLinks(self, open: bool) -> None:
    """
    Calls Qt's 'void QTextBrowser::setOpenExternalLinks(bool open)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#setOpenExternalLinks

    Parameters
    ----------

    open : bool
      Passed on as it is.
    """
    #  void QTextBrowser::setOpenExternalLinks(bool open)
    self.uglySide.call(
        'ritual_ZN12QTextBrowser20setOpenExternalLinksEb', open,
    )

  @overload(bool)
  def setOpenLinks(self, open: bool) -> None:
    """
    Calls Qt's 'void QTextBrowser::setOpenLinks(bool open)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#setOpenLinks

    Parameters
    ----------

    open : bool
      Passed on as it is.
    """
    #  void QTextBrowser::setOpenLinks(bool open)
    self.uglySide.call('ritual_ZN12QTextBrowser12setOpenLinksEb', open)

  @overload(QUrl)
  @overload(QUrl, QTextDocument.ResourceType)
  def setSource(
      self,
      name: QUrl,
      type: QTextDocument.ResourceType = (
          QTextDocument.ResourceType.UnknownResource),
  ) -> None:
    """
    Calls Qt's 'void QTextBrowser::setSource(const QUrl &name,
    QTextDocument::ResourceType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#setSource

    Parameters
    ----------

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : QTextDocument.ResourceType
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.ResourceType.UnknownResource.
    """
    #  void QTextBrowser::setSource(const QUrl &name,
    #      QTextDocument::ResourceType type)
    self.uglySide.call(
        'ritual_ZN12QTextBrowser9setSourceERK4QUrlN13QTextDocument12Resourc'
        'eTypeE',
        self._valueOf(name), type.value,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QTextBrowser::QTextBrowser(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#QTextBrowser

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextBrowser::QTextBrowser(QWidget *parent)
    self._noteCreation(QTextBrowser, lambda: Rituals.call(
        'ritual_ZN12QTextBrowserC1EP7QWidget', self._addressOf(parent),
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

  @overload(int, QUrl)
  def loadResource(self, type: int, name: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QTextBrowser::loadResource(int type, const QUrl
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#loadResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextBrowser::loadResource(int type, const QUrl &name)
    ritual = 'ritual_ZN12QTextBrowser12loadResourceEiRK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTextBrowser12loadResourceEiRK4QUrl'
    address = self.uglySide.call(ritual, type, self._valueOf(name))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def clearHistory(self) -> None:
    """
    Calls Qt's 'void QTextBrowser::clearHistory()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#clearHistory
    """
    #  void QTextBrowser::clearHistory()
    self.uglySide.call('ritual_ZN12QTextBrowser12clearHistoryEv')

  def backward(self) -> None:
    """
    Calls Qt's 'void QTextBrowser::backward()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#backward
    """
    #  void QTextBrowser::backward()
    ritual = 'ritual_ZN12QTextBrowser8backwardEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTextBrowser8backwardEv'
    self.uglySide.call(ritual)

  def forward(self) -> None:
    """
    Calls Qt's 'void QTextBrowser::forward()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#forward
    """
    #  void QTextBrowser::forward()
    ritual = 'ritual_ZN12QTextBrowser7forwardEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTextBrowser7forwardEv'
    self.uglySide.call(ritual)

  def home(self) -> None:
    """
    Calls Qt's 'void QTextBrowser::home()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#home
    """
    #  void QTextBrowser::home()
    ritual = 'ritual_ZN12QTextBrowser4homeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTextBrowser4homeEv'
    self.uglySide.call(ritual)

  def reload(self) -> None:
    """
    Calls Qt's 'void QTextBrowser::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#reload
    """
    #  void QTextBrowser::reload()
    ritual = 'ritual_ZN12QTextBrowser6reloadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QTextBrowser6reloadEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QTextBrowser::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTextBrowser::event(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN12QTextBrowser5eventEP6QEvent', self._addressOf(e),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, ev: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QTextBrowser::keyPressEvent(QKeyEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#keyPressEvent

    Parameters
    ----------

    ev : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBrowser::keyPressEvent(QKeyEvent *ev)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser13keyPressEventEP9QKeyEvent',
        self._addressOf(ev),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QTextBrowser::mouseMoveEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#mouseMoveEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBrowser::mouseMoveEvent(QMouseEvent *ev)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser14mouseMoveEventEP11QMouseEvent',
        self._addressOf(ev),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QTextBrowser::mousePressEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#mousePressEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBrowser::mousePressEvent(QMouseEvent *ev)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser15mousePressEventEP11QMouseEvent',
        self._addressOf(ev),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QTextBrowser::mouseReleaseEvent(QMouseEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#mouseReleaseEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBrowser::mouseReleaseEvent(QMouseEvent *ev)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(ev),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, ev: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QTextBrowser::focusOutEvent(QFocusEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#focusOutEvent

    Parameters
    ----------

    ev : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBrowser::focusOutEvent(QFocusEvent *ev)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser13focusOutEventEP11QFocusEvent',
        self._addressOf(ev),
    )

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QTextBrowser::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextbrowser.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QTextBrowser::focusNextPrevChild(bool next)
    return self.uglySide.call(
        'ritual_own_ZN12QTextBrowser18focusNextPrevChildEb', next,
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QTextBrowser::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBrowser::paintEvent(QPaintEvent *e)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser10paintEventEP11QPaintEvent',
        self._addressOf(e),
    )

  @overload(QUrl)
  @overload(QUrl, QTextDocument.ResourceType)
  def doSetSource(
      self,
      name: QUrl,
      type: QTextDocument.ResourceType = (
          QTextDocument.ResourceType.UnknownResource),
  ) -> None:
    """
    Calls Qt's 'void QTextBrowser::doSetSource(const QUrl &name,
    QTextDocument::ResourceType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextbrowser.html#doSetSource

    Parameters
    ----------

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : QTextDocument.ResourceType
      Passed on as its number. May be left out, as in Qt: it is then
      QTextDocument.ResourceType.UnknownResource.
    """
    #  void QTextBrowser::doSetSource(const QUrl &name,
    #      QTextDocument::ResourceType type)
    self.uglySide.call(
        'ritual_own_ZN12QTextBrowser11doSetSourceERK4QUrlN13QTextDocument12'
        'ResourceTypeE',
        self._valueOf(name), type.value,
    )
