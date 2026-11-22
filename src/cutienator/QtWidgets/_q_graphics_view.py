"""
QGraphicsView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtGui import QPainter
from . import QAbstractScrollArea, QGraphicsScene, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QPointF, QRect, QRectF
  from ..QtCore import QSize, QVariant
  from ..QtGui import QBrush, QContextMenuEvent, QDragEnterEvent
  from ..QtGui import QDragLeaveEvent, QDragMoveEvent, QDropEvent
  from ..QtGui import QFocusEvent, QInputMethodEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QPaintEvent, QPainterPath, QPolygon, QPolygonF
  from ..QtGui import QResizeEvent, QShowEvent, QTransform, QWheelEvent
  from . import QGraphicsItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QGraphicsItem = WAIT['QGraphicsItem']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPainterPath = WAIT['QPainterPath']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPolygon = WAIT['QPolygon']
  QPolygonF = WAIT['QPolygonF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']
  QTransform = WAIT['QTransform']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsView(QAbstractScrollArea):
  """
  The cute side of Qt's QGraphicsView: a plain Python object standing in
  front of one C++ QGraphicsView.

  It is built on the cute 'QAbstractScrollArea', as Qt's QGraphicsView is
  built on Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsView that has a ritual and that Python can
  call so far, 81 names in all: 'metaObject', 'tr', 'sizeHint',
  'renderHints', 'setRenderHint', 'setRenderHints', 'alignment',
  'setAlignment', 'transformationAnchor', 'setTransformationAnchor',
  'resizeAnchor', 'setResizeAnchor', 'viewportUpdateMode',
  'setViewportUpdateMode', 'optimizationFlags', 'setOptimizationFlag',
  'setOptimizationFlags', 'dragMode', 'setDragMode',
  'rubberBandSelectionMode', 'setRubberBandSelectionMode', 'rubberBandRect',
  'cacheMode', 'setCacheMode', 'resetCachedContent', 'isInteractive',
  'setInteractive', 'scene', 'setScene', 'sceneRect', 'setSceneRect',
  'transform', 'viewportTransform', 'isTransformed', 'setTransform',
  'resetTransform', 'rotate', 'scale', 'shear', 'translate', 'centerOn',
  'ensureVisible', 'fitInView', 'render', 'items', 'itemAt', 'mapToScene',
  'mapFromScene', 'inputMethodQuery', 'backgroundBrush',
  'setBackgroundBrush', 'foregroundBrush', 'setForegroundBrush',
  'updateScene', 'invalidateScene', 'updateSceneRect', 'setupViewport',
  'event', 'viewportEvent', 'contextMenuEvent', 'dragEnterEvent',
  'dragLeaveEvent', 'dragMoveEvent', 'dropEvent', 'focusInEvent',
  'focusNextPrevChild', 'focusOutEvent', 'keyPressEvent', 'keyReleaseEvent',
  'mouseDoubleClickEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'wheelEvent', 'paintEvent', 'resizeEvent',
  'scrollContentsBy', 'showEvent', 'inputMethodEvent', 'drawBackground',
  'drawForeground'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsView::~QGraphicsView()': the destructor: Python never
    removes a C++ QGraphicsView.

  What has no ritual
  ------------------

  11 of the 119 functions Qt declares: 3 private; 2 takes or gives a type
  that cannot be passed yet; 2 protected; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QGraphicsView is created at the first use, not by
    'QGraphicsView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsView.
  - Qt tells when it has removed the C++ QGraphicsView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGraphicsView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CacheModeFlag(CuteFlags):
    """
    The flags enum 'QGraphicsView::CacheModeFlag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QGraphicsView::CacheMode'.
    """

    CacheNone = 0x0
    CacheBackground = 0x1

  CacheMode = CacheModeFlag

  class DragMode(CuteNum):
    """
    The enum 'QGraphicsView::DragMode' of Qt, with the 3 names Qt gives in
    it.
    """

    NoDrag = Kee[int](0)
    ScrollHandDrag = Kee[int](1)
    RubberBandDrag = Kee[int](2)

  class OptimizationFlag(CuteFlags):
    """
    The flags enum 'QGraphicsView::OptimizationFlag' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QGraphicsView::OptimizationFlags'.
    """

    DontSavePainterState = 0x1
    DontAdjustForAntialiasing = 0x2
    IndirectPainting = 0x4

  OptimizationFlags = OptimizationFlag

  class ViewportAnchor(CuteNum):
    """
    The enum 'QGraphicsView::ViewportAnchor' of Qt, with the 3 names Qt gives
    in it.
    """

    NoAnchor = Kee[int](0)
    AnchorViewCenter = Kee[int](1)
    AnchorUnderMouse = Kee[int](2)

  class ViewportUpdateMode(CuteNum):
    """
    The enum 'QGraphicsView::ViewportUpdateMode' of Qt, with the 5 names Qt
    gives in it.
    """

    FullViewportUpdate = Kee[int](0)
    MinimalViewportUpdate = Kee[int](1)
    SmartViewportUpdate = Kee[int](2)
    NoViewportUpdate = Kee[int](3)
    BoundingRectViewportUpdate = Kee[int](4)

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
    Calls Qt's 'QString QGraphicsView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#tr

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
    #  QString QGraphicsView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QGraphicsView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsView'

  #  A C++ QGraphicsView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsView'

  #  The functions Qt calls itself that QGraphicsView is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'drawItems': (
          'void QGraphicsView::drawItems(QPainter *, int, QGraphicsItem '
          '**, const QStyleOptionGraphicsItem *)',
      ),
  }

  #  The functions Qt calls itself that QGraphicsView is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drawBackground': (
          ('_ZN13QGraphicsView14drawBackgroundEP8QPainterRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'drawForeground': (
          ('_ZN13QGraphicsView14drawForegroundEP8QPainterRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRectF'),
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
    Calls Qt's 'const QMetaObject *QGraphicsView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsView::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QGraphicsView::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGraphicsView::sizeHint() const
    ritual = 'ritual_ZNK13QGraphicsView8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QGraphicsView8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def renderHints(self) -> QPainter.RenderHints:
    """
    Calls Qt's 'QPainter::RenderHints QGraphicsView::renderHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#renderHints

    Returns
    -------

    QPainter.RenderHints
      The value standing for the combination Qt gave back.
    """
    #  QPainter::RenderHints QGraphicsView::renderHints() const
    return QPainter.RenderHints(self.uglySide.call(
        'ritual_ZNK13QGraphicsView11renderHintsEv',
    ))

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGraphicsView::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGraphicsView::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK13QGraphicsView9alignmentEv',
    ))

  def transformationAnchor(self) -> ViewportAnchor:
    """
    Calls Qt's 'ViewportAnchor QGraphicsView::transformationAnchor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#transformationAnchor

    Returns
    -------

    ViewportAnchor
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewportAnchor(number)'
      gives.
    """
    #  ViewportAnchor QGraphicsView::transformationAnchor() const
    return QGraphicsView.ViewportAnchor(self.uglySide.call(
        'ritual_ZNK13QGraphicsView20transformationAnchorEv',
    ))

  def resizeAnchor(self) -> ViewportAnchor:
    """
    Calls Qt's 'ViewportAnchor QGraphicsView::resizeAnchor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#resizeAnchor

    Returns
    -------

    ViewportAnchor
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewportAnchor(number)'
      gives.
    """
    #  ViewportAnchor QGraphicsView::resizeAnchor() const
    return QGraphicsView.ViewportAnchor(self.uglySide.call(
        'ritual_ZNK13QGraphicsView12resizeAnchorEv',
    ))

  def viewportUpdateMode(self) -> ViewportUpdateMode:
    """
    Calls Qt's 'ViewportUpdateMode QGraphicsView::viewportUpdateMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#viewportUpdateMode

    Returns
    -------

    ViewportUpdateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ViewportUpdateMode(number)' gives.
    """
    #  ViewportUpdateMode QGraphicsView::viewportUpdateMode() const
    return QGraphicsView.ViewportUpdateMode(self.uglySide.call(
        'ritual_ZNK13QGraphicsView18viewportUpdateModeEv',
    ))

  def optimizationFlags(self) -> OptimizationFlags:
    """
    Calls Qt's 'OptimizationFlags QGraphicsView::optimizationFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#optimizationFlags

    Returns
    -------

    OptimizationFlags
      The value standing for the combination Qt gave back.
    """
    #  OptimizationFlags QGraphicsView::optimizationFlags() const
    return QGraphicsView.OptimizationFlags(self.uglySide.call(
        'ritual_ZNK13QGraphicsView17optimizationFlagsEv',
    ))

  def dragMode(self) -> DragMode:
    """
    Calls Qt's 'DragMode QGraphicsView::dragMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#dragMode

    Returns
    -------

    DragMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DragMode(number)' gives.
    """
    #  DragMode QGraphicsView::dragMode() const
    return QGraphicsView.DragMode(self.uglySide.call(
        'ritual_ZNK13QGraphicsView8dragModeEv',
    ))

  def rubberBandSelectionMode(self) -> Qt.ItemSelectionMode:
    """
    Calls Qt's 'Qt::ItemSelectionMode
    QGraphicsView::rubberBandSelectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#rubberBandSelectionMode

    Returns
    -------

    Qt.ItemSelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ItemSelectionMode(number)' gives.
    """
    #  Qt::ItemSelectionMode QGraphicsView::rubberBandSelectionMode() const
    return Qt.ItemSelectionMode(self.uglySide.call(
        'ritual_ZNK13QGraphicsView23rubberBandSelectionModeEv',
    ))

  def rubberBandRect(self) -> QRect:
    """
    Calls Qt's 'QRect QGraphicsView::rubberBandRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#rubberBandRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QGraphicsView::rubberBandRect() const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView14rubberBandRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def cacheMode(self) -> CacheMode:
    """
    Calls Qt's 'CacheMode QGraphicsView::cacheMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#cacheMode

    Returns
    -------

    CacheMode
      The value standing for the combination Qt gave back.
    """
    #  CacheMode QGraphicsView::cacheMode() const
    return QGraphicsView.CacheMode(self.uglySide.call(
        'ritual_ZNK13QGraphicsView9cacheModeEv',
    ))

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsView::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#isInteractive
    """
    #  bool QGraphicsView::isInteractive() const
    return self.uglySide.call('ritual_ZNK13QGraphicsView13isInteractiveEv')

  def scene(self) -> Optional[QGraphicsScene]:
    """
    Calls Qt's 'QGraphicsScene *QGraphicsView::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#scene

    Returns
    -------

    Optional[QGraphicsScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsScene *QGraphicsView::scene() const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView5sceneEv')
    return QGraphicsScene._cuteAt(address)

  def sceneRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsView::sceneRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#sceneRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsView::sceneRect() const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView9sceneRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def transform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsView::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsView::transform() const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView9transformEv')
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def viewportTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsView::viewportTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#viewportTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsView::viewportTransform() const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView17viewportTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def isTransformed(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsView::isTransformed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#isTransformed
    """
    #  bool QGraphicsView::isTransformed() const
    return self.uglySide.call('ritual_ZNK13QGraphicsView13isTransformedEv')

  @overload()
  def items(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items() const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView5itemsEv')
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPoint)
  def items(self, pos: QPoint) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items(const QPoint
    &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView5itemsERK6QPoint', self._valueOf(pos),
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(int, int)
  def items(self, x: int, y: int) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items(int x, int y)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items(int x, int y) const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView5itemsEii', x, y)
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QRect)
  @overload(QRect, Qt.ItemSelectionMode)
  def items(
      self,
      rect: QRect,
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items(const QRect
    &rect, Qt::ItemSelectionMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items(const QRect &rect,
    #      Qt::ItemSelectionMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView5itemsERK5QRectN2Qt17ItemSelectionModeE',
        self._valueOf(rect), mode.value,
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(int, int, int, int)
  @overload(int, int, int, int, Qt.ItemSelectionMode)
  def items(
      self,
      x: int,
      y: int,
      w: int,
      h: int,
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items(int x, int y, int
    w, int h, Qt::ItemSelectionMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items(int x, int y, int w, int
    #      h, Qt::ItemSelectionMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView5itemsEiiiiN2Qt17ItemSelectionModeE',
        x, y, w, h, mode.value,
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPolygon)
  @overload(QPolygon, Qt.ItemSelectionMode)
  def items(
      self,
      polygon: QPolygon,
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items(const QPolygon
    &polygon, Qt::ItemSelectionMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Parameters
    ----------

    polygon : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items(const QPolygon &polygon,
    #      Qt::ItemSelectionMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView5itemsERK8QPolygonN2Qt17ItemSelectionMode'
        'E',
        self._valueOf(polygon), mode.value,
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPainterPath)
  @overload(QPainterPath, Qt.ItemSelectionMode)
  def items(
      self,
      path: QPainterPath,
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
  ) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> QGraphicsView::items(const
    QPainterPath &path, Qt::ItemSelectionMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#items

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> QGraphicsView::items(const QPainterPath &path,
    #      Qt::ItemSelectionMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView5itemsERK12QPainterPathN2Qt17ItemSelectio'
        'nModeE',
        self._valueOf(path), mode.value,
    )
    from . import QGraphicsItem
    return QList[QGraphicsItem]._cuteOwning(address)

  @overload(QPoint)
  def itemAt(self, pos: QPoint) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsView::itemAt(const QPoint &pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#itemAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsView::itemAt(const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView6itemAtERK6QPoint', self._valueOf(pos),
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  @overload(int, int)
  def itemAt(self, x: int, y: int) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsView::itemAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#itemAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsView::itemAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK13QGraphicsView6itemAtEii', x, y)
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  @overload(QPoint)
  def mapToScene(self, point: QPoint) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsView::mapToScene(const QPoint &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapToScene

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsView::mapToScene(const QPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView10mapToSceneERK6QPoint',
        self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRect)
  def mapToScene(self, rect: QRect) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsView::mapToScene(const QRect &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapToScene

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsView::mapToScene(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView10mapToSceneERK5QRect',
        self._valueOf(rect),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPolygon)
  def mapToScene(self, polygon: QPolygon) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsView::mapToScene(const QPolygon &polygon)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapToScene

    Parameters
    ----------

    polygon : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsView::mapToScene(const QPolygon &polygon) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView10mapToSceneERK8QPolygon',
        self._valueOf(polygon),
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPainterPath)
  def mapToScene(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsView::mapToScene(const QPainterPath
    &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapToScene

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsView::mapToScene(const QPainterPath &path) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView10mapToSceneERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(int, int)
  def mapToScene(self, x: int, y: int) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsView::mapToScene(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapToScene

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsView::mapToScene(int x, int y) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView10mapToSceneEii', x, y,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int, int, int, int)
  def mapToScene(self, x: int, y: int, w: int, h: int) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsView::mapToScene(int x, int y, int w, int
    h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapToScene

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsView::mapToScene(int x, int y, int w, int h) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView10mapToSceneEiiii', x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPointF)
  def mapFromScene(self, point: QPointF) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsView::mapFromScene(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapFromScene

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsView::mapFromScene(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView12mapFromSceneERK7QPointF',
        self._valueOf(point),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QRectF)
  def mapFromScene(self, rect: QRectF) -> QPolygon:
    """
    Calls Qt's 'QPolygon QGraphicsView::mapFromScene(const QRectF &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapFromScene

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QGraphicsView::mapFromScene(const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView12mapFromSceneERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtGui import QPolygon
    return QPolygon._cuteOwning(address)

  @overload(QPolygonF)
  def mapFromScene(self, polygon: QPolygonF) -> QPolygon:
    """
    Calls Qt's 'QPolygon QGraphicsView::mapFromScene(const QPolygonF
    &polygon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapFromScene

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QGraphicsView::mapFromScene(const QPolygonF &polygon) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView12mapFromSceneERK9QPolygonF',
        self._valueOf(polygon),
    )
    from ..QtGui import QPolygon
    return QPolygon._cuteOwning(address)

  @overload(QPainterPath)
  def mapFromScene(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsView::mapFromScene(const QPainterPath
    &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapFromScene

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsView::mapFromScene(const QPainterPath &path)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView12mapFromSceneERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(float, float)
  def mapFromScene(self, x: float, y: float) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsView::mapFromScene(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapFromScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsView::mapFromScene(qreal x, qreal y) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView12mapFromSceneEdd', x, y,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(float, float, float, float)
  def mapFromScene(self, x: float, y: float, w: float, h: float) -> QPolygon:
    """
    Calls Qt's 'QPolygon QGraphicsView::mapFromScene(qreal x, qreal y, qreal
    w, qreal h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mapFromScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QGraphicsView::mapFromScene(qreal x, qreal y, qreal w, qreal
    #      h) const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView12mapFromSceneEdddd', x, y, w, h,
    )
    from ..QtGui import QPolygon
    return QPolygon._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery
    query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery query)
    #      const
    ritual = (
        'ritual_ZNK13QGraphicsView16inputMethodQueryEN2Qt16InputMethodQuery'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QGraphicsView16inputMethodQueryEN2Qt16InputMetho'
          'dQueryE')
    address = self.uglySide.call(ritual, query.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def backgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QGraphicsView::backgroundBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#backgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QGraphicsView::backgroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView15backgroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def foregroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QGraphicsView::foregroundBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#foregroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QGraphicsView::foregroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK13QGraphicsView15foregroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainter.RenderHint)
  @overload(QPainter.RenderHint, bool)
  def setRenderHint(
      self,
      hint: QPainter.RenderHint,
      enabled: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::setRenderHint(QPainter::RenderHint hint,
    bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setRenderHint

    Parameters
    ----------

    hint : QPainter.RenderHint
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsView::setRenderHint(QPainter::RenderHint hint, bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView13setRenderHintEN8QPainter10RenderHintEb',
        hint.value, enabled,
    )

  @overload(QPainter.RenderHints)
  def setRenderHints(self, hints: QPainter.RenderHints) -> None:
    """
    Calls Qt's 'void QGraphicsView::setRenderHints(QPainter::RenderHints
    hints)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setRenderHints

    Parameters
    ----------

    hints : QPainter.RenderHints
      Passed on as its number.
    """
    #  void QGraphicsView::setRenderHints(QPainter::RenderHints hints)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView14setRenderHintsE6QFlagsIN8QPainter10Rende'
        'rHintEE',
        hints.value,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QGraphicsView::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGraphicsView::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView12setAlignmentE6QFlagsIN2Qt13AlignmentFlag'
        'EE',
        alignment.value,
    )

  @overload(ViewportAnchor)
  def setTransformationAnchor(self, anchor: ViewportAnchor) -> None:
    """
    Calls Qt's 'void QGraphicsView::setTransformationAnchor(ViewportAnchor
    anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setTransformationAnchor

    Parameters
    ----------

    anchor : ViewportAnchor
      Passed on as its number.
    """
    #  void QGraphicsView::setTransformationAnchor(ViewportAnchor anchor)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView23setTransformationAnchorENS_14ViewportAnc'
        'horE',
        anchor.value,
    )

  @overload(ViewportAnchor)
  def setResizeAnchor(self, anchor: ViewportAnchor) -> None:
    """
    Calls Qt's 'void QGraphicsView::setResizeAnchor(ViewportAnchor anchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setResizeAnchor

    Parameters
    ----------

    anchor : ViewportAnchor
      Passed on as its number.
    """
    #  void QGraphicsView::setResizeAnchor(ViewportAnchor anchor)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView15setResizeAnchorENS_14ViewportAnchorE',
        anchor.value,
    )

  @overload(ViewportUpdateMode)
  def setViewportUpdateMode(self, mode: ViewportUpdateMode) -> None:
    """
    Calls Qt's 'void QGraphicsView::setViewportUpdateMode(ViewportUpdateMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setViewportUpdateMode

    Parameters
    ----------

    mode : ViewportUpdateMode
      Passed on as its number.
    """
    #  void QGraphicsView::setViewportUpdateMode(ViewportUpdateMode mode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView21setViewportUpdateModeENS_18ViewportUpdat'
        'eModeE',
        mode.value,
    )

  @overload(OptimizationFlag)
  @overload(OptimizationFlag, bool)
  def setOptimizationFlag(
      self,
      flag: OptimizationFlag,
      enabled: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::setOptimizationFlag(OptimizationFlag
    flag, bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setOptimizationFlag

    Parameters
    ----------

    flag : OptimizationFlag
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsView::setOptimizationFlag(OptimizationFlag flag, bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView19setOptimizationFlagENS_16OptimizationFla'
        'gEb',
        flag.value, enabled,
    )

  @overload(OptimizationFlags)
  def setOptimizationFlags(self, flags: OptimizationFlags) -> None:
    """
    Calls Qt's 'void QGraphicsView::setOptimizationFlags(OptimizationFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setOptimizationFlags

    Parameters
    ----------

    flags : OptimizationFlags
      Passed on as its number.
    """
    #  void QGraphicsView::setOptimizationFlags(OptimizationFlags flags)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView20setOptimizationFlagsE6QFlagsINS_16Optimi'
        'zationFlagEE',
        flags.value,
    )

  @overload(DragMode)
  def setDragMode(self, mode: DragMode) -> None:
    """
    Calls Qt's 'void QGraphicsView::setDragMode(DragMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setDragMode

    Parameters
    ----------

    mode : DragMode
      Passed on as its number.
    """
    #  void QGraphicsView::setDragMode(DragMode mode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView11setDragModeENS_8DragModeE', mode.value,
    )

  @overload(Qt.ItemSelectionMode)
  def setRubberBandSelectionMode(self, mode: Qt.ItemSelectionMode) -> None:
    """
    Calls Qt's 'void
    QGraphicsView::setRubberBandSelectionMode(Qt::ItemSelectionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setRubberBandSelectionMode

    Parameters
    ----------

    mode : Qt.ItemSelectionMode
      Passed on as its number.
    """
    #  void QGraphicsView::setRubberBandSelectionMode(Qt::ItemSelectionMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView26setRubberBandSelectionModeEN2Qt17ItemSel'
        'ectionModeE',
        mode.value,
    )

  @overload(CacheMode)
  def setCacheMode(self, mode: CacheMode) -> None:
    """
    Calls Qt's 'void QGraphicsView::setCacheMode(CacheMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setCacheMode

    Parameters
    ----------

    mode : CacheMode
      Passed on as its number.
    """
    #  void QGraphicsView::setCacheMode(CacheMode mode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView12setCacheModeE6QFlagsINS_13CacheModeFlagE'
        'E',
        mode.value,
    )

  @overload(bool)
  def setInteractive(self, allowed: bool) -> None:
    """
    Calls Qt's 'void QGraphicsView::setInteractive(bool allowed)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setInteractive

    Parameters
    ----------

    allowed : bool
      Passed on as it is.
    """
    #  void QGraphicsView::setInteractive(bool allowed)
    self.uglySide.call('ritual_ZN13QGraphicsView14setInteractiveEb', allowed)

  @overload(QGraphicsScene)
  @overload(NoneType)
  def setScene(self, scene: Optional[QGraphicsScene]) -> None:
    """
    Calls Qt's 'void QGraphicsView::setScene(QGraphicsScene *scene)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setScene

    Parameters
    ----------

    scene : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::setScene(QGraphicsScene *scene)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView8setSceneEP14QGraphicsScene',
        self._addressOf(scene),
    )

  @overload(QRectF)
  def setSceneRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsView::setSceneRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setSceneRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsView::setSceneRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView12setSceneRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setSceneRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsView::setSceneRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setSceneRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsView::setSceneRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView12setSceneRectEdddd', x, y, w, h,
    )

  @overload(QTransform)
  @overload(QTransform, bool)
  def setTransform(self, matrix: QTransform, combine: bool = False) -> None:
    """
    Calls Qt's 'void QGraphicsView::setTransform(const QTransform &matrix,
    bool combine)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setTransform

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    combine : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsView::setTransform(const QTransform &matrix, bool
    #      combine)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView12setTransformERK10QTransformb',
        self._valueOf(matrix), combine,
    )

  @overload(QBrush)
  def setBackgroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QGraphicsView::setBackgroundBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setBackgroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QGraphicsView::setBackgroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView18setBackgroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForegroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QGraphicsView::setForegroundBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#setForegroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QGraphicsView::setForegroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView18setForegroundBrushERK6QBrush',
        self._valueOf(brush),
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
    Notes what was given, for Qt's 'QGraphicsView::QGraphicsView(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#QGraphicsView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsView::QGraphicsView(QWidget *parent)
    self._noteCreation(QGraphicsView, lambda: Rituals.call(
        'ritual_ZN13QGraphicsViewC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QGraphicsScene)
  @overload(QGraphicsScene, QWidget)
  @overload(QGraphicsScene, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      scene: Optional[QGraphicsScene],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsView::QGraphicsView(QGraphicsScene *scene, QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#QGraphicsView

    Parameters
    ----------

    scene : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsView::QGraphicsView(QGraphicsScene *scene, QWidget *parent)
    self._noteCreation(QGraphicsView, lambda: Rituals.call(
        'ritual_ZN13QGraphicsViewC1EP14QGraphicsSceneP7QWidget',
        self._addressOf(scene), self._addressOf(parent),
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

  def resetCachedContent(self) -> None:
    """
    Calls Qt's 'void QGraphicsView::resetCachedContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#resetCachedContent
    """
    #  void QGraphicsView::resetCachedContent()
    self.uglySide.call('ritual_ZN13QGraphicsView18resetCachedContentEv')

  def resetTransform(self) -> None:
    """
    Calls Qt's 'void QGraphicsView::resetTransform()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#resetTransform
    """
    #  void QGraphicsView::resetTransform()
    self.uglySide.call('ritual_ZN13QGraphicsView14resetTransformEv')

  @overload(float)
  def rotate(self, angle: float) -> None:
    """
    Calls Qt's 'void QGraphicsView::rotate(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QGraphicsView::rotate(qreal angle)
    self.uglySide.call('ritual_ZN13QGraphicsView6rotateEd', angle)

  @overload(float, float)
  def scale(self, sx: float, sy: float) -> None:
    """
    Calls Qt's 'void QGraphicsView::scale(qreal sx, qreal sy)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#scale

    Parameters
    ----------

    sx : float
      Passed on as it is.

    sy : float
      Passed on as it is.
    """
    #  void QGraphicsView::scale(qreal sx, qreal sy)
    self.uglySide.call('ritual_ZN13QGraphicsView5scaleEdd', sx, sy)

  @overload(float, float)
  def shear(self, sh: float, sv: float) -> None:
    """
    Calls Qt's 'void QGraphicsView::shear(qreal sh, qreal sv)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#shear

    Parameters
    ----------

    sh : float
      Passed on as it is.

    sv : float
      Passed on as it is.
    """
    #  void QGraphicsView::shear(qreal sh, qreal sv)
    self.uglySide.call('ritual_ZN13QGraphicsView5shearEdd', sh, sv)

  @overload(float, float)
  def translate(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QGraphicsView::translate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#translate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QGraphicsView::translate(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN13QGraphicsView9translateEdd', dx, dy)

  @overload(QPointF)
  def centerOn(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsView::centerOn(const QPointF &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#centerOn

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsView::centerOn(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView8centerOnERK7QPointF', self._valueOf(pos),
    )

  @overload(float, float)
  def centerOn(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QGraphicsView::centerOn(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#centerOn

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QGraphicsView::centerOn(qreal x, qreal y)
    self.uglySide.call('ritual_ZN13QGraphicsView8centerOnEdd', x, y)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def centerOn(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsView::centerOn(const QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#centerOn

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::centerOn(const QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView8centerOnEPK13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QRectF)
  @overload(QRectF, int)
  @overload(QRectF, int, int)
  def ensureVisible(
      self,
      rect: QRectF,
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::ensureVisible(const QRectF &rect, int
    xmargin, int ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#ensureVisible

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QGraphicsView::ensureVisible(const QRectF &rect, int xmargin, int
    #      ymargin)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView13ensureVisibleERK6QRectFii',
        self._valueOf(rect), xmargin, ymargin,
    )

  @overload(float, float, float, float)
  @overload(float, float, float, float, int)
  @overload(float, float, float, float, int, int)
  def ensureVisible(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::ensureVisible(qreal x, qreal y, qreal w,
    qreal h, int xmargin, int ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#ensureVisible

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QGraphicsView::ensureVisible(qreal x, qreal y, qreal w, qreal h,
    #      int xmargin, int ymargin)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView13ensureVisibleEddddii',
        x, y, w, h, xmargin, ymargin,
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, int)
  @overload(NoneType, int)
  @overload(QGraphicsItem, int, int)
  @overload(NoneType, int, int)
  def ensureVisible(
      self,
      item: Optional[QGraphicsItem],
      xmargin: int = 50,
      ymargin: int = 50,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::ensureVisible(const QGraphicsItem *item,
    int xmargin, int ymargin)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#ensureVisible

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xmargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    ymargin : int
      Passed on as it is. May be left out, as in Qt: it is then 50.
    """
    #  void QGraphicsView::ensureVisible(const QGraphicsItem *item, int
    #      xmargin, int ymargin)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView13ensureVisibleEPK13QGraphicsItemii',
        self._addressOf(item, 'QGraphicsItem'), xmargin, ymargin,
    )

  @overload(QRectF)
  @overload(QRectF, Qt.AspectRatioMode)
  def fitInView(
      self,
      rect: QRectF,
      aspectRadioMode: Qt.AspectRatioMode = (
          Qt.AspectRatioMode.IgnoreAspectRatio),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::fitInView(const QRectF &rect,
    Qt::AspectRatioMode aspectRadioMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#fitInView

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    aspectRadioMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.IgnoreAspectRatio.
    """
    #  void QGraphicsView::fitInView(const QRectF &rect, Qt::AspectRatioMode
    #      aspectRadioMode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView9fitInViewERK6QRectFN2Qt15AspectRatioModeE',
        self._valueOf(rect), aspectRadioMode.value,
    )

  @overload(float, float, float, float)
  @overload(float, float, float, float, Qt.AspectRatioMode)
  def fitInView(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      aspectRadioMode: Qt.AspectRatioMode = (
          Qt.AspectRatioMode.IgnoreAspectRatio),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::fitInView(qreal x, qreal y, qreal w,
    qreal h, Qt::AspectRatioMode aspectRadioMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#fitInView

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    aspectRadioMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.IgnoreAspectRatio.
    """
    #  void QGraphicsView::fitInView(qreal x, qreal y, qreal w, qreal h,
    #      Qt::AspectRatioMode aspectRadioMode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView9fitInViewEddddN2Qt15AspectRatioModeE',
        x, y, w, h, aspectRadioMode.value,
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, Qt.AspectRatioMode)
  @overload(NoneType, Qt.AspectRatioMode)
  def fitInView(
      self,
      item: Optional[QGraphicsItem],
      aspectRadioMode: Qt.AspectRatioMode = (
          Qt.AspectRatioMode.IgnoreAspectRatio),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::fitInView(const QGraphicsItem *item,
    Qt::AspectRatioMode aspectRadioMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#fitInView

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aspectRadioMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.IgnoreAspectRatio.
    """
    #  void QGraphicsView::fitInView(const QGraphicsItem *item,
    #      Qt::AspectRatioMode aspectRadioMode)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView9fitInViewEPK13QGraphicsItemN2Qt15AspectRa'
        'tioModeE',
        self._addressOf(item, 'QGraphicsItem'), aspectRadioMode.value,
    )

  @overload(QPainter)
  @overload(NoneType)
  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  @overload(QPainter, QRectF, QRect)
  @overload(NoneType, QRectF, QRect)
  @overload(QPainter, QRectF, QRect, Qt.AspectRatioMode)
  @overload(NoneType, QRectF, QRect, Qt.AspectRatioMode)
  def render(
      self,
      painter: Optional[QPainter],
      target: Optional[QRectF] = None,
      source: Optional[QRect] = None,
      aspectRatioMode: Qt.AspectRatioMode = (
          Qt.AspectRatioMode.KeepAspectRatio),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::render(QPainter *painter, const QRectF
    &target, const QRect &source, Qt::AspectRatioMode aspectRatioMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#render

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    source : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.

    aspectRatioMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.KeepAspectRatio.
    """
    #  void QGraphicsView::render(QPainter *painter, const QRectF &target,
    #      const QRect &source, Qt::AspectRatioMode aspectRatioMode)
    if target is None:
      from ..QtCore import QRectF
      target = QRectF()
    if source is None:
      from ..QtCore import QRect
      source = QRect()
    self.uglySide.call(
        'ritual_ZN13QGraphicsView6renderEP8QPainterRK6QRectFRK5QRectN2Qt15A'
        'spectRatioModeE',
        self._addressOf(painter), self._valueOf(target),
        self._valueOf(source), aspectRatioMode.value,
    )

  @overload(QList[QRectF])
  def updateScene(self, rects: QList[QRectF]) -> None:
    """
    Calls Qt's 'void QGraphicsView::updateScene(const QList<QRectF> &rects)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#updateScene

    Parameters
    ----------

    rects : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGraphicsView::updateScene(const QList<QRectF> &rects)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView11updateSceneERK5QListI6QRectFE',
        self._valueOf(rects),
    )

  @overload()
  @overload(QRectF)
  @overload(QRectF, QGraphicsScene.SceneLayers)
  def invalidateScene(
      self,
      rect: Optional[QRectF] = None,
      layers: QGraphicsScene.SceneLayers = (
          QGraphicsScene.SceneLayers.AllLayers),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::invalidateScene(const QRectF &rect,
    QGraphicsScene::SceneLayers layers)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#invalidateScene

    Parameters
    ----------

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    layers : QGraphicsScene.SceneLayers
      Passed on as its number. May be left out, as in Qt: it is then
      QGraphicsScene.SceneLayers.AllLayers.
    """
    #  void QGraphicsView::invalidateScene(const QRectF &rect,
    #      QGraphicsScene::SceneLayers layers)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self.uglySide.call(
        'ritual_ZN13QGraphicsView15invalidateSceneERK6QRectF6QFlagsIN14QGra'
        'phicsScene10SceneLayerEE',
        self._valueOf(rect), layers.value,
    )

  @overload(QRectF)
  def updateSceneRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsView::updateSceneRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#updateSceneRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsView::updateSceneRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN13QGraphicsView15updateSceneRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setupViewport(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsView::setupViewport(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#setupViewport

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::setupViewport(QWidget *widget)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView13setupViewportEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsView::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsView::event(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN13QGraphicsView5eventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def viewportEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGraphicsView::viewportEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#viewportEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsView::viewportEvent(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN13QGraphicsView13viewportEventEP6QEvent',
        self._addressOf(event),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::contextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::contextMenuEvent(QContextMenuEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView16contextMenuEventEP17QContextMenuEven'
        't',
        self._addressOf(event),
    )

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::dragEnterEvent(QDragEnterEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView14dragEnterEventEP15QDragEnterEvent',
        self._addressOf(event),
    )

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::dragLeaveEvent(QDragLeaveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::dragLeaveEvent(QDragLeaveEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView14dragLeaveEventEP15QDragLeaveEvent',
        self._addressOf(event),
    )

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::dragMoveEvent(QDragMoveEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView13dragMoveEventEP14QDragMoveEvent',
        self._addressOf(event),
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::dropEvent(QDropEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView9dropEventEP10QDropEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::focusInEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QGraphicsView::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QGraphicsView::focusNextPrevChild(bool next)
    return self.uglySide.call(
        'ritual_own_ZN13QGraphicsView18focusNextPrevChildEb', next,
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::focusOutEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView13focusOutEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::keyPressEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView13keyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::keyReleaseEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView15keyReleaseEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::mouseDoubleClickEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView21mouseDoubleClickEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::mousePressEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView15mousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::mouseMoveEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView14mouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::mouseReleaseEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::wheelEvent(QWheelEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView10wheelEventEP11QWheelEvent',
        self._addressOf(event),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::paintEvent(QPaintEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView10paintEventEP11QPaintEvent',
        self._addressOf(event),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::resizeEvent(QResizeEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView11resizeEventEP12QResizeEvent',
        self._addressOf(event),
    )

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QGraphicsView::scrollContentsBy(int dx, int dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QGraphicsView::scrollContentsBy(int dx, int dy)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView16scrollContentsByEii', dx, dy,
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::showEvent(QShowEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView9showEventEP10QShowEvent',
        self._addressOf(event),
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QGraphicsView::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsview.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsView::inputMethodEvent(QInputMethodEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView16inputMethodEventEP17QInputMethodEven'
        't',
        self._addressOf(event),
    )

  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  def drawBackground(
      self,
      painter: Optional[QPainter],
      rect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::drawBackground(QPainter *painter, const
    QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#drawBackground

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsView::drawBackground(QPainter *painter, const QRectF
    #      &rect)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView14drawBackgroundEP8QPainterRK6QRectF',
        self._addressOf(painter), self._valueOf(rect),
    )

  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  def drawForeground(
      self,
      painter: Optional[QPainter],
      rect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsView::drawForeground(QPainter *painter, const
    QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsview.html#drawForeground

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsView::drawForeground(QPainter *painter, const QRectF
    #      &rect)
    self.uglySide.call(
        'ritual_own_ZN13QGraphicsView14drawForegroundEP8QPainterRK6QRectF',
        self._addressOf(painter), self._valueOf(rect),
    )


#  Qt's 'QList<QGraphicsView *>': the list of QGraphicsView, which
#  'QList[QGraphicsView]' gives. It is made here, so that there is one as
#  soon as there can be a QGraphicsView.
QList.createKind(
    QGraphicsView, 'address',
    make='ritual_list_make_QGraphicsView_ptr',
    add='ritual_list_add_QGraphicsView_ptr',
    size='ritual_list_size_QGraphicsView_ptr',
    at='ritual_list_at_QGraphicsView_ptr',
    drop='ritual_list_drop_QGraphicsView_ptr',
)
