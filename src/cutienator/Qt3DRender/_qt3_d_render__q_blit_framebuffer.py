"""
Qt3DRender::QBlitFramebuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qblitframebuffer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlitFramebuffer(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QBlitFramebuffer: a plain Python object
  standing in front of one C++ Qt3DRender::QBlitFramebuffer.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QBlitFramebuffer is built on Qt's Qt3DRender::QFrameGraphNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QBlitFramebuffer that has a ritual and
  that Python can call so far, 24 names in all: 'metaObject', 'tr', 'source',
  'destination', 'sourceRect', 'destinationRect', 'sourceAttachmentPoint',
  'destinationAttachmentPoint', 'interpolationMethod', 'setSource',
  'setDestination', 'setSourceRect', 'setDestinationRect',
  'setSourceAttachmentPoint', 'setDestinationAttachmentPoint',
  'setInterpolationMethod', 'sourceChanged', 'destinationChanged',
  'sourceRectChanged', 'destinationRectChanged',
  'sourceAttachmentPointChanged', 'destinationAttachmentPointChanged',
  'interpolationMethodChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QBlitFramebuffer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QBlitFramebuffer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QBlitFramebuffer::~QBlitFramebuffer()': the destructor:
    Python never removes a C++ Qt3DRender::QBlitFramebuffer.
  - Qt's
    'Qt3DRender::QBlitFramebuffer::QBlitFramebuffer(QBlitFramebufferPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QBlitFramebufferPrivate
    *Qt3DRender::QBlitFramebuffer::d_func() const': takes in Python what
    'QBlitFramebufferPrivate *Qt3DRender::QBlitFramebuffer::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QBlitFramebuffer is created at the first use, not by
    'Qt3DRender::QBlitFramebuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QBlitFramebuffer.
  - Qt tells when it has removed the C++ Qt3DRender::QBlitFramebuffer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QBlitFramebuffer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InterpolationMethod(CuteNum):
    """
    The enum 'Qt3DRender::QBlitFramebuffer::InterpolationMethod' of Qt, with
    the 2 names Qt gives in it.
    """

    Nearest = Kee[int](0)
    Linear = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QBlitFramebuffer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#tr

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
    #  QString Qt3DRender::QBlitFramebuffer::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QBlitFramebuffer'

  #  A C++ Qt3DRender::QBlitFramebuffer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QBlitFramebuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QBlitFramebuffer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QBlitFramebuffer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> Optional[Qt3DRender.QRenderTarget]:
    """
    Calls Qt's 'QRenderTarget *Qt3DRender::QBlitFramebuffer::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#source

    Returns
    -------

    Optional[Qt3DRender.QRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderTarget *Qt3DRender::QBlitFramebuffer::source() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer6sourceEv',
    )
    return Qt3DRender.QRenderTarget._cuteAt(address)

  def destination(self) -> Optional[Qt3DRender.QRenderTarget]:
    """
    Calls Qt's 'QRenderTarget *Qt3DRender::QBlitFramebuffer::destination()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#destination

    Returns
    -------

    Optional[Qt3DRender.QRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderTarget *Qt3DRender::QBlitFramebuffer::destination() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer11destinationEv',
    )
    return Qt3DRender.QRenderTarget._cuteAt(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF Qt3DRender::QBlitFramebuffer::sourceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DRender::QBlitFramebuffer::sourceRect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer10sourceRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def destinationRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF Qt3DRender::QBlitFramebuffer::destinationRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#destinationRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DRender::QBlitFramebuffer::destinationRect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer15destinationRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sourceAttachmentPoint(
      self,
  ) -> Qt3DRender.QRenderTargetOutput.AttachmentPoint:
    """
    Calls Qt's 'Qt3DRender::QRenderTargetOutput::AttachmentPoint
    Qt3DRender::QBlitFramebuffer::sourceAttachmentPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Returns
    -------

    Qt3DRender.QRenderTargetOutput.AttachmentPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QRenderTargetOutput.AttachmentPoint(number)' gives.
    """
    #  Qt3DRender::QRenderTargetOutput::AttachmentPoint
    #      Qt3DRender::QBlitFramebuffer::sourceAttachmentPoint() const
    return Qt3DRender.QRenderTargetOutput.AttachmentPoint(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer21sourceAttachmentPointEv',
    ))

  def destinationAttachmentPoint(
      self,
  ) -> Qt3DRender.QRenderTargetOutput.AttachmentPoint:
    """
    Calls Qt's 'Qt3DRender::QRenderTargetOutput::AttachmentPoint
    Qt3DRender::QBlitFramebuffer::destinationAttachmentPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Returns
    -------

    Qt3DRender.QRenderTargetOutput.AttachmentPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QRenderTargetOutput.AttachmentPoint(number)' gives.
    """
    #  Qt3DRender::QRenderTargetOutput::AttachmentPoint
    #      Qt3DRender::QBlitFramebuffer::destinationAttachmentPoint() const
    return Qt3DRender.QRenderTargetOutput.AttachmentPoint(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer26destinationAttachmentPoi'
        'ntEv',
    ))

  def interpolationMethod(self) -> InterpolationMethod:
    """
    Calls Qt's 'InterpolationMethod
    Qt3DRender::QBlitFramebuffer::interpolationMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Returns
    -------

    InterpolationMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InterpolationMethod(number)' gives.
    """
    #  InterpolationMethod
    #      Qt3DRender::QBlitFramebuffer::interpolationMethod() const
    return QBlitFramebuffer.InterpolationMethod(self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QBlitFramebuffer19interpolationMethodEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QRenderTarget'])
  @overload(NoneType)
  def setSource(self, source: Optional[Qt3DRender.QRenderTarget]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::setSource(QRenderTarget
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#setSource

    Parameters
    ----------

    source : Optional[Qt3DRender.QRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QBlitFramebuffer::setSource(QRenderTarget *source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer9setSourceEPNS_13QRenderTar'
        'getE',
        self._addressOf(source),
    )

  @overload(WAIT['Qt3DRender.QRenderTarget'])
  @overload(NoneType)
  def setDestination(
      self,
      destination: Optional[Qt3DRender.QRenderTarget],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::setDestination(QRenderTarget
    *destination)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#setDestination

    Parameters
    ----------

    destination : Optional[Qt3DRender.QRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QBlitFramebuffer::setDestination(QRenderTarget
    #      *destination)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer14setDestinationEPNS_13QRen'
        'derTargetE',
        self._addressOf(destination),
    )

  @overload(QRectF)
  def setSourceRect(self, sourceRect: QRectF) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::setSourceRect(const QRectF
    &sourceRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#setSourceRect

    Parameters
    ----------

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void Qt3DRender::QBlitFramebuffer::setSourceRect(const QRectF
    #      &sourceRect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer13setSourceRectERK6QRectF',
        self._valueOf(sourceRect),
    )

  @overload(QRectF)
  def setDestinationRect(self, destinationRect: QRectF) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::setDestinationRect(const
    QRectF &destinationRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Parameters
    ----------

    destinationRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void Qt3DRender::QBlitFramebuffer::setDestinationRect(const QRectF
    #      &destinationRect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer18setDestinationRectERK6QRe'
        'ctF',
        self._valueOf(destinationRect),
    )

  @overload(Qt3DRender.QRenderTargetOutput.AttachmentPoint)
  def setSourceAttachmentPoint(
      self,
      sourceAttachmentPoint: Qt3DRender.QRenderTargetOutput.AttachmentPoint,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::setSourceAttachmentPoint(Qt3DRender::
    QRenderTargetOutput::AttachmentPoint sourceAttachmentPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Parameters
    ----------

    sourceAttachmentPoint : Qt3DRender.QRenderTargetOutput.AttachmentPoint
      Passed on as its number.
    """
    #  void Qt3DRender::QBlitFramebuffer::setSourceAttachmentPoint(
    #      Qt3DRender::QRenderTargetOutput::AttachmentPoint
    #      sourceAttachmentPoint)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer24setSourceAttachmentPointE'
        'NS_19QRenderTargetOutput15AttachmentPointE',
        sourceAttachmentPoint.value,
    )

  @overload(Qt3DRender.QRenderTargetOutput.AttachmentPoint)
  def setDestinationAttachmentPoint(
      self,
      destinationAttachmentPoint: Qt3DRender.QRenderTargetOutput.AttachmentPoint,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::setDestinationAttachmentPoint(Qt3DRender::
    QRenderTargetOutput::AttachmentPoint destinationAttachmentPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Parameters
    ----------

    destinationAttachmentPoint : Qt3DRender.QRenderTargetOutput.AttachmentPoint
      Passed on as its number.
    """
    #  void Qt3DRender::QBlitFramebuffer::setDestinationAttachmentPoint(
    #      Qt3DRender::QRenderTargetOutput::AttachmentPoint
    #      destinationAttachmentPoint)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer29setDestinationAttachmentP'
        'ointENS_19QRenderTargetOutput15AttachmentPointE',
        destinationAttachmentPoint.value,
    )

  @overload(InterpolationMethod)
  def setInterpolationMethod(
      self,
      interpolationMethod: InterpolationMethod,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::setInterpolationMethod(InterpolationMethod
    interpolationMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html

    Parameters
    ----------

    interpolationMethod : InterpolationMethod
      Passed on as its number.
    """
    #  void Qt3DRender::QBlitFramebuffer::setInterpolationMethod(
    #      InterpolationMethod interpolationMethod)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer22setInterpolationMethodENS'
        '0_19InterpolationMethodE',
        interpolationMethod.value,
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
    'Qt3DRender::QBlitFramebuffer::QBlitFramebuffer(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#QBlitFramebuffer

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QBlitFramebuffer::QBlitFramebuffer(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QBlitFramebuffer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QBlitFramebufferC1EPN8Qt3DCore5QNodeE',
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#sourceChanged
    """
    #  void Qt3DRender::QBlitFramebuffer::sourceChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer13sourceChangedEv',
    )

  def destinationChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::destinationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html
    """
    #  void Qt3DRender::QBlitFramebuffer::destinationChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer18destinationChangedEv',
    )

  def sourceRectChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::sourceRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#sourceRectChanged
    """
    #  void Qt3DRender::QBlitFramebuffer::sourceRectChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer17sourceRectChangedEv',
    )

  def destinationRectChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QBlitFramebuffer::destinationRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html
    """
    #  void Qt3DRender::QBlitFramebuffer::destinationRectChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer22destinationRectChangedEv',
    )

  def sourceAttachmentPointChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::sourceAttachmentPointChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html
    """
    #  void Qt3DRender::QBlitFramebuffer::sourceAttachmentPointChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer28sourceAttachmentPointChan'
        'gedEv',
    )

  def destinationAttachmentPointChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::destinationAttachmentPointChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html
    """
    #  void Qt3DRender::QBlitFramebuffer::destinationAttachmentPointChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer33destinationAttachmentPoin'
        'tChangedEv',
    )

  def interpolationMethodChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QBlitFramebuffer::interpolationMethodChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html
    """
    #  void Qt3DRender::QBlitFramebuffer::interpolationMethodChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer26interpolationMethodChange'
        'dEv',
    )

  def d_func(self) -> Optional[Qt3DRender.QBlitFramebufferPrivate]:
    """
    Calls Qt's 'QBlitFramebufferPrivate
    *Qt3DRender::QBlitFramebuffer::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblitframebuffer.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QBlitFramebufferPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlitFramebufferPrivate *Qt3DRender::QBlitFramebuffer::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender16QBlitFramebuffer6d_funcEv',
    )
    return Qt3DRender.QBlitFramebufferPrivate._cuteAt(address)
