"""
Qt3DRender::QRenderTargetOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrendertargetoutput.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderTargetOutput(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QRenderTargetOutput: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderTargetOutput.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::QRenderTargetOutput is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderTargetOutput that has a ritual
  and that Python can call so far, 18 names in all: 'metaObject', 'tr',
  'attachmentPoint', 'texture', 'mipLevel', 'layer', 'face',
  'setAttachmentPoint', 'setTexture', 'setMipLevel', 'setLayer', 'setFace',
  'attachmentPointChanged', 'textureChanged', 'mipLevelChanged',
  'layerChanged', 'faceChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderTargetOutput::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderTargetOutput::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRenderTargetOutput::~QRenderTargetOutput()': the
    destructor: Python never removes a C++ Qt3DRender::QRenderTargetOutput.
  - Qt's 'Qt3DRender::QRenderTargetOutput::QRenderTargetOutput(
    QRenderTargetOutputPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QRenderTargetOutputPrivate
    *Qt3DRender::QRenderTargetOutput::d_func() const': takes in Python what
    'QRenderTargetOutputPrivate *Qt3DRender::QRenderTargetOutput::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderTargetOutput is created at the first use, not
    by 'Qt3DRender::QRenderTargetOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderTargetOutput.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderTargetOutput.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QRenderTargetOutput, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class AttachmentPoint(CuteNum):
    """
    The enum 'Qt3DRender::QRenderTargetOutput::AttachmentPoint' of Qt, with
    the 21 names Qt gives in it.
    """

    Color0 = Kee[int](0)
    Color1 = Kee[int](1)
    Color2 = Kee[int](2)
    Color3 = Kee[int](3)
    Color4 = Kee[int](4)
    Color5 = Kee[int](5)
    Color6 = Kee[int](6)
    Color7 = Kee[int](7)
    Color8 = Kee[int](8)
    Color9 = Kee[int](9)
    Color10 = Kee[int](10)
    Color11 = Kee[int](11)
    Color12 = Kee[int](12)
    Color13 = Kee[int](13)
    Color14 = Kee[int](14)
    Color15 = Kee[int](15)
    Depth = Kee[int](16)
    Stencil = Kee[int](17)
    DepthStencil = Kee[int](18)
    Left = Kee[int](19)
    Right = Kee[int](20)

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
    Calls Qt's 'QString Qt3DRender::QRenderTargetOutput::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#tr

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
    #  QString Qt3DRender::QRenderTargetOutput::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderTargetOutput'

  #  A C++ Qt3DRender::QRenderTargetOutput Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderTargetOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::QRenderTargetOutput::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderTargetOutput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderTargetOutput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def attachmentPoint(self) -> AttachmentPoint:
    """
    Calls Qt's 'AttachmentPoint
    Qt3DRender::QRenderTargetOutput::attachmentPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html

    Returns
    -------

    AttachmentPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AttachmentPoint(number)'
      gives.
    """
    #  AttachmentPoint Qt3DRender::QRenderTargetOutput::attachmentPoint()
    #      const
    return QRenderTargetOutput.AttachmentPoint(self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderTargetOutput15attachmentPointEv',
    ))

  def texture(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'QAbstractTexture *Qt3DRender::QRenderTargetOutput::texture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#texture

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTexture *Qt3DRender::QRenderTargetOutput::texture() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderTargetOutput7textureEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderTargetOutput::mipLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#mipLevel
    """
    #  int Qt3DRender::QRenderTargetOutput::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderTargetOutput8mipLevelEv',
    )

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderTargetOutput::layer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#layer
    """
    #  int Qt3DRender::QRenderTargetOutput::layer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderTargetOutput5layerEv',
    )

  def face(self) -> Qt3DRender.QAbstractTexture.CubeMapFace:
    """
    Calls Qt's 'QAbstractTexture::CubeMapFace
    Qt3DRender::QRenderTargetOutput::face() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#face

    Returns
    -------

    Qt3DRender.QAbstractTexture.CubeMapFace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.CubeMapFace(number)' gives.
    """
    #  QAbstractTexture::CubeMapFace Qt3DRender::QRenderTargetOutput::face()
    #      const
    return Qt3DRender.QAbstractTexture.CubeMapFace(self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderTargetOutput4faceEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AttachmentPoint)
  def setAttachmentPoint(self, attachmentPoint: AttachmentPoint) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderTargetOutput::setAttachmentPoint(AttachmentPoint
    attachmentPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html

    Parameters
    ----------

    attachmentPoint : AttachmentPoint
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderTargetOutput::setAttachmentPoint(
    #      AttachmentPoint attachmentPoint)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput18setAttachmentPointENS0'
        '_15AttachmentPointE',
        attachmentPoint.value,
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setTexture(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderTargetOutput::setTexture(QAbstractTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#setTexture

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderTargetOutput::setTexture(QAbstractTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput10setTextureEPNS_16QAbst'
        'ractTextureE',
        self._addressOf(texture),
    )

  @overload(int)
  def setMipLevel(self, level: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderTargetOutput::setMipLevel(int
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#setMipLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void Qt3DRender::QRenderTargetOutput::setMipLevel(int level)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput11setMipLevelEi', level,
    )

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderTargetOutput::setLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QRenderTargetOutput::setLayer(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput8setLayerEi', layer,
    )

  @overload(Qt3DRender.QAbstractTexture.CubeMapFace)
  def setFace(self, face: Qt3DRender.QAbstractTexture.CubeMapFace) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderTargetOutput::setFace(QAbstractTexture::CubeMapFace
    face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#setFace

    Parameters
    ----------

    face : Qt3DRender.QAbstractTexture.CubeMapFace
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderTargetOutput::setFace(QAbstractTexture::
    #      CubeMapFace face)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput7setFaceENS_16QAbstractT'
        'exture11CubeMapFaceE',
        face.value,
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
    'Qt3DRender::QRenderTargetOutput::QRenderTargetOutput(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderTargetOutput::QRenderTargetOutput(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QRenderTargetOutput, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutputC1EPN8Qt3DCore5QNodeE',
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

  @overload(AttachmentPoint)
  def attachmentPointChanged(self, attachmentPoint: AttachmentPoint) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderTargetOutput::attachmentPointChanged(AttachmentPoint
    attachmentPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html

    Parameters
    ----------

    attachmentPoint : AttachmentPoint
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderTargetOutput::attachmentPointChanged(
    #      AttachmentPoint attachmentPoint)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput22attachmentPointChanged'
        'ENS0_15AttachmentPointE',
        attachmentPoint.value,
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def textureChanged(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderTargetOutput::textureChanged(QAbstractTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#textureChanged

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRenderTargetOutput::textureChanged(QAbstractTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput14textureChangedEPNS_16Q'
        'AbstractTextureE',
        self._addressOf(texture),
    )

  @overload(int)
  def mipLevelChanged(self, mipLevel: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderTargetOutput::mipLevelChanged(int
    mipLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.
    """
    #  void Qt3DRender::QRenderTargetOutput::mipLevelChanged(int mipLevel)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput15mipLevelChangedEi',
        mipLevel,
    )

  @overload(int)
  def layerChanged(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderTargetOutput::layerChanged(int
    layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#layerChanged

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QRenderTargetOutput::layerChanged(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput12layerChangedEi', layer,
    )

  @overload(Qt3DRender.QAbstractTexture.CubeMapFace)
  def faceChanged(
      self,
      face: Qt3DRender.QAbstractTexture.CubeMapFace,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderTargetOutput::faceChanged(QAbstractTexture::
    CubeMapFace face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#faceChanged

    Parameters
    ----------

    face : Qt3DRender.QAbstractTexture.CubeMapFace
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderTargetOutput::faceChanged(QAbstractTexture::
    #      CubeMapFace face)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput11faceChangedENS_16QAbst'
        'ractTexture11CubeMapFaceE',
        face.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QRenderTargetOutputPrivate]:
    """
    Calls Qt's 'QRenderTargetOutputPrivate
    *Qt3DRender::QRenderTargetOutput::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendertargetoutput.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderTargetOutputPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderTargetOutputPrivate *Qt3DRender::QRenderTargetOutput::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderTargetOutput6d_funcEv',
    )
    return Qt3DRender.QRenderTargetOutputPrivate._cuteAt(address)
