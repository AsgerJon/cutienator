"""
QQuickMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuBar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QFont, QHoverEvent, QKeyEvent
  from ..QtQml import QQmlComponent
  from . import QQuickMenu, QQuickMenuBarPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickMenu = WAIT['QQuickMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuBar(QQuickContainer):
  """
  The cute side of Qt's QQuickMenuBar: a plain Python object standing in
  front of one C++ QQuickMenuBar.

  It is built on the cute 'QQuickContainer', as Qt's QQuickMenuBar is built
  on Qt's QQuickContainer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuBar that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'delegate',
  'setDelegate', 'menuAt', 'addMenu', 'insertMenu', 'removeMenu', 'takeMenu',
  'delegateChanged', 'menusChanged', 'eventFilter', 'keyPressEvent',
  'keyReleaseEvent', 'hoverLeaveEvent', 'isContent', 'itemChange',
  'itemAdded', 'itemMoved', 'itemRemoved', 'componentComplete',
  'defaultFont', 'accessibleRole', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMenuBar::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickMenuBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMenuBar::~QQuickMenuBar()': the destructor: Python never
    removes a C++ QQuickMenuBar.
  - Qt's 'const QQuickMenuBarPrivate *QQuickMenuBar::d_func() const': takes
    in Python what 'QQuickMenuBarPrivate *QQuickMenuBar::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMenuBar is created at the first use, not by
    'QQuickMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuBar.
  - Qt tells when it has removed the C++ QQuickMenuBar. Every call on the
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
    Calls Qt's 'QString QQuickMenuBar::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#tr

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
    #  QString QQuickMenuBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickMenuBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuBar'

  #  A C++ QQuickMenuBar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenuBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMenuBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMenuBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickMenuBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickMenuBar::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickMenuBar::delegate() const
    address = self.uglySide.call('ritual_ZNK13QQuickMenuBar8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  @overload(int)
  def menuAt(self, index: int) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuBar::menuAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#menuAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuBar::menuAt(int index) const
    address = self.uglySide.call('ritual_ZNK13QQuickMenuBar6menuAtEi', index)
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def isContent(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBar::isContent(QQuickItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#isContent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMenuBar::isContent(QQuickItem *item) const
    ritual = 'ritual_ZNK13QQuickMenuBar9isContentEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickMenuBar9isContentEP10QQuickItem'
    return self.uglySide.call(ritual, self._addressOf(item))

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickMenuBar::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickMenuBar::defaultFont() const
    ritual = 'ritual_ZNK13QQuickMenuBar11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickMenuBar11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickMenuBar::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickMenuBar::accessibleRole() const
    ritual = 'ritual_ZNK13QQuickMenuBar14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickMenuBar14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::setDelegate(QQmlComponent *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN13QQuickMenuBar11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
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
    Notes what was given, for Qt's 'QQuickMenuBar::QQuickMenuBar(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#QQuickMenuBar

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMenuBar::QQuickMenuBar(QQuickItem *parent)
    self._noteCreation(QQuickMenuBar, lambda: Rituals.call(
        'ritual_ZN13QQuickMenuBarC1EP10QQuickItem', self._addressOf(parent),
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

  @overload(QQuickMenu)
  @overload(NoneType)
  def addMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::addMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#addMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::addMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN13QQuickMenuBar7addMenuEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(int, QQuickMenu)
  @overload(int, NoneType)
  def insertMenu(self, index: int, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::insertMenu(int index, QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#insertMenu

    Parameters
    ----------

    index : int
      Passed on as it is.

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::insertMenu(int index, QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN13QQuickMenuBar10insertMenuEiP10QQuickMenu',
        index, self._addressOf(menu),
    )

  @overload(QQuickMenu)
  @overload(NoneType)
  def removeMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::removeMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#removeMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::removeMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN13QQuickMenuBar10removeMenuEP10QQuickMenu',
        self._addressOf(menu),
    )

  @overload(int)
  def takeMenu(self, index: int) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenuBar::takeMenu(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#takeMenu

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenuBar::takeMenu(int index)
    address = self.uglySide.call(
        'ritual_ZN13QQuickMenuBar8takeMenuEi', index,
    )
    from . import QQuickMenu
    return QQuickMenu._cuteAt(address)

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::delegateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#delegateChanged
    """
    #  void QQuickMenuBar::delegateChanged()
    self.uglySide.call('ritual_ZN13QQuickMenuBar15delegateChangedEv')

  def menusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::menusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#menusChanged
    """
    #  void QQuickMenuBar::menusChanged()
    self.uglySide.call('ritual_ZN13QQuickMenuBar12menusChangedEv')

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBar::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMenuBar::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN13QQuickMenuBar11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QQuickMenuBar13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QQuickMenuBar15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickMenuBar15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar15hoverLeaveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::itemChange(QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickMenuBar::itemChange(QQuickItem::ItemChange change, const
    #      QQuickItem::ItemChangeData &value)
    ritual = (
        'ritual_ZN13QQuickMenuBar10itemChangeEN10QQuickItem10ItemChangeERKN'
        'S0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickMenuBar10itemChangeEN10QQuickItem10ItemChan'
          'geERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::itemAdded(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::itemAdded(int index, QQuickItem *item)
    ritual = 'ritual_ZN13QQuickMenuBar9itemAddedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar9itemAddedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemMoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::itemMoved(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#itemMoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::itemMoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN13QQuickMenuBar9itemMovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar9itemMovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::itemRemoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBar::itemRemoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN13QQuickMenuBar11itemRemovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar11itemRemovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubar.html#componentComplete
    """
    #  void QQuickMenuBar::componentComplete()
    ritual = 'ritual_ZN13QQuickMenuBar17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickMenuBar17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickMenuBarPrivate]:
    """
    Calls Qt's 'QQuickMenuBarPrivate *QQuickMenuBar::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubar.html#d_func

    Returns
    -------

    Optional[QQuickMenuBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBarPrivate *QQuickMenuBar::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickMenuBar6d_funcEv')
    from . import QQuickMenuBarPrivate
    return QQuickMenuBarPrivate._cuteAt(address)
