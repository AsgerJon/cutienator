"""
QGraphicsScene binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsscene.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QGraphicsSceneItemIndexMethod, QGraphicsSceneSceneLayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLineF, QMetaObject, QPointF, QRectF, QVariant
  from ..QtGui import QBrush, QFont, QPainter, QPainterPath, QPalette, QPen
  from ..QtGui import QPixmap, QPolygonF, QTransform
  from . import QGraphicsEllipseItem, QGraphicsItem, QGraphicsItemGroup
  from . import QGraphicsLineItem, QGraphicsPathItem, QGraphicsPixmapItem
  from . import QGraphicsPolygonItem, QGraphicsProxyWidget, QGraphicsRectItem
  from . import QGraphicsSimpleTextItem, QGraphicsTextItem, QGraphicsWidget
  from . import QStyle, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsItemGroup = WAIT['QGraphicsItemGroup']
  QGraphicsWidget = WAIT['QGraphicsWidget']
  QLineF = WAIT['QLineF']
  QPainter = WAIT['QPainter']
  QPainterPath = WAIT['QPainterPath']
  QPalette = WAIT['QPalette']
  QPen = WAIT['QPen']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QPolygonF = WAIT['QPolygonF']
  QRectF = WAIT['QRectF']
  QStyle = WAIT['QStyle']
  QTransform = WAIT['QTransform']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsScene(QObject):
  """
  The cute side of Qt's QGraphicsScene: a plain Python object standing in
  front of one C++ QGraphicsScene.

  It is built on the cute 'QObject', as Qt's QGraphicsScene is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsScene that has a ritual and that Python can
  call so far, 61 names in all: 'metaObject', 'tr', 'sceneRect', 'width',
  'height', 'setSceneRect', 'render', 'itemIndexMethod',
  'setItemIndexMethod', 'bspTreeDepth', 'setBspTreeDepth',
  'itemsBoundingRect', 'itemAt', 'selectionArea', 'setSelectionArea',
  'destroyItemGroup', 'addItem', 'addEllipse', 'addLine', 'addPath',
  'addPixmap', 'addPolygon', 'addRect', 'addText', 'addSimpleText',
  'addWidget', 'removeItem', 'focusItem', 'setFocusItem', 'hasFocus',
  'setFocus', 'clearFocus', 'setStickyFocus', 'stickyFocus',
  'mouseGrabberItem', 'backgroundBrush', 'setBackgroundBrush',
  'foregroundBrush', 'setForegroundBrush', 'inputMethodQuery', 'update',
  'invalidate', 'style', 'setStyle', 'font', 'setFont', 'palette',
  'setPalette', 'isActive', 'activePanel', 'setActivePanel', 'activeWindow',
  'setActiveWindow', 'sendEvent', 'minimumRenderSize',
  'setMinimumRenderSize', 'focusOnTouch', 'setFocusOnTouch', 'advance',
  'clearSelection', 'clear'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsScene::~QGraphicsScene()': the destructor: Python never
    removes a C++ QGraphicsScene.

  What has no ritual
  ------------------

  44 of the 117 functions Qt declares: 22 protected; 12 takes or gives a type
  that cannot be passed yet; 4 a signal; 3 private; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QGraphicsScene is created at the first use, not by
    'QGraphicsScene(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsScene.
  - Qt tells when it has removed the C++ QGraphicsScene. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGraphicsScene, and the names Qt has for the
  #  combinations of its flags enums.
  ItemIndexMethod = QGraphicsSceneItemIndexMethod
  SceneLayer = QGraphicsSceneSceneLayer
  SceneLayers = QGraphicsSceneSceneLayer

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
    Calls Qt's 'QString QGraphicsScene::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#tr

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
    #  QString QGraphicsScene::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QGraphicsScene2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsScene'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsScene::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsScene::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sceneRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsScene::sceneRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#sceneRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsScene::sceneRect() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene9sceneRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsScene::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#width
    """
    #  qreal QGraphicsScene::width() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsScene::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#height
    """
    #  qreal QGraphicsScene::height() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene6heightEv')

  def itemIndexMethod(self) -> ItemIndexMethod:
    """
    Calls Qt's 'ItemIndexMethod QGraphicsScene::itemIndexMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#itemIndexMethod

    Returns
    -------

    ItemIndexMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ItemIndexMethod(number)'
      gives.
    """
    #  ItemIndexMethod QGraphicsScene::itemIndexMethod() const
    return QGraphicsScene.ItemIndexMethod(self.uglySide.call(
        'ritual_ZNK14QGraphicsScene15itemIndexMethodEv',
    ))

  def bspTreeDepth(self) -> int:
    """
    Calls Qt's 'int QGraphicsScene::bspTreeDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#bspTreeDepth
    """
    #  int QGraphicsScene::bspTreeDepth() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene12bspTreeDepthEv')

  def itemsBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsScene::itemsBoundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#itemsBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsScene::itemsBoundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene17itemsBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPointF, QTransform)
  def itemAt(
      self,
      pos: QPointF,
      deviceTransform: QTransform,
  ) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsScene::itemAt(const QPointF &pos,
    const QTransform &deviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#itemAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    deviceTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsScene::itemAt(const QPointF &pos, const
    #      QTransform &deviceTransform) const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene6itemAtERK7QPointFRK10QTransform',
        self._valueOf(pos), self._valueOf(deviceTransform),
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  @overload(float, float, QTransform)
  def itemAt(
      self,
      x: float,
      y: float,
      deviceTransform: QTransform,
  ) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsScene::itemAt(qreal x, qreal y, const
    QTransform &deviceTransform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#itemAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    deviceTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsScene::itemAt(qreal x, qreal y, const
    #      QTransform &deviceTransform) const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene6itemAtEddRK10QTransform',
        x, y, self._valueOf(deviceTransform),
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def selectionArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsScene::selectionArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#selectionArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsScene::selectionArea() const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene13selectionAreaEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def focusItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsScene::focusItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#focusItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsScene::focusItem() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene9focusItemEv')
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def hasFocus(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsScene::hasFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#hasFocus
    """
    #  bool QGraphicsScene::hasFocus() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene8hasFocusEv')

  def stickyFocus(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsScene::stickyFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#stickyFocus
    """
    #  bool QGraphicsScene::stickyFocus() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene11stickyFocusEv')

  def mouseGrabberItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsScene::mouseGrabberItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#mouseGrabberItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsScene::mouseGrabberItem() const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene16mouseGrabberItemEv',
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def backgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QGraphicsScene::backgroundBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#backgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QGraphicsScene::backgroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene15backgroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def foregroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QGraphicsScene::foregroundBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#foregroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QGraphicsScene::foregroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene15foregroundBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QGraphicsScene::inputMethodQuery(Qt::InputMethodQuery query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsScene::inputMethodQuery(Qt::InputMethodQuery query)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene16inputMethodQueryEN2Qt16InputMethodQuer'
        'yE',
        query.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QGraphicsScene::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QGraphicsScene::style() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene5styleEv')
    from . import QStyle
    return QStyle._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphicsScene::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphicsScene::font() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def palette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QGraphicsScene::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QGraphicsScene::palette() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene7paletteEv')
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsScene::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#isActive
    """
    #  bool QGraphicsScene::isActive() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene8isActiveEv')

  def activePanel(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsScene::activePanel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#activePanel

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsScene::activePanel() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScene11activePanelEv')
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def activeWindow(self) -> Optional[QGraphicsWidget]:
    """
    Calls Qt's 'QGraphicsWidget *QGraphicsScene::activeWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#activeWindow

    Returns
    -------

    Optional[QGraphicsWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsWidget *QGraphicsScene::activeWindow() const
    address = self.uglySide.call(
        'ritual_ZNK14QGraphicsScene12activeWindowEv',
    )
    from . import QGraphicsWidget
    return QGraphicsWidget._cuteAt(address)

  def minimumRenderSize(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsScene::minimumRenderSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#minimumRenderSize
    """
    #  qreal QGraphicsScene::minimumRenderSize() const
    return self.uglySide.call(
        'ritual_ZNK14QGraphicsScene17minimumRenderSizeEv',
    )

  def focusOnTouch(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsScene::focusOnTouch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#focusOnTouch
    """
    #  bool QGraphicsScene::focusOnTouch() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScene12focusOnTouchEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setSceneRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setSceneRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setSceneRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsScene::setSceneRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene12setSceneRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setSceneRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setSceneRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setSceneRect

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
    #  void QGraphicsScene::setSceneRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene12setSceneRectEdddd', x, y, w, h,
    )

  @overload(ItemIndexMethod)
  def setItemIndexMethod(self, method: ItemIndexMethod) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setItemIndexMethod(ItemIndexMethod
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setItemIndexMethod

    Parameters
    ----------

    method : ItemIndexMethod
      Passed on as its number.
    """
    #  void QGraphicsScene::setItemIndexMethod(ItemIndexMethod method)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene18setItemIndexMethodENS_15ItemIndexMethod'
        'E',
        method.value,
    )

  @overload(int)
  def setBspTreeDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setBspTreeDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setBspTreeDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QGraphicsScene::setBspTreeDepth(int depth)
    self.uglySide.call('ritual_ZN14QGraphicsScene15setBspTreeDepthEi', depth)

  @overload(QPainterPath, QTransform)
  def setSelectionArea(
      self,
      path: QPainterPath,
      deviceTransform: QTransform,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setSelectionArea(const QPainterPath
    &path, const QTransform &deviceTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setSelectionArea

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    deviceTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QGraphicsScene::setSelectionArea(const QPainterPath &path, const
    #      QTransform &deviceTransform)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene16setSelectionAreaERK12QPainterPathRK10QT'
        'ransform',
        self._valueOf(path), self._valueOf(deviceTransform),
    )

  @overload(QPainterPath)
  @overload(QPainterPath, Qt.ItemSelectionOperation)
  @overload(QPainterPath, Qt.ItemSelectionOperation, Qt.ItemSelectionMode)
  @overload(
      QPainterPath, Qt.ItemSelectionOperation, Qt.ItemSelectionMode,
      QTransform,
  )
  def setSelectionArea(
      self,
      path: QPainterPath,
      selectionOperation: Qt.ItemSelectionOperation = (
          Qt.ItemSelectionOperation.ReplaceSelection),
      mode: Qt.ItemSelectionMode = Qt.ItemSelectionMode.IntersectsItemShape,
      deviceTransform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setSelectionArea(const QPainterPath
    &path, Qt::ItemSelectionOperation selectionOperation,
    Qt::ItemSelectionMode mode, const QTransform &deviceTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setSelectionArea

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    selectionOperation : Qt.ItemSelectionOperation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionOperation.ReplaceSelection.

    mode : Qt.ItemSelectionMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ItemSelectionMode.IntersectsItemShape.

    deviceTransform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.
    """
    #  void QGraphicsScene::setSelectionArea(const QPainterPath &path,
    #      Qt::ItemSelectionOperation selectionOperation,
    #      Qt::ItemSelectionMode mode, const QTransform &deviceTransform)
    if deviceTransform is None:
      from ..QtGui import QTransform
      deviceTransform = QTransform()
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene16setSelectionAreaERK12QPainterPathN2Qt22'
        'ItemSelectionOperationENS3_17ItemSelectionModeERK10QTransform',
        self._valueOf(path), selectionOperation.value, mode.value,
        self._valueOf(deviceTransform),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, Qt.FocusReason)
  @overload(NoneType, Qt.FocusReason)
  def setFocusItem(
      self,
      item: Optional[QGraphicsItem],
      focusReason: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setFocusItem(QGraphicsItem *item,
    Qt::FocusReason focusReason)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setFocusItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    focusReason : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  void QGraphicsScene::setFocusItem(QGraphicsItem *item, Qt::FocusReason
    #      focusReason)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene12setFocusItemEP13QGraphicsItemN2Qt11Focu'
        'sReasonE',
        self._addressOf(item), focusReason.value,
    )

  @overload()
  @overload(Qt.FocusReason)
  def setFocus(
      self,
      focusReason: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setFocus(Qt::FocusReason focusReason)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setFocus

    Parameters
    ----------

    focusReason : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  void QGraphicsScene::setFocus(Qt::FocusReason focusReason)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene8setFocusEN2Qt11FocusReasonE',
        focusReason.value,
    )

  @overload(bool)
  def setStickyFocus(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setStickyFocus(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setStickyFocus

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsScene::setStickyFocus(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene14setStickyFocusEb', enabled,
    )

  @overload(QBrush)
  def setBackgroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setBackgroundBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setBackgroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QGraphicsScene::setBackgroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene18setBackgroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForegroundBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setForegroundBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setForegroundBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QGraphicsScene::setForegroundBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene18setForegroundBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QStyle)
  @overload(NoneType)
  def setStyle(self, style: Optional[QStyle]) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setStyle(QStyle *style)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setStyle

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScene::setStyle(QStyle *style)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene8setStyleEP6QStyle',
        self._addressOf(style),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsScene::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QPalette)
  def setPalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setPalette(const QPalette &palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGraphicsScene::setPalette(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene10setPaletteERK8QPalette',
        self._valueOf(palette),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def setActivePanel(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setActivePanel(QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#setActivePanel

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScene::setActivePanel(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene14setActivePanelEP13QGraphicsItem',
        self._addressOf(item),
    )

  @overload(QGraphicsWidget)
  @overload(NoneType)
  def setActiveWindow(self, widget: Optional[QGraphicsWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setActiveWindow(QGraphicsWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setActiveWindow

    Parameters
    ----------

    widget : Optional[QGraphicsWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScene::setActiveWindow(QGraphicsWidget *widget)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene15setActiveWindowEP15QGraphicsWidget',
        self._addressOf(widget),
    )

  @overload(float)
  def setMinimumRenderSize(self, minSize: float) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setMinimumRenderSize(qreal minSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setMinimumRenderSize

    Parameters
    ----------

    minSize : float
      Passed on as it is.
    """
    #  void QGraphicsScene::setMinimumRenderSize(qreal minSize)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene20setMinimumRenderSizeEd', minSize,
    )

  @overload(bool)
  def setFocusOnTouch(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsScene::setFocusOnTouch(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#setFocusOnTouch

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsScene::setFocusOnTouch(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene15setFocusOnTouchEb', enabled,
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
    Notes what was given, for Qt's 'QGraphicsScene::QGraphicsScene(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#QGraphicsScene

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsScene::QGraphicsScene(QObject *parent)
    self._noteCreation(QGraphicsScene, lambda: Rituals.call(
        'ritual_ZN14QGraphicsSceneC1EP7QObject', self._addressOf(parent),
    ))

  @overload(QRectF)
  @overload(QRectF, QObject)
  @overload(QRectF, NoneType)
  def __init__(
      self,
      sceneRect: QRectF,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGraphicsScene::QGraphicsScene(const
    QRectF &sceneRect, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#QGraphicsScene

    Parameters
    ----------

    sceneRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsScene::QGraphicsScene(const QRectF &sceneRect, QObject
    #      *parent)
    self._noteCreation(QGraphicsScene, lambda: Rituals.call(
        'ritual_ZN14QGraphicsSceneC1ERK6QRectFP7QObject',
        self._valueOf(sceneRect), self._addressOf(parent),
    ))

  @overload(float, float, float, float)
  @overload(float, float, float, float, QObject)
  @overload(float, float, float, float, NoneType)
  def __init__(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGraphicsScene::QGraphicsScene(qreal x,
    qreal y, qreal width, qreal height, QObject *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#QGraphicsScene

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsScene::QGraphicsScene(qreal x, qreal y, qreal width, qreal
    #      height, QObject *parent)
    self._noteCreation(QGraphicsScene, lambda: Rituals.call(
        'ritual_ZN14QGraphicsSceneC1EddddP7QObject',
        x, y, width, height, self._addressOf(parent),
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

  @overload(QPainter)
  @overload(NoneType)
  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  @overload(QPainter, QRectF, QRectF)
  @overload(NoneType, QRectF, QRectF)
  @overload(QPainter, QRectF, QRectF, Qt.AspectRatioMode)
  @overload(NoneType, QRectF, QRectF, Qt.AspectRatioMode)
  def render(
      self,
      painter: Optional[QPainter],
      target: Optional[QRectF] = None,
      source: Optional[QRectF] = None,
      aspectRatioMode: Qt.AspectRatioMode = (
          Qt.AspectRatioMode.KeepAspectRatio),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::render(QPainter *painter, const QRectF
    &target, const QRectF &source, Qt::AspectRatioMode aspectRatioMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#render

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    source : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    aspectRatioMode : Qt.AspectRatioMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.AspectRatioMode.KeepAspectRatio.
    """
    #  void QGraphicsScene::render(QPainter *painter, const QRectF &target,
    #      const QRectF &source, Qt::AspectRatioMode aspectRatioMode)
    if target is None:
      from ..QtCore import QRectF
      target = QRectF()
    if source is None:
      from ..QtCore import QRectF
      source = QRectF()
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene6renderEP8QPainterRK6QRectFS4_N2Qt15Aspec'
        'tRatioModeE',
        self._addressOf(painter), self._valueOf(target),
        self._valueOf(source), aspectRatioMode.value,
    )

  @overload(QGraphicsItemGroup)
  @overload(NoneType)
  def destroyItemGroup(self, group: Optional[QGraphicsItemGroup]) -> None:
    """
    Calls Qt's 'void QGraphicsScene::destroyItemGroup(QGraphicsItemGroup
    *group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscene.html#destroyItemGroup

    Parameters
    ----------

    group : Optional[QGraphicsItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScene::destroyItemGroup(QGraphicsItemGroup *group)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene16destroyItemGroupEP18QGraphicsItemGroup',
        self._addressOf(group),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsScene::addItem(QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScene::addItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addItemEP13QGraphicsItem',
        self._addressOf(item),
    )

  @overload(QRectF)
  @overload(QRectF, QPen)
  @overload(QRectF, QPen, QBrush)
  def addEllipse(
      self,
      rect: QRectF,
      pen: Optional[QPen] = None,
      brush: Optional[QBrush] = None,
  ) -> Optional[QGraphicsEllipseItem]:
    """
    Calls Qt's 'QGraphicsEllipseItem *QGraphicsScene::addEllipse(const QRectF
    &rect, const QPen &pen, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addEllipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    brush : Optional[QBrush]
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own. May be left out, as in Qt: a new 'QBrush()' is then passed on.

    Returns
    -------

    Optional[QGraphicsEllipseItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEllipseItem *QGraphicsScene::addEllipse(const QRectF &rect,
    #      const QPen &pen, const QBrush &brush)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    if brush is None:
      from ..QtGui import QBrush
      brush = QBrush()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene10addEllipseERK6QRectFRK4QPenRK6QBrush',
        self._valueOf(rect), self._valueOf(pen), self._valueOf(brush),
    )
    from . import QGraphicsEllipseItem
    return QGraphicsEllipseItem._cuteAt(address)

  @overload(float, float, float, float)
  @overload(float, float, float, float, QPen)
  @overload(float, float, float, float, QPen, QBrush)
  def addEllipse(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      pen: Optional[QPen] = None,
      brush: Optional[QBrush] = None,
  ) -> Optional[QGraphicsEllipseItem]:
    """
    Calls Qt's 'QGraphicsEllipseItem *QGraphicsScene::addEllipse(qreal x,
    qreal y, qreal w, qreal h, const QPen &pen, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addEllipse

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

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    brush : Optional[QBrush]
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own. May be left out, as in Qt: a new 'QBrush()' is then passed on.

    Returns
    -------

    Optional[QGraphicsEllipseItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEllipseItem *QGraphicsScene::addEllipse(qreal x, qreal y,
    #      qreal w, qreal h, const QPen &pen, const QBrush &brush)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    if brush is None:
      from ..QtGui import QBrush
      brush = QBrush()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene10addEllipseEddddRK4QPenRK6QBrush',
        x, y, w, h, self._valueOf(pen), self._valueOf(brush),
    )
    from . import QGraphicsEllipseItem
    return QGraphicsEllipseItem._cuteAt(address)

  @overload(QLineF)
  @overload(QLineF, QPen)
  def addLine(
      self,
      line: QLineF,
      pen: Optional[QPen] = None,
  ) -> Optional[QGraphicsLineItem]:
    """
    Calls Qt's 'QGraphicsLineItem *QGraphicsScene::addLine(const QLineF
    &line, const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addLine

    Parameters
    ----------

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    Returns
    -------

    Optional[QGraphicsLineItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLineItem *QGraphicsScene::addLine(const QLineF &line, const
    #      QPen &pen)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addLineERK6QLineFRK4QPen',
        self._valueOf(line), self._valueOf(pen),
    )
    from . import QGraphicsLineItem
    return QGraphicsLineItem._cuteAt(address)

  @overload(float, float, float, float)
  @overload(float, float, float, float, QPen)
  def addLine(
      self,
      x1: float,
      y1: float,
      x2: float,
      y2: float,
      pen: Optional[QPen] = None,
  ) -> Optional[QGraphicsLineItem]:
    """
    Calls Qt's 'QGraphicsLineItem *QGraphicsScene::addLine(qreal x1, qreal
    y1, qreal x2, qreal y2, const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addLine

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    Returns
    -------

    Optional[QGraphicsLineItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLineItem *QGraphicsScene::addLine(qreal x1, qreal y1, qreal
    #      x2, qreal y2, const QPen &pen)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addLineEddddRK4QPen',
        x1, y1, x2, y2, self._valueOf(pen),
    )
    from . import QGraphicsLineItem
    return QGraphicsLineItem._cuteAt(address)

  @overload(QPainterPath)
  @overload(QPainterPath, QPen)
  @overload(QPainterPath, QPen, QBrush)
  def addPath(
      self,
      path: QPainterPath,
      pen: Optional[QPen] = None,
      brush: Optional[QBrush] = None,
  ) -> Optional[QGraphicsPathItem]:
    """
    Calls Qt's 'QGraphicsPathItem *QGraphicsScene::addPath(const QPainterPath
    &path, const QPen &pen, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    brush : Optional[QBrush]
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own. May be left out, as in Qt: a new 'QBrush()' is then passed on.

    Returns
    -------

    Optional[QGraphicsPathItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsPathItem *QGraphicsScene::addPath(const QPainterPath &path,
    #      const QPen &pen, const QBrush &brush)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    if brush is None:
      from ..QtGui import QBrush
      brush = QBrush()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addPathERK12QPainterPathRK4QPenRK6QBrush',
        self._valueOf(path), self._valueOf(pen), self._valueOf(brush),
    )
    from . import QGraphicsPathItem
    return QGraphicsPathItem._cuteAt(address)

  @overload(QPixmap)
  def addPixmap(self, pixmap: QPixmap) -> Optional[QGraphicsPixmapItem]:
    """
    Calls Qt's 'QGraphicsPixmapItem *QGraphicsScene::addPixmap(const QPixmap
    &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    Optional[QGraphicsPixmapItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsPixmapItem *QGraphicsScene::addPixmap(const QPixmap &pixmap)
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene9addPixmapERK7QPixmap',
        self._valueOf(pixmap),
    )
    from . import QGraphicsPixmapItem
    return QGraphicsPixmapItem._cuteAt(address)

  @overload(QPolygonF)
  @overload(QPolygonF, QPen)
  @overload(QPolygonF, QPen, QBrush)
  def addPolygon(
      self,
      polygon: QPolygonF,
      pen: Optional[QPen] = None,
      brush: Optional[QBrush] = None,
  ) -> Optional[QGraphicsPolygonItem]:
    """
    Calls Qt's 'QGraphicsPolygonItem *QGraphicsScene::addPolygon(const
    QPolygonF &polygon, const QPen &pen, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addPolygon

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    brush : Optional[QBrush]
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own. May be left out, as in Qt: a new 'QBrush()' is then passed on.

    Returns
    -------

    Optional[QGraphicsPolygonItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsPolygonItem *QGraphicsScene::addPolygon(const QPolygonF
    #      &polygon, const QPen &pen, const QBrush &brush)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    if brush is None:
      from ..QtGui import QBrush
      brush = QBrush()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene10addPolygonERK9QPolygonFRK4QPenRK6QBrush',
        self._valueOf(polygon), self._valueOf(pen), self._valueOf(brush),
    )
    from . import QGraphicsPolygonItem
    return QGraphicsPolygonItem._cuteAt(address)

  @overload(QRectF)
  @overload(QRectF, QPen)
  @overload(QRectF, QPen, QBrush)
  def addRect(
      self,
      rect: QRectF,
      pen: Optional[QPen] = None,
      brush: Optional[QBrush] = None,
  ) -> Optional[QGraphicsRectItem]:
    """
    Calls Qt's 'QGraphicsRectItem *QGraphicsScene::addRect(const QRectF
    &rect, const QPen &pen, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    brush : Optional[QBrush]
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own. May be left out, as in Qt: a new 'QBrush()' is then passed on.

    Returns
    -------

    Optional[QGraphicsRectItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsRectItem *QGraphicsScene::addRect(const QRectF &rect, const
    #      QPen &pen, const QBrush &brush)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    if brush is None:
      from ..QtGui import QBrush
      brush = QBrush()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addRectERK6QRectFRK4QPenRK6QBrush',
        self._valueOf(rect), self._valueOf(pen), self._valueOf(brush),
    )
    from . import QGraphicsRectItem
    return QGraphicsRectItem._cuteAt(address)

  @overload(float, float, float, float)
  @overload(float, float, float, float, QPen)
  @overload(float, float, float, float, QPen, QBrush)
  def addRect(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      pen: Optional[QPen] = None,
      brush: Optional[QBrush] = None,
  ) -> Optional[QGraphicsRectItem]:
    """
    Calls Qt's 'QGraphicsRectItem *QGraphicsScene::addRect(qreal x, qreal y,
    qreal w, qreal h, const QPen &pen, const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addRect

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

    pen : Optional[QPen]
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
      May be left out, as in Qt: a new 'QPen()' is then passed on.

    brush : Optional[QBrush]
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own. May be left out, as in Qt: a new 'QBrush()' is then passed on.

    Returns
    -------

    Optional[QGraphicsRectItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsRectItem *QGraphicsScene::addRect(qreal x, qreal y, qreal w,
    #      qreal h, const QPen &pen, const QBrush &brush)
    if pen is None:
      from ..QtGui import QPen
      pen = QPen()
    if brush is None:
      from ..QtGui import QBrush
      brush = QBrush()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addRectEddddRK4QPenRK6QBrush',
        x, y, w, h, self._valueOf(pen), self._valueOf(brush),
    )
    from . import QGraphicsRectItem
    return QGraphicsRectItem._cuteAt(address)

  @overload(str)
  @overload(str, QFont)
  def addText(
      self,
      text: str,
      font: Optional[QFont] = None,
  ) -> Optional[QGraphicsTextItem]:
    """
    Calls Qt's 'QGraphicsTextItem *QGraphicsScene::addText(const QString
    &text, const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    font : Optional[QFont]
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
      May be left out, as in Qt: a new 'QFont()' is then passed on.

    Returns
    -------

    Optional[QGraphicsTextItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsTextItem *QGraphicsScene::addText(const QString &text, const
    #      QFont &font)
    if font is None:
      from ..QtGui import QFont
      font = QFont()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene7addTextERK7QStringRK5QFont',
        text, self._valueOf(font),
    )
    from . import QGraphicsTextItem
    return QGraphicsTextItem._cuteAt(address)

  @overload(str)
  @overload(str, QFont)
  def addSimpleText(
      self,
      text: str,
      font: Optional[QFont] = None,
  ) -> Optional[QGraphicsSimpleTextItem]:
    """
    Calls Qt's 'QGraphicsSimpleTextItem *QGraphicsScene::addSimpleText(const
    QString &text, const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addSimpleText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    font : Optional[QFont]
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
      May be left out, as in Qt: a new 'QFont()' is then passed on.

    Returns
    -------

    Optional[QGraphicsSimpleTextItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsSimpleTextItem *QGraphicsScene::addSimpleText(const QString
    #      &text, const QFont &font)
    if font is None:
      from ..QtGui import QFont
      font = QFont()
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene13addSimpleTextERK7QStringRK5QFont',
        text, self._valueOf(font),
    )
    from . import QGraphicsSimpleTextItem
    return QGraphicsSimpleTextItem._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def addWidget(
      self,
      widget: Optional[QWidget],
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'QGraphicsProxyWidget *QGraphicsScene::addWidget(QWidget
    *widget, Qt::WindowFlags wFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#addWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsProxyWidget *QGraphicsScene::addWidget(QWidget *widget,
    #      Qt::WindowFlags wFlags)
    address = self.uglySide.call(
        'ritual_ZN14QGraphicsScene9addWidgetEP7QWidget6QFlagsIN2Qt10WindowT'
        'ypeEE',
        self._addressOf(widget), wFlags.value,
    )
    from . import QGraphicsProxyWidget
    return QGraphicsProxyWidget._cuteAt(address)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsScene::removeItem(QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#removeItem

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScene::removeItem(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene10removeItemEP13QGraphicsItem',
        self._addressOf(item),
    )

  def clearFocus(self) -> None:
    """
    Calls Qt's 'void QGraphicsScene::clearFocus()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#clearFocus
    """
    #  void QGraphicsScene::clearFocus()
    self.uglySide.call('ritual_ZN14QGraphicsScene10clearFocusEv')

  @overload(float, float, float, float)
  def update(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsScene::update(qreal x, qreal y, qreal w, qreal
    h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#update

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
    #  void QGraphicsScene::update(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call('ritual_ZN14QGraphicsScene6updateEdddd', x, y, w, h)

  @overload()
  @overload(QRectF)
  def update(self, rect: Optional[QRectF] = None) -> None:
    """
    Calls Qt's 'void QGraphicsScene::update(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#update

    Parameters
    ----------

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QGraphicsScene::update(const QRectF &rect)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene6updateERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  @overload(float, float, float, float, SceneLayers)
  def invalidate(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      layers: SceneLayers = SceneLayers.AllLayers,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::invalidate(qreal x, qreal y, qreal w,
    qreal h, SceneLayers layers)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#invalidate

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

    layers : SceneLayers
      Passed on as its number. May be left out, as in Qt: it is then
      SceneLayers.AllLayers.
    """
    #  void QGraphicsScene::invalidate(qreal x, qreal y, qreal w, qreal h,
    #      SceneLayers layers)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene10invalidateEdddd6QFlagsINS_10SceneLayerE'
        'E',
        x, y, w, h, layers.value,
    )

  @overload()
  @overload(QRectF)
  @overload(QRectF, SceneLayers)
  def invalidate(
      self,
      rect: Optional[QRectF] = None,
      layers: SceneLayers = SceneLayers.AllLayers,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsScene::invalidate(const QRectF &rect,
    SceneLayers layers)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#invalidate

    Parameters
    ----------

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    layers : SceneLayers
      Passed on as its number. May be left out, as in Qt: it is then
      SceneLayers.AllLayers.
    """
    #  void QGraphicsScene::invalidate(const QRectF &rect, SceneLayers
    #      layers)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self.uglySide.call(
        'ritual_ZN14QGraphicsScene10invalidateERK6QRectF6QFlagsINS_10SceneL'
        'ayerEE',
        self._valueOf(rect), layers.value,
    )

  @overload(QGraphicsItem, QEvent)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def sendEvent(
      self,
      item: Optional[QGraphicsItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsScene::sendEvent(QGraphicsItem *item, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#sendEvent

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsScene::sendEvent(QGraphicsItem *item, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN14QGraphicsScene9sendEventEP13QGraphicsItemP6QEvent',
        self._addressOf(item), self._addressOf(event),
    )

  def advance(self) -> None:
    """
    Calls Qt's 'void QGraphicsScene::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#advance
    """
    #  void QGraphicsScene::advance()
    self.uglySide.call('ritual_ZN14QGraphicsScene7advanceEv')

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QGraphicsScene::clearSelection()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#clearSelection
    """
    #  void QGraphicsScene::clearSelection()
    self.uglySide.call('ritual_ZN14QGraphicsScene14clearSelectionEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QGraphicsScene::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscene.html#clear
    """
    #  void QGraphicsScene::clear()
    self.uglySide.call('ritual_ZN14QGraphicsScene5clearEv')
