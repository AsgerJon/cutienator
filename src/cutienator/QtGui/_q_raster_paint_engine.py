"""
QRasterPaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QRasterPaintEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPaintEngine, QPaintEngineEx

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF
  from . import QBrush, QClipData, QColor, QFontEngine, QImage, QPaintDevice
  from . import QPainterPath, QPainterState, QPen, QPixmap, QRasterBuffer
  from . import QRasterPaintEnginePrivate, QRasterPaintEngineState, QRegion
  from . import QSpanData, QStaticTextItem, QTextItem, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFontEngine = WAIT['QFontEngine']
  QImage = WAIT['QImage']
  QLine = WAIT['QLine']
  QLineF = WAIT['QLineF']
  QPaintDevice = WAIT['QPaintDevice']
  QPainterPath = WAIT['QPainterPath']
  QPainterState = WAIT['QPainterState']
  QPen = WAIT['QPen']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QSpanData = WAIT['QSpanData']
  QStaticTextItem = WAIT['QStaticTextItem']
  QTextItem = WAIT['QTextItem']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRasterPaintEngine(QPaintEngineEx):
  """
  The cute side of Qt's QRasterPaintEngine: a plain Python object standing in
  front of one C++ QRasterPaintEngine.

  It is built on the cute 'QPaintEngineEx', as Qt's QRasterPaintEngine is
  built on Qt's QPaintEngineEx, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRasterPaintEngine that has a ritual and that Python
  can call so far, 49 names in all: 'd_func', 'begin', 'end', 'penChanged',
  'brushChanged', 'brushOriginChanged', 'opacityChanged',
  'compositionModeChanged', 'renderHintsChanged', 'transformChanged',
  'clipEnabledChanged', 'setState', 'createState', 'state', 'updateBrush',
  'updatePen', 'updateMatrix', 'fillPath', 'fillPolygon', 'drawPolygon',
  'drawEllipse', 'fillRect', 'drawRects', 'drawPixmap', 'drawImage',
  'drawTiledPixmap', 'drawTextItem', 'drawLines', 'drawPoints', 'clip',
  'clipData', 'drawStaticTextItem', 'clipType', 'clipBoundingRect',
  'rasterBuffer', 'type', 'coordinateOffset',
  'requiresPretransformedGlyphPositions', 'shouldDrawCachedGlyphs', 'init',
  'drawBitmap', 'setClipRectInDeviceCoords', 'toNormalizedFillRect',
  'ensureBrush', 'ensurePen', 'updateOutlineMapper', 'ensureOutlineMapper',
  'updateRasterState', 'ensureRasterState'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRasterPaintEnginePrivate *QRasterPaintEngine::d_func()
    const': takes in Python what 'QRasterPaintEnginePrivate
    *QRasterPaintEngine::d_func()' takes.
  - Qt's 'QRasterPaintEngine::~QRasterPaintEngine()': the destructor: Python
    never removes a C++ QRasterPaintEngine.
  - Qt's 'const QRasterPaintEngineState *QRasterPaintEngine::state() const':
    takes in Python what 'QRasterPaintEngineState
    *QRasterPaintEngine::state()' takes.
  - Qt's 'void QRasterPaintEngine::stroke(const QVectorPath &path, const QPen
    &pen)': takes a type Python has no way to hand over yet.
  - Qt's 'void QRasterPaintEngine::fill(const QVectorPath &path, const QBrush
    &brush)': takes a type Python has no way to hand over yet.
  - Qt's 'void QRasterPaintEngine::clip(const QVectorPath &path,
    Qt::ClipOperation op)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QRasterPaintEngine::drawCachedGlyphs(int numGlyphs, const
    glyph_t *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)':
    names 'glyph_t', which has no cute class yet.
  - Qt's 'void QRasterPaintEngine::alphaPenBlt(const void *src, int bpl, int
    depth, int rx, int ry, int w, int h, bool useGammaCorrection)': names
    'void', which has no cute class yet.
  - Qt's 'QRasterPaintEngine::QRasterPaintEngine(QRasterPaintEnginePrivate
    &d, QPaintDevice *a1)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QRasterPaintEngine is created at the first use, not by
    'QRasterPaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRasterPaintEngine.
  - Each name of Qt's QRasterPaintEngine that has no cute function yet,
    'alphaPenBlt', 'drawCachedGlyphs', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRasterPaintEngine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ClipType(CuteNum):
    """
    The enum 'QRasterPaintEngine::ClipType' of Qt, with the 2 names Qt gives
    in it.
    """

    RectClip = Kee[int](0)
    ComplexClip = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterPaintEngine'

  #  A C++ QRasterPaintEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRasterPaintEngine'

  #  The functions Qt calls itself that QRasterPaintEngine is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'drawCachedGlyphs': (
          'bool QRasterPaintEngine::drawCachedGlyphs(int, const glyph_t *, '
          'const QFixedPoint *, QFontEngine *)',
      ),
  }

  #  The functions Qt calls itself that QRasterPaintEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'fillPath': (
          ('_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSpanData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPainterPath'),
               ('address', 'address', 'QtGui:QSpanData'),
           )),
      ),
      'fillPolygon': (
          ('_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine'
           '15PolygonDrawModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QPointF'),
               ('int', 'number', ''),
               ('int', 'enum', 'QtGui:QPaintEngine.PolygonDrawMode'),
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

  @overload(QPainterState)
  @overload(NoneType)
  def createState(
      self,
      orig: Optional[QPainterState],
  ) -> Optional[QPainterState]:
    """
    Calls Qt's 'QPainterState *QRasterPaintEngine::createState(QPainterState
    *orig) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#createState

    Parameters
    ----------

    orig : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPainterState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterState *QRasterPaintEngine::createState(QPainterState *orig)
    #      const
    ritual = 'ritual_ZNK18QRasterPaintEngine11createStateEP13QPainterState'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QRasterPaintEngine11createStateEP13QPainterState')
    address = self.uglySide.call(ritual, self._addressOf(orig))
    from . import QPainterState
    return QPainterState._cuteAt(address)

  def clipData(self) -> Optional[QClipData]:
    """
    Calls Qt's 'const QClipData *QRasterPaintEngine::clipData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#clipData

    Returns
    -------

    Optional[QClipData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QClipData *QRasterPaintEngine::clipData() const
    address = self.uglySide.call('ritual_ZNK18QRasterPaintEngine8clipDataEv')
    from . import QClipData
    return QClipData._cuteAt(address)

  def clipType(self) -> ClipType:
    """
    Calls Qt's 'ClipType QRasterPaintEngine::clipType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#clipType

    Returns
    -------

    ClipType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClipType(number)' gives.
    """
    #  ClipType QRasterPaintEngine::clipType() const
    return QRasterPaintEngine.ClipType(self.uglySide.call(
        'ritual_ZNK18QRasterPaintEngine8clipTypeEv',
    ))

  def clipBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QRasterPaintEngine::clipBoundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#clipBoundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRasterPaintEngine::clipBoundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QRasterPaintEngine16clipBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def type(self) -> QPaintEngine.Type:
    """
    Calls Qt's 'Type QRasterPaintEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#type

    Returns
    -------

    QPaintEngine.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPaintEngine.Type(number)' gives.
    """
    #  Type QRasterPaintEngine::type() const
    ritual = 'ritual_ZNK18QRasterPaintEngine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QRasterPaintEngine4typeEv'
    return QPaintEngine.Type(self.uglySide.call(ritual))

  def coordinateOffset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QRasterPaintEngine::coordinateOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#coordinateOffset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QRasterPaintEngine::coordinateOffset() const
    ritual = 'ritual_ZNK18QRasterPaintEngine16coordinateOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QRasterPaintEngine16coordinateOffsetEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QFontEngine, QTransform)
  @overload(NoneType, QTransform)
  def requiresPretransformedGlyphPositions(
      self,
      fontEngine: Optional[QFontEngine],
      m: QTransform,
  ) -> bool:
    """
    Calls Qt's 'bool
    QRasterPaintEngine::requiresPretransformedGlyphPositions(QFontEngine
    *fontEngine, const QTransform &m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QRasterPaintEngine::requiresPretransformedGlyphPositions(
    #      QFontEngine *fontEngine, const QTransform &m) const
    ritual = (
        'ritual_ZNK18QRasterPaintEngine36requiresPretransformedGlyphPositio'
        'nsEP11QFontEngineRK10QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QRasterPaintEngine36requiresPretransformedGlyphP'
          'ositionsEP11QFontEngineRK10QTransform')
    return self.uglySide.call(
        ritual, self._addressOf(fontEngine), self._valueOf(m),
    )

  @overload(QFontEngine, QTransform)
  @overload(NoneType, QTransform)
  def shouldDrawCachedGlyphs(
      self,
      fontEngine: Optional[QFontEngine],
      m: QTransform,
  ) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEngine::shouldDrawCachedGlyphs(QFontEngine
    *fontEngine, const QTransform &m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#shouldDrawCachedGlyphs

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QRasterPaintEngine::shouldDrawCachedGlyphs(QFontEngine
    #      *fontEngine, const QTransform &m) const
    ritual = (
        'ritual_ZNK18QRasterPaintEngine22shouldDrawCachedGlyphsEP11QFontEng'
        'ineRK10QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QRasterPaintEngine22shouldDrawCachedGlyphsEP11QF'
          'ontEngineRK10QTransform')
    return self.uglySide.call(
        ritual, self._addressOf(fontEngine), self._valueOf(m),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainterState)
  @overload(NoneType)
  def setState(self, s: Optional[QPainterState]) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::setState(QPainterState *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#setState

    Parameters
    ----------

    s : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRasterPaintEngine::setState(QPainterState *s)
    ritual = 'ritual_ZN18QRasterPaintEngine8setStateEP13QPainterState'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine8setStateEP13QPainterState'
    self.uglySide.call(ritual, self._addressOf(s))

  @overload(QRect, Qt.ClipOperation)
  def setClipRectInDeviceCoords(
      self,
      r: QRect,
      op: Qt.ClipOperation,
  ) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEngine::setClipRectInDeviceCoords(const
    QRect &r, Qt::ClipOperation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#setClipRectInDeviceCoords

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  bool QRasterPaintEngine::setClipRectInDeviceCoords(const QRect &r,
    #      Qt::ClipOperation op)
    return self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine25setClipRectInDeviceCoordsERK5QRectN'
        '2Qt13ClipOperationE',
        self._valueOf(r), op.value,
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

  @overload(QPaintDevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QPaintDevice]) -> None:
    """
    Notes what was given, for Qt's
    'QRasterPaintEngine::QRasterPaintEngine(QPaintDevice *device)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#QRasterPaintEngine

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRasterPaintEngine::QRasterPaintEngine(QPaintDevice *device)
    self._noteCreation(QRasterPaintEngine, lambda: Rituals.call(
        'ritual_ZN18QRasterPaintEngineC1EP12QPaintDevice',
        self._addressOf(device, 'QPaintDevice'),
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

  def d_func(self) -> Optional[QRasterPaintEnginePrivate]:
    """
    Calls Qt's 'QRasterPaintEnginePrivate *QRasterPaintEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#d_func

    Returns
    -------

    Optional[QRasterPaintEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRasterPaintEnginePrivate *QRasterPaintEngine::d_func()
    address = self.uglySide.call('ritual_ZN18QRasterPaintEngine6d_funcEv')
    from . import QRasterPaintEnginePrivate
    return QRasterPaintEnginePrivate._cuteAt(address)

  @overload(QPaintDevice)
  @overload(NoneType)
  def begin(self, device: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEngine::begin(QPaintDevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#begin

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRasterPaintEngine::begin(QPaintDevice *device)
    ritual = 'ritual_ZN18QRasterPaintEngine5beginEP12QPaintDevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine5beginEP12QPaintDevice'
    return self.uglySide.call(
        ritual, self._addressOf(device, 'QPaintDevice'),
    )

  def end(self) -> bool:
    """
    Calls Qt's 'bool QRasterPaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#end
    """
    #  bool QRasterPaintEngine::end()
    ritual = 'ritual_ZN18QRasterPaintEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine3endEv'
    return self.uglySide.call(ritual)

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#penChanged
    """
    #  void QRasterPaintEngine::penChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine10penChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine10penChangedEv'
    self.uglySide.call(ritual)

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::brushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#brushChanged
    """
    #  void QRasterPaintEngine::brushChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine12brushChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine12brushChangedEv'
    self.uglySide.call(ritual)

  def brushOriginChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::brushOriginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#brushOriginChanged
    """
    #  void QRasterPaintEngine::brushOriginChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine18brushOriginChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine18brushOriginChangedEv'
    self.uglySide.call(ritual)

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#opacityChanged
    """
    #  void QRasterPaintEngine::opacityChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine14opacityChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine14opacityChangedEv'
    self.uglySide.call(ritual)

  def compositionModeChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::compositionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#compositionModeChanged
    """
    #  void QRasterPaintEngine::compositionModeChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine22compositionModeChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine22compositionModeChangedEv'
    self.uglySide.call(ritual)

  def renderHintsChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::renderHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#renderHintsChanged
    """
    #  void QRasterPaintEngine::renderHintsChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine18renderHintsChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine18renderHintsChangedEv'
    self.uglySide.call(ritual)

  def transformChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::transformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#transformChanged
    """
    #  void QRasterPaintEngine::transformChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine16transformChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine16transformChangedEv'
    self.uglySide.call(ritual)

  def clipEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::clipEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#clipEnabledChanged
    """
    #  void QRasterPaintEngine::clipEnabledChanged()
    ritual = 'ritual_ZN18QRasterPaintEngine18clipEnabledChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine18clipEnabledChangedEv'
    self.uglySide.call(ritual)

  def state(self) -> Optional[QRasterPaintEngineState]:
    """
    Calls Qt's 'QRasterPaintEngineState *QRasterPaintEngine::state()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#state

    Returns
    -------

    Optional[QRasterPaintEngineState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRasterPaintEngineState *QRasterPaintEngine::state()
    address = self.uglySide.call('ritual_ZN18QRasterPaintEngine5stateEv')
    from . import QRasterPaintEngineState
    return QRasterPaintEngineState._cuteAt(address)

  @overload(QBrush)
  def updateBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::updateBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#updateBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::updateBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine11updateBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def updatePen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::updatePen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#updatePen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QRasterPaintEngine::updatePen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine9updatePenERK4QPen',
        self._valueOf(pen),
    )

  @overload(QTransform)
  def updateMatrix(self, matrix: QTransform) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::updateMatrix(const QTransform
    &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#updateMatrix

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::updateMatrix(const QTransform &matrix)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine12updateMatrixERK10QTransform',
        self._valueOf(matrix),
    )

  @overload(QPainterPath, QSpanData)
  @overload(QPainterPath, NoneType)
  def fillPath(
      self,
      path: QPainterPath,
      fillData: Optional[QSpanData],
  ) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::fillPath(const QPainterPath &path,
    QSpanData *fillData)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#fillPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    fillData : Optional[QSpanData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRasterPaintEngine::fillPath(const QPainterPath &path, QSpanData
    #      *fillData)
    ritual = (
        'ritual_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSpanData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSp'
          'anData')
    self.uglySide.call(
        ritual, self._valueOf(path), self._addressOf(fillData),
    )

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def fillPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::fillPolygon(const QPointF *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#fillPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QRasterPaintEngine::fillPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEng'
        'ine15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPa'
          'intEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawPolygon(const QPointF *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QRasterPaintEngine::drawPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN18QRasterPaintEngine11drawPolygonEPK7QPointFiN12QPaintEng'
        'ine15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine11drawPolygonEPK7QPointFiN12QPa'
          'intEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QPoint, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPoint],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawPolygon(const QPoint *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QRasterPaintEngine::drawPolygon(const QPoint *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN18QRasterPaintEngine11drawPolygonEPK6QPointiN12QPaintEngi'
        'ne15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine11drawPolygonEPK6QPointiN12QPai'
          'ntEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points), pointCount, mode.value,
    )

  @overload(QRectF)
  def drawEllipse(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawEllipse(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#drawEllipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::drawEllipse(const QRectF &rect)
    ritual = 'ritual_ZN18QRasterPaintEngine11drawEllipseERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine11drawEllipseERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF, QBrush)
  def fillRect(self, rect: QRectF, brush: QBrush) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::fillRect(const QRectF &rect, const
    QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::fillRect(const QRectF &rect, const QBrush
    #      &brush)
    ritual = 'ritual_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QBrush'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QBrush')
    self.uglySide.call(ritual, self._valueOf(rect), self._valueOf(brush))

  @overload(QRectF, QColor)
  def fillRect(self, rect: QRectF, color: QColor) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::fillRect(const QRectF &rect, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::fillRect(const QRectF &rect, const QColor
    #      &color)
    ritual = 'ritual_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QColor')
    self.uglySide.call(ritual, self._valueOf(rect), self._valueOf(color))

  @overload(QRectF, QSpanData)
  @overload(QRectF, NoneType)
  def fillRect(self, rect: QRectF, data: Optional[QSpanData]) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::fillRect(const QRectF &rect,
    QSpanData *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    data : Optional[QSpanData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRasterPaintEngine::fillRect(const QRectF &rect, QSpanData *data)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine8fillRectERK6QRectFP9QSpanData',
        self._valueOf(rect), self._addressOf(data),
    )

  @overload(QRect, int)
  @overload(NoneType, int)
  def drawRects(self, rects: Optional[QRect], rectCount: int) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawRects(const QRect *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QRasterPaintEngine::drawRects(const QRect *rects, int rectCount)
    ritual = 'ritual_ZN18QRasterPaintEngine9drawRectsEPK5QRecti'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine9drawRectsEPK5QRecti'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QRectF, int)
  def drawRects(self, rects: Optional[QRectF], rectCount: int) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawRects(const QRectF *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QRasterPaintEngine::drawRects(const QRectF *rects, int rectCount)
    ritual = 'ritual_ZN18QRasterPaintEngine9drawRectsEPK6QRectFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine9drawRectsEPK6QRectFi'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QPointF, QPixmap)
  def drawPixmap(self, p: QPointF, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawPixmap(const QPointF &p, const
    QPixmap &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawPixmap

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::drawPixmap(const QPointF &p, const QPixmap
    #      &pm)
    ritual = 'ritual_ZN18QRasterPaintEngine10drawPixmapERK7QPointFRK7QPixmap'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine10drawPixmapERK7QPointFRK7QPixm'
          'ap')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(pm),
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawPixmap

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
    #  void QRasterPaintEngine::drawPixmap(const QRectF &r, const QPixmap
    #      &pm, const QRectF &sr)
    ritual = (
        'ritual_ZN18QRasterPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine10drawPixmapERK6QRectFRK7QPixma'
          'pS2_')
    self.uglySide.call(
        ritual, self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPointF, QImage)
  def drawImage(self, p: QPointF, img: QImage) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawImage(const QPointF &p, const
    QImage &img)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawImage

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    img : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::drawImage(const QPointF &p, const QImage
    #      &img)
    ritual = 'ritual_ZN18QRasterPaintEngine9drawImageERK7QPointFRK6QImage'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine9drawImageERK7QPointFRK6QImage')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(img),
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
    Calls Qt's 'void QRasterPaintEngine::drawImage(const QRectF &r, const
    QImage &pm, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawImage

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
    #  void QRasterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
    #      const QRectF &sr, Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN18QRasterPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFla'
        'gsIN2Qt19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine9drawImageERK6QRectFRK6QImageS2'
          '_6QFlagsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr), flags.value,
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pm: QPixmap, sr: QPointF) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawTiledPixmap(const QRectF &r,
    const QPixmap &pm, const QPointF &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#drawTiledPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::drawTiledPixmap(const QRectF &r, const
    #      QPixmap &pm, const QPointF &sr)
    ritual = (
        'ritual_ZN18QRasterPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmap'
        'RK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine15drawTiledPixmapERK6QRectFRK7Q'
          'PixmapRK7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr, 'QPointF'),
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawTextItem(const QPointF &p, const
    QTextItem &textItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::drawTextItem(const QPointF &p, const
    #      QTextItem &textItem)
    ritual = (
        'ritual_ZN18QRasterPaintEngine12drawTextItemERK7QPointFRK9QTextItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine12drawTextItemERK7QPointFRK9QTe'
          'xtItem')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(textItem),
    )

  @overload(QLine, int)
  @overload(NoneType, int)
  def drawLines(self, line: Optional[QLine], lineCount: int) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawLines(const QLine *line, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawLines

    Parameters
    ----------

    line : Optional[QLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QRasterPaintEngine::drawLines(const QLine *line, int lineCount)
    ritual = 'ritual_ZN18QRasterPaintEngine9drawLinesEPK5QLinei'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine9drawLinesEPK5QLinei'
    self.uglySide.call(ritual, self._addressOf(line), lineCount)

  @overload(QLineF, int)
  def drawLines(self, line: Optional[QLineF], lineCount: int) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawLines(const QLineF *line, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawLines

    Parameters
    ----------

    line : Optional[QLineF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QRasterPaintEngine::drawLines(const QLineF *line, int lineCount)
    ritual = 'ritual_ZN18QRasterPaintEngine9drawLinesEPK6QLineFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine9drawLinesEPK6QLineFi'
    self.uglySide.call(ritual, self._addressOf(line), lineCount)

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawPoints(const QPointF *points,
    int pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QRasterPaintEngine::drawPoints(const QPointF *points, int
    #      pointCount)
    ritual = 'ritual_ZN18QRasterPaintEngine10drawPointsEPK7QPointFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine10drawPointsEPK7QPointFi'
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount,
    )

  @overload(QPoint, int)
  def drawPoints(self, points: Optional[QPoint], pointCount: int) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawPoints(const QPoint *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QRasterPaintEngine::drawPoints(const QPoint *points, int
    #      pointCount)
    ritual = 'ritual_ZN18QRasterPaintEngine10drawPointsEPK6QPointi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRasterPaintEngine10drawPointsEPK6QPointi'
    self.uglySide.call(ritual, self._addressOf(points), pointCount)

  @overload(QRect, Qt.ClipOperation)
  def clip(self, rect: QRect, op: Qt.ClipOperation) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::clip(const QRect &rect,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#clip

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  void QRasterPaintEngine::clip(const QRect &rect, Qt::ClipOperation op)
    ritual = (
        'ritual_ZN18QRasterPaintEngine4clipERK5QRectN2Qt13ClipOperationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine4clipERK5QRectN2Qt13ClipOperati'
          'onE')
    self.uglySide.call(ritual, self._valueOf(rect), op.value)

  @overload(QRegion, Qt.ClipOperation)
  def clip(self, region: QRegion, op: Qt.ClipOperation) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::clip(const QRegion &region,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#clip

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  void QRasterPaintEngine::clip(const QRegion &region, Qt::ClipOperation
    #      op)
    ritual = (
        'ritual_ZN18QRasterPaintEngine4clipERK7QRegionN2Qt13ClipOperationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine4clipERK7QRegionN2Qt13ClipOpera'
          'tionE')
    self.uglySide.call(ritual, self._valueOf(region), op.value)

  @overload(QStaticTextItem)
  @overload(NoneType)
  def drawStaticTextItem(self, textItem: Optional[QStaticTextItem]) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawStaticTextItem(QStaticTextItem
    *textItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#drawStaticTextItem

    Parameters
    ----------

    textItem : Optional[QStaticTextItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRasterPaintEngine::drawStaticTextItem(QStaticTextItem *textItem)
    ritual = (
        'ritual_ZN18QRasterPaintEngine18drawStaticTextItemEP15QStaticTextIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRasterPaintEngine18drawStaticTextItemEP15QStatic'
          'TextItem')
    self.uglySide.call(ritual, self._addressOf(textItem))

  def rasterBuffer(self) -> Optional[QRasterBuffer]:
    """
    Calls Qt's 'QRasterBuffer *QRasterPaintEngine::rasterBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#rasterBuffer

    Returns
    -------

    Optional[QRasterBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRasterBuffer *QRasterPaintEngine::rasterBuffer()
    address = self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine12rasterBufferEv',
    )
    from . import QRasterBuffer
    return QRasterBuffer._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#init
    """
    #  void QRasterPaintEngine::init()
    self.uglySide.call('ritual_ZN18QRasterPaintEngine4initEv')

  @overload(QPointF, QImage, QSpanData)
  @overload(QPointF, QImage, NoneType)
  def drawBitmap(
      self,
      pos: QPointF,
      image: QImage,
      fill: Optional[QSpanData],
  ) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::drawBitmap(const QPointF &pos, const
    QImage &image, QSpanData *fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#drawBitmap

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    fill : Optional[QSpanData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRasterPaintEngine::drawBitmap(const QPointF &pos, const QImage
    #      &image, QSpanData *fill)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine10drawBitmapERK7QPointFRK6QImageP9QSp'
        'anData',
        self._valueOf(pos, 'QPointF'), self._valueOf(image),
        self._addressOf(fill),
    )

  @overload(QRectF)
  def toNormalizedFillRect(self, rect: QRectF) -> QRect:
    """
    Calls Qt's 'QRect QRasterPaintEngine::toNormalizedFillRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#toNormalizedFillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QRasterPaintEngine::toNormalizedFillRect(const QRectF &rect)
    address = self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine20toNormalizedFillRectERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QBrush)
  def ensureBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::ensureBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#ensureBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QRasterPaintEngine::ensureBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine11ensureBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload()
  def ensureBrush(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::ensureBrush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#ensureBrush
    """
    #  void QRasterPaintEngine::ensureBrush()
    self.uglySide.call('ritual_ZN18QRasterPaintEngine11ensureBrushEv')

  @overload(QPen)
  def ensurePen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::ensurePen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#ensurePen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QRasterPaintEngine::ensurePen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine9ensurePenERK4QPen',
        self._valueOf(pen),
    )

  @overload()
  def ensurePen(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::ensurePen()'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterpaintengine.html#ensurePen
    """
    #  void QRasterPaintEngine::ensurePen()
    self.uglySide.call('ritual_ZN18QRasterPaintEngine9ensurePenEv')

  def updateOutlineMapper(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::updateOutlineMapper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#updateOutlineMapper
    """
    #  void QRasterPaintEngine::updateOutlineMapper()
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine19updateOutlineMapperEv',
    )

  def ensureOutlineMapper(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::ensureOutlineMapper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#ensureOutlineMapper
    """
    #  void QRasterPaintEngine::ensureOutlineMapper()
    self.uglySide.call(
        'ritual_ZN18QRasterPaintEngine19ensureOutlineMapperEv',
    )

  def updateRasterState(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::updateRasterState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#updateRasterState
    """
    #  void QRasterPaintEngine::updateRasterState()
    self.uglySide.call('ritual_ZN18QRasterPaintEngine17updateRasterStateEv')

  def ensureRasterState(self) -> None:
    """
    Calls Qt's 'void QRasterPaintEngine::ensureRasterState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrasterpaintengine.html#ensureRasterState
    """
    #  void QRasterPaintEngine::ensureRasterState()
    self.uglySide.call('ritual_ZN18QRasterPaintEngine17ensureRasterStateEv')

  @staticmethod
  def alphaPenBlt(*__, **_) -> Never:
    """
    Qt's 'void QRasterPaintEngine::alphaPenBlt(const void *src, int bpl, int
    depth, int rx, int ry, int w, int h, bool useGammaCorrection)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRasterPaintEngine.alphaPenBlt' has no cute function yet. Qt's "
        "'void QRasterPaintEngine::alphaPenBlt(const void *src, int bpl, "
        "int depth, int rx, int ry, int w, int h, bool "
        "useGammaCorrection)': names 'void', which has no cute class yet.")

  @staticmethod
  def drawCachedGlyphs(*__, **_) -> Never:
    """
    Qt's 'bool QRasterPaintEngine::drawCachedGlyphs(int numGlyphs, const
    glyph_t *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)':
    names 'glyph_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRasterPaintEngine.drawCachedGlyphs' has no cute function yet. "
        "Qt's 'bool QRasterPaintEngine::drawCachedGlyphs(int numGlyphs, "
        "const glyph_t *glyphs, const QFixedPoint *positions, QFontEngine "
        "*fontEngine)': names 'glyph_t', which has no cute class yet.")
