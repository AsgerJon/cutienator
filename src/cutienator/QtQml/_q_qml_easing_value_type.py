"""
QQmlEasingValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlEasingValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QEasingCurve
from . import QQmlEasing

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlEasingValueType(QEasingCurve):
  """
  The cute side of Qt's QQmlEasingValueType: a plain Python object standing
  in front of one C++ QQmlEasingValueType.

  It is built on the cute 'QEasingCurve', as Qt's QQmlEasingValueType is
  built on Qt's QEasingCurve, and has everything that class has.

  C++ hands a QQmlEasingValueType around as a copy, so every C++
  QQmlEasingValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlEasingValueType that has a ritual and that
  Python can call so far, 9 names in all: 'valueForProgress', 'type',
  'amplitude', 'overshoot', 'period', 'setType', 'setAmplitude',
  'setOvershoot', 'setPeriod'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlEasingValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlEasingValueType::qt_qmlMarker_extended()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlEasingValueType::setBezierCurve(const QList<qreal> &a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<qreal> QQmlEasingValueType::bezierCurve() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlEasingValueType::~QQmlEasingValueType()': the destructor:
    Python removes its C++ QQmlEasingValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlEasingValueType is created at the first use, not by
    'QQmlEasingValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlEasingValueType back gives a copy the ritual made
    for Python, in a new cute QQmlEasingValueType.
  - Each name of Qt's QQmlEasingValueType that has no cute function yet,
    'bezierCurve', 'setBezierCurve', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEasingValueType'

  #  Qt's '~QQmlEasingValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlEasingValueType behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlEasingValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QQmlEasing.Type:
    """
    Calls Qt's 'QQmlEasing::Type QQmlEasingValueType::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasingvaluetype.html#type

    Returns
    -------

    QQmlEasing.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QQmlEasing.Type(number)'
      gives.
    """
    #  QQmlEasing::Type QQmlEasingValueType::type() const
    return QQmlEasing.Type(self.uglySide.call(
        'ritual_ZNK19QQmlEasingValueType4typeEv',
    ))

  def amplitude(self) -> float:
    """
    Calls Qt's 'qreal QQmlEasingValueType::amplitude() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasingvaluetype.html#amplitude
    """
    #  qreal QQmlEasingValueType::amplitude() const
    return self.uglySide.call('ritual_ZNK19QQmlEasingValueType9amplitudeEv')

  def overshoot(self) -> float:
    """
    Calls Qt's 'qreal QQmlEasingValueType::overshoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasingvaluetype.html#overshoot
    """
    #  qreal QQmlEasingValueType::overshoot() const
    return self.uglySide.call('ritual_ZNK19QQmlEasingValueType9overshootEv')

  def period(self) -> float:
    """
    Calls Qt's 'qreal QQmlEasingValueType::period() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasingvaluetype.html#period
    """
    #  qreal QQmlEasingValueType::period() const
    return self.uglySide.call('ritual_ZNK19QQmlEasingValueType6periodEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlEasing.Type)
  def setType(self, a0: QQmlEasing.Type) -> None:
    """
    Calls Qt's 'void QQmlEasingValueType::setType(QQmlEasing::Type a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasingvaluetype.html#setType

    Parameters
    ----------

    a0 : QQmlEasing.Type
      Passed on as its number.
    """
    #  void QQmlEasingValueType::setType(QQmlEasing::Type a0)
    self.uglySide.call(
        'ritual_ZN19QQmlEasingValueType7setTypeEN10QQmlEasing4TypeE',
        a0.value,
    )

  @overload(float)
  def setAmplitude(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlEasingValueType::setAmplitude(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmleasingvaluetype.html#setAmplitude

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlEasingValueType::setAmplitude(qreal a0)
    self.uglySide.call('ritual_ZN19QQmlEasingValueType12setAmplitudeEd', a0)

  @overload(float)
  def setOvershoot(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlEasingValueType::setOvershoot(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmleasingvaluetype.html#setOvershoot

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlEasingValueType::setOvershoot(qreal a0)
    self.uglySide.call('ritual_ZN19QQmlEasingValueType12setOvershootEd', a0)

  @overload(float)
  def setPeriod(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlEasingValueType::setPeriod(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmleasingvaluetype.html#setPeriod

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlEasingValueType::setPeriod(qreal a0)
    self.uglySide.call('ritual_ZN19QQmlEasingValueType9setPeriodEd', a0)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlEasingValueType::QQmlEasingValueType()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmleasingvaluetype.html#QQmlEasingValueType
    """
    #  QQmlEasingValueType::QQmlEasingValueType()
    self._noteCreation(QQmlEasingValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlEasingValueTypeC1Ev',
    ))

  @overload(QQmlEasing.Type)
  def __init__(self, type: QQmlEasing.Type) -> None:
    """
    Notes what was given, for Qt's
    'QQmlEasingValueType::QQmlEasingValueType(QQmlEasing::Type type)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmleasingvaluetype.html#QQmlEasingValueType

    Parameters
    ----------

    type : QQmlEasing.Type
      Passed on as its number.
    """
    #  QQmlEasingValueType::QQmlEasingValueType(QQmlEasing::Type type)
    self._noteCreation(QQmlEasingValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlEasingValueTypeC1EN10QQmlEasing4TypeE', type.value,
    ))

  @overload(QEasingCurve)
  def __init__(self, easing: QEasingCurve) -> None:
    """
    Notes what was given, for Qt's
    'QQmlEasingValueType::QQmlEasingValueType(const QEasingCurve &easing)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmleasingvaluetype.html#QQmlEasingValueType

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  QQmlEasingValueType::QQmlEasingValueType(const QEasingCurve &easing)
    self._noteCreation(QQmlEasingValueType, lambda: Rituals.call(
        'ritual_ZN19QQmlEasingValueTypeC1ERK12QEasingCurve',
        self._valueOf(easing),
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
  def valueForProgress(self, progress: float) -> float:
    """
    Calls Qt's 'qreal QQmlEasingValueType::valueForProgress(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmleasingvaluetype.html#valueForProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  qreal QQmlEasingValueType::valueForProgress(qreal progress)
    return self.uglySide.call(
        'ritual_ZN19QQmlEasingValueType16valueForProgressEd', progress,
    )

  @staticmethod
  def bezierCurve(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QQmlEasingValueType::bezierCurve() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlEasingValueType.bezierCurve' has no cute function yet. Qt's "
        "'QList<qreal> QQmlEasingValueType::bezierCurve() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setBezierCurve(*__, **_) -> Never:
    """
    Qt's 'void QQmlEasingValueType::setBezierCurve(const QList<qreal> &a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlEasingValueType.setBezierCurve' has no cute function yet. "
        "Qt's 'void QQmlEasingValueType::setBezierCurve(const QList<qreal> "
        "&a0)': takes a type Python has no way to hand over yet.")
