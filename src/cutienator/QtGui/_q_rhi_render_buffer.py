"""
QRhiRenderBuffer binding of the Qt C++
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
from . import QRhiResource, QRhiTexture

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


class QRhiRenderBuffer(QRhiResource):
  """
  The cute side of Qt's QRhiRenderBuffer: a plain Python object standing in
  front of one C++ QRhiRenderBuffer.

  It is built on the cute 'QRhiResource', as Qt's QRhiRenderBuffer is built
  on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiRenderBuffer that has a ritual and that Python
  can call so far, 12 names in all: 'resourceType', 'type', 'setType',
  'pixelSize', 'setPixelSize', 'sampleCount', 'setSampleCount', 'flags',
  'setFlags', 'create', 'createFrom', 'backingFormat'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiRenderBuffer is created at the first use, not by
    'QRhiRenderBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiRenderBuffer.
  """

  #  The enums Qt writes inside QRhiRenderBuffer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QRhiRenderBuffer::Flag' of Qt, with the 1 names Qt gives
    in it. Qt names the type of its combinations 'QRhiRenderBuffer::Flags'.
    """

    UsedWithSwapChainOnly = 0x1

  Flags = Flag

  class Type(CuteNum):
    """
    The enum 'QRhiRenderBuffer::Type' of Qt, with the 2 names Qt gives in it.
    """

    DepthStencil = Kee[int](0)
    Color = Kee[int](1)

  #  The classes Qt writes inside QRhiRenderBuffer, each a class in here as
  #  in C++.

  class NativeRenderBuffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiRenderBuffer::NativeRenderBuffer: a plain
    Python object standing in front of one C++
    QRhiRenderBuffer::NativeRenderBuffer.

    C++ hands a QRhiRenderBuffer::NativeRenderBuffer around as a copy, so
    every C++ QRhiRenderBuffer::NativeRenderBuffer behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiRenderBuffer::NativeRenderBuffer yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiRenderBuffer::NativeRenderBuffer::~NativeRenderBuffer()': the
      destructor: Python removes its C++ QRhiRenderBuffer::NativeRenderBuffer
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiRenderBuffer::NativeRenderBuffer is created at the first
      use, not by 'QRhiRenderBuffer::NativeRenderBuffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiRenderBuffer::NativeRenderBuffer back gives a
      copy the ritual made for Python, in a new cute
      QRhiRenderBuffer::NativeRenderBuffer.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiRenderBuffer::NativeRenderBuffer'

    #  Qt's '~QRhiRenderBuffer::NativeRenderBuffer()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QRhiRenderBuffer::NativeRenderBuffer behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN16QRhiRenderBuffer18NativeRenderBufferD1Ev'

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
  __qt_class__ = 'QRhiRenderBuffer'

  #  A C++ QRhiRenderBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiRenderBuffer'

  #  The functions Qt calls itself that QRhiRenderBuffer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN16QRhiRenderBuffer6createEv',
           ('bool', 'number', ''),
           ()),
      ),
      'createFrom': (
          ('_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE',
           ('bool', 'number', ''),
           (
               ('address', 'value',
                'QtGui:QRhiRenderBuffer.NativeRenderBuffer'),
           )),
      ),
      'backingFormat': (
          ('_ZNK16QRhiRenderBuffer13backingFormatEv',
           ('int', 'enum', 'QtGui:QRhiTexture.Format'),
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

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiRenderBuffer::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiRenderBuffer::resourceType() const
    ritual = 'ritual_ZNK16QRhiRenderBuffer12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QRhiRenderBuffer12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def type(self) -> Type:
    """
    Calls Qt's 'Type QRhiRenderBuffer::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QRhiRenderBuffer::type() const
    return QRhiRenderBuffer.Type(self.uglySide.call(
        'ritual_ZNK16QRhiRenderBuffer4typeEv',
    ))

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QRhiRenderBuffer::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QRhiRenderBuffer::pixelSize() const
    address = self.uglySide.call('ritual_ZNK16QRhiRenderBuffer9pixelSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QRhiRenderBuffer::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#sampleCount
    """
    #  int QRhiRenderBuffer::sampleCount() const
    return self.uglySide.call('ritual_ZNK16QRhiRenderBuffer11sampleCountEv')

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QRhiRenderBuffer::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QRhiRenderBuffer::flags() const
    return QRhiRenderBuffer.Flags(self.uglySide.call(
        'ritual_ZNK16QRhiRenderBuffer5flagsEv',
    ))

  def backingFormat(self) -> QRhiTexture.Format:
    """
    Calls Qt's 'QRhiTexture::Format QRhiRenderBuffer::backingFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderbuffer.html#backingFormat

    Returns
    -------

    QRhiTexture.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiTexture.Format(number)' gives.
    """
    #  QRhiTexture::Format QRhiRenderBuffer::backingFormat() const
    return QRhiTexture.Format(self.uglySide.call(
        'ritual_ZNK16QRhiRenderBuffer13backingFormatEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def setType(self, t: Type) -> None:
    """
    Calls Qt's 'void QRhiRenderBuffer::setType(Type t)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#setType

    Parameters
    ----------

    t : Type
      Passed on as its number.
    """
    #  void QRhiRenderBuffer::setType(Type t)
    self.uglySide.call(
        'ritual_ZN16QRhiRenderBuffer7setTypeENS_4TypeE', t.value,
    )

  @overload(QSize)
  def setPixelSize(self, sz: QSize) -> None:
    """
    Calls Qt's 'void QRhiRenderBuffer::setPixelSize(const QSize &sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#setPixelSize

    Parameters
    ----------

    sz : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QRhiRenderBuffer::setPixelSize(const QSize &sz)
    self.uglySide.call(
        'ritual_ZN16QRhiRenderBuffer12setPixelSizeERK5QSize',
        self._valueOf(sz),
    )

  @overload(int)
  def setSampleCount(self, s: int) -> None:
    """
    Calls Qt's 'void QRhiRenderBuffer::setSampleCount(int s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderbuffer.html#setSampleCount

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QRhiRenderBuffer::setSampleCount(int s)
    self.uglySide.call('ritual_ZN16QRhiRenderBuffer14setSampleCountEi', s)

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QRhiRenderBuffer::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QRhiRenderBuffer::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN16QRhiRenderBuffer8setFlagsE6QFlagsINS_4FlagEE', f.value,
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

  @overload(QRhiImplementation, Type, QSize, int, Flags, QRhiTexture.Format)
  @overload(NoneType, Type, QSize, int, Flags, QRhiTexture.Format)
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      type_: Type,
      pixelSize_: QSize,
      sampleCount_: int,
      flags_: Flags,
      backingFormatHint_: QRhiTexture.Format,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiRenderBuffer::QRhiRenderBuffer(QRhiImplementation *rhi, Type type_,
    const QSize &pixelSize_, int sampleCount_, Flags flags_,
    QRhiTexture::Format backingFormatHint_)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhirenderbuffer.html#QRhiRenderBuffer

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type_ : Type
      Passed on as its number.

    pixelSize_ : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount_ : int
      Passed on as it is.

    flags_ : Flags
      Passed on as its number.

    backingFormatHint_ : QRhiTexture.Format
      Passed on as its number.
    """
    #  QRhiRenderBuffer::QRhiRenderBuffer(QRhiImplementation *rhi, Type
    #      type_, const QSize &pixelSize_, int sampleCount_, Flags flags_,
    #      QRhiTexture::Format backingFormatHint_)
    self._noteCreation(QRhiRenderBuffer, lambda: Rituals.call(
        'ritual_ZN16QRhiRenderBufferC1EP18QRhiImplementationNS_4TypeERK5QSi'
        'zei6QFlagsINS_4FlagEEN11QRhiTexture6FormatE',
        self._addressOf(rhi), type_.value, self._valueOf(pixelSize_),
        sampleCount_, flags_.value, backingFormatHint_.value,
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
    Calls Qt's 'bool QRhiRenderBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#create
    """
    #  bool QRhiRenderBuffer::create()
    return self.uglySide.call('ritual_ZN16QRhiRenderBuffer6createEv')

  @overload(NativeRenderBuffer)
  def createFrom(self, src: NativeRenderBuffer) -> bool:
    """
    Calls Qt's 'bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhirenderbuffer.html#createFrom

    Parameters
    ----------

    src : NativeRenderBuffer
      Passed on as a value: Qt reads the C++
      QRhiRenderBuffer::NativeRenderBuffer, which stays Python's own.
    """
    #  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
    ritual = (
        'ritual_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBuf'
          'ferE')
    return self.uglySide.call(ritual, self._valueOf(src))
