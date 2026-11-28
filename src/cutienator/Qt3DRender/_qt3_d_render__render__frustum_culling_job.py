"""
Qt3DRender::Render::FrustumCullingJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/frustumcullingjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FrustumCullingJob to be private: it declares
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

  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FrustumCullingJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::FrustumCullingJob: a plain Python
  object standing in front of one C++ Qt3DRender::Render::FrustumCullingJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::FrustumCullingJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FrustumCullingJob that has a
  ritual and that Python can call so far, 8 names in all: 'setRoot',
  'setManagers', 'setActive', 'isActive', 'setViewProjection',
  'viewProjection', 'isRequired', 'run'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::FrustumCullingJob::~FrustumCullingJob()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::FrustumCullingJob.
  - Qt's 'void *Qt3DRender::Render::FrustumCullingJob::operator new(size_t
    s)': an operator Python has no name for.
  - Qt's 'void Qt3DRender::Render::FrustumCullingJob::operator delete(void
    *ptr)': an operator Python has no name for.
  - Qt's 'const std::vector<Entity *>
    &Qt3DRender::Render::FrustumCullingJob::visibleEntities() const': gives a
    type Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::FrustumCullingJob::cullScene(Entity *e,
    const Plane *planes)': names
    'Qt3DRender::Render::FrustumCullingJob::Plane', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FrustumCullingJob is created at the first
    use, not by 'Qt3DRender::Render::FrustumCullingJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::FrustumCullingJob.
  - Each name of Qt's Qt3DRender::Render::FrustumCullingJob that has no cute
    function yet, 'cullScene', 'visibleEntities', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FrustumCullingJob'

  #  A C++ Qt3DRender::Render::FrustumCullingJob Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_FrustumCullingJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::FrustumCullingJob::isActive()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html#isActive
    """
    #  bool Qt3DRender::Render::FrustumCullingJob::isActive() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render17FrustumCullingJob8isActiveEv',
    )

  def viewProjection(self) -> QMatrix4x4:
    """
    Calls Qt's 'Matrix4x4
    Qt3DRender::Render::FrustumCullingJob::viewProjection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  Matrix4x4 Qt3DRender::Render::FrustumCullingJob::viewProjection()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render17FrustumCullingJob14viewProjectionEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def setRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::FrustumCullingJob::setRoot(Entity
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html#setRoot

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrustumCullingJob::setRoot(Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrustumCullingJob7setRootEPNS0_6Enti'
        'tyE',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrustumCullingJob::setManagers(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrustumCullingJob::setManagers(NodeManagers
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrustumCullingJob11setManagersEPNS0_'
        '12NodeManagersE',
        self._addressOf(manager),
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::FrustumCullingJob::setActive(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::FrustumCullingJob::setActive(bool active)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrustumCullingJob9setActiveEb',
        active,
    )

  @overload(QMatrix4x4)
  def setViewProjection(self, viewProjection: QMatrix4x4) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrustumCullingJob::setViewProjection(const Matrix4x4
    &viewProjection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html

    Parameters
    ----------

    viewProjection : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::FrustumCullingJob::setViewProjection(const
    #      Matrix4x4 &viewProjection)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrustumCullingJob17setViewProjection'
        'ERK10QMatrix4x4',
        self._valueOf(viewProjection),
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
    'Qt3DRender::Render::FrustumCullingJob::FrustumCullingJob()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html
    """
    #  Qt3DRender::Render::FrustumCullingJob::FrustumCullingJob()
    self._noteCreation(FrustumCullingJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render17FrustumCullingJobC1Ev',
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

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::FrustumCullingJob::isRequired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html
    """
    #  bool Qt3DRender::Render::FrustumCullingJob::isRequired()
    ritual = 'ritual_ZN10Qt3DRender6Render17FrustumCullingJob10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render17FrustumCullingJob10isRequiredE'
          'v')
    return self.uglySide.call(ritual)

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::FrustumCullingJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-frustumcullingjob.html#run
    """
    #  void Qt3DRender::Render::FrustumCullingJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrustumCullingJob3runEv',
    )

  @staticmethod
  def cullScene(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::FrustumCullingJob::cullScene(Entity *e,
    const Plane *planes)': names
    'Qt3DRender::Render::FrustumCullingJob::Plane', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FrustumCullingJob.cullScene' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::FrustumCullingJob::cullScene(Entity *e, const "
        "Plane *planes)': names "
        "'Qt3DRender::Render::FrustumCullingJob::Plane', which has no cute "
        "class yet.")

  @staticmethod
  def visibleEntities(*__, **_) -> Never:
    """
    Qt's 'const std::vector<Entity *>
    &Qt3DRender::Render::FrustumCullingJob::visibleEntities() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FrustumCullingJob.visibleEntities' has no cute "
        "function yet. Qt's 'const std::vector<Entity *> "
        "&Qt3DRender::Render::FrustumCullingJob::visibleEntities() const': "
        "gives a type Python has no way to take yet.")
