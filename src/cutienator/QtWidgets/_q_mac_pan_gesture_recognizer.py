"""
QMacPanGestureRecognizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmacgesturerecognizer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QMacPanGestureRecognizer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGestureRecognizer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QTimerEvent
  from . import QGesture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QGesture = WAIT['QGesture']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMacPanGestureRecognizer(QObject, QGestureRecognizer):
  """
  The cute side of Qt's QMacPanGestureRecognizer: a plain Python object
  standing in front of one C++ QMacPanGestureRecognizer.

  It is built on the cute 'QObject', as Qt's QMacPanGestureRecognizer is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QGestureRecognizer' as well, as Qt's QMacPanGestureRecognizer is
  built on Qt's QGestureRecognizer too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMacPanGestureRecognizer that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'create',
  'recognize', 'reset', 'timerEvent'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMacPanGestureRecognizer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QMacPanGestureRecognizer::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QMacPanGestureRecognizer is created at the first use, not by
    'QMacPanGestureRecognizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMacPanGestureRecognizer.
  - Qt tells when it has removed the C++ QMacPanGestureRecognizer. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QMacPanGestureRecognizer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmacpangesturerecognizer.html#tr

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
    #  QString QMacPanGestureRecognizer::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QMacPanGestureRecognizer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMacPanGestureRecognizer'

  #  Qt's QMacPanGestureRecognizer is built on more than one class. The part
  #  of a C++ QMacPanGestureRecognizer that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGestureRecognizer':
          'ritual_cast_QMacPanGestureRecognizer_QGestureRecognizer',
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
    Calls Qt's 'const QMetaObject *QMacPanGestureRecognizer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmacpangesturerecognizer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMacPanGestureRecognizer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QMacPanGestureRecognizer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QMacPanGestureRecognizer::QMacPanGestureRecognizer()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmacpangesturerecognizer.html
    """
    #  QMacPanGestureRecognizer::QMacPanGestureRecognizer()
    self._noteCreation(QMacPanGestureRecognizer, lambda: Rituals.call(
        'ritual_ZN24QMacPanGestureRecognizerC1Ev',
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

  @overload(QObject)
  @overload(NoneType)
  def create(self, target: Optional[QObject]) -> Optional[QGesture]:
    """
    Calls Qt's 'QGesture *QMacPanGestureRecognizer::create(QObject *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmacpangesturerecognizer.html#create

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGesture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGesture *QMacPanGestureRecognizer::create(QObject *target)
    ritual = 'ritual_ZN24QMacPanGestureRecognizer6createEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QMacPanGestureRecognizer6createEP7QObject'
    address = self.uglySide.call(ritual, self._addressOf(target, 'QObject'))
    from . import QGesture
    return QGesture._cuteAt(address)

  @overload(QGesture, QObject, QEvent)
  @overload(QGesture, QObject, NoneType)
  @overload(QGesture, NoneType, QEvent)
  @overload(QGesture, NoneType, NoneType)
  @overload(NoneType, QObject, QEvent)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QEvent)
  @overload(NoneType, NoneType, NoneType)
  def recognize(
      self,
      gesture: Optional[QGesture],
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> QGestureRecognizer.Result:
    """
    Calls Qt's 'QGestureRecognizer::Result
    QMacPanGestureRecognizer::recognize(QGesture *gesture, QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmacpangesturerecognizer.html#recognize

    Parameters
    ----------

    gesture : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QGestureRecognizer.Result
      The value standing for the combination Qt gave back.
    """
    #  QGestureRecognizer::Result
    #      QMacPanGestureRecognizer::recognize(QGesture *gesture, QObject
    #      *watched, QEvent *event)
    ritual = (
        'ritual_ZN24QMacPanGestureRecognizer9recognizeEP8QGestureP7QObjectP'
        '6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QMacPanGestureRecognizer9recognizeEP8QGestureP7QO'
          'bjectP6QEvent')
    return QGestureRecognizer.Result(self.uglySide.call(
        ritual,
        self._addressOf(gesture), self._addressOf(watched, 'QObject'),
        self._addressOf(event),
    ))

  @overload(QGesture)
  @overload(NoneType)
  def reset(self, gesture: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QMacPanGestureRecognizer::reset(QGesture *gesture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmacpangesturerecognizer.html#reset

    Parameters
    ----------

    gesture : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMacPanGestureRecognizer::reset(QGesture *gesture)
    ritual = 'ritual_ZN24QMacPanGestureRecognizer5resetEP8QGesture'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QMacPanGestureRecognizer5resetEP8QGesture'
    self.uglySide.call(ritual, self._addressOf(gesture))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, ev: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMacPanGestureRecognizer::timerEvent(QTimerEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmacpangesturerecognizer.html#timerEvent

    Parameters
    ----------

    ev : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMacPanGestureRecognizer::timerEvent(QTimerEvent *ev)
    ritual = 'ritual_ZN24QMacPanGestureRecognizer10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QMacPanGestureRecognizer10timerEventEP11QTimerEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(ev))
