"""
Qt3DRender::Render::MaterialParameterGathererJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/materialparametergathererjob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::MaterialParameterGathererJob to be private:
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MaterialParameterGathererJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::MaterialParameterGathererJob: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::MaterialParameterGathererJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::MaterialParameterGathererJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::MaterialParameterGathererJob
  that has a ritual and that Python can call so far, 6 names in all:
  'setNodeManagers', 'setTechniqueFilter', 'setRenderPassFilter',
  'techniqueFilter', 'renderPassFilter', 'run'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const MaterialParameterGathererData
    &Qt3DRender::Render::MaterialParameterGathererJob::
    materialToPassAndParameter()': gives a type Python has no way to take
    yet.
  - Qt's 'void
    Qt3DRender::Render::MaterialParameterGathererJob::setHandles(std::
    vector<HMaterial> &&handles)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    Qt3DRender::Render::MaterialParameterGathererJob::setHandles(const
    std::vector<HMaterial> &handles)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::MaterialParameterGathererJob is created at
    the first use, not by
    'Qt3DRender::Render::MaterialParameterGathererJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::MaterialParameterGathererJob.
  - Each name of Qt's Qt3DRender::Render::MaterialParameterGathererJob that
    has no cute function yet, 'materialToPassAndParameter', 'setHandles',
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
  __qt_class__ = 'Qt3DRender::Render::MaterialParameterGathererJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def techniqueFilter(self) -> Optional[Qt3DRender.Render.TechniqueFilter]:
    """
    Calls Qt's 'TechniqueFilter
    *Qt3DRender::Render::MaterialParameterGathererJob::techniqueFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html

    Returns
    -------

    Optional[Qt3DRender.Render.TechniqueFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TechniqueFilter *Qt3DRender::Render::MaterialParameterGathererJob::
    #      techniqueFilter() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render28MaterialParameterGathererJob15techn'
        'iqueFilterEv',
    )
    return Qt3DRender.Render.TechniqueFilter._cuteAt(address)

  def renderPassFilter(self) -> Optional[Qt3DRender.Render.RenderPassFilter]:
    """
    Calls Qt's 'RenderPassFilter
    *Qt3DRender::Render::MaterialParameterGathererJob::renderPassFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html

    Returns
    -------

    Optional[Qt3DRender.Render.RenderPassFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderPassFilter *Qt3DRender::Render::MaterialParameterGathererJob::
    #      renderPassFilter() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render28MaterialParameterGathererJob16rende'
        'rPassFilterEv',
    )
    return Qt3DRender.Render.RenderPassFilter._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::MaterialParameterGathererJob::setNodeManagers(
    NodeManagers *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DRender::Render::MaterialParameterGathererJob::setNodeManagers(
    #      NodeManagers *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob15setNod'
        'eManagersEPNS0_12NodeManagersE',
        self._addressOf(manager),
    )

  @overload(WAIT['Qt3DRender.Render.TechniqueFilter'])
  @overload(NoneType)
  def setTechniqueFilter(
      self,
      techniqueFilter: Optional[Qt3DRender.Render.TechniqueFilter],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::MaterialParameterGathererJob::setTechniqueFilter(
    TechniqueFilter *techniqueFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html

    Parameters
    ----------

    techniqueFilter : Optional[Qt3DRender.Render.TechniqueFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::MaterialParameterGathererJob::
    #      setTechniqueFilter(TechniqueFilter *techniqueFilter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob18setTec'
        'hniqueFilterEPNS0_15TechniqueFilterE',
        self._addressOf(techniqueFilter),
    )

  @overload(WAIT['Qt3DRender.Render.RenderPassFilter'])
  @overload(NoneType)
  def setRenderPassFilter(
      self,
      renderPassFilter: Optional[Qt3DRender.Render.RenderPassFilter],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::MaterialParameterGathererJob::setRenderPassFilter(
    RenderPassFilter *renderPassFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html

    Parameters
    ----------

    renderPassFilter : Optional[Qt3DRender.Render.RenderPassFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::MaterialParameterGathererJob::
    #      setRenderPassFilter(RenderPassFilter *renderPassFilter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob19setRen'
        'derPassFilterEPNS0_16RenderPassFilterE',
        self._addressOf(renderPassFilter),
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
    'Qt3DRender::Render::MaterialParameterGathererJob::
    MaterialParameterGathererJob()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html
    """
    #  Qt3DRender::Render::MaterialParameterGathererJob::
    #      MaterialParameterGathererJob()
    self._noteCreation(MaterialParameterGathererJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJobC1Ev',
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
    Qt3DRender::Render::MaterialParameterGathererJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-materialparametergathererjob.html
    """
    #  void Qt3DRender::Render::MaterialParameterGathererJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob3runEv',
    )

  @staticmethod
  def materialToPassAndParameter(*__, **_) -> Never:
    """
    Qt's 'const MaterialParameterGathererData
    &Qt3DRender::Render::MaterialParameterGathererJob::
    materialToPassAndParameter()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.MaterialParameterGathererJob.materialToPassAndPa"
        "rameter' has no cute function yet. Qt's 'const "
        "MaterialParameterGathererData "
        "&Qt3DRender::Render::MaterialParameterGathererJob::materialToPassAn"
        "dParameter()': gives a type Python has no way to take yet.")

  @staticmethod
  def setHandles(*__, **_) -> Never:
    """
    - Qt's 'void
      Qt3DRender::Render::MaterialParameterGathererJob::setHandles(std::
      vector<HMaterial> &&handles)': takes a type Python has no way to hand
      over yet.
    - Qt's 'void
      Qt3DRender::Render::MaterialParameterGathererJob::setHandles(const
      std::vector<HMaterial> &handles)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.MaterialParameterGathererJob.setHandles' has no "
        "cute function yet. Qt's 'void "
        "Qt3DRender::Render::MaterialParameterGathererJob::setHandles(std::v"
        "ector<HMaterial> &&handles)': takes a type Python has no way to "
        "hand over yet. Qt's 'void "
        "Qt3DRender::Render::MaterialParameterGathererJob::setHandles(const "
        "std::vector<HMaterial> &handles)': takes a type Python has no way "
        "to hand over yet.")
