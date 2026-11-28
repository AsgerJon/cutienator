"""
Qt3DRender::Render::FilterCompatibleTechniqueJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/filtercompatibletechniquejob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FilterCompatibleTechniqueJob to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
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


class FilterCompatibleTechniqueJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::FilterCompatibleTechniqueJob: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::FilterCompatibleTechniqueJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::FilterCompatibleTechniqueJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FilterCompatibleTechniqueJob
  that has a ritual and that Python can call so far, 5 names in all:
  'setManager', 'manager', 'setRenderer', 'renderer', 'run'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FilterCompatibleTechniqueJob is created at
    the first use, not by
    'Qt3DRender::Render::FilterCompatibleTechniqueJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::FilterCompatibleTechniqueJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FilterCompatibleTechniqueJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def manager(self) -> Optional[Qt3DRender.Render.TechniqueManager]:
    """
    Calls Qt's 'TechniqueManager
    *Qt3DRender::Render::FilterCompatibleTechniqueJob::manager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filtercompatibletechniquejob.html

    Returns
    -------

    Optional[Qt3DRender.Render.TechniqueManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TechniqueManager
    #      *Qt3DRender::Render::FilterCompatibleTechniqueJob::manager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render28FilterCompatibleTechniqueJob7manage'
        'rEv',
    )
    return Qt3DRender.Render.TechniqueManager._cuteAt(address)

  def renderer(self) -> Optional[Qt3DRender.Render.AbstractRenderer]:
    """
    Calls Qt's 'AbstractRenderer
    *Qt3DRender::Render::FilterCompatibleTechniqueJob::renderer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filtercompatibletechniquejob.html

    Returns
    -------

    Optional[Qt3DRender.Render.AbstractRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractRenderer
    #      *Qt3DRender::Render::FilterCompatibleTechniqueJob::renderer()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render28FilterCompatibleTechniqueJob8render'
        'erEv',
    )
    return Qt3DRender.Render.AbstractRenderer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.TechniqueManager'])
  @overload(NoneType)
  def setManager(
      self,
      managers: Optional[Qt3DRender.Render.TechniqueManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FilterCompatibleTechniqueJob::setManager(
    TechniqueManager *managers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filtercompatibletechniquejob.html

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.TechniqueManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FilterCompatibleTechniqueJob::setManager(
    #      TechniqueManager *managers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob10setMan'
        'agerEPNS0_16TechniqueManagerE',
        self._addressOf(managers),
    )

  @overload(WAIT['Qt3DRender.Render.AbstractRenderer'])
  @overload(NoneType)
  def setRenderer(
      self,
      renderer: Optional[Qt3DRender.Render.AbstractRenderer],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FilterCompatibleTechniqueJob::setRenderer(
    AbstractRenderer *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filtercompatibletechniquejob.html

    Parameters
    ----------

    renderer : Optional[Qt3DRender.Render.AbstractRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FilterCompatibleTechniqueJob::setRenderer(
    #      AbstractRenderer *renderer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob11setRen'
        'dererEPNS0_16AbstractRendererE',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::FilterCompatibleTechniqueJob::
    FilterCompatibleTechniqueJob()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filtercompatibletechniquejob.html
    """
    #  Qt3DRender::Render::FilterCompatibleTechniqueJob::
    #      FilterCompatibleTechniqueJob()
    self._noteCreation(FilterCompatibleTechniqueJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJobC1Ev',
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
    Calls Qt's 'void
    Qt3DRender::Render::FilterCompatibleTechniqueJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filtercompatibletechniquejob.html
    """
    #  void Qt3DRender::Render::FilterCompatibleTechniqueJob::run()
    ritual = (
        'ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob3runEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob3r'
          'unEv')
    self.uglySide.call(ritual)
