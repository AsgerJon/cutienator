"""
QGraphicsRotation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QGraphicsTransform

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


class QGraphicsRotation(QGraphicsTransform):
  """
  The cute side of Qt's QGraphicsRotation: a plain Python object standing in
  front of one C++ QGraphicsRotation.

  It is built on the cute 'QGraphicsTransform', as Qt's QGraphicsRotation is
  built on Qt's QGraphicsTransform, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsRotation that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'origin', 'setOrigin',
  'angle', 'setAngle', 'axis', 'setAxis', 'applyTo'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsRotation::~QGraphicsRotation()': the destructor: Python
    never removes a C++ QGraphicsRotation.

  What has no ritual
  ------------------

  9 of the 21 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 3 a signal; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QGraphicsRotation is created at the first use, not by
    'QGraphicsRotation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsRotation.
  - Qt tells when it has removed the C++ QGraphicsRotation. Every call on the
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
    Calls Qt's 'QString QGraphicsRotation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#tr

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
    #  QString QGraphicsRotation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QGraphicsRotation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsRotation'

  #  A C++ QGraphicsRotation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsRotation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsRotation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsRotation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGraphicsRotation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QGraphicsRotation::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QGraphicsRotation::origin() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsRotation6originEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsRotation::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#angle
    """
    #  qreal QGraphicsRotation::angle() const
    return self.uglySide.call('ritual_ZNK17QGraphicsRotation5angleEv')

  def axis(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QGraphicsRotation::axis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#axis

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QGraphicsRotation::axis() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsRotation4axisEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, point: QVector3D) -> None:
    """
    Calls Qt's 'void QGraphicsRotation::setOrigin(const QVector3D &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#setOrigin

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QGraphicsRotation::setOrigin(const QVector3D &point)
    self.uglySide.call(
        'ritual_ZN17QGraphicsRotation9setOriginERK9QVector3D',
        self._valueOf(point),
    )

  @overload(float)
  def setAngle(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsRotation::setAngle(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#setAngle

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsRotation::setAngle(qreal a0)
    self.uglySide.call('ritual_ZN17QGraphicsRotation8setAngleEd', a0)

  @overload(QVector3D)
  def setAxis(self, axis: QVector3D) -> None:
    """
    Calls Qt's 'void QGraphicsRotation::setAxis(const QVector3D &axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#setAxis

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QGraphicsRotation::setAxis(const QVector3D &axis)
    self.uglySide.call(
        'ritual_ZN17QGraphicsRotation7setAxisERK9QVector3D',
        self._valueOf(axis),
    )

  @overload(Qt.Axis)
  def setAxis(self, axis: Qt.Axis) -> None:
    """
    Calls Qt's 'void QGraphicsRotation::setAxis(Qt::Axis axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#setAxis

    Parameters
    ----------

    axis : Qt.Axis
      Passed on as its number.
    """
    #  void QGraphicsRotation::setAxis(Qt::Axis axis)
    self.uglySide.call(
        'ritual_ZN17QGraphicsRotation7setAxisEN2Qt4AxisE', axis.value,
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
    Notes what was given, for Qt's
    'QGraphicsRotation::QGraphicsRotation(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsrotation.html#QGraphicsRotation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsRotation::QGraphicsRotation(QObject *parent)
    self._noteCreation(QGraphicsRotation, lambda: Rituals.call(
        'ritual_ZN17QGraphicsRotationC1EP7QObject', self._addressOf(parent),
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
    Calls Qt's 'void QGraphicsRotation::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrotation.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsRotation::applyTo(QMatrix4x4 *matrix) const
    ritual = 'ritual_ZNK17QGraphicsRotation7applyToEP10QMatrix4x4'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRotation7applyToEP10QMatrix4x4'
    self.uglySide.call(ritual, self._addressOf(matrix))
