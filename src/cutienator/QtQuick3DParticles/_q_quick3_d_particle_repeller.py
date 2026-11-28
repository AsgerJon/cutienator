"""
QQuick3DParticleRepeller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlerepeller_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleRepeller to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode
from . import QQuick3DParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuick3DParticleData, QQuick3DParticleDataCurrent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QQuick3DParticleDataCurrent = WAIT['QQuick3DParticleDataCurrent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleRepeller(QQuick3DParticleAffector):
  """
  The cute side of Qt's QQuick3DParticleRepeller: a plain Python object
  standing in front of one C++ QQuick3DParticleRepeller.

  It is built on the cute 'QQuick3DParticleAffector', as Qt's
  QQuick3DParticleRepeller is built on Qt's QQuick3DParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleRepeller that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'radius',
  'outerRadius', 'strength', 'setRadius', 'setOuterRadius', 'setStrength',
  'radiusChanged', 'outerRadiusChanged', 'strengthChanged',
  'prepareToAffect', 'affectParticle'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleRepeller::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleRepeller::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleRepeller is created at the first use, not by
    'QQuick3DParticleRepeller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleRepeller.
  - Qt tells when it has removed the C++ QQuick3DParticleRepeller. Every call
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
    Calls Qt's 'QString QQuick3DParticleRepeller::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#tr

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
    #  QString QQuick3DParticleRepeller::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuick3DParticleRepeller2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleRepeller'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleRepeller::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleRepeller::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleRepeller10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleRepeller::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#radius
    """
    #  float QQuick3DParticleRepeller::radius() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleRepeller6radiusEv',
    )

  def outerRadius(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleRepeller::outerRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#outerRadius
    """
    #  float QQuick3DParticleRepeller::outerRadius() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleRepeller11outerRadiusEv',
    )

  def strength(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleRepeller::strength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#strength
    """
    #  float QQuick3DParticleRepeller::strength() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleRepeller8strengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::setRadius(float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuick3DParticleRepeller::setRadius(float radius)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleRepeller9setRadiusEf', radius,
    )

  @overload(float)
  def setOuterRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::setOuterRadius(float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#setOuterRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuick3DParticleRepeller::setOuterRadius(float radius)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleRepeller14setOuterRadiusEf', radius,
    )

  @overload(float)
  def setStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::setStrength(float strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#setStrength

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void QQuick3DParticleRepeller::setStrength(float strength)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleRepeller11setStrengthEf', strength,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleRepeller::QQuick3DParticleRepeller(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleRepeller::QQuick3DParticleRepeller(QQuick3DNode
    #      *parent)
    self._noteCreation(QQuick3DParticleRepeller, lambda: Rituals.call(
        'ritual_ZN24QQuick3DParticleRepellerC1EP12QQuick3DNode',
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

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#radiusChanged
    """
    #  void QQuick3DParticleRepeller::radiusChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleRepeller13radiusChangedEv',
    )

  def outerRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::outerRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#outerRadiusChanged
    """
    #  void QQuick3DParticleRepeller::outerRadiusChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleRepeller18outerRadiusChangedEv',
    )

  def strengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::strengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#strengthChanged
    """
    #  void QQuick3DParticleRepeller::strengthChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleRepeller15strengthChangedEv',
    )

  def prepareToAffect(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::prepareToAffect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#prepareToAffect
    """
    #  void QQuick3DParticleRepeller::prepareToAffect()
    ritual = 'ritual_ZN24QQuick3DParticleRepeller15prepareToAffectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuick3DParticleRepeller15prepareToAffectEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleData, QQuick3DParticleDataCurrent, float)
  @overload(QQuick3DParticleData, NoneType, float)
  def affectParticle(
      self,
      sd: QQuick3DParticleData,
      d: Optional[QQuick3DParticleDataCurrent],
      time: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleRepeller::affectParticle(const
    QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlerepeller.html#affectParticle

    Parameters
    ----------

    sd : QQuick3DParticleData
      Passed on as a value: Qt reads the C++ QQuick3DParticleData, which
      stays Python's own.

    d : Optional[QQuick3DParticleDataCurrent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : float
      Passed on as it is.
    """
    #  void QQuick3DParticleRepeller::affectParticle(const
    #      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float
    #      time)
    ritual = (
        'ritual_ZN24QQuick3DParticleRepeller14affectParticleERK20QQuick3DPa'
        'rticleDataP27QQuick3DParticleDataCurrentf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuick3DParticleRepeller14affectParticleERK20QQui'
          'ck3DParticleDataP27QQuick3DParticleDataCurrentf')
    self.uglySide.call(ritual, self._valueOf(sd), self._addressOf(d), time)
