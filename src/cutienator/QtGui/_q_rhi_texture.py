"""
QRhiTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiTexture(QRhiResource):
  """
  The cute side of Qt's QRhiTexture: a plain Python object standing in front
  of one C++ QRhiTexture.

  It is built on the cute 'QRhiResource', as Qt's QRhiTexture is built on
  Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiTexture that has a ritual and that Python can
  call so far, 24 names in all: 'resourceType', 'format', 'setFormat',
  'pixelSize', 'setPixelSize', 'depth', 'setDepth', 'arraySize',
  'setArraySize', 'arrayRangeStart', 'arrayRangeLength', 'setArrayRange',
  'flags', 'setFlags', 'sampleCount', 'setSampleCount', 'readViewFormat',
  'setReadViewFormat', 'writeViewFormat', 'setWriteViewFormat', 'create',
  'nativeTexture', 'createFrom', 'setNativeLayout'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiTexture is created at the first use, not by
    'QRhiTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiTexture.
  """

  #  The enums Qt writes inside QRhiTexture, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QRhiTexture::Flag' of Qt, with the 14 names Qt gives in
    it. Qt names the type of its combinations 'QRhiTexture::Flags'.
    """

    RenderTarget = 0x1
    CubeMap = 0x4
    MipMapped = 0x8
    sRGB = 0x10
    UsedAsTransferSource = 0x20
    UsedWithGenerateMips = 0x40
    UsedWithLoadStore = 0x80
    UsedAsCompressedAtlas = 0x100
    ExternalOES = 0x200
    ThreeDimensional = 0x400
    TextureRectangleGL = 0x800
    TextureArray = 0x1000
    OneDimensional = 0x2000
    UsedAsShadingRateMap = 0x4000

  Flags = Flag

  class Format(CuteNum):
    """
    The enum 'QRhiTexture::Format' of Qt, with the 50 names Qt gives in it.
    """

    UnknownFormat = Kee[int](0)
    RGBA8 = Kee[int](1)
    BGRA8 = Kee[int](2)
    R8 = Kee[int](3)
    RG8 = Kee[int](4)
    R16 = Kee[int](5)
    RG16 = Kee[int](6)
    RED_OR_ALPHA8 = Kee[int](7)
    RGBA16F = Kee[int](8)
    RGBA32F = Kee[int](9)
    R16F = Kee[int](10)
    R32F = Kee[int](11)
    RGB10A2 = Kee[int](12)
    R8SI = Kee[int](13)
    R32SI = Kee[int](14)
    RG32SI = Kee[int](15)
    RGBA32SI = Kee[int](16)
    R8UI = Kee[int](17)
    R32UI = Kee[int](18)
    RG32UI = Kee[int](19)
    RGBA32UI = Kee[int](20)
    D16 = Kee[int](21)
    D24 = Kee[int](22)
    D24S8 = Kee[int](23)
    D32F = Kee[int](24)
    D32FS8 = Kee[int](25)
    BC1 = Kee[int](26)
    BC2 = Kee[int](27)
    BC3 = Kee[int](28)
    BC4 = Kee[int](29)
    BC5 = Kee[int](30)
    BC6H = Kee[int](31)
    BC7 = Kee[int](32)
    ETC2_RGB8 = Kee[int](33)
    ETC2_RGB8A1 = Kee[int](34)
    ETC2_RGBA8 = Kee[int](35)
    ASTC_4x4 = Kee[int](36)
    ASTC_5x4 = Kee[int](37)
    ASTC_5x5 = Kee[int](38)
    ASTC_6x5 = Kee[int](39)
    ASTC_6x6 = Kee[int](40)
    ASTC_8x5 = Kee[int](41)
    ASTC_8x6 = Kee[int](42)
    ASTC_8x8 = Kee[int](43)
    ASTC_10x5 = Kee[int](44)
    ASTC_10x6 = Kee[int](45)
    ASTC_10x8 = Kee[int](46)
    ASTC_10x10 = Kee[int](47)
    ASTC_12x10 = Kee[int](48)
    ASTC_12x12 = Kee[int](49)

  #  The classes Qt writes inside QRhiTexture, each a class in here as in
  #  C++.

  class NativeTexture(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiTexture::NativeTexture: a plain Python object
    standing in front of one C++ QRhiTexture::NativeTexture.

    C++ hands a QRhiTexture::NativeTexture around as a copy, so every C++
    QRhiTexture::NativeTexture behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiTexture::NativeTexture yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiTexture::NativeTexture::~NativeTexture()': the destructor:
      Python removes its C++ QRhiTexture::NativeTexture by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QRhiTexture::NativeTexture is created at the first use, not by
      'QRhiTexture::NativeTexture(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiTexture::NativeTexture back gives a copy the
      ritual made for Python, in a new cute QRhiTexture::NativeTexture.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiTexture::NativeTexture'

    #  Qt's '~QRhiTexture::NativeTexture()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiTexture::NativeTexture behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QRhiTexture13NativeTextureD1Ev'

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

  class ViewFormat(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiTexture::ViewFormat: a plain Python object
    standing in front of one C++ QRhiTexture::ViewFormat.

    C++ hands a QRhiTexture::ViewFormat around as a copy, so every C++
    QRhiTexture::ViewFormat behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiTexture::ViewFormat yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiTexture::ViewFormat::~ViewFormat()': the destructor: Python
      removes its C++ QRhiTexture::ViewFormat by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QRhiTexture::ViewFormat is created at the first use, not by
      'QRhiTexture::ViewFormat(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiTexture::ViewFormat back gives a copy the
      ritual made for Python, in a new cute QRhiTexture::ViewFormat.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiTexture::ViewFormat'

    #  Qt's '~QRhiTexture::ViewFormat()'. Naming it makes this a value class:
    #  Python owns every C++ QRhiTexture::ViewFormat behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QRhiTexture10ViewFormatD1Ev'

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
  __qt_class__ = 'QRhiTexture'

  #  A C++ QRhiTexture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiTexture'

  #  The functions Qt calls itself that QRhiTexture is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN11QRhiTexture6createEv',
           ('bool', 'number', ''),
           ()),
      ),
      'nativeTexture': (
          ('_ZN11QRhiTexture13nativeTextureEv',
           ('address', 'value', 'QtGui:QRhiTexture.NativeTexture'),
           ()),
      ),
      'createFrom': (
          ('_ZN11QRhiTexture10createFromENS_13NativeTextureE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QRhiTexture.NativeTexture'),
           )),
      ),
      'setNativeLayout': (
          ('_ZN11QRhiTexture15setNativeLayoutEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiTexture::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiTexture::resourceType() const
    ritual = 'ritual_ZNK11QRhiTexture12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QRhiTexture12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def format(self) -> Format:
    """
    Calls Qt's 'Format QRhiTexture::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QRhiTexture::format() const
    return QRhiTexture.Format(self.uglySide.call(
        'ritual_ZNK11QRhiTexture6formatEv',
    ))

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiTexture::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiTexture::pixelSize() const
    address = self.uglySide.call('ritual_ZNK11QRhiTexture9pixelSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QRhiTexture::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#depth
    """
    #  int QRhiTexture::depth() const
    return self.uglySide.call('ritual_ZNK11QRhiTexture5depthEv')

  def arraySize(self) -> int:
    """
    Calls Qt's 'int QRhiTexture::arraySize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#arraySize
    """
    #  int QRhiTexture::arraySize() const
    return self.uglySide.call('ritual_ZNK11QRhiTexture9arraySizeEv')

  def arrayRangeStart(self) -> int:
    """
    Calls Qt's 'int QRhiTexture::arrayRangeStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#arrayRangeStart
    """
    #  int QRhiTexture::arrayRangeStart() const
    return self.uglySide.call('ritual_ZNK11QRhiTexture15arrayRangeStartEv')

  def arrayRangeLength(self) -> int:
    """
    Calls Qt's 'int QRhiTexture::arrayRangeLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#arrayRangeLength
    """
    #  int QRhiTexture::arrayRangeLength() const
    return self.uglySide.call('ritual_ZNK11QRhiTexture16arrayRangeLengthEv')

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QRhiTexture::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QRhiTexture::flags() const
    return QRhiTexture.Flags(self.uglySide.call(
        'ritual_ZNK11QRhiTexture5flagsEv',
    ))

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QRhiTexture::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#sampleCount
    """
    #  int QRhiTexture::sampleCount() const
    return self.uglySide.call('ritual_ZNK11QRhiTexture11sampleCountEv')

  def readViewFormat(self) -> ViewFormat:
    """
    Calls Qt's 'ViewFormat QRhiTexture::readViewFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#readViewFormat

    Returns
    -------

    ViewFormat
      A new cute QRhiTexture::ViewFormat around the copy Qt gave back. Python
      owns it.
    """
    #  ViewFormat QRhiTexture::readViewFormat() const
    address = self.uglySide.call('ritual_ZNK11QRhiTexture14readViewFormatEv')
    return QRhiTexture.ViewFormat._cuteOwning(address)

  def writeViewFormat(self) -> ViewFormat:
    """
    Calls Qt's 'ViewFormat QRhiTexture::writeViewFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#writeViewFormat

    Returns
    -------

    ViewFormat
      A new cute QRhiTexture::ViewFormat around the copy Qt gave back. Python
      owns it.
    """
    #  ViewFormat QRhiTexture::writeViewFormat() const
    address = self.uglySide.call(
        'ritual_ZNK11QRhiTexture15writeViewFormatEv',
    )
    return QRhiTexture.ViewFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Format)
  def setFormat(self, fmt: Format) -> None:
    """
    Calls Qt's 'void QRhiTexture::setFormat(Format fmt)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setFormat

    Parameters
    ----------

    fmt : Format
      Passed on as its number.
    """
    #  void QRhiTexture::setFormat(Format fmt)
    self.uglySide.call(
        'ritual_ZN11QRhiTexture9setFormatENS_6FormatE', fmt.value,
    )

  @overload(QSize)
  def setPixelSize(self, sz: QSize) -> None:
    """
    Calls Qt's 'void QRhiTexture::setPixelSize(const QSize &sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setPixelSize

    Parameters
    ----------

    sz : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiTexture::setPixelSize(const QSize &sz)
    self.uglySide.call(
        'ritual_ZN11QRhiTexture12setPixelSizeERK5QSize', self._valueOf(sz),
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QRhiTexture::setDepth(int depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QRhiTexture::setDepth(int depth)
    self.uglySide.call('ritual_ZN11QRhiTexture8setDepthEi', depth)

  @overload(int)
  def setArraySize(self, arraySize: int) -> None:
    """
    Calls Qt's 'void QRhiTexture::setArraySize(int arraySize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setArraySize

    Parameters
    ----------

    arraySize : int
      Passed on as it is.
    """
    #  void QRhiTexture::setArraySize(int arraySize)
    self.uglySide.call('ritual_ZN11QRhiTexture12setArraySizeEi', arraySize)

  @overload(int, int)
  def setArrayRange(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QRhiTexture::setArrayRange(int startIndex, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setArrayRange

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QRhiTexture::setArrayRange(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN11QRhiTexture13setArrayRangeEii', startIndex, count,
    )

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QRhiTexture::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QRhiTexture::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN11QRhiTexture8setFlagsE6QFlagsINS_4FlagEE', f.value,
    )

  @overload(int)
  def setSampleCount(self, s: int) -> None:
    """
    Calls Qt's 'void QRhiTexture::setSampleCount(int s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setSampleCount

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QRhiTexture::setSampleCount(int s)
    self.uglySide.call('ritual_ZN11QRhiTexture14setSampleCountEi', s)

  @overload(ViewFormat)
  def setReadViewFormat(self, fmt: ViewFormat) -> None:
    """
    Calls Qt's 'void QRhiTexture::setReadViewFormat(const ViewFormat &fmt)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setReadViewFormat

    Parameters
    ----------

    fmt : ViewFormat
      Passed on as a value: Qt reads the C++ QRhiTexture::ViewFormat, which
      stays Python's own.
    """
    #  void QRhiTexture::setReadViewFormat(const ViewFormat &fmt)
    self.uglySide.call(
        'ritual_ZN11QRhiTexture17setReadViewFormatERKNS_10ViewFormatE',
        self._valueOf(fmt),
    )

  @overload(ViewFormat)
  def setWriteViewFormat(self, fmt: ViewFormat) -> None:
    """
    Calls Qt's 'void QRhiTexture::setWriteViewFormat(const ViewFormat &fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexture.html#setWriteViewFormat

    Parameters
    ----------

    fmt : ViewFormat
      Passed on as a value: Qt reads the C++ QRhiTexture::ViewFormat, which
      stays Python's own.
    """
    #  void QRhiTexture::setWriteViewFormat(const ViewFormat &fmt)
    self.uglySide.call(
        'ritual_ZN11QRhiTexture18setWriteViewFormatERKNS_10ViewFormatE',
        self._valueOf(fmt),
    )

  @overload(int)
  def setNativeLayout(self, layout: int) -> None:
    """
    Calls Qt's 'void QRhiTexture::setNativeLayout(int layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#setNativeLayout

    Parameters
    ----------

    layout : int
      Passed on as it is.
    """
    #  void QRhiTexture::setNativeLayout(int layout)
    ritual = 'ritual_ZN11QRhiTexture15setNativeLayoutEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QRhiTexture15setNativeLayoutEi'
    self.uglySide.call(ritual, layout)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiImplementation, Format, QSize, int, int, int, Flags)
  @overload(NoneType, Format, QSize, int, int, int, Flags)
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      format_: Format,
      pixelSize_: QSize,
      depth_: int,
      arraySize_: int,
      sampleCount_: int,
      flags_: Flags,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTexture::QRhiTexture(QRhiImplementation *rhi, Format format_, const
    QSize &pixelSize_, int depth_, int arraySize_, int sampleCount_, Flags
    flags_)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#QRhiTexture

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format_ : Format
      Passed on as its number.

    pixelSize_ : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    depth_ : int
      Passed on as it is.

    arraySize_ : int
      Passed on as it is.

    sampleCount_ : int
      Passed on as it is.

    flags_ : Flags
      Passed on as its number.
    """
    #  QRhiTexture::QRhiTexture(QRhiImplementation *rhi, Format format_,
    #      const QSize &pixelSize_, int depth_, int arraySize_, int
    #      sampleCount_, Flags flags_)
    self._noteCreation(QRhiTexture, lambda: Rituals.call(
        'ritual_ZN11QRhiTextureC1EP18QRhiImplementationNS_6FormatERK5QSizei'
        'ii6QFlagsINS_4FlagEE',
        self._addressOf(rhi), format_.value, self._valueOf(pixelSize_),
        depth_, arraySize_, sampleCount_, flags_.value,
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QRhiTexture::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#create
    """
    #  bool QRhiTexture::create()
    return self.uglySide.call('ritual_ZN11QRhiTexture6createEv')

  def nativeTexture(self) -> NativeTexture:
    """
    Calls Qt's 'NativeTexture QRhiTexture::nativeTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#nativeTexture

    Returns
    -------

    NativeTexture
      A new cute QRhiTexture::NativeTexture around the copy Qt gave back.
      Python owns it.
    """
    #  NativeTexture QRhiTexture::nativeTexture()
    ritual = 'ritual_ZN11QRhiTexture13nativeTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QRhiTexture13nativeTextureEv'
    address = self.uglySide.call(ritual)
    return QRhiTexture.NativeTexture._cuteOwning(address)

  @overload(NativeTexture)
  def createFrom(self, src: NativeTexture) -> bool:
    """
    Calls Qt's 'bool QRhiTexture::createFrom(NativeTexture src)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhitexture.html#createFrom

    Parameters
    ----------

    src : NativeTexture
      Passed on as a value: Qt reads the C++ QRhiTexture::NativeTexture,
      which stays Python's own.
    """
    #  bool QRhiTexture::createFrom(NativeTexture src)
    ritual = 'ritual_ZN11QRhiTexture10createFromENS_13NativeTextureE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QRhiTexture10createFromENS_13NativeTextureE'
    return self.uglySide.call(ritual, self._valueOf(src))
