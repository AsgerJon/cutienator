"""
Qt3DRender::Render::ShaderFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/shader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::ShaderFunctor to be private: it declares the
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


class ShaderFunctor(Qt3DCore.QBackendNodeMapper):
  """
  The cute side of Qt's Qt3DRender::Render::ShaderFunctor: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ShaderFunctor.

  It is built on the cute 'Qt3DCore::QBackendNodeMapper', as Qt's
  Qt3DRender::Render::ShaderFunctor is built on Qt's
  Qt3DCore::QBackendNodeMapper, and has everything that class has.

  C++ hands a Qt3DRender::Render::ShaderFunctor around as a copy, so every
  C++ Qt3DRender::Render::ShaderFunctor behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ShaderFunctor that has a ritual
  and that Python can call so far, 3 names in all: 'create', 'get',
  'destroy'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::ShaderFunctor::~ShaderFunctor()': the
    destructor: Python removes its C++ Qt3DRender::Render::ShaderFunctor by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ShaderFunctor is created at the first use,
    not by 'Qt3DRender::Render::ShaderFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::ShaderFunctor back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::ShaderFunctor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ShaderFunctor'

  #  Qt's '~Qt3DRender::Render::ShaderFunctor()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::ShaderFunctor
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render13ShaderFunctorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def create(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'Qt3DCore::QBackendNode
    *Qt3DRender::Render::ShaderFunctor::create(Qt3DCore::QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderfunctor.html#create

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QBackendNode
    #      *Qt3DRender::Render::ShaderFunctor::create(Qt3DCore::QNodeId id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderFunctor6createEN8Qt3DCore7QNo'
        'deIdE',
        self._valueOf(id),
    )
    return Qt3DCore.QBackendNode._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def get(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'Qt3DCore::QBackendNode
    *Qt3DRender::Render::ShaderFunctor::get(Qt3DCore::QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderfunctor.html#get

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QBackendNode
    #      *Qt3DRender::Render::ShaderFunctor::get(Qt3DCore::QNodeId id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderFunctor3getEN8Qt3DCore7QNodeI'
        'dE',
        self._valueOf(id),
    )
    return Qt3DCore.QBackendNode._cuteAt(address)

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

  @overload(
      WAIT['Qt3DRender.Render.AbstractRenderer'],
      WAIT['Qt3DRender.Render.ShaderManager'],
  )
  @overload(WAIT['Qt3DRender.Render.AbstractRenderer'], NoneType)
  @overload(NoneType, WAIT['Qt3DRender.Render.ShaderManager'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      renderer: Optional[Qt3DRender.Render.AbstractRenderer],
      manager: Optional[Qt3DRender.Render.ShaderManager],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::ShaderFunctor::ShaderFunctor(AbstractRenderer
    *renderer, ShaderManager *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderfunctor.html#ShaderFunctor

    Parameters
    ----------

    renderer : Optional[Qt3DRender.Render.AbstractRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    manager : Optional[Qt3DRender.Render.ShaderManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::ShaderFunctor::ShaderFunctor(AbstractRenderer
    #      *renderer, ShaderManager *manager)
    self._noteCreation(ShaderFunctor, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13ShaderFunctorC1EPNS0_16AbstractRende'
        'rerEPNS0_13ShaderManagerE',
        self._addressOf(renderer), self._addressOf(manager),
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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def destroy(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ShaderFunctor::destroy(Qt3DCore::QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-shaderfunctor.html#destroy

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::ShaderFunctor::destroy(Qt3DCore::QNodeId id)
    #      const
    self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13ShaderFunctor7destroyEN8Qt3DCore7QN'
        'odeIdE',
        self._valueOf(id),
    )
