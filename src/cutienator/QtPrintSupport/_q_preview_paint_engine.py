"""
QPreviewPaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_preview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPreviewPaintEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QPaintDevice, QPaintEngine
from . import QPrintEngine, QPrinter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF, QVariant
  from ..QtGui import QPaintEngineState, QPainterPath, QPixmap, QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEngineState = WAIT['QPaintEngineState']
  QPainterPath = WAIT['QPainterPath']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTextItem = WAIT['QTextItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPreviewPaintEngine(QPaintEngine, QPrintEngine):
  """
  The cute side of Qt's QPreviewPaintEngine: a plain Python object standing
  in front of one C++ QPreviewPaintEngine.

  It is built on the cute 'QPaintEngine', as Qt's QPreviewPaintEngine is
  built on Qt's QPaintEngine, and has everything that class has. It is built
  on the cute 'QPrintEngine' as well, as Qt's QPreviewPaintEngine is built on
  Qt's QPrintEngine too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPreviewPaintEngine that has a ritual and that
  Python can call so far, 15 names in all: 'begin', 'end', 'updateState',
  'drawPath', 'drawPolygon', 'drawTextItem', 'drawPixmap', 'drawTiledPixmap',
  'type', 'setProperty', 'property', 'newPage', 'abort', 'metric',
  'printerState'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPreviewPaintEnginePrivate *QPreviewPaintEngine::d_func()': gives
    'QPreviewPaintEnginePrivate', which has no cute class yet.
  - Qt's 'const QPreviewPaintEnginePrivate *QPreviewPaintEngine::d_func()
    const': gives 'QPreviewPaintEnginePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPreviewPaintEngine is created at the first use, not by
    'QPreviewPaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPreviewPaintEngine.
  - Each name of Qt's QPreviewPaintEngine that has no cute function yet,
    '__init__', 'pages', 'setProxyEngines', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPreviewPaintEngine'

  #  Qt's QPreviewPaintEngine is built on more than one class. The part of a
  #  C++ QPreviewPaintEngine that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QPrintEngine': 'ritual_cast_QPreviewPaintEngine_QPrintEngine',
  }

  #  A C++ QPreviewPaintEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPreviewPaintEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QPaintEngine.Type:
    """
    Calls Qt's 'QPaintEngine::Type QPreviewPaintEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#type

    Returns
    -------

    QPaintEngine.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPaintEngine.Type(number)' gives.
    """
    #  QPaintEngine::Type QPreviewPaintEngine::type() const
    ritual = 'ritual_ZNK19QPreviewPaintEngine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QPreviewPaintEngine4typeEv'
    return QPaintEngine.Type(self.uglySide.call(ritual))

  @overload(QPrintEngine.PrintEnginePropertyKey)
  def property(self, key: QPrintEngine.PrintEnginePropertyKey) -> QVariant:
    """
    Calls Qt's 'QVariant QPreviewPaintEngine::property(PrintEnginePropertyKey
    key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#property

    Parameters
    ----------

    key : QPrintEngine.PrintEnginePropertyKey
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPreviewPaintEngine::property(PrintEnginePropertyKey key)
    #      const
    ritual = (
        'ritual_ZNK19QPreviewPaintEngine8propertyEN12QPrintEngine22PrintEng'
        'inePropertyKeyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QPreviewPaintEngine8propertyEN12QPrintEngine22Pr'
          'intEnginePropertyKeyE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, a0: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int
    QPreviewPaintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#metric

    Parameters
    ----------

    a0 : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPreviewPaintEngine::metric(QPaintDevice::PaintDeviceMetric a0)
    #      const
    ritual = (
        'ritual_ZNK19QPreviewPaintEngine6metricEN12QPaintDevice17PaintDevic'
        'eMetricE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QPreviewPaintEngine6metricEN12QPaintDevice17Pain'
          'tDeviceMetricE')
    return self.uglySide.call(ritual, a0.value)

  def printerState(self) -> QPrinter.PrinterState:
    """
    Calls Qt's 'QPrinter::PrinterState QPreviewPaintEngine::printerState()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#printerState

    Returns
    -------

    QPrinter.PrinterState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPrinter.PrinterState(number)' gives.
    """
    #  QPrinter::PrinterState QPreviewPaintEngine::printerState() const
    ritual = 'ritual_ZNK19QPreviewPaintEngine12printerStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QPreviewPaintEngine12printerStateEv'
    return QPrinter.PrinterState(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPrintEngine.PrintEnginePropertyKey, QVariant)
  def setProperty(
      self,
      key: QPrintEngine.PrintEnginePropertyKey,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::setProperty(PrintEnginePropertyKey
    key, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#setProperty

    Parameters
    ----------

    key : QPrintEngine.PrintEnginePropertyKey
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPreviewPaintEngine::setProperty(PrintEnginePropertyKey key,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN19QPreviewPaintEngine11setPropertyEN12QPrintEngine22Print'
        'EnginePropertyKeyERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPreviewPaintEngine11setPropertyEN12QPrintEngine2'
          '2PrintEnginePropertyKeyERK8QVariant')
    self.uglySide.call(ritual, key.value, self._valueOf(value))

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
    Qt's 'QPreviewPaintEngine::QPreviewPaintEngine()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QPreviewPaintEnginePrivate'.
    """
    raise NotImplementedError(
        "'QPreviewPaintEngine.__init__' has no cute function yet. Qt's "
        "'QPreviewPaintEngine::QPreviewPaintEngine()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QPreviewPaintEnginePrivate'.")

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
  def begin(self, dev: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QPreviewPaintEngine::begin(QPaintDevice *dev)'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#begin

    Parameters
    ----------

    dev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPreviewPaintEngine::begin(QPaintDevice *dev)
    ritual = 'ritual_ZN19QPreviewPaintEngine5beginEP12QPaintDevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPreviewPaintEngine5beginEP12QPaintDevice'
    return self.uglySide.call(ritual, self._addressOf(dev, 'QPaintDevice'))

  def end(self) -> bool:
    """
    Calls Qt's 'bool QPreviewPaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#end
    """
    #  bool QPreviewPaintEngine::end()
    ritual = 'ritual_ZN19QPreviewPaintEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPreviewPaintEngine3endEv'
    return self.uglySide.call(ritual)

  @overload(QPaintEngineState)
  def updateState(self, state: QPaintEngineState) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::updateState(const QPaintEngineState
    &state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#updateState

    Parameters
    ----------

    state : QPaintEngineState
      Passed on as a value: Qt reads the C++ QPaintEngineState, which stays
      Python's own.
    """
    #  void QPreviewPaintEngine::updateState(const QPaintEngineState &state)
    ritual = (
        'ritual_ZN19QPreviewPaintEngine11updateStateERK17QPaintEngineState')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPreviewPaintEngine11updateStateERK17QPaintEngine'
          'State')
    self.uglySide.call(ritual, self._valueOf(state))

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::drawPath(const QPainterPath
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPreviewPaintEngine::drawPath(const QPainterPath &path)
    ritual = 'ritual_ZN19QPreviewPaintEngine8drawPathERK12QPainterPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPreviewPaintEngine8drawPathERK12QPainterPath'
    self.uglySide.call(ritual, self._valueOf(path))

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::drawPolygon(const QPointF *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#drawPolygon

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
    #  void QPreviewPaintEngine::drawPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN19QPreviewPaintEngine11drawPolygonEPK7QPointFiN12QPaintEn'
        'gine15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPreviewPaintEngine11drawPolygonEPK7QPointFiN12QP'
          'aintEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::drawTextItem(const QPointF &p,
    const QTextItem &textItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QPreviewPaintEngine::drawTextItem(const QPointF &p, const
    #      QTextItem &textItem)
    ritual = (
        'ritual_ZN19QPreviewPaintEngine12drawTextItemERK7QPointFRK9QTextIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPreviewPaintEngine12drawTextItemERK7QPointFRK9QT'
          'extItem')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(textItem),
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#drawPixmap

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
    #  void QPreviewPaintEngine::drawPixmap(const QRectF &r, const QPixmap
    #      &pm, const QRectF &sr)
    ritual = (
        'ritual_ZN19QPreviewPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPreviewPaintEngine10drawPixmapERK6QRectFRK7QPixm'
          'apS2_')
    self.uglySide.call(
        ritual, self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pm: QPixmap, p: QPointF) -> None:
    """
    Calls Qt's 'void QPreviewPaintEngine::drawTiledPixmap(const QRectF &r,
    const QPixmap &pm, const QPointF &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpreviewpaintengine.html#drawTiledPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPreviewPaintEngine::drawTiledPixmap(const QRectF &r, const
    #      QPixmap &pm, const QPointF &p)
    ritual = (
        'ritual_ZN19QPreviewPaintEngine15drawTiledPixmapERK6QRectFRK7QPixma'
        'pRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPreviewPaintEngine15drawTiledPixmapERK6QRectFRK7'
          'QPixmapRK7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(p, 'QPointF'),
    )

  def newPage(self) -> bool:
    """
    Calls Qt's 'bool QPreviewPaintEngine::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#newPage
    """
    #  bool QPreviewPaintEngine::newPage()
    ritual = 'ritual_ZN19QPreviewPaintEngine7newPageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPreviewPaintEngine7newPageEv'
    return self.uglySide.call(ritual)

  def abort(self) -> bool:
    """
    Calls Qt's 'bool QPreviewPaintEngine::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qpreviewpaintengine.html#abort
    """
    #  bool QPreviewPaintEngine::abort()
    ritual = 'ritual_ZN19QPreviewPaintEngine5abortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPreviewPaintEngine5abortEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def pages(*__, **_) -> Never:
    """
    Qt's 'QList<const QPicture *> QPreviewPaintEngine::pages()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QPreviewPaintEnginePrivate'.
    """
    raise NotImplementedError(
        "'QPreviewPaintEngine.pages' has no cute function yet. Qt's "
        "'QList<const QPicture *> QPreviewPaintEngine::pages()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QPreviewPaintEnginePrivate'.")

  @staticmethod
  def setProxyEngines(*__, **_) -> Never:
    """
    Qt's 'void QPreviewPaintEngine::setProxyEngines(QPrintEngine
    *printEngine, QPaintEngine *paintEngine)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QPreviewPaintEnginePrivate'.
    """
    raise NotImplementedError(
        "'QPreviewPaintEngine.setProxyEngines' has no cute function yet. "
        "Qt's 'void QPreviewPaintEngine::setProxyEngines(QPrintEngine "
        "*printEngine, QPaintEngine *paintEngine)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QPreviewPaintEnginePrivate'.")
