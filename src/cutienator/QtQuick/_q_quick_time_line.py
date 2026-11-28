"""
QQuickTimeLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTimeLine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QMetaObject
  from . import QQuickTimeLineCallback, QQuickTimeLineObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QQuickTimeLineCallback = WAIT['QQuickTimeLineCallback']
  QQuickTimeLineObject = WAIT['QQuickTimeLineObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTimeLine(QObject, QAbstractAnimationJob):
  """
  The cute side of Qt's QQuickTimeLine: a plain Python object standing in
  front of one C++ QQuickTimeLine.

  It is built on the cute 'QObject', as Qt's QQuickTimeLine is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QAbstractAnimationJob' as well, as Qt's QQuickTimeLine is built on Qt's
  QAbstractAnimationJob too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTimeLine that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'syncMode',
  'setSyncMode', 'callback', 'sync', 'setSyncPoint', 'syncPoint', 'complete',
  'clear', 'isActive', 'time', 'duration', 'updated', 'completed',
  'updateCurrentTime', 'debugAnimation', 'remove'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTimeLine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTimeLine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTimeLine::~QQuickTimeLine()': the destructor: Python never
    removes a C++ QQuickTimeLine.
  - Qt's 'void QQuickTimeLine::pause(QQuickTimeLineObject &a0, int a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTimeLine::set(QQuickTimeLineValue &a0, qreal a1)': takes
    a type Python has no way to hand over yet.
  - Qt's 'int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal velocity,
    qreal accel)': takes a type Python has no way to hand over yet.
  - Qt's 'int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal velocity,
    qreal accel, qreal maxDistance)': takes a type Python has no way to hand
    over yet.
  - Qt's 'int QQuickTimeLine::accelDistance(QQuickTimeLineValue &a0, qreal
    velocity, qreal distance)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal
    destination, int time)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal
    destination, const QEasingCurve &a2, int time)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal change,
    int time)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal change,
    const QEasingCurve &a2, int time)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQuickTimeLine::sync(QQuickTimeLineValue &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuickTimeLine::sync(QQuickTimeLineValue &a0,
    QQuickTimeLineValue &a1)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickTimeLine::reset(QQuickTimeLineValue &a0)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTimeLine is created at the first use, not by
    'QQuickTimeLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTimeLine.
  - Qt tells when it has removed the C++ QQuickTimeLine. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTimeLine that has no cute function yet, 'accel',
    'accelDistance', 'move', 'moveBy', 'reset', 'set', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickTimeLine, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SyncMode(CuteNum):
    """
    The enum 'QQuickTimeLine::SyncMode' of Qt, with the 2 names Qt gives in
    it.
    """

    LocalSync = Kee[int](0)
    GlobalSync = Kee[int](1)

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
    Calls Qt's 'QString QQuickTimeLine::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#tr

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
    #  QString QQuickTimeLine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickTimeLine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTimeLine'

  #  Qt's QQuickTimeLine is built on more than one class. The part of a C++
  #  QQuickTimeLine that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractAnimationJob':
          'ritual_cast_QQuickTimeLine_QAbstractAnimationJob',
  }

  #  A C++ QQuickTimeLine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTimeLine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTimeLine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTimeLine::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTimeLine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def syncMode(self) -> SyncMode:
    """
    Calls Qt's 'SyncMode QQuickTimeLine::syncMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#syncMode

    Returns
    -------

    SyncMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SyncMode(number)' gives.
    """
    #  SyncMode QQuickTimeLine::syncMode() const
    return QQuickTimeLine.SyncMode(self.uglySide.call(
        'ritual_ZNK14QQuickTimeLine8syncModeEv',
    ))

  def syncPoint(self) -> int:
    """
    Calls Qt's 'int QQuickTimeLine::syncPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#syncPoint
    """
    #  int QQuickTimeLine::syncPoint() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeLine9syncPointEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickTimeLine::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#isActive
    """
    #  bool QQuickTimeLine::isActive() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeLine8isActiveEv')

  def time(self) -> int:
    """
    Calls Qt's 'int QQuickTimeLine::time() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#time
    """
    #  int QQuickTimeLine::time() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeLine4timeEv')

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickTimeLine::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#duration
    """
    #  int QQuickTimeLine::duration() const
    ritual = 'ritual_ZNK14QQuickTimeLine8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTimeLine8durationEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SyncMode)
  def setSyncMode(self, a0: SyncMode) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::setSyncMode(SyncMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#setSyncMode

    Parameters
    ----------

    a0 : SyncMode
      Passed on as its number.
    """
    #  void QQuickTimeLine::setSyncMode(SyncMode a0)
    self.uglySide.call(
        'ritual_ZN14QQuickTimeLine11setSyncModeENS_8SyncModeE', a0.value,
    )

  @overload(int)
  def setSyncPoint(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::setSyncPoint(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#setSyncPoint

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickTimeLine::setSyncPoint(int a0)
    self.uglySide.call('ritual_ZN14QQuickTimeLine12setSyncPointEi', a0)

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
    Notes what was given, for Qt's 'QQuickTimeLine::QQuickTimeLine(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#QQuickTimeLine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTimeLine::QQuickTimeLine(QObject *parent)
    self._noteCreation(QQuickTimeLine, lambda: Rituals.call(
        'ritual_ZN14QQuickTimeLineC1EP7QObject',
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

  @overload(QQuickTimeLineCallback)
  def callback(self, a0: QQuickTimeLineCallback) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::callback(const QQuickTimeLineCallback
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#callback

    Parameters
    ----------

    a0 : QQuickTimeLineCallback
      Passed on as a value: Qt reads the C++ QQuickTimeLineCallback, which
      stays Python's own.
    """
    #  void QQuickTimeLine::callback(const QQuickTimeLineCallback &a0)
    self.uglySide.call(
        'ritual_ZN14QQuickTimeLine8callbackERK22QQuickTimeLineCallback',
        self._valueOf(a0),
    )

  def sync(self) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#sync
    """
    #  void QQuickTimeLine::sync()
    self.uglySide.call('ritual_ZN14QQuickTimeLine4syncEv')

  def complete(self) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::complete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#complete
    """
    #  void QQuickTimeLine::complete()
    self.uglySide.call('ritual_ZN14QQuickTimeLine8completeEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#clear
    """
    #  void QQuickTimeLine::clear()
    self.uglySide.call('ritual_ZN14QQuickTimeLine5clearEv')

  def updated(self) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#updated
    """
    #  void QQuickTimeLine::updated()
    self.uglySide.call('ritual_ZN14QQuickTimeLine7updatedEv')

  def completed(self) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::completed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#completed
    """
    #  void QQuickTimeLine::completed()
    self.uglySide.call('ritual_ZN14QQuickTimeLine9completedEv')

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimeline.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickTimeLine::updateCurrentTime(int a0)
    ritual = 'ritual_ZN14QQuickTimeLine17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTimeLine17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::debugAnimation(QDebug d) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QQuickTimeLine::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK14QQuickTimeLine14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTimeLine14debugAnimationE6QDebug'
    self.uglySide.call(ritual, self._valueOf(d))

  @overload(QQuickTimeLineObject)
  @overload(NoneType)
  def remove(self, a0: Optional[QQuickTimeLineObject]) -> None:
    """
    Calls Qt's 'void QQuickTimeLine::remove(QQuickTimeLineObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#remove

    Parameters
    ----------

    a0 : Optional[QQuickTimeLineObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTimeLine::remove(QQuickTimeLineObject *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickTimeLine6removeEP20QQuickTimeLineObject',
        self._addressOf(a0),
    )

  @staticmethod
  def accel(*__, **_) -> Never:
    """
    - Qt's 'int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal
      velocity, qreal accel)': takes a type Python has no way to hand over
      yet.
    - Qt's 'int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal
      velocity, qreal accel, qreal maxDistance)': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTimeLine.accel' has no cute function yet. Qt's 'int "
        "QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal velocity, "
        "qreal accel)': takes a type Python has no way to hand over yet. "
        "Qt's 'int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal "
        "velocity, qreal accel, qreal maxDistance)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def accelDistance(*__, **_) -> Never:
    """
    Qt's 'int QQuickTimeLine::accelDistance(QQuickTimeLineValue &a0, qreal
    velocity, qreal distance)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickTimeLine.accelDistance' has no cute function yet. Qt's 'int "
        "QQuickTimeLine::accelDistance(QQuickTimeLineValue &a0, qreal "
        "velocity, qreal distance)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def move(*__, **_) -> Never:
    """
    - Qt's 'void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal
      destination, int time)': takes a type Python has no way to hand over
      yet.
    - Qt's 'void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal
      destination, const QEasingCurve &a2, int time)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTimeLine.move' has no cute function yet. Qt's 'void "
        "QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal destination, "
        "int time)': takes a type Python has no way to hand over yet. Qt's "
        "'void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal "
        "destination, const QEasingCurve &a2, int time)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def moveBy(*__, **_) -> Never:
    """
    - Qt's 'void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal
      change, int time)': takes a type Python has no way to hand over yet.
    - Qt's 'void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal
      change, const QEasingCurve &a2, int time)': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTimeLine.moveBy' has no cute function yet. Qt's 'void "
        "QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal change, int "
        "time)': takes a type Python has no way to hand over yet. Qt's "
        "'void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal "
        "change, const QEasingCurve &a2, int time)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def reset(*__, **_) -> Never:
    """
    Qt's 'void QQuickTimeLine::reset(QQuickTimeLineValue &a0)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTimeLine.reset' has no cute function yet. Qt's 'void "
        "QQuickTimeLine::reset(QQuickTimeLineValue &a0)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def set(*__, **_) -> Never:
    """
    Qt's 'void QQuickTimeLine::set(QQuickTimeLineValue &a0, qreal a1)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTimeLine.set' has no cute function yet. Qt's 'void "
        "QQuickTimeLine::set(QQuickTimeLineValue &a0, qreal a1)': takes a "
        "type Python has no way to hand over yet.")
