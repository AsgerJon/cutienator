"""
QQuick3DParticleScaleAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlescaleaffector_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleScaleAffector to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode
from . import QQuick3DParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEasingCurve, QMetaObject
  from . import QQuick3DParticleData, QQuick3DParticleDataCurrent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QQuick3DParticleDataCurrent = WAIT['QQuick3DParticleDataCurrent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleScaleAffector(QQuick3DParticleAffector):
  """
  The cute side of Qt's QQuick3DParticleScaleAffector: a plain Python object
  standing in front of one C++ QQuick3DParticleScaleAffector.

  It is built on the cute 'QQuick3DParticleAffector', as Qt's
  QQuick3DParticleScaleAffector is built on Qt's QQuick3DParticleAffector,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleScaleAffector that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject', 'tr',
  'minSize', 'maxSize', 'duration', 'type', 'easingCurve', 'setMinSize',
  'setMaxSize', 'setDuration', 'setType', 'setEasingCurve', 'minSizeChanged',
  'maxSizeChanged', 'durationChanged', 'typeChanged', 'easingCurveChanged',
  'prepareToAffect', 'affectParticle'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleScaleAffector::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleScaleAffector::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleScaleAffector is created at the first use, not by
    'QQuick3DParticleScaleAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleScaleAffector.
  - Qt tells when it has removed the C++ QQuick3DParticleScaleAffector. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DParticleScaleAffector, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class ScalingType(CuteNum):
    """
    The enum 'QQuick3DParticleScaleAffector::ScalingType' of Qt, with the 6
    names Qt gives in it.
    """

    Linear = Kee[int](0)
    SewSaw = Kee[int](1)
    SineWave = Kee[int](2)
    AbsSineWave = Kee[int](3)
    Step = Kee[int](4)
    SmoothStep = Kee[int](5)

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
    Calls Qt's 'QString QQuick3DParticleScaleAffector::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#tr

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
    #  QString QQuick3DParticleScaleAffector::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuick3DParticleScaleAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleScaleAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DParticleScaleAffector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleScaleAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleScaleAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minSize(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleScaleAffector::minSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#minSize
    """
    #  float QQuick3DParticleScaleAffector::minSize() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleScaleAffector7minSizeEv',
    )

  def maxSize(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleScaleAffector::maxSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#maxSize
    """
    #  float QQuick3DParticleScaleAffector::maxSize() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleScaleAffector7maxSizeEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleScaleAffector::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#duration
    """
    #  int QQuick3DParticleScaleAffector::duration() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleScaleAffector8durationEv',
    )

  def type(self) -> ScalingType:
    """
    Calls Qt's 'ScalingType QQuick3DParticleScaleAffector::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#type

    Returns
    -------

    ScalingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ScalingType(number)'
      gives.
    """
    #  ScalingType QQuick3DParticleScaleAffector::type() const
    return QQuick3DParticleScaleAffector.ScalingType(self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleScaleAffector4typeEv',
    ))

  def easingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuick3DParticleScaleAffector::easingCurve()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#easingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuick3DParticleScaleAffector::easingCurve() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleScaleAffector11easingCurveEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMinSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::setMinSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#setMinSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuick3DParticleScaleAffector::setMinSize(float size)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector10setMinSizeEf', size,
    )

  @overload(float)
  def setMaxSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::setMaxSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#setMaxSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuick3DParticleScaleAffector::setMaxSize(float size)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector10setMaxSizeEf', size,
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::setDuration(int
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleScaleAffector::setDuration(int duration)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector11setDurationEi', duration,
    )

  @overload(ScalingType)
  def setType(self, type: ScalingType) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::setType(ScalingType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#setType

    Parameters
    ----------

    type : ScalingType
      Passed on as its number.
    """
    #  void QQuick3DParticleScaleAffector::setType(ScalingType type)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector7setTypeENS_11ScalingTypeE',
        type.value,
    )

  @overload(QEasingCurve)
  def setEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::setEasingCurve(const
    QEasingCurve &curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#setEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuick3DParticleScaleAffector::setEasingCurve(const QEasingCurve
    #      &curve)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector14setEasingCurveERK12QEasi'
        'ngCurve',
        self._valueOf(curve),
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
    'QQuick3DParticleScaleAffector::QQuick3DParticleScaleAffector(
    QQuick3DNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleScaleAffector::QQuick3DParticleScaleAffector(
    #      QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleScaleAffector, lambda: Rituals.call(
        'ritual_ZN29QQuick3DParticleScaleAffectorC1EP12QQuick3DNode',
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

  def minSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::minSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#minSizeChanged
    """
    #  void QQuick3DParticleScaleAffector::minSizeChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector14minSizeChangedEv',
    )

  def maxSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::maxSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#maxSizeChanged
    """
    #  void QQuick3DParticleScaleAffector::maxSizeChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector14maxSizeChangedEv',
    )

  def durationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::durationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#durationChanged
    """
    #  void QQuick3DParticleScaleAffector::durationChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector15durationChangedEv',
    )

  def typeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::typeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#typeChanged
    """
    #  void QQuick3DParticleScaleAffector::typeChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector11typeChangedEv',
    )

  def easingCurveChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::easingCurveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html
    """
    #  void QQuick3DParticleScaleAffector::easingCurveChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleScaleAffector18easingCurveChangedEv',
    )

  def prepareToAffect(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::prepareToAffect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#prepareToAffect
    """
    #  void QQuick3DParticleScaleAffector::prepareToAffect()
    ritual = 'ritual_ZN29QQuick3DParticleScaleAffector15prepareToAffectEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuick3DParticleScaleAffector15prepareToAffectEv')
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleData, QQuick3DParticleDataCurrent, float)
  @overload(QQuick3DParticleData, NoneType, float)
  def affectParticle(
      self,
      a0: QQuick3DParticleData,
      d: Optional[QQuick3DParticleDataCurrent],
      time: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleScaleAffector::affectParticle(const
    QQuick3DParticleData &a0, QQuick3DParticleDataCurrent *d, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlescaleaffector.html#affectParticle

    Parameters
    ----------

    a0 : QQuick3DParticleData
      Passed on as a value: Qt reads the C++ QQuick3DParticleData, which
      stays Python's own.

    d : Optional[QQuick3DParticleDataCurrent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : float
      Passed on as it is.
    """
    #  void QQuick3DParticleScaleAffector::affectParticle(const
    #      QQuick3DParticleData &a0, QQuick3DParticleDataCurrent *d, float
    #      time)
    ritual = (
        'ritual_ZN29QQuick3DParticleScaleAffector14affectParticleERK20QQuic'
        'k3DParticleDataP27QQuick3DParticleDataCurrentf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuick3DParticleScaleAffector14affectParticleERK2'
          '0QQuick3DParticleDataP27QQuick3DParticleDataCurrentf')
    self.uglySide.call(ritual, self._valueOf(a0), self._addressOf(d), time)
