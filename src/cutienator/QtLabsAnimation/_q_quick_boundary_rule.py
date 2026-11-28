"""
QQuickBoundaryRule binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsAnimation/6.12.0/QtLabsAnimation/private/qquickboundaryrule_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickBoundaryRule to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEasingCurve, QMetaObject, QObject, QVariant
  from ..QtQml import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QObject = WAIT['QObject']
  QQmlProperty = WAIT['QQmlProperty']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBoundaryRule(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickBoundaryRule: a plain Python object standing in
  front of one C++ QQuickBoundaryRule.

  What exists
  -----------

  Every function of Qt's QQuickBoundaryRule that has a ritual and that Python
  can call so far, 39 names in all: 'metaObject', 'tr', 'setTarget', 'write',
  'enabled', 'setEnabled', 'minimum', 'setMinimum', 'minimumOvershoot',
  'setMinimumOvershoot', 'maximum', 'setMaximum', 'maximumOvershoot',
  'setMaximumOvershoot', 'overshootScale', 'setOvershootScale',
  'currentOvershoot', 'peakOvershoot', 'overshootFilter',
  'setOvershootFilter', 'returnToBounds', 'easing', 'setEasing',
  'returnDuration', 'setReturnDuration', 'classBegin', 'componentComplete',
  'enabledChanged', 'minimumChanged', 'minimumOvershootChanged',
  'maximumChanged', 'maximumOvershootChanged', 'overshootScaleChanged',
  'currentOvershootChanged', 'peakOvershootChanged',
  'overshootFilterChanged', 'easingChanged', 'returnDurationChanged',
  'returnedToBounds'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBoundaryRule::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickBoundaryRule::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickBoundaryRulePrivate *QQuickBoundaryRule::d_func()': gives
    'QQuickBoundaryRulePrivate', which has no cute class yet.
  - Qt's 'const QQuickBoundaryRulePrivate *QQuickBoundaryRule::d_func()
    const': gives 'QQuickBoundaryRulePrivate', which has no cute class yet.
  - Qt's 'QQuickBoundaryRule::~QQuickBoundaryRule()': the destructor: Python
    never removes a C++ QQuickBoundaryRule.

  What has no ritual
  ------------------

  2 of the 47 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickBoundaryRule is created at the first use, not by
    'QQuickBoundaryRule(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBoundaryRule.
  - Qt tells when it has removed the C++ QQuickBoundaryRule. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickBoundaryRule, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class OvershootFilter(CuteNum):
    """
    The enum 'QQuickBoundaryRule::OvershootFilter' of Qt, with the 2 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Peak = Kee[int](1)

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
    Calls Qt's 'QString QQuickBoundaryRule::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#tr

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
    #  QString QQuickBoundaryRule::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickBoundaryRule2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBoundaryRule'

  #  A C++ QQuickBoundaryRule Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBoundaryRule'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBoundaryRule::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBoundaryRule::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickBoundaryRule::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#enabled
    """
    #  bool QQuickBoundaryRule::enabled() const
    return self.uglySide.call('ritual_ZNK18QQuickBoundaryRule7enabledEv')

  def minimum(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#minimum
    """
    #  qreal QQuickBoundaryRule::minimum() const
    return self.uglySide.call('ritual_ZNK18QQuickBoundaryRule7minimumEv')

  def minimumOvershoot(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::minimumOvershoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#minimumOvershoot
    """
    #  qreal QQuickBoundaryRule::minimumOvershoot() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule16minimumOvershootEv',
    )

  def maximum(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#maximum
    """
    #  qreal QQuickBoundaryRule::maximum() const
    return self.uglySide.call('ritual_ZNK18QQuickBoundaryRule7maximumEv')

  def maximumOvershoot(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::maximumOvershoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#maximumOvershoot
    """
    #  qreal QQuickBoundaryRule::maximumOvershoot() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule16maximumOvershootEv',
    )

  def overshootScale(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::overshootScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#overshootScale
    """
    #  qreal QQuickBoundaryRule::overshootScale() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule14overshootScaleEv',
    )

  def currentOvershoot(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::currentOvershoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#currentOvershoot
    """
    #  qreal QQuickBoundaryRule::currentOvershoot() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule16currentOvershootEv',
    )

  def peakOvershoot(self) -> float:
    """
    Calls Qt's 'qreal QQuickBoundaryRule::peakOvershoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#peakOvershoot
    """
    #  qreal QQuickBoundaryRule::peakOvershoot() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule13peakOvershootEv',
    )

  def overshootFilter(self) -> OvershootFilter:
    """
    Calls Qt's 'OvershootFilter QQuickBoundaryRule::overshootFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#overshootFilter

    Returns
    -------

    OvershootFilter
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OvershootFilter(number)'
      gives.
    """
    #  OvershootFilter QQuickBoundaryRule::overshootFilter() const
    return QQuickBoundaryRule.OvershootFilter(self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule15overshootFilterEv',
    ))

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickBoundaryRule::easing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickBoundaryRule::easing() const
    address = self.uglySide.call('ritual_ZNK18QQuickBoundaryRule6easingEv')
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def returnDuration(self) -> int:
    """
    Calls Qt's 'int QQuickBoundaryRule::returnDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#returnDuration
    """
    #  int QQuickBoundaryRule::returnDuration() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickBoundaryRule14returnDurationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlProperty)
  def setTarget(self, a0: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setTarget(const QQmlProperty &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#setTarget

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQuickBoundaryRule::setTarget(const QQmlProperty &a0)
    ritual = 'ritual_ZN18QQuickBoundaryRule9setTargetERK12QQmlProperty'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickBoundaryRule9setTargetERK12QQmlProperty'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule10setEnabledEb', enabled,
    )

  @overload(float)
  def setMinimum(self, minimum: float) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setMinimum(qreal minimum)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#setMinimum

    Parameters
    ----------

    minimum : float
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setMinimum(qreal minimum)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule10setMinimumEd', minimum,
    )

  @overload(float)
  def setMinimumOvershoot(self, minimum: float) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setMinimumOvershoot(qreal minimum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#setMinimumOvershoot

    Parameters
    ----------

    minimum : float
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setMinimumOvershoot(qreal minimum)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule19setMinimumOvershootEd', minimum,
    )

  @overload(float)
  def setMaximum(self, maximum: float) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setMaximum(qreal maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#setMaximum

    Parameters
    ----------

    maximum : float
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setMaximum(qreal maximum)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule10setMaximumEd', maximum,
    )

  @overload(float)
  def setMaximumOvershoot(self, maximum: float) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setMaximumOvershoot(qreal maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#setMaximumOvershoot

    Parameters
    ----------

    maximum : float
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setMaximumOvershoot(qreal maximum)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule19setMaximumOvershootEd', maximum,
    )

  @overload(float)
  def setOvershootScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setOvershootScale(qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#setOvershootScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setOvershootScale(qreal scale)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule17setOvershootScaleEd', scale,
    )

  @overload(OvershootFilter)
  def setOvershootFilter(self, overshootFilter: OvershootFilter) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setOvershootFilter(OvershootFilter
    overshootFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#setOvershootFilter

    Parameters
    ----------

    overshootFilter : OvershootFilter
      Passed on as its number.
    """
    #  void QQuickBoundaryRule::setOvershootFilter(OvershootFilter
    #      overshootFilter)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule18setOvershootFilterENS_15OvershootFi'
        'lterE',
        overshootFilter.value,
    )

  @overload(QEasingCurve)
  def setEasing(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setEasing(const QEasingCurve
    &easing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#setEasing

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickBoundaryRule::setEasing(const QEasingCurve &easing)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule9setEasingERK12QEasingCurve',
        self._valueOf(easing),
    )

  @overload(int)
  def setReturnDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::setReturnDuration(int duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#setReturnDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuickBoundaryRule::setReturnDuration(int duration)
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule17setReturnDurationEi', duration,
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
    'QQuickBoundaryRule::QQuickBoundaryRule(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#QQuickBoundaryRule

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickBoundaryRule::QQuickBoundaryRule(QObject *parent)
    self._noteCreation(QQuickBoundaryRule, lambda: Rituals.call(
        'ritual_ZN18QQuickBoundaryRuleC1EP7QObject',
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

  @overload(QVariant)
  def write(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::write(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#write

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickBoundaryRule::write(const QVariant &value)
    ritual = 'ritual_ZN18QQuickBoundaryRule5writeERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickBoundaryRule5writeERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(value))

  def returnToBounds(self) -> bool:
    """
    Calls Qt's 'bool QQuickBoundaryRule::returnToBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#returnToBounds
    """
    #  bool QQuickBoundaryRule::returnToBounds()
    return self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule14returnToBoundsEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickboundaryrule.html#classBegin
    """
    #  void QQuickBoundaryRule::classBegin()
    ritual = 'ritual_ZN18QQuickBoundaryRule10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickBoundaryRule10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#componentComplete
    """
    #  void QQuickBoundaryRule::componentComplete()
    ritual = 'ritual_ZN18QQuickBoundaryRule17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickBoundaryRule17componentCompleteEv'
    self.uglySide.call(ritual)

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#enabledChanged
    """
    #  void QQuickBoundaryRule::enabledChanged()
    self.uglySide.call('ritual_ZN18QQuickBoundaryRule14enabledChangedEv')

  def minimumChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::minimumChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#minimumChanged
    """
    #  void QQuickBoundaryRule::minimumChanged()
    self.uglySide.call('ritual_ZN18QQuickBoundaryRule14minimumChangedEv')

  def minimumOvershootChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::minimumOvershootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#minimumOvershootChanged
    """
    #  void QQuickBoundaryRule::minimumOvershootChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule23minimumOvershootChangedEv',
    )

  def maximumChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::maximumChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#maximumChanged
    """
    #  void QQuickBoundaryRule::maximumChanged()
    self.uglySide.call('ritual_ZN18QQuickBoundaryRule14maximumChangedEv')

  def maximumOvershootChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::maximumOvershootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#maximumOvershootChanged
    """
    #  void QQuickBoundaryRule::maximumOvershootChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule23maximumOvershootChangedEv',
    )

  def overshootScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::overshootScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#overshootScaleChanged
    """
    #  void QQuickBoundaryRule::overshootScaleChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule21overshootScaleChangedEv',
    )

  def currentOvershootChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::currentOvershootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#currentOvershootChanged
    """
    #  void QQuickBoundaryRule::currentOvershootChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule23currentOvershootChangedEv',
    )

  def peakOvershootChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::peakOvershootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#peakOvershootChanged
    """
    #  void QQuickBoundaryRule::peakOvershootChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule20peakOvershootChangedEv',
    )

  def overshootFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::overshootFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#overshootFilterChanged
    """
    #  void QQuickBoundaryRule::overshootFilterChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule22overshootFilterChangedEv',
    )

  def easingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::easingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#easingChanged
    """
    #  void QQuickBoundaryRule::easingChanged()
    self.uglySide.call('ritual_ZN18QQuickBoundaryRule13easingChangedEv')

  def returnDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::returnDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#returnDurationChanged
    """
    #  void QQuickBoundaryRule::returnDurationChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickBoundaryRule21returnDurationChangedEv',
    )

  def returnedToBounds(self) -> None:
    """
    Calls Qt's 'void QQuickBoundaryRule::returnedToBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickboundaryrule.html#returnedToBounds
    """
    #  void QQuickBoundaryRule::returnedToBounds()
    self.uglySide.call('ritual_ZN18QQuickBoundaryRule16returnedToBoundsEv')
