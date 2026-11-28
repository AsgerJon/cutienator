"""
QPixelFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QPixelFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPixelFormat: a plain Python object standing in front
  of one C++ QPixelFormat.

  C++ hands a QPixelFormat around as a copy, so every C++ QPixelFormat behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPixelFormat that has a ritual and that Python can
  call so far, 26 names in all: 'colorModel', 'channelCount', 'redSize',
  'greenSize', 'blueSize', 'cyanSize', 'magentaSize', 'yellowSize',
  'blackSize', 'hueSize', 'saturationSize', 'lightnessSize',
  'brightnessSize', 'alphaSize', 'bitsPerPixel', 'alphaUsage',
  'alphaPosition', 'premultiplied', 'typeInterpretation', 'byteOrder',
  'yuvLayout', 'subEnum', 'resolveByteOrder', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'uchar QPixelFormat::get(Field offset, FieldWidth width) const':
    names the enum 'QPixelFormat::Field', whose class cannot be named here.
  - Qt's 'quint64 QPixelFormat::set(Field offset, FieldWidth width, uchar
    value)': names the enum 'QPixelFormat::Field', whose class cannot be
    named here.
  - Qt's 'QPixelFormat::~QPixelFormat()': the destructor: Python removes its
    C++ QPixelFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 35 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPixelFormat is created at the first use, not by
    'QPixelFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPixelFormat back gives a copy the ritual made for
    Python, in a new cute QPixelFormat.
  - Each name of Qt's QPixelFormat that has no cute function yet, 'get',
    'set', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QPixelFormat, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AlphaPosition(CuteNum):
    """
    The enum 'QPixelFormat::AlphaPosition' of Qt, with the 2 names Qt gives
    in it.
    """

    AtBeginning = Kee[int](0)
    AtEnd = Kee[int](1)

  class AlphaPremultiplied(CuteNum):
    """
    The enum 'QPixelFormat::AlphaPremultiplied' of Qt, with the 2 names Qt
    gives in it.
    """

    NotPremultiplied = Kee[int](0)
    Premultiplied = Kee[int](1)

  class AlphaUsage(CuteNum):
    """
    The enum 'QPixelFormat::AlphaUsage' of Qt, with the 2 names Qt gives in
    it.
    """

    UsesAlpha = Kee[int](0)
    IgnoresAlpha = Kee[int](1)

  class ByteOrder(CuteNum):
    """
    The enum 'QPixelFormat::ByteOrder' of Qt, with the 3 names Qt gives in
    it.
    """

    LittleEndian = Kee[int](0)
    BigEndian = Kee[int](1)
    CurrentSystemEndian = Kee[int](2)

  class ColorModel(CuteNum):
    """
    The enum 'QPixelFormat::ColorModel' of Qt, with the 9 names Qt gives in
    it.
    """

    RGB = Kee[int](0)
    BGR = Kee[int](1)
    Indexed = Kee[int](2)
    Grayscale = Kee[int](3)
    CMYK = Kee[int](4)
    HSL = Kee[int](5)
    HSV = Kee[int](6)
    YUV = Kee[int](7)
    Alpha = Kee[int](8)

  class TypeInterpretation(CuteNum):
    """
    The enum 'QPixelFormat::TypeInterpretation' of Qt, with the 4 names Qt
    gives in it.
    """

    UnsignedInteger = Kee[int](0)
    UnsignedShort = Kee[int](1)
    UnsignedByte = Kee[int](2)
    FloatingPoint = Kee[int](3)

  class YUVLayout(CuteNum):
    """
    The enum 'QPixelFormat::YUVLayout' of Qt, with the 16 names Qt gives in
    it.
    """

    YUV444 = Kee[int](0)
    YUV422 = Kee[int](1)
    YUV411 = Kee[int](2)
    YUV420P = Kee[int](3)
    YUV420SP = Kee[int](4)
    YV12 = Kee[int](5)
    UYVY = Kee[int](6)
    YUYV = Kee[int](7)
    NV12 = Kee[int](8)
    NV21 = Kee[int](9)
    IMC1 = Kee[int](10)
    IMC2 = Kee[int](11)
    IMC3 = Kee[int](12)
    IMC4 = Kee[int](13)
    Y8 = Kee[int](14)
    Y16 = Kee[int](15)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(ByteOrder)
  def resolveByteOrder(bo: ByteOrder) -> ByteOrder:
    """
    Calls Qt's 'ByteOrder QPixelFormat::resolveByteOrder(ByteOrder bo)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#resolveByteOrder

    Parameters
    ----------

    bo : ByteOrder
      Passed on as its number.

    Returns
    -------

    ByteOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ByteOrder(number)' gives.
    """
    #  ByteOrder QPixelFormat::resolveByteOrder(ByteOrder bo)
    return QPixelFormat.ByteOrder(Rituals.call(
        'ritual_ZN12QPixelFormat16resolveByteOrderENS_9ByteOrderE', bo.value,
    ))

  @staticmethod
  @overload(ByteOrder, TypeInterpretation)
  def resolveByteOrder(bo: ByteOrder, ti: TypeInterpretation) -> ByteOrder:
    """
    Calls Qt's 'ByteOrder QPixelFormat::resolveByteOrder(ByteOrder bo,
    TypeInterpretation ti)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#resolveByteOrder

    Parameters
    ----------

    bo : ByteOrder
      Passed on as its number.

    ti : TypeInterpretation
      Passed on as its number.

    Returns
    -------

    ByteOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ByteOrder(number)' gives.
    """
    #  ByteOrder QPixelFormat::resolveByteOrder(ByteOrder bo,
    #      TypeInterpretation ti)
    return QPixelFormat.ByteOrder(Rituals.call(
        'ritual_ZN12QPixelFormat16resolveByteOrderENS_9ByteOrderENS_18TypeI'
        'nterpretationE',
        bo.value, ti.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixelFormat'

  #  Qt's '~QPixelFormat()'. Naming it makes this a value class: Python owns
  #  every C++ QPixelFormat behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QPixelFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def colorModel(self) -> ColorModel:
    """
    Calls Qt's 'ColorModel QPixelFormat::colorModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#colorModel

    Returns
    -------

    ColorModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorModel(number)'
      gives.
    """
    #  ColorModel QPixelFormat::colorModel() const
    return QPixelFormat.ColorModel(self.uglySide.call(
        'ritual_ZNK12QPixelFormat10colorModelEv',
    ))

  def channelCount(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::channelCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#channelCount
    """
    #  uchar QPixelFormat::channelCount() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat12channelCountEv')

  def redSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::redSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#redSize
    """
    #  uchar QPixelFormat::redSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat7redSizeEv')

  def greenSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::greenSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#greenSize
    """
    #  uchar QPixelFormat::greenSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat9greenSizeEv')

  def blueSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::blueSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#blueSize
    """
    #  uchar QPixelFormat::blueSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat8blueSizeEv')

  def cyanSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::cyanSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#cyanSize
    """
    #  uchar QPixelFormat::cyanSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat8cyanSizeEv')

  def magentaSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::magentaSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#magentaSize
    """
    #  uchar QPixelFormat::magentaSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat11magentaSizeEv')

  def yellowSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::yellowSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#yellowSize
    """
    #  uchar QPixelFormat::yellowSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat10yellowSizeEv')

  def blackSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::blackSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#blackSize
    """
    #  uchar QPixelFormat::blackSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat9blackSizeEv')

  def hueSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::hueSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#hueSize
    """
    #  uchar QPixelFormat::hueSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat7hueSizeEv')

  def saturationSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::saturationSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#saturationSize
    """
    #  uchar QPixelFormat::saturationSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat14saturationSizeEv')

  def lightnessSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::lightnessSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#lightnessSize
    """
    #  uchar QPixelFormat::lightnessSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat13lightnessSizeEv')

  def brightnessSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::brightnessSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#brightnessSize
    """
    #  uchar QPixelFormat::brightnessSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat14brightnessSizeEv')

  def alphaSize(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::alphaSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#alphaSize
    """
    #  uchar QPixelFormat::alphaSize() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat9alphaSizeEv')

  def bitsPerPixel(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::bitsPerPixel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#bitsPerPixel
    """
    #  uchar QPixelFormat::bitsPerPixel() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat12bitsPerPixelEv')

  def alphaUsage(self) -> AlphaUsage:
    """
    Calls Qt's 'AlphaUsage QPixelFormat::alphaUsage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#alphaUsage

    Returns
    -------

    AlphaUsage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AlphaUsage(number)'
      gives.
    """
    #  AlphaUsage QPixelFormat::alphaUsage() const
    return QPixelFormat.AlphaUsage(self.uglySide.call(
        'ritual_ZNK12QPixelFormat10alphaUsageEv',
    ))

  def alphaPosition(self) -> AlphaPosition:
    """
    Calls Qt's 'AlphaPosition QPixelFormat::alphaPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#alphaPosition

    Returns
    -------

    AlphaPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AlphaPosition(number)'
      gives.
    """
    #  AlphaPosition QPixelFormat::alphaPosition() const
    return QPixelFormat.AlphaPosition(self.uglySide.call(
        'ritual_ZNK12QPixelFormat13alphaPositionEv',
    ))

  def premultiplied(self) -> AlphaPremultiplied:
    """
    Calls Qt's 'AlphaPremultiplied QPixelFormat::premultiplied() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#premultiplied

    Returns
    -------

    AlphaPremultiplied
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AlphaPremultiplied(number)' gives.
    """
    #  AlphaPremultiplied QPixelFormat::premultiplied() const
    return QPixelFormat.AlphaPremultiplied(self.uglySide.call(
        'ritual_ZNK12QPixelFormat13premultipliedEv',
    ))

  def typeInterpretation(self) -> TypeInterpretation:
    """
    Calls Qt's 'TypeInterpretation QPixelFormat::typeInterpretation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixelformat.html#typeInterpretation

    Returns
    -------

    TypeInterpretation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TypeInterpretation(number)' gives.
    """
    #  TypeInterpretation QPixelFormat::typeInterpretation() const
    return QPixelFormat.TypeInterpretation(self.uglySide.call(
        'ritual_ZNK12QPixelFormat18typeInterpretationEv',
    ))

  def byteOrder(self) -> ByteOrder:
    """
    Calls Qt's 'ByteOrder QPixelFormat::byteOrder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#byteOrder

    Returns
    -------

    ByteOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ByteOrder(number)' gives.
    """
    #  ByteOrder QPixelFormat::byteOrder() const
    return QPixelFormat.ByteOrder(self.uglySide.call(
        'ritual_ZNK12QPixelFormat9byteOrderEv',
    ))

  def yuvLayout(self) -> YUVLayout:
    """
    Calls Qt's 'YUVLayout QPixelFormat::yuvLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#yuvLayout

    Returns
    -------

    YUVLayout
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'YUVLayout(number)' gives.
    """
    #  YUVLayout QPixelFormat::yuvLayout() const
    return QPixelFormat.YUVLayout(self.uglySide.call(
        'ritual_ZNK12QPixelFormat9yuvLayoutEv',
    ))

  def subEnum(self) -> int:
    """
    Calls Qt's 'uchar QPixelFormat::subEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#subEnum
    """
    #  uchar QPixelFormat::subEnum() const
    return self.uglySide.call('ritual_ZNK12QPixelFormat7subEnumEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, fmt2: QPixelFormat) -> bool:
    """
    Calls Qt's 'bool operator==(QPixelFormat fmt1, QPixelFormat fmt2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#operator==

    Parameters
    ----------

    fmt2 : QPixelFormat
      Passed on as a value: Qt reads the C++ QPixelFormat, which stays
      Python's own.
    """
    #  bool operator==(QPixelFormat fmt1, QPixelFormat fmt2)
    return Rituals.call(
        'ritual_Zeq12QPixelFormatS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(fmt2),
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
  def __ne__(self, fmt2: QPixelFormat) -> bool:
    """
    Calls Qt's 'bool operator!=(QPixelFormat fmt1, QPixelFormat fmt2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#operator!=

    Parameters
    ----------

    fmt2 : QPixelFormat
      Passed on as a value: Qt reads the C++ QPixelFormat, which stays
      Python's own.
    """
    #  bool operator!=(QPixelFormat fmt1, QPixelFormat fmt2)
    return Rituals.call(
        'ritual_Zne12QPixelFormatS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(fmt2),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QPixelFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QPixelFormat &format)
    address = Rituals.call(
        'ritual_Zls6QDebugRK12QPixelFormat',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QPixelFormat::QPixelFormat()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#QPixelFormat
    """
    #  QPixelFormat::QPixelFormat()
    self._noteCreation(QPixelFormat, lambda: Rituals.call(
        'ritual_ZN12QPixelFormatC1Ev',
    ))

  @overload(
      ColorModel, int, int, int, int, int, int, AlphaUsage, AlphaPosition,
      AlphaPremultiplied, TypeInterpretation,
  )
  @overload(
      ColorModel, int, int, int, int, int, int, AlphaUsage, AlphaPosition,
      AlphaPremultiplied, TypeInterpretation, ByteOrder,
  )
  @overload(
      ColorModel, int, int, int, int, int, int, AlphaUsage, AlphaPosition,
      AlphaPremultiplied, TypeInterpretation, ByteOrder, int,
  )
  def __init__(
      self,
      colorModel: ColorModel,
      firstSize: int,
      secondSize: int,
      thirdSize: int,
      fourthSize: int,
      fifthSize: int,
      alphaSize: int,
      alphaUsage: AlphaUsage,
      alphaPosition: AlphaPosition,
      premultiplied: AlphaPremultiplied,
      typeInterpretation: TypeInterpretation,
      byteOrder: ByteOrder = ByteOrder.CurrentSystemEndian,
      subEnum: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPixelFormat::QPixelFormat(ColorModel
    colorModel, uchar firstSize, uchar secondSize, uchar thirdSize, uchar
    fourthSize, uchar fifthSize, uchar alphaSize, AlphaUsage alphaUsage,
    AlphaPosition alphaPosition, AlphaPremultiplied premultiplied,
    TypeInterpretation typeInterpretation, ByteOrder byteOrder, uchar
    subEnum)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixelformat.html#QPixelFormat

    Parameters
    ----------

    colorModel : ColorModel
      Passed on as its number.

    firstSize : int
      Passed on as it is.

    secondSize : int
      Passed on as it is.

    thirdSize : int
      Passed on as it is.

    fourthSize : int
      Passed on as it is.

    fifthSize : int
      Passed on as it is.

    alphaSize : int
      Passed on as it is.

    alphaUsage : AlphaUsage
      Passed on as its number.

    alphaPosition : AlphaPosition
      Passed on as its number.

    premultiplied : AlphaPremultiplied
      Passed on as its number.

    typeInterpretation : TypeInterpretation
      Passed on as its number.

    byteOrder : ByteOrder
      Passed on as its number. May be left out, as in Qt: it is then
      ByteOrder.CurrentSystemEndian.

    subEnum : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QPixelFormat::QPixelFormat(ColorModel colorModel, uchar firstSize,
    #      uchar secondSize, uchar thirdSize, uchar fourthSize, uchar
    #      fifthSize, uchar alphaSize, AlphaUsage alphaUsage, AlphaPosition
    #      alphaPosition, AlphaPremultiplied premultiplied,
    #      TypeInterpretation typeInterpretation, ByteOrder byteOrder, uchar
    #      subEnum)
    self._noteCreation(QPixelFormat, lambda: Rituals.call(
        'ritual_ZN12QPixelFormatC1ENS_10ColorModelEhhhhhhNS_10AlphaUsageENS'
        '_13AlphaPositionENS_18AlphaPremultipliedENS_18TypeInterpretationEN'
        'S_9ByteOrderEh',
        colorModel.value, firstSize, secondSize, thirdSize, fourthSize,
        fifthSize, alphaSize, alphaUsage.value, alphaPosition.value,
        premultiplied.value, typeInterpretation.value, byteOrder.value,
        subEnum,
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

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'uchar QPixelFormat::get(Field offset, FieldWidth width) const':
    names the enum 'QPixelFormat::Field', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QPixelFormat.get' has no cute function yet. Qt's 'uchar "
        "QPixelFormat::get(Field offset, FieldWidth width) const': names "
        "the enum 'QPixelFormat::Field', whose class cannot be named here.")

  @staticmethod
  def set(*__, **_) -> Never:
    """
    Qt's 'quint64 QPixelFormat::set(Field offset, FieldWidth width, uchar
    value)': names the enum 'QPixelFormat::Field', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QPixelFormat.set' has no cute function yet. Qt's 'quint64 "
        "QPixelFormat::set(Field offset, FieldWidth width, uchar value)': "
        "names the enum 'QPixelFormat::Field', whose class cannot be named "
        "here.")
