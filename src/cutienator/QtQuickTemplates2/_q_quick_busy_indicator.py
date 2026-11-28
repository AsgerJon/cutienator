"""
QQuickBusyIndicator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbusyindicator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickBusyIndicator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QTouchEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBusyIndicator(QQuickControl):
  """
  The cute side of Qt's QQuickBusyIndicator: a plain Python object standing
  in front of one C++ QQuickBusyIndicator.

  It is built on the cute 'QQuickControl', as Qt's QQuickBusyIndicator is
  built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBusyIndicator that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'isRunning',
  'setRunning', 'runningChanged', 'touchEvent', 'accessibleRole'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBusyIndicator::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickBusyIndicator::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickBusyIndicatorPrivate *QQuickBusyIndicator::d_func()': gives
    'QQuickBusyIndicatorPrivate', which has no cute class yet.
  - Qt's 'const QQuickBusyIndicatorPrivate *QQuickBusyIndicator::d_func()
    const': gives 'QQuickBusyIndicatorPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickBusyIndicator is created at the first use, not by
    'QQuickBusyIndicator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBusyIndicator.
  - Qt tells when it has removed the C++ QQuickBusyIndicator. Every call on
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
    Calls Qt's 'QString QQuickBusyIndicator::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbusyindicator.html#tr

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
    #  QString QQuickBusyIndicator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickBusyIndicator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBusyIndicator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBusyIndicator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbusyindicator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBusyIndicator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickBusyIndicator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickBusyIndicator::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbusyindicator.html#isRunning
    """
    #  bool QQuickBusyIndicator::isRunning() const
    return self.uglySide.call('ritual_ZNK19QQuickBusyIndicator9isRunningEv')

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickBusyIndicator::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbusyindicator.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickBusyIndicator::accessibleRole() const
    ritual = 'ritual_ZNK19QQuickBusyIndicator14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickBusyIndicator14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QQuickBusyIndicator::setRunning(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbusyindicator.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQuickBusyIndicator::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN19QQuickBusyIndicator10setRunningEb', running,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickBusyIndicator::QQuickBusyIndicator(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbusyindicator.html#QQuickBusyIndicator

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickBusyIndicator::QQuickBusyIndicator(QQuickItem *parent)
    self._noteCreation(QQuickBusyIndicator, lambda: Rituals.call(
        'ritual_ZN19QQuickBusyIndicatorC1EP10QQuickItem',
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

  def runningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBusyIndicator::runningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbusyindicator.html#runningChanged
    """
    #  void QQuickBusyIndicator::runningChanged()
    self.uglySide.call('ritual_ZN19QQuickBusyIndicator14runningChangedEv')

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickBusyIndicator::touchEvent(QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbusyindicator.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBusyIndicator::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN19QQuickBusyIndicator10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickBusyIndicator10touchEventEP11QTouchEvent')
    self.uglySide.call(ritual, self._addressOf(event))
