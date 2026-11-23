"""
QVariantAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qvariantanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractAnimation, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEasingCurve, QEvent, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QEvent = WAIT['QEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVariantAnimation(QAbstractAnimation):
  """
  The cute side of Qt's QVariantAnimation: a plain Python object standing in
  front of one C++ QVariantAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's QVariantAnimation is
  built on Qt's QAbstractAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVariantAnimation that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'startValue',
  'setStartValue', 'endValue', 'setEndValue', 'keyValueAt', 'setKeyValueAt',
  'currentValue', 'duration', 'setDuration', 'easingCurve', 'setEasingCurve',
  'event', 'updateCurrentTime', 'updateState', 'updateCurrentValue',
  'interpolated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariantAnimation::~QVariantAnimation()': the destructor: Python
    never removes a C++ QVariantAnimation.

  What has no ritual
  ------------------

  15 of the 35 functions Qt declares: 10 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QVariantAnimation is created at the first use, not by
    'QVariantAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVariantAnimation.
  - Qt tells when it has removed the C++ QVariantAnimation. Every call on the
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
    Calls Qt's 'QString QVariantAnimation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#tr

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
    #  QString QVariantAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QVariantAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVariantAnimation'

  #  A C++ QVariantAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVariantAnimation'

  #  The functions Qt calls itself that QVariantAnimation is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateCurrentValue': (
          ('_ZN17QVariantAnimation18updateCurrentValueERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'interpolated': (
          ('_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value', 'QtCore:QVariant'),
               ('double', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVariantAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVariantAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QVariantAnimation10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def startValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QVariantAnimation::startValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#startValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVariantAnimation::startValue() const
    address = self.uglySide.call(
        'ritual_ZNK17QVariantAnimation10startValueEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def endValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QVariantAnimation::endValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#endValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVariantAnimation::endValue() const
    address = self.uglySide.call('ritual_ZNK17QVariantAnimation8endValueEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(float)
  def keyValueAt(self, step: float) -> QVariant:
    """
    Calls Qt's 'QVariant QVariantAnimation::keyValueAt(qreal step) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#keyValueAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVariantAnimation::keyValueAt(qreal step) const
    address = self.uglySide.call(
        'ritual_ZNK17QVariantAnimation10keyValueAtEd', step,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QVariantAnimation::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVariantAnimation::currentValue() const
    address = self.uglySide.call(
        'ritual_ZNK17QVariantAnimation12currentValueEv',
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QVariantAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#duration
    """
    #  int QVariantAnimation::duration() const
    ritual = 'ritual_ZNK17QVariantAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QVariantAnimation8durationEv'
    return self.uglySide.call(ritual)

  def easingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QVariantAnimation::easingCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#easingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QVariantAnimation::easingCurve() const
    address = self.uglySide.call(
        'ritual_ZNK17QVariantAnimation11easingCurveEv',
    )
    from . import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  @overload(QVariant, QVariant, float)
  def interpolated(
      self,
      from_: QVariant,
      to: QVariant,
      progress: float,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QVariantAnimation::interpolated(const QVariant
    &from, const QVariant &to, qreal progress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#interpolated

    Parameters
    ----------

    from_ : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    to : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    progress : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVariantAnimation::interpolated(const QVariant &from, const
    #      QVariant &to, qreal progress) const
    ritual = 'ritual_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d')
    address = self.uglySide.call(
        ritual, self._valueOf(from_), self._valueOf(to), progress,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setStartValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QVariantAnimation::setStartValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#setStartValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QVariantAnimation::setStartValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN17QVariantAnimation13setStartValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(QVariant)
  def setEndValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QVariantAnimation::setEndValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#setEndValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QVariantAnimation::setEndValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN17QVariantAnimation11setEndValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(float, QVariant)
  def setKeyValueAt(self, step: float, value: QVariant) -> None:
    """
    Calls Qt's 'void QVariantAnimation::setKeyValueAt(qreal step, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#setKeyValueAt

    Parameters
    ----------

    step : float
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QVariantAnimation::setKeyValueAt(qreal step, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN17QVariantAnimation13setKeyValueAtEdRK8QVariant',
        step, self._valueOf(value),
    )

  @overload(int)
  def setDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void QVariantAnimation::setDuration(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#setDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QVariantAnimation::setDuration(int msecs)
    self.uglySide.call('ritual_ZN17QVariantAnimation11setDurationEi', msecs)

  @overload(QEasingCurve)
  def setEasingCurve(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void QVariantAnimation::setEasingCurve(const QEasingCurve
    &easing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#setEasingCurve

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QVariantAnimation::setEasingCurve(const QEasingCurve &easing)
    self.uglySide.call(
        'ritual_ZN17QVariantAnimation14setEasingCurveERK12QEasingCurve',
        self._valueOf(easing),
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
    'QVariantAnimation::QVariantAnimation(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#QVariantAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVariantAnimation::QVariantAnimation(QObject *parent)
    self._noteCreation(QVariantAnimation, lambda: Rituals.call(
        'ritual_ZN17QVariantAnimationC1EP7QObject', self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QVariantAnimation::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVariantAnimation::event(QEvent *event)
    ritual = 'ritual_ZN17QVariantAnimation5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QVariantAnimation5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QVariantAnimation::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QVariantAnimation::updateCurrentTime(int a0)
    ritual = 'ritual_ZN17QVariantAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QVariantAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)

  @overload(QAbstractAnimation.State, QAbstractAnimation.State)
  def updateState(
      self,
      newState: QAbstractAnimation.State,
      oldState: QAbstractAnimation.State,
  ) -> None:
    """
    Calls Qt's 'void QVariantAnimation::updateState(QAbstractAnimation::State
    newState, QAbstractAnimation::State oldState)'.

    Qt's own words: https://doc.qt.io/qt-6/qvariantanimation.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimation.State
      Passed on as its number.

    oldState : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void QVariantAnimation::updateState(QAbstractAnimation::State
    #      newState, QAbstractAnimation::State oldState)
    ritual = (
        'ritual_ZN17QVariantAnimation11updateStateEN18QAbstractAnimation5St'
        'ateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QVariantAnimation11updateStateEN18QAbstractAnimat'
          'ion5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)

  @overload(QVariant)
  def updateCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QVariantAnimation::updateCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvariantanimation.html#updateCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QVariantAnimation::updateCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN17QVariantAnimation18updateCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QVariantAnimation18updateCurrentValueERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(value))
