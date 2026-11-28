"""
QQuickItemDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickitemdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickItemDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickAbstractButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from . import QQuickItemDelegatePrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemDelegate(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickItemDelegate: a plain Python object standing in
  front of one C++ QQuickItemDelegate.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickItemDelegate
  is built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemDelegate that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'isHighlighted',
  'setHighlighted', 'highlightedChanged', 'defaultFont', 'accessibleRole',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemDelegate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickItemDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickItemDelegate::QQuickItemDelegate(QQuickItemDelegatePrivate
    &dd, QQuickItem *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QQuickItemDelegatePrivate *QQuickItemDelegate::d_func()
    const': takes in Python what 'QQuickItemDelegatePrivate
    *QQuickItemDelegate::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickItemDelegate is created at the first use, not by
    'QQuickItemDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemDelegate.
  - Qt tells when it has removed the C++ QQuickItemDelegate. Every call on
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
    Calls Qt's 'QString QQuickItemDelegate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemdelegate.html#tr

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
    #  QString QQuickItemDelegate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickItemDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItemDelegate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickItemDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isHighlighted(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemDelegate::isHighlighted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemdelegate.html#isHighlighted
    """
    #  bool QQuickItemDelegate::isHighlighted() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickItemDelegate13isHighlightedEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickItemDelegate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemdelegate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickItemDelegate::defaultFont() const
    ritual = 'ritual_ZNK18QQuickItemDelegate11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickItemDelegate11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickItemDelegate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemdelegate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickItemDelegate::accessibleRole() const
    ritual = 'ritual_ZNK18QQuickItemDelegate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickItemDelegate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHighlighted(self, highlighted: bool) -> None:
    """
    Calls Qt's 'void QQuickItemDelegate::setHighlighted(bool highlighted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemdelegate.html#setHighlighted

    Parameters
    ----------

    highlighted : bool
      Passed on as it is.
    """
    #  void QQuickItemDelegate::setHighlighted(bool highlighted)
    self.uglySide.call(
        'ritual_ZN18QQuickItemDelegate14setHighlightedEb', highlighted,
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
    'QQuickItemDelegate::QQuickItemDelegate(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemdelegate.html#QQuickItemDelegate

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickItemDelegate::QQuickItemDelegate(QQuickItem *parent)
    self._noteCreation(QQuickItemDelegate, lambda: Rituals.call(
        'ritual_ZN18QQuickItemDelegateC1EP10QQuickItem',
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

  def highlightedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemDelegate::highlightedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemdelegate.html#highlightedChanged
    """
    #  void QQuickItemDelegate::highlightedChanged()
    self.uglySide.call('ritual_ZN18QQuickItemDelegate18highlightedChangedEv')

  def d_func(self) -> Optional[QQuickItemDelegatePrivate]:
    """
    Calls Qt's 'QQuickItemDelegatePrivate *QQuickItemDelegate::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemdelegate.html#d_func

    Returns
    -------

    Optional[QQuickItemDelegatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemDelegatePrivate *QQuickItemDelegate::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickItemDelegate6d_funcEv')
    from . import QQuickItemDelegatePrivate
    return QQuickItemDelegatePrivate._cuteAt(address)
