"""
QQuickProgressBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickprogressbar_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickProgressBar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickProgressBar(QQuickControl):
  """
  The cute side of Qt's QQuickProgressBar: a plain Python object standing in
  front of one C++ QQuickProgressBar.

  It is built on the cute 'QQuickControl', as Qt's QQuickProgressBar is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickProgressBar that has a ritual and that Python
  can call so far, 21 names in all: 'metaObject', 'tr', 'from_', 'setFrom',
  'to', 'setTo', 'value', 'setValue', 'position', 'visualPosition',
  'isIndeterminate', 'setIndeterminate', 'fromChanged', 'toChanged',
  'valueChanged', 'positionChanged', 'visualPositionChanged',
  'indeterminateChanged', 'mirrorChange', 'componentComplete',
  'accessibleRole'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickProgressBar::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickProgressBar::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickProgressBarPrivate *QQuickProgressBar::d_func()': gives
    'QQuickProgressBarPrivate', which has no cute class yet.
  - Qt's 'const QQuickProgressBarPrivate *QQuickProgressBar::d_func() const':
    gives 'QQuickProgressBarPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickProgressBar is created at the first use, not by
    'QQuickProgressBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickProgressBar.
  - Qt tells when it has removed the C++ QQuickProgressBar. Every call on the
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
    Calls Qt's 'QString QQuickProgressBar::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#tr

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
    #  QString QQuickProgressBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickProgressBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickProgressBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickProgressBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickProgressBar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickProgressBar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickProgressBar::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#from
    """
    #  qreal QQuickProgressBar::from() const
    return self.uglySide.call('ritual_ZNK17QQuickProgressBar4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickProgressBar::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#to
    """
    #  qreal QQuickProgressBar::to() const
    return self.uglySide.call('ritual_ZNK17QQuickProgressBar2toEv')

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickProgressBar::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#value
    """
    #  qreal QQuickProgressBar::value() const
    return self.uglySide.call('ritual_ZNK17QQuickProgressBar5valueEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickProgressBar::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#position
    """
    #  qreal QQuickProgressBar::position() const
    return self.uglySide.call('ritual_ZNK17QQuickProgressBar8positionEv')

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickProgressBar::visualPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#visualPosition
    """
    #  qreal QQuickProgressBar::visualPosition() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickProgressBar14visualPositionEv',
    )

  def isIndeterminate(self) -> bool:
    """
    Calls Qt's 'bool QQuickProgressBar::isIndeterminate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#isIndeterminate
    """
    #  bool QQuickProgressBar::isIndeterminate() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickProgressBar15isIndeterminateEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickProgressBar::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickProgressBar::accessibleRole() const
    ritual = 'ritual_ZNK17QQuickProgressBar14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickProgressBar14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::setFrom(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickProgressBar::setFrom(qreal from)
    self.uglySide.call('ritual_ZN17QQuickProgressBar7setFromEd', from_)

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::setTo(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickProgressBar::setTo(qreal to)
    self.uglySide.call('ritual_ZN17QQuickProgressBar5setToEd', to)

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::setValue(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickProgressBar::setValue(qreal value)
    self.uglySide.call('ritual_ZN17QQuickProgressBar8setValueEd', value)

  @overload(bool)
  def setIndeterminate(self, indeterminate: bool) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::setIndeterminate(bool
    indeterminate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#setIndeterminate

    Parameters
    ----------

    indeterminate : bool
      Passed on as it is.
    """
    #  void QQuickProgressBar::setIndeterminate(bool indeterminate)
    self.uglySide.call(
        'ritual_ZN17QQuickProgressBar16setIndeterminateEb', indeterminate,
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
    'QQuickProgressBar::QQuickProgressBar(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#QQuickProgressBar

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickProgressBar::QQuickProgressBar(QQuickItem *parent)
    self._noteCreation(QQuickProgressBar, lambda: Rituals.call(
        'ritual_ZN17QQuickProgressBarC1EP10QQuickItem',
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

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::fromChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#fromChanged
    """
    #  void QQuickProgressBar::fromChanged()
    self.uglySide.call('ritual_ZN17QQuickProgressBar11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprogressbar.html#toChanged
    """
    #  void QQuickProgressBar::toChanged()
    self.uglySide.call('ritual_ZN17QQuickProgressBar9toChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::valueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#valueChanged
    """
    #  void QQuickProgressBar::valueChanged()
    self.uglySide.call('ritual_ZN17QQuickProgressBar12valueChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#positionChanged
    """
    #  void QQuickProgressBar::positionChanged()
    self.uglySide.call('ritual_ZN17QQuickProgressBar15positionChangedEv')

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#visualPositionChanged
    """
    #  void QQuickProgressBar::visualPositionChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickProgressBar21visualPositionChangedEv',
    )

  def indeterminateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::indeterminateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#indeterminateChanged
    """
    #  void QQuickProgressBar::indeterminateChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickProgressBar20indeterminateChangedEv',
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#mirrorChange
    """
    #  void QQuickProgressBar::mirrorChange()
    ritual = 'ritual_ZN17QQuickProgressBar12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickProgressBar12mirrorChangeEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickProgressBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprogressbar.html#componentComplete
    """
    #  void QQuickProgressBar::componentComplete()
    ritual = 'ritual_ZN17QQuickProgressBar17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickProgressBar17componentCompleteEv'
    self.uglySide.call(ritual)
