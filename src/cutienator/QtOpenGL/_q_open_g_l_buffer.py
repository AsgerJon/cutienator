"""
QOpenGLBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglbuffer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpenGLBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLBuffer: a plain Python object standing in
  front of one C++ QOpenGLBuffer.

  C++ hands a QOpenGLBuffer around as a copy, so every C++ QOpenGLBuffer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLBuffer that has a ritual and that Python can
  call so far, 12 names in all: 'type', 'usagePattern', 'setUsagePattern',
  'create', 'isCreated', 'destroy', 'bind', 'release', 'bufferId', 'size',
  'allocate', 'unmap'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLBuffer::QOpenGLBuffer(QOpenGLBuffer &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QOpenGLBuffer::~QOpenGLBuffer()': the destructor: Python removes
    its C++ QOpenGLBuffer by it, and has no other use for it.
  - Qt's 'QOpenGLBuffer &QOpenGLBuffer::operator=(const QOpenGLBuffer
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpenGLBuffer &QOpenGLBuffer::operator=(QOpenGLBuffer &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QOpenGLBuffer::swap(QOpenGLBuffer &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QOpenGLBuffer::read(int offset, void *data, int count)': names
    'void', which has no cute class yet.
  - Qt's 'void QOpenGLBuffer::write(int offset, const void *data, int
    count)': names 'void', which has no cute class yet.
  - Qt's 'void QOpenGLBuffer::allocate(const void *data, int count)': names
    'void', which has no cute class yet.
  - Qt's 'void *QOpenGLBuffer::map(QOpenGLBuffer::Access access)': gives
    'void', which has no cute class yet.
  - Qt's 'void *QOpenGLBuffer::mapRange(int offset, int count,
    QOpenGLBuffer::RangeAccessFlags access)': gives 'void', which has no cute
    class yet.
  - Qt's 'QOpenGLBufferPrivate *QOpenGLBuffer::d_func()': gives
    'QOpenGLBufferPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLBufferPrivate *QOpenGLBuffer::d_func() const': gives
    'QOpenGLBufferPrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLBuffer is created at the first use, not by
    'QOpenGLBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLBuffer back gives a copy the ritual made for
    Python, in a new cute QOpenGLBuffer.
  - Each name of Qt's QOpenGLBuffer that has no cute function yet, 'd_func',
    'map', 'mapRange', 'read', 'swap', 'write', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpenGLBuffer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Access(CuteNum):
    """
    The enum 'QOpenGLBuffer::Access' of Qt, with the 3 names Qt gives in it.
    """

    ReadOnly = Kee[int](35000)
    WriteOnly = Kee[int](35001)
    ReadWrite = Kee[int](35002)

  class RangeAccessFlag(CuteFlags):
    """
    The flags enum 'QOpenGLBuffer::RangeAccessFlag' of Qt, with the 6 names
    Qt gives in it. Qt names the type of its combinations
    'QOpenGLBuffer::RangeAccessFlags'.
    """

    RangeRead = 0x1
    RangeWrite = 0x2
    RangeInvalidate = 0x4
    RangeInvalidateBuffer = 0x8
    RangeFlushExplicit = 0x10
    RangeUnsynchronized = 0x20

  RangeAccessFlags = RangeAccessFlag

  class Type(CuteNum):
    """
    The enum 'QOpenGLBuffer::Type' of Qt, with the 4 names Qt gives in it.
    """

    VertexBuffer = Kee[int](34962)
    IndexBuffer = Kee[int](34963)
    PixelPackBuffer = Kee[int](35051)
    PixelUnpackBuffer = Kee[int](35052)

  class UsagePattern(CuteNum):
    """
    The enum 'QOpenGLBuffer::UsagePattern' of Qt, with the 9 names Qt gives
    in it.
    """

    StreamDraw = Kee[int](35040)
    StreamRead = Kee[int](35041)
    StreamCopy = Kee[int](35042)
    StaticDraw = Kee[int](35044)
    StaticRead = Kee[int](35045)
    StaticCopy = Kee[int](35046)
    DynamicDraw = Kee[int](35048)
    DynamicRead = Kee[int](35049)
    DynamicCopy = Kee[int](35050)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLBuffer'

  #  Qt's '~QOpenGLBuffer()'. Naming it makes this a value class: Python owns
  #  every C++ QOpenGLBuffer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QOpenGLBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'QOpenGLBuffer::Type QOpenGLBuffer::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  QOpenGLBuffer::Type QOpenGLBuffer::type() const
    return QOpenGLBuffer.Type(self.uglySide.call(
        'ritual_ZNK13QOpenGLBuffer4typeEv',
    ))

  def usagePattern(self) -> UsagePattern:
    """
    Calls Qt's 'QOpenGLBuffer::UsagePattern QOpenGLBuffer::usagePattern()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#usagePattern

    Returns
    -------

    UsagePattern
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UsagePattern(number)'
      gives.
    """
    #  QOpenGLBuffer::UsagePattern QOpenGLBuffer::usagePattern() const
    return QOpenGLBuffer.UsagePattern(self.uglySide.call(
        'ritual_ZNK13QOpenGLBuffer12usagePatternEv',
    ))

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLBuffer::isCreated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#isCreated
    """
    #  bool QOpenGLBuffer::isCreated() const
    return self.uglySide.call('ritual_ZNK13QOpenGLBuffer9isCreatedEv')

  def bufferId(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLBuffer::bufferId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#bufferId
    """
    #  GLuint QOpenGLBuffer::bufferId() const
    return self.uglySide.call('ritual_ZNK13QOpenGLBuffer8bufferIdEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QOpenGLBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#size
    """
    #  int QOpenGLBuffer::size() const
    return self.uglySide.call('ritual_ZNK13QOpenGLBuffer4sizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(UsagePattern)
  def setUsagePattern(self, value: UsagePattern) -> None:
    """
    Calls Qt's 'void
    QOpenGLBuffer::setUsagePattern(QOpenGLBuffer::UsagePattern value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#setUsagePattern

    Parameters
    ----------

    value : UsagePattern
      Passed on as its number.
    """
    #  void QOpenGLBuffer::setUsagePattern(QOpenGLBuffer::UsagePattern value)
    self.uglySide.call(
        'ritual_ZN13QOpenGLBuffer15setUsagePatternENS_12UsagePatternE',
        value.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLBuffer::QOpenGLBuffer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#QOpenGLBuffer
    """
    #  QOpenGLBuffer::QOpenGLBuffer()
    self._noteCreation(QOpenGLBuffer, lambda: Rituals.call(
        'ritual_ZN13QOpenGLBufferC1Ev',
    ))

  @overload(Type)
  def __init__(self, type: Type) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLBuffer::QOpenGLBuffer(QOpenGLBuffer::Type type)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#QOpenGLBuffer

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  QOpenGLBuffer::QOpenGLBuffer(QOpenGLBuffer::Type type)
    self._noteCreation(QOpenGLBuffer, lambda: Rituals.call(
        'ritual_ZN13QOpenGLBufferC1ENS_4TypeE', type.value,
    ))

  @overload(THIS)
  def __init__(self, other: QOpenGLBuffer) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLBuffer::QOpenGLBuffer(const
    QOpenGLBuffer &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#QOpenGLBuffer

    Parameters
    ----------

    other : QOpenGLBuffer
      Passed on as a value: Qt reads the C++ QOpenGLBuffer, which stays
      Python's own.
    """
    #  QOpenGLBuffer::QOpenGLBuffer(const QOpenGLBuffer &other)
    self._noteCreation(QOpenGLBuffer, lambda: Rituals.call(
        'ritual_ZN13QOpenGLBufferC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'bool QOpenGLBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#create
    """
    #  bool QOpenGLBuffer::create()
    return self.uglySide.call('ritual_ZN13QOpenGLBuffer6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#destroy
    """
    #  void QOpenGLBuffer::destroy()
    self.uglySide.call('ritual_ZN13QOpenGLBuffer7destroyEv')

  def bind(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLBuffer::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#bind
    """
    #  bool QOpenGLBuffer::bind()
    return self.uglySide.call('ritual_ZN13QOpenGLBuffer4bindEv')

  @overload()
  def release(self) -> None:
    """
    Calls Qt's 'void QOpenGLBuffer::release()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#release
    """
    #  void QOpenGLBuffer::release()
    self.uglySide.call('ritual_ZN13QOpenGLBuffer7releaseEv')

  @staticmethod
  @overload(Type)
  def release(type: Type) -> None:
    """
    Calls Qt's 'void QOpenGLBuffer::release(QOpenGLBuffer::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#release

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void QOpenGLBuffer::release(QOpenGLBuffer::Type type)
    Rituals.call('ritual_ZN13QOpenGLBuffer7releaseENS_4TypeE', type.value)

  @overload(int)
  def allocate(self, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLBuffer::allocate(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#allocate

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QOpenGLBuffer::allocate(int count)
    self.uglySide.call('ritual_ZN13QOpenGLBuffer8allocateEi', count)

  def unmap(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLBuffer::unmap()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglbuffer.html#unmap
    """
    #  bool QOpenGLBuffer::unmap()
    return self.uglySide.call('ritual_ZN13QOpenGLBuffer5unmapEv')

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QOpenGLBufferPrivate *QOpenGLBuffer::d_func()': gives
      'QOpenGLBufferPrivate', which has no cute class yet.
    - Qt's 'const QOpenGLBufferPrivate *QOpenGLBuffer::d_func() const': gives
      'QOpenGLBufferPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLBuffer.d_func' has no cute function yet. Qt's "
        "'QOpenGLBufferPrivate *QOpenGLBuffer::d_func()': gives "
        "'QOpenGLBufferPrivate', which has no cute class yet. Qt's 'const "
        "QOpenGLBufferPrivate *QOpenGLBuffer::d_func() const': gives "
        "'QOpenGLBufferPrivate', which has no cute class yet.")

  @staticmethod
  def map(*__, **_) -> Never:
    """
    Qt's 'void *QOpenGLBuffer::map(QOpenGLBuffer::Access access)': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLBuffer.map' has no cute function yet. Qt's 'void "
        "*QOpenGLBuffer::map(QOpenGLBuffer::Access access)': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def mapRange(*__, **_) -> Never:
    """
    Qt's 'void *QOpenGLBuffer::mapRange(int offset, int count,
    QOpenGLBuffer::RangeAccessFlags access)': gives 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QOpenGLBuffer.mapRange' has no cute function yet. Qt's 'void "
        "*QOpenGLBuffer::mapRange(int offset, int count, "
        "QOpenGLBuffer::RangeAccessFlags access)': gives 'void', which has "
        "no cute class yet.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'bool QOpenGLBuffer::read(int offset, void *data, int count)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLBuffer.read' has no cute function yet. Qt's 'bool "
        "QOpenGLBuffer::read(int offset, void *data, int count)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLBuffer::swap(QOpenGLBuffer &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLBuffer.swap' has no cute function yet. Qt's 'void "
        "QOpenGLBuffer::swap(QOpenGLBuffer &other)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLBuffer::write(int offset, const void *data, int
    count)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLBuffer.write' has no cute function yet. Qt's 'void "
        "QOpenGLBuffer::write(int offset, const void *data, int count)': "
        "names 'void', which has no cute class yet.")
