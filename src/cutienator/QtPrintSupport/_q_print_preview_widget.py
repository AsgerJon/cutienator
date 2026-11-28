"""
QPrintPreviewWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qprintpreviewwidget.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QPageLayout
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinter = WAIT['QPrinter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPrintPreviewWidget(QWidget):
  """
  The cute side of Qt's QPrintPreviewWidget: a plain Python object standing
  in front of one C++ QPrintPreviewWidget.

  It is built on the cute 'QWidget', as Qt's QPrintPreviewWidget is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPrintPreviewWidget that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr', 'zoomFactor',
  'orientation', 'viewMode', 'zoomMode', 'currentPage', 'pageCount',
  'setVisible', 'print', 'zoomIn', 'zoomOut', 'setZoomFactor',
  'setOrientation', 'setViewMode', 'setZoomMode', 'setCurrentPage',
  'fitToWidth', 'fitInView', 'setLandscapeOrientation',
  'setPortraitOrientation', 'setSinglePageViewMode',
  'setFacingPagesViewMode', 'setAllPagesViewMode', 'updatePreview',
  'paintRequested', 'previewChanged'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPrintPreviewWidget::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPrintPreviewWidget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPrintPreviewWidgetPrivate *QPrintPreviewWidget::d_func()': gives
    'QPrintPreviewWidgetPrivate', which has no cute class yet.
  - Qt's 'const QPrintPreviewWidgetPrivate *QPrintPreviewWidget::d_func()
    const': gives 'QPrintPreviewWidgetPrivate', which has no cute class yet.
  - Qt's 'QPrintPreviewWidget::~QPrintPreviewWidget()': the destructor:
    Python never removes a C++ QPrintPreviewWidget.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPrintPreviewWidget is created at the first use, not by
    'QPrintPreviewWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPrintPreviewWidget.
  - Qt tells when it has removed the C++ QPrintPreviewWidget. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPrintPreviewWidget, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ViewMode(CuteNum):
    """
    The enum 'QPrintPreviewWidget::ViewMode' of Qt, with the 3 names Qt gives
    in it.
    """

    SinglePageView = Kee[int](0)
    FacingPagesView = Kee[int](1)
    AllPagesView = Kee[int](2)

  class ZoomMode(CuteNum):
    """
    The enum 'QPrintPreviewWidget::ZoomMode' of Qt, with the 3 names Qt gives
    in it.
    """

    CustomZoom = Kee[int](0)
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
    Calls Qt's 'QString QPrintPreviewWidget::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#tr

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
    #  QString QPrintPreviewWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QPrintPreviewWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrintPreviewWidget'

  #  A C++ QPrintPreviewWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPrintPreviewWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPrintPreviewWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPrintPreviewWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QPrintPreviewWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'qreal QPrintPreviewWidget::zoomFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#zoomFactor
    """
    #  qreal QPrintPreviewWidget::zoomFactor() const
    return self.uglySide.call(
        'ritual_ZNK19QPrintPreviewWidget10zoomFactorEv',
    )

  def orientation(self) -> QPageLayout.Orientation:
    """
    Calls Qt's 'QPageLayout::Orientation QPrintPreviewWidget::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#orientation

    Returns
    -------

    QPageLayout.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPageLayout.Orientation(number)' gives.
    """
    #  QPageLayout::Orientation QPrintPreviewWidget::orientation() const
    return QPageLayout.Orientation(self.uglySide.call(
        'ritual_ZNK19QPrintPreviewWidget11orientationEv',
    ))

  def viewMode(self) -> ViewMode:
    """
    Calls Qt's 'ViewMode QPrintPreviewWidget::viewMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#viewMode

    Returns
    -------

    ViewMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewMode(number)' gives.
    """
    #  ViewMode QPrintPreviewWidget::viewMode() const
    return QPrintPreviewWidget.ViewMode(self.uglySide.call(
        'ritual_ZNK19QPrintPreviewWidget8viewModeEv',
    ))

  def zoomMode(self) -> ZoomMode:
    """
    Calls Qt's 'ZoomMode QPrintPreviewWidget::zoomMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#zoomMode

    Returns
    -------

    ZoomMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ZoomMode(number)' gives.
    """
    #  ZoomMode QPrintPreviewWidget::zoomMode() const
    return QPrintPreviewWidget.ZoomMode(self.uglySide.call(
        'ritual_ZNK19QPrintPreviewWidget8zoomModeEv',
    ))

  def currentPage(self) -> int:
    """
    Calls Qt's 'int QPrintPreviewWidget::currentPage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#currentPage
    """
    #  int QPrintPreviewWidget::currentPage() const
    return self.uglySide.call(
        'ritual_ZNK19QPrintPreviewWidget11currentPageEv',
    )

  def pageCount(self) -> int:
    """
    Calls Qt's 'int QPrintPreviewWidget::pageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#pageCount
    """
    #  int QPrintPreviewWidget::pageCount() const
    return self.uglySide.call('ritual_ZNK19QPrintPreviewWidget9pageCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPrintPreviewWidget::setVisible(bool visible)
    ritual = 'ritual_ZN19QPrintPreviewWidget10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPrintPreviewWidget10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(float)
  def setZoomFactor(self, zoomFactor: float) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setZoomFactor(qreal zoomFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setZoomFactor

    Parameters
    ----------

    zoomFactor : float
      Passed on as it is.
    """
    #  void QPrintPreviewWidget::setZoomFactor(qreal zoomFactor)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget13setZoomFactorEd', zoomFactor,
    )

  @overload(QPageLayout.Orientation)
  def setOrientation(self, orientation: QPageLayout.Orientation) -> None:
    """
    Calls Qt's 'void
    QPrintPreviewWidget::setOrientation(QPageLayout::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setOrientation

    Parameters
    ----------

    orientation : QPageLayout.Orientation
      Passed on as its number.
    """
    #  void QPrintPreviewWidget::setOrientation(QPageLayout::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget14setOrientationEN11QPageLayout11Ori'
        'entationE',
        orientation.value,
    )

  @overload(ViewMode)
  def setViewMode(self, viewMode: ViewMode) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setViewMode(ViewMode viewMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setViewMode

    Parameters
    ----------

    viewMode : ViewMode
      Passed on as its number.
    """
    #  void QPrintPreviewWidget::setViewMode(ViewMode viewMode)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget11setViewModeENS_8ViewModeE',
        viewMode.value,
    )

  @overload(ZoomMode)
  def setZoomMode(self, zoomMode: ZoomMode) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setZoomMode(ZoomMode zoomMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setZoomMode

    Parameters
    ----------

    zoomMode : ZoomMode
      Passed on as its number.
    """
    #  void QPrintPreviewWidget::setZoomMode(ZoomMode zoomMode)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget11setZoomModeENS_8ZoomModeE',
        zoomMode.value,
    )

  @overload(int)
  def setCurrentPage(self, pageNumber: int) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setCurrentPage(int pageNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setCurrentPage

    Parameters
    ----------

    pageNumber : int
      Passed on as it is.
    """
    #  void QPrintPreviewWidget::setCurrentPage(int pageNumber)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget14setCurrentPageEi', pageNumber,
    )

  def setLandscapeOrientation(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setLandscapeOrientation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setLandscapeOrientation
    """
    #  void QPrintPreviewWidget::setLandscapeOrientation()
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget23setLandscapeOrientationEv',
    )

  def setPortraitOrientation(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setPortraitOrientation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setPortraitOrientation
    """
    #  void QPrintPreviewWidget::setPortraitOrientation()
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget22setPortraitOrientationEv',
    )

  def setSinglePageViewMode(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setSinglePageViewMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setSinglePageViewMode
    """
    #  void QPrintPreviewWidget::setSinglePageViewMode()
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget21setSinglePageViewModeEv',
    )

  def setFacingPagesViewMode(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setFacingPagesViewMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setFacingPagesViewMode
    """
    #  void QPrintPreviewWidget::setFacingPagesViewMode()
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget22setFacingPagesViewModeEv',
    )

  def setAllPagesViewMode(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::setAllPagesViewMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#setAllPagesViewMode
    """
    #  void QPrintPreviewWidget::setAllPagesViewMode()
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget19setAllPagesViewModeEv',
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

  @overload(QPrinter)
  @overload(NoneType)
  @overload(QPrinter, QWidget)
  @overload(QPrinter, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QPrinter, QWidget, Qt.WindowFlags)
  @overload(QPrinter, NoneType, Qt.WindowFlags)
  @overload(NoneType, QWidget, Qt.WindowFlags)
  @overload(NoneType, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      printer: Optional[QPrinter],
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPrintPreviewWidget::QPrintPreviewWidget(QPrinter *printer, QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#QPrintPreviewWidget

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QPrintPreviewWidget::QPrintPreviewWidget(QPrinter *printer, QWidget
    #      *parent, Qt::WindowFlags flags)
    self._noteCreation(QPrintPreviewWidget, lambda: Rituals.call(
        'ritual_ZN19QPrintPreviewWidgetC1EP8QPrinterP7QWidget6QFlagsIN2Qt10'
        'WindowTypeEE',
        self._addressOf(printer), self._addressOf(parent), flags.value,
    ))

  @overload()
  @overload(QWidget)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPrintPreviewWidget::QPrintPreviewWidget(QWidget *parent,
    Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#QPrintPreviewWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QPrintPreviewWidget::QPrintPreviewWidget(QWidget *parent,
    #      Qt::WindowFlags flags)
    self._noteCreation(QPrintPreviewWidget, lambda: Rituals.call(
        'ritual_ZN19QPrintPreviewWidgetC1EP7QWidget6QFlagsIN2Qt10WindowType'
        'EE',
        self._addressOf(parent), flags.value,
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

  def print(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::print()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#print
    """
    #  void QPrintPreviewWidget::print()
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget5printEv')

  @overload()
  @overload(float)
  def zoomIn(self, zoom: float = 1.1) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::zoomIn(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#zoomIn

    Parameters
    ----------

    zoom : float
      Passed on as it is. May be left out, as in Qt: it is then 1.1.
    """
    #  void QPrintPreviewWidget::zoomIn(qreal zoom)
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget6zoomInEd', zoom)

  @overload()
  @overload(float)
  def zoomOut(self, zoom: float = 1.1) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::zoomOut(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#zoomOut

    Parameters
    ----------

    zoom : float
      Passed on as it is. May be left out, as in Qt: it is then 1.1.
    """
    #  void QPrintPreviewWidget::zoomOut(qreal zoom)
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget7zoomOutEd', zoom)

  def fitToWidth(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::fitToWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#fitToWidth
    """
    #  void QPrintPreviewWidget::fitToWidth()
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget10fitToWidthEv')

  def fitInView(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::fitInView()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewwidget.html#fitInView
    """
    #  void QPrintPreviewWidget::fitInView()
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget9fitInViewEv')

  def updatePreview(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::updatePreview()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#updatePreview
    """
    #  void QPrintPreviewWidget::updatePreview()
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget13updatePreviewEv')

  @overload(QPrinter)
  @overload(NoneType)
  def paintRequested(self, printer: Optional[QPrinter]) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::paintRequested(QPrinter *printer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#paintRequested

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPrintPreviewWidget::paintRequested(QPrinter *printer)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewWidget14paintRequestedEP8QPrinter',
        self._addressOf(printer),
    )

  def previewChanged(self) -> None:
    """
    Calls Qt's 'void QPrintPreviewWidget::previewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewwidget.html#previewChanged
    """
    #  void QPrintPreviewWidget::previewChanged()
    self.uglySide.call('ritual_ZN19QPrintPreviewWidget14previewChangedEv')
