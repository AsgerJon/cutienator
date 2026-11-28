"""
Qt3DRender::Render::BackendNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/backendnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::BackendNode to be private: it declares the
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BackendNode(Qt3DCore.QBackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::BackendNode: a plain Python
  object standing in front of one C++ Qt3DRender::Render::BackendNode.

  It is built on the cute 'Qt3DCore::QBackendNode', as Qt's
  Qt3DRender::Render::BackendNode is built on Qt's Qt3DCore::QBackendNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::BackendNode that has a ritual
  and that Python can call so far, 4 names in all: 'syncFromFrontEnd',
  'setRenderer', 'renderer', 'markDirty'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::BackendNode::~BackendNode()': the destructor:
    Python never removes a C++ Qt3DRender::Render::BackendNode.
  - Qt's 'QSharedPointer<RenderBackendResourceAccessor>
    Qt3DRender::Render::BackendNode::resourceAccessor() const': gives a type
    Python has no way to take yet.
  - Qt's 'Qt3DRender::Render::BackendNode::BackendNode(Qt3DCore::
    QBackendNodePrivate &dd)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::BackendNode is created at the first use, not
    by 'Qt3DRender::Render::BackendNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::BackendNode.
  - Each name of Qt's Qt3DRender::Render::BackendNode that has no cute
    function yet, 'resourceAccessor', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::BackendNode'

  #  A C++ Qt3DRender::Render::BackendNode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_BackendNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def renderer(self) -> Optional[Qt3DRender.Render.AbstractRenderer]:
    """
    Calls Qt's 'AbstractRenderer *Qt3DRender::Render::BackendNode::renderer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-backendnode.html#renderer

    Returns
    -------

    Optional[Qt3DRender.Render.AbstractRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractRenderer *Qt3DRender::Render::BackendNode::renderer() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render11BackendNode8rendererEv',
    )
    return Qt3DRender.Render.AbstractRenderer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.AbstractRenderer'])
  @overload(NoneType)
  def setRenderer(
      self,
      renderer: Optional[Qt3DRender.Render.AbstractRenderer],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::BackendNode::setRenderer(AbstractRenderer
    *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-backendnode.html#setRenderer

    Parameters
    ----------

    renderer : Optional[Qt3DRender.Render.AbstractRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::BackendNode::setRenderer(AbstractRenderer
    #      *renderer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render11BackendNode11setRendererEPNS0_16Abst'
        'ractRendererE',
        self._addressOf(renderer),
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
  @overload(Qt3DCore.QBackendNode.Mode)
  def __init__(
      self,
      mode: Qt3DCore.QBackendNode.Mode = Qt3DCore.QBackendNode.Mode.ReadOnly,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::BackendNode::BackendNode(Qt3DCore::QBackendNode::
    Mode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-backendnode.html#BackendNode

    Parameters
    ----------

    mode : Qt3DCore.QBackendNode.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt3DCore.QBackendNode.Mode.ReadOnly.
    """
    #  Qt3DRender::Render::BackendNode::BackendNode(Qt3DCore::
    #      QBackendNode::Mode mode)
    self._noteCreation(BackendNode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render11BackendNodeC1EN8Qt3DCore12QBackendNo'
        'de4ModeE',
        mode.value,
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::BackendNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-backendnode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::BackendNode::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render11BackendNode16syncFromFrontEndEPKN8Qt'
        '3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render11BackendNode16syncFromFrontEndE'
          'PKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(Qt3DRender.Render.AbstractRenderer.BackendNodeDirtySet)
  def markDirty(
      self,
      changes: Qt3DRender.Render.AbstractRenderer.BackendNodeDirtySet,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::BackendNode::markDirty(AbstractRenderer::
    BackendNodeDirtySet changes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-backendnode.html#markDirty

    Parameters
    ----------

    changes : Qt3DRender.Render.AbstractRenderer.BackendNodeDirtySet
      Passed on as its number.
    """
    #  void Qt3DRender::Render::BackendNode::markDirty(AbstractRenderer::
    #      BackendNodeDirtySet changes)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render11BackendNode9markDirtyE6QFlagsINS0_16'
        'AbstractRenderer20BackendNodeDirtyFlagEE',
        changes.value,
    )

  @staticmethod
  def resourceAccessor(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<RenderBackendResourceAccessor>
    Qt3DRender::Render::BackendNode::resourceAccessor() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.BackendNode.resourceAccessor' has no cute "
        "function yet. Qt's 'QSharedPointer<RenderBackendResourceAccessor> "
        "Qt3DRender::Render::BackendNode::resourceAccessor() const': gives "
        "a type Python has no way to take yet.")
