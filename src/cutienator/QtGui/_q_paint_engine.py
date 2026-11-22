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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..QtCore import Qt

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

  #  The enums Qt writes inside QPaintEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class DirtyFlag(CuteFlags):
    """
    The flags enum 'QPaintEngine::DirtyFlag' of Qt, with the 14 names Qt
    gives in it. Qt names the type of its combinations
    'QPaintEngine::DirtyFlags'.
    """

    DirtyPen = 0x1
    DirtyBrush = 0x2
    DirtyBrushOrigin = 0x4
    DirtyFont = 0x8
    DirtyBackground = 0x10
    DirtyBackgroundMode = 0x20
    DirtyTransform = 0x40
    DirtyClipRegion = 0x80
    DirtyClipPath = 0x100
    DirtyHints = 0x200
    DirtyCompositionMode = 0x400
    DirtyClipEnabled = 0x800
    DirtyOpacity = 0x1000
    AllDirty = 0xffff

  DirtyFlags = DirtyFlag

  class PaintEngineFeature(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QPaintEngine::PaintEngineFeature' of Qt, with the 20
    names Qt gives in it. Qt names the type of its combinations
    'QPaintEngine::PaintEngineFeatures'.
    """

    PrimitiveTransform = 0x1
    PatternTransform = 0x2
    PixmapTransform = 0x4
    PatternBrush = 0x8
    LinearGradientFill = 0x10
    RadialGradientFill = 0x20
    ConicalGradientFill = 0x40
    AlphaBlend = 0x80
    PorterDuff = 0x100
    PainterPaths = 0x200
    Antialiasing = 0x400
    BrushStroke = 0x800
    ConstantOpacity = 0x1000
    MaskedBrush = 0x2000
    PerspectiveTransform = 0x4000
    BlendModes = 0x8000
    ObjectBoundingModeGradients = 0x10000
    RasterOpModes = 0x20000
    PaintOutsidePaintEvent = 0x20000000
    AllFeatures = 0xffffffff

  PaintEngineFeatures = PaintEngineFeature

  class PolygonDrawMode(CuteNum):
    """
    The enum 'QPaintEngine::PolygonDrawMode' of Qt, with the 4 names Qt gives
    in it.
    """

    OddEvenMode = Kee[int](0)
    WindingMode = Kee[int](1)
    ConvexMode = Kee[int](2)
    PolylineMode = Kee[int](3)

  class Type(CuteNum):
    """
    The enum 'QPaintEngine::Type' of Qt, with the 19 names Qt gives in it.
    """

    X11 = Kee[int](0)
    Windows = Kee[int](1)
    QuickDraw = Kee[int](2)
    CoreGraphics = Kee[int](3)
    MacPrinter = Kee[int](4)
    QWindowSystem = Kee[int](5)
    OpenGL = Kee[int](6)
    Picture = Kee[int](7)
    SVG = Kee[int](8)
    Raster = Kee[int](9)
    Direct3D = Kee[int](10)
    Pdf = Kee[int](11)
    OpenVG = Kee[int](12)
    OpenGL2 = Kee[int](13)
    PaintBuffer = Kee[int](14)
    Blitter = Kee[int](15)
    Direct2D = Kee[int](16)
    User = Kee[int](50)
    MaxUser = Kee[int](100)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintEngine'

  #  A C++ QPaintEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPaintEngine'

  #  The functions Qt calls itself that QPaintEngine is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'begin': (
          ('_ZN12QPaintEngine5beginEP12QPaintDevice',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPaintDevice'),
           )),
      ),
      'end': (
          ('_ZN12QPaintEngine3endEv',
           ('bool', 'number', ''),
           ()),
      ),
      'updateState': (
          ('_ZN12QPaintEngine11updateStateERK17QPaintEngineState',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPaintEngineState'),
           )),
      ),
      'drawRects': (
          ('_ZN12QPaintEngine9drawRectsEPK5QRecti',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QRect'),
               ('int', 'number', ''),
           )),
          ('_ZN12QPaintEngine9drawRectsEPK6QRectFi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QRectF'),
               ('int', 'number', ''),
           )),
      ),
      'drawLines': (
          ('_ZN12QPaintEngine9drawLinesEPK5QLinei',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QLine'),
               ('int', 'number', ''),
           )),
          ('_ZN12QPaintEngine9drawLinesEPK6QLineFi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QLineF'),
               ('int', 'number', ''),
           )),
      ),
      'drawEllipse': (
          ('_ZN12QPaintEngine11drawEllipseERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
          ('_ZN12QPaintEngine11drawEllipseERK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'drawPath': (
          ('_ZN12QPaintEngine8drawPathERK12QPainterPath',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPainterPath'),
           )),
      ),
      'drawPoints': (
          ('_ZN12QPaintEngine10drawPointsEPK7QPointFi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QPointF'),
               ('int', 'number', ''),
           )),
          ('_ZN12QPaintEngine10drawPointsEPK6QPointi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QPoint'),
               ('int', 'number', ''),
           )),
      ),
      'drawPolygon': (
          ('_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QPointF'),
               ('int', 'number', ''),
               ('int', 'enum', 'QtGui:QPaintEngine.PolygonDrawMode'),
           )),
          ('_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QPoint'),
               ('int', 'number', ''),
               ('int', 'enum', 'QtGui:QPaintEngine.PolygonDrawMode'),
           )),
      ),
      'drawPixmap': (
          ('_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'drawTextItem': (
          ('_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtGui:QTextItem'),
           )),
      ),
      'drawTiledPixmap': (
          ('_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPoint'
           'F',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'drawImage': (
          ('_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19'
           'ImageConversionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QImage'),
               ('address', 'value', 'QtCore:QRectF'),
               ('int', 'flags', 'QtCore:Qt.ImageConversionFlag'),
           )),
      ),
      'coordinateOffset': (
          ('_ZNK12QPaintEngine16coordinateOffsetEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
      'type': (
          ('_ZNK12QPaintEngine4typeEv',
           ('int', 'enum', 'QtGui:QPaintEngine.Type'),
           ()),
      ),
      'createPixmap': (
          ('_ZN12QPaintEngine12createPixmapE5QSize',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'createPixmapFromImage': (
          ('_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt19I'
           'mageConversionFlagEE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'value', 'QtGui:QImage'),
               ('int', 'flags', 'QtCore:Qt.ImageConversionFlag'),
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
    ritual = 'ritual_ZNK12QPaintEngine16coordinateOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QPaintEngine16coordinateOffsetEv'
    address = self.uglySide.call(ritual)
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
        self._addressOf(device, 'QPaintDevice'),
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
        self._addressOf(pdev, 'QPaintDevice'),
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
    ritual = 'ritual_ZN12QPaintEngine9drawRectsEPK5QRecti'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine9drawRectsEPK5QRecti'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

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
    ritual = 'ritual_ZN12QPaintEngine9drawRectsEPK6QRectFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine9drawRectsEPK6QRectFi'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

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
    ritual = 'ritual_ZN12QPaintEngine9drawLinesEPK5QLinei'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine9drawLinesEPK5QLinei'
    self.uglySide.call(ritual, self._addressOf(lines), lineCount)

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
    ritual = 'ritual_ZN12QPaintEngine9drawLinesEPK6QLineFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine9drawLinesEPK6QLineFi'
    self.uglySide.call(ritual, self._addressOf(lines), lineCount)

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
    ritual = 'ritual_ZN12QPaintEngine11drawEllipseERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine11drawEllipseERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(r))

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
    ritual = 'ritual_ZN12QPaintEngine11drawEllipseERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine11drawEllipseERK5QRect'
    self.uglySide.call(ritual, self._valueOf(r))

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
    ritual = 'ritual_ZN12QPaintEngine8drawPathERK12QPainterPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine8drawPathERK12QPainterPath'
    self.uglySide.call(ritual, self._valueOf(path))

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
    ritual = 'ritual_ZN12QPaintEngine10drawPointsEPK7QPointFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine10drawPointsEPK7QPointFi'
    self.uglySide.call(ritual, self._addressOf(points), pointCount)

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
    ritual = 'ritual_ZN12QPaintEngine10drawPointsEPK6QPointi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine10drawPointsEPK6QPointi'
    self.uglySide.call(ritual, self._addressOf(points), pointCount)

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
    ritual = (
        'ritual_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawMo'
        'deE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15Polygon'
          'DrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points), pointCount, mode.value,
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
    ritual = (
        'ritual_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawMod'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonD'
          'rawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points), pointCount, mode.value,
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
    ritual = 'ritual_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem')
    self.uglySide.call(ritual, self._valueOf(p), self._valueOf(textItem))

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
    ritual = (
        'ritual_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPo'
        'intF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmap'
          'RK7QPointF')
    self.uglySide.call(
        ritual, self._valueOf(r), self._valueOf(pixmap), self._valueOf(s),
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
    ritual = (
        'ritual_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Q'
        't19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFla'
          'gsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(
        ritual,
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
    ritual = 'ritual_ZN12QPaintEngine12createPixmapE5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPaintEngine12createPixmapE5QSize'
    address = self.uglySide.call(ritual, self._valueOf(size))
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
    ritual = (
        'ritual_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt'
        '19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlag'
          'sIN2Qt19ImageConversionFlagEE')
    address = self.uglySide.call(ritual, self._valueOf(image), flags.value)
    from . import QPixmap
    return QPixmap._cuteOwning(address)
