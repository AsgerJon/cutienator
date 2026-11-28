"""
Qt3DAnimation::Animation::Skeleton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/skeleton_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::Skeleton to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Skeleton(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::Skeleton: a plain Python
  object standing in front of one C++ Qt3DAnimation::Animation::Skeleton.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::Skeleton is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::Skeleton that has a ritual
  and that Python can call so far, 10 names in all: 'cleanup',
  'syncFromFrontEnd', 'jointCount', 'jointName', 'setJointScale',
  'jointScale', 'setJointRotation', 'jointRotation', 'setJointTranslation',
  'jointTranslation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVector<Qt3DCore::Sqt> Qt3DAnimation::Animation::Skeleton::joints()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::Skeleton is created at the first use,
    not by 'Qt3DAnimation::Animation::Skeleton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::Skeleton.
  - Each name of Qt's Qt3DAnimation::Animation::Skeleton that has no cute
    function yet, 'joints', holds a function that raises
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
  __qt_class__ = 'Qt3DAnimation::Animation::Skeleton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def jointCount(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::Skeleton::jointCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html#jointCount
    """
    #  int Qt3DAnimation::Animation::Skeleton::jointCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation8Skeleton10jointCountEv',
    )

  @overload(int)
  def jointName(self, jointIndex: int) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::Animation::Skeleton::jointName(int
    jointIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html#jointName

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::Animation::Skeleton::jointName(int jointIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation8Skeleton9jointNameEi',
        jointIndex,
    )

  @overload(int)
  def jointScale(self, jointIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DAnimation::Animation::Skeleton::jointScale(int
    jointIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html#jointScale

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DAnimation::Animation::Skeleton::jointScale(int
    #      jointIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation8Skeleton10jointScaleEi',
        jointIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def jointRotation(self, jointIndex: int) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion
    Qt3DAnimation::Animation::Skeleton::jointRotation(int jointIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DAnimation::Animation::Skeleton::jointRotation(int
    #      jointIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation8Skeleton13jointRotationEi',
        jointIndex,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(int)
  def jointTranslation(self, jointIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DAnimation::Animation::Skeleton::jointTranslation(int jointIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DAnimation::Animation::Skeleton::jointTranslation(int
    #      jointIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation8Skeleton16jointTranslationEi',
        jointIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVector3D)
  def setJointScale(self, jointIndex: int, scale: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::Skeleton::setJointScale(int
    jointIndex, const QVector3D &scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DAnimation::Animation::Skeleton::setJointScale(int jointIndex,
    #      const QVector3D &scale)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation8Skeleton13setJointScaleEiRK9QVe'
        'ctor3D',
        jointIndex, self._valueOf(scale),
    )

  @overload(int, QQuaternion)
  def setJointRotation(self, jointIndex: int, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::Skeleton::setJointRotation(int
    jointIndex, const QQuaternion &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::Skeleton::setJointRotation(int
    #      jointIndex, const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation8Skeleton16setJointRotationEiRK1'
        '1QQuaternion',
        jointIndex, self._valueOf(rotation),
    )

  @overload(int, QVector3D)
  def setJointTranslation(
      self,
      jointIndex: int,
      translation: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::Skeleton::setJointTranslation(int jointIndex,
    const QVector3D &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html

    Parameters
    ----------

    jointIndex : int
      Passed on as it is.

    translation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DAnimation::Animation::Skeleton::setJointTranslation(int
    #      jointIndex, const QVector3D &translation)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation8Skeleton19setJointTranslationEi'
        'RK9QVector3D',
        jointIndex, self._valueOf(translation),
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
    'Qt3DAnimation::Animation::Skeleton::Skeleton()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html#Skeleton
    """
    #  Qt3DAnimation::Animation::Skeleton::Skeleton()
    self._noteCreation(Skeleton, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation8SkeletonC1Ev',
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
    Calls Qt's 'void Qt3DAnimation::Animation::Skeleton::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html#cleanup
    """
    #  void Qt3DAnimation::Animation::Skeleton::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation8Skeleton7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::Skeleton::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-skeleton.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::Skeleton::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation8Skeleton16syncFromFrontEndEPKN8'
        'Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation8Skeleton16syncFromFrontEn'
          'dEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def joints(*__, **_) -> Never:
    """
    Qt's 'QVector<Qt3DCore::Sqt> Qt3DAnimation::Animation::Skeleton::joints()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Skeleton.joints' has no cute function "
        "yet. Qt's 'QVector<Qt3DCore::Sqt> "
        "Qt3DAnimation::Animation::Skeleton::joints() const': gives a type "
        "Python has no way to take yet.")
