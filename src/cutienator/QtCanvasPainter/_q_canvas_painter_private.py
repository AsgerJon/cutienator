"""
QCanvasPainterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainter_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasPainterPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QCanvasPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QFont, QImage, QRhiTexture, QTransform
  from . import QCPainterEngine, QCanvasBoxShadow, QCanvasImage
  from . import QCanvasOffscreenCanvas
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBoxShadow = WAIT['QCanvasBoxShadow']
  QCanvasOffscreenCanvas = WAIT['QCanvasOffscreenCanvas']
  QFont = WAIT['QFont']
  QImage = WAIT['QImage']
  QRectF = WAIT['QRectF']
  QRhiTexture = WAIT['QRhiTexture']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasPainterPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPainterPrivate: a plain Python object standing
  in front of one C++ QCanvasPainterPrivate.

  What exists
  -----------

  Every function of Qt's QCanvasPainterPrivate that has a ritual and that
  Python can call so far, 14 names in all: 'engine', 'get',
  'generateImageKey', 'getQCanvasImage', 'handleCleanupTextures',
  'clearTextureCache', 'markTextureIdUsed', 'setStencilClip',
  'setBrushTransform', 'setFont', 'fillText', 'textBoundingBox',
  'drawBoxShadow', 'setAntialiasingEnabled'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasPainterPrivate::~QCanvasPainterPrivate()': the destructor:
    Python never removes a C++ QCanvasPainterPrivate.
  - Qt's 'const QCanvasPainterPrivate *QCanvasPainterPrivate::get(const
    QCanvasPainter *painter)': takes in Python what 'QCanvasPainterPrivate
    *QCanvasPainterPrivate::get(QCanvasPainter *painter)' takes.
  - Qt's 'void QCanvasPainterPrivate::setStencilClip(const QVectorPath
    &clipPath)': takes a type Python has no way to hand over yet.
  - Qt's 'void QCanvasPainterPrivate::fillShapedText(QFontEngine *fontEngine,
    const quint32 *glyphIndexes, const QFixedPoint *glyphPositions, int
    glyphCount)': names 'quint32', which has no cute class yet.

  What to expect
  --------------

  - The C++ QCanvasPainterPrivate is created at the first use, not by
    'QCanvasPainterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasPainterPrivate.
  - Each name of Qt's QCanvasPainterPrivate that has no cute function yet,
    'fillShapedText', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasPainter)
  @overload(NoneType)
  def get(
      painter: Optional[QCanvasPainter],
  ) -> Optional[QCanvasPainterPrivate]:
    """
    Calls Qt's 'QCanvasPainterPrivate
    *QCanvasPainterPrivate::get(QCanvasPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterprivate.html#get

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasPainterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainterPrivate *QCanvasPainterPrivate::get(QCanvasPainter
    #      *painter)
    address = Rituals.call(
        'ritual_ZN21QCanvasPainterPrivate3getEP14QCanvasPainter',
        CuteMixin._addressOf(painter),
    )
    return QCanvasPainterPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasPainterPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def engine(self) -> Optional[QCPainterEngine]:
    """
    Calls Qt's 'QCPainterEngine *QCanvasPainterPrivate::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterprivate.html#engine

    Returns
    -------

    Optional[QCPainterEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCPainterEngine *QCanvasPainterPrivate::engine() const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasPainterPrivate6engineEv',
    )
    from . import QCPainterEngine
    return QCPainterEngine._cuteAt(address)

  @overload(QImage, QCanvasPainter.ImageFlags)
  def generateImageKey(
      self,
      image: QImage,
      flags: QCanvasPainter.ImageFlags,
  ) -> int:
    """
    Calls Qt's 'qint64 QCanvasPainterPrivate::generateImageKey(const QImage
    &image, QCanvasPainter::ImageFlags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#generateImageKey

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : QCanvasPainter.ImageFlags
      Passed on as its number.
    """
    #  qint64 QCanvasPainterPrivate::generateImageKey(const QImage &image,
    #      QCanvasPainter::ImageFlags flags) const
    return self.uglySide.call(
        'ritual_ZNK21QCanvasPainterPrivate16generateImageKeyERK6QImage6QFla'
        'gsIN14QCanvasPainter9ImageFlagEE',
        self._valueOf(image), flags.value,
    )

  @overload(str, float, float)
  @overload(str, float, float, float)
  def textBoundingBox(
      self,
      text: str,
      x: float,
      y: float,
      maxWidth: float = -1.0,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasPainterPrivate::textBoundingBox(const QString
    &text, qreal x, qreal y, qreal maxWidth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#textBoundingBox

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    maxWidth : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasPainterPrivate::textBoundingBox(const QString &text,
    #      qreal x, qreal y, qreal maxWidth) const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasPainterPrivate15textBoundingBoxERK7QStringddd',
        text, x, y, maxWidth,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, QRectF)
  def textBoundingBox(self, text: str, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasPainterPrivate::textBoundingBox(const QString
    &text, const QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#textBoundingBox

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasPainterPrivate::textBoundingBox(const QString &text,
    #      const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasPainterPrivate15textBoundingBoxERK7QStringRK6QR'
        'ectF',
        text, self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QRectF])
  def setStencilClip(self, rects: QList[QRectF]) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::setStencilClip(const
    QList<QRectF> &rects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#setStencilClip

    Parameters
    ----------

    rects : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCanvasPainterPrivate::setStencilClip(const QList<QRectF> &rects)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate14setStencilClipERK5QListI6QRectFE',
        self._valueOf(rects),
    )

  @overload(QTransform)
  def setBrushTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::setBrushTransform(const
    QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#setBrushTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QCanvasPainterPrivate::setBrushTransform(const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate17setBrushTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterprivate.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QCanvasPainterPrivate::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(bool)
  def setAntialiasingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::setAntialiasingEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#setAntialiasingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCanvasPainterPrivate::setAntialiasingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate22setAntialiasingEnabledEb',
        enabled,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasPainterPrivate::QCanvasPainterPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#QCanvasPainterPrivate
    """
    #  QCanvasPainterPrivate::QCanvasPainterPrivate()
    self._noteCreation(QCanvasPainterPrivate, lambda: Rituals.call(
        'ritual_ZN21QCanvasPainterPrivateC1Ev',
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

  @overload(QImage, QCanvasPainter.ImageFlags)
  @overload(QImage, QCanvasPainter.ImageFlags, int)
  def getQCanvasImage(
      self,
      image: QImage,
      flags: QCanvasPainter.ImageFlags,
      imageKey: int = 0,
  ) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasPainterPrivate::getQCanvasImage(const
    QImage &image, QCanvasPainter::ImageFlags flags, qint64 imageKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#getQCanvasImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : QCanvasPainter.ImageFlags
      Passed on as its number.

    imageKey : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasPainterPrivate::getQCanvasImage(const QImage
    #      &image, QCanvasPainter::ImageFlags flags, qint64 imageKey)
    address = self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate15getQCanvasImageERK6QImage6QFlags'
        'IN14QCanvasPainter9ImageFlagEEx',
        self._valueOf(image), flags.value, imageKey,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  @overload(QRhiTexture, QCanvasPainter.ImageFlags)
  @overload(NoneType, QCanvasPainter.ImageFlags)
  def getQCanvasImage(
      self,
      texture: Optional[QRhiTexture],
      flags: QCanvasPainter.ImageFlags,
  ) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage
    QCanvasPainterPrivate::getQCanvasImage(QRhiTexture *texture,
    QCanvasPainter::ImageFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#getQCanvasImage

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QCanvasPainter.ImageFlags
      Passed on as its number.

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasPainterPrivate::getQCanvasImage(QRhiTexture
    #      *texture, QCanvasPainter::ImageFlags flags)
    address = self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate15getQCanvasImageEP11QRhiTexture6Q'
        'FlagsIN14QCanvasPainter9ImageFlagEE',
        self._addressOf(texture), flags.value,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  @overload(QCanvasOffscreenCanvas, QCanvasPainter.ImageFlags)
  def getQCanvasImage(
      self,
      canvas: QCanvasOffscreenCanvas,
      flags: QCanvasPainter.ImageFlags,
  ) -> QCanvasImage:
    """
    Calls Qt's 'QCanvasImage QCanvasPainterPrivate::getQCanvasImage(const
    QCanvasOffscreenCanvas &canvas, QCanvasPainter::ImageFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#getQCanvasImage

    Parameters
    ----------

    canvas : QCanvasOffscreenCanvas
      Passed on as a value: Qt reads the C++ QCanvasOffscreenCanvas, which
      stays Python's own.

    flags : QCanvasPainter.ImageFlags
      Passed on as its number.

    Returns
    -------

    QCanvasImage
      A new cute QCanvasImage around the copy Qt gave back. Python owns it.
    """
    #  QCanvasImage QCanvasPainterPrivate::getQCanvasImage(const
    #      QCanvasOffscreenCanvas &canvas, QCanvasPainter::ImageFlags flags)
    address = self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate15getQCanvasImageERK22QCanvasOffsc'
        'reenCanvas6QFlagsIN14QCanvasPainter9ImageFlagEE',
        self._valueOf(canvas), flags.value,
    )
    from . import QCanvasImage
    return QCanvasImage._cuteOwning(address)

  def handleCleanupTextures(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::handleCleanupTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#handleCleanupTextures
    """
    #  void QCanvasPainterPrivate::handleCleanupTextures()
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate21handleCleanupTexturesEv',
    )

  def clearTextureCache(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::clearTextureCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#clearTextureCache
    """
    #  void QCanvasPainterPrivate::clearTextureCache()
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate17clearTextureCacheEv',
    )

  @overload(int)
  def markTextureIdUsed(self, imageId: int) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::markTextureIdUsed(int imageId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#markTextureIdUsed

    Parameters
    ----------

    imageId : int
      Passed on as it is.
    """
    #  void QCanvasPainterPrivate::markTextureIdUsed(int imageId)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate17markTextureIdUsedEi', imageId,
    )

  @overload(str, float, float)
  @overload(str, float, float, float)
  def fillText(
      self,
      text: str,
      x: float,
      y: float,
      maxWidth: float = -1.0,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::fillText(const QString &text,
    qreal x, qreal y, qreal maxWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#fillText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    maxWidth : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.
    """
    #  void QCanvasPainterPrivate::fillText(const QString &text, qreal x,
    #      qreal y, qreal maxWidth)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate8fillTextERK7QStringddd',
        text, x, y, maxWidth,
    )

  @overload(str, QRectF)
  def fillText(self, text: str, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::fillText(const QString &text,
    const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#fillText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPainterPrivate::fillText(const QString &text, const QRectF
    #      &rect)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate8fillTextERK7QStringRK6QRectF',
        text, self._valueOf(rect),
    )

  @overload(QCanvasPainter, QCanvasBoxShadow)
  @overload(NoneType, QCanvasBoxShadow)
  def drawBoxShadow(
      self,
      painter: Optional[QCanvasPainter],
      shadow: QCanvasBoxShadow,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPainterPrivate::drawBoxShadow(QCanvasPainter
    *painter, const QCanvasBoxShadow &shadow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterprivate.html#drawBoxShadow

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    shadow : QCanvasBoxShadow
      Passed on as a value: Qt reads the C++ QCanvasBoxShadow, which stays
      Python's own.
    """
    #  void QCanvasPainterPrivate::drawBoxShadow(QCanvasPainter *painter,
    #      const QCanvasBoxShadow &shadow)
    self.uglySide.call(
        'ritual_ZN21QCanvasPainterPrivate13drawBoxShadowEP14QCanvasPainterR'
        'K16QCanvasBoxShadow',
        self._addressOf(painter), self._valueOf(shadow),
    )

  @staticmethod
  def fillShapedText(*__, **_) -> Never:
    """
    Qt's 'void QCanvasPainterPrivate::fillShapedText(QFontEngine *fontEngine,
    const quint32 *glyphIndexes, const QFixedPoint *glyphPositions, int
    glyphCount)': names 'quint32', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCanvasPainterPrivate.fillShapedText' has no cute function yet. "
        "Qt's 'void QCanvasPainterPrivate::fillShapedText(QFontEngine "
        "*fontEngine, const quint32 *glyphIndexes, const QFixedPoint "
        "*glyphPositions, int glyphCount)': names 'quint32', which has no "
        "cute class yet.")
