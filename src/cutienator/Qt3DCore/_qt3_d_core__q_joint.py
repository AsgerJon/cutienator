"""
Qt3DCore::QJoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qjoint.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJoint(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QJoint: a plain Python object standing in
  front of one C++ Qt3DCore::QJoint.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QJoint is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QJoint that has a ritual and that Python
  can call so far, 30 names in all: 'metaObject', 'tr', 'scale', 'rotation',
  'translation', 'inverseBindMatrix', 'rotationX', 'rotationY', 'rotationZ',
  'name', 'addChildJoint', 'removeChildJoint', 'setScale', 'setRotation',
  'setTranslation', 'setInverseBindMatrix', 'setRotationX', 'setRotationY',
  'setRotationZ', 'setName', 'setToIdentity', 'scaleChanged',
  'rotationChanged', 'translationChanged', 'inverseBindMatrixChanged',
  'rotationXChanged', 'rotationYChanged', 'rotationZChanged', 'nameChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QJoint::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Qt3DCore::QJoint::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QJoint::~QJoint()': the destructor: Python never removes
    a C++ Qt3DCore::QJoint.
  - Qt's 'QList<QJoint *> Qt3DCore::QJoint::childJoints() const': gives a
    type Python has no way to take yet.
  - Qt's 'const QJointPrivate *Qt3DCore::QJoint::d_func() const': takes in
    Python what 'QJointPrivate *Qt3DCore::QJoint::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 38 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QJoint is created at the first use, not by
    'Qt3DCore::QJoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QJoint.
  - Qt tells when it has removed the C++ Qt3DCore::QJoint. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QJoint that has no cute function yet,
    'childJoints', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QJoint::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QJoint::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore6QJoint2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QJoint'

  #  A C++ Qt3DCore::QJoint Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QJoint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QJoint::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QJoint::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QJoint::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#scale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QJoint::scale() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint5scaleEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QJoint::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QJoint::rotation() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def translation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QJoint::translation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#translation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QJoint::translation() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint11translationEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def inverseBindMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DCore::QJoint::inverseBindMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#inverseBindMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::QJoint::inverseBindMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore6QJoint17inverseBindMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def rotationX(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QJoint::rotationX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationX
    """
    #  float Qt3DCore::QJoint::rotationX() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint9rotationXEv')

  def rotationY(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QJoint::rotationY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationY
    """
    #  float Qt3DCore::QJoint::rotationY() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint9rotationYEv')

  def rotationZ(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QJoint::rotationZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationZ
    """
    #  float Qt3DCore::QJoint::rotationZ() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint9rotationZEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QJoint::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QJoint::name() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore6QJoint4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setScale(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setScale(const QVector3D &scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setScale

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QJoint::setScale(const QVector3D &scale)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint8setScaleERK9QVector3D',
        self._valueOf(scale),
    )

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setRotation(const QQuaternion
    &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DCore::QJoint::setRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint11setRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def setTranslation(self, translation: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setTranslation(const QVector3D
    &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setTranslation

    Parameters
    ----------

    translation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QJoint::setTranslation(const QVector3D &translation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint14setTranslationERK9QVector3D',
        self._valueOf(translation),
    )

  @overload(QMatrix4x4)
  def setInverseBindMatrix(self, inverseBindMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setInverseBindMatrix(const QMatrix4x4
    &inverseBindMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setInverseBindMatrix

    Parameters
    ----------

    inverseBindMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DCore::QJoint::setInverseBindMatrix(const QMatrix4x4
    #      &inverseBindMatrix)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint20setInverseBindMatrixERK10QMatrix4x4',
        self._valueOf(inverseBindMatrix),
    )

  @overload(float)
  def setRotationX(self, rotationX: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setRotationX(float rotationX)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setRotationX

    Parameters
    ----------

    rotationX : float
      Passed on as it is.
    """
    #  void Qt3DCore::QJoint::setRotationX(float rotationX)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint12setRotationXEf', rotationX,
    )

  @overload(float)
  def setRotationY(self, rotationY: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setRotationY(float rotationY)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setRotationY

    Parameters
    ----------

    rotationY : float
      Passed on as it is.
    """
    #  void Qt3DCore::QJoint::setRotationY(float rotationY)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint12setRotationYEf', rotationY,
    )

  @overload(float)
  def setRotationZ(self, rotationZ: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setRotationZ(float rotationZ)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setRotationZ

    Parameters
    ----------

    rotationZ : float
      Passed on as it is.
    """
    #  void Qt3DCore::QJoint::setRotationZ(float rotationZ)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint12setRotationZEf', rotationZ,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QJoint::setName(const QString &name)
    self.uglySide.call('ritual_ZN8Qt3DCore6QJoint7setNameERK7QString', name)

  def setToIdentity(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::setToIdentity()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#setToIdentity
    """
    #  void Qt3DCore::QJoint::setToIdentity()
    self.uglySide.call('ritual_ZN8Qt3DCore6QJoint13setToIdentityEv')

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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QJoint::QJoint(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#QJoint

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QJoint::QJoint(Qt3DCore::QNode *parent)
    self._noteCreation(QJoint, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore6QJointC1EPNS_5QNodeE', self._addressOf(parent),
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

  @overload(THIS)
  @overload(NoneType)
  def addChildJoint(self, joint: Optional[QJoint]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::addChildJoint(QJoint *joint)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#addChildJoint

    Parameters
    ----------

    joint : Optional[QJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QJoint::addChildJoint(QJoint *joint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint13addChildJointEPS0_',
        self._addressOf(joint),
    )

  @overload(THIS)
  @overload(NoneType)
  def removeChildJoint(self, joint: Optional[QJoint]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::removeChildJoint(QJoint *joint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#removeChildJoint

    Parameters
    ----------

    joint : Optional[QJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QJoint::removeChildJoint(QJoint *joint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint16removeChildJointEPS0_',
        self._addressOf(joint),
    )

  @overload(QVector3D)
  def scaleChanged(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::scaleChanged(const QVector3D &scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#scaleChanged

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QJoint::scaleChanged(const QVector3D &scale)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint12scaleChangedERK9QVector3D',
        self._valueOf(scale),
    )

  @overload(QQuaternion)
  def rotationChanged(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::rotationChanged(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationChanged

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DCore::QJoint::rotationChanged(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint15rotationChangedERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def translationChanged(self, translation: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::translationChanged(const QVector3D
    &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#translationChanged

    Parameters
    ----------

    translation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QJoint::translationChanged(const QVector3D
    #      &translation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint18translationChangedERK9QVector3D',
        self._valueOf(translation),
    )

  @overload(QMatrix4x4)
  def inverseBindMatrixChanged(self, inverseBindMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::inverseBindMatrixChanged(const
    QMatrix4x4 &inverseBindMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#inverseBindMatrixChanged

    Parameters
    ----------

    inverseBindMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DCore::QJoint::inverseBindMatrixChanged(const QMatrix4x4
    #      &inverseBindMatrix)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint24inverseBindMatrixChangedERK10QMatrix4x4',
        self._valueOf(inverseBindMatrix),
    )

  @overload(float)
  def rotationXChanged(self, rotationX: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::rotationXChanged(float rotationX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationXChanged

    Parameters
    ----------

    rotationX : float
      Passed on as it is.
    """
    #  void Qt3DCore::QJoint::rotationXChanged(float rotationX)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint16rotationXChangedEf', rotationX,
    )

  @overload(float)
  def rotationYChanged(self, rotationY: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::rotationYChanged(float rotationY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationYChanged

    Parameters
    ----------

    rotationY : float
      Passed on as it is.
    """
    #  void Qt3DCore::QJoint::rotationYChanged(float rotationY)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint16rotationYChangedEf', rotationY,
    )

  @overload(float)
  def rotationZChanged(self, rotationZ: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::rotationZChanged(float rotationZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qjoint.html#rotationZChanged

    Parameters
    ----------

    rotationZ : float
      Passed on as it is.
    """
    #  void Qt3DCore::QJoint::rotationZChanged(float rotationZ)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint16rotationZChangedEf', rotationZ,
    )

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QJoint::nameChanged(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QJoint::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QJoint11nameChangedERK7QString', name,
    )

  def d_func(self) -> Optional[Qt3DCore.QJointPrivate]:
    """
    Calls Qt's 'QJointPrivate *Qt3DCore::QJoint::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qjoint.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QJointPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJointPrivate *Qt3DCore::QJoint::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore6QJoint6d_funcEv')
    return Qt3DCore.QJointPrivate._cuteAt(address)

  @staticmethod
  def childJoints(*__, **_) -> Never:
    """
    Qt's 'QList<QJoint *> Qt3DCore::QJoint::childJoints() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QJoint.childJoints' has no cute function yet. Qt's "
        "'QList<QJoint *> Qt3DCore::QJoint::childJoints() const': gives a "
        "type Python has no way to take yet.")
