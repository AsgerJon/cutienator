"""
QSGSoftwareLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarelayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGSoftwareLayer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGLayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QImage, QPixmap
  from . import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareLayer(QSGLayer):
  """
  The cute side of Qt's QSGSoftwareLayer: a plain Python object standing in
  front of one C++ QSGSoftwareLayer.

  It is built on the cute 'QSGLayer', as Qt's QSGSoftwareLayer is built on
  Qt's QSGLayer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareLayer that has a ritual and that Python
  can call so far, 22 names in all: 'metaObject', 'pixmap', 'comparisonKey',
  'textureSize', 'hasAlphaChannel', 'hasMipmaps', 'updateTexture', 'setItem',
  'setRect', 'setSize', 'scheduleUpdate', 'toImage', 'setLive',
  'setRecursive', 'setFormat', 'setHasMipmaps', 'setDevicePixelRatio',
  'setMirrorHorizontal', 'setMirrorVertical', 'setSamples',
  'markDirtyTexture', 'invalidated'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGSoftwareLayer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSGSoftwareLayer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGSoftwareLayer::~QSGSoftwareLayer()': the destructor: Python
    never removes a C++ QSGSoftwareLayer.

  What has no ritual
  ------------------

  5 of the 30 functions Qt declares: 2 not a gap; 2 leans on
  'QSGSoftwareLayer; 1 leans on 'QSGSoftwarePixmapRenderer.

  What to expect
  --------------

  - The C++ QSGSoftwareLayer is created at the first use, not by
    'QSGSoftwareLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareLayer.
  - Qt tells when it has removed the C++ QSGSoftwareLayer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGSoftwareLayer that has no cute function yet,
    '__init__', 'grab', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareLayer'

  #  A C++ QSGSoftwareLayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareLayer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGSoftwareLayer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGSoftwareLayer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGSoftwareLayer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'const QPixmap &QSGSoftwareLayer::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  const QPixmap &QSGSoftwareLayer::pixmap() const
    address = self.uglySide.call('ritual_ZNK16QSGSoftwareLayer6pixmapEv')
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGSoftwareLayer::comparisonKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#comparisonKey
    """
    #  qint64 QSGSoftwareLayer::comparisonKey() const
    ritual = 'ritual_ZNK16QSGSoftwareLayer13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGSoftwareLayer13comparisonKeyEv'
    return self.uglySide.call(ritual)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGSoftwareLayer::textureSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGSoftwareLayer::textureSize() const
    ritual = 'ritual_ZNK16QSGSoftwareLayer11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGSoftwareLayer11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareLayer::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#hasAlphaChannel
    """
    #  bool QSGSoftwareLayer::hasAlphaChannel() const
    ritual = 'ritual_ZNK16QSGSoftwareLayer15hasAlphaChannelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGSoftwareLayer15hasAlphaChannelEv'
    return self.uglySide.call(ritual)

  def hasMipmaps(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareLayer::hasMipmaps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#hasMipmaps
    """
    #  bool QSGSoftwareLayer::hasMipmaps() const
    ritual = 'ritual_ZNK16QSGSoftwareLayer10hasMipmapsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGSoftwareLayer10hasMipmapsEv'
    return self.uglySide.call(ritual)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QSGSoftwareLayer::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGSoftwareLayer::toImage() const
    ritual = 'ritual_ZNK16QSGSoftwareLayer7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSGSoftwareLayer7toImageEv'
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
    Calls Qt's 'void QSGSoftwareLayer::setItem(QSGNode *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setItem

    Parameters
    ----------

    item : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareLayer::setItem(QSGNode *item)
    ritual = 'ritual_ZN16QSGSoftwareLayer7setItemEP7QSGNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer7setItemEP7QSGNode'
    self.uglySide.call(ritual, self._addressOf(item, 'QSGNode'))

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareLayer::setRect(const QRectF &rect)
    ritual = 'ritual_ZN16QSGSoftwareLayer7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer7setRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSoftwareLayer::setSize(const QSize &size)
    ritual = 'ritual_ZN16QSGSoftwareLayer7setSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer7setSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setLive(bool live)
    ritual = 'ritual_ZN16QSGSoftwareLayer7setLiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer7setLiveEb'
    self.uglySide.call(ritual, live)

  @overload(bool)
  def setRecursive(self, recursive: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setRecursive(bool recursive)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setRecursive

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setRecursive(bool recursive)
    ritual = 'ritual_ZN16QSGSoftwareLayer12setRecursiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer12setRecursiveEb'
    self.uglySide.call(ritual, recursive)

  @overload(QSGLayer.Format)
  def setFormat(self, a0: QSGLayer.Format) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setFormat(Format a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setFormat

    Parameters
    ----------

    a0 : QSGLayer.Format
      Passed on as its number.
    """
    #  void QSGSoftwareLayer::setFormat(Format a0)
    ritual = 'ritual_ZN16QSGSoftwareLayer9setFormatEN8QSGLayer6FormatE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer9setFormatEN8QSGLayer6FormatE'
    self.uglySide.call(ritual, a0.value)

  @overload(bool)
  def setHasMipmaps(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setHasMipmaps(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setHasMipmaps

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setHasMipmaps(bool a0)
    ritual = 'ritual_ZN16QSGSoftwareLayer13setHasMipmapsEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer13setHasMipmapsEb'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setDevicePixelRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setDevicePixelRatio(qreal ratio)
    ritual = 'ritual_ZN16QSGSoftwareLayer19setDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer19setDevicePixelRatioEd'
    self.uglySide.call(ritual, ratio)

  @overload(bool)
  def setMirrorHorizontal(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setMirrorHorizontal(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setMirrorHorizontal

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setMirrorHorizontal(bool mirror)
    ritual = 'ritual_ZN16QSGSoftwareLayer19setMirrorHorizontalEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer19setMirrorHorizontalEb'
    self.uglySide.call(ritual, mirror)

  @overload(bool)
  def setMirrorVertical(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setMirrorVertical(bool mirror)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setMirrorVertical

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setMirrorVertical(bool mirror)
    ritual = 'ritual_ZN16QSGSoftwareLayer17setMirrorVerticalEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer17setMirrorVerticalEb'
    self.uglySide.call(ritual, mirror)

  @overload(int)
  def setSamples(self, a0: int) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::setSamples(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#setSamples

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSGSoftwareLayer::setSamples(int a0)
    ritual = 'ritual_ZN16QSGSoftwareLayer10setSamplesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer10setSamplesEi'
    self.uglySide.call(ritual, a0)

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
    Qt's 'QSGSoftwareLayer::QSGSoftwareLayer(QSGRenderContext
    *renderContext)': leans on
    'QSGSoftwareLayer::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareLayer.__init__' has no cute function yet. Qt's "
        "'QSGSoftwareLayer::QSGSoftwareLayer(QSGRenderContext "
        "*renderContext)': leans on "
        "'QSGSoftwareLayer::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'bool QSGSoftwareLayer::updateTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#updateTexture
    """
    #  bool QSGSoftwareLayer::updateTexture()
    return self.uglySide.call('ritual_ZN16QSGSoftwareLayer13updateTextureEv')

  def scheduleUpdate(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::scheduleUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#scheduleUpdate
    """
    #  void QSGSoftwareLayer::scheduleUpdate()
    ritual = 'ritual_ZN16QSGSoftwareLayer14scheduleUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer14scheduleUpdateEv'
    self.uglySide.call(ritual)

  def markDirtyTexture(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::markDirtyTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarelayer.html#markDirtyTexture
    """
    #  void QSGSoftwareLayer::markDirtyTexture()
    ritual = 'ritual_ZN16QSGSoftwareLayer16markDirtyTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer16markDirtyTextureEv'
    self.uglySide.call(ritual)

  def invalidated(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareLayer::invalidated()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarelayer.html#invalidated
    """
    #  void QSGSoftwareLayer::invalidated()
    ritual = 'ritual_ZN16QSGSoftwareLayer11invalidatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QSGSoftwareLayer11invalidatedEv'
    self.uglySide.call(ritual)

  @staticmethod
  def grab(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareLayer::grab()': leans on
    'QSGSoftwarePixmapRenderer::render(QPaintDevice*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareLayer.grab' has no cute function yet. Qt's 'void "
        "QSGSoftwareLayer::grab()': leans on "
        "'QSGSoftwarePixmapRenderer::render(QPaintDevice*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
