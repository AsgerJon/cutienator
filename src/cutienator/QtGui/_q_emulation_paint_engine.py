"""
QEmulationPaintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qemulationpaintengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QEmulationPaintEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QPaintEngine, QPaintEngineEx

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from . import QImage, QPaintDevice, QPainterState, QPixmap, QStaticTextItem
  from . import QTextItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPaintDevice = WAIT['QPaintDevice']
  QPainterState = WAIT['QPainterState']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QStaticTextItem = WAIT['QStaticTextItem']
  QTextItem = WAIT['QTextItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEmulationPaintEngine(QPaintEngineEx):
  """
  The cute side of Qt's QEmulationPaintEngine: a plain Python object standing
  in front of one C++ QEmulationPaintEngine.

  It is built on the cute 'QPaintEngineEx', as Qt's QEmulationPaintEngine is
  built on Qt's QPaintEngineEx, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEmulationPaintEngine that has a ritual and that
  Python can call so far, 23 names in all: 'begin', 'end', 'type',
  'createState', 'drawPixmap', 'drawTextItem', 'drawStaticTextItem',
  'drawTiledPixmap', 'drawImage', 'clipEnabledChanged', 'penChanged',
  'brushChanged', 'brushOriginChanged', 'opacityChanged',
  'compositionModeChanged', 'renderHintsChanged', 'transformChanged',
  'setState', 'beginNativePainting', 'endNativePainting', 'flags', 'state',
  'fillBGRect'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QEmulationPaintEngine::fill(const QVectorPath &path, const
    QBrush &brush)': takes a type Python has no way to hand over yet.
  - Qt's 'void QEmulationPaintEngine::stroke(const QVectorPath &path, const
    QPen &pen)': takes a type Python has no way to hand over yet.
  - Qt's 'void QEmulationPaintEngine::clip(const QVectorPath &path,
    Qt::ClipOperation op)': takes a type Python has no way to hand over yet.
  - Qt's 'const QPainterState *QEmulationPaintEngine::state() const': takes
    in Python what 'QPainterState *QEmulationPaintEngine::state()' takes.

  What has no ritual
  ------------------

  1 of the 28 functions Qt declares: 1 leans on 'QEmulationPaintEngine.

  What to expect
  --------------

  - The C++ QEmulationPaintEngine is created at the first use, not by
    'QEmulationPaintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEmulationPaintEngine.
  - Each name of Qt's QEmulationPaintEngine that has no cute function yet,
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
  __qt_class__ = 'QEmulationPaintEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QPaintEngine.Type:
    """
    Calls Qt's 'Type QEmulationPaintEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qemulationpaintengine.html#type

    Returns
    -------

    QPaintEngine.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPaintEngine.Type(number)' gives.
    """
    #  Type QEmulationPaintEngine::type() const
    ritual = 'ritual_ZNK21QEmulationPaintEngine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QEmulationPaintEngine4typeEv'
    return QPaintEngine.Type(self.uglySide.call(ritual))

  @overload(QPainterState)
  @overload(NoneType)
  def createState(
      self,
      orig: Optional[QPainterState],
  ) -> Optional[QPainterState]:
    """
    Calls Qt's 'QPainterState
    *QEmulationPaintEngine::createState(QPainterState *orig) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#createState

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
    #  QPainterState *QEmulationPaintEngine::createState(QPainterState *orig)
    #      const
    ritual = (
        'ritual_ZNK21QEmulationPaintEngine11createStateEP13QPainterState')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QEmulationPaintEngine11createStateEP13QPainterSt'
          'ate')
    address = self.uglySide.call(ritual, self._addressOf(orig))
    from . import QPainterState
    return QPainterState._cuteAt(address)

  def flags(self) -> int:
    """
    Calls Qt's 'uint QEmulationPaintEngine::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qemulationpaintengine.html#flags
    """
    #  uint QEmulationPaintEngine::flags() const
    ritual = 'ritual_ZNK21QEmulationPaintEngine5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QEmulationPaintEngine5flagsEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainterState)
  @overload(NoneType)
  def setState(self, s: Optional[QPainterState]) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::setState(QPainterState *s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#setState

    Parameters
    ----------

    s : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEmulationPaintEngine::setState(QPainterState *s)
    ritual = 'ritual_ZN21QEmulationPaintEngine8setStateEP13QPainterState'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QEmulationPaintEngine8setStateEP13QPainterState')
    self.uglySide.call(ritual, self._addressOf(s))

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
    Qt's 'QEmulationPaintEngine::QEmulationPaintEngine(QPaintEngineEx
    *engine)': leans on 'QEmulationPaintEngine::drawTextItem(QPointF const&,
    QTextItem const&)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QEmulationPaintEngine.__init__' has no cute function yet. Qt's "
        "'QEmulationPaintEngine::QEmulationPaintEngine(QPaintEngineEx "
        "*engine)': leans on 'QEmulationPaintEngine::drawTextItem(QPointF "
        "const&, QTextItem const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'bool QEmulationPaintEngine::begin(QPaintDevice *pdev)'.

    Qt's own words: https://doc.qt.io/qt-6/qemulationpaintengine.html#begin

    Parameters
    ----------

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QEmulationPaintEngine::begin(QPaintDevice *pdev)
    ritual = 'ritual_ZN21QEmulationPaintEngine5beginEP12QPaintDevice'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine5beginEP12QPaintDevice'
    return self.uglySide.call(ritual, self._addressOf(pdev, 'QPaintDevice'))

  def end(self) -> bool:
    """
    Calls Qt's 'bool QEmulationPaintEngine::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qemulationpaintengine.html#end
    """
    #  bool QEmulationPaintEngine::end()
    ritual = 'ritual_ZN21QEmulationPaintEngine3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine3endEv'
    return self.uglySide.call(ritual)

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#drawPixmap

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
    #  void QEmulationPaintEngine::drawPixmap(const QRectF &r, const QPixmap
    #      &pm, const QRectF &sr)
    ritual = (
        'ritual_ZN21QEmulationPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QEmulationPaintEngine10drawPixmapERK6QRectFRK7QPi'
          'xmapS2_')
    self.uglySide.call(
        ritual, self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPointF, QTextItem)
  def drawTextItem(self, p: QPointF, textItem: QTextItem) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::drawTextItem(const QPointF &p,
    const QTextItem &textItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#drawTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    textItem : QTextItem
      Passed on as a value: Qt reads the C++ QTextItem, which stays Python's
      own.
    """
    #  void QEmulationPaintEngine::drawTextItem(const QPointF &p, const
    #      QTextItem &textItem)
    self.uglySide.call(
        'ritual_ZN21QEmulationPaintEngine12drawTextItemERK7QPointFRK9QTextI'
        'tem',
        self._valueOf(p, 'QPointF'), self._valueOf(textItem),
    )

  @overload(QStaticTextItem)
  @overload(NoneType)
  def drawStaticTextItem(self, item: Optional[QStaticTextItem]) -> None:
    """
    Calls Qt's 'void
    QEmulationPaintEngine::drawStaticTextItem(QStaticTextItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#drawStaticTextItem

    Parameters
    ----------

    item : Optional[QStaticTextItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEmulationPaintEngine::drawStaticTextItem(QStaticTextItem *item)
    ritual = (
        'ritual_ZN21QEmulationPaintEngine18drawStaticTextItemEP15QStaticTex'
        'tItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QEmulationPaintEngine18drawStaticTextItemEP15QSta'
          'ticTextItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pixmap: QPixmap, s: QPointF) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::drawTiledPixmap(const QRectF &r,
    const QPixmap &pixmap, const QPointF &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#drawTiledPixmap

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
    #  void QEmulationPaintEngine::drawTiledPixmap(const QRectF &r, const
    #      QPixmap &pixmap, const QPointF &s)
    ritual = (
        'ritual_ZN21QEmulationPaintEngine15drawTiledPixmapERK6QRectFRK7QPix'
        'mapRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QEmulationPaintEngine15drawTiledPixmapERK6QRectFR'
          'K7QPixmapRK7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pixmap), self._valueOf(s, 'QPointF'),
    )

  @overload(QRectF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      r: QRectF,
      pm: QImage,
      sr: QRectF,
      flags: Qt.ImageConversionFlags,
  ) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::drawImage(const QRectF &r, const
    QImage &pm, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#drawImage

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
      Passed on as its number.
    """
    #  void QEmulationPaintEngine::drawImage(const QRectF &r, const QImage
    #      &pm, const QRectF &sr, Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN21QEmulationPaintEngine9drawImageERK6QRectFRK6QImageS2_6Q'
        'FlagsIN2Qt19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QEmulationPaintEngine9drawImageERK6QRectFRK6QImag'
          'eS2_6QFlagsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr), flags.value,
    )

  def clipEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::clipEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#clipEnabledChanged
    """
    #  void QEmulationPaintEngine::clipEnabledChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine18clipEnabledChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine18clipEnabledChangedEv'
    self.uglySide.call(ritual)

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::penChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#penChanged
    """
    #  void QEmulationPaintEngine::penChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine10penChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine10penChangedEv'
    self.uglySide.call(ritual)

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::brushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#brushChanged
    """
    #  void QEmulationPaintEngine::brushChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine12brushChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine12brushChangedEv'
    self.uglySide.call(ritual)

  def brushOriginChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::brushOriginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#brushOriginChanged
    """
    #  void QEmulationPaintEngine::brushOriginChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine18brushOriginChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine18brushOriginChangedEv'
    self.uglySide.call(ritual)

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#opacityChanged
    """
    #  void QEmulationPaintEngine::opacityChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine14opacityChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine14opacityChangedEv'
    self.uglySide.call(ritual)

  def compositionModeChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::compositionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#compositionModeChanged
    """
    #  void QEmulationPaintEngine::compositionModeChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine22compositionModeChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QEmulationPaintEngine22compositionModeChangedEv')
    self.uglySide.call(ritual)

  def renderHintsChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::renderHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#renderHintsChanged
    """
    #  void QEmulationPaintEngine::renderHintsChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine18renderHintsChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine18renderHintsChangedEv'
    self.uglySide.call(ritual)

  def transformChanged(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::transformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#transformChanged
    """
    #  void QEmulationPaintEngine::transformChanged()
    ritual = 'ritual_ZN21QEmulationPaintEngine16transformChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine16transformChangedEv'
    self.uglySide.call(ritual)

  def beginNativePainting(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::beginNativePainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#beginNativePainting
    """
    #  void QEmulationPaintEngine::beginNativePainting()
    ritual = 'ritual_ZN21QEmulationPaintEngine19beginNativePaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine19beginNativePaintingEv'
    self.uglySide.call(ritual)

  def endNativePainting(self) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::endNativePainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#endNativePainting
    """
    #  void QEmulationPaintEngine::endNativePainting()
    ritual = 'ritual_ZN21QEmulationPaintEngine17endNativePaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QEmulationPaintEngine17endNativePaintingEv'
    self.uglySide.call(ritual)

  def state(self) -> Optional[QPainterState]:
    """
    Calls Qt's 'QPainterState *QEmulationPaintEngine::state()'.

    Qt's own words: https://doc.qt.io/qt-6/qemulationpaintengine.html#state

    Returns
    -------

    Optional[QPainterState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterState *QEmulationPaintEngine::state()
    address = self.uglySide.call('ritual_ZN21QEmulationPaintEngine5stateEv')
    from . import QPainterState
    return QPainterState._cuteAt(address)

  @overload(QRectF)
  def fillBGRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QEmulationPaintEngine::fillBGRect(const QRectF &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qemulationpaintengine.html#fillBGRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QEmulationPaintEngine::fillBGRect(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN21QEmulationPaintEngine10fillBGRectERK6QRectF',
        self._valueOf(r),
    )
