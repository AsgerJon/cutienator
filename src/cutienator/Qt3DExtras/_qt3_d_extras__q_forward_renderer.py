"""
Qt3DExtras::QForwardRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qforwardrenderer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QForwardRenderer(Qt3DRender.QTechniqueFilter):
  """
  The cute side of Qt's Qt3DExtras::QForwardRenderer: a plain Python object
  standing in front of one C++ Qt3DExtras::QForwardRenderer.

  It is built on the cute 'Qt3DRender::QTechniqueFilter', as Qt's
  Qt3DExtras::QForwardRenderer is built on Qt's Qt3DRender::QTechniqueFilter,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QForwardRenderer that has a ritual and
  that Python can call so far, 30 names in all: 'metaObject', 'tr',
  'viewportRect', 'clearColor', 'buffersToClear', 'camera', 'surface',
  'externalRenderTargetSize', 'isFrustumCullingEnabled', 'gamma',
  'showDebugOverlay', 'setViewportRect', 'setClearColor',
  'setBuffersToClear', 'setCamera', 'setSurface',
  'setExternalRenderTargetSize', 'setFrustumCullingEnabled', 'setGamma',
  'setShowDebugOverlay', 'viewportRectChanged', 'clearColorChanged',
  'buffersToClearChanged', 'cameraChanged', 'surfaceChanged',
  'externalRenderTargetSizeChanged', 'frustumCullingEnabledChanged',
  'gammaChanged', 'showDebugOverlayChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QForwardRenderer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QForwardRenderer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QForwardRenderer::~QForwardRenderer()': the destructor:
    Python never removes a C++ Qt3DExtras::QForwardRenderer.
  - Qt's 'const QForwardRendererPrivate
    *Qt3DExtras::QForwardRenderer::d_func() const': takes in Python what
    'QForwardRendererPrivate *Qt3DExtras::QForwardRenderer::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QForwardRenderer is created at the first use, not by
    'Qt3DExtras::QForwardRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QForwardRenderer.
  - Qt tells when it has removed the C++ Qt3DExtras::QForwardRenderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString Qt3DExtras::QForwardRenderer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#tr

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
    #  QString Qt3DExtras::QForwardRenderer::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QForwardRenderer'

  #  A C++ Qt3DExtras::QForwardRenderer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QForwardRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QForwardRenderer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QForwardRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def viewportRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF Qt3DExtras::QForwardRenderer::viewportRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#viewportRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DExtras::QForwardRenderer::viewportRect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer12viewportRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def clearColor(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QForwardRenderer::clearColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#clearColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QForwardRenderer::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer10clearColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def buffersToClear(self) -> Qt3DRender.QClearBuffers.BufferType:
    """
    Calls Qt's 'Qt3DRender::QClearBuffers::BufferType
    Qt3DExtras::QForwardRenderer::buffersToClear() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#buffersToClear

    Returns
    -------

    Qt3DRender.QClearBuffers.BufferType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QClearBuffers.BufferType(number)' gives.
    """
    #  Qt3DRender::QClearBuffers::BufferType
    #      Qt3DExtras::QForwardRenderer::buffersToClear() const
    return Qt3DRender.QClearBuffers.BufferType(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer14buffersToClearEv',
    ))

  def camera(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DExtras::QForwardRenderer::camera()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#camera

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DExtras::QForwardRenderer::camera() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer6cameraEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  def surface(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *Qt3DExtras::QForwardRenderer::surface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#surface

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *Qt3DExtras::QForwardRenderer::surface() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer7surfaceEv',
    )
    return QObject._cuteAt(address)

  def externalRenderTargetSize(self) -> QSize:
    """
    Calls Qt's 'QSize
    Qt3DExtras::QForwardRenderer::externalRenderTargetSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::QForwardRenderer::externalRenderTargetSize() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer24externalRenderTargetSize'
        'Ev',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isFrustumCullingEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QForwardRenderer::isFrustumCullingEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html
    """
    #  bool Qt3DExtras::QForwardRenderer::isFrustumCullingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer23isFrustumCullingEnabledE'
        'v',
    )

  def gamma(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QForwardRenderer::gamma() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#gamma
    """
    #  float Qt3DExtras::QForwardRenderer::gamma() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer5gammaEv',
    )

  def showDebugOverlay(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QForwardRenderer::showDebugOverlay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#showDebugOverlay
    """
    #  bool Qt3DExtras::QForwardRenderer::showDebugOverlay() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QForwardRenderer16showDebugOverlayEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setViewportRect(self, viewportRect: QRectF) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::setViewportRect(const
    QRectF &viewportRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#setViewportRect

    Parameters
    ----------

    viewportRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void Qt3DExtras::QForwardRenderer::setViewportRect(const QRectF
    #      &viewportRect)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer15setViewportRectERK6QRectF',
        self._valueOf(viewportRect),
    )

  @overload(QColor)
  def setClearColor(self, clearColor: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::setClearColor(const QColor
    &clearColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#setClearColor

    Parameters
    ----------

    clearColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QForwardRenderer::setClearColor(const QColor
    #      &clearColor)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer13setClearColorERK6QColor',
        self._valueOf(clearColor),
    )

  @overload(Qt3DRender.QClearBuffers.BufferType)
  def setBuffersToClear(
      self,
      a0: Qt3DRender.QClearBuffers.BufferType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::setBuffersToClear(Qt3DRender::
    QClearBuffers::BufferType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#setBuffersToClear

    Parameters
    ----------

    a0 : Qt3DRender.QClearBuffers.BufferType
      Passed on as its number.
    """
    #  void Qt3DExtras::QForwardRenderer::setBuffersToClear(Qt3DRender::
    #      QClearBuffers::BufferType a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer17setBuffersToClearEN10Qt3D'
        'Render13QClearBuffers10BufferTypeE',
        a0.value,
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setCamera(self, camera: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::setCamera(Qt3DCore::QEntity *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#setCamera

    Parameters
    ----------

    camera : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QForwardRenderer::setCamera(Qt3DCore::QEntity
    #      *camera)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer9setCameraEPN8Qt3DCore7QEnt'
        'ityE',
        self._addressOf(camera),
    )

  @overload(QObject)
  @overload(NoneType)
  def setSurface(self, surface: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::setSurface(QObject
    *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#setSurface

    Parameters
    ----------

    surface : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QForwardRenderer::setSurface(QObject *surface)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer10setSurfaceEP7QObject',
        self._addressOf(surface, 'QObject'),
    )

  @overload(QSize)
  def setExternalRenderTargetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::setExternalRenderTargetSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QForwardRenderer::setExternalRenderTargetSize(const
    #      QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer27setExternalRenderTargetSi'
        'zeERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def setFrustumCullingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::setFrustumCullingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QForwardRenderer::setFrustumCullingEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer24setFrustumCullingEnabledE'
        'b',
        enabled,
    )

  @overload(float)
  def setGamma(self, gamma: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::setGamma(float gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#setGamma

    Parameters
    ----------

    gamma : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QForwardRenderer::setGamma(float gamma)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer8setGammaEf', gamma,
    )

  @overload(bool)
  def setShowDebugOverlay(self, showDebugOverlay: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::setShowDebugOverlay(bool
    showDebugOverlay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    showDebugOverlay : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QForwardRenderer::setShowDebugOverlay(bool
    #      showDebugOverlay)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer19setShowDebugOverlayEb',
        showDebugOverlay,
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
    'Qt3DExtras::QForwardRenderer::QForwardRenderer(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#QForwardRenderer

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QForwardRenderer::QForwardRenderer(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QForwardRenderer, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras16QForwardRendererC1EPN8Qt3DCore5QNodeE',
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

  @overload(QRectF)
  def viewportRectChanged(self, viewportRect: QRectF) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::viewportRectChanged(const
    QRectF &viewportRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    viewportRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void Qt3DExtras::QForwardRenderer::viewportRectChanged(const QRectF
    #      &viewportRect)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer19viewportRectChangedERK6QR'
        'ectF',
        self._valueOf(viewportRect),
    )

  @overload(QColor)
  def clearColorChanged(self, clearColor: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::clearColorChanged(const
    QColor &clearColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#clearColorChanged

    Parameters
    ----------

    clearColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QForwardRenderer::clearColorChanged(const QColor
    #      &clearColor)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer17clearColorChangedERK6QCol'
        'or',
        self._valueOf(clearColor),
    )

  @overload(Qt3DRender.QClearBuffers.BufferType)
  def buffersToClearChanged(
      self,
      a0: Qt3DRender.QClearBuffers.BufferType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::buffersToClearChanged(Qt3DRender::
    QClearBuffers::BufferType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    a0 : Qt3DRender.QClearBuffers.BufferType
      Passed on as its number.
    """
    #  void Qt3DExtras::QForwardRenderer::buffersToClearChanged(Qt3DRender::
    #      QClearBuffers::BufferType a0)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer21buffersToClearChangedEN10'
        'Qt3DRender13QClearBuffers10BufferTypeE',
        a0.value,
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def cameraChanged(self, camera: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::cameraChanged(Qt3DCore::QEntity *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#cameraChanged

    Parameters
    ----------

    camera : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QForwardRenderer::cameraChanged(Qt3DCore::QEntity
    #      *camera)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer13cameraChangedEPN8Qt3DCore'
        '7QEntityE',
        self._addressOf(camera),
    )

  @overload(QObject)
  @overload(NoneType)
  def surfaceChanged(self, surface: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::surfaceChanged(QObject
    *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#surfaceChanged

    Parameters
    ----------

    surface : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QForwardRenderer::surfaceChanged(QObject *surface)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer14surfaceChangedEP7QObject',
        self._addressOf(surface, 'QObject'),
    )

  @overload(QSize)
  def externalRenderTargetSizeChanged(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::externalRenderTargetSizeChanged(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DExtras::QForwardRenderer::externalRenderTargetSizeChanged(
    #      const QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer31externalRenderTargetSizeC'
        'hangedERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def frustumCullingEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::frustumCullingEnabledChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QForwardRenderer::frustumCullingEnabledChanged(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer28frustumCullingEnabledChan'
        'gedEb',
        enabled,
    )

  @overload(float)
  def gammaChanged(self, gamma: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QForwardRenderer::gammaChanged(float
    gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#gammaChanged

    Parameters
    ----------

    gamma : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QForwardRenderer::gammaChanged(float gamma)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer12gammaChangedEf', gamma,
    )

  @overload(bool)
  def showDebugOverlayChanged(self, showDebugOverlay: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QForwardRenderer::showDebugOverlayChanged(bool
    showDebugOverlay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html

    Parameters
    ----------

    showDebugOverlay : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QForwardRenderer::showDebugOverlayChanged(bool
    #      showDebugOverlay)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer23showDebugOverlayChangedEb',
        showDebugOverlay,
    )

  def d_func(self) -> Optional[Qt3DExtras.QForwardRendererPrivate]:
    """
    Calls Qt's 'QForwardRendererPrivate
    *Qt3DExtras::QForwardRenderer::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrenderer.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QForwardRendererPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QForwardRendererPrivate *Qt3DExtras::QForwardRenderer::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QForwardRenderer6d_funcEv',
    )
    return Qt3DExtras.QForwardRendererPrivate._cuteAt(address)
