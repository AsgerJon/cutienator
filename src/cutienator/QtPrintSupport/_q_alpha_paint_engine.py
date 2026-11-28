"""
QAlphaPaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_alpha_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAlphaPaintEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QPaintEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPaintDevice, QPaintEngineState, QPainterPath, QPixmap
  from ..QtGui import QRegion, QTextItem
  from . import QAlphaPaintEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
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


class QAlphaPaintEngine(QPaintEngine):
  """
  The cute side of Qt's QAlphaPaintEngine: a plain Python object standing in
  front of one C++ QAlphaPaintEngine.

  It is built on the cute 'QPaintEngine', as Qt's QAlphaPaintEngine is built
  on Qt's QPaintEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAlphaPaintEngine that has a ritual and that Python
  can call so far, 13 names in all: 'd_func', 'begin', 'end', 'updateState',
  'drawPath', 'drawPolygon', 'drawPixmap', 'drawTextItem', 'drawTiledPixmap',
  'alphaClipping', 'continueCall', 'flushAndInit', 'cleanUp'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAlphaPaintEnginePrivate *QAlphaPaintEngine::d_func() const':
    takes in Python what 'QAlphaPaintEnginePrivate
    *QAlphaPaintEngine::d_func()' takes.
  - Qt's 'QAlphaPaintEngine::~QAlphaPaintEngine()': the destructor: Python
    never removes a C++ QAlphaPaintEngine.
  - Qt's 'QAlphaPaintEngine::QAlphaPaintEngine(QAlphaPaintEnginePrivate
    &data, PaintEngineFeatures devcaps)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QAlphaPaintEngine is created at the first use, not by
    'QAlphaPaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAlphaPaintEngine.
  - Each name of Qt's QAlphaPaintEngine that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAlphaPaintEngine'

  #  A C++ QAlphaPaintEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAlphaPaintEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def alphaClipping(self) -> QRegion:
    """
    Calls Qt's 'QRegion QAlphaPaintEngine::alphaClipping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengine.html#alphaClipping

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QAlphaPaintEngine::alphaClipping() const
    address = self.uglySide.call(
        'ritual_ZNK17QAlphaPaintEngine13alphaClippingEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def continueCall(self) -> bool:
    """
    Calls Qt's 'bool QAlphaPaintEngine::continueCall() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengine.html#continueCall
    """
    #  bool QAlphaPaintEngine::continueCall() const
    return self.uglySide.call(
        'ritual_ZNK17QAlphaPaintEngine12continueCallEv',
    )

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
    Qt's 'QAlphaPaintEngine::QAlphaPaintEngine(QAlphaPaintEnginePrivate
    &data, PaintEngineFeatures devcaps)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QAlphaPaintEngine.__init__' has no cute function yet. Qt's "
        "'QAlphaPaintEngine::QAlphaPaintEngine(QAlphaPaintEnginePrivate "
        "&data, PaintEngineFeatures devcaps)': takes a type Python has no "
        "way to hand over yet.")

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

  def d_func(self) -> Optional[QAlphaPaintEnginePrivate]:
    """
    Calls Qt's 'QAlphaPaintEnginePrivate *QAlphaPaintEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#d_func

    Returns
    -------

    Optional[QAlphaPaintEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAlphaPaintEnginePrivate *QAlphaPaintEngine::d_func()
    address = self.uglySide.call('ritual_ZN17QAlphaPaintEngine6d_funcEv')
    from . import QAlphaPaintEnginePrivate
    return QAlphaPaintEnginePrivate._cuteAt(address)

  @overload(QPaintDevice)
  @overload(NoneType)
  def begin(self, pdev: Optional[QPaintDevice]) -> bool:
    """
    Calls Qt's 'bool QAlphaPaintEngine::begin(QPaintDevice *pdev)'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#begin

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAlphaPaintEngine::begin(QPaintDevice *pdev)
    ritual = 'ritual_ZN17QAlphaPaintEngine5beginEP12QPaintDevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAlphaPaintEngine5beginEP12QPaintDevice'
    return self.uglySide.call(ritual, self._addressOf(pdev, 'QPaintDevice'))

  def end(self) -> bool:
    """
    Calls Qt's 'bool QAlphaPaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#end
    """
    #  bool QAlphaPaintEngine::end()
    ritual = 'ritual_ZN17QAlphaPaintEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAlphaPaintEngine3endEv'
    return self.uglySide.call(ritual)

  @overload(QPaintEngineState)
  def updateState(self, state: QPaintEngineState) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::updateState(const QPaintEngineState
    &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#updateState

    Parameters
    ----------

    state : QPaintEngineState
      Passed on as a value: Qt reads the C++ QPaintEngineState, which stays
      Python's own.
    """
    #  void QAlphaPaintEngine::updateState(const QPaintEngineState &state)
    ritual = (
        'ritual_ZN17QAlphaPaintEngine11updateStateERK17QPaintEngineState')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAlphaPaintEngine11updateStateERK17QPaintEngineSt'
          'ate')
    self.uglySide.call(ritual, self._valueOf(state))

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::drawPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QAlphaPaintEngine::drawPath(const QPainterPath &path)
    ritual = 'ritual_ZN17QAlphaPaintEngine8drawPathERK12QPainterPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAlphaPaintEngine8drawPathERK12QPainterPath'
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
    Calls Qt's 'void QAlphaPaintEngine::drawPolygon(const QPointF *points,
    int pointCount, PolygonDrawMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#drawPolygon

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
    #  void QAlphaPaintEngine::drawPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN17QAlphaPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngi'
        'ne15PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAlphaPaintEngine11drawPolygonEPK7QPointFiN12QPai'
          'ntEngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#drawPixmap

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
    #  void QAlphaPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
    #      const QRectF &sr)
    ritual = (
        'ritual_ZN17QAlphaPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAlphaPaintEngine10drawPixmapERK6QRectFRK7QPixmap'
          'S2_')
    self.uglySide.call(
        ritual, self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::drawTextItem(const QPointF &p, const
    QTextItem &textItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QAlphaPaintEngine::drawTextItem(const QPointF &p, const QTextItem
    #      &textItem)
    ritual = (
        'ritual_ZN17QAlphaPaintEngine12drawTextItemERK7QPointFRK9QTextItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAlphaPaintEngine12drawTextItemERK7QPointFRK9QTex'
          'tItem')
    self.uglySide.call(
        ritual, self._valueOf(p, 'QPointF'), self._valueOf(textItem),
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pixmap: QPixmap, s: QPointF) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::drawTiledPixmap(const QRectF &r,
    const QPixmap &pixmap, const QPointF &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengine.html#drawTiledPixmap

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
    #  void QAlphaPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
    #      &pixmap, const QPointF &s)
    ritual = (
        'ritual_ZN17QAlphaPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapR'
        'K7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAlphaPaintEngine15drawTiledPixmapERK6QRectFRK7QP'
          'ixmapRK7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pixmap), self._valueOf(s, 'QPointF'),
    )

  @overload()
  @overload(bool)
  def flushAndInit(self, init: bool = True) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::flushAndInit(bool init)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengine.html#flushAndInit

    Parameters
    ----------

    init : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAlphaPaintEngine::flushAndInit(bool init)
    self.uglySide.call('ritual_ZN17QAlphaPaintEngine12flushAndInitEb', init)

  def cleanUp(self) -> None:
    """
    Calls Qt's 'void QAlphaPaintEngine::cleanUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qalphapaintengine.html#cleanUp
    """
    #  void QAlphaPaintEngine::cleanUp()
    self.uglySide.call('ritual_ZN17QAlphaPaintEngine7cleanUpEv')
