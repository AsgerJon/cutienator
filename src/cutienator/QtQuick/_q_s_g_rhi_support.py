"""
QSGRhiSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhisupport_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGRhiSupport to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QRhi, QSurface
from . import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QImage, QOffscreenSurface, QRhiCommandBuffer
  from ..QtGui import QRhiSwapChain, QRhiTexture, QWindow
  from . import QQuickGraphicsConfiguration, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGraphicsConfiguration = WAIT['QQuickGraphicsConfiguration']
  QQuickWindow = WAIT['QQuickWindow']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QRhiSwapChain = WAIT['QRhiSwapChain']
  QRhiTexture = WAIT['QRhiTexture']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiSupport(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGRhiSupport: a plain Python object standing in
  front of one C++ QSGRhiSupport.

  C++ hands a QSGRhiSupport around as a copy, so every C++ QSGRhiSupport
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGRhiSupport that has a ritual and that Python can
  call so far, 22 names in all: 'instance_internal', 'instance',
  'chooseSampleCount', 'chooseSampleCountForWindowWithRhi',
  'grabAndBlockInCurrentFrame', 'checkEnvQSgInfo', 'configure', 'rhiBackend',
  'rhiBackendName', 'graphicsApi', 'windowSurfaceType',
  'maybeCreateOffscreenSurface', 'createRhi', 'destroyRhi',
  'prepareWindowForRhi', 'grabOffscreen', 'applySwapChainFormat',
  'attemptReinitWithSwRastUponFail', 'applySettings',
  'adjustToPlatformQuirks', 'preparePipelineCache', 'finalizePipelineCache'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormatFromGL(uint
    format, QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which
    has no cute class yet.
  - Qt's 'QRhiTexture::Format
    QSGRhiSupport::toRhiTextureFormatFromVulkan(uint format,
    QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which has no
    cute class yet.
  - Qt's 'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormatFromMetal(uint
    format, QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which
    has no cute class yet.
  - Qt's 'const void
    *QSGRhiSupport::rifResource(QSGRendererInterface::Resource res, const
    QSGDefaultRenderContext *rc, const QQuickWindow *w)': gives 'void', which
    has no cute class yet.
  - Qt's 'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormat(uint
    nativeFormat, QRhiTexture::Flags *flags) const': names
    'QRhiTexture::Flags', which has no cute class yet.
  - Qt's 'QSGRhiSupport::~QSGRhiSupport()': the destructor: Python removes
    its C++ QSGRhiSupport by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGRhiSupport is created at the first use, not by
    'QSGRhiSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGRhiSupport back gives a copy the ritual made for
    Python, in a new cute QSGRhiSupport.
  - Each name of Qt's QSGRhiSupport that has no cute function yet,
    'rifResource', 'toRhiTextureFormat', 'toRhiTextureFormatFromGL',
    'toRhiTextureFormatFromMetal', 'toRhiTextureFormatFromVulkan', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGRhiSupport, each a class in here as in
  #  C++.

  class RhiCreateResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGRhiSupport::RhiCreateResult: a plain Python
    object standing in front of one C++ QSGRhiSupport::RhiCreateResult.

    C++ hands a QSGRhiSupport::RhiCreateResult around as a copy, so every C++
    QSGRhiSupport::RhiCreateResult behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSGRhiSupport::RhiCreateResult yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGRhiSupport::RhiCreateResult::~RhiCreateResult()': the
      destructor: Python removes its C++ QSGRhiSupport::RhiCreateResult by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSGRhiSupport::RhiCreateResult is created at the first use, not
      by 'QSGRhiSupport::RhiCreateResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGRhiSupport::RhiCreateResult back gives a copy
      the ritual made for Python, in a new cute
      QSGRhiSupport::RhiCreateResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGRhiSupport::RhiCreateResult'

    #  Qt's '~QSGRhiSupport::RhiCreateResult()'. Naming it makes this a value
    #  class: Python owns every C++ QSGRhiSupport::RhiCreateResult behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSGRhiSupport15RhiCreateResultD1Ev'

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

  @staticmethod
  def instance_internal() -> Optional[QSGRhiSupport]:
    """
    Calls Qt's 'QSGRhiSupport *QSGRhiSupport::instance_internal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#instance_internal

    Returns
    -------

    Optional[QSGRhiSupport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRhiSupport *QSGRhiSupport::instance_internal()
    address = Rituals.call('ritual_ZN13QSGRhiSupport17instance_internalEv')
    return QSGRhiSupport._cuteAt(address)

  @staticmethod
  def instance() -> Optional[QSGRhiSupport]:
    """
    Calls Qt's 'QSGRhiSupport *QSGRhiSupport::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#instance

    Returns
    -------

    Optional[QSGRhiSupport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRhiSupport *QSGRhiSupport::instance()
    address = Rituals.call('ritual_ZN13QSGRhiSupport8instanceEv')
    return QSGRhiSupport._cuteAt(address)

  @staticmethod
  @overload(int, QRhi)
  @overload(int, NoneType)
  def chooseSampleCount(samples: int, rhi: Optional[QRhi]) -> int:
    """
    Calls Qt's 'int QSGRhiSupport::chooseSampleCount(int samples, QRhi
    *rhi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#chooseSampleCount

    Parameters
    ----------

    samples : int
      Passed on as it is.

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGRhiSupport::chooseSampleCount(int samples, QRhi *rhi)
    return Rituals.call(
        'ritual_ZN13QSGRhiSupport17chooseSampleCountEiP4QRhi',
        samples, CuteMixin._addressOf(rhi),
    )

  @staticmethod
  @overload(QWindow, QRhi)
  @overload(QWindow, NoneType)
  @overload(NoneType, QRhi)
  @overload(NoneType, NoneType)
  def chooseSampleCountForWindowWithRhi(
      window: Optional[QWindow],
      rhi: Optional[QRhi],
  ) -> int:
    """
    Calls Qt's 'int QSGRhiSupport::chooseSampleCountForWindowWithRhi(QWindow
    *window, QRhi *rhi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGRhiSupport::chooseSampleCountForWindowWithRhi(QWindow *window,
    #      QRhi *rhi)
    return Rituals.call(
        'ritual_ZN13QSGRhiSupport33chooseSampleCountForWindowWithRhiEP7QWin'
        'dowP4QRhi',
        CuteMixin._addressOf(window), CuteMixin._addressOf(rhi),
    )

  @staticmethod
  @overload(QRhi, QRhiCommandBuffer)
  @overload(QRhi, NoneType)
  @overload(NoneType, QRhiCommandBuffer)
  @overload(NoneType, NoneType)
  @overload(QRhi, QRhiCommandBuffer, QRhiTexture)
  @overload(QRhi, QRhiCommandBuffer, NoneType)
  @overload(QRhi, NoneType, QRhiTexture)
  @overload(QRhi, NoneType, NoneType)
  @overload(NoneType, QRhiCommandBuffer, QRhiTexture)
  @overload(NoneType, QRhiCommandBuffer, NoneType)
  @overload(NoneType, NoneType, QRhiTexture)
  @overload(NoneType, NoneType, NoneType)
  def grabAndBlockInCurrentFrame(
      rhi: Optional[QRhi],
      cb: Optional[QRhiCommandBuffer],
      src: Optional[QRhiTexture] = None,
  ) -> QImage:
    """
    Calls Qt's 'QImage QSGRhiSupport::grabAndBlockInCurrentFrame(QRhi *rhi,
    QRhiCommandBuffer *cb, QRhiTexture *src)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#grabAndBlockInCurrentFrame

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    src : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGRhiSupport::grabAndBlockInCurrentFrame(QRhi *rhi,
    #      QRhiCommandBuffer *cb, QRhiTexture *src)
    address = Rituals.call(
        'ritual_ZN13QSGRhiSupport26grabAndBlockInCurrentFrameEP4QRhiP17QRhi'
        'CommandBufferP11QRhiTexture',
        CuteMixin._addressOf(rhi), CuteMixin._addressOf(cb),
        CuteMixin._addressOf(src),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @staticmethod
  def checkEnvQSgInfo() -> None:
    """
    Calls Qt's 'void QSGRhiSupport::checkEnvQSgInfo()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#checkEnvQSgInfo
    """
    #  void QSGRhiSupport::checkEnvQSgInfo()
    Rituals.call('ritual_ZN13QSGRhiSupport15checkEnvQSgInfoEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiSupport'

  #  Qt's '~QSGRhiSupport()'. Naming it makes this a value class: Python owns
  #  every C++ QSGRhiSupport behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QSGRhiSupportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rhiBackend(self) -> QRhi.Implementation:
    """
    Calls Qt's 'QRhi::Implementation QSGRhiSupport::rhiBackend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#rhiBackend

    Returns
    -------

    QRhi.Implementation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.Implementation(number)' gives.
    """
    #  QRhi::Implementation QSGRhiSupport::rhiBackend() const
    return QRhi.Implementation(self.uglySide.call(
        'ritual_ZNK13QSGRhiSupport10rhiBackendEv',
    ))

  def rhiBackendName(self) -> str:
    """
    Calls Qt's 'QString QSGRhiSupport::rhiBackendName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#rhiBackendName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSGRhiSupport::rhiBackendName() const
    return self.uglySide.call('ritual_ZNK13QSGRhiSupport14rhiBackendNameEv')

  def graphicsApi(self) -> QSGRendererInterface.GraphicsApi:
    """
    Calls Qt's 'QSGRendererInterface::GraphicsApi
    QSGRhiSupport::graphicsApi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#graphicsApi

    Returns
    -------

    QSGRendererInterface.GraphicsApi
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGRendererInterface.GraphicsApi(number)' gives.
    """
    #  QSGRendererInterface::GraphicsApi QSGRhiSupport::graphicsApi() const
    return QSGRendererInterface.GraphicsApi(self.uglySide.call(
        'ritual_ZNK13QSGRhiSupport11graphicsApiEv',
    ))

  def windowSurfaceType(self) -> QSurface.SurfaceType:
    """
    Calls Qt's 'QSurface::SurfaceType QSGRhiSupport::windowSurfaceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#windowSurfaceType

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  QSurface::SurfaceType QSGRhiSupport::windowSurfaceType() const
    return QSurface.SurfaceType(self.uglySide.call(
        'ritual_ZNK13QSGRhiSupport17windowSurfaceTypeEv',
    ))

  def attemptReinitWithSwRastUponFail(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiSupport::attemptReinitWithSwRastUponFail() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#attemptReinitWithSwRastUponFail
    """
    #  bool QSGRhiSupport::attemptReinitWithSwRastUponFail() const
    return self.uglySide.call(
        'ritual_ZNK13QSGRhiSupport31attemptReinitWithSwRastUponFailEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSGRhiSupport::QSGRhiSupport()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#QSGRhiSupport
    """
    #  QSGRhiSupport::QSGRhiSupport()
    self._noteCreation(QSGRhiSupport, lambda: Rituals.call(
        'ritual_ZN13QSGRhiSupportC1Ev',
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

  @overload(QSGRendererInterface.GraphicsApi)
  def configure(self, api: QSGRendererInterface.GraphicsApi) -> None:
    """
    Calls Qt's 'void
    QSGRhiSupport::configure(QSGRendererInterface::GraphicsApi api)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#configure

    Parameters
    ----------

    api : QSGRendererInterface.GraphicsApi
      Passed on as its number.
    """
    #  void QSGRhiSupport::configure(QSGRendererInterface::GraphicsApi api)
    self.uglySide.call(
        'ritual_ZN13QSGRhiSupport9configureEN20QSGRendererInterface11Graphi'
        'csApiE',
        api.value,
    )

  @overload(QWindow)
  @overload(NoneType)
  def maybeCreateOffscreenSurface(
      self,
      window: Optional[QWindow],
  ) -> Optional[QOffscreenSurface]:
    """
    Calls Qt's 'QOffscreenSurface
    *QSGRhiSupport::maybeCreateOffscreenSurface(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#maybeCreateOffscreenSurface

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOffscreenSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOffscreenSurface *QSGRhiSupport::maybeCreateOffscreenSurface(QWindow
    #      *window)
    address = self.uglySide.call(
        'ritual_ZN13QSGRhiSupport27maybeCreateOffscreenSurfaceEP7QWindow',
        self._addressOf(window),
    )
    from ..QtGui import QOffscreenSurface
    return QOffscreenSurface._cuteAt(address)

  @overload(QQuickWindow, QSurface)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QSurface)
  @overload(NoneType, NoneType)
  @overload(QQuickWindow, QSurface, bool)
  @overload(QQuickWindow, NoneType, bool)
  @overload(NoneType, QSurface, bool)
  @overload(NoneType, NoneType, bool)
  def createRhi(
      self,
      window: Optional[QQuickWindow],
      offscreenSurface: Optional[QSurface],
      forcePreferSwRenderer: bool = False,
  ) -> RhiCreateResult:
    """
    Calls Qt's 'RhiCreateResult QSGRhiSupport::createRhi(QQuickWindow
    *window, QSurface *offscreenSurface, bool forcePreferSwRenderer)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#createRhi

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offscreenSurface : Optional[QSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forcePreferSwRenderer : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    RhiCreateResult
      A new cute QSGRhiSupport::RhiCreateResult around the copy Qt gave back.
      Python owns it.
    """
    #  RhiCreateResult QSGRhiSupport::createRhi(QQuickWindow *window,
    #      QSurface *offscreenSurface, bool forcePreferSwRenderer)
    address = self.uglySide.call(
        'ritual_ZN13QSGRhiSupport9createRhiEP12QQuickWindowP8QSurfaceb',
        self._addressOf(window), self._addressOf(offscreenSurface,
        'QSurface'), forcePreferSwRenderer,
    )
    return QSGRhiSupport.RhiCreateResult._cuteOwning(address)

  @overload(QRhi, QQuickGraphicsConfiguration)
  @overload(NoneType, QQuickGraphicsConfiguration)
  def destroyRhi(
      self,
      rhi: Optional[QRhi],
      config: QQuickGraphicsConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::destroyRhi(QRhi *rhi, const
    QQuickGraphicsConfiguration &config)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#destroyRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QQuickGraphicsConfiguration
      Passed on as a value: Qt reads the C++ QQuickGraphicsConfiguration,
      which stays Python's own.
    """
    #  void QSGRhiSupport::destroyRhi(QRhi *rhi, const
    #      QQuickGraphicsConfiguration &config)
    self.uglySide.call(
        'ritual_ZN13QSGRhiSupport10destroyRhiEP4QRhiRK27QQuickGraphicsConfi'
        'guration',
        self._addressOf(rhi), self._valueOf(config),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def prepareWindowForRhi(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::prepareWindowForRhi(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#prepareWindowForRhi

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiSupport::prepareWindowForRhi(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRhiSupport19prepareWindowForRhiEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def grabOffscreen(self, window: Optional[QQuickWindow]) -> QImage:
    """
    Calls Qt's 'QImage QSGRhiSupport::grabOffscreen(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#grabOffscreen

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGRhiSupport::grabOffscreen(QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN13QSGRhiSupport13grabOffscreenEP12QQuickWindow',
        self._addressOf(window),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QRhiSwapChain, QQuickWindow)
  @overload(QRhiSwapChain, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def applySwapChainFormat(
      self,
      scWithWindowSet: Optional[QRhiSwapChain],
      window: Optional[QQuickWindow],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::applySwapChainFormat(QRhiSwapChain
    *scWithWindowSet, QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#applySwapChainFormat

    Parameters
    ----------

    scWithWindowSet : Optional[QRhiSwapChain]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiSupport::applySwapChainFormat(QRhiSwapChain
    #      *scWithWindowSet, QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRhiSupport20applySwapChainFormatEP13QRhiSwapChainP12'
        'QQuickWindow',
        self._addressOf(scWithWindowSet), self._addressOf(window),
    )

  def applySettings(self) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::applySettings()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhisupport.html#applySettings
    """
    #  void QSGRhiSupport::applySettings()
    self.uglySide.call('ritual_ZN13QSGRhiSupport13applySettingsEv')

  def adjustToPlatformQuirks(self) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::adjustToPlatformQuirks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#adjustToPlatformQuirks
    """
    #  void QSGRhiSupport::adjustToPlatformQuirks()
    self.uglySide.call('ritual_ZN13QSGRhiSupport22adjustToPlatformQuirksEv')

  @overload(QRhi, QQuickWindow)
  @overload(QRhi, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def preparePipelineCache(
      self,
      rhi: Optional[QRhi],
      window: Optional[QQuickWindow],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::preparePipelineCache(QRhi *rhi,
    QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#preparePipelineCache

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiSupport::preparePipelineCache(QRhi *rhi, QQuickWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN13QSGRhiSupport20preparePipelineCacheEP4QRhiP12QQuickWind'
        'ow',
        self._addressOf(rhi), self._addressOf(window),
    )

  @overload(QRhi, QQuickGraphicsConfiguration)
  @overload(NoneType, QQuickGraphicsConfiguration)
  def finalizePipelineCache(
      self,
      rhi: Optional[QRhi],
      config: QQuickGraphicsConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QSGRhiSupport::finalizePipelineCache(QRhi *rhi, const
    QQuickGraphicsConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhisupport.html#finalizePipelineCache

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    config : QQuickGraphicsConfiguration
      Passed on as a value: Qt reads the C++ QQuickGraphicsConfiguration,
      which stays Python's own.
    """
    #  void QSGRhiSupport::finalizePipelineCache(QRhi *rhi, const
    #      QQuickGraphicsConfiguration &config)
    self.uglySide.call(
        'ritual_ZN13QSGRhiSupport21finalizePipelineCacheEP4QRhiRK27QQuickGr'
        'aphicsConfiguration',
        self._addressOf(rhi), self._valueOf(config),
    )

  @staticmethod
  def rifResource(*__, **_) -> Never:
    """
    Qt's 'const void
    *QSGRhiSupport::rifResource(QSGRendererInterface::Resource res, const
    QSGDefaultRenderContext *rc, const QQuickWindow *w)': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiSupport.rifResource' has no cute function yet. Qt's 'const "
        "void *QSGRhiSupport::rifResource(QSGRendererInterface::Resource "
        "res, const QSGDefaultRenderContext *rc, const QQuickWindow *w)': "
        "gives 'void', which has no cute class yet.")

  @staticmethod
  def toRhiTextureFormat(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormat(uint
    nativeFormat, QRhiTexture::Flags *flags) const': names
    'QRhiTexture::Flags', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiSupport.toRhiTextureFormat' has no cute function yet. Qt's "
        "'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormat(uint "
        "nativeFormat, QRhiTexture::Flags *flags) const': names "
        "'QRhiTexture::Flags', which has no cute class yet.")

  @staticmethod
  def toRhiTextureFormatFromGL(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormatFromGL(uint
    format, QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiSupport.toRhiTextureFormatFromGL' has no cute function yet. "
        "Qt's 'QRhiTexture::Format "
        "QSGRhiSupport::toRhiTextureFormatFromGL(uint format, "
        "QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which has "
        "no cute class yet.")

  @staticmethod
  def toRhiTextureFormatFromMetal(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture::Format QSGRhiSupport::toRhiTextureFormatFromMetal(uint
    format, QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiSupport.toRhiTextureFormatFromMetal' has no cute function "
        "yet. Qt's 'QRhiTexture::Format "
        "QSGRhiSupport::toRhiTextureFormatFromMetal(uint format, "
        "QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which has "
        "no cute class yet.")

  @staticmethod
  def toRhiTextureFormatFromVulkan(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture::Format
    QSGRhiSupport::toRhiTextureFormatFromVulkan(uint format,
    QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiSupport.toRhiTextureFormatFromVulkan' has no cute function "
        "yet. Qt's 'QRhiTexture::Format "
        "QSGRhiSupport::toRhiTextureFormatFromVulkan(uint format, "
        "QRhiTexture::Flags *flags)': names 'QRhiTexture::Flags', which has "
        "no cute class yet.")
