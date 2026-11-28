"""
QQuickGravityAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickgravity_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickGravityAffector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGravityAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickGravityAffector: a plain Python object standing
  in front of one C++ QQuickGravityAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickGravityAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGravityAffector that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'magnitude',
  'angle', 'affectParticle', 'magnitudeChanged', 'angleChanged',
  'setMagnitude', 'setAcceleration', 'setAngle'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGravityAffector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGravityAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGravityAffector is created at the first use, not by
    'QQuickGravityAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGravityAffector.
  - Qt tells when it has removed the C++ QQuickGravityAffector. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickGravityAffector::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgravityaffector.html#tr

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
    #  QString QQuickGravityAffector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickGravityAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGravityAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGravityAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGravityAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickGravityAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def magnitude(self) -> float:
    """
    Calls Qt's 'qreal QQuickGravityAffector::magnitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#magnitude
    """
    #  qreal QQuickGravityAffector::magnitude() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickGravityAffector9magnitudeEv',
    )

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickGravityAffector::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgravityaffector.html#angle
    """
    #  qreal QQuickGravityAffector::angle() const
    return self.uglySide.call('ritual_ZNK21QQuickGravityAffector5angleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMagnitude(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickGravityAffector::setMagnitude(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#setMagnitude

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickGravityAffector::setMagnitude(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickGravityAffector12setMagnitudeEd', arg,
    )

  @overload(float)
  def setAcceleration(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickGravityAffector::setAcceleration(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#setAcceleration

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickGravityAffector::setAcceleration(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickGravityAffector15setAccelerationEd', arg,
    )

  @overload(float)
  def setAngle(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickGravityAffector::setAngle(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#setAngle

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickGravityAffector::setAngle(qreal arg)
    self.uglySide.call('ritual_ZN21QQuickGravityAffector8setAngleEd', arg)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGravityAffector::QQuickGravityAffector(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#QQuickGravityAffector

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGravityAffector::QQuickGravityAffector(QQuickItem *parent)
    self._noteCreation(QQuickGravityAffector, lambda: Rituals.call(
        'ritual_ZN21QQuickGravityAffectorC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QQuickParticleData, float)
  @overload(NoneType, float)
  def affectParticle(
      self,
      d: Optional[QQuickParticleData],
      dt: float,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickGravityAffector::affectParticle(QQuickParticleData
    *d, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickGravityAffector::affectParticle(QQuickParticleData *d,
    #      qreal dt)
    ritual = (
        'ritual_ZN21QQuickGravityAffector14affectParticleEP18QQuickParticle'
        'Datad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickGravityAffector14affectParticleEP18QQuickPa'
          'rticleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(float)
  def magnitudeChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickGravityAffector::magnitudeChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#magnitudeChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickGravityAffector::magnitudeChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickGravityAffector16magnitudeChangedEd', arg,
    )

  @overload(float)
  def angleChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickGravityAffector::angleChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgravityaffector.html#angleChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickGravityAffector::angleChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickGravityAffector12angleChangedEd', arg,
    )
