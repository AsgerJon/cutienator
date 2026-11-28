"""
QSSGRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QSSGRenderContextInterface, QSSGRenderGraphObject
  from . import QSSGRenderLayer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QSSGRenderLayer = WAIT['QSSGRenderLayer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderer: a plain Python object standing in front
  of one C++ QSSGRenderer.

  What exists
  -----------

  Every function of Qt's QSSGRenderer that has a ritual and that Python can
  call so far, 14 names in all: 'frameCount', 'setViewport', 'viewport',
  'setDpr', 'dpr', 'setScissorRect', 'scissorRect', 'frameDepth',
  'contextInterface', 'endLayerRender', 'addMaterialDirtyClear',
  'cleanupUnreferencedBuffers', 'resetResourceCounters',
  'releaseCachedResources'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderer::~QSSGRenderer()': the destructor: Python never
    removes a C++ QSSGRenderer.
  - Qt's 'bool QSSGRenderer::prepareLayerForRender(QSSGRenderLayer
    &inLayer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::rhiPrepare(QSSGRenderLayer &inLayer)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::rhiRender(QSSGRenderLayer &inLayer)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::beginFrame(QSSGRenderLayer &layer, bool
    allowRecursion)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGRenderer::endFrame(QSSGRenderLayer &layer, bool
    allowRecursion)': takes a type Python has no way to hand over yet.
  - Qt's 'const std::unique_ptr<QSSGRhiQuadRenderer>
    &QSSGRenderer::rhiQuadRenderer() const': gives a type Python has no way
    to take yet.
  - Qt's 'const std::unique_ptr<QSSGRhiCubeRenderer>
    &QSSGRenderer::rhiCubeRenderer() const': gives a type Python has no way
    to take yet.
  - Qt's 'void QSSGRenderer::beginSubLayerRender(QSSGLayerRenderData
    &inLayer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::endSubLayerRender(QSSGLayerRenderData
    &inLayer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::releaseItem2DData(const QSSGRenderItem2D
    &item2D)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::cleanupResources(QList<QSSGRenderGraphObject *>
    &resources)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::cleanupResources(QSet<QSSGRenderGraphObject *>
    &resources)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGLayerRenderData
    *QSSGRenderer::getOrCreateLayerRenderData(QSSGRenderLayer &layer)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::beginLayerRender(QSSGLayerRenderData &inLayer)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::registerItem2DData(QSSGRenderItem2DData &data)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderer::unregisterItem2DData(QSSGRenderItem2DData
    &data)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderer is created at the first use, not by
    'QSSGRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderer.
  - Each name of Qt's QSSGRenderer that has no cute function yet,
    'beginFrame', 'beginLayerRender', 'beginSubLayerRender',
    'cleanupResources', 'endFrame', 'endSubLayerRender',
    'getOrCreateLayerRenderData', 'prepareLayerForRender',
    'registerItem2DData', 'releaseItem2DData', 'rhiCubeRenderer',
    'rhiPrepare', 'rhiQuadRenderer', 'rhiRender', 'unregisterItem2DData',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def frameCount(self) -> int:
    """
    Calls Qt's 'quint32 QSSGRenderer::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#frameCount
    """
    #  quint32 QSSGRenderer::frameCount() const
    return self.uglySide.call('ritual_ZNK12QSSGRenderer10frameCountEv')

  def viewport(self) -> QRect:
    """
    Calls Qt's 'QRect QSSGRenderer::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#viewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSSGRenderer::viewport() const
    address = self.uglySide.call('ritual_ZNK12QSSGRenderer8viewportEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def dpr(self) -> float:
    """
    Calls Qt's 'float QSSGRenderer::dpr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#dpr
    """
    #  float QSSGRenderer::dpr() const
    return self.uglySide.call('ritual_ZNK12QSSGRenderer3dprEv')

  def scissorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QSSGRenderer::scissorRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#scissorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSSGRenderer::scissorRect() const
    address = self.uglySide.call('ritual_ZNK12QSSGRenderer11scissorRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def frameDepth(self) -> int:
    """
    Calls Qt's 'quint32 QSSGRenderer::frameDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#frameDepth
    """
    #  quint32 QSSGRenderer::frameDepth() const
    return self.uglySide.call('ritual_ZNK12QSSGRenderer10frameDepthEv')

  def contextInterface(self) -> Optional[QSSGRenderContextInterface]:
    """
    Calls Qt's 'QSSGRenderContextInterface *QSSGRenderer::contextInterface()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#contextInterface

    Returns
    -------

    Optional[QSSGRenderContextInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderContextInterface *QSSGRenderer::contextInterface() const
    address = self.uglySide.call(
        'ritual_ZNK12QSSGRenderer16contextInterfaceEv',
    )
    from . import QSSGRenderContextInterface
    return QSSGRenderContextInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setViewport(self, inViewport: QRect) -> None:
    """
    Calls Qt's 'void QSSGRenderer::setViewport(QRect inViewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#setViewport

    Parameters
    ----------

    inViewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSSGRenderer::setViewport(QRect inViewport)
    self.uglySide.call(
        'ritual_ZN12QSSGRenderer11setViewportE5QRect',
        self._valueOf(inViewport),
    )

  @overload(float)
  def setDpr(self, dpr: float) -> None:
    """
    Calls Qt's 'void QSSGRenderer::setDpr(float dpr)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#setDpr

    Parameters
    ----------

    dpr : float
      Passed on as it is.
    """
    #  void QSSGRenderer::setDpr(float dpr)
    self.uglySide.call('ritual_ZN12QSSGRenderer6setDprEf', dpr)

  @overload(QRect)
  def setScissorRect(self, inScissorRect: QRect) -> None:
    """
    Calls Qt's 'void QSSGRenderer::setScissorRect(QRect inScissorRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#setScissorRect

    Parameters
    ----------

    inScissorRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSSGRenderer::setScissorRect(QRect inScissorRect)
    self.uglySide.call(
        'ritual_ZN12QSSGRenderer14setScissorRectE5QRect',
        self._valueOf(inScissorRect),
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
    Notes what was given, for Qt's 'QSSGRenderer::QSSGRenderer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#QSSGRenderer
    """
    #  QSSGRenderer::QSSGRenderer()
    self._noteCreation(QSSGRenderer, lambda: Rituals.call(
        'ritual_ZN12QSSGRendererC1Ev',
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

  def endLayerRender(self) -> None:
    """
    Calls Qt's 'void QSSGRenderer::endLayerRender()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderer.html#endLayerRender
    """
    #  void QSSGRenderer::endLayerRender()
    self.uglySide.call('ritual_ZN12QSSGRenderer14endLayerRenderEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def addMaterialDirtyClear(
      self,
      material: Optional[QSSGRenderGraphObject],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGRenderer::addMaterialDirtyClear(QSSGRenderGraphObject *material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderer.html#addMaterialDirtyClear

    Parameters
    ----------

    material : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRenderer::addMaterialDirtyClear(QSSGRenderGraphObject
    #      *material)
    self.uglySide.call(
        'ritual_ZN12QSSGRenderer21addMaterialDirtyClearEP21QSSGRenderGraphO'
        'bject',
        self._addressOf(material),
    )

  @overload(QSSGRenderLayer)
  @overload(NoneType)
  def cleanupUnreferencedBuffers(
      self,
      inLayer: Optional[QSSGRenderLayer],
  ) -> None:
    """
    Calls Qt's 'void QSSGRenderer::cleanupUnreferencedBuffers(QSSGRenderLayer
    *inLayer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderer.html#cleanupUnreferencedBuffers

    Parameters
    ----------

    inLayer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRenderer::cleanupUnreferencedBuffers(QSSGRenderLayer
    #      *inLayer)
    self.uglySide.call(
        'ritual_ZN12QSSGRenderer26cleanupUnreferencedBuffersEP15QSSGRenderL'
        'ayer',
        self._addressOf(inLayer),
    )

  @overload(QSSGRenderLayer)
  @overload(NoneType)
  def resetResourceCounters(
      self,
      inLayer: Optional[QSSGRenderLayer],
  ) -> None:
    """
    Calls Qt's 'void QSSGRenderer::resetResourceCounters(QSSGRenderLayer
    *inLayer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderer.html#resetResourceCounters

    Parameters
    ----------

    inLayer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRenderer::resetResourceCounters(QSSGRenderLayer *inLayer)
    self.uglySide.call(
        'ritual_ZN12QSSGRenderer21resetResourceCountersEP15QSSGRenderLayer',
        self._addressOf(inLayer),
    )

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGRenderer::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderer.html#releaseCachedResources
    """
    #  void QSSGRenderer::releaseCachedResources()
    self.uglySide.call('ritual_ZN12QSSGRenderer22releaseCachedResourcesEv')

  @staticmethod
  def beginFrame(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::beginFrame(QSSGRenderLayer &layer, bool
    allowRecursion)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.beginFrame' has no cute function yet. Qt's 'void "
        "QSSGRenderer::beginFrame(QSSGRenderLayer &layer, bool "
        "allowRecursion)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def beginLayerRender(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::beginLayerRender(QSSGLayerRenderData &inLayer)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.beginLayerRender' has no cute function yet. Qt's "
        "'void QSSGRenderer::beginLayerRender(QSSGLayerRenderData "
        "&inLayer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def beginSubLayerRender(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::beginSubLayerRender(QSSGLayerRenderData
    &inLayer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.beginSubLayerRender' has no cute function yet. Qt's "
        "'void QSSGRenderer::beginSubLayerRender(QSSGLayerRenderData "
        "&inLayer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def cleanupResources(*__, **_) -> Never:
    """
    - Qt's 'void QSSGRenderer::cleanupResources(QList<QSSGRenderGraphObject
      *> &resources)': takes a type Python has no way to hand over yet.
    - Qt's 'void QSSGRenderer::cleanupResources(QSet<QSSGRenderGraphObject *>
      &resources)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.cleanupResources' has no cute function yet. Qt's "
        "'void QSSGRenderer::cleanupResources(QList<QSSGRenderGraphObject "
        "*> &resources)': takes a type Python has no way to hand over yet. "
        "Qt's 'void "
        "QSSGRenderer::cleanupResources(QSet<QSSGRenderGraphObject *> "
        "&resources)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def endFrame(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderer::endFrame(QSSGRenderLayer &layer, bool
    allowRecursion)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.endFrame' has no cute function yet. Qt's 'bool "
        "QSSGRenderer::endFrame(QSSGRenderLayer &layer, bool "
        "allowRecursion)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def endSubLayerRender(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::endSubLayerRender(QSSGLayerRenderData
    &inLayer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.endSubLayerRender' has no cute function yet. Qt's "
        "'void QSSGRenderer::endSubLayerRender(QSSGLayerRenderData "
        "&inLayer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getOrCreateLayerRenderData(*__, **_) -> Never:
    """
    Qt's 'QSSGLayerRenderData
    *QSSGRenderer::getOrCreateLayerRenderData(QSSGRenderLayer &layer)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.getOrCreateLayerRenderData' has no cute function "
        "yet. Qt's 'QSSGLayerRenderData "
        "*QSSGRenderer::getOrCreateLayerRenderData(QSSGRenderLayer "
        "&layer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def prepareLayerForRender(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderer::prepareLayerForRender(QSSGRenderLayer
    &inLayer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.prepareLayerForRender' has no cute function yet. "
        "Qt's 'bool QSSGRenderer::prepareLayerForRender(QSSGRenderLayer "
        "&inLayer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def registerItem2DData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::registerItem2DData(QSSGRenderItem2DData &data)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.registerItem2DData' has no cute function yet. Qt's "
        "'void QSSGRenderer::registerItem2DData(QSSGRenderItem2DData "
        "&data)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def releaseItem2DData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::releaseItem2DData(const QSSGRenderItem2D
    &item2D)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.releaseItem2DData' has no cute function yet. Qt's "
        "'void QSSGRenderer::releaseItem2DData(const QSSGRenderItem2D "
        "&item2D)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def rhiCubeRenderer(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGRhiCubeRenderer>
    &QSSGRenderer::rhiCubeRenderer() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.rhiCubeRenderer' has no cute function yet. Qt's "
        "'const std::unique_ptr<QSSGRhiCubeRenderer> "
        "&QSSGRenderer::rhiCubeRenderer() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def rhiPrepare(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::rhiPrepare(QSSGRenderLayer &inLayer)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.rhiPrepare' has no cute function yet. Qt's 'void "
        "QSSGRenderer::rhiPrepare(QSSGRenderLayer &inLayer)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def rhiQuadRenderer(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGRhiQuadRenderer>
    &QSSGRenderer::rhiQuadRenderer() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.rhiQuadRenderer' has no cute function yet. Qt's "
        "'const std::unique_ptr<QSSGRhiQuadRenderer> "
        "&QSSGRenderer::rhiQuadRenderer() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def rhiRender(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::rhiRender(QSSGRenderLayer &inLayer)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.rhiRender' has no cute function yet. Qt's 'void "
        "QSSGRenderer::rhiRender(QSSGRenderLayer &inLayer)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def unregisterItem2DData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderer::unregisterItem2DData(QSSGRenderItem2DData
    &data)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderer.unregisterItem2DData' has no cute function yet. Qt's "
        "'void QSSGRenderer::unregisterItem2DData(QSSGRenderItem2DData "
        "&data)': takes a type Python has no way to hand over yet.")
