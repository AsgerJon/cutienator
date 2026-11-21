"""
QEasingCurve binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qeasingcurve.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QEasingCurveType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QEasingCurve(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QEasingCurve: a plain Python object standing in front
  of one C++ QEasingCurve.

  C++ hands a QEasingCurve around as a copy, so every C++ QEasingCurve behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QEasingCurve that has a ritual and that Python can
  call so far, 12 names in all: 'amplitude', 'setAmplitude', 'period',
  'setPeriod', 'overshoot', 'setOvershoot', 'addCubicBezierSegment',
  'addTCBSegment', 'type', 'setType', 'valueForProgress', 'fromCubicBezier'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QEasingCurve::~QEasingCurve()': the destructor: Python removes its
    C++ QEasingCurve by it, and has no other use for it.

  What has no ritual
  ------------------

  10 of the 25 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QEasingCurve is created at the first use, not by
    'QEasingCurve(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QEasingCurve back gives a copy the ritual made for
    Python, in a new cute QEasingCurve.
  """

  #  The enums Qt writes inside QEasingCurve, and the names Qt has for the
  #  combinations of its flags enums.
  Type = QEasingCurveType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPointF, QPointF)
  def fromCubicBezier(c1: QPointF, c2: QPointF) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QEasingCurve::fromCubicBezier(QPointF c1,
    QPointF c2)'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#fromCubicBezier

    Parameters
    ----------

    c1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    c2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QEasingCurve::fromCubicBezier(QPointF c1, QPointF c2)
    address = Rituals.call(
        'ritual_ZN12QEasingCurve15fromCubicBezierE7QPointFS0_',
        CuteMixin._valueOf(c1), CuteMixin._valueOf(c2),
    )
    return QEasingCurve._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEasingCurve'

  #  Qt's '~QEasingCurve()'. Naming it makes this a value class: Python owns
  #  every C++ QEasingCurve behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QEasingCurveD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def amplitude(self) -> float:
    """
    Calls Qt's 'qreal QEasingCurve::amplitude() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#amplitude
    """
    #  qreal QEasingCurve::amplitude() const
    return self.uglySide.call('ritual_ZNK12QEasingCurve9amplitudeEv')

  def period(self) -> float:
    """
    Calls Qt's 'qreal QEasingCurve::period() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#period
    """
    #  qreal QEasingCurve::period() const
    return self.uglySide.call('ritual_ZNK12QEasingCurve6periodEv')

  def overshoot(self) -> float:
    """
    Calls Qt's 'qreal QEasingCurve::overshoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#overshoot
    """
    #  qreal QEasingCurve::overshoot() const
    return self.uglySide.call('ritual_ZNK12QEasingCurve9overshootEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QEasingCurve::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QEasingCurve::type() const
    return QEasingCurve.Type(self.uglySide.call(
        'ritual_ZNK12QEasingCurve4typeEv',
    ))

  @overload(float)
  def valueForProgress(self, progress: float) -> float:
    """
    Calls Qt's 'qreal QEasingCurve::valueForProgress(qreal progress) const'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#valueForProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  qreal QEasingCurve::valueForProgress(qreal progress) const
    return self.uglySide.call(
        'ritual_ZNK12QEasingCurve16valueForProgressEd', progress,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAmplitude(self, amplitude: float) -> None:
    """
    Calls Qt's 'void QEasingCurve::setAmplitude(qreal amplitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#setAmplitude

    Parameters
    ----------

    amplitude : float
      Passed on as it is.
    """
    #  void QEasingCurve::setAmplitude(qreal amplitude)
    self.uglySide.call('ritual_ZN12QEasingCurve12setAmplitudeEd', amplitude)

  @overload(float)
  def setPeriod(self, period: float) -> None:
    """
    Calls Qt's 'void QEasingCurve::setPeriod(qreal period)'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#setPeriod

    Parameters
    ----------

    period : float
      Passed on as it is.
    """
    #  void QEasingCurve::setPeriod(qreal period)
    self.uglySide.call('ritual_ZN12QEasingCurve9setPeriodEd', period)

  @overload(float)
  def setOvershoot(self, overshoot: float) -> None:
    """
    Calls Qt's 'void QEasingCurve::setOvershoot(qreal overshoot)'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#setOvershoot

    Parameters
    ----------

    overshoot : float
      Passed on as it is.
    """
    #  void QEasingCurve::setOvershoot(qreal overshoot)
    self.uglySide.call('ritual_ZN12QEasingCurve12setOvershootEd', overshoot)

  @overload(Type)
  def setType(self, type: Type) -> None:
    """
    Calls Qt's 'void QEasingCurve::setType(Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#setType

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void QEasingCurve::setType(Type type)
    self.uglySide.call(
        'ritual_ZN12QEasingCurve7setTypeENS_4TypeE', type.value,
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
  @overload(Type)
  def __init__(self, type: Type = Type.Linear) -> None:
    """
    Notes what was given, for Qt's 'QEasingCurve::QEasingCurve(Type type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#QEasingCurve

    Parameters
    ----------

    type : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.Linear.
    """
    #  QEasingCurve::QEasingCurve(Type type)
    self._noteCreation(QEasingCurve, lambda: Rituals.call(
        'ritual_ZN12QEasingCurveC1ENS_4TypeE', type.value,
    ))

  @overload(THIS)
  def __init__(self, other: QEasingCurve) -> None:
    """
    Notes what was given, for Qt's 'QEasingCurve::QEasingCurve(const
    QEasingCurve &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#QEasingCurve

    Parameters
    ----------

    other : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  QEasingCurve::QEasingCurve(const QEasingCurve &other)
    self._noteCreation(QEasingCurve, lambda: Rituals.call(
        'ritual_ZN12QEasingCurveC1ERKS_', self._valueOf(other),
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

  @overload(QPointF, QPointF, QPointF)
  def addCubicBezierSegment(
      self,
      c1: QPointF,
      c2: QPointF,
      endPoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QEasingCurve::addCubicBezierSegment(const QPointF &c1,
    const QPointF &c2, const QPointF &endPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeasingcurve.html#addCubicBezierSegment

    Parameters
    ----------

    c1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    c2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QEasingCurve::addCubicBezierSegment(const QPointF &c1, const
    #      QPointF &c2, const QPointF &endPoint)
    self.uglySide.call(
        'ritual_ZN12QEasingCurve21addCubicBezierSegmentERK7QPointFS2_S2_',
        self._valueOf(c1), self._valueOf(c2), self._valueOf(endPoint),
    )

  @overload(QPointF, float, float, float)
  def addTCBSegment(
      self,
      nextPoint: QPointF,
      t: float,
      c: float,
      b: float,
  ) -> None:
    """
    Calls Qt's 'void QEasingCurve::addTCBSegment(const QPointF &nextPoint,
    qreal t, qreal c, qreal b)'.

    Qt's own words: https://doc.qt.io/qt-6/qeasingcurve.html#addTCBSegment

    Parameters
    ----------

    nextPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    t : float
      Passed on as it is.

    c : float
      Passed on as it is.

    b : float
      Passed on as it is.
    """
    #  void QEasingCurve::addTCBSegment(const QPointF &nextPoint, qreal t,
    #      qreal c, qreal b)
    self.uglySide.call(
        'ritual_ZN12QEasingCurve13addTCBSegmentERK7QPointFddd',
        self._valueOf(nextPoint), t, c, b,
    )
