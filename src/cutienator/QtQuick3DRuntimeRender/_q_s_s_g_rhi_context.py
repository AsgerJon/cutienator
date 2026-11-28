"""
QSSGRhiContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QRhiCommandBuffer, QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QColor, QRhi, QRhiRenderPassDescriptor
  from ..QtGui import QRhiRenderTarget, QRhiResourceUpdateBatch, QRhiSampler
  from . import QSSGRhiContextPrivate, QSSGRhiSamplerDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QSSGRhiSamplerDescription = WAIT['QSSGRhiSamplerDescription']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiContext: a plain Python object standing in
  front of one C++ QSSGRhiContext.

  What exists
  -----------

  Every function of Qt's QSSGRhiContext that has a ritual and that Python can
  call so far, 12 names in all: 'rhi', 'isValid', 'mainRenderPassDescriptor',
  'commandBuffer', 'renderTarget', 'mainPassSampleCount',
  'mainPassViewCount', 'sampler', 'checkAndAdjustForNPoT', 'dummyTexture',
  'commonPassFlags', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiContext::~QSSGRhiContext()': the destructor: Python never
    removes a C++ QSSGRhiContext.
  - Qt's 'const QSSGRhiContextPrivate *QSSGRhiContext::d_func() const': takes
    in Python what 'QSSGRhiContextPrivate *QSSGRhiContext::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRhiContext is created at the first use, not by
    'QSSGRhiContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRhiContext.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QSSGRhiContext::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QSSGRhiContext::rhi() const
    address = self.uglySide.call('ritual_ZNK14QSSGRhiContext3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSSGRhiContext::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#isValid
    """
    #  bool QSSGRhiContext::isValid() const
    return self.uglySide.call('ritual_ZNK14QSSGRhiContext7isValidEv')

  def mainRenderPassDescriptor(self) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QSSGRhiContext::mainRenderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontext.html#mainRenderPassDescriptor

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor *QSSGRhiContext::mainRenderPassDescriptor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QSSGRhiContext24mainRenderPassDescriptorEv',
    )
    from ..QtGui import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def commandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer *QSSGRhiContext::commandBuffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#commandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QSSGRhiContext::commandBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK14QSSGRhiContext13commandBufferEv',
    )
    return QRhiCommandBuffer._cuteAt(address)

  def renderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget *QSSGRhiContext::renderTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#renderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QSSGRhiContext::renderTarget() const
    address = self.uglySide.call(
        'ritual_ZNK14QSSGRhiContext12renderTargetEv',
    )
    from ..QtGui import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def mainPassSampleCount(self) -> int:
    """
    Calls Qt's 'int QSSGRhiContext::mainPassSampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontext.html#mainPassSampleCount
    """
    #  int QSSGRhiContext::mainPassSampleCount() const
    return self.uglySide.call(
        'ritual_ZNK14QSSGRhiContext19mainPassSampleCountEv',
    )

  def mainPassViewCount(self) -> int:
    """
    Calls Qt's 'int QSSGRhiContext::mainPassViewCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontext.html#mainPassViewCount
    """
    #  int QSSGRhiContext::mainPassViewCount() const
    return self.uglySide.call(
        'ritual_ZNK14QSSGRhiContext17mainPassViewCountEv',
    )

  def commonPassFlags(self) -> QRhiCommandBuffer.BeginPassFlags:
    """
    Calls Qt's 'QRhiCommandBuffer::BeginPassFlags
    QSSGRhiContext::commonPassFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontext.html#commonPassFlags

    Returns
    -------

    QRhiCommandBuffer.BeginPassFlags
      The value standing for the combination Qt gave back.
    """
    #  QRhiCommandBuffer::BeginPassFlags QSSGRhiContext::commonPassFlags()
    #      const
    return QRhiCommandBuffer.BeginPassFlags(self.uglySide.call(
        'ritual_ZNK14QSSGRhiContext15commonPassFlagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhi]) -> None:
    """
    Notes what was given, for Qt's 'QSSGRhiContext::QSSGRhiContext(QRhi
    *rhi)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#QSSGRhiContext

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSSGRhiContext::QSSGRhiContext(QRhi *rhi)
    self._noteCreation(QSSGRhiContext, lambda: Rituals.call(
        'ritual_ZN14QSSGRhiContextC1EP4QRhi', self._addressOf(rhi),
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

  @overload(QSSGRhiSamplerDescription)
  def sampler(
      self,
      samplerDescription: QSSGRhiSamplerDescription,
  ) -> Optional[QRhiSampler]:
    """
    Calls Qt's 'QRhiSampler *QSSGRhiContext::sampler(const
    QSSGRhiSamplerDescription &samplerDescription)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#sampler

    Parameters
    ----------

    samplerDescription : QSSGRhiSamplerDescription
      Passed on as a value: Qt reads the C++ QSSGRhiSamplerDescription, which
      stays Python's own.

    Returns
    -------

    Optional[QRhiSampler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSampler *QSSGRhiContext::sampler(const QSSGRhiSamplerDescription
    #      &samplerDescription)
    address = self.uglySide.call(
        'ritual_ZN14QSSGRhiContext7samplerERK25QSSGRhiSamplerDescription',
        self._valueOf(samplerDescription),
    )
    from ..QtGui import QRhiSampler
    return QRhiSampler._cuteAt(address)

  @overload(QRhiTexture, QSSGRhiSamplerDescription)
  @overload(QRhiTexture, NoneType)
  @overload(NoneType, QSSGRhiSamplerDescription)
  @overload(NoneType, NoneType)
  def checkAndAdjustForNPoT(
      self,
      texture: Optional[QRhiTexture],
      samplerDescription: Optional[QSSGRhiSamplerDescription],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiContext::checkAndAdjustForNPoT(QRhiTexture
    *texture, QSSGRhiSamplerDescription *samplerDescription)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontext.html#checkAndAdjustForNPoT

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    samplerDescription : Optional[QSSGRhiSamplerDescription]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContext::checkAndAdjustForNPoT(QRhiTexture *texture,
    #      QSSGRhiSamplerDescription *samplerDescription)
    self.uglySide.call(
        'ritual_ZN14QSSGRhiContext21checkAndAdjustForNPoTEP11QRhiTextureP25'
        'QSSGRhiSamplerDescription',
        self._addressOf(texture), self._addressOf(samplerDescription),
    )

  @overload(QRhiTexture.Flags, QRhiResourceUpdateBatch)
  @overload(QRhiTexture.Flags, NoneType)
  @overload(QRhiTexture.Flags, QRhiResourceUpdateBatch, QSize)
  @overload(QRhiTexture.Flags, NoneType, QSize)
  @overload(QRhiTexture.Flags, QRhiResourceUpdateBatch, QSize, QColor)
  @overload(QRhiTexture.Flags, NoneType, QSize, QColor)
  @overload(QRhiTexture.Flags, QRhiResourceUpdateBatch, QSize, QColor, int)
  @overload(QRhiTexture.Flags, NoneType, QSize, QColor, int)
  def dummyTexture(
      self,
      flags: QRhiTexture.Flags,
      rub: Optional[QRhiResourceUpdateBatch],
      size: Optional[QSize] = None,
      fillColor: Optional[QColor] = None,
      arraySize: int = 0,
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSSGRhiContext::dummyTexture(QRhiTexture::Flags
    flags, QRhiResourceUpdateBatch *rub, const QSize &size, const QColor
    &fillColor, int arraySize)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#dummyTexture

    Parameters
    ----------

    flags : QRhiTexture.Flags
      Passed on as its number.

    rub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize(64, 64)' is then passed on.

    fillColor : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor(Qt.GlobalColor.black)' is
      then passed on.

    arraySize : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSSGRhiContext::dummyTexture(QRhiTexture::Flags flags,
    #      QRhiResourceUpdateBatch *rub, const QSize &size, const QColor
    #      &fillColor, int arraySize)
    if size is None:
      from ..QtCore import QSize
      size = QSize(64, 64)
    if fillColor is None:
      from ..QtGui import QColor
      fillColor = QColor(Qt.GlobalColor.black)
    address = self.uglySide.call(
        'ritual_ZN14QSSGRhiContext12dummyTextureE6QFlagsIN11QRhiTexture4Fla'
        'gEEP23QRhiResourceUpdateBatchRK5QSizeRK6QColori',
        flags.value, self._addressOf(rub), self._valueOf(size),
        self._valueOf(fillColor), arraySize,
    )
    return QRhiTexture._cuteAt(address)

  def d_func(self) -> Optional[QSSGRhiContextPrivate]:
    """
    Calls Qt's 'QSSGRhiContextPrivate *QSSGRhiContext::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontext.html#d_func

    Returns
    -------

    Optional[QSSGRhiContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRhiContextPrivate *QSSGRhiContext::d_func()
    address = self.uglySide.call('ritual_ZN14QSSGRhiContext6d_funcEv')
    from . import QSSGRhiContextPrivate
    return QSSGRhiContextPrivate._cuteAt(address)
