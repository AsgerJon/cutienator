"""
QWaylandBufferRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandbufferref.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QWaylandSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QImage
  from ..QtOpenGL import QOpenGLTexture


class QWaylandBufferRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandBufferRef: a plain Python object standing in
  front of one C++ QWaylandBufferRef.

  C++ hands a QWaylandBufferRef around as a copy, so every C++
  QWaylandBufferRef behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWaylandBufferRef that has a ritual and that Python
  can call so far, 16 names in all: 'isNull', 'hasBuffer', 'hasContent',
  'hasProtectedContent', 'isDestroyed', 'size', 'origin', 'bufferType',
  'bufferFormatEgl', 'isSharedMemory', 'image', 'toOpenGLTexture',
  'lockNativeBuffer', 'unlockNativeBuffer', '__eq__', '__ne__'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWaylandBufferRef::~QWaylandBufferRef()': the destructor: Python
    removes its C++ QWaylandBufferRef by it, and has no other use for it.
  - Qt's 'QWaylandBufferRef &QWaylandBufferRef::operator=(const
    QWaylandBufferRef &ref)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'struct wl_resource *QWaylandBufferRef::wl_buffer() const': gives
    'struct wl_resource', which has no cute class yet.
  - Qt's 'QWaylandBufferRef::QWaylandBufferRef(QtWayland::ClientBuffer
    *buffer)': names 'QtWayland::ClientBuffer', which has no cute class yet.
  - Qt's 'QtWayland::ClientBuffer *QWaylandBufferRef::buffer() const': gives
    'QtWayland::ClientBuffer', which has no cute class yet.

  What to expect
  --------------

  - The C++ QWaylandBufferRef is created at the first use, not by
    'QWaylandBufferRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWaylandBufferRef back gives a copy the ritual made
    for Python, in a new cute QWaylandBufferRef.
  - Each name of Qt's QWaylandBufferRef that has no cute function yet,
    'buffer', 'wl_buffer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandBufferRef, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BufferFormatEgl(CuteNum):
    """
    The enum 'QWaylandBufferRef::BufferFormatEgl' of Qt, with the 7 names Qt
    gives in it.
    """

    BufferFormatEgl_Null = Kee[int](0)
    BufferFormatEgl_RGB = Kee[int](1)
    BufferFormatEgl_RGBA = Kee[int](2)
    BufferFormatEgl_EXTERNAL_OES = Kee[int](3)
    BufferFormatEgl_Y_U_V = Kee[int](4)
    BufferFormatEgl_Y_UV = Kee[int](5)
    BufferFormatEgl_Y_XUXV = Kee[int](6)

  class BufferType(CuteNum):
    """
    The enum 'QWaylandBufferRef::BufferType' of Qt, with the 3 names Qt gives
    in it.
    """

    BufferType_Null = Kee[int](0)
    BufferType_SharedMemory = Kee[int](1)
    BufferType_Egl = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandBufferRef'

  #  Qt's '~QWaylandBufferRef()'. Naming it makes this a value class: Python
  #  owns every C++ QWaylandBufferRef behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QWaylandBufferRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QWaylandBufferRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#isNull
    """
    #  bool QWaylandBufferRef::isNull() const
    return self.uglySide.call('ritual_ZNK17QWaylandBufferRef6isNullEv')

  def hasBuffer(self) -> bool:
    """
    Calls Qt's 'bool QWaylandBufferRef::hasBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#hasBuffer
    """
    #  bool QWaylandBufferRef::hasBuffer() const
    return self.uglySide.call('ritual_ZNK17QWaylandBufferRef9hasBufferEv')

  def hasContent(self) -> bool:
    """
    Calls Qt's 'bool QWaylandBufferRef::hasContent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#hasContent
    """
    #  bool QWaylandBufferRef::hasContent() const
    return self.uglySide.call('ritual_ZNK17QWaylandBufferRef10hasContentEv')

  def hasProtectedContent(self) -> bool:
    """
    Calls Qt's 'bool QWaylandBufferRef::hasProtectedContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#hasProtectedContent
    """
    #  bool QWaylandBufferRef::hasProtectedContent() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandBufferRef19hasProtectedContentEv',
    )

  def isDestroyed(self) -> bool:
    """
    Calls Qt's 'bool QWaylandBufferRef::isDestroyed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#isDestroyed
    """
    #  bool QWaylandBufferRef::isDestroyed() const
    return self.uglySide.call('ritual_ZNK17QWaylandBufferRef11isDestroyedEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandBufferRef::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandBufferRef::size() const
    address = self.uglySide.call('ritual_ZNK17QWaylandBufferRef4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def origin(self) -> QWaylandSurface.Origin:
    """
    Calls Qt's 'QWaylandSurface::Origin QWaylandBufferRef::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#origin

    Returns
    -------

    QWaylandSurface.Origin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWaylandSurface.Origin(number)' gives.
    """
    #  QWaylandSurface::Origin QWaylandBufferRef::origin() const
    return QWaylandSurface.Origin(self.uglySide.call(
        'ritual_ZNK17QWaylandBufferRef6originEv',
    ))

  def bufferType(self) -> BufferType:
    """
    Calls Qt's 'BufferType QWaylandBufferRef::bufferType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#bufferType

    Returns
    -------

    BufferType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BufferType(number)'
      gives.
    """
    #  BufferType QWaylandBufferRef::bufferType() const
    return QWaylandBufferRef.BufferType(self.uglySide.call(
        'ritual_ZNK17QWaylandBufferRef10bufferTypeEv',
    ))

  def bufferFormatEgl(self) -> BufferFormatEgl:
    """
    Calls Qt's 'BufferFormatEgl QWaylandBufferRef::bufferFormatEgl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#bufferFormatEgl

    Returns
    -------

    BufferFormatEgl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BufferFormatEgl(number)'
      gives.
    """
    #  BufferFormatEgl QWaylandBufferRef::bufferFormatEgl() const
    return QWaylandBufferRef.BufferFormatEgl(self.uglySide.call(
        'ritual_ZNK17QWaylandBufferRef15bufferFormatEglEv',
    ))

  def isSharedMemory(self) -> bool:
    """
    Calls Qt's 'bool QWaylandBufferRef::isSharedMemory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#isSharedMemory
    """
    #  bool QWaylandBufferRef::isSharedMemory() const
    return self.uglySide.call(
        'ritual_ZNK17QWaylandBufferRef14isSharedMemoryEv',
    )

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QWaylandBufferRef::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QWaylandBufferRef::image() const
    address = self.uglySide.call('ritual_ZNK17QWaylandBufferRef5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload()
  @overload(int)
  def toOpenGLTexture(self, plane: int = 0) -> Optional[QOpenGLTexture]:
    """
    Calls Qt's 'QOpenGLTexture *QWaylandBufferRef::toOpenGLTexture(int plane)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#toOpenGLTexture

    Parameters
    ----------

    plane : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QOpenGLTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLTexture *QWaylandBufferRef::toOpenGLTexture(int plane) const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandBufferRef15toOpenGLTextureEi', plane,
    )
    from ..QtOpenGL import QOpenGLTexture
    return QOpenGLTexture._cuteAt(address)

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
  def __eq__(self, rhs: QWaylandBufferRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QWaylandBufferRef &lhs, const
    QWaylandBufferRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#operator==

    Parameters
    ----------

    rhs : QWaylandBufferRef
      Passed on as a value: Qt reads the C++ QWaylandBufferRef, which stays
      Python's own.
    """
    #  bool operator==(const QWaylandBufferRef &lhs, const QWaylandBufferRef
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK17QWaylandBufferRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QWaylandBufferRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QWaylandBufferRef &lhs, const
    QWaylandBufferRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandbufferref.html#operator!=

    Parameters
    ----------

    rhs : QWaylandBufferRef
      Passed on as a value: Qt reads the C++ QWaylandBufferRef, which stays
      Python's own.
    """
    #  bool operator!=(const QWaylandBufferRef &lhs, const QWaylandBufferRef
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK17QWaylandBufferRefS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's 'QWaylandBufferRef::QWaylandBufferRef()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#QWaylandBufferRef
    """
    #  QWaylandBufferRef::QWaylandBufferRef()
    self._noteCreation(QWaylandBufferRef, lambda: Rituals.call(
        'ritual_ZN17QWaylandBufferRefC1Ev',
    ))

  @overload(THIS)
  def __init__(self, ref: QWaylandBufferRef) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandBufferRef::QWaylandBufferRef(const QWaylandBufferRef &ref)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#QWaylandBufferRef

    Parameters
    ----------

    ref : QWaylandBufferRef
      Passed on as a value: Qt reads the C++ QWaylandBufferRef, which stays
      Python's own.
    """
    #  QWaylandBufferRef::QWaylandBufferRef(const QWaylandBufferRef &ref)
    self._noteCreation(QWaylandBufferRef, lambda: Rituals.call(
        'ritual_ZN17QWaylandBufferRefC1ERKS_', self._valueOf(ref),
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

  def lockNativeBuffer(self) -> int:
    """
    Calls Qt's 'quintptr QWaylandBufferRef::lockNativeBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#lockNativeBuffer
    """
    #  quintptr QWaylandBufferRef::lockNativeBuffer()
    return self.uglySide.call(
        'ritual_ZN17QWaylandBufferRef16lockNativeBufferEv',
    )

  @overload(int)
  def unlockNativeBuffer(self, handle: int) -> None:
    """
    Calls Qt's 'void QWaylandBufferRef::unlockNativeBuffer(quintptr handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandbufferref.html#unlockNativeBuffer

    Parameters
    ----------

    handle : int
      Passed on as it is.
    """
    #  void QWaylandBufferRef::unlockNativeBuffer(quintptr handle)
    self.uglySide.call(
        'ritual_ZN17QWaylandBufferRef18unlockNativeBufferEy', handle,
    )

  @staticmethod
  def buffer(*__, **_) -> Never:
    """
    Qt's 'QtWayland::ClientBuffer *QWaylandBufferRef::buffer() const': gives
    'QtWayland::ClientBuffer', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandBufferRef.buffer' has no cute function yet. Qt's "
        "'QtWayland::ClientBuffer *QWaylandBufferRef::buffer() const': "
        "gives 'QtWayland::ClientBuffer', which has no cute class yet.")

  @staticmethod
  def wl_buffer(*__, **_) -> Never:
    """
    Qt's 'struct wl_resource *QWaylandBufferRef::wl_buffer() const': gives
    'struct wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandBufferRef.wl_buffer' has no cute function yet. Qt's "
        "'struct wl_resource *QWaylandBufferRef::wl_buffer() const': gives "
        "'struct wl_resource', which has no cute class yet.")
