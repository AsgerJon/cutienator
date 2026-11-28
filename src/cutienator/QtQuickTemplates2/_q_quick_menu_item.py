"""
QQuickMenuItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenuitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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
  from . import QQuickMenu, QQuickMenuItemPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuItem(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickMenuItem: a plain Python object standing in
  front of one C++ QQuickMenuItem.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickMenuItem is
  built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuItem that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'isHighlighted',
  'setHighlighted', 'arrow', 'setArrow', 'menu', 'subMenu', 'textPadding',
  'implicitTextPadding', 'setImplicitTextPadding', 'triggered',
  'highlightedChanged', 'arrowChanged', 'menuChanged', 'subMenuChanged',
  'implicitTextPaddingChanged', 'textPaddingChanged', 'componentComplete',
  'defaultFont', 'accessibleRole', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMenuItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickMenuItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickMenuItemPrivate *QQuickMenuItem::d_func() const': takes
    in Python what 'QQuickMenuItemPrivate *QQuickMenuItem::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMenuItem is created at the first use, not by
    'QQuickMenuItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuItem.
  - Qt tells when it has removed the C++ QQuickMenuItem. Every call on the
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
    Calls Qt's 'QString QQuickMenuItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#tr

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
    #  QString QQuickMenuItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickMenuItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMenuItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMenuItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickMenuItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isHighlighted(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuItem::isHighlighted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#isHighlighted
    """
    #  bool QQuickMenuItem::isHighlighted() const
    return self.uglySide.call('ritual_ZNK14QQuickMenuItem13isHighlightedEv')

  def arrow(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenuItem::arrow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#arrow

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenuItem::arrow() const
    address = self.uglySide.call('ritual_ZNK14QQuickMenuItem5arrowEv')
    return QQuickItem._cuteAt(address)

  def menu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuItem::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#menu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuItem::menu() const
    address = self.uglySide.call('ritual_ZNK14QQuickMenuItem4menuEv')
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def subMenu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuItem::subMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#subMenu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuItem::subMenu() const
    address = self.uglySide.call('ritual_ZNK14QQuickMenuItem7subMenuEv')
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def textPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickMenuItem::textPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#textPadding
    """
    #  qreal QQuickMenuItem::textPadding() const
    return self.uglySide.call('ritual_ZNK14QQuickMenuItem11textPaddingEv')

  def implicitTextPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickMenuItem::implicitTextPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitem.html#implicitTextPadding
    """
    #  qreal QQuickMenuItem::implicitTextPadding() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickMenuItem19implicitTextPaddingEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickMenuItem::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickMenuItem::defaultFont() const
    ritual = 'ritual_ZNK14QQuickMenuItem11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickMenuItem11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickMenuItem::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickMenuItem::accessibleRole() const
    ritual = 'ritual_ZNK14QQuickMenuItem14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickMenuItem14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHighlighted(self, highlighted: bool) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::setHighlighted(bool highlighted)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#setHighlighted

    Parameters
    ----------

    highlighted : bool
      Passed on as it is.
    """
    #  void QQuickMenuItem::setHighlighted(bool highlighted)
    self.uglySide.call(
        'ritual_ZN14QQuickMenuItem14setHighlightedEb', highlighted,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setArrow(self, arrow: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::setArrow(QQuickItem *arrow)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#setArrow

    Parameters
    ----------

    arrow : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuItem::setArrow(QQuickItem *arrow)
    self.uglySide.call(
        'ritual_ZN14QQuickMenuItem8setArrowEP10QQuickItem',
        self._addressOf(arrow),
    )

  @overload(float)
  def setImplicitTextPadding(self, newImplicitTextPadding: float) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::setImplicitTextPadding(qreal
    newImplicitTextPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitem.html#setImplicitTextPadding

    Parameters
    ----------

    newImplicitTextPadding : float
      Passed on as it is.
    """
    #  void QQuickMenuItem::setImplicitTextPadding(qreal
    #      newImplicitTextPadding)
    self.uglySide.call(
        'ritual_ZN14QQuickMenuItem22setImplicitTextPaddingEd',
        newImplicitTextPadding,
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
    Notes what was given, for Qt's 'QQuickMenuItem::QQuickMenuItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#QQuickMenuItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMenuItem::QQuickMenuItem(QQuickItem *parent)
    self._noteCreation(QQuickMenuItem, lambda: Rituals.call(
        'ritual_ZN14QQuickMenuItemC1EP10QQuickItem', self._addressOf(parent),
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

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::triggered()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#triggered
    """
    #  void QQuickMenuItem::triggered()
    self.uglySide.call('ritual_ZN14QQuickMenuItem9triggeredEv')

  def highlightedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::highlightedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitem.html#highlightedChanged
    """
    #  void QQuickMenuItem::highlightedChanged()
    self.uglySide.call('ritual_ZN14QQuickMenuItem18highlightedChangedEv')

  def arrowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::arrowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#arrowChanged
    """
    #  void QQuickMenuItem::arrowChanged()
    self.uglySide.call('ritual_ZN14QQuickMenuItem12arrowChangedEv')

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::menuChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#menuChanged
    """
    #  void QQuickMenuItem::menuChanged()
    self.uglySide.call('ritual_ZN14QQuickMenuItem11menuChangedEv')

  def subMenuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::subMenuChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#subMenuChanged
    """
    #  void QQuickMenuItem::subMenuChanged()
    self.uglySide.call('ritual_ZN14QQuickMenuItem14subMenuChangedEv')

  def implicitTextPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::implicitTextPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitem.html#implicitTextPaddingChanged
    """
    #  void QQuickMenuItem::implicitTextPaddingChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickMenuItem26implicitTextPaddingChangedEv',
    )

  def textPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::textPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitem.html#textPaddingChanged
    """
    #  void QQuickMenuItem::textPaddingChanged()
    self.uglySide.call('ritual_ZN14QQuickMenuItem18textPaddingChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitem.html#componentComplete
    """
    #  void QQuickMenuItem::componentComplete()
    ritual = 'ritual_ZN14QQuickMenuItem17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickMenuItem17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickMenuItemPrivate]:
    """
    Calls Qt's 'QQuickMenuItemPrivate *QQuickMenuItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenuitem.html#d_func

    Returns
    -------

    Optional[QQuickMenuItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItemPrivate *QQuickMenuItem::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickMenuItem6d_funcEv')
    from . import QQuickMenuItemPrivate
    return QQuickMenuItemPrivate._cuteAt(address)
