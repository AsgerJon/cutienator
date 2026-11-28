"""
QQuickMenuBarItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuBarItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickAbstractButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QFont, QKeyEvent
  from . import QQuickMenu, QQuickMenuBar, QQuickMenuBarItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QQuickMenu = WAIT['QQuickMenu']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuBarItem(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickMenuBarItem: a plain Python object standing in
  front of one C++ QQuickMenuBarItem.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickMenuBarItem
  is built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuBarItem that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'menuBar', 'menu',
  'setMenu', 'isHighlighted', 'setHighlighted', 'triggered',
  'menuBarChanged', 'menuChanged', 'highlightedChanged', 'event',
  'keyPressEvent', 'keyReleaseEvent', 'geometryChange', 'defaultFont',
  'accessibleRole', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMenuBarItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMenuBarItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickMenuBarItemPrivate *QQuickMenuBarItem::d_func() const':
    takes in Python what 'QQuickMenuBarItemPrivate
    *QQuickMenuBarItem::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMenuBarItem is created at the first use, not by
    'QQuickMenuBarItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuBarItem.
  - Qt tells when it has removed the C++ QQuickMenuBarItem. Every call on the
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
    Calls Qt's 'QString QQuickMenuBarItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#tr

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
    #  QString QQuickMenuBarItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickMenuBarItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuBarItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMenuBarItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMenuBarItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMenuBarItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def menuBar(self) -> Optional[QQuickMenuBar]:
    """
    Calls Qt's 'QQuickMenuBar *QQuickMenuBarItem::menuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#menuBar

    Returns
    -------

    Optional[QQuickMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBar *QQuickMenuBarItem::menuBar() const
    address = self.uglySide.call('ritual_ZNK17QQuickMenuBarItem7menuBarEv')
    from . import QQuickMenuBar
    return QQuickMenuBar._cuteAt(address)

  def menu(self) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuBarItem::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#menu

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuBarItem::menu() const
    address = self.uglySide.call('ritual_ZNK17QQuickMenuBarItem4menuEv')
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def isHighlighted(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBarItem::isHighlighted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#isHighlighted
    """
    #  bool QQuickMenuBarItem::isHighlighted() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickMenuBarItem13isHighlightedEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickMenuBarItem::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickMenuBarItem::defaultFont() const
    ritual = 'ritual_ZNK17QQuickMenuBarItem11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickMenuBarItem11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickMenuBarItem::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickMenuBarItem::accessibleRole() const
    ritual = 'ritual_ZNK17QQuickMenuBarItem14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickMenuBarItem14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::setMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#setMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarItem::setMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuBarItem7setMenuEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(bool)
  def setHighlighted(self, highlighted: bool) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::setHighlighted(bool highlighted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#setHighlighted

    Parameters
    ----------

    highlighted : bool
      Passed on as it is.
    """
    #  void QQuickMenuBarItem::setHighlighted(bool highlighted)
    self.uglySide.call(
        'ritual_ZN17QQuickMenuBarItem14setHighlightedEb', highlighted,
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
    'QQuickMenuBarItem::QQuickMenuBarItem(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#QQuickMenuBarItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMenuBarItem::QQuickMenuBarItem(QQuickItem *parent)
    self._noteCreation(QQuickMenuBarItem, lambda: Rituals.call(
        'ritual_ZN17QQuickMenuBarItemC1EP10QQuickItem',
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

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::triggered()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#triggered
    """
    #  void QQuickMenuBarItem::triggered()
    self.uglySide.call('ritual_ZN17QQuickMenuBarItem9triggeredEv')

  def menuBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::menuBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#menuBarChanged
    """
    #  void QQuickMenuBarItem::menuBarChanged()
    self.uglySide.call('ritual_ZN17QQuickMenuBarItem14menuBarChangedEv')

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::menuChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#menuChanged
    """
    #  void QQuickMenuBarItem::menuChanged()
    self.uglySide.call('ritual_ZN17QQuickMenuBarItem11menuChangedEv')

  def highlightedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::highlightedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#highlightedChanged
    """
    #  void QQuickMenuBarItem::highlightedChanged()
    self.uglySide.call('ritual_ZN17QQuickMenuBarItem18highlightedChangedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBarItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMenuBarItem::event(QEvent *event)
    ritual = 'ritual_ZN17QQuickMenuBarItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickMenuBarItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarItem::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QQuickMenuBarItem13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickMenuBarItem13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarItem::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QQuickMenuBarItem15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuBarItem15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMenuBarItem::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN17QQuickMenuBarItem14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickMenuBarItem14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def d_func(self) -> Optional[QQuickMenuBarItemPrivate]:
    """
    Calls Qt's 'QQuickMenuBarItemPrivate *QQuickMenuBarItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritem.html#d_func

    Returns
    -------

    Optional[QQuickMenuBarItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBarItemPrivate *QQuickMenuBarItem::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickMenuBarItem6d_funcEv')
    from . import QQuickMenuBarItemPrivate
    return QQuickMenuBarItemPrivate._cuteAt(address)
