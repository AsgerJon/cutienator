"""
QSGRhiLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhilayer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGRhiLayer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QSGLayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QImage, QRhi, QRhiResourceUpdateBatch, QRhiTexture
  from . import QSGNode, QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QSGNode = WAIT['QSGNode']
  QSGRenderContext = WAIT['QSGRenderContext']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiLayer(QSGLayer):
  """
  The cute side of Qt's QSGRhiLayer: a plain Python object standing in front
  of one C++ QSGRhiLayer.

  It is built on the cute 'QSGLayer', as Qt's QSGRhiLayer is built on Qt's
  QSGLayer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiLayer that has a ritual and that Python can
  call so far, 28 names in all: 'metaObject', 'tr', 'updateTexture',
  'hasAlphaChannel', 'hasMipmaps', 'textureSize', 'comparisonKey',
  'rhiTexture', 'commitTextureOperations', 'setItem', 'setRect', 'setSize',
  'setHasMipmaps', 'setFormat', 'setLive', 'setRecursive',
  'setDevicePixelRatio', 'setMirrorHorizontal', 'setMirrorVertical',
  'normalizedTextureSubRect', 'setSamples', 'scheduleUpdate', 'toImage',
  'markDirtyTexture', 'invalidated', 'grab', 'releaseResources',
  'clearMainTexture'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRhiLayer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSGRhiLayer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRhiLayer::~QSGRhiLayer()': the destructor: Python never removes
    a C++ QSGRhiLayer.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGRhiLayer is created at the first use, not by
    'QSGRhiLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiLayer.
  - Qt tells when it has removed the C++ QSGRhiLayer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString QSGRhiLayer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#tr

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
    #  QString QSGRhiLayer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QSGRhiLayer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiLayer'

  #  A C++ QSGRhiLayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiLayer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGRhiLayer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRhiLayer::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QSGRhiLayer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiLayer::hasAlphaChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#hasAlphaChannel
    """
    #  bool QSGRhiLayer::hasAlphaChannel() const
    ritual = 'ritual_ZNK11QSGRhiLayer15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiLayer::hasMipmaps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#hasMipmaps
    """
    #  bool QSGRhiLayer::hasMipmaps() const
    ritual = 'ritual_ZNK11QSGRhiLayer10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer10hasMipmapsEv'
    return self.uglySide.call(ritual)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGRhiLayer::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGRhiLayer::textureSize() const
    ritual = 'ritual_ZNK11QSGRhiLayer11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGRhiLayer::comparisonKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#comparisonKey
    """
    #  qint64 QSGRhiLayer::comparisonKey() const
    ritual = 'ritual_ZNK11QSGRhiLayer13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer13comparisonKeyEv'
    return self.uglySide.call(ritual)

  def rhiTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGRhiLayer::rhiTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#rhiTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGRhiLayer::rhiTexture() const
    ritual = 'ritual_ZNK11QSGRhiLayer10rhiTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer10rhiTextureEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def normalizedTextureSubRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGRhiLayer::normalizedTextureSubRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhilayer.html#normalizedTextureSubRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGRhiLayer::normalizedTextureSubRect() const
    ritual = 'ritual_ZNK11QSGRhiLayer24normalizedTextureSubRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer24normalizedTextureSubRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QSGRhiLayer::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGRhiLayer::toImage() const
    ritual = 'ritual_ZNK11QSGRhiLayer7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSGRhiLayer7toImageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGNode)
  @overload(NoneType)
  def setItem(self, item: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setItem(QSGNode *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setItem

    Parameters
    ----------

    item : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiLayer::setItem(QSGNode *item)
    ritual = 'ritual_ZN11QSGRhiLayer7setItemEP7QSGNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer7setItemEP7QSGNode'
    self.uglySide.call(ritual, self._addressOf(item, 'QSGNode'))

  @overload(QRectF)
  def setRect(self, logicalRect: QRectF) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setRect(const QRectF &logicalRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setRect

    Parameters
    ----------

    logicalRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGRhiLayer::setRect(const QRectF &logicalRect)
    ritual = 'ritual_ZN11QSGRhiLayer7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer7setRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(logicalRect))

  @overload(QSize)
  def setSize(self, pixelSize: QSize) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setSize(const QSize &pixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setSize

    Parameters
    ----------

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGRhiLayer::setSize(const QSize &pixelSize)
    ritual = 'ritual_ZN11QSGRhiLayer7setSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer7setSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(pixelSize))

  @overload(bool)
  def setHasMipmaps(self, mipmap: bool) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setHasMipmaps(bool mipmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setHasMipmaps

    Parameters
    ----------

    mipmap : bool
      Passed on as it is.
    """
    #  void QSGRhiLayer::setHasMipmaps(bool mipmap)
    ritual = 'ritual_ZN11QSGRhiLayer13setHasMipmapsEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer13setHasMipmapsEb'
    self.uglySide.call(ritual, mipmap)

  @overload(QSGLayer.Format)
  def setFormat(self, format: QSGLayer.Format) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setFormat(Format format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setFormat

    Parameters
    ----------

    format : QSGLayer.Format
      Passed on as its number.
    """
    #  void QSGRhiLayer::setFormat(Format format)
    ritual = 'ritual_ZN11QSGRhiLayer9setFormatEN8QSGLayer6FormatE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer9setFormatEN8QSGLayer6FormatE'
    self.uglySide.call(ritual, format.value)

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QSGRhiLayer::setLive(bool live)
    ritual = 'ritual_ZN11QSGRhiLayer7setLiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer7setLiveEb'
    self.uglySide.call(ritual, live)

  @overload(bool)
  def setRecursive(self, recursive: bool) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setRecursive(bool recursive)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setRecursive

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void QSGRhiLayer::setRecursive(bool recursive)
    ritual = 'ritual_ZN11QSGRhiLayer12setRecursiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer12setRecursiveEb'
    self.uglySide.call(ritual, recursive)

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setDevicePixelRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhilayer.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGRhiLayer::setDevicePixelRatio(qreal ratio)
    ritual = 'ritual_ZN11QSGRhiLayer19setDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer19setDevicePixelRatioEd'
    self.uglySide.call(ritual, ratio)

  @overload(bool)
  def setMirrorHorizontal(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setMirrorHorizontal(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhilayer.html#setMirrorHorizontal

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QSGRhiLayer::setMirrorHorizontal(bool mirror)
    ritual = 'ritual_ZN11QSGRhiLayer19setMirrorHorizontalEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer19setMirrorHorizontalEb'
    self.uglySide.call(ritual, mirror)

  @overload(bool)
  def setMirrorVertical(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setMirrorVertical(bool mirror)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setMirrorVertical

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QSGRhiLayer::setMirrorVertical(bool mirror)
    ritual = 'ritual_ZN11QSGRhiLayer17setMirrorVerticalEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer17setMirrorVerticalEb'
    self.uglySide.call(ritual, mirror)

  @overload(int)
  def setSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::setSamples(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#setSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QSGRhiLayer::setSamples(int samples)
    ritual = 'ritual_ZN11QSGRhiLayer10setSamplesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer10setSamplesEi'
    self.uglySide.call(ritual, samples)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's 'QSGRhiLayer::QSGRhiLayer(QSGRenderContext
    *context)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#QSGRhiLayer

    Parameters
    ----------

    context : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGRhiLayer::QSGRhiLayer(QSGRenderContext *context)
    self._noteCreation(QSGRhiLayer, lambda: Rituals.call(
        'ritual_ZN11QSGRhiLayerC1EP16QSGRenderContext',
        self._addressOf(context),
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

  def updateTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiLayer::updateTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#updateTexture
    """
    #  bool QSGRhiLayer::updateTexture()
    ritual = 'ritual_ZN11QSGRhiLayer13updateTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer13updateTextureEv'
    return self.uglySide.call(ritual)

  @overload(QRhi, QRhiResourceUpdateBatch)
  @overload(QRhi, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def commitTextureOperations(
      self,
      rhi: Optional[QRhi],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::commitTextureOperations(QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhilayer.html#commitTextureOperations

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiLayer::commitTextureOperations(QRhi *rhi,
    #      QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN11QSGRhiLayer23commitTextureOperationsEP4QRhiP23QRhiResou'
        'rceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSGRhiLayer23commitTextureOperationsEP4QRhiP23QRh'
          'iResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(rhi), self._addressOf(resourceUpdates),
    )

  def scheduleUpdate(self) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::scheduleUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#scheduleUpdate
    """
    #  void QSGRhiLayer::scheduleUpdate()
    ritual = 'ritual_ZN11QSGRhiLayer14scheduleUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer14scheduleUpdateEv'
    self.uglySide.call(ritual)

  def markDirtyTexture(self) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::markDirtyTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#markDirtyTexture
    """
    #  void QSGRhiLayer::markDirtyTexture()
    ritual = 'ritual_ZN11QSGRhiLayer16markDirtyTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer16markDirtyTextureEv'
    self.uglySide.call(ritual)

  def invalidated(self) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::invalidated()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#invalidated
    """
    #  void QSGRhiLayer::invalidated()
    ritual = 'ritual_ZN11QSGRhiLayer11invalidatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRhiLayer11invalidatedEv'
    self.uglySide.call(ritual)

  def grab(self) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::grab()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#grab
    """
    #  void QSGRhiLayer::grab()
    self.uglySide.call('ritual_ZN11QSGRhiLayer4grabEv')

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::releaseResources()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#releaseResources
    """
    #  void QSGRhiLayer::releaseResources()
    self.uglySide.call('ritual_ZN11QSGRhiLayer16releaseResourcesEv')

  def clearMainTexture(self) -> None:
    """
    Calls Qt's 'void QSGRhiLayer::clearMainTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhilayer.html#clearMainTexture
    """
    #  void QSGRhiLayer::clearMainTexture()
    self.uglySide.call('ritual_ZN11QSGRhiLayer16clearMainTextureEv')
