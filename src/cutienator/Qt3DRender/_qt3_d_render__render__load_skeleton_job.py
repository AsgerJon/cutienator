"""
Qt3DRender::Render::LoadSkeletonJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/loadskeletonjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::LoadSkeletonJob to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
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


class LoadSkeletonJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::LoadSkeletonJob: a plain Python
  object standing in front of one C++ Qt3DRender::Render::LoadSkeletonJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::LoadSkeletonJob is built on Qt's Qt3DCore::QAspectJob,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::LoadSkeletonJob that has a
  ritual and that Python can call so far, 5 names in all: 'setNodeManagers',
  'run', 'loadSkeletonFromData', 'createFrontendJoints',
  'createFrontendJoint'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DRender::Render::LoadSkeletonJob::processJointHierarchy(Qt3DCore::
    QNodeId jointId, int parentJointIndex, SkeletonData &skeletonData)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here; 2 leans on 'Qt3DRender; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::LoadSkeletonJob is created at the first use,
    not by 'Qt3DRender::Render::LoadSkeletonJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::LoadSkeletonJob.
  - Each name of Qt's Qt3DRender::Render::LoadSkeletonJob that has no cute
    function yet, '__init__', 'loadSkeleton', 'loadSkeletonFromUrl',
    'processJointHierarchy', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::LoadSkeletonJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.SkeletonData'])
  def createFrontendJoints(
      self,
      skeletonData: Qt3DRender.Render.SkeletonData,
  ) -> Optional[Qt3DCore.QJoint]:
    """
    Calls Qt's 'Qt3DCore::QJoint
    *Qt3DRender::Render::LoadSkeletonJob::createFrontendJoints(const
    SkeletonData &skeletonData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadskeletonjob.html

    Parameters
    ----------

    skeletonData : Qt3DRender.Render.SkeletonData
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::SkeletonData, which stays Python's own.

    Returns
    -------

    Optional[Qt3DCore.QJoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QJoint
    #      *Qt3DRender::Render::LoadSkeletonJob::createFrontendJoints(const
    #      SkeletonData &skeletonData) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15LoadSkeletonJob20createFrontendJoin'
        'tsERKNS0_12SkeletonDataE',
        self._valueOf(skeletonData),
    )
    return Qt3DCore.QJoint._cuteAt(address)

  @overload(str, WAIT['Qt3DCore.Sqt'], QMatrix4x4)
  def createFrontendJoint(
      self,
      jointName: str,
      localPose: Qt3DCore.Sqt,
      inverseBindMatrix: QMatrix4x4,
  ) -> Optional[Qt3DCore.QJoint]:
    """
    Calls Qt's 'Qt3DCore::QJoint
    *Qt3DRender::Render::LoadSkeletonJob::createFrontendJoint(const QString
    &jointName, const Qt3DCore::Sqt &localPose, const QMatrix4x4
    &inverseBindMatrix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadskeletonjob.html

    Parameters
    ----------

    jointName : str
      Passed on as it is: a QString is made of it for the call.

    localPose : Qt3DCore.Sqt
      Passed on as a value: Qt reads the C++ Qt3DCore::Sqt, which stays
      Python's own.

    inverseBindMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    Optional[Qt3DCore.QJoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QJoint
    #      *Qt3DRender::Render::LoadSkeletonJob::createFrontendJoint(const
    #      QString &jointName, const Qt3DCore::Sqt &localPose, const
    #      QMatrix4x4 &inverseBindMatrix) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15LoadSkeletonJob19createFrontendJoin'
        'tERK7QStringRKN8Qt3DCore3SqtERK10QMatrix4x4',
        jointName, self._valueOf(localPose),
        self._valueOf(inverseBindMatrix),
    )
    return Qt3DCore.QJoint._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManagers(
      self,
      nodeManagers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::LoadSkeletonJob::setNodeManagers(NodeManagers
    *nodeManagers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadskeletonjob.html

    Parameters
    ----------

    nodeManagers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::LoadSkeletonJob::setNodeManagers(NodeManagers
    #      *nodeManagers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render15LoadSkeletonJob15setNodeManagersEPNS'
        '0_12NodeManagersE',
        self._addressOf(nodeManagers),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::LoadSkeletonJob::LoadSkeletonJob(const
    HSkeleton &handle)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSkeletonJob.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DRender::Render::LoadSkeletonJob::LoadSkeletonJob(const "
        "HSkeleton &handle)': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void Qt3DRender::Render::LoadSkeletonJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadskeletonjob.html#run
    """
    #  void Qt3DRender::Render::LoadSkeletonJob::run()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render15LoadSkeletonJob3runEv')

  @overload(WAIT['Qt3DRender.Render.Skeleton'])
  @overload(NoneType)
  def loadSkeletonFromData(
      self,
      skeleton: Optional[Qt3DRender.Render.Skeleton],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::LoadSkeletonJob::loadSkeletonFromData(Skeleton
    *skeleton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadskeletonjob.html

    Parameters
    ----------

    skeleton : Optional[Qt3DRender.Render.Skeleton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DRender::Render::LoadSkeletonJob::loadSkeletonFromData(Skeleton
    #      *skeleton)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render15LoadSkeletonJob20loadSkeletonFromDat'
        'aEPNS0_8SkeletonE',
        self._addressOf(skeleton),
    )

  @staticmethod
  def loadSkeleton(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::LoadSkeletonJob::loadSkeleton(Skeleton
    *skeleton)': leans on
    'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSkeletonJob.loadSkeleton' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::LoadSkeletonJob::loadSkeleton(Skeleton "
        "*skeleton)': leans on "
        "'Qt3DRender::Render::GLTFSkeletonLoader::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadSkeletonFromUrl(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::LoadSkeletonJob::loadSkeletonFromUrl(Skeleton
    *skeleton)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'LoadSkeletonJobPrivate'.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSkeletonJob.loadSkeletonFromUrl' has no "
        "cute function yet. Qt's 'void "
        "Qt3DRender::Render::LoadSkeletonJob::loadSkeletonFromUrl(Skeleton "
        "*skeleton)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'LoadSkeletonJobPrivate'.")

  @staticmethod
  def processJointHierarchy(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::LoadSkeletonJob::processJointHierarchy(Qt3DCore::
    QNodeId jointId, int parentJointIndex, SkeletonData &skeletonData)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSkeletonJob.processJointHierarchy' has no "
        "cute function yet. Qt's 'void "
        "Qt3DRender::Render::LoadSkeletonJob::processJointHierarchy(Qt3DCore"
        "::QNodeId jointId, int parentJointIndex, SkeletonData "
        "&skeletonData)': takes a type Python has no way to hand over yet.")
