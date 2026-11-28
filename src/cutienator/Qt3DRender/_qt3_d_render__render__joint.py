"""
Qt3DRender::Render::Joint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/joint_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Joint to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Joint(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Joint: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Joint.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Joint is built on Qt's Qt3DRender::Render::BackendNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Joint that has a ritual and that
  Python can call so far, 12 names in all: 'cleanup', 'syncFromFrontEnd',
  'localPose', 'inverseBindMatrix', 'name', 'translation', 'rotation',
  'scale', 'setJointManager', 'jointManager', 'setSkeletonManager',
  'skeletonManager'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Qt3DCore::QNodeId> Qt3DRender::Render::Joint::childJointIds()
    const': gives a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::Joint::setOwningSkeleton(HSkeleton
    skeletonHandle)': takes a type Python has no way to hand over yet.
  - Qt's 'HSkeleton Qt3DRender::Render::Joint::owningSkeleton() const': gives
    a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Joint is created at the first use, not by
    'Qt3DRender::Render::Joint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Joint.
  - Each name of Qt's Qt3DRender::Render::Joint that has no cute function
    yet, 'childJointIds', 'owningSkeleton', 'setOwningSkeleton', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Joint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def localPose(self) -> Qt3DCore.Sqt:
    """
    Calls Qt's 'Qt3DCore::Sqt Qt3DRender::Render::Joint::localPose() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#localPose

    Returns
    -------

    Qt3DCore.Sqt
      A new cute Qt3DCore::Sqt around the copy Qt gave back. Python owns it.
    """
    #  Qt3DCore::Sqt Qt3DRender::Render::Joint::localPose() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint9localPoseEv',
    )
    return Qt3DCore.Sqt._cuteOwning(address)

  def inverseBindMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DRender::Render::Joint::inverseBindMatrix()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#inverseBindMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DRender::Render::Joint::inverseBindMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint17inverseBindMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::Joint::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-joint.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::Joint::name() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender6Render5Joint4nameEv')

  def translation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::Joint::translation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#translation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::Joint::translation() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint11translationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DRender::Render::Joint::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DRender::Render::Joint::rotation() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint8rotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def scale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::Joint::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-joint.html#scale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::Joint::scale() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint5scaleEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def jointManager(self) -> Optional[Qt3DRender.Render.JointManager]:
    """
    Calls Qt's 'JointManager *Qt3DRender::Render::Joint::jointManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#jointManager

    Returns
    -------

    Optional[Qt3DRender.Render.JointManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  JointManager *Qt3DRender::Render::Joint::jointManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint12jointManagerEv',
    )
    return Qt3DRender.Render.JointManager._cuteAt(address)

  def skeletonManager(self) -> Optional[Qt3DRender.Render.SkeletonManager]:
    """
    Calls Qt's 'SkeletonManager *Qt3DRender::Render::Joint::skeletonManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#skeletonManager

    Returns
    -------

    Optional[Qt3DRender.Render.SkeletonManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SkeletonManager *Qt3DRender::Render::Joint::skeletonManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render5Joint15skeletonManagerEv',
    )
    return Qt3DRender.Render.SkeletonManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.JointManager'])
  @overload(NoneType)
  def setJointManager(
      self,
      jointManager: Optional[Qt3DRender.Render.JointManager],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Joint::setJointManager(JointManager
    *jointManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#setJointManager

    Parameters
    ----------

    jointManager : Optional[Qt3DRender.Render.JointManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Joint::setJointManager(JointManager
    #      *jointManager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Joint15setJointManagerEPNS0_12JointMa'
        'nagerE',
        self._addressOf(jointManager),
    )

  @overload(WAIT['Qt3DRender.Render.SkeletonManager'])
  @overload(NoneType)
  def setSkeletonManager(
      self,
      skeletonManager: Optional[Qt3DRender.Render.SkeletonManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Joint::setSkeletonManager(SkeletonManager
    *skeletonManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#setSkeletonManager

    Parameters
    ----------

    skeletonManager : Optional[Qt3DRender.Render.SkeletonManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Joint::setSkeletonManager(SkeletonManager
    #      *skeletonManager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Joint18setSkeletonManagerEPNS0_15Skel'
        'etonManagerE',
        self._addressOf(skeletonManager),
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
    Notes what was given, for Qt's 'Qt3DRender::Render::Joint::Joint()',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-joint.html#Joint
    """
    #  Qt3DRender::Render::Joint::Joint()
    self._noteCreation(Joint, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render5JointC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::Joint::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#cleanup
    """
    #  void Qt3DRender::Render::Joint::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render5Joint7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Joint::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-joint.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Joint::syncFromFrontEnd(const Qt3DCore::QNode
    #      *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render5Joint16syncFromFrontEndEPKN8Qt3DCore5'
        'QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render5Joint16syncFromFrontEndEPKN8Qt3'
          'DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def childJointIds(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId> Qt3DRender::Render::Joint::childJointIds()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Joint.childJointIds' has no cute function yet. "
        "Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::Joint::childJointIds() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def owningSkeleton(*__, **_) -> Never:
    """
    Qt's 'HSkeleton Qt3DRender::Render::Joint::owningSkeleton() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Joint.owningSkeleton' has no cute function yet. "
        "Qt's 'HSkeleton Qt3DRender::Render::Joint::owningSkeleton() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setOwningSkeleton(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Joint::setOwningSkeleton(HSkeleton
    skeletonHandle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Joint.setOwningSkeleton' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::Render::Joint::setOwningSkeleton(HSkeleton "
        "skeletonHandle)': takes a type Python has no way to hand over yet.")
