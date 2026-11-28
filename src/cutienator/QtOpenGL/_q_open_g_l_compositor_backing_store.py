"""
QOpenGLCompositorBackingStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositorbackingstore_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QOpenGLCompositorBackingStore to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QPlatformBackingStore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QSize
  from ..QtGui import QImage, QPaintDevice, QPlatformTextureList, QRegion
  from ..QtGui import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformTextureList = WAIT['QPlatformTextureList']
  QPoint = WAIT['QPoint']
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLCompositorBackingStore(QPlatformBackingStore):
  """
  The cute side of Qt's QOpenGLCompositorBackingStore: a plain Python object
  standing in front of one C++ QOpenGLCompositorBackingStore.

  It is built on the cute 'QPlatformBackingStore', as Qt's
  QOpenGLCompositorBackingStore is built on Qt's QPlatformBackingStore, and
  has everything that class has.

  C++ hands a QOpenGLCompositorBackingStore around as a copy, so every C++
  QOpenGLCompositorBackingStore behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpenGLCompositorBackingStore that has a ritual and
  that Python can call so far, 9 names in all: 'paintDevice', 'beginPaint',
  'flush', 'resize', 'toImage', 'rhiFlush', 'textures', 'notifyComposited',
  'updateTexture'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLCompositorBackingStore::~QOpenGLCompositorBackingStore()':
    the destructor: Python removes its C++ QOpenGLCompositorBackingStore by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLCompositorBackingStore is created at the first use, not by
    'QOpenGLCompositorBackingStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLCompositorBackingStore back gives a copy the
    ritual made for Python, in a new cute QOpenGLCompositorBackingStore.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLCompositorBackingStore'

  #  A C++ QOpenGLCompositorBackingStore Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLCompositorBackingStore'

  #  Qt's '~QOpenGLCompositorBackingStore()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLCompositorBackingStore behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QOpenGLCompositorBackingStoreD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLCompositorBackingStore::toImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLCompositorBackingStore::toImage() const
    ritual = 'ritual_ZNK29QOpenGLCompositorBackingStore7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QOpenGLCompositorBackingStore7toImageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def textures(self) -> Optional[QPlatformTextureList]:
    """
    Calls Qt's 'const QPlatformTextureList
    *QOpenGLCompositorBackingStore::textures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#textures

    Returns
    -------

    Optional[QPlatformTextureList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlatformTextureList *QOpenGLCompositorBackingStore::textures()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QOpenGLCompositorBackingStore8texturesEv',
    )
    from ..QtGui import QPlatformTextureList
    return QPlatformTextureList._cuteAt(address)

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

  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLCompositorBackingStore::QOpenGLCompositorBackingStore(QWindow
    *window)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLCompositorBackingStore::QOpenGLCompositorBackingStore(QWindow
    #      *window)
    self._noteCreation(QOpenGLCompositorBackingStore, lambda: Rituals.call(
        'ritual_ZN29QOpenGLCompositorBackingStoreC1EP7QWindow',
        self._addressOf(window),
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

  def paintDevice(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QOpenGLCompositorBackingStore::paintDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#paintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QOpenGLCompositorBackingStore::paintDevice()
    ritual = 'ritual_ZN29QOpenGLCompositorBackingStore11paintDeviceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QOpenGLCompositorBackingStore11paintDeviceEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintDevice
    return QPaintDevice._cuteAt(address)

  @overload(QRegion)
  def beginPaint(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorBackingStore::beginPaint(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#beginPaint

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QOpenGLCompositorBackingStore::beginPaint(const QRegion &region)
    ritual = (
        'ritual_ZN29QOpenGLCompositorBackingStore10beginPaintERK7QRegion')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QOpenGLCompositorBackingStore10beginPaintERK7QReg'
          'ion')
    self.uglySide.call(ritual, self._valueOf(region))

  @overload(QWindow, QRegion, QPoint)
  @overload(NoneType, QRegion, QPoint)
  def flush(
      self,
      window: Optional[QWindow],
      region: QRegion,
      offset: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorBackingStore::flush(QWindow *window,
    const QRegion &region, const QPoint &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#flush

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QOpenGLCompositorBackingStore::flush(QWindow *window, const
    #      QRegion &region, const QPoint &offset)
    ritual = (
        'ritual_ZN29QOpenGLCompositorBackingStore5flushEP7QWindowRK7QRegion'
        'RK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QOpenGLCompositorBackingStore5flushEP7QWindowRK7Q'
          'RegionRK6QPoint')
    self.uglySide.call(
        ritual,
        self._addressOf(window), self._valueOf(region),
        self._valueOf(offset),
    )

  @overload(QSize, QRegion)
  def resize(self, size: QSize, staticContents: QRegion) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorBackingStore::resize(const QSize &size,
    const QRegion &staticContents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#resize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    staticContents : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QOpenGLCompositorBackingStore::resize(const QSize &size, const
    #      QRegion &staticContents)
    ritual = (
        'ritual_ZN29QOpenGLCompositorBackingStore6resizeERK5QSizeRK7QRegion')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QOpenGLCompositorBackingStore6resizeERK5QSizeRK7Q'
          'Region')
    self.uglySide.call(
        ritual, self._valueOf(size), self._valueOf(staticContents),
    )

  @overload(QWindow, float, QRegion, QPoint, QPlatformTextureList, bool)
  @overload(QWindow, float, QRegion, QPoint, NoneType, bool)
  @overload(NoneType, float, QRegion, QPoint, QPlatformTextureList, bool)
  @overload(NoneType, float, QRegion, QPoint, NoneType, bool)
  @overload(
      QWindow, float, QRegion, QPoint, QPlatformTextureList, bool, float,
  )
  @overload(QWindow, float, QRegion, QPoint, NoneType, bool, float)
  @overload(
      NoneType, float, QRegion, QPoint, QPlatformTextureList, bool, float,
  )
  @overload(NoneType, float, QRegion, QPoint, NoneType, bool, float)
  def rhiFlush(
      self,
      window: Optional[QWindow],
      sourceDevicePixelRatio: float,
      region: QRegion,
      offset: QPoint,
      textures: Optional[QPlatformTextureList],
      translucentBackground: bool,
      sourceTransformFactor: float = 0.0,
  ) -> QPlatformBackingStore.FlushResult:
    """
    Calls Qt's 'FlushResult QOpenGLCompositorBackingStore::rhiFlush(QWindow
    *window, qreal sourceDevicePixelRatio, const QRegion &region, const
    QPoint &offset, QPlatformTextureList *textures, bool
    translucentBackground, qreal sourceTransformFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#rhiFlush

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceDevicePixelRatio : float
      Passed on as it is.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    textures : Optional[QPlatformTextureList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    translucentBackground : bool
      Passed on as it is.

    sourceTransformFactor : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QPlatformBackingStore.FlushResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformBackingStore.FlushResult(number)' gives.
    """
    #  FlushResult QOpenGLCompositorBackingStore::rhiFlush(QWindow *window,
    #      qreal sourceDevicePixelRatio, const QRegion &region, const QPoint
    #      &offset, QPlatformTextureList *textures, bool
    #      translucentBackground, qreal sourceTransformFactor)
    ritual = (
        'ritual_ZN29QOpenGLCompositorBackingStore8rhiFlushEP7QWindowdRK7QRe'
        'gionRK6QPointP20QPlatformTextureListbd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QOpenGLCompositorBackingStore8rhiFlushEP7QWindowd'
          'RK7QRegionRK6QPointP20QPlatformTextureListbd')
    return QPlatformBackingStore.FlushResult(self.uglySide.call(
        ritual,
        self._addressOf(window), sourceDevicePixelRatio,
        self._valueOf(region), self._valueOf(offset),
        self._addressOf(textures), translucentBackground,
        sourceTransformFactor,
    ))

  def notifyComposited(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorBackingStore::notifyComposited()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html
    """
    #  void QOpenGLCompositorBackingStore::notifyComposited()
    self.uglySide.call(
        'ritual_ZN29QOpenGLCompositorBackingStore16notifyCompositedEv',
    )

  def updateTexture(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorBackingStore::updateTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorbackingstore.html#updateTexture
    """
    #  void QOpenGLCompositorBackingStore::updateTexture()
    self.uglySide.call(
        'ritual_ZN29QOpenGLCompositorBackingStore13updateTextureEv',
    )
