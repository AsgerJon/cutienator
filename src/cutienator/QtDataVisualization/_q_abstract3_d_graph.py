"""
QAbstract3DGraph binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qabstract3dgraph.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QOpenGLFunctions, QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLocale, QMetaObject, QSize
  from ..QtGui import QExposeEvent, QImage, QMouseEvent, QResizeEvent
  from ..QtGui import QSurfaceFormat, QTouchEvent, QVector3D, QWheelEvent
  from . import Q3DScene, Q3DTheme, QAbstract3DAxis, QAbstract3DGraphPrivate
  from . import QAbstract3DInputHandler, QAbstract3DSeries, QCustom3DItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DTheme = WAIT['Q3DTheme']
  QAbstract3DGraphPrivate = WAIT['QAbstract3DGraphPrivate']
  QAbstract3DInputHandler = WAIT['QAbstract3DInputHandler']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QCustom3DItem = WAIT['QtDataVisualization:QCustom3DItem']
  QEvent = WAIT['QEvent']
  QExposeEvent = WAIT['QExposeEvent']
  QLocale = WAIT['QLocale']
  QMouseEvent = WAIT['QMouseEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QSize = WAIT['QSize']
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QTouchEvent = WAIT['QTouchEvent']
  QVector3D = WAIT['QVector3D']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DGraph(QWindow, QOpenGLFunctions):
  """
  The cute side of Qt's QAbstract3DGraph: a plain Python object standing in
  front of one C++ QAbstract3DGraph.

  It is built on the cute 'QWindow', as Qt's QAbstract3DGraph is built on
  Qt's QWindow, and has everything that class has. It is built on the cute
  'QOpenGLFunctions' as well, as Qt's QAbstract3DGraph is built on Qt's
  QOpenGLFunctions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DGraph that has a ritual and that Python
  can call so far, 84 names in all: 'metaObject', 'tr', 'addInputHandler',
  'releaseInputHandler', 'setActiveInputHandler', 'activeInputHandler',
  'inputHandlers', 'addTheme', 'releaseTheme', 'setActiveTheme',
  'activeTheme', 'themes', 'setSelectionMode', 'selectionMode',
  'setShadowQuality', 'shadowQuality', 'shadowsSupported', 'scene',
  'clearSelection', 'hasSeries', 'addCustomItem', 'removeCustomItems',
  'removeCustomItem', 'removeCustomItemAt', 'releaseCustomItem',
  'customItems', 'selectedLabelIndex', 'selectedAxis',
  'selectedCustomItemIndex', 'selectedCustomItem', 'renderToImage',
  'setMeasureFps', 'measureFps', 'currentFps', 'setOrthoProjection',
  'isOrthoProjection', 'selectedElement', 'setAspectRatio', 'aspectRatio',
  'setOptimizationHints', 'optimizationHints', 'setPolar', 'isPolar',
  'setRadialLabelOffset', 'radialLabelOffset', 'setHorizontalAspectRatio',
  'horizontalAspectRatio', 'setReflection', 'isReflection',
  'setReflectivity', 'reflectivity', 'setLocale', 'locale',
  'queriedGraphPosition', 'setMargin', 'margin', 'hasContext', 'event',
  'resizeEvent', 'exposeEvent', 'mouseDoubleClickEvent', 'touchEvent',
  'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent', 'wheelEvent',
  'activeInputHandlerChanged', 'activeThemeChanged', 'selectionModeChanged',
  'shadowQualityChanged', 'selectedElementChanged', 'measureFpsChanged',
  'currentFpsChanged', 'orthoProjectionChanged', 'aspectRatioChanged',
  'optimizationHintsChanged', 'polarChanged', 'radialLabelOffsetChanged',
  'horizontalAspectRatioChanged', 'reflectionChanged', 'reflectivityChanged',
  'localeChanged', 'queriedGraphPositionChanged', 'marginChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DGraph::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstract3DGraph::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstract3DGraph::~QAbstract3DGraph()': the destructor: Python
    never removes a C++ QAbstract3DGraph.

  What has no ritual
  ------------------

  4 of the 92 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstract3DGraph is created at the first use, not by
    'QAbstract3DGraph(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DGraph.
  - Qt tells when it has removed the C++ QAbstract3DGraph. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstract3DGraph, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ElementType(CuteNum):
    """
    The enum 'QAbstract3DGraph::ElementType' of Qt, with the 6 names Qt gives
    in it.
    """

    ElementNone = Kee[int](0)
    ElementSeries = Kee[int](1)
    ElementAxisXLabel = Kee[int](2)
    ElementAxisYLabel = Kee[int](3)
    ElementAxisZLabel = Kee[int](4)
    ElementCustomItem = Kee[int](5)

  class OptimizationHint(CuteFlags):
    """
    The flags enum 'QAbstract3DGraph::OptimizationHint' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QAbstract3DGraph::OptimizationHints'.
    """

    OptimizationDefault = 0x0
    OptimizationStatic = 0x1

  OptimizationHints = OptimizationHint

  class SelectionFlag(CuteFlags):
    """
    The flags enum 'QAbstract3DGraph::SelectionFlag' of Qt, with the 10 names
    Qt gives in it. Qt names the type of its combinations
    'QAbstract3DGraph::SelectionFlags'.
    """

    SelectionNone = 0x0
    SelectionItem = 0x1
    SelectionRow = 0x2
    SelectionItemAndRow = 0x3
    SelectionColumn = 0x4
    SelectionItemAndColumn = 0x5
    SelectionRowAndColumn = 0x6
    SelectionItemRowAndColumn = 0x7
    SelectionSlice = 0x8
    SelectionMultiSeries = 0x10

  SelectionFlags = SelectionFlag

  class ShadowQuality(CuteNum):
    """
    The enum 'QAbstract3DGraph::ShadowQuality' of Qt, with the 7 names Qt
    gives in it.
    """

    ShadowQualityNone = Kee[int](0)
    ShadowQualityLow = Kee[int](1)
    ShadowQualityMedium = Kee[int](2)
    ShadowQualityHigh = Kee[int](3)
    ShadowQualitySoftLow = Kee[int](4)
    ShadowQualitySoftMedium = Kee[int](5)
    ShadowQualitySoftHigh = Kee[int](6)

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
    Calls Qt's 'QString QAbstract3DGraph::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#tr

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
    #  QString QAbstract3DGraph::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QAbstract3DGraph2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DGraph'

  #  Qt's QAbstract3DGraph is built on more than one class. The part of a C++
  #  QAbstract3DGraph that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QOpenGLFunctions': 'ritual_cast_QAbstract3DGraph_QOpenGLFunctions',
  }

  #  A C++ QAbstract3DGraph Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DGraph'

  #  The functions Qt calls itself that QAbstract3DGraph is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'shadowsSupported': (
          ('_ZNK16QAbstract3DGraph16shadowsSupportedEv',
           ('bool', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DGraph::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DGraph::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeInputHandler(self) -> Optional[QAbstract3DInputHandler]:
    """
    Calls Qt's 'QAbstract3DInputHandler
    *QAbstract3DGraph::activeInputHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#activeInputHandler

    Returns
    -------

    Optional[QAbstract3DInputHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DInputHandler *QAbstract3DGraph::activeInputHandler() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph18activeInputHandlerEv',
    )
    from . import QAbstract3DInputHandler
    return QAbstract3DInputHandler._cuteAt(address)

  def inputHandlers(self) -> QList[QAbstract3DInputHandler]:
    """
    Calls Qt's 'QList<QAbstract3DInputHandler *>
    QAbstract3DGraph::inputHandlers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#inputHandlers

    Returns
    -------

    QList[QAbstract3DInputHandler]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DInputHandler *> QAbstract3DGraph::inputHandlers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph13inputHandlersEv',
    )
    from . import QAbstract3DInputHandler
    return QList[QAbstract3DInputHandler]._cuteOwning(address)

  def activeTheme(self) -> Optional[Q3DTheme]:
    """
    Calls Qt's 'Q3DTheme *QAbstract3DGraph::activeTheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#activeTheme

    Returns
    -------

    Optional[Q3DTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DTheme *QAbstract3DGraph::activeTheme() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph11activeThemeEv',
    )
    from . import Q3DTheme
    return Q3DTheme._cuteAt(address)

  def themes(self) -> QList[Q3DTheme]:
    """
    Calls Qt's 'QList<Q3DTheme *> QAbstract3DGraph::themes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#themes

    Returns
    -------

    QList[Q3DTheme]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<Q3DTheme *> QAbstract3DGraph::themes() const
    address = self.uglySide.call('ritual_ZNK16QAbstract3DGraph6themesEv')
    from . import Q3DTheme
    return QList[Q3DTheme]._cuteOwning(address)

  def selectionMode(self) -> SelectionFlags:
    """
    Calls Qt's 'SelectionFlags QAbstract3DGraph::selectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectionMode

    Returns
    -------

    SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  SelectionFlags QAbstract3DGraph::selectionMode() const
    return QAbstract3DGraph.SelectionFlags(self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph13selectionModeEv',
    ))

  def shadowQuality(self) -> ShadowQuality:
    """
    Calls Qt's 'ShadowQuality QAbstract3DGraph::shadowQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#shadowQuality

    Returns
    -------

    ShadowQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShadowQuality(number)'
      gives.
    """
    #  ShadowQuality QAbstract3DGraph::shadowQuality() const
    return QAbstract3DGraph.ShadowQuality(self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph13shadowQualityEv',
    ))

  def shadowsSupported(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::shadowsSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#shadowsSupported
    """
    #  bool QAbstract3DGraph::shadowsSupported() const
    ritual = 'ritual_ZNK16QAbstract3DGraph16shadowsSupportedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAbstract3DGraph16shadowsSupportedEv'
    return self.uglySide.call(ritual)

  def scene(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *QAbstract3DGraph::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#scene

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *QAbstract3DGraph::scene() const
    address = self.uglySide.call('ritual_ZNK16QAbstract3DGraph5sceneEv')
    from . import Q3DScene
    return Q3DScene._cuteAt(address)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def hasSeries(self, series: Optional[QAbstract3DSeries]) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::hasSeries(QAbstract3DSeries *series)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#hasSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstract3DGraph::hasSeries(QAbstract3DSeries *series) const
    return self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph9hasSeriesEP17QAbstract3DSeries',
        self._addressOf(series),
    )

  def customItems(self) -> QList[QCustom3DItem]:
    """
    Calls Qt's 'QList<QCustom3DItem *> QAbstract3DGraph::customItems()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#customItems

    Returns
    -------

    QList[QCustom3DItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCustom3DItem *> QAbstract3DGraph::customItems() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph11customItemsEv',
    )
    from . import QCustom3DItem
    return QList[QCustom3DItem]._cuteOwning(address)

  def selectedLabelIndex(self) -> int:
    """
    Calls Qt's 'int QAbstract3DGraph::selectedLabelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectedLabelIndex
    """
    #  int QAbstract3DGraph::selectedLabelIndex() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph18selectedLabelIndexEv',
    )

  def selectedAxis(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QAbstract3DGraph::selectedAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#selectedAxis

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QAbstract3DGraph::selectedAxis() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph12selectedAxisEv',
    )
    from . import QAbstract3DAxis
    return QAbstract3DAxis._cuteAt(address)

  def selectedCustomItemIndex(self) -> int:
    """
    Calls Qt's 'int QAbstract3DGraph::selectedCustomItemIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectedCustomItemIndex
    """
    #  int QAbstract3DGraph::selectedCustomItemIndex() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph23selectedCustomItemIndexEv',
    )

  def selectedCustomItem(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *QAbstract3DGraph::selectedCustomItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectedCustomItem

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *QAbstract3DGraph::selectedCustomItem() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph18selectedCustomItemEv',
    )
    from . import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  def measureFps(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::measureFps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#measureFps
    """
    #  bool QAbstract3DGraph::measureFps() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph10measureFpsEv')

  def currentFps(self) -> float:
    """
    Calls Qt's 'qreal QAbstract3DGraph::currentFps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#currentFps
    """
    #  qreal QAbstract3DGraph::currentFps() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph10currentFpsEv')

  def isOrthoProjection(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::isOrthoProjection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#isOrthoProjection
    """
    #  bool QAbstract3DGraph::isOrthoProjection() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph17isOrthoProjectionEv',
    )

  def selectedElement(self) -> ElementType:
    """
    Calls Qt's 'ElementType QAbstract3DGraph::selectedElement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectedElement

    Returns
    -------

    ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ElementType(number)'
      gives.
    """
    #  ElementType QAbstract3DGraph::selectedElement() const
    return QAbstract3DGraph.ElementType(self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph15selectedElementEv',
    ))

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'qreal QAbstract3DGraph::aspectRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#aspectRatio
    """
    #  qreal QAbstract3DGraph::aspectRatio() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph11aspectRatioEv')

  def optimizationHints(self) -> OptimizationHints:
    """
    Calls Qt's 'OptimizationHints QAbstract3DGraph::optimizationHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#optimizationHints

    Returns
    -------

    OptimizationHints
      The value standing for the combination Qt gave back.
    """
    #  OptimizationHints QAbstract3DGraph::optimizationHints() const
    return QAbstract3DGraph.OptimizationHints(self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph17optimizationHintsEv',
    ))

  def isPolar(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::isPolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#isPolar
    """
    #  bool QAbstract3DGraph::isPolar() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph7isPolarEv')

  def radialLabelOffset(self) -> float:
    """
    Calls Qt's 'float QAbstract3DGraph::radialLabelOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#radialLabelOffset
    """
    #  float QAbstract3DGraph::radialLabelOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph17radialLabelOffsetEv',
    )

  def horizontalAspectRatio(self) -> float:
    """
    Calls Qt's 'qreal QAbstract3DGraph::horizontalAspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#horizontalAspectRatio
    """
    #  qreal QAbstract3DGraph::horizontalAspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph21horizontalAspectRatioEv',
    )

  def isReflection(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::isReflection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#isReflection
    """
    #  bool QAbstract3DGraph::isReflection() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph12isReflectionEv')

  def reflectivity(self) -> float:
    """
    Calls Qt's 'qreal QAbstract3DGraph::reflectivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#reflectivity
    """
    #  qreal QAbstract3DGraph::reflectivity() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph12reflectivityEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QAbstract3DGraph::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QAbstract3DGraph::locale() const
    address = self.uglySide.call('ritual_ZNK16QAbstract3DGraph6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def queriedGraphPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QAbstract3DGraph::queriedGraphPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#queriedGraphPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QAbstract3DGraph::queriedGraphPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16QAbstract3DGraph20queriedGraphPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def margin(self) -> float:
    """
    Calls Qt's 'qreal QAbstract3DGraph::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#margin
    """
    #  qreal QAbstract3DGraph::margin() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph6marginEv')

  def hasContext(self) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::hasContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#hasContext
    """
    #  bool QAbstract3DGraph::hasContext() const
    return self.uglySide.call('ritual_ZNK16QAbstract3DGraph10hasContextEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def setActiveInputHandler(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::setActiveInputHandler(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setActiveInputHandler

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::setActiveInputHandler(QAbstract3DInputHandler
    #      *inputHandler)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph21setActiveInputHandlerEP23QAbstract3DI'
        'nputHandler',
        self._addressOf(inputHandler),
    )

  @overload(Q3DTheme)
  @overload(NoneType)
  def setActiveTheme(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setActiveTheme(Q3DTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setActiveTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::setActiveTheme(Q3DTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph14setActiveThemeEP8Q3DTheme',
        self._addressOf(theme),
    )

  @overload(SelectionFlags)
  def setSelectionMode(self, mode: SelectionFlags) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setSelectionMode(SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setSelectionMode

    Parameters
    ----------

    mode : SelectionFlags
      Passed on as its number.
    """
    #  void QAbstract3DGraph::setSelectionMode(SelectionFlags mode)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph16setSelectionModeE6QFlagsINS_13Selecti'
        'onFlagEE',
        mode.value,
    )

  @overload(ShadowQuality)
  def setShadowQuality(self, quality: ShadowQuality) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setShadowQuality(ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setShadowQuality

    Parameters
    ----------

    quality : ShadowQuality
      Passed on as its number.
    """
    #  void QAbstract3DGraph::setShadowQuality(ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph16setShadowQualityENS_13ShadowQualityE',
        quality.value,
    )

  @overload(bool)
  def setMeasureFps(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setMeasureFps(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setMeasureFps

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setMeasureFps(bool enable)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph13setMeasureFpsEb', enable,
    )

  @overload(bool)
  def setOrthoProjection(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setOrthoProjection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setOrthoProjection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setOrthoProjection(bool enable)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph18setOrthoProjectionEb', enable,
    )

  @overload(float)
  def setAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setAspectRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph14setAspectRatioEd', ratio,
    )

  @overload(OptimizationHints)
  def setOptimizationHints(self, hints: OptimizationHints) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setOptimizationHints(OptimizationHints
    hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setOptimizationHints

    Parameters
    ----------

    hints : OptimizationHints
      Passed on as its number.
    """
    #  void QAbstract3DGraph::setOptimizationHints(OptimizationHints hints)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph20setOptimizationHintsE6QFlagsINS_16Opt'
        'imizationHintEE',
        hints.value,
    )

  @overload(bool)
  def setPolar(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setPolar(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#setPolar

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setPolar(bool enable)
    self.uglySide.call('ritual_ZN16QAbstract3DGraph8setPolarEb', enable)

  @overload(float)
  def setRadialLabelOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setRadialLabelOffset(float offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setRadialLabelOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setRadialLabelOffset(float offset)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph20setRadialLabelOffsetEf', offset,
    )

  @overload(float)
  def setHorizontalAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setHorizontalAspectRatio(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setHorizontalAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setHorizontalAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph24setHorizontalAspectRatioEd', ratio,
    )

  @overload(bool)
  def setReflection(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setReflection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setReflection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setReflection(bool enable)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph13setReflectionEb', enable,
    )

  @overload(float)
  def setReflectivity(self, reflectivity: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setReflectivity(qreal reflectivity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#setReflectivity

    Parameters
    ----------

    reflectivity : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setReflectivity(qreal reflectivity)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph15setReflectivityEd', reflectivity,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QAbstract3DGraph::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::setMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#setMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::setMargin(qreal margin)
    self.uglySide.call('ritual_ZN16QAbstract3DGraph9setMarginEd', margin)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DGraphPrivate, QSurfaceFormat)
  @overload(QAbstract3DGraphPrivate, NoneType)
  @overload(NoneType, QSurfaceFormat)
  @overload(NoneType, NoneType)
  @overload(QAbstract3DGraphPrivate, QSurfaceFormat, QWindow)
  @overload(QAbstract3DGraphPrivate, QSurfaceFormat, NoneType)
  @overload(QAbstract3DGraphPrivate, NoneType, QWindow)
  @overload(QAbstract3DGraphPrivate, NoneType, NoneType)
  @overload(NoneType, QSurfaceFormat, QWindow)
  @overload(NoneType, QSurfaceFormat, NoneType)
  @overload(NoneType, NoneType, QWindow)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QAbstract3DGraphPrivate],
      format: Optional[QSurfaceFormat],
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstract3DGraph::QAbstract3DGraph(QAbstract3DGraphPrivate *d, const
    QSurfaceFormat *format, QWindow *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#QAbstract3DGraph

    Parameters
    ----------

    d : Optional[QAbstract3DGraphPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[QSurfaceFormat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstract3DGraph::QAbstract3DGraph(QAbstract3DGraphPrivate *d, const
    #      QSurfaceFormat *format, QWindow *parent)
    self._noteCreation(QAbstract3DGraph, lambda: Rituals.call(
        'ritual_ZN16QAbstract3DGraphC1EP23QAbstract3DGraphPrivatePK14QSurfa'
        'ceFormatP7QWindow',
        self._addressOf(d), self._addressOf(format), self._addressOf(parent),
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

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def addInputHandler(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::addInputHandler(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#addInputHandler

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::addInputHandler(QAbstract3DInputHandler
    #      *inputHandler)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph15addInputHandlerEP23QAbstract3DInputHa'
        'ndler',
        self._addressOf(inputHandler),
    )

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def releaseInputHandler(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::releaseInputHandler(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#releaseInputHandler

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::releaseInputHandler(QAbstract3DInputHandler
    #      *inputHandler)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph19releaseInputHandlerEP23QAbstract3DInp'
        'utHandler',
        self._addressOf(inputHandler),
    )

  @overload(Q3DTheme)
  @overload(NoneType)
  def addTheme(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::addTheme(Q3DTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#addTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::addTheme(Q3DTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph8addThemeEP8Q3DTheme',
        self._addressOf(theme),
    )

  @overload(Q3DTheme)
  @overload(NoneType)
  def releaseTheme(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::releaseTheme(Q3DTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#releaseTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::releaseTheme(Q3DTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph12releaseThemeEP8Q3DTheme',
        self._addressOf(theme),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#clearSelection
    """
    #  void QAbstract3DGraph::clearSelection()
    self.uglySide.call('ritual_ZN16QAbstract3DGraph14clearSelectionEv')

  @overload(QCustom3DItem)
  @overload(NoneType)
  def addCustomItem(self, item: Optional[QCustom3DItem]) -> int:
    """
    Calls Qt's 'int QAbstract3DGraph::addCustomItem(QCustom3DItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#addCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAbstract3DGraph::addCustomItem(QCustom3DItem *item)
    return self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph13addCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  def removeCustomItems(self) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::removeCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#removeCustomItems
    """
    #  void QAbstract3DGraph::removeCustomItems()
    self.uglySide.call('ritual_ZN16QAbstract3DGraph17removeCustomItemsEv')

  @overload(QCustom3DItem)
  @overload(NoneType)
  def removeCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::removeCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#removeCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::removeCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph16removeCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(QVector3D)
  def removeCustomItemAt(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::removeCustomItemAt(const QVector3D
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#removeCustomItemAt

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QAbstract3DGraph::removeCustomItemAt(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph18removeCustomItemAtERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def releaseCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::releaseCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#releaseCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::releaseCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph17releaseCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload()
  @overload(int)
  @overload(int, QSize)
  def renderToImage(
      self,
      msaaSamples: int = 0,
      imageSize: Optional[QSize] = None,
  ) -> QImage:
    """
    Calls Qt's 'QImage QAbstract3DGraph::renderToImage(int msaaSamples, const
    QSize &imageSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#renderToImage

    Parameters
    ----------

    msaaSamples : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    imageSize : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QAbstract3DGraph::renderToImage(int msaaSamples, const QSize
    #      &imageSize)
    if imageSize is None:
      from ..QtCore import QSize
      imageSize = QSize()
    address = self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph13renderToImageEiRK5QSize',
        msaaSamples, self._valueOf(imageSize),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstract3DGraph::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstract3DGraph::event(QEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstract3DGraph5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstract3DGraph11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QExposeEvent)
  @overload(NoneType)
  def exposeEvent(self, event: Optional[QExposeEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::exposeEvent(QExposeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#exposeEvent

    Parameters
    ----------

    event : Optional[QExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::exposeEvent(QExposeEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph11exposeEventEP12QExposeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstract3DGraph11exposeEventEP12QExposeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN16QAbstract3DGraph21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAbstract3DGraph21mouseDoubleClickEventEP11QMouse'
          'Event')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstract3DGraph10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAbstract3DGraph15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAbstract3DGraph17mouseReleaseEventEP11QMouseEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAbstract3DGraph14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN16QAbstract3DGraph10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAbstract3DGraph10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def activeInputHandlerChanged(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::activeInputHandlerChanged(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#activeInputHandlerChanged

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::activeInputHandlerChanged(
    #      QAbstract3DInputHandler *inputHandler)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph25activeInputHandlerChangedEP23QAbstrac'
        't3DInputHandler',
        self._addressOf(inputHandler),
    )

  @overload(Q3DTheme)
  @overload(NoneType)
  def activeThemeChanged(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::activeThemeChanged(Q3DTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#activeThemeChanged

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraph::activeThemeChanged(Q3DTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph18activeThemeChangedEP8Q3DTheme',
        self._addressOf(theme),
    )

  @overload(SelectionFlags)
  def selectionModeChanged(self, mode: SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::selectionModeChanged(QAbstract3DGraph::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectionModeChanged

    Parameters
    ----------

    mode : SelectionFlags
      Passed on as its number.
    """
    #  void QAbstract3DGraph::selectionModeChanged(QAbstract3DGraph::
    #      SelectionFlags mode)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph20selectionModeChangedE6QFlagsINS_13Sel'
        'ectionFlagEE',
        mode.value,
    )

  @overload(ShadowQuality)
  def shadowQualityChanged(self, quality: ShadowQuality) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::shadowQualityChanged(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#shadowQualityChanged

    Parameters
    ----------

    quality : ShadowQuality
      Passed on as its number.
    """
    #  void QAbstract3DGraph::shadowQualityChanged(QAbstract3DGraph::
    #      ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph20shadowQualityChangedENS_13ShadowQuali'
        'tyE',
        quality.value,
    )

  @overload(ElementType)
  def selectedElementChanged(self, type: ElementType) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::selectedElementChanged(QAbstract3DGraph::ElementType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#selectedElementChanged

    Parameters
    ----------

    type : ElementType
      Passed on as its number.
    """
    #  void QAbstract3DGraph::selectedElementChanged(QAbstract3DGraph::
    #      ElementType type)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph22selectedElementChangedENS_11ElementTy'
        'peE',
        type.value,
    )

  @overload(bool)
  def measureFpsChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::measureFpsChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#measureFpsChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::measureFpsChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph17measureFpsChangedEb', enabled,
    )

  @overload(float)
  def currentFpsChanged(self, fps: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::currentFpsChanged(qreal fps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#currentFpsChanged

    Parameters
    ----------

    fps : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::currentFpsChanged(qreal fps)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph17currentFpsChangedEd', fps,
    )

  @overload(bool)
  def orthoProjectionChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::orthoProjectionChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#orthoProjectionChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::orthoProjectionChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph22orthoProjectionChangedEb', enabled,
    )

  @overload(float)
  def aspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::aspectRatioChanged(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#aspectRatioChanged

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::aspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph18aspectRatioChangedEd', ratio,
    )

  @overload(OptimizationHints)
  def optimizationHintsChanged(self, hints: OptimizationHints) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraph::optimizationHintsChanged(QAbstract3DGraph::
    OptimizationHints hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#optimizationHintsChanged

    Parameters
    ----------

    hints : OptimizationHints
      Passed on as its number.
    """
    #  void QAbstract3DGraph::optimizationHintsChanged(QAbstract3DGraph::
    #      OptimizationHints hints)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph24optimizationHintsChangedE6QFlagsINS_1'
        '6OptimizationHintEE',
        hints.value,
    )

  @overload(bool)
  def polarChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::polarChanged(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dgraph.html#polarChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::polarChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph12polarChangedEb', enabled,
    )

  @overload(float)
  def radialLabelOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::radialLabelOffsetChanged(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#radialLabelOffsetChanged

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::radialLabelOffsetChanged(float offset)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph24radialLabelOffsetChangedEf', offset,
    )

  @overload(float)
  def horizontalAspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::horizontalAspectRatioChanged(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#horizontalAspectRatioChanged

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::horizontalAspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph28horizontalAspectRatioChangedEd', ratio,
    )

  @overload(bool)
  def reflectionChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::reflectionChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#reflectionChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAbstract3DGraph::reflectionChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph17reflectionChangedEb', enabled,
    )

  @overload(float)
  def reflectivityChanged(self, reflectivity: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::reflectivityChanged(qreal
    reflectivity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#reflectivityChanged

    Parameters
    ----------

    reflectivity : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::reflectivityChanged(qreal reflectivity)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph19reflectivityChangedEd', reflectivity,
    )

  @overload(QLocale)
  def localeChanged(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::localeChanged(const QLocale &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#localeChanged

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QAbstract3DGraph::localeChanged(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph13localeChangedERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QVector3D)
  def queriedGraphPositionChanged(self, data: QVector3D) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::queriedGraphPositionChanged(const
    QVector3D &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#queriedGraphPositionChanged

    Parameters
    ----------

    data : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QAbstract3DGraph::queriedGraphPositionChanged(const QVector3D
    #      &data)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph27queriedGraphPositionChangedERK9QVecto'
        'r3D',
        self._valueOf(data),
    )

  @overload(float)
  def marginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void QAbstract3DGraph::marginChanged(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraph.html#marginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QAbstract3DGraph::marginChanged(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QAbstract3DGraph13marginChangedEd', margin,
    )
