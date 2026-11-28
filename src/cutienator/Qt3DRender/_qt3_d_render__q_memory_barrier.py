"""
Qt3DRender::QMemoryBarrier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qmemorybarrier.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMemoryBarrier(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QMemoryBarrier: a plain Python object
  standing in front of one C++ Qt3DRender::QMemoryBarrier.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QMemoryBarrier is built on Qt's Qt3DRender::QFrameGraphNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QMemoryBarrier that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'waitOperations', 'setWaitOperations', 'waitOperationsChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QMemoryBarrier::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QMemoryBarrier::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QMemoryBarrier::~QMemoryBarrier()': the destructor:
    Python never removes a C++ Qt3DRender::QMemoryBarrier.
  - Qt's 'Qt3DRender::QMemoryBarrier::QMemoryBarrier(QMemoryBarrierPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QMemoryBarrierPrivate *Qt3DRender::QMemoryBarrier::d_func()
    const': takes in Python what 'QMemoryBarrierPrivate
    *Qt3DRender::QMemoryBarrier::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QMemoryBarrier is created at the first use, not by
    'Qt3DRender::QMemoryBarrier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QMemoryBarrier.
  - Qt tells when it has removed the C++ Qt3DRender::QMemoryBarrier. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QMemoryBarrier, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Operation(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt3DRender::QMemoryBarrier::Operation' of Qt, with the 16
    names Qt gives in it. Qt names the type of its combinations
    'Qt3DRender::QMemoryBarrier::Operations'.
    """

    NULL = 0x0
    VertexAttributeArray = 0x1
    ElementArray = 0x2
    Uniform = 0x4
    TextureFetch = 0x8
    ShaderImageAccess = 0x10
    Command = 0x20
    PixelBuffer = 0x40
    TextureUpdate = 0x80
    BufferUpdate = 0x100
    FrameBuffer = 0x200
    TransformFeedback = 0x400
    AtomicCounter = 0x800
    ShaderStorage = 0x1000
    QueryBuffer = 0x2000
    All = 0xffffffff

  Operations = Operation

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QMemoryBarrier::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QMemoryBarrier::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QMemoryBarrier2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QMemoryBarrier'

  #  A C++ Qt3DRender::QMemoryBarrier Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QMemoryBarrier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QMemoryBarrier::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QMemoryBarrier::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QMemoryBarrier10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def waitOperations(self) -> Operations:
    """
    Calls Qt's 'Operations Qt3DRender::QMemoryBarrier::waitOperations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html#waitOperations

    Returns
    -------

    Operations
      The value standing for the combination Qt gave back.
    """
    #  Operations Qt3DRender::QMemoryBarrier::waitOperations() const
    return QMemoryBarrier.Operations(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QMemoryBarrier14waitOperationsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Operations)
  def setWaitOperations(self, operations: Operations) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QMemoryBarrier::setWaitOperations(QMemoryBarrier::Operations
    operations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html#setWaitOperations

    Parameters
    ----------

    operations : Operations
      Passed on as its number.
    """
    #  void Qt3DRender::QMemoryBarrier::setWaitOperations(QMemoryBarrier::
    #      Operations operations)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QMemoryBarrier17setWaitOperationsE6QFlagsIN'
        'S0_9OperationEE',
        operations.value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QMemoryBarrier::QMemoryBarrier(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html#QMemoryBarrier

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QMemoryBarrier::QMemoryBarrier(Qt3DCore::QNode *parent)
    self._noteCreation(QMemoryBarrier, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QMemoryBarrierC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(Operations)
  def waitOperationsChanged(self, barrierTypes: Operations) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QMemoryBarrier::waitOperationsChanged(QMemoryBarrier::
    Operations barrierTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html

    Parameters
    ----------

    barrierTypes : Operations
      Passed on as its number.
    """
    #  void Qt3DRender::QMemoryBarrier::waitOperationsChanged(
    #      QMemoryBarrier::Operations barrierTypes)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QMemoryBarrier21waitOperationsChangedE6QFla'
        'gsINS0_9OperationEE',
        barrierTypes.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QMemoryBarrierPrivate]:
    """
    Calls Qt's 'QMemoryBarrierPrivate *Qt3DRender::QMemoryBarrier::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmemorybarrier.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QMemoryBarrierPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMemoryBarrierPrivate *Qt3DRender::QMemoryBarrier::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QMemoryBarrier6d_funcEv',
    )
    return Qt3DRender.QMemoryBarrierPrivate._cuteAt(address)
