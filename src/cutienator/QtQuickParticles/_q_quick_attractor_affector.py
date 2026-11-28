"""
QQuickAttractorAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickpointattractor_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAttractorAffector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
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


class QQuickAttractorAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickAttractorAffector: a plain Python object
  standing in front of one C++ QQuickAttractorAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickAttractorAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAttractorAffector that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'strength',
  'pointX', 'pointY', 'affectedParameter', 'proportionalToDistance',
  'strengthChanged', 'pointXChanged', 'pointYChanged',
  'affectedParameterChanged', 'proportionalToDistanceChanged', 'setStrength',
  'setPointX', 'setPointY', 'setAffectedParameter',
  'setProportionalToDistance', 'affectParticle'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAttractorAffector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAttractorAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAttractorAffector is created at the first use, not by
    'QQuickAttractorAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAttractorAffector.
  - Qt tells when it has removed the C++ QQuickAttractorAffector. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickAttractorAffector, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AffectableParameters(CuteNum):
    """
    The enum 'QQuickAttractorAffector::AffectableParameters' of Qt, with the
    3 names Qt gives in it.
    """

    Position = Kee[int](0)
    Velocity = Kee[int](1)
    Acceleration = Kee[int](2)

  class Proportion(CuteNum):
    """
    The enum 'QQuickAttractorAffector::Proportion' of Qt, with the 5 names Qt
    gives in it.
    """

    Constant = Kee[int](0)
    Linear = Kee[int](1)
    Quadratic = Kee[int](2)
    InverseLinear = Kee[int](3)
    InverseQuadratic = Kee[int](4)

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
    Calls Qt's 'QString QQuickAttractorAffector::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickattractoraffector.html#tr

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
    #  QString QQuickAttractorAffector::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickAttractorAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAttractorAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAttractorAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAttractorAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickAttractorAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def strength(self) -> float:
    """
    Calls Qt's 'qreal QQuickAttractorAffector::strength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#strength
    """
    #  qreal QQuickAttractorAffector::strength() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickAttractorAffector8strengthEv',
    )

  def pointX(self) -> float:
    """
    Calls Qt's 'qreal QQuickAttractorAffector::pointX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#pointX
    """
    #  qreal QQuickAttractorAffector::pointX() const
    return self.uglySide.call('ritual_ZNK23QQuickAttractorAffector6pointXEv')

  def pointY(self) -> float:
    """
    Calls Qt's 'qreal QQuickAttractorAffector::pointY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#pointY
    """
    #  qreal QQuickAttractorAffector::pointY() const
    return self.uglySide.call('ritual_ZNK23QQuickAttractorAffector6pointYEv')

  def affectedParameter(self) -> AffectableParameters:
    """
    Calls Qt's 'AffectableParameters
    QQuickAttractorAffector::affectedParameter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#affectedParameter

    Returns
    -------

    AffectableParameters
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AffectableParameters(number)' gives.
    """
    #  AffectableParameters QQuickAttractorAffector::affectedParameter()
    #      const
    return QQuickAttractorAffector.AffectableParameters(self.uglySide.call(
        'ritual_ZNK23QQuickAttractorAffector17affectedParameterEv',
    ))

  def proportionalToDistance(self) -> Proportion:
    """
    Calls Qt's 'Proportion QQuickAttractorAffector::proportionalToDistance()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html

    Returns
    -------

    Proportion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Proportion(number)'
      gives.
    """
    #  Proportion QQuickAttractorAffector::proportionalToDistance() const
    return QQuickAttractorAffector.Proportion(self.uglySide.call(
        'ritual_ZNK23QQuickAttractorAffector22proportionalToDistanceEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStrength(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAttractorAffector::setStrength(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#setStrength

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAttractorAffector::setStrength(qreal arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector11setStrengthEd', arg,
    )

  @overload(float)
  def setPointX(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAttractorAffector::setPointX(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#setPointX

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAttractorAffector::setPointX(qreal arg)
    self.uglySide.call('ritual_ZN23QQuickAttractorAffector9setPointXEd', arg)

  @overload(float)
  def setPointY(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAttractorAffector::setPointY(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#setPointY

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAttractorAffector::setPointY(qreal arg)
    self.uglySide.call('ritual_ZN23QQuickAttractorAffector9setPointYEd', arg)

  @overload(AffectableParameters)
  def setAffectedParameter(self, arg: AffectableParameters) -> None:
    """
    Calls Qt's 'void
    QQuickAttractorAffector::setAffectedParameter(AffectableParameters arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#setAffectedParameter

    Parameters
    ----------

    arg : AffectableParameters
      Passed on as its number.
    """
    #  void
    #      QQuickAttractorAffector::setAffectedParameter(AffectableParameters
    #      arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector20setAffectedParameterENS_20Affe'
        'ctableParametersE',
        arg.value,
    )

  @overload(Proportion)
  def setProportionalToDistance(self, arg: Proportion) -> None:
    """
    Calls Qt's 'void
    QQuickAttractorAffector::setProportionalToDistance(Proportion arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html

    Parameters
    ----------

    arg : Proportion
      Passed on as its number.
    """
    #  void QQuickAttractorAffector::setProportionalToDistance(Proportion
    #      arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector25setProportionalToDistanceENS_1'
        '0ProportionE',
        arg.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAttractorAffector::QQuickAttractorAffector(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAttractorAffector::QQuickAttractorAffector(QQuickItem *parent)
    self._noteCreation(QQuickAttractorAffector, lambda: Rituals.call(
        'ritual_ZN23QQuickAttractorAffectorC1EP10QQuickItem',
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

  @overload(float)
  def strengthChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAttractorAffector::strengthChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#strengthChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAttractorAffector::strengthChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector15strengthChangedEd', arg,
    )

  @overload(float)
  def pointXChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAttractorAffector::pointXChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#pointXChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAttractorAffector::pointXChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector13pointXChangedEd', arg,
    )

  @overload(float)
  def pointYChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAttractorAffector::pointYChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#pointYChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAttractorAffector::pointYChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector13pointYChangedEd', arg,
    )

  @overload(AffectableParameters)
  def affectedParameterChanged(self, arg: AffectableParameters) -> None:
    """
    Calls Qt's 'void
    QQuickAttractorAffector::affectedParameterChanged(AffectableParameters
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html

    Parameters
    ----------

    arg : AffectableParameters
      Passed on as its number.
    """
    #  void QQuickAttractorAffector::affectedParameterChanged(
    #      AffectableParameters arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector24affectedParameterChangedENS_20'
        'AffectableParametersE',
        arg.value,
    )

  @overload(Proportion)
  def proportionalToDistanceChanged(self, arg: Proportion) -> None:
    """
    Calls Qt's 'void
    QQuickAttractorAffector::proportionalToDistanceChanged(Proportion arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html

    Parameters
    ----------

    arg : Proportion
      Passed on as its number.
    """
    #  void QQuickAttractorAffector::proportionalToDistanceChanged(Proportion
    #      arg)
    self.uglySide.call(
        'ritual_ZN23QQuickAttractorAffector29proportionalToDistanceChangedE'
        'NS_10ProportionE',
        arg.value,
    )

  @overload(QQuickParticleData, float)
  @overload(NoneType, float)
  def affectParticle(
      self,
      d: Optional[QQuickParticleData],
      dt: float,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickAttractorAffector::affectParticle(QQuickParticleData *d, qreal
    dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattractoraffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickAttractorAffector::affectParticle(QQuickParticleData *d,
    #      qreal dt)
    ritual = (
        'ritual_ZN23QQuickAttractorAffector14affectParticleEP18QQuickPartic'
        'leDatad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickAttractorAffector14affectParticleEP18QQuick'
          'ParticleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)
