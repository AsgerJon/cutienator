"""
QPdfView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdfWidgets/qpdfview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtWidgets import QAbstractScrollArea, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMargins, QMetaObject
  from ..QtGui import QMouseEvent, QPaintEvent, QResizeEvent, QWheelEvent
  from ..QtPdf import QPdfDocument, QPdfPageNavigator, QPdfSearchModel
  from . import QPdfViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMargins = WAIT['QMargins']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPdfDocument = WAIT['QPdfDocument']
  QPdfSearchModel = WAIT['QPdfSearchModel']
  QResizeEvent = WAIT['QResizeEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfView(QAbstractScrollArea):
  """
  The cute side of Qt's QPdfView: a plain Python object standing in front of
  one C++ QPdfView.

  It is built on the cute 'QAbstractScrollArea', as Qt's QPdfView is built on
  Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfView that has a ritual and that Python can call
  so far, 35 names in all: 'metaObject', 'tr', 'setDocument', 'document',
  'searchModel', 'setSearchModel', 'currentSearchResultIndex',
  'pageNavigator', 'pageMode', 'zoomMode', 'zoomFactor', 'pageSpacing',
  'setPageSpacing', 'documentMargins', 'setDocumentMargins', 'setPageMode',
  'setZoomMode', 'setZoomFactor', 'setCurrentSearchResultIndex',
  'documentChanged', 'pageModeChanged', 'zoomModeChanged',
  'zoomFactorChanged', 'pageSpacingChanged', 'documentMarginsChanged',
  'searchModelChanged', 'currentSearchResultIndexChanged', 'paintEvent',
  'resizeEvent', 'scrollContentsBy', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'wheelEvent', 'd_func'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfView::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QPdfView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfView::~QPdfView()': the destructor: Python never removes a C++
    QPdfView.
  - Qt's 'const QPdfViewPrivate *QPdfView::d_func() const': takes in Python
    what 'QPdfViewPrivate *QPdfView::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 43 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfView is created at the first use, not by 'QPdfView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfView.
  - Qt tells when it has removed the C++ QPdfView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QPdfView, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class PageMode(CuteNum, scoped=True):
    """
    The enum 'QPdfView::PageMode' of Qt, with the 2 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    SinglePage = Kee[int](0)
    MultiPage = Kee[int](1)

  class ZoomMode(CuteNum, scoped=True):
    """
    The enum 'QPdfView::ZoomMode' of Qt, with the 3 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Custom = Kee[int](0)
    FitToWidth = Kee[int](1)
    FitInView = Kee[int](2)

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
    Calls Qt's 'QString QPdfView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#tr

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
    #  QString QPdfView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QPdfView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfView'

  #  A C++ QPdfView Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfView::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QPdfView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QPdfDocument]:
    """
    Calls Qt's 'QPdfDocument *QPdfView::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#document

    Returns
    -------

    Optional[QPdfDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfDocument *QPdfView::document() const
    address = self.uglySide.call('ritual_ZNK8QPdfView8documentEv')
    from ..QtPdf import QPdfDocument
    return QPdfDocument._cuteAt(address)

  def searchModel(self) -> Optional[QPdfSearchModel]:
    """
    Calls Qt's 'QPdfSearchModel *QPdfView::searchModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#searchModel

    Returns
    -------

    Optional[QPdfSearchModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfSearchModel *QPdfView::searchModel() const
    address = self.uglySide.call('ritual_ZNK8QPdfView11searchModelEv')
    from ..QtPdf import QPdfSearchModel
    return QPdfSearchModel._cuteAt(address)

  def currentSearchResultIndex(self) -> int:
    """
    Calls Qt's 'int QPdfView::currentSearchResultIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfview.html#currentSearchResultIndex
    """
    #  int QPdfView::currentSearchResultIndex() const
    return self.uglySide.call(
        'ritual_ZNK8QPdfView24currentSearchResultIndexEv',
    )

  def pageNavigator(self) -> Optional[QPdfPageNavigator]:
    """
    Calls Qt's 'QPdfPageNavigator *QPdfView::pageNavigator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#pageNavigator

    Returns
    -------

    Optional[QPdfPageNavigator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfPageNavigator *QPdfView::pageNavigator() const
    address = self.uglySide.call('ritual_ZNK8QPdfView13pageNavigatorEv')
    from ..QtPdf import QPdfPageNavigator
    return QPdfPageNavigator._cuteAt(address)

  def pageMode(self) -> PageMode:
    """
    Calls Qt's 'PageMode QPdfView::pageMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#pageMode

    Returns
    -------

    PageMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PageMode(number)' gives.
    """
    #  PageMode QPdfView::pageMode() const
    return QPdfView.PageMode(self.uglySide.call(
        'ritual_ZNK8QPdfView8pageModeEv',
    ))

  def zoomMode(self) -> ZoomMode:
    """
    Calls Qt's 'ZoomMode QPdfView::zoomMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#zoomMode

    Returns
    -------

    ZoomMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ZoomMode(number)' gives.
    """
    #  ZoomMode QPdfView::zoomMode() const
    return QPdfView.ZoomMode(self.uglySide.call(
        'ritual_ZNK8QPdfView8zoomModeEv',
    ))

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'qreal QPdfView::zoomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#zoomFactor
    """
    #  qreal QPdfView::zoomFactor() const
    return self.uglySide.call('ritual_ZNK8QPdfView10zoomFactorEv')

  def pageSpacing(self) -> int:
    """
    Calls Qt's 'int QPdfView::pageSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#pageSpacing
    """
    #  int QPdfView::pageSpacing() const
    return self.uglySide.call('ritual_ZNK8QPdfView11pageSpacingEv')

  def documentMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QPdfView::documentMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#documentMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QPdfView::documentMargins() const
    address = self.uglySide.call('ritual_ZNK8QPdfView15documentMarginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPdfDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfView::setDocument(QPdfDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setDocument

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::setDocument(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN8QPdfView11setDocumentEP12QPdfDocument',
        self._addressOf(document),
    )

  @overload(QPdfSearchModel)
  @overload(NoneType)
  def setSearchModel(self, searchModel: Optional[QPdfSearchModel]) -> None:
    """
    Calls Qt's 'void QPdfView::setSearchModel(QPdfSearchModel *searchModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setSearchModel

    Parameters
    ----------

    searchModel : Optional[QPdfSearchModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::setSearchModel(QPdfSearchModel *searchModel)
    self.uglySide.call(
        'ritual_ZN8QPdfView14setSearchModelEP15QPdfSearchModel',
        self._addressOf(searchModel),
    )

  @overload(int)
  def setPageSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QPdfView::setPageSpacing(int spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setPageSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QPdfView::setPageSpacing(int spacing)
    self.uglySide.call('ritual_ZN8QPdfView14setPageSpacingEi', spacing)

  @overload(QMargins)
  def setDocumentMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void QPdfView::setDocumentMargins(QMargins margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setDocumentMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QPdfView::setDocumentMargins(QMargins margins)
    self.uglySide.call(
        'ritual_ZN8QPdfView18setDocumentMarginsE8QMargins',
        self._valueOf(margins, 'QMargins'),
    )

  @overload(PageMode)
  def setPageMode(self, mode: PageMode) -> None:
    """
    Calls Qt's 'void QPdfView::setPageMode(QPdfView::PageMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setPageMode

    Parameters
    ----------

    mode : PageMode
      Passed on as its number.
    """
    #  void QPdfView::setPageMode(QPdfView::PageMode mode)
    self.uglySide.call(
        'ritual_ZN8QPdfView11setPageModeENS_8PageModeE', mode.value,
    )

  @overload(ZoomMode)
  def setZoomMode(self, mode: ZoomMode) -> None:
    """
    Calls Qt's 'void QPdfView::setZoomMode(QPdfView::ZoomMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setZoomMode

    Parameters
    ----------

    mode : ZoomMode
      Passed on as its number.
    """
    #  void QPdfView::setZoomMode(QPdfView::ZoomMode mode)
    self.uglySide.call(
        'ritual_ZN8QPdfView11setZoomModeENS_8ZoomModeE', mode.value,
    )

  @overload(float)
  def setZoomFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QPdfView::setZoomFactor(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#setZoomFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QPdfView::setZoomFactor(qreal factor)
    self.uglySide.call('ritual_ZN8QPdfView13setZoomFactorEd', factor)

  @overload(int)
  def setCurrentSearchResultIndex(self, currentResult: int) -> None:
    """
    Calls Qt's 'void QPdfView::setCurrentSearchResultIndex(int
    currentResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfview.html#setCurrentSearchResultIndex

    Parameters
    ----------

    currentResult : int
      Passed on as it is.
    """
    #  void QPdfView::setCurrentSearchResultIndex(int currentResult)
    self.uglySide.call(
        'ritual_ZN8QPdfView27setCurrentSearchResultIndexEi', currentResult,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfView::QPdfView()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#QPdfView
    """
    #  QPdfView::QPdfView()
    self._noteCreation(QPdfView, lambda: Rituals.call(
        'ritual_ZN8QPdfViewC1Ev',
    ))

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's 'QPdfView::QPdfView(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#QPdfView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfView::QPdfView(QWidget *parent)
    self._noteCreation(QPdfView, lambda: Rituals.call(
        'ritual_ZN8QPdfViewC1EP7QWidget', self._addressOf(parent),
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

  @overload(QPdfDocument)
  @overload(NoneType)
  def documentChanged(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfView::documentChanged(QPdfDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#documentChanged

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::documentChanged(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN8QPdfView15documentChangedEP12QPdfDocument',
        self._addressOf(document),
    )

  @overload(PageMode)
  def pageModeChanged(self, pageMode: PageMode) -> None:
    """
    Calls Qt's 'void QPdfView::pageModeChanged(QPdfView::PageMode pageMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#pageModeChanged

    Parameters
    ----------

    pageMode : PageMode
      Passed on as its number.
    """
    #  void QPdfView::pageModeChanged(QPdfView::PageMode pageMode)
    self.uglySide.call(
        'ritual_ZN8QPdfView15pageModeChangedENS_8PageModeE', pageMode.value,
    )

  @overload(ZoomMode)
  def zoomModeChanged(self, zoomMode: ZoomMode) -> None:
    """
    Calls Qt's 'void QPdfView::zoomModeChanged(QPdfView::ZoomMode zoomMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#zoomModeChanged

    Parameters
    ----------

    zoomMode : ZoomMode
      Passed on as its number.
    """
    #  void QPdfView::zoomModeChanged(QPdfView::ZoomMode zoomMode)
    self.uglySide.call(
        'ritual_ZN8QPdfView15zoomModeChangedENS_8ZoomModeE', zoomMode.value,
    )

  @overload(float)
  def zoomFactorChanged(self, zoomFactor: float) -> None:
    """
    Calls Qt's 'void QPdfView::zoomFactorChanged(qreal zoomFactor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#zoomFactorChanged

    Parameters
    ----------

    zoomFactor : float
      Passed on as it is.
    """
    #  void QPdfView::zoomFactorChanged(qreal zoomFactor)
    self.uglySide.call('ritual_ZN8QPdfView17zoomFactorChangedEd', zoomFactor)

  @overload(int)
  def pageSpacingChanged(self, pageSpacing: int) -> None:
    """
    Calls Qt's 'void QPdfView::pageSpacingChanged(int pageSpacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#pageSpacingChanged

    Parameters
    ----------

    pageSpacing : int
      Passed on as it is.
    """
    #  void QPdfView::pageSpacingChanged(int pageSpacing)
    self.uglySide.call(
        'ritual_ZN8QPdfView18pageSpacingChangedEi', pageSpacing,
    )

  @overload(QMargins)
  def documentMarginsChanged(self, documentMargins: QMargins) -> None:
    """
    Calls Qt's 'void QPdfView::documentMarginsChanged(QMargins
    documentMargins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfview.html#documentMarginsChanged

    Parameters
    ----------

    documentMargins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QPdfView::documentMarginsChanged(QMargins documentMargins)
    self.uglySide.call(
        'ritual_ZN8QPdfView22documentMarginsChangedE8QMargins',
        self._valueOf(documentMargins, 'QMargins'),
    )

  @overload(QPdfSearchModel)
  @overload(NoneType)
  def searchModelChanged(
      self,
      searchModel: Optional[QPdfSearchModel],
  ) -> None:
    """
    Calls Qt's 'void QPdfView::searchModelChanged(QPdfSearchModel
    *searchModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#searchModelChanged

    Parameters
    ----------

    searchModel : Optional[QPdfSearchModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::searchModelChanged(QPdfSearchModel *searchModel)
    self.uglySide.call(
        'ritual_ZN8QPdfView18searchModelChangedEP15QPdfSearchModel',
        self._addressOf(searchModel),
    )

  @overload(int)
  def currentSearchResultIndexChanged(self, currentResult: int) -> None:
    """
    Calls Qt's 'void QPdfView::currentSearchResultIndexChanged(int
    currentResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfview.html#currentSearchResultIndexChanged

    Parameters
    ----------

    currentResult : int
      Passed on as it is.
    """
    #  void QPdfView::currentSearchResultIndexChanged(int currentResult)
    self.uglySide.call(
        'ritual_ZN8QPdfView31currentSearchResultIndexChangedEi',
        currentResult,
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QPdfView::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN8QPdfView10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QPdfView::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN8QPdfView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QPdfView::scrollContentsBy(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QPdfView::scrollContentsBy(int dx, int dy)
    ritual = 'ritual_ZN8QPdfView16scrollContentsByEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView16scrollContentsByEii'
    self.uglySide.call(ritual, dx, dy)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPdfView::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8QPdfView15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPdfView::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8QPdfView14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QPdfView::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8QPdfView17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QPdfView::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfView::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN8QPdfView10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPdfView10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QPdfViewPrivate]:
    """
    Calls Qt's 'QPdfViewPrivate *QPdfView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfview.html#d_func

    Returns
    -------

    Optional[QPdfViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfViewPrivate *QPdfView::d_func()
    address = self.uglySide.call('ritual_ZN8QPdfView6d_funcEv')
    from . import QPdfViewPrivate
    return QPdfViewPrivate._cuteAt(address)
