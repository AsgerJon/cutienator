"""
QQuickRotation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRotation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRotation(QQuickTransform):
  """
  The cute side of Qt's QQuickRotation: a plain Python object standing in
  front of one C++ QQuickRotation.

  It is built on the cute 'QQuickTransform', as Qt's QQuickRotation is built
  on Qt's QQuickTransform, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRotation that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'origin', 'setOrigin',
  'angle', 'setAngle', 'axis', 'setAxis', 'distanceToPlane',
  'setDistanceToPlane', 'applyTo', 'originChanged', 'angleChanged',
  'axisChanged', 'distanceToPlaneChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRotation::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickRotation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRotationPrivate *QQuickRotation::d_func()': gives
    'QQuickRotationPrivate', which has no cute class yet.
  - Qt's 'const QQuickRotationPrivate *QQuickRotation::d_func() const': gives
    'QQuickRotationPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRotation is created at the first use, not by
    'QQuickRotation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRotation.
  - Qt tells when it has removed the C++ QQuickRotation. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickRotation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#tr

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
    #  QString QQuickRotation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickRotation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRotation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRotation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRotation::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickRotation10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickRotation::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickRotation::origin() const
    address = self.uglySide.call('ritual_ZNK14QQuickRotation6originEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickRotation::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#angle
    """
    #  qreal QQuickRotation::angle() const
    return self.uglySide.call('ritual_ZNK14QQuickRotation5angleEv')

  def axis(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickRotation::axis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#axis

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickRotation::axis() const
    address = self.uglySide.call('ritual_ZNK14QQuickRotation4axisEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def distanceToPlane(self) -> float:
    """
    Calls Qt's 'qreal QQuickRotation::distanceToPlane() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotation.html#distanceToPlane
    """
    #  qreal QQuickRotation::distanceToPlane() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickRotation15distanceToPlaneEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, point: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickRotation::setOrigin(const QVector3D &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#setOrigin

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickRotation::setOrigin(const QVector3D &point)
    self.uglySide.call(
        'ritual_ZN14QQuickRotation9setOriginERK9QVector3D',
        self._valueOf(point),
    )

  @overload(float)
  def setAngle(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickRotation::setAngle(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#setAngle

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickRotation::setAngle(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickRotation8setAngleEd', a0)

  @overload(QVector3D)
  def setAxis(self, axis: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickRotation::setAxis(const QVector3D &axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#setAxis

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickRotation::setAxis(const QVector3D &axis)
    self.uglySide.call(
        'ritual_ZN14QQuickRotation7setAxisERK9QVector3D',
        self._valueOf(axis),
    )

  @overload(Qt.Axis)
  def setAxis(self, axis: Qt.Axis) -> None:
    """
    Calls Qt's 'void QQuickRotation::setAxis(Qt::Axis axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#setAxis

    Parameters
    ----------

    axis : Qt.Axis
      Passed on as its number.
    """
    #  void QQuickRotation::setAxis(Qt::Axis axis)
    self.uglySide.call(
        'ritual_ZN14QQuickRotation7setAxisEN2Qt4AxisE', axis.value,
    )

  @overload(float)
  def setDistanceToPlane(self, newDistanceToPlane: float) -> None:
    """
    Calls Qt's 'void QQuickRotation::setDistanceToPlane(qreal
    newDistanceToPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotation.html#setDistanceToPlane

    Parameters
    ----------

    newDistanceToPlane : float
      Passed on as it is.
    """
    #  void QQuickRotation::setDistanceToPlane(qreal newDistanceToPlane)
    self.uglySide.call(
        'ritual_ZN14QQuickRotation18setDistanceToPlaneEd',
        newDistanceToPlane,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickRotation::QQuickRotation(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#QQuickRotation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRotation::QQuickRotation(QObject *parent)
    self._noteCreation(QQuickRotation, lambda: Rituals.call(
        'ritual_ZN14QQuickRotationC1EP7QObject',
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

  @overload(QMatrix4x4)
  @overload(NoneType)
  def applyTo(self, matrix: Optional[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QQuickRotation::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRotation::applyTo(QMatrix4x4 *matrix) const
    ritual = 'ritual_ZNK14QQuickRotation7applyToEP10QMatrix4x4'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickRotation7applyToEP10QMatrix4x4'
    self.uglySide.call(ritual, self._addressOf(matrix))

  def originChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRotation::originChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#originChanged
    """
    #  void QQuickRotation::originChanged()
    self.uglySide.call('ritual_ZN14QQuickRotation13originChangedEv')

  def angleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRotation::angleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#angleChanged
    """
    #  void QQuickRotation::angleChanged()
    self.uglySide.call('ritual_ZN14QQuickRotation12angleChangedEv')

  def axisChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRotation::axisChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotation.html#axisChanged
    """
    #  void QQuickRotation::axisChanged()
    self.uglySide.call('ritual_ZN14QQuickRotation11axisChangedEv')

  def distanceToPlaneChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRotation::distanceToPlaneChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotation.html#distanceToPlaneChanged
    """
    #  void QQuickRotation::distanceToPlaneChanged()
    self.uglySide.call('ritual_ZN14QQuickRotation22distanceToPlaneChangedEv')
