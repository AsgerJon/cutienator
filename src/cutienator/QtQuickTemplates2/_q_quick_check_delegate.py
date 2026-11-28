"""
QQuickCheckDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcheckdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickCheckDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCheckDelegate(QQuickItemDelegate):
  """
  The cute side of Qt's QQuickCheckDelegate: a plain Python object standing
  in front of one C++ QQuickCheckDelegate.

  It is built on the cute 'QQuickItemDelegate', as Qt's QQuickCheckDelegate
  is built on Qt's QQuickItemDelegate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCheckDelegate that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'isTristate',
  'setTristate', 'checkState', 'setCheckState', 'tristateChanged',
  'checkStateChanged', 'nextCheckStateChanged', 'defaultFont',
  'nextCheckState', 'accessibleRole'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCheckDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickCheckDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickCheckDelegate::buttonChange(ButtonChange change)': names
    the enum 'QQuickAbstractButton::ButtonChange', whose class cannot be
    named here.
  - Qt's 'QQuickCheckDelegatePrivate *QQuickCheckDelegate::d_func()': gives
    'QQuickCheckDelegatePrivate', which has no cute class yet.
  - Qt's 'const QQuickCheckDelegatePrivate *QQuickCheckDelegate::d_func()
    const': gives 'QQuickCheckDelegatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickCheckDelegate is created at the first use, not by
    'QQuickCheckDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCheckDelegate.
  - Qt tells when it has removed the C++ QQuickCheckDelegate. Every call on
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
    Calls Qt's 'QString QQuickCheckDelegate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcheckdelegate.html#tr

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
    #  QString QQuickCheckDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickCheckDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCheckDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickCheckDelegate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCheckDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickCheckDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isTristate(self) -> bool:
    """
    Calls Qt's 'bool QQuickCheckDelegate::isTristate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#isTristate
    """
    #  bool QQuickCheckDelegate::isTristate() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickCheckDelegate10isTristateEv',
    )

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QQuickCheckDelegate::checkState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QQuickCheckDelegate::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK19QQuickCheckDelegate10checkStateEv',
    ))

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickCheckDelegate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickCheckDelegate::defaultFont() const
    ritual = 'ritual_ZNK19QQuickCheckDelegate11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickCheckDelegate11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickCheckDelegate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickCheckDelegate::accessibleRole() const
    ritual = 'ritual_ZNK19QQuickCheckDelegate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickCheckDelegate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTristate(self, tristate: bool) -> None:
    """
    Calls Qt's 'void QQuickCheckDelegate::setTristate(bool tristate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#setTristate

    Parameters
    ----------

    tristate : bool
      Passed on as it is.
    """
    #  void QQuickCheckDelegate::setTristate(bool tristate)
    self.uglySide.call(
        'ritual_ZN19QQuickCheckDelegate11setTristateEb', tristate,
    )

  @overload(Qt.CheckState)
  def setCheckState(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QQuickCheckDelegate::setCheckState(Qt::CheckState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#setCheckState

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QQuickCheckDelegate::setCheckState(Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN19QQuickCheckDelegate13setCheckStateEN2Qt10CheckStateE',
        state.value,
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
    'QQuickCheckDelegate::QQuickCheckDelegate(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#QQuickCheckDelegate

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickCheckDelegate::QQuickCheckDelegate(QQuickItem *parent)
    self._noteCreation(QQuickCheckDelegate, lambda: Rituals.call(
        'ritual_ZN19QQuickCheckDelegateC1EP10QQuickItem',
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

  def tristateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCheckDelegate::tristateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#tristateChanged
    """
    #  void QQuickCheckDelegate::tristateChanged()
    self.uglySide.call('ritual_ZN19QQuickCheckDelegate15tristateChangedEv')

  def checkStateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCheckDelegate::checkStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#checkStateChanged
    """
    #  void QQuickCheckDelegate::checkStateChanged()
    self.uglySide.call('ritual_ZN19QQuickCheckDelegate17checkStateChangedEv')

  def nextCheckStateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCheckDelegate::nextCheckStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#nextCheckStateChanged
    """
    #  void QQuickCheckDelegate::nextCheckStateChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickCheckDelegate21nextCheckStateChangedEv',
    )

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QQuickCheckDelegate::nextCheckState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcheckdelegate.html#nextCheckState
    """
    #  void QQuickCheckDelegate::nextCheckState()
    ritual = 'ritual_ZN19QQuickCheckDelegate14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickCheckDelegate14nextCheckStateEv'
    self.uglySide.call(ritual)
