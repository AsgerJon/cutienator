"""
RotationData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means RotationData to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']


class RotationData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's RotationData: a plain Python object standing in front
  of one C++ RotationData.

  C++ hands a RotationData around as a copy, so every C++ RotationData behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's RotationData that has a ritual and that Python can
  call so far, 6 names in all: '__eq__', '__ne__', 'toEulerAngles',
  'toQuaternion', 'dotProduct', 'fuzzyQuaternionCompare'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'RotationData &RotationData::operator=(const QVector3D &r)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'RotationData &RotationData::operator=(const QQuaternion &r)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'bool operator==(const QVector3D &eulerRotation, const RotationData
    &a)': takes in Python what 'bool operator==(const RotationData &a, const
    QVector3D &eulerRotation)' takes.
  - Qt's 'bool operator!=(const QVector3D &eulerRotation, const RotationData
    &a)': takes in Python what 'bool operator!=(const RotationData &a, const
    QVector3D &eulerRotation)' takes.
  - Qt's 'bool operator==(const QQuaternion &rotation, const RotationData
    &a)': takes in Python what 'bool operator==(const RotationData &a, const
    QQuaternion &rotation)' takes.
  - Qt's 'bool operator!=(const QQuaternion &rotation, const RotationData
    &a)': takes in Python what 'bool operator!=(const RotationData &a, const
    QQuaternion &rotation)' takes.
  - Qt's 'QMatrix3x3 RotationData::toRotationMatrix() const': gives a type
    Python has no way to take yet.
  - Qt's 'RotationData::~RotationData()': the destructor: Python removes its
    C++ RotationData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ RotationData is created at the first use, not by
    'RotationData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a RotationData back gives a copy the ritual made for
    Python, in a new cute RotationData.
  - Each name of Qt's RotationData that has no cute function yet,
    'toRotationMatrix', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuaternion, QQuaternion)
  def dotProduct(q1: QQuaternion, q2: QQuaternion) -> float:
    """
    Calls Qt's 'double RotationData::dotProduct(const QQuaternion &q1, const
    QQuaternion &q2)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#dotProduct

    Parameters
    ----------

    q1 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    q2 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  double RotationData::dotProduct(const QQuaternion &q1, const
    #      QQuaternion &q2)
    return Rituals.call(
        'ritual_ZN12RotationData10dotProductERK11QQuaternionS2_',
        CuteMixin._valueOf(q1), CuteMixin._valueOf(q2),
    )

  @staticmethod
  @overload(QQuaternion, QQuaternion)
  def fuzzyQuaternionCompare(a: QQuaternion, b: QQuaternion) -> bool:
    """
    Calls Qt's 'bool RotationData::fuzzyQuaternionCompare(const QQuaternion
    &a, const QQuaternion &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/rotationdata.html#fuzzyQuaternionCompare

    Parameters
    ----------

    a : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    b : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  bool RotationData::fuzzyQuaternionCompare(const QQuaternion &a, const
    #      QQuaternion &b)
    return Rituals.call(
        'ritual_ZN12RotationData22fuzzyQuaternionCompareERK11QQuaternionS2_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'RotationData'

  #  Qt's '~RotationData()'. Naming it makes this a value class: Python owns
  #  every C++ RotationData behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12RotationDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toEulerAngles(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D RotationData::toEulerAngles() const'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#toEulerAngles

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D RotationData::toEulerAngles() const
    address = self.uglySide.call('ritual_ZNK12RotationData13toEulerAnglesEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def toQuaternion(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion RotationData::toQuaternion() const'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#toQuaternion

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion RotationData::toQuaternion() const
    address = self.uglySide.call('ritual_ZNK12RotationData12toQuaternionEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: RotationData) -> bool:
    """
    Calls Qt's 'bool operator==(const RotationData &a, const RotationData
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#operator==

    Parameters
    ----------

    b : RotationData
      Passed on as a value: Qt reads the C++ RotationData, which stays
      Python's own.
    """
    #  bool operator==(const RotationData &a, const RotationData &b)
    return Rituals.call(
        'ritual_ZeqRK12RotationDataS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload(QVector3D)
  def __eq__(self, eulerRotation: QVector3D) -> bool:
    """
    Calls Qt's 'bool operator==(const RotationData &a, const QVector3D
    &eulerRotation)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#operator==

    Parameters
    ----------

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool operator==(const RotationData &a, const QVector3D &eulerRotation)
    return Rituals.call(
        'ritual_ZeqRK12RotationDataRK9QVector3D',
        CuteMixin._valueOf(self), CuteMixin._valueOf(eulerRotation),
    )

  @overload(QQuaternion)
  def __eq__(self, rotation: QQuaternion) -> bool:
    """
    Calls Qt's 'bool operator==(const RotationData &a, const QQuaternion
    &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#operator==

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  bool operator==(const RotationData &a, const QQuaternion &rotation)
    return Rituals.call(
        'ritual_ZeqRK12RotationDataRK11QQuaternion',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rotation),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, b: RotationData) -> bool:
    """
    Calls Qt's 'bool operator!=(const RotationData &a, const RotationData
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#operator!=

    Parameters
    ----------

    b : RotationData
      Passed on as a value: Qt reads the C++ RotationData, which stays
      Python's own.
    """
    #  bool operator!=(const RotationData &a, const RotationData &b)
    return Rituals.call(
        'ritual_ZneRK12RotationDataS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload(QVector3D)
  def __ne__(self, eulerRotation: QVector3D) -> bool:
    """
    Calls Qt's 'bool operator!=(const RotationData &a, const QVector3D
    &eulerRotation)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#operator!=

    Parameters
    ----------

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool operator!=(const RotationData &a, const QVector3D &eulerRotation)
    return Rituals.call(
        'ritual_ZneRK12RotationDataRK9QVector3D',
        CuteMixin._valueOf(self), CuteMixin._valueOf(eulerRotation),
    )

  @overload(QQuaternion)
  def __ne__(self, rotation: QQuaternion) -> bool:
    """
    Calls Qt's 'bool operator!=(const RotationData &a, const QQuaternion
    &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#operator!=

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  bool operator!=(const RotationData &a, const QQuaternion &rotation)
    return Rituals.call(
        'ritual_ZneRK12RotationDataRK11QQuaternion',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rotation),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'RotationData::RotationData()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#RotationData
    """
    #  RotationData::RotationData()
    self._noteCreation(RotationData, lambda: Rituals.call(
        'ritual_ZN12RotationDataC1Ev',
    ))

  @overload(QVector3D)
  def __init__(self, r: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'RotationData::RotationData(const
    QVector3D &r)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#RotationData

    Parameters
    ----------

    r : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  RotationData::RotationData(const QVector3D &r)
    self._noteCreation(RotationData, lambda: Rituals.call(
        'ritual_ZN12RotationDataC1ERK9QVector3D', self._valueOf(r),
    ))

  @overload(QQuaternion)
  def __init__(self, r: QQuaternion) -> None:
    """
    Notes what was given, for Qt's 'RotationData::RotationData(const
    QQuaternion &r)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/rotationdata.html#RotationData

    Parameters
    ----------

    r : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  RotationData::RotationData(const QQuaternion &r)
    self._noteCreation(RotationData, lambda: Rituals.call(
        'ritual_ZN12RotationDataC1ERK11QQuaternion', self._valueOf(r),
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

  @staticmethod
  def toRotationMatrix(*__, **_) -> Never:
    """
    Qt's 'QMatrix3x3 RotationData::toRotationMatrix() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'RotationData.toRotationMatrix' has no cute function yet. Qt's "
        "'QMatrix3x3 RotationData::toRotationMatrix() const': gives a type "
        "Python has no way to take yet.")
