"""
QQuickAnimatorJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnimatorJob to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQml import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug, QEasingCurve
  from . import QQuickAnimatorController, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QEasingCurve = WAIT['QEasingCurve']
  QQuickAnimatorController = WAIT['QQuickAnimatorController']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatorJob(QAbstractAnimationJob):
  """
  The cute side of Qt's QQuickAnimatorJob: a plain Python object standing in
  front of one C++ QQuickAnimatorJob.

  It is built on the cute 'QAbstractAnimationJob', as Qt's QQuickAnimatorJob
  is built on Qt's QAbstractAnimationJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatorJob that has a ritual and that Python
  can call so far, 23 names in all: 'setTarget', 'target', 'setFrom',
  'from_', 'setTo', 'to', 'setDuration', 'duration', 'easingCurve',
  'setEasingCurve', 'initialize', 'invalidate', 'writeBack', 'preSync',
  'postSync', 'commit', 'isTransform', 'isUniform', 'value', 'controller',
  'debugAnimation', 'progress', 'boundValue'. It can be made from Python, in
  1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickAnimatorJob is created at the first use, not by
    'QQuickAnimatorJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatorJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatorJob'

  #  A C++ QQuickAnimatorJob Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimatorJob'

  #  The functions Qt calls itself that QQuickAnimatorJob is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setTarget': (
          ('_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'initialize': (
          ('_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorController',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickAnimatorController'),
           )),
      ),
      'invalidate': (
          ('_ZN17QQuickAnimatorJob10invalidateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'writeBack': (
          ('_ZN17QQuickAnimatorJob9writeBackEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'preSync': (
          ('_ZN17QQuickAnimatorJob7preSyncEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'postSync': (
          ('_ZN17QQuickAnimatorJob8postSyncEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'commit': (
          ('_ZN17QQuickAnimatorJob6commitEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAnimatorJob::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAnimatorJob::target() const
    address = self.uglySide.call('ritual_ZNK17QQuickAnimatorJob6targetEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimatorJob::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#from
    """
    #  qreal QQuickAnimatorJob::from() const
    return self.uglySide.call('ritual_ZNK17QQuickAnimatorJob4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimatorJob::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#to
    """
    #  qreal QQuickAnimatorJob::to() const
    return self.uglySide.call('ritual_ZNK17QQuickAnimatorJob2toEv')

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatorJob::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#duration
    """
    #  int QQuickAnimatorJob::duration() const
    ritual = 'ritual_ZNK17QQuickAnimatorJob8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickAnimatorJob8durationEv'
    return self.uglySide.call(ritual)

  def easingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickAnimatorJob::easingCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#easingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickAnimatorJob::easingCurve() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickAnimatorJob11easingCurveEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def isTransform(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatorJob::isTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#isTransform
    """
    #  bool QQuickAnimatorJob::isTransform() const
    return self.uglySide.call('ritual_ZNK17QQuickAnimatorJob11isTransformEv')

  def isUniform(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatorJob::isUniform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#isUniform
    """
    #  bool QQuickAnimatorJob::isUniform() const
    return self.uglySide.call('ritual_ZNK17QQuickAnimatorJob9isUniformEv')

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimatorJob::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#value
    """
    #  qreal QQuickAnimatorJob::value() const
    return self.uglySide.call('ritual_ZNK17QQuickAnimatorJob5valueEv')

  def controller(self) -> Optional[QQuickAnimatorController]:
    """
    Calls Qt's 'QQuickAnimatorController *QQuickAnimatorJob::controller()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#controller

    Returns
    -------

    Optional[QQuickAnimatorController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatorController *QQuickAnimatorJob::controller() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickAnimatorJob10controllerEv',
    )
    from . import QQuickAnimatorController
    return QQuickAnimatorController._cuteAt(address)

  @overload(int)
  def progress(self, time: int) -> float:
    """
    Calls Qt's 'qreal QQuickAnimatorJob::progress(int time) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#progress

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  qreal QQuickAnimatorJob::progress(int time) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickAnimatorJob8progressEi', time,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::setTarget(QQuickItem *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#setTarget

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatorJob::setTarget(QQuickItem *target)
    ritual = 'ritual_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(target))

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::setFrom(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickAnimatorJob::setFrom(qreal from)
    self.uglySide.call('ritual_ZN17QQuickAnimatorJob7setFromEd', from_)

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::setTo(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickAnimatorJob::setTo(qreal to)
    self.uglySide.call('ritual_ZN17QQuickAnimatorJob5setToEd', to)

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::setDuration(int duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuickAnimatorJob::setDuration(int duration)
    self.uglySide.call(
        'ritual_ZN17QQuickAnimatorJob11setDurationEi', duration,
    )

  @overload(QEasingCurve)
  def setEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::setEasingCurve(const QEasingCurve
    &curve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorjob.html#setEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickAnimatorJob::setEasingCurve(const QEasingCurve &curve)
    self.uglySide.call(
        'ritual_ZN17QQuickAnimatorJob14setEasingCurveERK12QEasingCurve',
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
    Notes what was given, for Qt's 'QQuickAnimatorJob::QQuickAnimatorJob()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorjob.html#QQuickAnimatorJob
    """
    #  QQuickAnimatorJob::QQuickAnimatorJob()
    self._noteCreation(QQuickAnimatorJob, lambda: Rituals.call(
        'ritual_ZN17QQuickAnimatorJobC1Ev',
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

  @overload(QQuickAnimatorController)
  @overload(NoneType)
  def initialize(
      self,
      controller: Optional[QQuickAnimatorController],
  ) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::initialize(QQuickAnimatorController
    *controller)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#initialize

    Parameters
    ----------

    controller : Optional[QQuickAnimatorController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatorJob::initialize(QQuickAnimatorController
    #      *controller)
    ritual = (
        'ritual_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorControll'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorCo'
          'ntroller')
    self.uglySide.call(ritual, self._addressOf(controller))

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#invalidate
    """
    #  void QQuickAnimatorJob::invalidate()
    self.uglySide.call('ritual_ZN17QQuickAnimatorJob10invalidateEv')

  def writeBack(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::writeBack()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#writeBack
    """
    #  void QQuickAnimatorJob::writeBack()
    self.uglySide.call('ritual_ZN17QQuickAnimatorJob9writeBackEv')

  def preSync(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::preSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#preSync
    """
    #  void QQuickAnimatorJob::preSync()
    ritual = 'ritual_ZN17QQuickAnimatorJob7preSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickAnimatorJob7preSyncEv'
    self.uglySide.call(ritual)

  def postSync(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::postSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#postSync
    """
    #  void QQuickAnimatorJob::postSync()
    ritual = 'ritual_ZN17QQuickAnimatorJob8postSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickAnimatorJob8postSyncEv'
    self.uglySide.call(ritual)

  def commit(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#commit
    """
    #  void QQuickAnimatorJob::commit()
    ritual = 'ritual_ZN17QQuickAnimatorJob6commitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickAnimatorJob6commitEv'
    self.uglySide.call(ritual)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::debugAnimation(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorjob.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QQuickAnimatorJob::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK17QQuickAnimatorJob14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickAnimatorJob14debugAnimationE6QDebug'
    self.uglySide.call(ritual, self._valueOf(d))

  def boundValue(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatorJob::boundValue()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorjob.html#boundValue
    """
    #  void QQuickAnimatorJob::boundValue()
    self.uglySide.call('ritual_ZN17QQuickAnimatorJob10boundValueEv')
