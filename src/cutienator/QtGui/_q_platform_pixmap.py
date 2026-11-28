"""
QPlatformPixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformpixmap.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QSharedData
from . import QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QBitmap, QColor, QImage, QImageReader, QPaintEngine, QPixmap
  from . import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBitmap = WAIT['QBitmap']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QImageReader = WAIT['QImageReader']
  QRect = WAIT['QRect']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformPixmap(QSharedData):
  """
  The cute side of Qt's QPlatformPixmap: a plain Python object standing in
  front of one C++ QPlatformPixmap.

  It is built on the cute 'QSharedData', as Qt's QPlatformPixmap is built on
  Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformPixmap that has a ritual and that Python
  can call so far, 31 names in all: 'createCompatiblePlatformPixmap',
  'resize', 'fromImage', 'fromImageReader', 'fromFile', 'copy', 'scroll',
  'metric', 'fill', 'mask', 'setMask', 'hasAlphaChannel', 'transformed',
  'toImage', 'paintEngine', 'serialNumber', 'pixelType', 'classId',
  'devicePixelRatio', 'setDevicePixelRatio', 'buffer', 'width', 'height',
  'colorCount', 'depth', 'isNull', 'cacheKey', 'create', 'setSerialNumber',
  'setDetachNumber', 'callDestructionHooks'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformPixmap::~QPlatformPixmap()': the destructor: Python never
    removes a C++ QPlatformPixmap.
  - Qt's 'void QPlatformPixmap::fromImageInPlace(QImage &image,
    Qt::ImageConversionFlags flags)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QPlatformPixmap::fromData(const uchar *buffer, uint len, const
    char *format, Qt::ImageConversionFlags flags)': names 'uchar', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ QPlatformPixmap is created at the first use, not by
    'QPlatformPixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformPixmap.
  - Each name of Qt's QPlatformPixmap that has no cute function yet,
    'fromData', 'fromImageInPlace', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformPixmap, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ClassId(CuteNum):
    """
    The enum 'QPlatformPixmap::ClassId' of Qt, with the 5 names Qt gives in
    it.
    """

    RasterClass = Kee[int](0)
    DirectFBClass = Kee[int](1)
    BlitterClass = Kee[int](2)
    Direct2DClass = Kee[int](3)
    CustomClass = Kee[int](1024)

  class PixelType(CuteNum):
    """
    The enum 'QPlatformPixmap::PixelType' of Qt, with the 2 names Qt gives in
    it.
    """

    PixmapType = Kee[int](0)
    BitmapType = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int, PixelType)
  def create(w: int, h: int, type: PixelType) -> Optional[QPlatformPixmap]:
    """
    Calls Qt's 'QPlatformPixmap *QPlatformPixmap::create(int w, int h,
    PixelType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#create

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    type : PixelType
      Passed on as its number.

    Returns
    -------

    Optional[QPlatformPixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformPixmap *QPlatformPixmap::create(int w, int h, PixelType type)
    address = Rituals.call(
        'ritual_ZN15QPlatformPixmap6createEiiNS_9PixelTypeE',
        w, h, type.value,
    )
    return QPlatformPixmap._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformPixmap'

  #  A C++ QPlatformPixmap Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformPixmap'

  #  The functions Qt calls itself that QPlatformPixmap is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'fromImageInPlace': (
          'void QPlatformPixmap::fromImageInPlace(QImage &, '
          'Qt::ImageConversionFlags)',
      ),
      'fromFile': (
          'bool QPlatformPixmap::fromFile(const QString &, const char *, '
          'Qt::ImageConversionFlags)',
      ),
      'fromData': (
          'bool QPlatformPixmap::fromData(const uchar *, uint, const char '
          '*, Qt::ImageConversionFlags)',
      ),
  }

  #  The functions Qt calls itself that QPlatformPixmap is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createCompatiblePlatformPixmap': (
          ('_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapEv',
           ('address', 'address', 'QtGui:QPlatformPixmap'),
           ()),
      ),
      'resize': (
          ('_ZN15QPlatformPixmap6resizeEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'fromImage': (
          ('_ZN15QPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConv'
           'ersionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QImage'),
               ('int', 'flags', 'QtCore:Qt.ImageConversionFlag'),
           )),
      ),
      'fromImageReader': (
          ('_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6QFlagsIN2'
           'Qt19ImageConversionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QImageReader'),
               ('int', 'flags', 'QtCore:Qt.ImageConversionFlag'),
           )),
      ),
      'copy': (
          ('_ZN15QPlatformPixmap4copyEPKS_RK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformPixmap'),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'scroll': (
          ('_ZN15QPlatformPixmap6scrollEiiRK5QRect',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'metric': (
          ('_ZNK15QPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMetric'
           'E',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPaintDevice.PaintDeviceMetric'),
           )),
      ),
      'fill': (
          ('_ZN15QPlatformPixmap4fillERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'mask': (
          ('_ZNK15QPlatformPixmap4maskEv',
           ('address', 'value', 'QtGui:QBitmap'),
           ()),
      ),
      'setMask': (
          ('_ZN15QPlatformPixmap7setMaskERK7QBitmap',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QBitmap'),
           )),
      ),
      'hasAlphaChannel': (
          ('_ZNK15QPlatformPixmap15hasAlphaChannelEv',
           ('bool', 'number', ''),
           ()),
      ),
      'transformed': (
          ('_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt18Transfor'
           'mationModeE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'value', 'QtGui:QTransform'),
               ('int', 'enum', 'QtCore:Qt.TransformationMode'),
           )),
      ),
      'toImage': (
          ('_ZNK15QPlatformPixmap7toImageEv',
           ('address', 'value', 'QtGui:QImage'),
           ()),
          ('_ZNK15QPlatformPixmap7toImageERK5QRect',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'paintEngine': (
          ('_ZNK15QPlatformPixmap11paintEngineEv',
           ('address', 'address', 'QtGui:QPaintEngine'),
           ()),
      ),
      'devicePixelRatio': (
          ('_ZNK15QPlatformPixmap16devicePixelRatioEv',
           ('double', 'number', ''),
           ()),
      ),
      'setDevicePixelRatio': (
          ('_ZN15QPlatformPixmap19setDevicePixelRatioEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'buffer': (
          ('_ZN15QPlatformPixmap6bufferEv',
           ('address', 'address', 'QtGui:QImage'),
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

  def createCompatiblePlatformPixmap(self) -> Optional[QPlatformPixmap]:
    """
    Calls Qt's 'QPlatformPixmap
    *QPlatformPixmap::createCompatiblePlatformPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html

    Returns
    -------

    Optional[QPlatformPixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformPixmap *QPlatformPixmap::createCompatiblePlatformPixmap()
    #      const
    ritual = 'ritual_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QPlatformPixmap30createCompatiblePlatformPixmapE'
          'v')
    address = self.uglySide.call(ritual)
    return QPlatformPixmap._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric
    metric) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPlatformPixmap::metric(QPaintDevice::PaintDeviceMetric metric)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QPlatformPixmap6metricEN12QPaintDevice17PaintDeviceMet'
        'ricE',
        metric.value,
    )

  def mask(self) -> QBitmap:
    """
    Calls Qt's 'QBitmap QPlatformPixmap::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#mask

    Returns
    -------

    QBitmap
      A new cute QBitmap around the copy Qt gave back. Python owns it.
    """
    #  QBitmap QPlatformPixmap::mask() const
    ritual = 'ritual_ZNK15QPlatformPixmap4maskEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformPixmap4maskEv'
    address = self.uglySide.call(ritual)
    from . import QBitmap
    return QBitmap._cuteOwning(address)

  def hasAlphaChannel(self) -> bool:
    """
    Calls Qt's 'bool QPlatformPixmap::hasAlphaChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#hasAlphaChannel
    """
    #  bool QPlatformPixmap::hasAlphaChannel() const
    return self.uglySide.call(
        'ritual_ZNK15QPlatformPixmap15hasAlphaChannelEv',
    )

  @overload(QTransform, Qt.TransformationMode)
  def transformed(
      self,
      matrix: QTransform,
      mode: Qt.TransformationMode,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QPlatformPixmap::transformed(const QTransform
    &matrix, Qt::TransformationMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#transformed

    Parameters
    ----------

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    mode : Qt.TransformationMode
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPlatformPixmap::transformed(const QTransform &matrix,
    #      Qt::TransformationMode mode) const
    ritual = (
        'ritual_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt18Trans'
        'formationModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QPlatformPixmap11transformedERK10QTransformN2Qt1'
          '8TransformationModeE')
    address = self.uglySide.call(ritual, self._valueOf(matrix), mode.value)
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload()
  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QPlatformPixmap::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QPlatformPixmap::toImage() const
    address = self.uglySide.call('ritual_ZNK15QPlatformPixmap7toImageEv')
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(QRect)
  def toImage(self, rect: QRect) -> QImage:
    """
    Calls Qt's 'QImage QPlatformPixmap::toImage(const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#toImage

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QPlatformPixmap::toImage(const QRect &rect) const
    ritual = 'ritual_ZNK15QPlatformPixmap7toImageERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformPixmap7toImageERK5QRect'
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from . import QImage
    return QImage._cuteOwning(address)

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPlatformPixmap::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPlatformPixmap::paintEngine() const
    address = self.uglySide.call(
        'ritual_ZNK15QPlatformPixmap11paintEngineEv',
    )
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def serialNumber(self) -> int:
    """
    Calls Qt's 'int QPlatformPixmap::serialNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#serialNumber
    """
    #  int QPlatformPixmap::serialNumber() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap12serialNumberEv')

  def pixelType(self) -> PixelType:
    """
    Calls Qt's 'PixelType QPlatformPixmap::pixelType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#pixelType

    Returns
    -------

    PixelType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PixelType(number)' gives.
    """
    #  PixelType QPlatformPixmap::pixelType() const
    return QPlatformPixmap.PixelType(self.uglySide.call(
        'ritual_ZNK15QPlatformPixmap9pixelTypeEv',
    ))

  def classId(self) -> ClassId:
    """
    Calls Qt's 'ClassId QPlatformPixmap::classId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#classId

    Returns
    -------

    ClassId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClassId(number)' gives.
    """
    #  ClassId QPlatformPixmap::classId() const
    return QPlatformPixmap.ClassId(self.uglySide.call(
        'ritual_ZNK15QPlatformPixmap7classIdEv',
    ))

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QPlatformPixmap::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#devicePixelRatio
    """
    #  qreal QPlatformPixmap::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK15QPlatformPixmap16devicePixelRatioEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int QPlatformPixmap::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#width
    """
    #  int QPlatformPixmap::width() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QPlatformPixmap::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#height
    """
    #  int QPlatformPixmap::height() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap6heightEv')

  def colorCount(self) -> int:
    """
    Calls Qt's 'int QPlatformPixmap::colorCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#colorCount
    """
    #  int QPlatformPixmap::colorCount() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap10colorCountEv')

  def depth(self) -> int:
    """
    Calls Qt's 'int QPlatformPixmap::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#depth
    """
    #  int QPlatformPixmap::depth() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap5depthEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPlatformPixmap::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#isNull
    """
    #  bool QPlatformPixmap::isNull() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap6isNullEv')

  def cacheKey(self) -> int:
    """
    Calls Qt's 'qint64 QPlatformPixmap::cacheKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#cacheKey
    """
    #  qint64 QPlatformPixmap::cacheKey() const
    return self.uglySide.call('ritual_ZNK15QPlatformPixmap8cacheKeyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBitmap)
  def setMask(self, mask: QBitmap) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::setMask(const QBitmap &mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#setMask

    Parameters
    ----------

    mask : QBitmap
      Passed on as a value: Qt reads the C++ QBitmap, which stays Python's
      own.
    """
    #  void QPlatformPixmap::setMask(const QBitmap &mask)
    ritual = 'ritual_ZN15QPlatformPixmap7setMaskERK7QBitmap'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformPixmap7setMaskERK7QBitmap'
    self.uglySide.call(ritual, self._valueOf(mask))

  @overload(float)
  def setDevicePixelRatio(self, scaleFactor: float) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::setDevicePixelRatio(qreal
    scaleFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#setDevicePixelRatio

    Parameters
    ----------

    scaleFactor : float
      Passed on as it is.
    """
    #  void QPlatformPixmap::setDevicePixelRatio(qreal scaleFactor)
    self.uglySide.call(
        'ritual_ZN15QPlatformPixmap19setDevicePixelRatioEd', scaleFactor,
    )

  @overload(int)
  def setSerialNumber(self, serNo: int) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::setSerialNumber(int serNo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#setSerialNumber

    Parameters
    ----------

    serNo : int
      Passed on as it is.
    """
    #  void QPlatformPixmap::setSerialNumber(int serNo)
    self.uglySide.call(
        'ritual_ZN15QPlatformPixmap15setSerialNumberEi', serNo,
    )

  @overload(int)
  def setDetachNumber(self, detNo: int) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::setDetachNumber(int detNo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#setDetachNumber

    Parameters
    ----------

    detNo : int
      Passed on as it is.
    """
    #  void QPlatformPixmap::setDetachNumber(int detNo)
    self.uglySide.call(
        'ritual_ZN15QPlatformPixmap15setDetachNumberEi', detNo,
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

  @overload(PixelType, int)
  def __init__(self, pixelType: PixelType, classId: int) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformPixmap::QPlatformPixmap(PixelType pixelType, int classId)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#QPlatformPixmap

    Parameters
    ----------

    pixelType : PixelType
      Passed on as its number.

    classId : int
      Passed on as it is.
    """
    #  QPlatformPixmap::QPlatformPixmap(PixelType pixelType, int classId)
    self._noteCreation(QPlatformPixmap, lambda: Rituals.call(
        'ritual_ZN15QPlatformPixmapC1ENS_9PixelTypeEi',
        pixelType.value, classId,
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

  @overload(int, int)
  def resize(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::resize(int width, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#resize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QPlatformPixmap::resize(int width, int height)
    self.uglySide.call('ritual_ZN15QPlatformPixmap6resizeEii', width, height)

  @overload(QImage, Qt.ImageConversionFlags)
  def fromImage(self, image: QImage, flags: Qt.ImageConversionFlags) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::fromImage(const QImage &image,
    Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#fromImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  void QPlatformPixmap::fromImage(const QImage &image,
    #      Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN15QPlatformPixmap9fromImageERK6QImage6QFlagsIN2Qt19ImageC'
        'onversionFlagEE',
        self._valueOf(image), flags.value,
    )

  @overload(QImageReader, Qt.ImageConversionFlags)
  @overload(NoneType, Qt.ImageConversionFlags)
  def fromImageReader(
      self,
      imageReader: Optional[QImageReader],
      flags: Qt.ImageConversionFlags,
  ) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::fromImageReader(QImageReader
    *imageReader, Qt::ImageConversionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#fromImageReader

    Parameters
    ----------

    imageReader : Optional[QImageReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  void QPlatformPixmap::fromImageReader(QImageReader *imageReader,
    #      Qt::ImageConversionFlags flags)
    ritual = (
        'ritual_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6QFlags'
        'IN2Qt19ImageConversionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QPlatformPixmap15fromImageReaderEP12QImageReader6'
          'QFlagsIN2Qt19ImageConversionFlagEE')
    self.uglySide.call(ritual, self._addressOf(imageReader), flags.value)

  @overload(str, str, Qt.ImageConversionFlags)
  @overload(str, NoneType, Qt.ImageConversionFlags)
  def fromFile(
      self,
      filename: str,
      format: Optional[str],
      flags: Qt.ImageConversionFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QPlatformPixmap::fromFile(const QString &filename, const
    char *format, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#fromFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    flags : Qt.ImageConversionFlags
      Passed on as its number.
    """
    #  bool QPlatformPixmap::fromFile(const QString &filename, const char
    #      *format, Qt::ImageConversionFlags flags)
    return self.uglySide.call(
        'ritual_ZN15QPlatformPixmap8fromFileERK7QStringPKc6QFlagsIN2Qt19Ima'
        'geConversionFlagEE',
        filename, self._bytesOf(format), flags.value,
    )

  @overload(THIS, QRect)
  @overload(NoneType, QRect)
  def copy(self, data: Optional[QPlatformPixmap], rect: QRect) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::copy(const QPlatformPixmap *data, const
    QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#copy

    Parameters
    ----------

    data : Optional[QPlatformPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPlatformPixmap::copy(const QPlatformPixmap *data, const QRect
    #      &rect)
    ritual = 'ritual_ZN15QPlatformPixmap4copyEPKS_RK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformPixmap4copyEPKS_RK5QRect'
    self.uglySide.call(ritual, self._addressOf(data), self._valueOf(rect))

  @overload(int, int, QRect)
  def scroll(self, dx: int, dy: int, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QPlatformPixmap::scroll(int dx, int dy, const QRect
    &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#scroll

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QPlatformPixmap::scroll(int dx, int dy, const QRect &rect)
    ritual = 'ritual_ZN15QPlatformPixmap6scrollEiiRK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformPixmap6scrollEiiRK5QRect'
    return self.uglySide.call(ritual, dx, dy, self._valueOf(rect))

  @overload(QColor)
  def fill(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::fill(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#fill

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPlatformPixmap::fill(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QPlatformPixmap4fillERK6QColor', self._valueOf(color),
    )

  def buffer(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage *QPlatformPixmap::buffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformpixmap.html#buffer

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QPlatformPixmap::buffer()
    ritual = 'ritual_ZN15QPlatformPixmap6bufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformPixmap6bufferEv'
    address = self.uglySide.call(ritual)
    from . import QImage
    return QImage._cuteAt(address)

  def callDestructionHooks(self) -> None:
    """
    Calls Qt's 'void QPlatformPixmap::callDestructionHooks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformpixmap.html#callDestructionHooks
    """
    #  void QPlatformPixmap::callDestructionHooks()
    self.uglySide.call('ritual_ZN15QPlatformPixmap20callDestructionHooksEv')

  @staticmethod
  def fromData(*__, **_) -> Never:
    """
    Qt's 'bool QPlatformPixmap::fromData(const uchar *buffer, uint len, const
    char *format, Qt::ImageConversionFlags flags)': names 'uchar', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformPixmap.fromData' has no cute function yet. Qt's 'bool "
        "QPlatformPixmap::fromData(const uchar *buffer, uint len, const "
        "char *format, Qt::ImageConversionFlags flags)': names 'uchar', "
        "which has no cute class yet.")

  @staticmethod
  def fromImageInPlace(*__, **_) -> Never:
    """
    Qt's 'void QPlatformPixmap::fromImageInPlace(QImage &image,
    Qt::ImageConversionFlags flags)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QPlatformPixmap.fromImageInPlace' has no cute function yet. Qt's "
        "'void QPlatformPixmap::fromImageInPlace(QImage &image, "
        "Qt::ImageConversionFlags flags)': takes a type Python has no way "
        "to hand over yet.")
