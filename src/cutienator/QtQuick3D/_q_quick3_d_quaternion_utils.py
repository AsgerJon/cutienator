"""
QQuick3DQuaternionUtils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dquaternionutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DQuaternionUtils to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DQuaternionUtils(QObject):
  """
  The cute side of Qt's QQuick3DQuaternionUtils: a plain Python object
  standing in front of one C++ QQuick3DQuaternionUtils.

  It is built on the cute 'QObject', as Qt's QQuick3DQuaternionUtils is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DQuaternionUtils that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'fromAxesAndAngles', 'fromAxisAndAngle', 'fromEulerAngles', 'lookAt'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DQuaternionUtils::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DQuaternionUtils::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DQuaternionUtils::qt_qmlMarker_singleton()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DQuaternionUtils is created at the first use, not by
    'QQuick3DQuaternionUtils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DQuaternionUtils.
  - Qt tells when it has removed the C++ QQuick3DQuaternionUtils. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DQuaternionUtils::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dquaternionutils.html#tr

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
    #  QString QQuick3DQuaternionUtils::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QVector3D, float, QVector3D, float, QVector3D, float)
  def fromAxesAndAngles(
      axis1: QVector3D,
      angle1: float,
      axis2: QVector3D,
      angle2: float,
      axis3: QVector3D,
      angle3: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::fromAxesAndAngles(const
    QVector3D &axis1, float angle1, const QVector3D &axis2, float angle2,
    const QVector3D &axis3, float angle3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#fromAxesAndAngles

    Parameters
    ----------

    axis1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle1 : float
      Passed on as it is.

    axis2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle2 : float
      Passed on as it is.

    axis3 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle3 : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::fromAxesAndAngles(const QVector3D
    #      &axis1, float angle1, const QVector3D &axis2, float angle2, const
    #      QVector3D &axis3, float angle3)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils17fromAxesAndAnglesERK9QVector3D'
        'fS2_fS2_f',
        CuteMixin._valueOf(axis1), angle1, CuteMixin._valueOf(axis2), angle2,
        CuteMixin._valueOf(axis3), angle3,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, float, QVector3D, float)
  def fromAxesAndAngles(
      axis1: QVector3D,
      angle1: float,
      axis2: QVector3D,
      angle2: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::fromAxesAndAngles(const
    QVector3D &axis1, float angle1, const QVector3D &axis2, float angle2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#fromAxesAndAngles

    Parameters
    ----------

    axis1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle1 : float
      Passed on as it is.

    axis2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle2 : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::fromAxesAndAngles(const QVector3D
    #      &axis1, float angle1, const QVector3D &axis2, float angle2)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils17fromAxesAndAnglesERK9QVector3D'
        'fS2_f',
        CuteMixin._valueOf(axis1), angle1, CuteMixin._valueOf(axis2), angle2,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(float, float, float, float)
  def fromAxisAndAngle(
      x: float,
      y: float,
      z: float,
      angle: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::fromAxisAndAngle(float
    x, float y, float z, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#fromAxisAndAngle

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::fromAxisAndAngle(float x, float
    #      y, float z, float angle)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils16fromAxisAndAngleEffff',
        x, y, z, angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, float)
  def fromAxisAndAngle(axis: QVector3D, angle: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::fromAxisAndAngle(const
    QVector3D &axis, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#fromAxisAndAngle

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::fromAxisAndAngle(const QVector3D
    #      &axis, float angle)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils16fromAxisAndAngleERK9QVector3Df',
        CuteMixin._valueOf(axis), angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(float, float, float)
  def fromEulerAngles(x: float, y: float, z: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::fromEulerAngles(float x,
    float y, float z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#fromEulerAngles

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::fromEulerAngles(float x, float y,
    #      float z)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils15fromEulerAnglesEfff', x, y, z,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D)
  def fromEulerAngles(eulerAngles: QVector3D) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::fromEulerAngles(const
    QVector3D &eulerAngles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#fromEulerAngles

    Parameters
    ----------

    eulerAngles : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::fromEulerAngles(const QVector3D
    #      &eulerAngles)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils15fromEulerAnglesERK9QVector3D',
        CuteMixin._valueOf(eulerAngles),
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D)
  @overload(QVector3D, QVector3D, QVector3D)
  @overload(QVector3D, QVector3D, QVector3D, QVector3D)
  def lookAt(
      sourcePosition: QVector3D,
      targetPosition: QVector3D,
      forwardDirection: Optional[QVector3D] = None,
      upDirection: Optional[QVector3D] = None,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DQuaternionUtils::lookAt(const QVector3D
    &sourcePosition, const QVector3D &targetPosition, const QVector3D
    &forwardDirection, const QVector3D &upDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#lookAt

    Parameters
    ----------

    sourcePosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    targetPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    forwardDirection : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D(0, 0, -1)' is then
      passed on.

    upDirection : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D(0, 1, 0)' is then
      passed on.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DQuaternionUtils::lookAt(const QVector3D
    #      &sourcePosition, const QVector3D &targetPosition, const QVector3D
    #      &forwardDirection, const QVector3D &upDirection)
    if forwardDirection is None:
      from ..QtGui import QVector3D
      forwardDirection = QVector3D(0, 0, -1)
    if upDirection is None:
      from ..QtGui import QVector3D
      upDirection = QVector3D(0, 1, 0)
    address = Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtils6lookAtERK9QVector3DS2_S2_S2_',
        CuteMixin._valueOf(sourcePosition),
        CuteMixin._valueOf(targetPosition),
        CuteMixin._valueOf(forwardDirection),
        CuteMixin._valueOf(upDirection),
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DQuaternionUtils'

  #  A C++ QQuick3DQuaternionUtils Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DQuaternionUtils'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DQuaternionUtils::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DQuaternionUtils::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DQuaternionUtils10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DQuaternionUtils::QQuick3DQuaternionUtils(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dquaternionutils.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DQuaternionUtils::QQuick3DQuaternionUtils(QObject *parent)
    self._noteCreation(QQuick3DQuaternionUtils, lambda: Rituals.call(
        'ritual_ZN23QQuick3DQuaternionUtilsC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
