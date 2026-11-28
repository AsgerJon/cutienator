"""
QQuick3DParticleGravity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlegravity_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleGravity to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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
  from ..QtGui import QVector3D
  from . import QQuick3DParticleData, QQuick3DParticleDataCurrent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QQuick3DParticleDataCurrent = WAIT['QQuick3DParticleDataCurrent']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleGravity(QQuick3DParticleAffector):
  """
  The cute side of Qt's QQuick3DParticleGravity: a plain Python object
  standing in front of one C++ QQuick3DParticleGravity.

  It is built on the cute 'QQuick3DParticleAffector', as Qt's
  QQuick3DParticleGravity is built on Qt's QQuick3DParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleGravity that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'magnitude',
  'direction', 'setDirection', 'setMagnitude', 'magnitudeChanged',
  'directionChanged', 'affectParticle'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleGravity::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DParticleGravity::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleGravity is created at the first use, not by
    'QQuick3DParticleGravity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleGravity.
  - Qt tells when it has removed the C++ QQuick3DParticleGravity. Every call
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
    Calls Qt's 'QString QQuick3DParticleGravity::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlegravity.html#tr

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
    #  QString QQuick3DParticleGravity::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuick3DParticleGravity2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleGravity'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleGravity::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleGravity::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleGravity10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def magnitude(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleGravity::magnitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#magnitude
    """
    #  float QQuick3DParticleGravity::magnitude() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleGravity9magnitudeEv',
    )

  def direction(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QQuick3DParticleGravity::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#direction

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QQuick3DParticleGravity::direction() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleGravity9directionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setDirection(self, direction: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleGravity::setDirection(const QVector3D
    &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#setDirection

    Parameters
    ----------

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleGravity::setDirection(const QVector3D &direction)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleGravity12setDirectionERK9QVector3D',
        self._valueOf(direction),
    )

  @overload(float)
  def setMagnitude(self, magnitude: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleGravity::setMagnitude(float magnitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#setMagnitude

    Parameters
    ----------

    magnitude : float
      Passed on as it is.
    """
    #  void QQuick3DParticleGravity::setMagnitude(float magnitude)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleGravity12setMagnitudeEf', magnitude,
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
    'QQuick3DParticleGravity::QQuick3DParticleGravity(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleGravity::QQuick3DParticleGravity(QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleGravity, lambda: Rituals.call(
        'ritual_ZN23QQuick3DParticleGravityC1EP12QQuick3DNode',
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

  def magnitudeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleGravity::magnitudeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#magnitudeChanged
    """
    #  void QQuick3DParticleGravity::magnitudeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleGravity16magnitudeChangedEv',
    )

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleGravity::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#directionChanged
    """
    #  void QQuick3DParticleGravity::directionChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleGravity16directionChangedEv',
    )

  @overload(QQuick3DParticleData, QQuick3DParticleDataCurrent, float)
  @overload(QQuick3DParticleData, NoneType, float)
  def affectParticle(
      self,
      sd: QQuick3DParticleData,
      d: Optional[QQuick3DParticleDataCurrent],
      time: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleGravity::affectParticle(const
    QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlegravity.html#affectParticle

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
    #  void QQuick3DParticleGravity::affectParticle(const
    #      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float
    #      time)
    ritual = (
        'ritual_ZN23QQuick3DParticleGravity14affectParticleERK20QQuick3DPar'
        'ticleDataP27QQuick3DParticleDataCurrentf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DParticleGravity14affectParticleERK20QQuic'
          'k3DParticleDataP27QQuick3DParticleDataCurrentf')
    self.uglySide.call(ritual, self._valueOf(sd), self._addressOf(d), time)
