"""
QPlatformBackingStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QSize
  from . import QBackingStore, QImage, QPaintDevice
  from . import QPlatformBackingStoreRhiConfig, QPlatformGraphicsBuffer
  from . import QPlatformTextureList, QRegion, QRhi, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBackingStore = WAIT['QBackingStore']
  QPlatformBackingStoreRhiConfig = WAIT['QPlatformBackingStoreRhiConfig']
  QPlatformTextureList = WAIT['QPlatformTextureList']
  QPoint = WAIT['QPoint']
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformBackingStore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformBackingStore: a plain Python object standing
  in front of one C++ QPlatformBackingStore.

  What exists
  -----------

  Every function of Qt's QPlatformBackingStore that has a ritual and that
  Python can call so far, 15 names in all: 'window', 'backingStore',
  'paintDevice', 'flush', 'rhiFlush', 'toImage', 'graphicsBuffer', 'resize',
  'scroll', 'beginPaint', 'endPaint', 'createRhi', 'rhi',
  'graphicsDeviceReportedLost', 'setBackingStore'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformBackingStore::~QPlatformBackingStore()': the destructor:
    Python never removes a C++ QPlatformBackingStore.
  - Qt's 'QRhiTexture
    *QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch
    *resourceUpdates, const QRegion &dirtyRegion, TextureFlags *flags)
    const': names 'QPlatformBackingStore::TextureFlags', which has no cute
    class yet.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QPlatformBackingStore is created at the first use, not by
    'QPlatformBackingStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformBackingStore.
  - Each name of Qt's QPlatformBackingStore that has no cute function yet,
    'surfaceAboutToBeDestroyed', 'toTexture', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformBackingStore, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class FlushResult(CuteNum):
    """
    The enum 'QPlatformBackingStore::FlushResult' of Qt, with the 3 names Qt
    gives in it.
    """

    FlushSuccess = Kee[int](0)
    FlushFailed = Kee[int](1)
    FlushFailedDueToLostDevice = Kee[int](2)

  class TextureFlag(CuteFlags):
    """
    The flags enum 'QPlatformBackingStore::TextureFlag' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QPlatformBackingStore::TextureFlags'.
    """

    TextureSwizzle = 0x1
    TextureFlip = 0x2
    TexturePremultiplied = 0x4

  TextureFlags = TextureFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformBackingStore'

  #  A C++ QPlatformBackingStore Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformBackingStore'

  #  The functions Qt calls itself that QPlatformBackingStore is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'toTexture': (
          'QRhiTexture '
          '*QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch *, '
          'const QRegion &, TextureFlags *) const',
      ),
  }

  #  The functions Qt calls itself that QPlatformBackingStore is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'paintDevice': (
          ('_ZN21QPlatformBackingStore11paintDeviceEv',
           ('address', 'address', 'QtGui:QPaintDevice'),
           ()),
      ),
      'flush': (
          ('_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
               ('address', 'value', 'QtGui:QRegion'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'rhiFlush': (
          ('_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPoi'
           'ntP20QPlatformTextureListbd',
           ('int', 'enum', 'QtGui:QPlatformBackingStore.FlushResult'),
           (
               ('address', 'address', 'QtGui:QWindow'),
               ('double', 'number', ''),
               ('address', 'value', 'QtGui:QRegion'),
               ('address', 'value', 'QtCore:QPoint'),
               ('address', 'address', 'QtGui:QPlatformTextureList'),
               ('bool', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'toImage': (
          ('_ZNK21QPlatformBackingStore7toImageEv',
           ('address', 'value', 'QtGui:QImage'),
           ()),
      ),
      'graphicsBuffer': (
          ('_ZNK21QPlatformBackingStore14graphicsBufferEv',
           ('address', 'address', 'QtGui:QPlatformGraphicsBuffer'),
           ()),
      ),
      'resize': (
          ('_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtGui:QRegion'),
           )),
      ),
      'scroll': (
          ('_ZN21QPlatformBackingStore6scrollERK7QRegionii',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QRegion'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'beginPaint': (
          ('_ZN21QPlatformBackingStore10beginPaintERK7QRegion',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QRegion'),
           )),
      ),
      'endPaint': (
          ('_ZN21QPlatformBackingStore8endPaintEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QPlatformBackingStore::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformbackingstore.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QPlatformBackingStore::window() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformBackingStore6windowEv',
    )
    from . import QWindow
    return QWindow._cuteAt(address)

  def backingStore(self) -> Optional[QBackingStore]:
    """
    Calls Qt's 'QBackingStore *QPlatformBackingStore::backingStore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#backingStore

    Returns
    -------

    Optional[QBackingStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackingStore *QPlatformBackingStore::backingStore() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformBackingStore12backingStoreEv',
    )
    from . import QBackingStore
    return QBackingStore._cuteAt(address)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QPlatformBackingStore::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformbackingstore.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QPlatformBackingStore::toImage() const
    ritual = 'ritual_ZNK21QPlatformBackingStore7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformBackingStore7toImageEv'
    address = self.uglySide.call(ritual)
    from . import QImage
    return QImage._cuteOwning(address)

  def graphicsBuffer(self) -> Optional[QPlatformGraphicsBuffer]:
    """
    Calls Qt's 'QPlatformGraphicsBuffer
    *QPlatformBackingStore::graphicsBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#graphicsBuffer

    Returns
    -------

    Optional[QPlatformGraphicsBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformGraphicsBuffer *QPlatformBackingStore::graphicsBuffer() const
    ritual = 'ritual_ZNK21QPlatformBackingStore14graphicsBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformBackingStore14graphicsBufferEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformGraphicsBuffer
    return QPlatformGraphicsBuffer._cuteAt(address)

  @overload(QWindow)
  @overload(NoneType)
  def rhi(self, window: Optional[QWindow]) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QPlatformBackingStore::rhi(QWindow *window) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformbackingstore.html#rhi

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QPlatformBackingStore::rhi(QWindow *window) const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformBackingStore3rhiEP7QWindow',
        self._addressOf(window),
    )
    from . import QRhi
    return QRhi._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBackingStore)
  @overload(NoneType)
  def setBackingStore(self, a0: Optional[QBackingStore]) -> None:
    """
    Calls Qt's 'void QPlatformBackingStore::setBackingStore(QBackingStore
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#setBackingStore

    Parameters
    ----------

    a0 : Optional[QBackingStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformBackingStore::setBackingStore(QBackingStore *a0)
    self.uglySide.call(
        'ritual_ZN21QPlatformBackingStore15setBackingStoreEP13QBackingStore',
        self._addressOf(a0),
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

  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformBackingStore::QPlatformBackingStore(QWindow *window)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#QPlatformBackingStore

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformBackingStore::QPlatformBackingStore(QWindow *window)
    self._noteCreation(QPlatformBackingStore, lambda: Rituals.call(
        'ritual_ZN21QPlatformBackingStoreC1EP7QWindow',
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
    Calls Qt's 'QPaintDevice *QPlatformBackingStore::paintDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#paintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QPlatformBackingStore::paintDevice()
    address = self.uglySide.call(
        'ritual_ZN21QPlatformBackingStore11paintDeviceEv',
    )
    from . import QPaintDevice
    return QPaintDevice._cuteAt(address)

  @overload(QWindow, QRegion, QPoint)
  @overload(NoneType, QRegion, QPoint)
  def flush(
      self,
      window: Optional[QWindow],
      region: QRegion,
      offset: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QPlatformBackingStore::flush(QWindow *window, const
    QRegion &region, const QPoint &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformbackingstore.html#flush

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
    #  void QPlatformBackingStore::flush(QWindow *window, const QRegion
    #      &region, const QPoint &offset)
    ritual = (
        'ritual_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoin'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK'
          '6QPoint')
    self.uglySide.call(
        ritual,
        self._addressOf(window), self._valueOf(region),
        self._valueOf(offset),
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
  ) -> FlushResult:
    """
    Calls Qt's 'FlushResult QPlatformBackingStore::rhiFlush(QWindow *window,
    qreal sourceDevicePixelRatio, const QRegion &region, const QPoint
    &offset, QPlatformTextureList *textures, bool translucentBackground,
    qreal sourceTransformFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#rhiFlush

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

    FlushResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlushResult(number)'
      gives.
    """
    #  FlushResult QPlatformBackingStore::rhiFlush(QWindow *window, qreal
    #      sourceDevicePixelRatio, const QRegion &region, const QPoint
    #      &offset, QPlatformTextureList *textures, bool
    #      translucentBackground, qreal sourceTransformFactor)
    ritual = (
        'ritual_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6Q'
        'PointP20QPlatformTextureListbd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegi'
          'onRK6QPointP20QPlatformTextureListbd')
    return QPlatformBackingStore.FlushResult(self.uglySide.call(
        ritual,
        self._addressOf(window), sourceDevicePixelRatio,
        self._valueOf(region), self._valueOf(offset),
        self._addressOf(textures), translucentBackground,
        sourceTransformFactor,
    ))

  @overload(QSize, QRegion)
  def resize(self, size: QSize, staticContents: QRegion) -> None:
    """
    Calls Qt's 'void QPlatformBackingStore::resize(const QSize &size, const
    QRegion &staticContents)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformbackingstore.html#resize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    staticContents : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPlatformBackingStore::resize(const QSize &size, const QRegion
    #      &staticContents)
    self.uglySide.call(
        'ritual_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion',
        self._valueOf(size), self._valueOf(staticContents),
    )

  @overload(QRegion, int, int)
  def scroll(self, area: QRegion, dx: int, dy: int) -> bool:
    """
    Calls Qt's 'bool QPlatformBackingStore::scroll(const QRegion &area, int
    dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformbackingstore.html#scroll

    Parameters
    ----------

    area : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  bool QPlatformBackingStore::scroll(const QRegion &area, int dx, int
    #      dy)
    ritual = 'ritual_ZN21QPlatformBackingStore6scrollERK7QRegionii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformBackingStore6scrollERK7QRegionii'
    return self.uglySide.call(ritual, self._valueOf(area), dx, dy)

  @overload(QRegion)
  def beginPaint(self, a0: QRegion) -> None:
    """
    Calls Qt's 'void QPlatformBackingStore::beginPaint(const QRegion &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#beginPaint

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPlatformBackingStore::beginPaint(const QRegion &a0)
    ritual = 'ritual_ZN21QPlatformBackingStore10beginPaintERK7QRegion'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformBackingStore10beginPaintERK7QRegion'
    self.uglySide.call(ritual, self._valueOf(a0))

  def endPaint(self) -> None:
    """
    Calls Qt's 'void QPlatformBackingStore::endPaint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#endPaint
    """
    #  void QPlatformBackingStore::endPaint()
    ritual = 'ritual_ZN21QPlatformBackingStore8endPaintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformBackingStore8endPaintEv'
    self.uglySide.call(ritual)

  @overload(QWindow, QPlatformBackingStoreRhiConfig)
  @overload(NoneType, QPlatformBackingStoreRhiConfig)
  def createRhi(
      self,
      window: Optional[QWindow],
      config: QPlatformBackingStoreRhiConfig,
  ) -> None:
    """
    Calls Qt's 'void QPlatformBackingStore::createRhi(QWindow *window,
    QPlatformBackingStoreRhiConfig config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html#createRhi

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QPlatformBackingStoreRhiConfig
      Passed on as a value: Qt reads the C++ QPlatformBackingStoreRhiConfig,
      which stays Python's own.
    """
    #  void QPlatformBackingStore::createRhi(QWindow *window,
    #      QPlatformBackingStoreRhiConfig config)
    self.uglySide.call(
        'ritual_ZN21QPlatformBackingStore9createRhiEP7QWindow30QPlatformBac'
        'kingStoreRhiConfig',
        self._addressOf(window), self._valueOf(config),
    )

  @overload(QWindow)
  @overload(NoneType)
  def graphicsDeviceReportedLost(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void
    QPlatformBackingStore::graphicsDeviceReportedLost(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstore.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformBackingStore::graphicsDeviceReportedLost(QWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN21QPlatformBackingStore26graphicsDeviceReportedLostEP7QWi'
        'ndow',
        self._addressOf(window),
    )

  @staticmethod
  def surfaceAboutToBeDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QPlatformBackingStore::surfaceAboutToBeDestroyed()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QPlatformBackingStore.surfaceAboutToBeDestroyed' has no cute "
        "function yet. Qt's 'void "
        "QPlatformBackingStore::surfaceAboutToBeDestroyed()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def toTexture(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture
    *QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch
    *resourceUpdates, const QRegion &dirtyRegion, TextureFlags *flags)
    const': names 'QPlatformBackingStore::TextureFlags', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QPlatformBackingStore.toTexture' has no cute function yet. Qt's "
        "'QRhiTexture "
        "*QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch "
        "*resourceUpdates, const QRegion &dirtyRegion, TextureFlags *flags) "
        "const': names 'QPlatformBackingStore::TextureFlags', which has no "
        "cute class yet.")
