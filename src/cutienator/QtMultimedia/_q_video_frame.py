"""
QVideoFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qvideoframe.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QtVideo, QVideoFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF, QSize
  from ..QtGui import QImage, QPainter
  from . import QAbstractVideoBuffer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractVideoBuffer = WAIT['QAbstractVideoBuffer']
  QImage = WAIT['QImage']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVideoFrame: a plain Python object standing in front
  of one C++ QVideoFrame.

  C++ hands a QVideoFrame around as a copy, so every C++ QVideoFrame behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVideoFrame that has a ritual and that Python can
  call so far, 35 names in all: '__eq__', '__ne__', 'isValid', 'pixelFormat',
  'surfaceFormat', 'handleType', 'size', 'width', 'height', 'isMapped',
  'isReadable', 'isWritable', 'mapMode', 'map', 'unmap', 'bytesPerLine',
  'mappedBytes', 'planeCount', 'startTime', 'setStartTime', 'endTime',
  'setEndTime', 'setRotationAngle', 'rotationAngle', 'setRotation',
  'rotation', 'setMirrored', 'mirrored', 'setStreamFrameRate',
  'streamFrameRate', 'toImage', 'subtitleText', 'setSubtitleText', 'paint',
  'videoBuffer'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoFrame::~QVideoFrame()': the destructor: Python removes its
    C++ QVideoFrame by it, and has no other use for it.
  - Qt's 'QVideoFrame::QVideoFrame(QVideoFrame &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVideoFrame &QVideoFrame::operator=(QVideoFrame &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QVideoFrame::swap(QVideoFrame &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVideoFrame &QVideoFrame::operator=(const QVideoFrame &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const uchar *QVideoFrame::bits(int plane) const': gives 'unsigned
    char', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 51 functions Qt declares: 3 not a gap; 1 takes or gives a type
  that cannot be passed yet; 1 the compiler refuses its ritual as it would be
  written here.

  What to expect
  --------------

  - The C++ QVideoFrame is created at the first use, not by
    'QVideoFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVideoFrame back gives a copy the ritual made for
    Python, in a new cute QVideoFrame.
  - Each name of Qt's QVideoFrame that has no cute function yet, 'bits',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QVideoFrame, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class HandleType(CuteNum):
    """
    The enum 'QVideoFrame::HandleType' of Qt, with the 2 names Qt gives in
    it.
    """

    NoHandle = Kee[int](0)
    RhiTextureHandle = Kee[int](1)

  class MapMode(CuteNum):
    """
    The enum 'QVideoFrame::MapMode' of Qt, with the 4 names Qt gives in it.
    """

    NotMapped = Kee[int](0)
    ReadOnly = Kee[int](1)
    WriteOnly = Kee[int](2)
    ReadWrite = Kee[int](3)

  class RotationAngle(CuteNum):
    """
    The enum 'QVideoFrame::RotationAngle' of Qt, with the 4 names Qt gives in
    it.
    """

    Rotation0 = Kee[int](0)
    Rotation90 = Kee[int](90)
    Rotation180 = Kee[int](180)
    Rotation270 = Kee[int](270)

  #  The classes Qt writes inside QVideoFrame, each a class in here as in
  #  C++.

  class PaintOptions(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QVideoFrame::PaintOptions: a plain Python object
    standing in front of one C++ QVideoFrame::PaintOptions.

    C++ hands a QVideoFrame::PaintOptions around as a copy, so every C++
    QVideoFrame::PaintOptions behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QVideoFrame::PaintOptions yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QVideoFrame::PaintOptions::~PaintOptions()': the destructor:
      Python removes its C++ QVideoFrame::PaintOptions by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QVideoFrame::PaintOptions is created at the first use, not by
      'QVideoFrame::PaintOptions(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QVideoFrame::PaintOptions back gives a copy the
      ritual made for Python, in a new cute QVideoFrame::PaintOptions.
    """

    #  The enums Qt writes inside QVideoFrame::PaintOptions, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class PaintFlag(CuteFlags):
      """
      The flags enum 'QVideoFrame::PaintOptions::PaintFlag' of Qt, with the 1
      names Qt gives in it. Qt names the type of its combinations
      'QVideoFrame::PaintOptions::PaintFlags'.
      """

      DontDrawSubtitles = 0x1

    PaintFlags = PaintFlag

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QVideoFrame::PaintOptions'

    #  Qt's '~QVideoFrame::PaintOptions()'. Naming it makes this a value
    #  class: Python owns every C++ QVideoFrame::PaintOptions behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QVideoFrame12PaintOptionsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoFrame'

  #  Qt's '~QVideoFrame()'. Naming it makes this a value class: Python owns
  #  every C++ QVideoFrame behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QVideoFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#isValid
    """
    #  bool QVideoFrame::isValid() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame7isValidEv')

  def pixelFormat(self) -> QVideoFrameFormat.PixelFormat:
    """
    Calls Qt's 'QVideoFrameFormat::PixelFormat QVideoFrame::pixelFormat()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#pixelFormat

    Returns
    -------

    QVideoFrameFormat.PixelFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrameFormat.PixelFormat(number)' gives.
    """
    #  QVideoFrameFormat::PixelFormat QVideoFrame::pixelFormat() const
    return QVideoFrameFormat.PixelFormat(self.uglySide.call(
        'ritual_ZNK11QVideoFrame11pixelFormatEv',
    ))

  def surfaceFormat(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QVideoFrame::surfaceFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#surfaceFormat

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QVideoFrame::surfaceFormat() const
    address = self.uglySide.call('ritual_ZNK11QVideoFrame13surfaceFormatEv')
    return QVideoFrameFormat._cuteOwning(address)

  def handleType(self) -> HandleType:
    """
    Calls Qt's 'QVideoFrame::HandleType QVideoFrame::handleType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#handleType

    Returns
    -------

    HandleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandleType(number)'
      gives.
    """
    #  QVideoFrame::HandleType QVideoFrame::handleType() const
    return QVideoFrame.HandleType(self.uglySide.call(
        'ritual_ZNK11QVideoFrame10handleTypeEv',
    ))

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QVideoFrame::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVideoFrame::size() const
    address = self.uglySide.call('ritual_ZNK11QVideoFrame4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QVideoFrame::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#width
    """
    #  int QVideoFrame::width() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QVideoFrame::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#height
    """
    #  int QVideoFrame::height() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame6heightEv')

  def isMapped(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::isMapped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#isMapped
    """
    #  bool QVideoFrame::isMapped() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame8isMappedEv')

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#isReadable
    """
    #  bool QVideoFrame::isReadable() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame10isReadableEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#isWritable
    """
    #  bool QVideoFrame::isWritable() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame10isWritableEv')

  def mapMode(self) -> MapMode:
    """
    Calls Qt's 'QVideoFrame::MapMode QVideoFrame::mapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#mapMode

    Returns
    -------

    MapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MapMode(number)' gives.
    """
    #  QVideoFrame::MapMode QVideoFrame::mapMode() const
    return QVideoFrame.MapMode(self.uglySide.call(
        'ritual_ZNK11QVideoFrame7mapModeEv',
    ))

  @overload(int)
  def bytesPerLine(self, plane: int) -> int:
    """
    Calls Qt's 'int QVideoFrame::bytesPerLine(int plane) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#bytesPerLine

    Parameters
    ----------

    plane : int
      Passed on as it is.
    """
    #  int QVideoFrame::bytesPerLine(int plane) const
    return self.uglySide.call(
        'ritual_ZNK11QVideoFrame12bytesPerLineEi', plane,
    )

  @overload(int)
  def mappedBytes(self, plane: int) -> int:
    """
    Calls Qt's 'int QVideoFrame::mappedBytes(int plane) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#mappedBytes

    Parameters
    ----------

    plane : int
      Passed on as it is.
    """
    #  int QVideoFrame::mappedBytes(int plane) const
    return self.uglySide.call(
        'ritual_ZNK11QVideoFrame11mappedBytesEi', plane,
    )

  def planeCount(self) -> int:
    """
    Calls Qt's 'int QVideoFrame::planeCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#planeCount
    """
    #  int QVideoFrame::planeCount() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame10planeCountEv')

  def startTime(self) -> int:
    """
    Calls Qt's 'qint64 QVideoFrame::startTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#startTime
    """
    #  qint64 QVideoFrame::startTime() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame9startTimeEv')

  def endTime(self) -> int:
    """
    Calls Qt's 'qint64 QVideoFrame::endTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#endTime
    """
    #  qint64 QVideoFrame::endTime() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame7endTimeEv')

  def rotationAngle(self) -> RotationAngle:
    """
    Calls Qt's 'RotationAngle QVideoFrame::rotationAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#rotationAngle

    Returns
    -------

    RotationAngle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RotationAngle(number)'
      gives.
    """
    #  RotationAngle QVideoFrame::rotationAngle() const
    return QVideoFrame.RotationAngle(self.uglySide.call(
        'ritual_ZNK11QVideoFrame13rotationAngleEv',
    ))

  def rotation(self) -> QtVideo.Rotation:
    """
    Calls Qt's 'QtVideo::Rotation QVideoFrame::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#rotation

    Returns
    -------

    QtVideo.Rotation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtVideo.Rotation(number)'
      gives.
    """
    #  QtVideo::Rotation QVideoFrame::rotation() const
    return QtVideo.Rotation(self.uglySide.call(
        'ritual_ZNK11QVideoFrame8rotationEv',
    ))

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::mirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#mirrored
    """
    #  bool QVideoFrame::mirrored() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame8mirroredEv')

  def streamFrameRate(self) -> float:
    """
    Calls Qt's 'qreal QVideoFrame::streamFrameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#streamFrameRate
    """
    #  qreal QVideoFrame::streamFrameRate() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame15streamFrameRateEv')

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QVideoFrame::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QVideoFrame::toImage() const
    address = self.uglySide.call('ritual_ZNK11QVideoFrame7toImageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def subtitleText(self) -> str:
    """
    Calls Qt's 'QString QVideoFrame::subtitleText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#subtitleText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVideoFrame::subtitleText() const
    return self.uglySide.call('ritual_ZNK11QVideoFrame12subtitleTextEv')

  def videoBuffer(self) -> Optional[QAbstractVideoBuffer]:
    """
    Calls Qt's 'QAbstractVideoBuffer *QVideoFrame::videoBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#videoBuffer

    Returns
    -------

    Optional[QAbstractVideoBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractVideoBuffer *QVideoFrame::videoBuffer() const
    address = self.uglySide.call('ritual_ZNK11QVideoFrame11videoBufferEv')
    from . import QAbstractVideoBuffer
    return QAbstractVideoBuffer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStartTime(self, time: int) -> None:
    """
    Calls Qt's 'void QVideoFrame::setStartTime(qint64 time)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#setStartTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QVideoFrame::setStartTime(qint64 time)
    self.uglySide.call('ritual_ZN11QVideoFrame12setStartTimeEx', time)

  @overload(int)
  def setEndTime(self, time: int) -> None:
    """
    Calls Qt's 'void QVideoFrame::setEndTime(qint64 time)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#setEndTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QVideoFrame::setEndTime(qint64 time)
    self.uglySide.call('ritual_ZN11QVideoFrame10setEndTimeEx', time)

  @overload(RotationAngle)
  def setRotationAngle(self, angle: RotationAngle) -> None:
    """
    Calls Qt's 'void QVideoFrame::setRotationAngle(RotationAngle angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#setRotationAngle

    Parameters
    ----------

    angle : RotationAngle
      Passed on as its number.
    """
    #  void QVideoFrame::setRotationAngle(RotationAngle angle)
    self.uglySide.call(
        'ritual_ZN11QVideoFrame16setRotationAngleENS_13RotationAngleE',
        angle.value,
    )

  @overload(QtVideo.Rotation)
  def setRotation(self, angle: QtVideo.Rotation) -> None:
    """
    Calls Qt's 'void QVideoFrame::setRotation(QtVideo::Rotation angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#setRotation

    Parameters
    ----------

    angle : QtVideo.Rotation
      Passed on as its number.
    """
    #  void QVideoFrame::setRotation(QtVideo::Rotation angle)
    self.uglySide.call(
        'ritual_ZN11QVideoFrame11setRotationEN7QtVideo8RotationE',
        angle.value,
    )

  @overload(bool)
  def setMirrored(self, a0: bool) -> None:
    """
    Calls Qt's 'void QVideoFrame::setMirrored(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#setMirrored

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QVideoFrame::setMirrored(bool a0)
    self.uglySide.call('ritual_ZN11QVideoFrame11setMirroredEb', a0)

  @overload(float)
  def setStreamFrameRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QVideoFrame::setStreamFrameRate(qreal rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframe.html#setStreamFrameRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QVideoFrame::setStreamFrameRate(qreal rate)
    self.uglySide.call('ritual_ZN11QVideoFrame18setStreamFrameRateEd', rate)

  @overload(str)
  def setSubtitleText(self, text: str) -> None:
    """
    Calls Qt's 'void QVideoFrame::setSubtitleText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#setSubtitleText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QVideoFrame::setSubtitleText(const QString &text)
    self.uglySide.call(
        'ritual_ZN11QVideoFrame15setSubtitleTextERK7QString', text,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QVideoFrame) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::operator==(const QVideoFrame &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#operator==

    Parameters
    ----------

    other : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  bool QVideoFrame::operator==(const QVideoFrame &other) const
    return self.uglySide.call(
        'ritual_ZNK11QVideoFrameeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QVideoFrame) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::operator!=(const QVideoFrame &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#operator!=

    Parameters
    ----------

    other : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  bool QVideoFrame::operator!=(const QVideoFrame &other) const
    return self.uglySide.call(
        'ritual_ZNK11QVideoFrameneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QVideoFrame::QVideoFrame()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#QVideoFrame
    """
    #  QVideoFrame::QVideoFrame()
    self._noteCreation(QVideoFrame, lambda: Rituals.call(
        'ritual_ZN11QVideoFrameC1Ev',
    ))

  @overload(QVideoFrameFormat)
  def __init__(self, format: QVideoFrameFormat) -> None:
    """
    Notes what was given, for Qt's 'QVideoFrame::QVideoFrame(const
    QVideoFrameFormat &format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#QVideoFrame

    Parameters
    ----------

    format : QVideoFrameFormat
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own.
    """
    #  QVideoFrame::QVideoFrame(const QVideoFrameFormat &format)
    self._noteCreation(QVideoFrame, lambda: Rituals.call(
        'ritual_ZN11QVideoFrameC1ERK17QVideoFrameFormat',
        self._valueOf(format),
    ))

  @overload(QImage)
  def __init__(self, image: QImage) -> None:
    """
    Notes what was given, for Qt's 'QVideoFrame::QVideoFrame(const QImage
    &image)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#QVideoFrame

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QVideoFrame::QVideoFrame(const QImage &image)
    self._noteCreation(QVideoFrame, lambda: Rituals.call(
        'ritual_ZN11QVideoFrameC1ERK6QImage', self._valueOf(image),
    ))

  @overload(THIS)
  def __init__(self, other: QVideoFrame) -> None:
    """
    Notes what was given, for Qt's 'QVideoFrame::QVideoFrame(const
    QVideoFrame &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#QVideoFrame

    Parameters
    ----------

    other : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  QVideoFrame::QVideoFrame(const QVideoFrame &other)
    self._noteCreation(QVideoFrame, lambda: Rituals.call(
        'ritual_ZN11QVideoFrameC1ERKS_', self._valueOf(other),
    ))

  @overload(QAbstractVideoBuffer, QVideoFrameFormat)
  @overload(NoneType, QVideoFrameFormat)
  def __init__(
      self,
      buffer: Optional[QAbstractVideoBuffer],
      format: QVideoFrameFormat,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QVideoFrame::QVideoFrame(QAbstractVideoBuffer *buffer, const
    QVideoFrameFormat &format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#QVideoFrame

    Parameters
    ----------

    buffer : Optional[QAbstractVideoBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QVideoFrameFormat
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own.
    """
    #  QVideoFrame::QVideoFrame(QAbstractVideoBuffer *buffer, const
    #      QVideoFrameFormat &format)
    self._noteCreation(QVideoFrame, lambda: Rituals.call(
        'ritual_ZN11QVideoFrameC1EP20QAbstractVideoBufferRK17QVideoFrameFor'
        'mat',
        self._addressOf(buffer), self._valueOf(format),
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

  @overload(MapMode)
  def map(self, mode: MapMode) -> bool:
    """
    Calls Qt's 'bool QVideoFrame::map(QVideoFrame::MapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#map

    Parameters
    ----------

    mode : MapMode
      Passed on as its number.
    """
    #  bool QVideoFrame::map(QVideoFrame::MapMode mode)
    return self.uglySide.call(
        'ritual_ZN11QVideoFrame3mapENS_7MapModeE', mode.value,
    )

  def unmap(self) -> None:
    """
    Calls Qt's 'void QVideoFrame::unmap()'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#unmap
    """
    #  void QVideoFrame::unmap()
    self.uglySide.call('ritual_ZN11QVideoFrame5unmapEv')

  @overload(QPainter, QRectF, PaintOptions)
  @overload(NoneType, QRectF, PaintOptions)
  def paint(
      self,
      painter: Optional[QPainter],
      rect: QRectF,
      options: PaintOptions,
  ) -> None:
    """
    Calls Qt's 'void QVideoFrame::paint(QPainter *painter, const QRectF
    &rect, const PaintOptions &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframe.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    options : PaintOptions
      Passed on as a value: Qt reads the C++ QVideoFrame::PaintOptions, which
      stays Python's own.
    """
    #  void QVideoFrame::paint(QPainter *painter, const QRectF &rect, const
    #      PaintOptions &options)
    self.uglySide.call(
        'ritual_ZN11QVideoFrame5paintEP8QPainterRK6QRectFRKNS_12PaintOption'
        'sE',
        self._addressOf(painter), self._valueOf(rect),
        self._valueOf(options),
    )

  @staticmethod
  def bits(*__, **_) -> Never:
    """
    - Qt's 'const uchar *QVideoFrame::bits(int plane) const': gives 'unsigned
      char', which has no cute class yet.
    - Qt's 'uchar *QVideoFrame::bits(int plane)': takes or gives a type that
      cannot be passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QVideoFrame.bits' has no cute function yet. Qt's 'const uchar "
        "*QVideoFrame::bits(int plane) const': gives 'unsigned char', which "
        "has no cute class yet. Qt's 'uchar *QVideoFrame::bits(int plane)': "
        "takes or gives a type that cannot be passed yet: uchar *.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QVideoFrame::swap(QVideoFrame &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVideoFrame.swap' has no cute function yet. Qt's 'void "
        "QVideoFrame::swap(QVideoFrame &other)': takes a type Python has no "
        "way to hand over yet.")
