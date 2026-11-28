"""
Qt3DRender::QClearBuffers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qclearbuffers.h, Qt 6.12.0. Changes made here are lost.
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
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QClearBuffers(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QClearBuffers: a plain Python object
  standing in front of one C++ Qt3DRender::QClearBuffers.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QClearBuffers is built on Qt's Qt3DRender::QFrameGraphNode, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QClearBuffers that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'buffers',
  'clearColor', 'clearDepthValue', 'clearStencilValue', 'colorBuffer',
  'setBuffers', 'setClearColor', 'setClearDepthValue',
  'setClearStencilValue', 'setColorBuffer', 'buffersChanged',
  'clearColorChanged', 'clearDepthValueChanged', 'clearStencilValueChanged',
  'colorBufferChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QClearBuffers::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QClearBuffers::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QClearBuffers::~QClearBuffers()': the destructor:
    Python never removes a C++ Qt3DRender::QClearBuffers.
  - Qt's 'Qt3DRender::QClearBuffers::QClearBuffers(QClearBuffersPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QClearBuffersPrivate *Qt3DRender::QClearBuffers::d_func()
    const': takes in Python what 'QClearBuffersPrivate
    *Qt3DRender::QClearBuffers::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QClearBuffers is created at the first use, not by
    'Qt3DRender::QClearBuffers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QClearBuffers.
  - Qt tells when it has removed the C++ Qt3DRender::QClearBuffers. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QClearBuffers, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class BufferType(CuteFlags, number='unsigned int'):
    """
    The flags enum 'Qt3DRender::QClearBuffers::BufferType' of Qt, with the 8
    names Qt gives in it. Qt names the type of its combinations
    'Qt3DRender::QClearBuffers::BufferTypeFlags'.
    """

    NULL = 0x0
    ColorBuffer = 0x1
    DepthBuffer = 0x2
    StencilBuffer = 0x4
    DepthStencilBuffer = 0x6
    ColorDepthBuffer = 0x3
    ColorDepthStencilBuffer = 0x7
    AllBuffers = 0xffffffff

  BufferTypeFlags = BufferType

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
    Calls Qt's 'QString Qt3DRender::QClearBuffers::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#tr

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
    #  QString Qt3DRender::QClearBuffers::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender13QClearBuffers2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QClearBuffers'

  #  A C++ Qt3DRender::QClearBuffers Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QClearBuffers'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QClearBuffers::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QClearBuffers::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QClearBuffers10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buffers(self) -> BufferType:
    """
    Calls Qt's 'BufferType Qt3DRender::QClearBuffers::buffers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#buffers

    Returns
    -------

    BufferType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BufferType(number)'
      gives.
    """
    #  BufferType Qt3DRender::QClearBuffers::buffers() const
    return QClearBuffers.BufferType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QClearBuffers7buffersEv',
    ))

  def clearColor(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DRender::QClearBuffers::clearColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#clearColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DRender::QClearBuffers::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QClearBuffers10clearColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def clearDepthValue(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QClearBuffers::clearDepthValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#clearDepthValue
    """
    #  float Qt3DRender::QClearBuffers::clearDepthValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QClearBuffers15clearDepthValueEv',
    )

  def clearStencilValue(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QClearBuffers::clearStencilValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#clearStencilValue
    """
    #  int Qt3DRender::QClearBuffers::clearStencilValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QClearBuffers17clearStencilValueEv',
    )

  def colorBuffer(self) -> Optional[Qt3DRender.QRenderTargetOutput]:
    """
    Calls Qt's 'QRenderTargetOutput *Qt3DRender::QClearBuffers::colorBuffer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#colorBuffer

    Returns
    -------

    Optional[Qt3DRender.QRenderTargetOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderTargetOutput *Qt3DRender::QClearBuffers::colorBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QClearBuffers11colorBufferEv',
    )
    return Qt3DRender.QRenderTargetOutput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BufferType)
  def setBuffers(self, buffers: BufferType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::setBuffers(BufferType
    buffers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#setBuffers

    Parameters
    ----------

    buffers : BufferType
      Passed on as its number.
    """
    #  void Qt3DRender::QClearBuffers::setBuffers(BufferType buffers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers10setBuffersENS0_10BufferTypeE',
        buffers.value,
    )

  @overload(QColor)
  def setClearColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::setClearColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#setClearColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DRender::QClearBuffers::setClearColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers13setClearColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setClearDepthValue(self, clearDepthValue: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::setClearDepthValue(float
    clearDepthValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#setClearDepthValue

    Parameters
    ----------

    clearDepthValue : float
      Passed on as it is.
    """
    #  void Qt3DRender::QClearBuffers::setClearDepthValue(float
    #      clearDepthValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers18setClearDepthValueEf',
        clearDepthValue,
    )

  @overload(int)
  def setClearStencilValue(self, clearStencilValue: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::setClearStencilValue(int
    clearStencilValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#setClearStencilValue

    Parameters
    ----------

    clearStencilValue : int
      Passed on as it is.
    """
    #  void Qt3DRender::QClearBuffers::setClearStencilValue(int
    #      clearStencilValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers20setClearStencilValueEi',
        clearStencilValue,
    )

  @overload(WAIT['Qt3DRender.QRenderTargetOutput'])
  @overload(NoneType)
  def setColorBuffer(
      self,
      buffer: Optional[Qt3DRender.QRenderTargetOutput],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QClearBuffers::setColorBuffer(QRenderTargetOutput *buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#setColorBuffer

    Parameters
    ----------

    buffer : Optional[Qt3DRender.QRenderTargetOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QClearBuffers::setColorBuffer(QRenderTargetOutput
    #      *buffer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers14setColorBufferEPNS_19QRender'
        'TargetOutputE',
        self._addressOf(buffer),
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
    'Qt3DRender::QClearBuffers::QClearBuffers(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#QClearBuffers

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QClearBuffers::QClearBuffers(Qt3DCore::QNode *parent)
    self._noteCreation(QClearBuffers, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QClearBuffersC1EPN8Qt3DCore5QNodeE',
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

  @overload(BufferType)
  def buffersChanged(self, buffers: BufferType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::buffersChanged(BufferType
    buffers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#buffersChanged

    Parameters
    ----------

    buffers : BufferType
      Passed on as its number.
    """
    #  void Qt3DRender::QClearBuffers::buffersChanged(BufferType buffers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers14buffersChangedENS0_10BufferT'
        'ypeE',
        buffers.value,
    )

  @overload(QColor)
  def clearColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::clearColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#clearColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DRender::QClearBuffers::clearColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers17clearColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def clearDepthValueChanged(self, clearDepthValue: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::clearDepthValueChanged(float
    clearDepthValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html

    Parameters
    ----------

    clearDepthValue : float
      Passed on as it is.
    """
    #  void Qt3DRender::QClearBuffers::clearDepthValueChanged(float
    #      clearDepthValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers22clearDepthValueChangedEf',
        clearDepthValue,
    )

  @overload(int)
  def clearStencilValueChanged(self, clearStencilValue: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QClearBuffers::clearStencilValueChanged(int
    clearStencilValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html

    Parameters
    ----------

    clearStencilValue : int
      Passed on as it is.
    """
    #  void Qt3DRender::QClearBuffers::clearStencilValueChanged(int
    #      clearStencilValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers24clearStencilValueChangedEi',
        clearStencilValue,
    )

  @overload(WAIT['Qt3DRender.QRenderTargetOutput'])
  @overload(NoneType)
  def colorBufferChanged(
      self,
      buffer: Optional[Qt3DRender.QRenderTargetOutput],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QClearBuffers::colorBufferChanged(QRenderTargetOutput
    *buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#colorBufferChanged

    Parameters
    ----------

    buffer : Optional[Qt3DRender.QRenderTargetOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QClearBuffers::colorBufferChanged(QRenderTargetOutput
    #      *buffer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers18colorBufferChangedEPNS_19QRe'
        'nderTargetOutputE',
        self._addressOf(buffer),
    )

  def d_func(self) -> Optional[Qt3DRender.QClearBuffersPrivate]:
    """
    Calls Qt's 'QClearBuffersPrivate *Qt3DRender::QClearBuffers::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qclearbuffers.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QClearBuffersPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QClearBuffersPrivate *Qt3DRender::QClearBuffers::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender13QClearBuffers6d_funcEv',
    )
    return Qt3DRender.QClearBuffersPrivate._cuteAt(address)
