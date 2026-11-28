"""
QSSGPlane binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgplane_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGPlane to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QSSGPlane(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGPlane: a plain Python object standing in front of
  one C++ QSSGPlane.

  C++ hands a QSSGPlane around as a copy, so every C++ QSSGPlane behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGPlane that has a ritual and that Python can call
  so far, 5 names in all: 'distance', 'contains', 'project', 'pointInPlane',
  'normalize'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGPlane::~QSSGPlane()': the destructor: Python removes its C++
    QSSGPlane by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGPlane is created at the first use, not by 'QSSGPlane(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGPlane back gives a copy the ritual made for
    Python, in a new cute QSSGPlane.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGPlane'

  #  Qt's '~QSSGPlane()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGPlane behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSSGPlaneD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def distance(self, p: QVector3D) -> float:
    """
    Calls Qt's 'float QSSGPlane::distance(const QVector3D &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#distance

    Parameters
    ----------

    p : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QSSGPlane::distance(const QVector3D &p) const
    return self.uglySide.call(
        'ritual_ZNK9QSSGPlane8distanceERK9QVector3D', self._valueOf(p),
    )

  @overload(QVector3D)
  def contains(self, p: QVector3D) -> bool:
    """
    Calls Qt's 'bool QSSGPlane::contains(const QVector3D &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#contains

    Parameters
    ----------

    p : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QSSGPlane::contains(const QVector3D &p) const
    return self.uglySide.call(
        'ritual_ZNK9QSSGPlane8containsERK9QVector3D', self._valueOf(p),
    )

  @overload(QVector3D)
  def project(self, p: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGPlane::project(const QVector3D &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#project

    Parameters
    ----------

    p : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGPlane::project(const QVector3D &p) const
    address = self.uglySide.call(
        'ritual_ZNK9QSSGPlane7projectERK9QVector3D', self._valueOf(p),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def pointInPlane(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGPlane::pointInPlane() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#pointInPlane

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGPlane::pointInPlane() const
    address = self.uglySide.call('ritual_ZNK9QSSGPlane12pointInPlaneEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGPlane::QSSGPlane()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#QSSGPlane
    """
    #  QSSGPlane::QSSGPlane()
    self._noteCreation(QSSGPlane, lambda: Rituals.call(
        'ritual_ZN9QSSGPlaneC1Ev',
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      nx: float,
      ny: float,
      nz: float,
      distance: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSSGPlane::QSSGPlane(float nx, float ny,
    float nz, float distance)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#QSSGPlane

    Parameters
    ----------

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.

    nz : float
      Passed on as it is.

    distance : float
      Passed on as it is.
    """
    #  QSSGPlane::QSSGPlane(float nx, float ny, float nz, float distance)
    self._noteCreation(QSSGPlane, lambda: Rituals.call(
        'ritual_ZN9QSSGPlaneC1Effff', nx, ny, nz, distance,
    ))

  @overload(QVector3D, float)
  def __init__(self, normal: QVector3D, distance: float) -> None:
    """
    Notes what was given, for Qt's 'QSSGPlane::QSSGPlane(const QVector3D
    &normal, float distance)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#QSSGPlane

    Parameters
    ----------

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    distance : float
      Passed on as it is.
    """
    #  QSSGPlane::QSSGPlane(const QVector3D &normal, float distance)
    self._noteCreation(QSSGPlane, lambda: Rituals.call(
        'ritual_ZN9QSSGPlaneC1ERK9QVector3Df',
        self._valueOf(normal), distance,
    ))

  @overload(QVector3D, QVector3D)
  def __init__(self, point: QVector3D, normal: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QSSGPlane::QSSGPlane(const QVector3D
    &point, const QVector3D &normal)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#QSSGPlane

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QSSGPlane::QSSGPlane(const QVector3D &point, const QVector3D &normal)
    self._noteCreation(QSSGPlane, lambda: Rituals.call(
        'ritual_ZN9QSSGPlaneC1ERK9QVector3DS2_',
        self._valueOf(point), self._valueOf(normal),
    ))

  @overload(QVector3D, QVector3D, QVector3D)
  def __init__(self, p0: QVector3D, p1: QVector3D, p2: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QSSGPlane::QSSGPlane(const QVector3D &p0,
    const QVector3D &p1, const QVector3D &p2)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#QSSGPlane

    Parameters
    ----------

    p0 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    p1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    p2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QSSGPlane::QSSGPlane(const QVector3D &p0, const QVector3D &p1, const
    #      QVector3D &p2)
    self._noteCreation(QSSGPlane, lambda: Rituals.call(
        'ritual_ZN9QSSGPlaneC1ERK9QVector3DS2_S2_',
        self._valueOf(p0), self._valueOf(p1), self._valueOf(p2),
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

  def normalize(self) -> None:
    """
    Calls Qt's 'void QSSGPlane::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgplane.html#normalize
    """
    #  void QSSGPlane::normalize()
    self.uglySide.call('ritual_ZN9QSSGPlane9normalizeEv')
