"""
QPaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt
from . import QPaintEngineDirtyFlag, QPaintEnginePaintEngineFeature
from . import QPaintEnginePolygonDrawMode, QPaintEngineType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF, QSize
  from . import QImage, QPaintDevice, QPaintEngineState, QPainter
  from . import QPainterPath, QPixmap, QRegion, QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QLine = WAIT['QLine']
  QLineF = WAIT['QLineF']
  QPaintDevice = WAIT['QPaintDevice']
  QPaintEngineState = WAIT['QPaintEngineState']
  QPainterPath = WAIT['QPainterPath']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QTextItem = WAIT['QTextItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPaintEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPaintEngine: a plain Python object standing in front
  of one C++ QPaintEngine.

  What exists
  -----------

  Every function of Qt's QPaintEngine that has a ritual and that Python can
  call so far, 32 names in all: 'isActive', 'setActive', 'begin', 'end',
  'updateState', 'drawRects', 'drawLines', 'drawEllipse', 'drawPath',
  'drawPoints', 'drawPolygon', 'drawPixmap', 'drawTextItem',
  'drawTiledPixmap', 'drawImage', 'setPaintDevice', 'paintDevice',
  'setSystemClip', 'systemClip', 'setSystemRect', 'systemRect',
  'coordinateOffset', 'type', 'testDirty', 'setDirty', 'clearDirty',
  'hasFeature', 'painter', 'syncState', 'isExtended', 'createPixmap',
  'createPixmapFromImage'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPaintEngine::~QPaintEngine()': the destructor: Python never
    removes a C++ QPaintEngine.
  - Qt's 'void QPaintEngine::fix_neg_rect(int *x, int *y, int *w, int *h)':
    takes a number to change where it is.

  What has no ritual
  ------------------

  8 of the 47 functions Qt declares: 4 private; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one; 1 protected.

  What to expect
  --------------

  - The C++ QPaintEngine is created at the first use, not by
    'QPaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPaintEngine.
  """

  #  The enums Qt writes inside QPaintEngine, and the names Qt has for the
  #  combinations of its flags enums.
  DirtyFlag = QPaintEngineDirtyFlag
  DirtyFlags = QPaintEngineDirtyFlag
  PaintEngineFeature = QPaintEnginePaintEngineFeature
  PaintEngineFeatures = QPaintEnginePaintEngineFeature
  PolygonDrawMode = QPaintEnginePolygonDrawMode
  Type = QPaintEngineType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPaintEngine::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#isActive
    """
    #  bool QPaintEngine::isActive() const
    return self.uglySide.call('ritual_ZNK12QPaintEngine8isActiveEv')

  def paintDevice(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QPaintEngine::paintDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#paintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QPaintEngine::paintDevice() const
    address = self.uglySide.call('ritual_ZNK12QPaintEngine11paintDeviceEv')
    from . import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def systemClip(self) -> QRegion:
    """
    Calls Qt's 'QRegion QPaintEngine::systemClip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#systemClip

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QPaintEngine::systemClip() const
    address = self.uglySide.call('ritual_ZNK12QPaintEngine10systemClipEv')
    from . import QRegion
    return QRegion._cuteOwning(address)

  def systemRect(self) -> QRect:
    """
    Calls Qt's 'QRect QPaintEngine::systemRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#systemRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPaintEngine::systemRect() const
    address = self.uglySide.call('ritual_ZNK12QPaintEngine10systemRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def coordinateOffset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPaintEngine::coordinateOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#coordinateOffset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPaintEngine::coordinateOffset() const
    address = self.uglySide.call(
        'ritual_ZNK12QPaintEngine16coordinateOffsetEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QPaintEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QPaintEngine::type() const
    return QPaintEngine.Type(self.uglySide.call(
        'ritual_ZNK12QPaintEngine4typeEv',
    ))

  @overload(PaintEngineFeatures)
  def hasFeature(self, feature: PaintEngineFeatures) -> bool:
    """
    Calls Qt's 'bool QPaintEngine::hasFeature(PaintEngineFeatures feature)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#hasFeature

    Parameters
    ----------

    feature : PaintEngineFeatures
      Passed on as its number.
    """
    #  bool QPaintEngine::hasFeature(PaintEngineFeatures feature) const
    return self.uglySide.call(
        'ritual_ZNK12QPaintEngine10hasFeatureE6QFlagsINS_18PaintEngineFeatu'
        'reEE',
        feature.value,
    )

  def painter(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QPaintEngine::painter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#painter

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QPaintEngine::painter() const
    address = self.uglySide.call('ritual_ZNK12QPaintEngine7painterEv')
    from . import QPainter
    return QPainter._cuteAt(address)

  def isExtended(self) -> bool:
    """
    Calls Qt's 'bool QPaintEngine::isExtended() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#isExtended
    """
    #  bool QPaintEngine::isExtended() const
    return self.uglySide.call('ritual_ZNK12QPaintEngine10isExtendedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, newState: bool) -> None:
    """
    Calls Qt's 'void QPaintEngine::setActive(bool newState)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#setActive

    Parameters
    ----------

    newState : bool
      Passed on as it is.
    """
    #  void QPaintEngine::setActive(bool newState)
    self.uglySide.call('ritual_ZN12QPaintEngine9setActiveEb', newState)

  @overload(QPaintDevice)
  @overload(NoneType)
  def setPaintDevice(self, device: Optional[QPaintDevice]) -> None:
    """
    Calls Qt's 'void QPaintEngine::setPaintDevice(QPaintDevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#setPaintDevice

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPaintEngine::setPaintDevice(QPaintDevice *device)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine14setPaintDeviceEP12QPaintDevice',
        self._addressOf(device),
    )

  @overload(QRegion)
  def setSystemClip(self, baseClip: QRegion) -> None:
    """
    Calls Qt's 'void QPaintEngine::setSystemClip(const QRegion &baseClip)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#setSystemClip

    Parameters
    ----------

    baseClip : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintEngine::setSystemClip(const QRegion &baseClip)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine13setSystemClipERK7QRegion',
        self._valueOf(baseClip),
    )

  @overload(QRect)
  def setSystemRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QPaintEngine::setSystemRect(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#setSystemRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPaintEngine::setSystemRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine13setSystemRectERK5QRect',
        self._valueOf(rect),
    )

  @overload(DirtyFlags)
  def setDirty(self, df: DirtyFlags) -> None:
    """
    Calls Qt's 'void QPaintEngine::setDirty(DirtyFlags df)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#setDirty

    Parameters
    ----------

    df : DirtyFlags
      Passed on as its number.
    """
    #  void QPaintEngine::setDirty(DirtyFlags df)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine8setDirtyE6QFlagsINS_9DirtyFlagEE', df.value,
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

  @overload(QPaintDevice)
  @overload(NoneType)
  def begin(self, pdev: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QPaintEngine::begin(QPaintDevice *pdev)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#begin

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPaintEngine::begin(QPaintDevice *pdev)
    return self.uglySide.call(
        'ritual_ZN12QPaintEngine5beginEP12QPaintDevice',
        self._addressOf(pdev),
    )

  def end(self) -> bool:
    """
    Calls Qt's 'bool QPaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#end
    """
    #  bool QPaintEngine::end()
    return self.uglySide.call('ritual_ZN12QPaintEngine3endEv')

  @overload(QPaintEngineState)
  def updateState(self, state: QPaintEngineState) -> None:
    """
    Calls Qt's 'void QPaintEngine::updateState(const QPaintEngineState
    &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#updateState

    Parameters
    ----------

    state : QPaintEngineState
      Passed on as a value: Qt reads the C++ QPaintEngineState, which stays
      Python's own.
    """
    #  void QPaintEngine::updateState(const QPaintEngineState &state)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine11updateStateERK17QPaintEngineState',
        self._valueOf(state),
    )

  @overload(QRect, int)
  @overload(NoneType, int)
  def drawRects(self, rects: Optional[QRect], rectCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawRects(const QRect *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine9drawRectsEPK5QRecti',
        self._addressOf(rects), rectCount,
    )

  @overload(QRectF, int)
  def drawRects(self, rects: Optional[QRectF], rectCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawRects(const QRectF *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine9drawRectsEPK6QRectFi',
        self._addressOf(rects), rectCount,
    )

  @overload(QLine, int)
  @overload(NoneType, int)
  def drawLines(self, lines: Optional[QLine], lineCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawLines(const QLine *lines, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawLines

    Parameters
    ----------

    lines : Optional[QLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine9drawLinesEPK5QLinei',
        self._addressOf(lines), lineCount,
    )

  @overload(QLineF, int)
  def drawLines(self, lines: Optional[QLineF], lineCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawLines(const QLineF *lines, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawLines

    Parameters
    ----------

    lines : Optional[QLineF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine9drawLinesEPK6QLineFi',
        self._addressOf(lines), lineCount,
    )

  @overload(QRectF)
  def drawEllipse(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawEllipse(const QRectF &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawEllipse

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPaintEngine::drawEllipse(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine11drawEllipseERK6QRectF', self._valueOf(r),
    )

  @overload(QRect)
  def drawEllipse(self, r: QRect) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawEllipse(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawEllipse

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPaintEngine::drawEllipse(const QRect &r)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine11drawEllipseERK5QRect', self._valueOf(r),
    )

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPaintEngine::drawPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine8drawPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawPoints(const QPointF *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine10drawPointsEPK7QPointFi',
        self._addressOf(points), pointCount,
    )

  @overload(QPoint, int)
  def drawPoints(self, points: Optional[QPoint], pointCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawPoints(const QPoint *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine10drawPointsEPK6QPointi',
        self._addressOf(points), pointCount,
    )

  @overload(QPointF, int, PolygonDrawMode)
  @overload(NoneType, int, PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawPolygon(const QPointF *points, int
    pointCount, PolygonDrawMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : PolygonDrawMode
      Passed on as its number.
    """
    #  void QPaintEngine::drawPolygon(const QPointF *points, int pointCount,
    #      PolygonDrawMode mode)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawMo'
        'deE',
        self._addressOf(points), pointCount, mode.value,
    )

  @overload(QPoint, int, PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPoint],
      pointCount: int,
      mode: PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawPolygon(const QPoint *points, int
    pointCount, PolygonDrawMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : PolygonDrawMode
      Passed on as its number.
    """
    #  void QPaintEngine::drawPolygon(const QPoint *points, int pointCount,
    #      PolygonDrawMode mode)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawMod'
        'eE',
        self._addressOf(points), pointCount, mode.value,
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawPixmap(const QRectF &r, const QPixmap
    &pm, const QRectF &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
    #      const QRectF &sr)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_',
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawTextItem(const QPointF &p, const
    QTextItem &textItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPaintEngine::drawTextItem(const QPointF &p, const QTextItem
    #      &textItem)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem',
        self._valueOf(p), self._valueOf(textItem),
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pixmap: QPixmap, s: QPointF) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawTiledPixmap(const QRectF &r, const
    QPixmap &pixmap, const QPointF &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawTiledPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    s : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
    #      &pixmap, const QPointF &s)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPo'
        'intF',
        self._valueOf(r), self._valueOf(pixmap), self._valueOf(s),
    )

  @overload(QRectF, QImage, QRectF)
  @overload(QRectF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      r: QRectF,
      pm: QImage,
      sr: QRectF,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngine::drawImage(const QRectF &r, const QImage
    &pm, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#drawImage

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPaintEngine::drawImage(const QRectF &r, const QImage &pm, const
    #      QRectF &sr, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Q'
        't19ImageConversionFlagEE',
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr), flags.value,
    )

  @overload(DirtyFlags)
  def testDirty(self, df: DirtyFlags) -> bool:
    """
    Calls Qt's 'bool QPaintEngine::testDirty(DirtyFlags df)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#testDirty

    Parameters
    ----------

    df : DirtyFlags
      Passed on as its number.
    """
    #  bool QPaintEngine::testDirty(DirtyFlags df)
    return self.uglySide.call(
        'ritual_ZN12QPaintEngine9testDirtyE6QFlagsINS_9DirtyFlagEE',
        df.value,
    )

  @overload(DirtyFlags)
  def clearDirty(self, df: DirtyFlags) -> None:
    """
    Calls Qt's 'void QPaintEngine::clearDirty(DirtyFlags df)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#clearDirty

    Parameters
    ----------

    df : DirtyFlags
      Passed on as its number.
    """
    #  void QPaintEngine::clearDirty(DirtyFlags df)
    self.uglySide.call(
        'ritual_ZN12QPaintEngine10clearDirtyE6QFlagsINS_9DirtyFlagEE',
        df.value,
    )

  def syncState(self) -> None:
    """
    Calls Qt's 'void QPaintEngine::syncState()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#syncState
    """
    #  void QPaintEngine::syncState()
    self.uglySide.call('ritual_ZN12QPaintEngine9syncStateEv')

  @overload(QSize)
  def createPixmap(self, size: QSize) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPaintEngine::createPixmap(QSize size)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengine.html#createPixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPaintEngine::createPixmap(QSize size)
    address = self.uglySide.call(
        'ritual_ZN12QPaintEngine12createPixmapE5QSize', self._valueOf(size),
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QImage)
  @overload(QImage, Qt.ImageConversionFlags)
  def createPixmapFromImage(
      self,
      image: QImage,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPaintEngine::createPixmapFromImage(QImage image,
    Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengine.html#createPixmapFromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPaintEngine::createPixmapFromImage(QImage image,
    #      Qt::ImageConversionFlags flags)
    address = self.uglySide.call(
        'ritual_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt'
        '19ImageConversionFlagEE',
        self._valueOf(image), flags.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)
