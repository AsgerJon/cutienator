"""
QQuickBulkValueAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickBulkValueAnimator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQml import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QEasingCurve
  from . import QQuickBulkValueUpdater
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QEasingCurve = WAIT['QEasingCurve']
  QQuickBulkValueUpdater = WAIT['QQuickBulkValueUpdater']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBulkValueAnimator(QAbstractAnimationJob):
  """
  The cute side of Qt's QQuickBulkValueAnimator: a plain Python object
  standing in front of one C++ QQuickBulkValueAnimator.

  It is built on the cute 'QAbstractAnimationJob', as Qt's
  QQuickBulkValueAnimator is built on Qt's QAbstractAnimationJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBulkValueAnimator that has a ritual and that
  Python can call so far, 9 names in all: 'setAnimValue', 'getAnimValue',
  'duration', 'setDuration', 'easingCurve', 'setEasingCurve',
  'updateCurrentTime', 'topLevelAnimationLoopChanged', 'debugAnimation'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickBulkValueAnimator::~QQuickBulkValueAnimator()': the
    destructor: Python never removes a C++ QQuickBulkValueAnimator.
  - Qt's 'void QQuickBulkValueAnimator::setFromIsSourcedValue(bool *value)':
    takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickBulkValueAnimator is created at the first use, not by
    'QQuickBulkValueAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBulkValueAnimator.
  - Each name of Qt's QQuickBulkValueAnimator that has no cute function yet,
    'setFromIsSourcedValue', holds a function that raises
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
  __qt_class__ = 'QQuickBulkValueAnimator'

  #  A C++ QQuickBulkValueAnimator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBulkValueAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getAnimValue(self) -> Optional[QQuickBulkValueUpdater]:
    """
    Calls Qt's 'QQuickBulkValueUpdater
    *QQuickBulkValueAnimator::getAnimValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#getAnimValue

    Returns
    -------

    Optional[QQuickBulkValueUpdater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickBulkValueUpdater *QQuickBulkValueAnimator::getAnimValue() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickBulkValueAnimator12getAnimValueEv',
    )
    from . import QQuickBulkValueUpdater
    return QQuickBulkValueUpdater._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickBulkValueAnimator::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#duration
    """
    #  int QQuickBulkValueAnimator::duration() const
    ritual = 'ritual_ZNK23QQuickBulkValueAnimator8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickBulkValueAnimator8durationEv'
    return self.uglySide.call(ritual)

  def easingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickBulkValueAnimator::easingCurve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#easingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickBulkValueAnimator::easingCurve() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickBulkValueAnimator11easingCurveEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickBulkValueUpdater)
  @overload(NoneType)
  def setAnimValue(self, value: Optional[QQuickBulkValueUpdater]) -> None:
    """
    Calls Qt's 'void
    QQuickBulkValueAnimator::setAnimValue(QQuickBulkValueUpdater *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#setAnimValue

    Parameters
    ----------

    value : Optional[QQuickBulkValueUpdater]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBulkValueAnimator::setAnimValue(QQuickBulkValueUpdater
    #      *value)
    self.uglySide.call(
        'ritual_ZN23QQuickBulkValueAnimator12setAnimValueEP22QQuickBulkValu'
        'eUpdater',
        self._addressOf(value),
    )

  @overload(int)
  def setDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void QQuickBulkValueAnimator::setDuration(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#setDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QQuickBulkValueAnimator::setDuration(int msecs)
    self.uglySide.call(
        'ritual_ZN23QQuickBulkValueAnimator11setDurationEi', msecs,
    )

  @overload(QEasingCurve)
  def setEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickBulkValueAnimator::setEasingCurve(const
    QEasingCurve &curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#setEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickBulkValueAnimator::setEasingCurve(const QEasingCurve
    #      &curve)
    self.uglySide.call(
        'ritual_ZN23QQuickBulkValueAnimator14setEasingCurveERK12QEasingCurv'
        'e',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickBulkValueAnimator::QQuickBulkValueAnimator()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html
    """
    #  QQuickBulkValueAnimator::QQuickBulkValueAnimator()
    self._noteCreation(QQuickBulkValueAnimator, lambda: Rituals.call(
        'ritual_ZN23QQuickBulkValueAnimatorC1Ev',
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

  @overload(int)
  def updateCurrentTime(self, currentTime: int) -> None:
    """
    Calls Qt's 'void QQuickBulkValueAnimator::updateCurrentTime(int
    currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#updateCurrentTime

    Parameters
    ----------

    currentTime : int
      Passed on as it is.
    """
    #  void QQuickBulkValueAnimator::updateCurrentTime(int currentTime)
    ritual = 'ritual_ZN23QQuickBulkValueAnimator17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickBulkValueAnimator17updateCurrentTimeEi'
    self.uglySide.call(ritual, currentTime)

  def topLevelAnimationLoopChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickBulkValueAnimator::topLevelAnimationLoopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html
    """
    #  void QQuickBulkValueAnimator::topLevelAnimationLoopChanged()
    ritual = (
        'ritual_ZN23QQuickBulkValueAnimator28topLevelAnimationLoopChangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickBulkValueAnimator28topLevelAnimationLoopCha'
          'ngedEv')
    self.uglySide.call(ritual)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QQuickBulkValueAnimator::debugAnimation(QDebug d)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbulkvalueanimator.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QQuickBulkValueAnimator::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK23QQuickBulkValueAnimator14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QQuickBulkValueAnimator14debugAnimationE6QDebug')
    self.uglySide.call(ritual, self._valueOf(d))

  @staticmethod
  def setFromIsSourcedValue(*__, **_) -> Never:
    """
    Qt's 'void QQuickBulkValueAnimator::setFromIsSourcedValue(bool *value)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickBulkValueAnimator.setFromIsSourcedValue' has no cute "
        "function yet. Qt's 'void "
        "QQuickBulkValueAnimator::setFromIsSourcedValue(bool *value)': "
        "takes a number to change where it is.")
