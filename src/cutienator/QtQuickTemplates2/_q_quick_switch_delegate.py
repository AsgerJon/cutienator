"""
QQuickSwitchDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswitchdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwitchDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickItemDelegate

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


class QQuickSwitchDelegate(QQuickItemDelegate):
  """
  The cute side of Qt's QQuickSwitchDelegate: a plain Python object standing
  in front of one C++ QQuickSwitchDelegate.

  It is built on the cute 'QQuickItemDelegate', as Qt's QQuickSwitchDelegate
  is built on Qt's QQuickItemDelegate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwitchDelegate that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'position',
  'setPosition', 'visualPosition', 'positionChanged',
  'visualPositionChanged', 'mouseMoveEvent', 'touchEvent', 'defaultFont',
  'mirrorChange', 'nextCheckState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwitchDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSwitchDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSwitchDelegate::buttonChange(ButtonChange change)':
    names the enum 'QQuickAbstractButton::ButtonChange', whose class cannot
    be named here.
  - Qt's 'QQuickSwitchDelegatePrivate *QQuickSwitchDelegate::d_func()': gives
    'QQuickSwitchDelegatePrivate', which has no cute class yet.
  - Qt's 'const QQuickSwitchDelegatePrivate *QQuickSwitchDelegate::d_func()
    const': gives 'QQuickSwitchDelegatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwitchDelegate is created at the first use, not by
    'QQuickSwitchDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwitchDelegate.
  - Qt tells when it has removed the C++ QQuickSwitchDelegate. Every call on
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
    Calls Qt's 'QString QQuickSwitchDelegate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitchdelegate.html#tr

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
    #  QString QQuickSwitchDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickSwitchDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwitchDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwitchDelegate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwitchDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickSwitchDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickSwitchDelegate::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswitchdelegate.html#position
    """
    #  qreal QQuickSwitchDelegate::position() const
    return self.uglySide.call('ritual_ZNK20QQuickSwitchDelegate8positionEv')

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickSwitchDelegate::visualPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#visualPosition
    """
    #  qreal QQuickSwitchDelegate::visualPosition() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickSwitchDelegate14visualPositionEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickSwitchDelegate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickSwitchDelegate::defaultFont() const
    ritual = 'ritual_ZNK20QQuickSwitchDelegate11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickSwitchDelegate11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::setPosition(qreal position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void QQuickSwitchDelegate::setPosition(qreal position)
    self.uglySide.call(
        'ritual_ZN20QQuickSwitchDelegate11setPositionEd', position,
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
    'QQuickSwitchDelegate::QQuickSwitchDelegate(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#QQuickSwitchDelegate

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSwitchDelegate::QQuickSwitchDelegate(QQuickItem *parent)
    self._noteCreation(QQuickSwitchDelegate, lambda: Rituals.call(
        'ritual_ZN20QQuickSwitchDelegateC1EP10QQuickItem',
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#positionChanged
    """
    #  void QQuickSwitchDelegate::positionChanged()
    self.uglySide.call('ritual_ZN20QQuickSwitchDelegate15positionChangedEv')

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#visualPositionChanged
    """
    #  void QQuickSwitchDelegate::visualPositionChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickSwitchDelegate21visualPositionChangedEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::mouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwitchDelegate::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN20QQuickSwitchDelegate14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickSwitchDelegate14mouseMoveEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::touchEvent(QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwitchDelegate::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN20QQuickSwitchDelegate10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickSwitchDelegate10touchEventEP11QTouchEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#mirrorChange
    """
    #  void QQuickSwitchDelegate::mirrorChange()
    ritual = 'ritual_ZN20QQuickSwitchDelegate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickSwitchDelegate12mirrorChangeEv'
    self.uglySide.call(ritual)

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QQuickSwitchDelegate::nextCheckState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswitchdelegate.html#nextCheckState
    """
    #  void QQuickSwitchDelegate::nextCheckState()
    ritual = 'ritual_ZN20QQuickSwitchDelegate14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickSwitchDelegate14nextCheckStateEv'
    self.uglySide.call(ritual)
