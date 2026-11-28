"""
Qt3DRender::Render::LightGatherer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/lightgatherer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::LightGatherer to be private: it declares the
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


class LightGatherer(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::LightGatherer: a plain Python
  object standing in front of one C++ Qt3DRender::Render::LightGatherer.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::LightGatherer is built on Qt's Qt3DCore::QAspectJob,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::LightGatherer that has a ritual
  and that Python can call so far, 3 names in all: 'setManager',
  'environmentLight', 'run'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::vector<LightSource>
    &Qt3DRender::Render::LightGatherer::lights()': gives a type Python has no
    way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::LightGatherer is created at the first use,
    not by 'Qt3DRender::Render::LightGatherer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::LightGatherer.
  - Each name of Qt's Qt3DRender::Render::LightGatherer that has no cute
    function yet, 'lights', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::LightGatherer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def environmentLight(self) -> Optional[Qt3DRender.Render.EnvironmentLight]:
    """
    Calls Qt's 'EnvironmentLight
    *Qt3DRender::Render::LightGatherer::environmentLight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-lightgatherer.html

    Returns
    -------

    Optional[Qt3DRender.Render.EnvironmentLight]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EnvironmentLight
    #      *Qt3DRender::Render::LightGatherer::environmentLight() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13LightGatherer16environmentLightEv',
    )
    return Qt3DRender.Render.EnvironmentLight._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.EntityManager'])
  @overload(NoneType)
  def setManager(
      self,
      manager: Optional[Qt3DRender.Render.EntityManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::LightGatherer::setManager(EntityManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-lightgatherer.html#setManager

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.EntityManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::LightGatherer::setManager(EntityManager
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13LightGatherer10setManagerEPNS0_13Ent'
        'ityManagerE',
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
    'Qt3DRender::Render::LightGatherer::LightGatherer()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-lightgatherer.html#LightGatherer
    """
    #  Qt3DRender::Render::LightGatherer::LightGatherer()
    self._noteCreation(LightGatherer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13LightGathererC1Ev',
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::LightGatherer::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-lightgatherer.html#run
    """
    #  void Qt3DRender::Render::LightGatherer::run()
    ritual = 'ritual_ZN10Qt3DRender6Render13LightGatherer3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender6Render13LightGatherer3runEv'
    self.uglySide.call(ritual)

  @staticmethod
  def lights(*__, **_) -> Never:
    """
    Qt's 'std::vector<LightSource>
    &Qt3DRender::Render::LightGatherer::lights()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LightGatherer.lights' has no cute function yet. "
        "Qt's 'std::vector<LightSource> "
        "&Qt3DRender::Render::LightGatherer::lights()': gives a type Python "
        "has no way to take yet.")
