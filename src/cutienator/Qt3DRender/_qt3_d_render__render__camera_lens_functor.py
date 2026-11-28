"""
Qt3DRender::Render::CameraLensFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/cameralens_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::CameraLensFunctor to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class CameraLensFunctor(Qt3DCore.QBackendNodeMapper):
  """
  The cute side of Qt's Qt3DRender::Render::CameraLensFunctor: a plain Python
  object standing in front of one C++ Qt3DRender::Render::CameraLensFunctor.

  It is built on the cute 'Qt3DCore::QBackendNodeMapper', as Qt's
  Qt3DRender::Render::CameraLensFunctor is built on Qt's
  Qt3DCore::QBackendNodeMapper, and has everything that class has.

  C++ hands a Qt3DRender::Render::CameraLensFunctor around as a copy, so
  every C++ Qt3DRender::Render::CameraLensFunctor behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::CameraLensFunctor that has a
  ritual and that Python can call so far, 3 names in all: 'create', 'get',
  'destroy'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::CameraLensFunctor::~CameraLensFunctor()': the
    destructor: Python removes its C++ Qt3DRender::Render::CameraLensFunctor
    by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::CameraLensFunctor is created at the first
    use, not by 'Qt3DRender::Render::CameraLensFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::CameraLensFunctor back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::CameraLensFunctor.
  - Each name of Qt's Qt3DRender::Render::CameraLensFunctor that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::CameraLensFunctor'

  #  Qt's '~Qt3DRender::Render::CameraLensFunctor()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::CameraLensFunctor
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render17CameraLensFunctorD1Ev'

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
    *Qt3DRender::Render::CameraLensFunctor::create(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralensfunctor.html#create

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
    #      *Qt3DRender::Render::CameraLensFunctor::create(Qt3DCore::QNodeId
    #      id) const
    ritual = (
        'ritual_ZNK10Qt3DRender6Render17CameraLensFunctor6createEN8Qt3DCore'
        '7QNodeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10Qt3DRender6Render17CameraLensFunctor6createEN8Qt'
          '3DCore7QNodeIdE')
    address = self.uglySide.call(ritual, self._valueOf(id))
    return Qt3DCore.QBackendNode._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def get(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'Qt3DCore::QBackendNode
    *Qt3DRender::Render::CameraLensFunctor::get(Qt3DCore::QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralensfunctor.html#get

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
    #      *Qt3DRender::Render::CameraLensFunctor::get(Qt3DCore::QNodeId id)
    #      const
    ritual = (
        'ritual_ZNK10Qt3DRender6Render17CameraLensFunctor3getEN8Qt3DCore7QN'
        'odeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10Qt3DRender6Render17CameraLensFunctor3getEN8Qt3DC'
          'ore7QNodeIdE')
    address = self.uglySide.call(ritual, self._valueOf(id))
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::CameraLensFunctor::CameraLensFunctor(
    AbstractRenderer *renderer, QRenderAspect *renderAspect)': leans on
    'Qt3DRender::Render::CameraManager*
    Qt3DRender::Render::NodeManagers::manager<Qt3DRender::Render::CameraLens,
    Qt3DRender::Render::CameraManager>() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.CameraLensFunctor.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::Render::CameraLensFunctor::CameraLensFunctor(AbstractR"
        "enderer *renderer, QRenderAspect *renderAspect)': leans on "
        "'Qt3DRender::Render::CameraManager* "
        "Qt3DRender::Render::NodeManagers::manager<Qt3DRender::Render::Camer"
        "aLens, Qt3DRender::Render::CameraManager>() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Qt3DRender::Render::CameraLensFunctor::destroy(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralensfunctor.html#destroy

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::CameraLensFunctor::destroy(Qt3DCore::QNodeId
    #      id) const
    ritual = (
        'ritual_ZNK10Qt3DRender6Render17CameraLensFunctor7destroyEN8Qt3DCor'
        'e7QNodeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10Qt3DRender6Render17CameraLensFunctor7destroyEN8Q'
          't3DCore7QNodeIdE')
    self.uglySide.call(ritual, self._valueOf(id))
