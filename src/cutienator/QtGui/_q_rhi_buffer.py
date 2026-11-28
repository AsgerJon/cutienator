"""
QRhiBuffer binding of the Qt C++
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
  from typing import Never, Optional

  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiBuffer(QRhiResource):
  """
  The cute side of Qt's QRhiBuffer: a plain Python object standing in front
  of one C++ QRhiBuffer.

  It is built on the cute 'QRhiResource', as Qt's QRhiBuffer is built on Qt's
  QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiBuffer that has a ritual and that Python can
  call so far, 10 names in all: 'resourceType', 'type', 'setType', 'usage',
  'setUsage', 'size', 'setSize', 'create', 'nativeBuffer',
  'endFullDynamicBufferUpdateForCurrentFrame'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char *QRhiBuffer::beginFullDynamicBufferUpdateForCurrentFrame()':
    gives 'char', which has no cute class yet.
  - Qt's 'void QRhiBuffer::fullDynamicBufferUpdateForCurrentFrame(const void
    *data, quint32 size)': names 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QRhiBuffer is created at the first use, not by 'QRhiBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiBuffer.
  - Each name of Qt's QRhiBuffer that has no cute function yet,
    'beginFullDynamicBufferUpdateForCurrentFrame',
    'fullDynamicBufferUpdateForCurrentFrame', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiBuffer, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """The enum 'QRhiBuffer::Type' of Qt, with the 3 names Qt gives in it."""

    Immutable = Kee[int](0)
    Static = Kee[int](1)
    Dynamic = Kee[int](2)

  class UsageFlag(CuteFlags):
    """
    The flags enum 'QRhiBuffer::UsageFlag' of Qt, with the 5 names Qt gives
    in it. Qt names the type of its combinations 'QRhiBuffer::UsageFlags'.
    """

    VertexBuffer = 0x1
    IndexBuffer = 0x2
    UniformBuffer = 0x4
    StorageBuffer = 0x8
    IndirectBuffer = 0x10

  UsageFlags = UsageFlag

  #  The classes Qt writes inside QRhiBuffer, each a class in here as in C++.

  class NativeBuffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiBuffer::NativeBuffer: a plain Python object
    standing in front of one C++ QRhiBuffer::NativeBuffer.

    C++ hands a QRhiBuffer::NativeBuffer around as a copy, so every C++
    QRhiBuffer::NativeBuffer behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QRhiBuffer::NativeBuffer yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiBuffer::NativeBuffer::~NativeBuffer()': the destructor:
      Python removes its C++ QRhiBuffer::NativeBuffer by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QRhiBuffer::NativeBuffer is created at the first use, not by
      'QRhiBuffer::NativeBuffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiBuffer::NativeBuffer back gives a copy the
      ritual made for Python, in a new cute QRhiBuffer::NativeBuffer.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiBuffer::NativeBuffer'

    #  Qt's '~QRhiBuffer::NativeBuffer()'. Naming it makes this a value
    #  class: Python owns every C++ QRhiBuffer::NativeBuffer behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QRhiBuffer12NativeBufferD1Ev'

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
  __qt_class__ = 'QRhiBuffer'

  #  A C++ QRhiBuffer Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiBuffer'

  #  The functions Qt calls itself that QRhiBuffer is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'beginFullDynamicBufferUpdateForCurrentFrame': (
          'char *QRhiBuffer::beginFullDynamicBufferUpdateForCurrentFrame()',
      ),
      'fullDynamicBufferUpdateForCurrentFrame': (
          'void QRhiBuffer::fullDynamicBufferUpdateForCurrentFrame(const '
          'void *, quint32)',
      ),
  }

  #  The functions Qt calls itself that QRhiBuffer is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN10QRhiBuffer6createEv',
           ('bool', 'number', ''),
           ()),
      ),
      'nativeBuffer': (
          ('_ZN10QRhiBuffer12nativeBufferEv',
           ('address', 'value', 'QtGui:QRhiBuffer.NativeBuffer'),
           ()),
      ),
      'endFullDynamicBufferUpdateForCurrentFrame': (
          ('_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv',
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

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiBuffer::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiBuffer::resourceType() const
    ritual = 'ritual_ZNK10QRhiBuffer12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QRhiBuffer12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def type(self) -> Type:
    """
    Calls Qt's 'Type QRhiBuffer::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QRhiBuffer::type() const
    return QRhiBuffer.Type(self.uglySide.call(
        'ritual_ZNK10QRhiBuffer4typeEv',
    ))

  def usage(self) -> UsageFlags:
    """
    Calls Qt's 'UsageFlags QRhiBuffer::usage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#usage

    Returns
    -------

    UsageFlags
      The value standing for the combination Qt gave back.
    """
    #  UsageFlags QRhiBuffer::usage() const
    return QRhiBuffer.UsageFlags(self.uglySide.call(
        'ritual_ZNK10QRhiBuffer5usageEv',
    ))

  def size(self) -> int:
    """
    Calls Qt's 'quint32 QRhiBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#size
    """
    #  quint32 QRhiBuffer::size() const
    return self.uglySide.call('ritual_ZNK10QRhiBuffer4sizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def setType(self, t: Type) -> None:
    """
    Calls Qt's 'void QRhiBuffer::setType(Type t)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#setType

    Parameters
    ----------

    t : Type
      Passed on as its number.
    """
    #  void QRhiBuffer::setType(Type t)
    self.uglySide.call('ritual_ZN10QRhiBuffer7setTypeENS_4TypeE', t.value)

  @overload(UsageFlags)
  def setUsage(self, u: UsageFlags) -> None:
    """
    Calls Qt's 'void QRhiBuffer::setUsage(UsageFlags u)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#setUsage

    Parameters
    ----------

    u : UsageFlags
      Passed on as its number.
    """
    #  void QRhiBuffer::setUsage(UsageFlags u)
    self.uglySide.call(
        'ritual_ZN10QRhiBuffer8setUsageE6QFlagsINS_9UsageFlagEE', u.value,
    )

  @overload(int)
  def setSize(self, sz: int) -> None:
    """
    Calls Qt's 'void QRhiBuffer::setSize(quint32 sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#setSize

    Parameters
    ----------

    sz : int
      Passed on as it is.
    """
    #  void QRhiBuffer::setSize(quint32 sz)
    self.uglySide.call('ritual_ZN10QRhiBuffer7setSizeEj', sz)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiImplementation, Type, UsageFlags, int)
  @overload(NoneType, Type, UsageFlags, int)
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      type_: Type,
      usage_: UsageFlags,
      size_: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRhiBuffer::QRhiBuffer(QRhiImplementation
    *rhi, Type type_, UsageFlags usage_, quint32 size_)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#QRhiBuffer

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type_ : Type
      Passed on as its number.

    usage_ : UsageFlags
      Passed on as its number.

    size_ : int
      Passed on as it is.
    """
    #  QRhiBuffer::QRhiBuffer(QRhiImplementation *rhi, Type type_, UsageFlags
    #      usage_, quint32 size_)
    self._noteCreation(QRhiBuffer, lambda: Rituals.call(
        'ritual_ZN10QRhiBufferC1EP18QRhiImplementationNS_4TypeE6QFlagsINS_9'
        'UsageFlagEEj',
        self._addressOf(rhi), type_.value, usage_.value, size_,
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
    Calls Qt's 'bool QRhiBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#create
    """
    #  bool QRhiBuffer::create()
    return self.uglySide.call('ritual_ZN10QRhiBuffer6createEv')

  def nativeBuffer(self) -> NativeBuffer:
    """
    Calls Qt's 'NativeBuffer QRhiBuffer::nativeBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibuffer.html#nativeBuffer

    Returns
    -------

    NativeBuffer
      A new cute QRhiBuffer::NativeBuffer around the copy Qt gave back.
      Python owns it.
    """
    #  NativeBuffer QRhiBuffer::nativeBuffer()
    ritual = 'ritual_ZN10QRhiBuffer12nativeBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QRhiBuffer12nativeBufferEv'
    address = self.uglySide.call(ritual)
    return QRhiBuffer.NativeBuffer._cuteOwning(address)

  def endFullDynamicBufferUpdateForCurrentFrame(self) -> None:
    """
    Calls Qt's 'void
    QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhibuffer.html
    """
    #  void QRhiBuffer::endFullDynamicBufferUpdateForCurrentFrame()
    ritual = (
        'ritual_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentF'
          'rameEv')
    self.uglySide.call(ritual)

  @staticmethod
  def beginFullDynamicBufferUpdateForCurrentFrame(*__, **_) -> Never:
    """
    Qt's 'char *QRhiBuffer::beginFullDynamicBufferUpdateForCurrentFrame()':
    gives 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiBuffer.beginFullDynamicBufferUpdateForCurrentFrame' has no "
        "cute function yet. Qt's 'char "
        "*QRhiBuffer::beginFullDynamicBufferUpdateForCurrentFrame()': gives "
        "'char', which has no cute class yet.")

  @staticmethod
  def fullDynamicBufferUpdateForCurrentFrame(*__, **_) -> Never:
    """
    Qt's 'void QRhiBuffer::fullDynamicBufferUpdateForCurrentFrame(const void
    *data, quint32 size)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRhiBuffer.fullDynamicBufferUpdateForCurrentFrame' has no cute "
        "function yet. Qt's 'void "
        "QRhiBuffer::fullDynamicBufferUpdateForCurrentFrame(const void "
        "*data, quint32 size)': names 'void', which has no cute class yet.")
