"""
QQuickSpringAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickspringanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickSpringAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickNumberAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSpringAnimation(QQuickNumberAnimation):
  """
  The cute side of Qt's QQuickSpringAnimation: a plain Python object standing
  in front of one C++ QQuickSpringAnimation.

  It is built on the cute 'QQuickNumberAnimation', as Qt's
  QQuickSpringAnimation is built on Qt's QQuickNumberAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSpringAnimation that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'velocity',
  'setVelocity', 'spring', 'setSpring', 'damping', 'setDamping', 'epsilon',
  'setEpsilon', 'mass', 'setMass', 'modulus', 'setModulus', 'modulusChanged',
  'massChanged', 'syncChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSpringAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSpringAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSpringAnimationPrivate *QQuickSpringAnimation::d_func()':
    gives 'QQuickSpringAnimationPrivate', which has no cute class yet.
  - Qt's 'const QQuickSpringAnimationPrivate *QQuickSpringAnimation::d_func()
    const': gives 'QQuickSpringAnimationPrivate', which has no cute class
    yet.
  - Qt's 'QQuickSpringAnimation::~QQuickSpringAnimation()': the destructor:
    Python never removes a C++ QQuickSpringAnimation.
  - Qt's 'QAbstractAnimationJob
    *QQuickSpringAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 30 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSpringAnimation is created at the first use, not by
    'QQuickSpringAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSpringAnimation.
  - Qt tells when it has removed the C++ QQuickSpringAnimation. Every call on
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
    Calls Qt's 'QString QQuickSpringAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#tr

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
    #  QString QQuickSpringAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickSpringAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSpringAnimation'

  #  A C++ QQuickSpringAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSpringAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSpringAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSpringAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickSpringAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def velocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickSpringAnimation::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#velocity
    """
    #  qreal QQuickSpringAnimation::velocity() const
    return self.uglySide.call('ritual_ZNK21QQuickSpringAnimation8velocityEv')

  def spring(self) -> float:
    """
    Calls Qt's 'qreal QQuickSpringAnimation::spring() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#spring
    """
    #  qreal QQuickSpringAnimation::spring() const
    return self.uglySide.call('ritual_ZNK21QQuickSpringAnimation6springEv')

  def damping(self) -> float:
    """
    Calls Qt's 'qreal QQuickSpringAnimation::damping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#damping
    """
    #  qreal QQuickSpringAnimation::damping() const
    return self.uglySide.call('ritual_ZNK21QQuickSpringAnimation7dampingEv')

  def epsilon(self) -> float:
    """
    Calls Qt's 'qreal QQuickSpringAnimation::epsilon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#epsilon
    """
    #  qreal QQuickSpringAnimation::epsilon() const
    return self.uglySide.call('ritual_ZNK21QQuickSpringAnimation7epsilonEv')

  def mass(self) -> float:
    """
    Calls Qt's 'qreal QQuickSpringAnimation::mass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#mass
    """
    #  qreal QQuickSpringAnimation::mass() const
    return self.uglySide.call('ritual_ZNK21QQuickSpringAnimation4massEv')

  def modulus(self) -> float:
    """
    Calls Qt's 'qreal QQuickSpringAnimation::modulus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#modulus
    """
    #  qreal QQuickSpringAnimation::modulus() const
    return self.uglySide.call('ritual_ZNK21QQuickSpringAnimation7modulusEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setVelocity(self, velocity: float) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::setVelocity(qreal velocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#setVelocity

    Parameters
    ----------

    velocity : float
      Passed on as it is.
    """
    #  void QQuickSpringAnimation::setVelocity(qreal velocity)
    self.uglySide.call(
        'ritual_ZN21QQuickSpringAnimation11setVelocityEd', velocity,
    )

  @overload(float)
  def setSpring(self, spring: float) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::setSpring(qreal spring)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#setSpring

    Parameters
    ----------

    spring : float
      Passed on as it is.
    """
    #  void QQuickSpringAnimation::setSpring(qreal spring)
    self.uglySide.call(
        'ritual_ZN21QQuickSpringAnimation9setSpringEd', spring,
    )

  @overload(float)
  def setDamping(self, damping: float) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::setDamping(qreal damping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#setDamping

    Parameters
    ----------

    damping : float
      Passed on as it is.
    """
    #  void QQuickSpringAnimation::setDamping(qreal damping)
    self.uglySide.call(
        'ritual_ZN21QQuickSpringAnimation10setDampingEd', damping,
    )

  @overload(float)
  def setEpsilon(self, epsilon: float) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::setEpsilon(qreal epsilon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#setEpsilon

    Parameters
    ----------

    epsilon : float
      Passed on as it is.
    """
    #  void QQuickSpringAnimation::setEpsilon(qreal epsilon)
    self.uglySide.call(
        'ritual_ZN21QQuickSpringAnimation10setEpsilonEd', epsilon,
    )

  @overload(float)
  def setMass(self, modulus: float) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::setMass(qreal modulus)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspringanimation.html#setMass

    Parameters
    ----------

    modulus : float
      Passed on as it is.
    """
    #  void QQuickSpringAnimation::setMass(qreal modulus)
    self.uglySide.call('ritual_ZN21QQuickSpringAnimation7setMassEd', modulus)

  @overload(float)
  def setModulus(self, modulus: float) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::setModulus(qreal modulus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#setModulus

    Parameters
    ----------

    modulus : float
      Passed on as it is.
    """
    #  void QQuickSpringAnimation::setModulus(qreal modulus)
    self.uglySide.call(
        'ritual_ZN21QQuickSpringAnimation10setModulusEd', modulus,
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
    'QQuickSpringAnimation::QQuickSpringAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#QQuickSpringAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSpringAnimation::QQuickSpringAnimation(QObject *parent)
    self._noteCreation(QQuickSpringAnimation, lambda: Rituals.call(
        'ritual_ZN21QQuickSpringAnimationC1EP7QObject',
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

  def modulusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::modulusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#modulusChanged
    """
    #  void QQuickSpringAnimation::modulusChanged()
    self.uglySide.call('ritual_ZN21QQuickSpringAnimation14modulusChangedEv')

  def massChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::massChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#massChanged
    """
    #  void QQuickSpringAnimation::massChanged()
    self.uglySide.call('ritual_ZN21QQuickSpringAnimation11massChangedEv')

  def syncChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpringAnimation::syncChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspringanimation.html#syncChanged
    """
    #  void QQuickSpringAnimation::syncChanged()
    self.uglySide.call('ritual_ZN21QQuickSpringAnimation11syncChangedEv')
