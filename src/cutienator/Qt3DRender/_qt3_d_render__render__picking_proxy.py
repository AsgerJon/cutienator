"""
Qt3DRender::Render::PickingProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickingproxy_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::PickingProxy to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PickingProxy(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::PickingProxy: a plain Python
  object standing in front of one C++ Qt3DRender::Render::PickingProxy.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::PickingProxy is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::PickingProxy that has a ritual
  and that Python can call so far, 17 names in all: 'cleanup', 'setManager',
  'syncFromFrontEnd', 'geometryId', 'instanceCount', 'vertexCount',
  'indexOffset', 'firstInstance', 'firstVertex', 'indexBufferByteOffset',
  'restartIndexValue', 'verticesPerPatch', 'primitiveRestartEnabled',
  'primitiveType', 'isValid', 'isDirty', 'unsetDirty'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::PickingProxy::~PickingProxy()': the destructor:
    Python never removes a C++ Qt3DRender::Render::PickingProxy.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PickingProxy is created at the first use, not
    by 'Qt3DRender::Render::PickingProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::PickingProxy.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::PickingProxy'

  #  A C++ Qt3DRender::Render::PickingProxy Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_PickingProxy'

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
    Qt3DRender::Render::PickingProxy::geometryId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#geometryId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::PickingProxy::geometryId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy10geometryIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::instanceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#instanceCount
    """
    #  int Qt3DRender::Render::PickingProxy::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy13instanceCountEv',
    )

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::vertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#vertexCount
    """
    #  int Qt3DRender::Render::PickingProxy::vertexCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy11vertexCountEv',
    )

  def indexOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::indexOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#indexOffset
    """
    #  int Qt3DRender::Render::PickingProxy::indexOffset() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy11indexOffsetEv',
    )

  def firstInstance(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::firstInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#firstInstance
    """
    #  int Qt3DRender::Render::PickingProxy::firstInstance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy13firstInstanceEv',
    )

  def firstVertex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::firstVertex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#firstVertex
    """
    #  int Qt3DRender::Render::PickingProxy::firstVertex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy11firstVertexEv',
    )

  def indexBufferByteOffset(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::indexBufferByteOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html
    """
    #  int Qt3DRender::Render::PickingProxy::indexBufferByteOffset() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy21indexBufferByteOffset'
        'Ev',
    )

  def restartIndexValue(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::restartIndexValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html
    """
    #  int Qt3DRender::Render::PickingProxy::restartIndexValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy17restartIndexValueEv',
    )

  def verticesPerPatch(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::PickingProxy::verticesPerPatch()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html
    """
    #  int Qt3DRender::Render::PickingProxy::verticesPerPatch() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy16verticesPerPatchEv',
    )

  def primitiveRestartEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::PickingProxy::primitiveRestartEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html
    """
    #  bool Qt3DRender::Render::PickingProxy::primitiveRestartEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy23primitiveRestartEnabl'
        'edEv',
    )

  def primitiveType(self) -> Qt3DCore.QGeometryView.PrimitiveType:
    """
    Calls Qt's 'Qt3DCore::QGeometryView::PrimitiveType
    Qt3DRender::Render::PickingProxy::primitiveType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#primitiveType

    Returns
    -------

    Qt3DCore.QGeometryView.PrimitiveType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QGeometryView.PrimitiveType(number)' gives.
    """
    #  Qt3DCore::QGeometryView::PrimitiveType
    #      Qt3DRender::Render::PickingProxy::primitiveType() const
    return Qt3DCore.QGeometryView.PrimitiveType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy13primitiveTypeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::PickingProxy::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#isValid
    """
    #  bool Qt3DRender::Render::PickingProxy::isValid() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy7isValidEv',
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::PickingProxy::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#isDirty
    """
    #  bool Qt3DRender::Render::PickingProxy::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingProxy7isDirtyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.PickingProxyManager'])
  @overload(NoneType)
  def setManager(
      self,
      manager: Optional[Qt3DRender.Render.PickingProxyManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PickingProxy::setManager(PickingProxyManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#setManager

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.PickingProxyManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::PickingProxy::setManager(PickingProxyManager
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12PickingProxy10setManagerEPNS0_19Pick'
        'ingProxyManagerE',
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
    'Qt3DRender::Render::PickingProxy::PickingProxy()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#PickingProxy
    """
    #  Qt3DRender::Render::PickingProxy::PickingProxy()
    self._noteCreation(PickingProxy, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12PickingProxyC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::PickingProxy::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#cleanup
    """
    #  void Qt3DRender::Render::PickingProxy::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12PickingProxy7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::PickingProxy::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::PickingProxy::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render12PickingProxy16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render12PickingProxy16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def unsetDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::PickingProxy::unsetDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingproxy.html#unsetDirty
    """
    #  void Qt3DRender::Render::PickingProxy::unsetDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12PickingProxy10unsetDirtyEv',
    )
