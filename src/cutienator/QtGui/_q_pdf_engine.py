"""
QPdfEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPdfEngine to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QPageLayout, QPaintDevice, QPaintEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QLineF, QMarginsF, QPointF, QRectF, QUrl
  from . import QImage, QPageSize, QPaintEngineState, QPainterPath
  from . import QPdfEnginePrivate, QPixmap, QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QImage = WAIT['QImage']
  QLineF = WAIT['QLineF']
  QMarginsF = WAIT['QMarginsF']
  QPageSize = WAIT['QPageSize']
  QPaintEngineState = WAIT['QPaintEngineState']
  QPainterPath = WAIT['QPainterPath']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTextItem = WAIT['QTextItem']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfEngine(QPaintEngine):
  """
  The cute side of Qt's QPdfEngine: a plain Python object standing in front
  of one C++ QPdfEngine.

  It is built on the cute 'QPaintEngine', as Qt's QPdfEngine is built on Qt's
  QPaintEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfEngine that has a ritual and that Python can
  call so far, 33 names in all: 'd_func', 'setOutputFilename',
  'setResolution', 'resolution', 'setPdfVersion', 'setDocumentXmpMetadata',
  'documentXmpMetadata', 'addFileAttachment', 'begin', 'end', 'drawPoints',
  'drawLines', 'drawRects', 'drawPolygon', 'drawPath', 'drawTextItem',
  'drawPixmap', 'drawImage', 'drawTiledPixmap', 'drawHyperlink',
  'updateState', 'metric', 'type', 'newPage', 'setPageLayout', 'setPageSize',
  'setPageOrientation', 'setPageMargins', 'pageLayout', 'setPen', 'setBrush',
  'setupGraphicsState', 'updateClipPath'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPdfEnginePrivate *QPdfEngine::d_func() const': takes in
    Python what 'QPdfEnginePrivate *QPdfEngine::d_func()' takes.
  - Qt's 'QPdfEngine::QPdfEngine(QPdfEnginePrivate &d)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QPdfEngine::~QPdfEngine()': the destructor: Python never removes a
    C++ QPdfEngine.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QPdfEngine is created at the first use, not by 'QPdfEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfEngine.
  - Each name of Qt's QPdfEngine that has no cute function yet, 'colorModel',
    'setColorModel', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QPdfEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ColorModel(CuteNum, scoped=True):
    """
    The enum 'QPdfEngine::ColorModel' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    RGB = Kee[int](0)
    Grayscale = Kee[int](1)
    CMYK = Kee[int](2)
    Auto = Kee[int](3)

  class PdfVersion(CuteNum):
    """
    The enum 'QPdfEngine::PdfVersion' of Qt, with the 4 names Qt gives in it.
    """

    Version_1_4 = Kee[int](0)
    Version_A1b = Kee[int](1)
    Version_1_6 = Kee[int](2)
    Version_X4 = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfEngine'

  #  A C++ QPdfEngine Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resolution(self) -> int:
    """
    Calls Qt's 'int QPdfEngine::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#resolution
    """
    #  int QPdfEngine::resolution() const
    return self.uglySide.call('ritual_ZNK10QPdfEngine10resolutionEv')

  def documentXmpMetadata(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QPdfEngine::documentXmpMetadata() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengine.html#documentXmpMetadata

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QPdfEngine::documentXmpMetadata() const
    address = self.uglySide.call(
        'ritual_ZNK10QPdfEngine19documentXmpMetadataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metricType: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPdfEngine::metric(QPaintDevice::PaintDeviceMetric
    metricType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#metric

    Parameters
    ----------

    metricType : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPdfEngine::metric(QPaintDevice::PaintDeviceMetric metricType)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QPdfEngine6metricEN12QPaintDevice17PaintDeviceMetricE',
        metricType.value,
    )

  def type(self) -> QPaintEngine.Type:
    """
    Calls Qt's 'Type QPdfEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#type

    Returns
    -------

    QPaintEngine.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPaintEngine.Type(number)' gives.
    """
    #  Type QPdfEngine::type() const
    ritual = 'ritual_ZNK10QPdfEngine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QPdfEngine4typeEv'
    return QPaintEngine.Type(self.uglySide.call(ritual))

  def pageLayout(self) -> QPageLayout:
    """
    Calls Qt's 'QPageLayout QPdfEngine::pageLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#pageLayout

    Returns
    -------

    QPageLayout
      A new cute QPageLayout around the copy Qt gave back. Python owns it.
    """
    #  QPageLayout QPdfEngine::pageLayout() const
    address = self.uglySide.call('ritual_ZNK10QPdfEngine10pageLayoutEv')
    return QPageLayout._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setOutputFilename(self, filename: str) -> None:
    """
    Calls Qt's 'void QPdfEngine::setOutputFilename(const QString &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setOutputFilename

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfEngine::setOutputFilename(const QString &filename)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine17setOutputFilenameERK7QString', filename,
    )

  @overload(int)
  def setResolution(self, resolution: int) -> None:
    """
    Calls Qt's 'void QPdfEngine::setResolution(int resolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setResolution

    Parameters
    ----------

    resolution : int
      Passed on as it is.
    """
    #  void QPdfEngine::setResolution(int resolution)
    self.uglySide.call('ritual_ZN10QPdfEngine13setResolutionEi', resolution)

  @overload(PdfVersion)
  def setPdfVersion(self, version: PdfVersion) -> None:
    """
    Calls Qt's 'void QPdfEngine::setPdfVersion(PdfVersion version)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setPdfVersion

    Parameters
    ----------

    version : PdfVersion
      Passed on as its number.
    """
    #  void QPdfEngine::setPdfVersion(PdfVersion version)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine13setPdfVersionENS_10PdfVersionE',
        version.value,
    )

  @overload(QByteArray)
  def setDocumentXmpMetadata(self, xmpMetadata: QByteArray) -> None:
    """
    Calls Qt's 'void QPdfEngine::setDocumentXmpMetadata(const QByteArray
    &xmpMetadata)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfengine.html#setDocumentXmpMetadata

    Parameters
    ----------

    xmpMetadata : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QPdfEngine::setDocumentXmpMetadata(const QByteArray &xmpMetadata)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine22setDocumentXmpMetadataERK10QByteArray',
        self._valueOf(xmpMetadata),
    )

  @overload(QPageLayout)
  def setPageLayout(self, pageLayout: QPageLayout) -> None:
    """
    Calls Qt's 'void QPdfEngine::setPageLayout(const QPageLayout
    &pageLayout)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setPageLayout

    Parameters
    ----------

    pageLayout : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.
    """
    #  void QPdfEngine::setPageLayout(const QPageLayout &pageLayout)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine13setPageLayoutERK11QPageLayout',
        self._valueOf(pageLayout),
    )

  @overload(QPageSize)
  def setPageSize(self, pageSize: QPageSize) -> None:
    """
    Calls Qt's 'void QPdfEngine::setPageSize(const QPageSize &pageSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setPageSize

    Parameters
    ----------

    pageSize : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  void QPdfEngine::setPageSize(const QPageSize &pageSize)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine11setPageSizeERK9QPageSize',
        self._valueOf(pageSize),
    )

  @overload(QPageLayout.Orientation)
  def setPageOrientation(self, orientation: QPageLayout.Orientation) -> None:
    """
    Calls Qt's 'void QPdfEngine::setPageOrientation(QPageLayout::Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setPageOrientation

    Parameters
    ----------

    orientation : QPageLayout.Orientation
      Passed on as its number.
    """
    #  void QPdfEngine::setPageOrientation(QPageLayout::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine18setPageOrientationEN11QPageLayout11Orientat'
        'ionE',
        orientation.value,
    )

  @overload(QMarginsF)
  @overload(QMarginsF, QPageLayout.Unit)
  def setPageMargins(
      self,
      margins: QMarginsF,
      units: QPageLayout.Unit = QPageLayout.Unit.Point,
  ) -> None:
    """
    Calls Qt's 'void QPdfEngine::setPageMargins(const QMarginsF &margins,
    QPageLayout::Unit units)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setPageMargins

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    units : QPageLayout.Unit
      Passed on as its number. May be left out, as in Qt: it is then
      QPageLayout.Unit.Point.
    """
    #  void QPdfEngine::setPageMargins(const QMarginsF &margins,
    #      QPageLayout::Unit units)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine14setPageMarginsERK9QMarginsFN11QPageLayout4U'
        'nitE',
        self._valueOf(margins), units.value,
    )

  def setPen(self) -> None:
    """
    Calls Qt's 'void QPdfEngine::setPen()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setPen
    """
    #  void QPdfEngine::setPen()
    self.uglySide.call('ritual_ZN10QPdfEngine6setPenEv')

  def setBrush(self) -> None:
    """
    Calls Qt's 'void QPdfEngine::setBrush()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setBrush
    """
    #  void QPdfEngine::setBrush()
    self.uglySide.call('ritual_ZN10QPdfEngine8setBrushEv')

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
    Notes what was given, for Qt's 'QPdfEngine::QPdfEngine()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#QPdfEngine
    """
    #  QPdfEngine::QPdfEngine()
    self._noteCreation(QPdfEngine, lambda: Rituals.call(
        'ritual_ZN10QPdfEngineC1Ev',
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

  def d_func(self) -> Optional[QPdfEnginePrivate]:
    """
    Calls Qt's 'QPdfEnginePrivate *QPdfEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#d_func

    Returns
    -------

    Optional[QPdfEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfEnginePrivate *QPdfEngine::d_func()
    address = self.uglySide.call('ritual_ZN10QPdfEngine6d_funcEv')
    from . import QPdfEnginePrivate
    return QPdfEnginePrivate._cuteAt(address)

  @overload(str, QByteArray, str)
  def addFileAttachment(
      self,
      fileName: str,
      data: QByteArray,
      mimeType: str,
  ) -> None:
    """
    Calls Qt's 'void QPdfEngine::addFileAttachment(const QString &fileName,
    const QByteArray &data, const QString &mimeType)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#addFileAttachment

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfEngine::addFileAttachment(const QString &fileName, const
    #      QByteArray &data, const QString &mimeType)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine17addFileAttachmentERK7QStringRK10QByteArrayS'
        '2_',
        fileName, self._valueOf(data), mimeType,
    )

  @overload(QPaintDevice)
  @overload(NoneType)
  def begin(self, pdev: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QPdfEngine::begin(QPaintDevice *pdev)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#begin

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPdfEngine::begin(QPaintDevice *pdev)
    ritual = 'ritual_ZN10QPdfEngine5beginEP12QPaintDevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine5beginEP12QPaintDevice'
    return self.uglySide.call(ritual, self._addressOf(pdev, 'QPaintDevice'))

  def end(self) -> bool:
    """
    Calls Qt's 'bool QPdfEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#end
    """
    #  bool QPdfEngine::end()
    ritual = 'ritual_ZN10QPdfEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine3endEv'
    return self.uglySide.call(ritual)

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawPoints(const QPointF *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawPoints

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPdfEngine::drawPoints(const QPointF *points, int pointCount)
    ritual = 'ritual_ZN10QPdfEngine10drawPointsEPK7QPointFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine10drawPointsEPK7QPointFi'
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount,
    )

  @overload(QLineF, int)
  @overload(NoneType, int)
  def drawLines(self, lines: Optional[QLineF], lineCount: int) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawLines(const QLineF *lines, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawLines

    Parameters
    ----------

    lines : Optional[QLineF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPdfEngine::drawLines(const QLineF *lines, int lineCount)
    ritual = 'ritual_ZN10QPdfEngine9drawLinesEPK6QLineFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine9drawLinesEPK6QLineFi'
    self.uglySide.call(ritual, self._addressOf(lines), lineCount)

  @overload(QRectF, int)
  @overload(NoneType, int)
  def drawRects(self, rects: Optional[QRectF], rectCount: int) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawRects(const QRectF *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawRects

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPdfEngine::drawRects(const QRectF *rects, int rectCount)
    ritual = 'ritual_ZN10QPdfEngine9drawRectsEPK6QRectFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine9drawRectsEPK6QRectFi'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawPolygon(const QPointF *points, int
    pointCount, PolygonDrawMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawPolygon

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
    #  void QPdfEngine::drawPolygon(const QPointF *points, int pointCount,
    #      PolygonDrawMode mode)
    ritual = (
        'ritual_ZN10QPdfEngine11drawPolygonEPK7QPointFiN12QPaintEngine15Pol'
        'ygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QPdfEngine11drawPolygonEPK7QPointFiN12QPaintEngin'
          'e15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPdfEngine::drawPath(const QPainterPath &path)
    ritual = 'ritual_ZN10QPdfEngine8drawPathERK12QPainterPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine8drawPathERK12QPainterPath'
    self.uglySide.call(ritual, self._valueOf(path))

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawTextItem(const QPointF &p, const
    QTextItem &textItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPdfEngine::drawTextItem(const QPointF &p, const QTextItem
    #      &textItem)
    ritual = 'ritual_ZN10QPdfEngine12drawTextItemERK7QPointFRK9QTextItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QPdfEngine12drawTextItemERK7QPointFRK9QTextItem')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(textItem),
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(
      self,
      rectangle: QRectF,
      pixmap: QPixmap,
      sr: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawPixmap(const QRectF &rectangle, const
    QPixmap &pixmap, const QRectF &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawPixmap

    Parameters
    ----------

    rectangle : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPdfEngine::drawPixmap(const QRectF &rectangle, const QPixmap
    #      &pixmap, const QRectF &sr)
    ritual = 'ritual_ZN10QPdfEngine10drawPixmapERK6QRectFRK7QPixmapS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine10drawPixmapERK6QRectFRK7QPixmapS2_'
    self.uglySide.call(
        ritual,
        self._valueOf(rectangle), self._valueOf(pixmap), self._valueOf(sr),
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
    Calls Qt's 'void QPdfEngine::drawImage(const QRectF &r, const QImage &pm,
    const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawImage

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
    #  void QPdfEngine::drawImage(const QRectF &r, const QImage &pm, const
    #      QRectF &sr, Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN10QPdfEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt1'
        '9ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QPdfEngine9drawImageERK6QRectFRK6QImageS2_6QFlags'
          'IN2Qt19ImageConversionFlagEE')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr), flags.value,
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(
      self,
      rectangle: QRectF,
      pixmap: QPixmap,
      point: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawTiledPixmap(const QRectF &rectangle,
    const QPixmap &pixmap, const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawTiledPixmap

    Parameters
    ----------

    rectangle : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPdfEngine::drawTiledPixmap(const QRectF &rectangle, const
    #      QPixmap &pixmap, const QPointF &point)
    ritual = (
        'ritual_ZN10QPdfEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPoin'
        'tF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QPdfEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK'
          '7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(rectangle), self._valueOf(pixmap), self._valueOf(point,
        'QPointF'),
    )

  @overload(QRectF, QUrl)
  def drawHyperlink(self, r: QRectF, url: QUrl) -> None:
    """
    Calls Qt's 'void QPdfEngine::drawHyperlink(const QRectF &r, const QUrl
    &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#drawHyperlink

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPdfEngine::drawHyperlink(const QRectF &r, const QUrl &url)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine13drawHyperlinkERK6QRectFRK4QUrl',
        self._valueOf(r), self._valueOf(url),
    )

  @overload(QPaintEngineState)
  def updateState(self, state: QPaintEngineState) -> None:
    """
    Calls Qt's 'void QPdfEngine::updateState(const QPaintEngineState
    &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#updateState

    Parameters
    ----------

    state : QPaintEngineState
      Passed on as a value: Qt reads the C++ QPaintEngineState, which stays
      Python's own.
    """
    #  void QPdfEngine::updateState(const QPaintEngineState &state)
    ritual = 'ritual_ZN10QPdfEngine11updateStateERK17QPaintEngineState'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPdfEngine11updateStateERK17QPaintEngineState'
    self.uglySide.call(ritual, self._valueOf(state))

  def newPage(self) -> bool:
    """
    Calls Qt's 'bool QPdfEngine::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#newPage
    """
    #  bool QPdfEngine::newPage()
    return self.uglySide.call('ritual_ZN10QPdfEngine7newPageEv')

  @overload(QPaintEngine.DirtyFlags)
  def setupGraphicsState(self, flags: QPaintEngine.DirtyFlags) -> None:
    """
    Calls Qt's 'void QPdfEngine::setupGraphicsState(QPaintEngine::DirtyFlags
    flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#setupGraphicsState

    Parameters
    ----------

    flags : QPaintEngine.DirtyFlags
      Passed on as its number.
    """
    #  void QPdfEngine::setupGraphicsState(QPaintEngine::DirtyFlags flags)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine18setupGraphicsStateE6QFlagsIN12QPaintEngine9'
        'DirtyFlagEE',
        flags.value,
    )

  @overload(QPainterPath, Qt.ClipOperation)
  def updateClipPath(self, path: QPainterPath, op: Qt.ClipOperation) -> None:
    """
    Calls Qt's 'void QPdfEngine::updateClipPath(const QPainterPath &path,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfengine.html#updateClipPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  void QPdfEngine::updateClipPath(const QPainterPath &path,
    #      Qt::ClipOperation op)
    self.uglySide.call(
        'ritual_ZN10QPdfEngine14updateClipPathERK12QPainterPathN2Qt13ClipOp'
        'erationE',
        self._valueOf(path), op.value,
    )

  @staticmethod
  def colorModel(*__, **_) -> Never:
    """
    Qt's 'ColorModel QPdfEngine::colorModel() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QPdfEngine.colorModel' has no cute function yet. Qt's 'ColorModel "
        "QPdfEngine::colorModel() const': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setColorModel(*__, **_) -> Never:
    """
    Qt's 'void QPdfEngine::setColorModel(ColorModel model)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QPdfEngine.setColorModel' has no cute function yet. Qt's 'void "
        "QPdfEngine::setColorModel(ColorModel model)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
