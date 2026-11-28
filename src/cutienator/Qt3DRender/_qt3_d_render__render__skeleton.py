"""
Qt3DRender::Render::Skeleton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/skeleton_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Skeleton to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Skeleton(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Skeleton: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Skeleton.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Skeleton is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Skeleton that has a ritual and
  that Python can call so far, 18 names in all: 'setSkeletonManager',
  'skeletonManager', 'setJointManager', 'jointManager', 'cleanup',
  'syncFromFrontEnd', 'setStatus', 'status', 'source', 'dataType',
  'createJoints', 'setName', 'name', 'jointCount', 'rootJointId',
  'clearData', 'setSkeletonData', 'skeletonData'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVector<JointInfo> Qt3DRender::Render::Skeleton::joints() const':
    gives a type Python has no way to take yet.
  - Qt's 'QVector<QString> Qt3DRender::Render::Skeleton::jointNames() const':
    gives a type Python has no way to take yet.
  - Qt's 'QVector<Qt3DCore::Sqt> Qt3DRender::Render::Skeleton::localPoses()
    const': gives a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::Skeleton::setLocalPose(HJoint jointHandle,
    const Qt3DCore::Sqt &localPose)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QVector<QMatrix4x4>
    Qt3DRender::Render::Skeleton::calculateSkinningMatrixPalette()': gives a
    type Python has no way to take yet.
  - Qt's 'SkeletonData Qt3DRender::Render::Skeleton::skeletonData()': takes
    in Python what 'const SkeletonData
    &Qt3DRender::Render::Skeleton::skeletonData() const' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Skeleton is created at the first use, not by
    'Qt3DRender::Render::Skeleton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Skeleton.
  - Each name of Qt's Qt3DRender::Render::Skeleton that has no cute function
    yet, 'calculateSkinningMatrixPalette', 'jointNames', 'joints',
    'localPoses', 'setLocalPose', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::Skeleton, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SkeletonDataType(CuteNum):
    """
    The enum 'Qt3DRender::Render::Skeleton::SkeletonDataType' of Qt, with the
    3 names Qt gives in it.
    """

    Unknown = Kee[int](0)
    File = Kee[int](1)
    Data = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Skeleton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def skeletonManager(self) -> Optional[Qt3DRender.Render.SkeletonManager]:
    """
    Calls Qt's 'SkeletonManager
    *Qt3DRender::Render::Skeleton::skeletonManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#skeletonManager

    Returns
    -------

    Optional[Qt3DRender.Render.SkeletonManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SkeletonManager *Qt3DRender::Render::Skeleton::skeletonManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton15skeletonManagerEv',
    )
    return Qt3DRender.Render.SkeletonManager._cuteAt(address)

  def jointManager(self) -> Optional[Qt3DRender.Render.JointManager]:
    """
    Calls Qt's 'JointManager *Qt3DRender::Render::Skeleton::jointManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#jointManager

    Returns
    -------

    Optional[Qt3DRender.Render.JointManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  JointManager *Qt3DRender::Render::Skeleton::jointManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton12jointManagerEv',
    )
    return Qt3DRender.Render.JointManager._cuteAt(address)

  def status(self) -> Qt3DCore.QSkeletonLoader.Status:
    """
    Calls Qt's 'Qt3DCore::QSkeletonLoader::Status
    Qt3DRender::Render::Skeleton::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#status

    Returns
    -------

    Qt3DCore.QSkeletonLoader.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QSkeletonLoader.Status(number)' gives.
    """
    #  Qt3DCore::QSkeletonLoader::Status
    #      Qt3DRender::Render::Skeleton::status() const
    return Qt3DCore.QSkeletonLoader.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton6statusEv',
    ))

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::Render::Skeleton::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::Render::Skeleton::source() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def dataType(self) -> SkeletonDataType:
    """
    Calls Qt's 'SkeletonDataType Qt3DRender::Render::Skeleton::dataType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#dataType

    Returns
    -------

    SkeletonDataType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SkeletonDataType(number)'
      gives.
    """
    #  SkeletonDataType Qt3DRender::Render::Skeleton::dataType() const
    return Skeleton.SkeletonDataType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton8dataTypeEv',
    ))

  def createJoints(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Skeleton::createJoints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#createJoints
    """
    #  bool Qt3DRender::Render::Skeleton::createJoints() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton12createJointsEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::Skeleton::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::Skeleton::name() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton4nameEv',
    )

  def jointCount(self) -> int:
    """
    Calls Qt's 'qsizetype Qt3DRender::Render::Skeleton::jointCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#jointCount
    """
    #  qsizetype Qt3DRender::Render::Skeleton::jointCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton10jointCountEv',
    )

  def rootJointId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId Qt3DRender::Render::Skeleton::rootJointId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#rootJointId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::Skeleton::rootJointId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton11rootJointIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def skeletonData(self) -> Qt3DRender.Render.SkeletonData:
    """
    Calls Qt's 'const SkeletonData
    &Qt3DRender::Render::Skeleton::skeletonData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#skeletonData

    Returns
    -------

    Qt3DRender.Render.SkeletonData
      A new cute Qt3DRender::Render::SkeletonData around the copy Qt gave
      back. Python owns it.
    """
    #  const SkeletonData &Qt3DRender::Render::Skeleton::skeletonData() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render8Skeleton12skeletonDataEv',
    )
    return Qt3DRender.Render.SkeletonData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.SkeletonManager'])
  @overload(NoneType)
  def setSkeletonManager(
      self,
      skeletonManager: Optional[Qt3DRender.Render.SkeletonManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Skeleton::setSkeletonManager(SkeletonManager
    *skeletonManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#setSkeletonManager

    Parameters
    ----------

    skeletonManager : Optional[Qt3DRender.Render.SkeletonManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Skeleton::setSkeletonManager(SkeletonManager
    #      *skeletonManager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render8Skeleton18setSkeletonManagerEPNS0_15S'
        'keletonManagerE',
        self._addressOf(skeletonManager),
    )

  @overload(WAIT['Qt3DRender.Render.JointManager'])
  @overload(NoneType)
  def setJointManager(
      self,
      jointManager: Optional[Qt3DRender.Render.JointManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Skeleton::setJointManager(JointManager
    *jointManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#setJointManager

    Parameters
    ----------

    jointManager : Optional[Qt3DRender.Render.JointManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Skeleton::setJointManager(JointManager
    #      *jointManager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render8Skeleton15setJointManagerEPNS0_12Join'
        'tManagerE',
        self._addressOf(jointManager),
    )

  @overload(Qt3DCore.QSkeletonLoader.Status)
  def setStatus(self, status: Qt3DCore.QSkeletonLoader.Status) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Skeleton::setStatus(Qt3DCore::QSkeletonLoader::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#setStatus

    Parameters
    ----------

    status : Qt3DCore.QSkeletonLoader.Status
      Passed on as its number.
    """
    #  void Qt3DRender::Render::Skeleton::setStatus(Qt3DCore::
    #      QSkeletonLoader::Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render8Skeleton9setStatusEN8Qt3DCore15QSkele'
        'tonLoader6StatusE',
        status.value,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Skeleton::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::Render::Skeleton::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render8Skeleton7setNameERK7QString', name,
    )

  @overload(WAIT['Qt3DRender.Render.SkeletonData'])
  def setSkeletonData(self, data: Qt3DRender.Render.SkeletonData) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Skeleton::setSkeletonData(const
    SkeletonData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#setSkeletonData

    Parameters
    ----------

    data : Qt3DRender.Render.SkeletonData
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::SkeletonData, which stays Python's own.
    """
    #  void Qt3DRender::Render::Skeleton::setSkeletonData(const SkeletonData
    #      &data)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render8Skeleton15setSkeletonDataERKNS0_12Ske'
        'letonDataE',
        self._valueOf(data),
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
    'Qt3DRender::Render::Skeleton::Skeleton()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#Skeleton
    """
    #  Qt3DRender::Render::Skeleton::Skeleton()
    self._noteCreation(Skeleton, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render8SkeletonC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::Skeleton::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#cleanup
    """
    #  void Qt3DRender::Render::Skeleton::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render8Skeleton7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Skeleton::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Skeleton::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render8Skeleton16syncFromFrontEndEPKN8Qt3DCo'
        're5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render8Skeleton16syncFromFrontEndEPKN8'
          'Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def clearData(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Skeleton::clearData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-skeleton.html#clearData
    """
    #  void Qt3DRender::Render::Skeleton::clearData()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render8Skeleton9clearDataEv')

  @staticmethod
  def calculateSkinningMatrixPalette(*__, **_) -> Never:
    """
    Qt's 'QVector<QMatrix4x4>
    Qt3DRender::Render::Skeleton::calculateSkinningMatrixPalette()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Skeleton.calculateSkinningMatrixPalette' has no "
        "cute function yet. Qt's 'QVector<QMatrix4x4> "
        "Qt3DRender::Render::Skeleton::calculateSkinningMatrixPalette()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def jointNames(*__, **_) -> Never:
    """
    Qt's 'QVector<QString> Qt3DRender::Render::Skeleton::jointNames() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Skeleton.jointNames' has no cute function yet. "
        "Qt's 'QVector<QString> Qt3DRender::Render::Skeleton::jointNames() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def joints(*__, **_) -> Never:
    """
    Qt's 'QVector<JointInfo> Qt3DRender::Render::Skeleton::joints() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Skeleton.joints' has no cute function yet. Qt's "
        "'QVector<JointInfo> Qt3DRender::Render::Skeleton::joints() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def localPoses(*__, **_) -> Never:
    """
    Qt's 'QVector<Qt3DCore::Sqt> Qt3DRender::Render::Skeleton::localPoses()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Skeleton.localPoses' has no cute function yet. "
        "Qt's 'QVector<Qt3DCore::Sqt> "
        "Qt3DRender::Render::Skeleton::localPoses() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setLocalPose(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Skeleton::setLocalPose(HJoint jointHandle,
    const Qt3DCore::Sqt &localPose)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Skeleton.setLocalPose' has no cute function "
        "yet. Qt's 'void Qt3DRender::Render::Skeleton::setLocalPose(HJoint "
        "jointHandle, const Qt3DCore::Sqt &localPose)': takes a type Python "
        "has no way to hand over yet.")
