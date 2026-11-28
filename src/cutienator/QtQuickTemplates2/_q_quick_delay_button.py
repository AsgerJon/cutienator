"""
QQuickDelayButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdelaybutton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDelayButton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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
  from ..QtGui import QFont
  from ..QtQuick import QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTransition = WAIT['QQuickTransition']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDelayButton(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickDelayButton: a plain Python object standing in
  front of one C++ QQuickDelayButton.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickDelayButton
  is built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDelayButton that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'delay', 'setDelay',
  'progress', 'setProgress', 'transition', 'setTransition', 'activated',
  'delayChanged', 'progressChanged', 'transitionChanged', 'nextCheckState',
  'defaultFont'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDelayButton::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickDelayButton::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDelayButton::buttonChange(ButtonChange change)': names
    the enum 'QQuickAbstractButton::ButtonChange', whose class cannot be
    named here.
  - Qt's 'QQuickDelayButtonPrivate *QQuickDelayButton::d_func()': gives
    'QQuickDelayButtonPrivate', which has no cute class yet.
  - Qt's 'const QQuickDelayButtonPrivate *QQuickDelayButton::d_func() const':
    gives 'QQuickDelayButtonPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDelayButton is created at the first use, not by
    'QQuickDelayButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDelayButton.
  - Qt tells when it has removed the C++ QQuickDelayButton. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickDelayButton::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#tr

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
    #  QString QQuickDelayButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickDelayButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDelayButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDelayButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDelayButton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickDelayButton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def delay(self) -> int:
    """
    Calls Qt's 'int QQuickDelayButton::delay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#delay
    """
    #  int QQuickDelayButton::delay() const
    return self.uglySide.call('ritual_ZNK17QQuickDelayButton5delayEv')

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickDelayButton::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#progress
    """
    #  qreal QQuickDelayButton::progress() const
    return self.uglySide.call('ritual_ZNK17QQuickDelayButton8progressEv')

  def transition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickDelayButton::transition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#transition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickDelayButton::transition() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickDelayButton10transitionEv',
    )
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickDelayButton::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickDelayButton::defaultFont() const
    ritual = 'ritual_ZNK17QQuickDelayButton11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickDelayButton11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::setDelay(int delay)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#setDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickDelayButton::setDelay(int delay)
    self.uglySide.call('ritual_ZN17QQuickDelayButton8setDelayEi', delay)

  @overload(float)
  def setProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::setProgress(qreal progress)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickDelayButton::setProgress(qreal progress)
    self.uglySide.call(
        'ritual_ZN17QQuickDelayButton11setProgressEd', progress,
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setTransition(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::setTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdelaybutton.html#setTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDelayButton::setTransition(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN17QQuickDelayButton13setTransitionEP16QQuickTransition',
        self._addressOf(transition),
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
    'QQuickDelayButton::QQuickDelayButton(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdelaybutton.html#QQuickDelayButton

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDelayButton::QQuickDelayButton(QQuickItem *parent)
    self._noteCreation(QQuickDelayButton, lambda: Rituals.call(
        'ritual_ZN17QQuickDelayButtonC1EP10QQuickItem',
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

  def activated(self) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::activated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdelaybutton.html#activated
    """
    #  void QQuickDelayButton::activated()
    self.uglySide.call('ritual_ZN17QQuickDelayButton9activatedEv')

  def delayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::delayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdelaybutton.html#delayChanged
    """
    #  void QQuickDelayButton::delayChanged()
    self.uglySide.call('ritual_ZN17QQuickDelayButton12delayChangedEv')

  def progressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::progressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdelaybutton.html#progressChanged
    """
    #  void QQuickDelayButton::progressChanged()
    self.uglySide.call('ritual_ZN17QQuickDelayButton15progressChangedEv')

  def transitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::transitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdelaybutton.html#transitionChanged
    """
    #  void QQuickDelayButton::transitionChanged()
    self.uglySide.call('ritual_ZN17QQuickDelayButton17transitionChangedEv')

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QQuickDelayButton::nextCheckState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdelaybutton.html#nextCheckState
    """
    #  void QQuickDelayButton::nextCheckState()
    ritual = 'ritual_ZN17QQuickDelayButton14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickDelayButton14nextCheckStateEv'
    self.uglySide.call(ritual)
