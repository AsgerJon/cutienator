"""
QQuickSwitch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswitch_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwitch to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickAbstractButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QMouseEvent, QTouchEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwitch(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickSwitch: a plain Python object standing in front
  of one C++ QQuickSwitch.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickSwitch is
  built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwitch that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'position',
  'setPosition', 'visualPosition', 'positionChanged',
  'visualPositionChanged', 'mouseMoveEvent', 'touchEvent', 'mirrorChange',
  'nextCheckState', 'defaultFont'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwitch::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSwitch::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSwitch::buttonChange(ButtonChange change)': names the
    enum 'QQuickAbstractButton::ButtonChange', whose class cannot be named
    here.
  - Qt's 'QQuickSwitchPrivate *QQuickSwitch::d_func()': gives
    'QQuickSwitchPrivate', which has no cute class yet.
  - Qt's 'const QQuickSwitchPrivate *QQuickSwitch::d_func() const': gives
    'QQuickSwitchPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwitch is created at the first use, not by
    'QQuickSwitch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwitch.
  - Qt tells when it has removed the C++ QQuickSwitch. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QQuickSwitch::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#tr

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
    #  QString QQuickSwitch::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickSwitch2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwitch'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwitch::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwitch::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickSwitch10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickSwitch::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#position
    """
    #  qreal QQuickSwitch::position() const
    return self.uglySide.call('ritual_ZNK12QQuickSwitch8positionEv')

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickSwitch::visualPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#visualPosition
    """
    #  qreal QQuickSwitch::visualPosition() const
    return self.uglySide.call('ritual_ZNK12QQuickSwitch14visualPositionEv')

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickSwitch::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickSwitch::defaultFont() const
    ritual = 'ritual_ZNK12QQuickSwitch11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickSwitch11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void QQuickSwitch::setPosition(qreal position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void QQuickSwitch::setPosition(qreal position)
    self.uglySide.call('ritual_ZN12QQuickSwitch11setPositionEd', position)

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
    Notes what was given, for Qt's 'QQuickSwitch::QQuickSwitch(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#QQuickSwitch

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSwitch::QQuickSwitch(QQuickItem *parent)
    self._noteCreation(QQuickSwitch, lambda: Rituals.call(
        'ritual_ZN12QQuickSwitchC1EP10QQuickItem', self._addressOf(parent),
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwitch::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#positionChanged
    """
    #  void QQuickSwitch::positionChanged()
    self.uglySide.call('ritual_ZN12QQuickSwitch15positionChangedEv')

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwitch::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitch.html#visualPositionChanged
    """
    #  void QQuickSwitch::visualPositionChanged()
    self.uglySide.call('ritual_ZN12QQuickSwitch21visualPositionChangedEv')

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwitch::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwitch::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN12QQuickSwitch14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSwitch14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwitch::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwitch::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN12QQuickSwitch10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSwitch10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickSwitch::mirrorChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#mirrorChange
    """
    #  void QQuickSwitch::mirrorChange()
    ritual = 'ritual_ZN12QQuickSwitch12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSwitch12mirrorChangeEv'
    self.uglySide.call(ritual)

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QQuickSwitch::nextCheckState()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitch.html#nextCheckState
    """
    #  void QQuickSwitch::nextCheckState()
    ritual = 'ritual_ZN12QQuickSwitch14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSwitch14nextCheckStateEv'
    self.uglySide.call(ritual)
