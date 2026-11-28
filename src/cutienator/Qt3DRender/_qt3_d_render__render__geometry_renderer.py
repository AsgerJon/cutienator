"""
Qt3DRender::Render::GeometryRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::GeometryRenderer to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GeometryRenderer(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::GeometryRenderer: a plain Python
  object standing in front of one C++ Qt3DRender::Render::GeometryRenderer.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::GeometryRenderer is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::GeometryRenderer that has a
  ritual and that Python can call so far, 19 names in all: 'cleanup',
  'setManager', 'syncFromFrontEnd', 'executeFunctor', 'geometryId',
  'instanceCount', 'vertexCount', 'indexOffset', 'firstInstance',
  'firstVertex', 'indexBufferByteOffset', 'restartIndexValue',
  'verticesPerPatch', 'primitiveRestartEnabled', 'primitiveType', 'isDirty',
  'unsetDirty', 'hasView', 'sortIndex'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::GeometryRenderer::~GeometryRenderer()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::GeometryRenderer.
  - Qt's 'Qt3DCore::QGeometryFactoryPtr
    Qt3DRender::Render::GeometryRenderer::geometryFactory() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::GeometryRenderer is created at the first use,
    not by 'Qt3DRender::Render::GeometryRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::GeometryRenderer.
  - Each name of Qt's Qt3DRender::Render::GeometryRenderer that has no cute
    function yet, 'geometryFactory', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::GeometryRenderer'

  #  A C++ Qt3DRender::Render::GeometryRenderer Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_GeometryRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def geometryId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::GeometryRenderer::geometryId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#geometryId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::GeometryRenderer::geometryId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer10geometryIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::instanceCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer13instanceCountEv',
    )

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::vertexCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::vertexCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer11vertexCountEv',
    )

  def indexOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::indexOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::indexOffset() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer11indexOffsetEv',
    )

  def firstInstance(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::firstInstance()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::firstInstance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer13firstInstanceEv',
    )

  def firstVertex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::firstVertex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::firstVertex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer11firstVertexEv',
    )

  def indexBufferByteOffset(self) -> int:
    """
    Calls Qt's 'int
    Qt3DRender::Render::GeometryRenderer::indexBufferByteOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::indexBufferByteOffset()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer21indexBufferByteOf'
        'fsetEv',
    )

  def restartIndexValue(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::restartIndexValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::restartIndexValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer17restartIndexValue'
        'Ev',
    )

  def verticesPerPatch(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::GeometryRenderer::verticesPerPatch()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  int Qt3DRender::Render::GeometryRenderer::verticesPerPatch() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer16verticesPerPatchE'
        'v',
    )

  def primitiveRestartEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::GeometryRenderer::primitiveRestartEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  bool Qt3DRender::Render::GeometryRenderer::primitiveRestartEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer23primitiveRestartE'
        'nabledEv',
    )

  def primitiveType(self) -> Qt3DRender.QGeometryRenderer.PrimitiveType:
    """
    Calls Qt's 'QGeometryRenderer::PrimitiveType
    Qt3DRender::Render::GeometryRenderer::primitiveType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html

    Returns
    -------

    Qt3DRender.QGeometryRenderer.PrimitiveType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QGeometryRenderer.PrimitiveType(number)' gives.
    """
    #  QGeometryRenderer::PrimitiveType
    #      Qt3DRender::Render::GeometryRenderer::primitiveType() const
    return Qt3DRender.QGeometryRenderer.PrimitiveType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer13primitiveTypeEv',
    ))

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::GeometryRenderer::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#isDirty
    """
    #  bool Qt3DRender::Render::GeometryRenderer::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer7isDirtyEv',
    )

  def hasView(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::GeometryRenderer::hasView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#hasView
    """
    #  bool Qt3DRender::Render::GeometryRenderer::hasView() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer7hasViewEv',
    )

  def sortIndex(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::GeometryRenderer::sortIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#sortIndex
    """
    #  float Qt3DRender::Render::GeometryRenderer::sortIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16GeometryRenderer9sortIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.GeometryRendererManager'])
  @overload(NoneType)
  def setManager(
      self,
      manager: Optional[Qt3DRender.Render.GeometryRendererManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::GeometryRenderer::setManager(GeometryRendererManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#setManager

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.GeometryRendererManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::GeometryRenderer::setManager(
    #      GeometryRendererManager *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16GeometryRenderer10setManagerEPNS0_23'
        'GeometryRendererManagerE',
        self._addressOf(manager),
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
    Notes what was given, for Qt's
    'Qt3DRender::Render::GeometryRenderer::GeometryRenderer()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html
    """
    #  Qt3DRender::Render::GeometryRenderer::GeometryRenderer()
    self._noteCreation(GeometryRenderer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render16GeometryRendererC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::GeometryRenderer::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#cleanup
    """
    #  void Qt3DRender::Render::GeometryRenderer::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16GeometryRenderer7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::GeometryRenderer::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::GeometryRenderer::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render16GeometryRenderer16syncFromFrontEndEP'
        'KN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render16GeometryRenderer16syncFromFron'
          'tEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def executeFunctor(self) -> Qt3DRender.Render.GeometryFunctorResult:
    """
    Calls Qt's 'GeometryFunctorResult
    Qt3DRender::Render::GeometryRenderer::executeFunctor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html

    Returns
    -------

    Qt3DRender.Render.GeometryFunctorResult
      A new cute Qt3DRender::Render::GeometryFunctorResult around the copy Qt
      gave back. Python owns it.
    """
    #  GeometryFunctorResult
    #      Qt3DRender::Render::GeometryRenderer::executeFunctor()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16GeometryRenderer14executeFunctorEv',
    )
    return Qt3DRender.Render.GeometryFunctorResult._cuteOwning(address)

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::GeometryRenderer::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-geometryrenderer.html#unsetDirty
    """
    #  void Qt3DRender::Render::GeometryRenderer::unsetDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16GeometryRenderer10unsetDirtyEv',
    )

  @staticmethod
  def geometryFactory(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QGeometryFactoryPtr
    Qt3DRender::Render::GeometryRenderer::geometryFactory() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.GeometryRenderer.geometryFactory' has no cute "
        "function yet. Qt's 'Qt3DCore::QGeometryFactoryPtr "
        "Qt3DRender::Render::GeometryRenderer::geometryFactory() const': "
        "gives a type Python has no way to take yet.")
