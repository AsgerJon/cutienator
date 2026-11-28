"""
QPicturePaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_pic_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPicturePaintEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QPaintEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from . import QImage, QPaintDevice, QPaintEngineState, QPainterPath
  from . import QPixmap, QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPaintDevice = WAIT['QPaintDevice']
  QPaintEngineState = WAIT['QPaintEngineState']
  QPainterPath = WAIT['QPainterPath']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTextItem = WAIT['QTextItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPicturePaintEngine(QPaintEngine):
  """
  The cute side of Qt's QPicturePaintEngine: a plain Python object standing
  in front of one C++ QPicturePaintEngine.

  It is built on the cute 'QPaintEngine', as Qt's QPicturePaintEngine is
  built on Qt's QPaintEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPicturePaintEngine that has a ritual and that
  Python can call so far, 11 names in all: 'begin', 'end', 'updateState',
  'drawEllipse', 'drawPath', 'drawPolygon', 'drawPixmap', 'drawTiledPixmap',
  'drawImage', 'drawTextItem', 'type'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPicturePaintEnginePrivate *QPicturePaintEngine::d_func()': gives
    'QPicturePaintEnginePrivate', which has no cute class yet.
  - Qt's 'const QPicturePaintEnginePrivate *QPicturePaintEngine::d_func()
    const': gives 'QPicturePaintEnginePrivate', which has no cute class yet.
  - Qt's 'QPicturePaintEngine::~QPicturePaintEngine()': the destructor:
    Python never removes a C++ QPicturePaintEngine.

  What has no ritual
  ------------------

  19 of the 33 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden.

  What to expect
  --------------

  - The C++ QPicturePaintEngine is created at the first use, not by
    'QPicturePaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPicturePaintEngine.
  - Each name of Qt's QPicturePaintEngine that has no cute function yet,
    '__init__', 'updateBackground', 'updateBrush', 'updateBrushOrigin',
    'updateClipEnabled', 'updateClipPath', 'updateClipRegion',
    'updateCompositionMode', 'updateFont', 'updateMatrix', 'updateOpacity',
    'updatePen', 'updateRenderHints', 'writeCmdLength', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPicturePaintEngine'

  #  A C++ QPicturePaintEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPicturePaintEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QPaintEngine.Type:
    """
    Calls Qt's 'Type QPicturePaintEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicturepaintengine.html#type

    Returns
    -------

    QPaintEngine.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPaintEngine.Type(number)' gives.
    """
    #  Type QPicturePaintEngine::type() const
    ritual = 'ritual_ZNK19QPicturePaintEngine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QPicturePaintEngine4typeEv'
    return QPaintEngine.Type(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QPicturePaintEngine::QPicturePaintEngine()': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: member access into incomplete type
      'QPicturePaintEnginePrivate'.
    - Qt's 'QPicturePaintEngine::QPicturePaintEngine(QPaintEnginePrivate
      &dptr)': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: member access into incomplete
      type 'QPicturePaintEnginePrivate'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.__init__' has no cute function yet. Qt's "
        "'QPicturePaintEngine::QPicturePaintEngine()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QPicturePaintEnginePrivate'. Qt's "
        "'QPicturePaintEngine::QPicturePaintEngine(QPaintEnginePrivate "
        "&dptr)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QPicturePaintEnginePrivate'.")

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
    Calls Qt's 'bool QPicturePaintEngine::begin(QPaintDevice *pdev)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicturepaintengine.html#begin

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPicturePaintEngine::begin(QPaintDevice *pdev)
    return self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine5beginEP12QPaintDevice',
        self._addressOf(pdev, 'QPaintDevice'),
    )

  def end(self) -> bool:
    """
    Calls Qt's 'bool QPicturePaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qpicturepaintengine.html#end
    """
    #  bool QPicturePaintEngine::end()
    ritual = 'ritual_ZN19QPicturePaintEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPicturePaintEngine3endEv'
    return self.uglySide.call(ritual)

  @overload(QPaintEngineState)
  def updateState(self, state: QPaintEngineState) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::updateState(const QPaintEngineState
    &state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpicturepaintengine.html#updateState

    Parameters
    ----------

    state : QPaintEngineState
      Passed on as a value: Qt reads the C++ QPaintEngineState, which stays
      Python's own.
    """
    #  void QPicturePaintEngine::updateState(const QPaintEngineState &state)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine11updateStateERK17QPaintEngineState',
        self._valueOf(state),
    )

  @overload(QRectF)
  def drawEllipse(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawEllipse(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpicturepaintengine.html#drawEllipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPicturePaintEngine::drawEllipse(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine11drawEllipseERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawPath(const QPainterPath
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicturepaintengine.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPicturePaintEngine::drawPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine8drawPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      numPoints: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawPolygon(const QPointF *points,
    int numPoints, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpicturepaintengine.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    numPoints : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QPicturePaintEngine::drawPolygon(const QPointF *points, int
    #      numPoints, PolygonDrawMode mode)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine11drawPolygonEPK7QPointFiN12QPaintEn'
        'gine15PolygonDrawModeE',
        self._addressOf(points, 'QPointF'), numPoints, mode.value,
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpicturepaintengine.html#drawPixmap

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
    #  void QPicturePaintEngine::drawPixmap(const QRectF &r, const QPixmap
    #      &pm, const QRectF &sr)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_',
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pixmap: QPixmap, s: QPointF) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawTiledPixmap(const QRectF &r,
    const QPixmap &pixmap, const QPointF &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpicturepaintengine.html#drawTiledPixmap

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
    #  void QPicturePaintEngine::drawTiledPixmap(const QRectF &r, const
    #      QPixmap &pixmap, const QPointF &s)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine15drawTiledPixmapERK6QRectFRK7QPixma'
        'pRK7QPointF',
        self._valueOf(r), self._valueOf(pixmap), self._valueOf(s, 'QPointF'),
    )

  @overload(QRectF, QImage, QRectF)
  @overload(QRectF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      r: QRectF,
      image: QImage,
      sr: QRectF,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawImage(const QRectF &r, const
    QImage &image, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicturepaintengine.html#drawImage

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPicturePaintEngine::drawImage(const QRectF &r, const QImage
    #      &image, const QRectF &sr, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine9drawImageERK6QRectFRK6QImageS2_6QFl'
        'agsIN2Qt19ImageConversionFlagEE',
        self._valueOf(r), self._valueOf(image), self._valueOf(sr),
        flags.value,
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, ti: QTextItem) -> None:
    """
    Calls Qt's 'void QPicturePaintEngine::drawTextItem(const QPointF &p,
    const QTextItem &ti)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpicturepaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ti : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPicturePaintEngine::drawTextItem(const QPointF &p, const
    #      QTextItem &ti)
    self.uglySide.call(
        'ritual_ZN19QPicturePaintEngine12drawTextItemERK7QPointFRK9QTextIte'
        'm',
        self._valueOf(p, 'QPointF'), self._valueOf(ti),
    )

  @staticmethod
  def updateBackground(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateBackground(Qt::BGMode bgmode, const
    QBrush &bgBrush)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateBackground' has no cute function yet. "
        "Qt's 'void QPicturePaintEngine::updateBackground(Qt::BGMode "
        "bgmode, const QBrush &bgBrush)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def updateBrush(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateBrush(const QBrush &brush)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateBrush' has no cute function yet. Qt's "
        "'void QPicturePaintEngine::updateBrush(const QBrush &brush)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'SERIALIZE_CMD'.")

  @staticmethod
  def updateBrushOrigin(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateBrushOrigin(const QPointF
    &origin)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateBrushOrigin' has no cute function yet. "
        "Qt's 'void QPicturePaintEngine::updateBrushOrigin(const QPointF "
        "&origin)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def updateClipEnabled(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateClipEnabled(bool enabled)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateClipEnabled' has no cute function yet. "
        "Qt's 'void QPicturePaintEngine::updateClipEnabled(bool enabled)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'SERIALIZE_CMD'.")

  @staticmethod
  def updateClipPath(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateClipPath(const QPainterPath &path,
    Qt::ClipOperation op)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateClipPath' has no cute function yet. "
        "Qt's 'void QPicturePaintEngine::updateClipPath(const QPainterPath "
        "&path, Qt::ClipOperation op)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def updateClipRegion(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateClipRegion(const QRegion &region,
    Qt::ClipOperation op)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateClipRegion' has no cute function yet. "
        "Qt's 'void QPicturePaintEngine::updateClipRegion(const QRegion "
        "&region, Qt::ClipOperation op)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def updateCompositionMode(*__, **_) -> Never:
    """
    Qt's 'void
    QPicturePaintEngine::updateCompositionMode(QPainter::CompositionMode
    cmode)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateCompositionMode' has no cute function "
        "yet. Qt's 'void "
        "QPicturePaintEngine::updateCompositionMode(QPainter::CompositionMod"
        "e cmode)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def updateFont(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateFont(const QFont &font)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateFont' has no cute function yet. Qt's "
        "'void QPicturePaintEngine::updateFont(const QFont &font)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'SERIALIZE_CMD'.")

  @staticmethod
  def updateMatrix(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateMatrix(const QTransform &matrix)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateMatrix' has no cute function yet. Qt's "
        "'void QPicturePaintEngine::updateMatrix(const QTransform "
        "&matrix)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def updateOpacity(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateOpacity(qreal opacity)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateOpacity' has no cute function yet. Qt's "
        "'void QPicturePaintEngine::updateOpacity(qreal opacity)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'SERIALIZE_CMD'.")

  @staticmethod
  def updatePen(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updatePen(const QPen &pen)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QPicturePaintEnginePrivate'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updatePen' has no cute function yet. Qt's "
        "'void QPicturePaintEngine::updatePen(const QPen &pen)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QPicturePaintEnginePrivate'.")

  @staticmethod
  def updateRenderHints(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::updateRenderHints(QPainter::RenderHints
    hints)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'SERIALIZE_CMD'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.updateRenderHints' has no cute function yet. "
        "Qt's 'void "
        "QPicturePaintEngine::updateRenderHints(QPainter::RenderHints "
        "hints)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'SERIALIZE_CMD'.")

  @staticmethod
  def writeCmdLength(*__, **_) -> Never:
    """
    Qt's 'void QPicturePaintEngine::writeCmdLength(int pos, const QRectF &r,
    bool corr)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QPicturePaintEnginePrivate'.
    """
    raise NotImplementedError(
        "'QPicturePaintEngine.writeCmdLength' has no cute function yet. "
        "Qt's 'void QPicturePaintEngine::writeCmdLength(int pos, const "
        "QRectF &r, bool corr)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QPicturePaintEnginePrivate'.")
