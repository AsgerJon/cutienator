"""
QLineEditIconButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLineEditIconButton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QToolButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QActionEvent, QPaintEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QActionEvent = WAIT['QActionEvent']
  QPaintEvent = WAIT['QPaintEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLineEditIconButton(QToolButton):
  """
  The cute side of Qt's QLineEditIconButton: a plain Python object standing
  in front of one C++ QLineEditIconButton.

  It is built on the cute 'QToolButton', as Qt's QLineEditIconButton is built
  on Qt's QToolButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLineEditIconButton that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'opacity',
  'setOpacity', 'shouldHideWithText', 'setHideWithText', 'needsSpace',
  'actionEvent', 'paintEvent', 'updateCursor', 'onAnimationFinished'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  9 of the 19 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 leans on 'QLineEditIconButton; 1 a template; 1 declared and
  nowhere to be found; 1 leans on 'vtable for QLineEditIconButton', which
  Qt's library does not offer and Qt's source has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QLineEditIconButton is created at the first use, not by
    'QLineEditIconButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLineEditIconButton.
  - Qt tells when it has removed the C++ QLineEditIconButton. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLineEditIconButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLineEditIconButton::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLineEditIconButton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QLineEditIconButton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QLineEditIconButton::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineediticonbutton.html#opacity
    """
    #  qreal QLineEditIconButton::opacity() const
    return self.uglySide.call('ritual_ZNK19QLineEditIconButton7opacityEv')

  def shouldHideWithText(self) -> bool:
    """
    Calls Qt's 'bool QLineEditIconButton::shouldHideWithText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#shouldHideWithText
    """
    #  bool QLineEditIconButton::shouldHideWithText() const
    return self.uglySide.call(
        'ritual_ZNK19QLineEditIconButton18shouldHideWithTextEv',
    )

  def needsSpace(self) -> bool:
    """
    Calls Qt's 'bool QLineEditIconButton::needsSpace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#needsSpace
    """
    #  bool QLineEditIconButton::needsSpace() const
    return self.uglySide.call(
        'ritual_ZNK19QLineEditIconButton10needsSpaceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setOpacity(self, value: float) -> None:
    """
    Calls Qt's 'void QLineEditIconButton::setOpacity(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#setOpacity

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QLineEditIconButton::setOpacity(qreal value)
    self.uglySide.call('ritual_ZN19QLineEditIconButton10setOpacityEd', value)

  @overload(bool)
  def setHideWithText(self, hide: bool) -> None:
    """
    Calls Qt's 'void QLineEditIconButton::setHideWithText(bool hide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#setHideWithText

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QLineEditIconButton::setHideWithText(bool hide)
    self.uglySide.call(
        'ritual_ZN19QLineEditIconButton15setHideWithTextEb', hide,
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

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, e: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QLineEditIconButton::actionEvent(QActionEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#actionEvent

    Parameters
    ----------

    e : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLineEditIconButton::actionEvent(QActionEvent *e)
    ritual = 'ritual_ZN19QLineEditIconButton11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QLineEditIconButton11actionEventEP12QActionEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QLineEditIconButton::paintEvent(QPaintEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLineEditIconButton::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN19QLineEditIconButton10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QLineEditIconButton10paintEventEP11QPaintEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def updateCursor(self) -> None:
    """
    Calls Qt's 'void QLineEditIconButton::updateCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#updateCursor
    """
    #  void QLineEditIconButton::updateCursor()
    self.uglySide.call('ritual_ZN19QLineEditIconButton12updateCursorEv')

  def onAnimationFinished(self) -> None:
    """
    Calls Qt's 'void QLineEditIconButton::onAnimationFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineediticonbutton.html#onAnimationFinished
    """
    #  void QLineEditIconButton::onAnimationFinished()
    self.uglySide.call(
        'ritual_ZN19QLineEditIconButton19onAnimationFinishedEv',
    )
