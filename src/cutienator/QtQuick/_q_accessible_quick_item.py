"""
QAccessibleQuickItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qaccessiblequickitem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleQuickItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from ..QtGui import QAccessible, QAccessibleActionInterface
from ..QtGui import QAccessibleAttributesInterface, QAccessibleInterface
from ..QtGui import QAccessibleObject, QAccessibleTextInterface
from ..QtGui import QAccessibleValueInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QRect, QVariant
  from ..QtGui import QTextDocument, QWindow
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QQuickItem = WAIT['QQuickItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickItem(QAccessibleObject, QAccessibleActionInterface, QAccessibleValueInterface, QAccessibleTextInterface, QAccessibleAttributesInterface):
  """
  The cute side of Qt's QAccessibleQuickItem: a plain Python object standing
  in front of one C++ QAccessibleQuickItem.

  It is built on the cute 'QAccessibleObject', as Qt's QAccessibleQuickItem
  is built on Qt's QAccessibleObject, and has everything that class has. It
  is built on the cute 'QAccessibleActionInterface' as well, as Qt's
  QAccessibleQuickItem is built on Qt's QAccessibleActionInterface too, and
  has everything that class has. It is built on the cute
  'QAccessibleValueInterface' as well, as Qt's QAccessibleQuickItem is built
  on Qt's QAccessibleValueInterface too, and has everything that class has.
  It is built on the cute 'QAccessibleTextInterface' as well, as Qt's
  QAccessibleQuickItem is built on Qt's QAccessibleTextInterface too, and has
  everything that class has. It is built on the cute
  'QAccessibleAttributesInterface' as well, as Qt's QAccessibleQuickItem is
  built on Qt's QAccessibleAttributesInterface too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickItem that has a ritual and that
  Python can call so far, 37 names in all: 'isValid', 'window', 'rect',
  'viewRect', 'clipsChildren', 'childAt', 'parent', 'child', 'childCount',
  'indexOfChild', 'childItems', 'state', 'role', 'text', 'setText',
  'isAccessible', 'actionNames', 'doAction', 'keyBindingsForAction',
  'currentValue', 'setCurrentValue', 'maximumValue', 'minimumValue',
  'minimumStepSize', 'selectionCount', 'addSelection', 'removeSelection',
  'setSelection', 'cursorPosition', 'setCursorPosition', 'characterCount',
  'characterRect', 'offsetAtPoint', 'scrollToSubstring', 'textDocument',
  'attributeValue', 'item'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<std::pair<QAccessibleInterface *, QAccessible::Relation>>
    QAccessibleQuickItem::relations(QAccessible::Relation match) const':
    gives a type Python has no way to take yet.
  - Qt's 'void QAccessibleQuickItem::selection(int selectionIndex, int
    *startOffset, int *endOffset) const': takes a number to change where it
    is.
  - Qt's 'QString QAccessibleQuickItem::textBeforeOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleQuickItem::textAfterOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleQuickItem::textAtOffset(int offset,
    QAccessible::TextBoundaryType boundaryType, int *startOffset, int
    *endOffset) const': takes a number to change where it is.
  - Qt's 'QString QAccessibleQuickItem::attributes(int a0, int *startOffset,
    int *endOffset) const': takes a number to change where it is.
  - Qt's 'QList<QAccessible::Attribute> QAccessibleQuickItem::attributeKeys()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    *QAccessibleQuickItem::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickItem is created at the first use, not by
    'QAccessibleQuickItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickItem'

  #  Qt's QAccessibleQuickItem is built on more than one class. The part of a
  #  C++ QAccessibleQuickItem that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleActionInterface':
          'ritual_cast_QAccessibleQuickItem_QAccessibleActionInterface',
      'QAccessibleValueInterface':
          'ritual_cast_QAccessibleQuickItem_QAccessibleValueInterface',
      'QAccessibleTextInterface':
          'ritual_cast_QAccessibleQuickItem_QAccessibleTextInterface',
      'QAccessibleAttributesInterface':
          'ritual_cast_QAccessibleQuickItem_QAccessibleAttributesInterface',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleQuickItem::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#isValid
    """
    #  bool QAccessibleQuickItem::isValid() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem7isValidEv'
    return self.uglySide.call(ritual)

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QAccessibleQuickItem::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QAccessibleQuickItem::window() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem6windowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem6windowEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleQuickItem::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleQuickItem::rect() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewRect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleQuickItem::viewRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#viewRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleQuickItem::viewRect() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem8viewRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def clipsChildren(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleQuickItem::clipsChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#clipsChildren
    """
    #  bool QAccessibleQuickItem::clipsChildren() const
    return self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem13clipsChildrenEv',
    )

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickItem::childAt(int x,
    int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleQuickItem::childAt(int x, int y)
    #      const
    ritual = 'ritual_ZNK20QAccessibleQuickItem7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickItem::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleQuickItem::parent() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickItem::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleQuickItem::child(int index) const
    ritual = 'ritual_ZNK20QAccessibleQuickItem5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickItem::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#childCount
    """
    #  int QAccessibleQuickItem::childCount() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleQuickItem::indexOfChild(const
    QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#indexOfChild

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleQuickItem::indexOfChild(const QAccessibleInterface
    #      *iface) const
    ritual = (
        'ritual_ZNK20QAccessibleQuickItem12indexOfChildEPK20QAccessibleInte'
        'rface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleQuickItem12indexOfChildEPK20QAccessib'
          'leInterface')
    return self.uglySide.call(
        ritual, self._addressOf(iface, 'QAccessibleInterface'),
    )

  def childItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QAccessibleQuickItem::childItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#childItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QAccessibleQuickItem::childItems() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem10childItemsEv',
    )
    from . import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleQuickItem::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleQuickItem::state() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleQuickItem::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleQuickItem::role() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  @overload(QAccessible.Text)
  def text(self, a0: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleQuickItem::text(QAccessible::Text a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#text

    Parameters
    ----------

    a0 : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleQuickItem::text(QAccessible::Text a0) const
    ritual = 'ritual_ZNK20QAccessibleQuickItem4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleQuickItem4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, a0.value)

  @overload(int, int)
  def text(self, startOffset: int, endOffset: int) -> str:
    """
    Calls Qt's 'QString QAccessibleQuickItem::text(int startOffset, int
    endOffset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#text

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleQuickItem::text(int startOffset, int endOffset)
    #      const
    ritual = 'ritual_ZNK20QAccessibleQuickItem4textEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem4textEii'
    return self.uglySide.call(ritual, startOffset, endOffset)

  def isAccessible(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleQuickItem::isAccessible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#isAccessible
    """
    #  bool QAccessibleQuickItem::isAccessible() const
    return self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem12isAccessibleEv',
    )

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleQuickItem::actionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleQuickItem::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def keyBindingsForAction(self, actionName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleQuickItem::keyBindingsForAction(const
    QString &actionName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#keyBindingsForAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleQuickItem::keyBindingsForAction(const QString
    #      &actionName) const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem20keyBindingsForActionERK7QString',
        actionName,
    )
    return QStringList._cuteOwning(address)

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickItem::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickItem::currentValue() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem12currentValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem12currentValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maximumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickItem::maximumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#maximumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickItem::maximumValue() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem12maximumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem12maximumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickItem::minimumValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#minimumValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickItem::minimumValue() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem12minimumValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem12minimumValueEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def minimumStepSize(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAccessibleQuickItem::minimumStepSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#minimumStepSize

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickItem::minimumStepSize() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem15minimumStepSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem15minimumStepSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def selectionCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickItem::selectionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#selectionCount
    """
    #  int QAccessibleQuickItem::selectionCount() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem14selectionCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem14selectionCountEv'
    return self.uglySide.call(ritual)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickItem::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#cursorPosition
    """
    #  int QAccessibleQuickItem::cursorPosition() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem14cursorPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem14cursorPositionEv'
    return self.uglySide.call(ritual)

  def characterCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleQuickItem::characterCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#characterCount
    """
    #  int QAccessibleQuickItem::characterCount() const
    ritual = 'ritual_ZNK20QAccessibleQuickItem14characterCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem14characterCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def characterRect(self, a0: int) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleQuickItem::characterRect(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#characterRect

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleQuickItem::characterRect(int a0) const
    ritual = 'ritual_ZNK20QAccessibleQuickItem13characterRectEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickItem13characterRectEi'
    address = self.uglySide.call(ritual, a0)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def offsetAtPoint(self, a0: QPoint) -> int:
    """
    Calls Qt's 'int QAccessibleQuickItem::offsetAtPoint(const QPoint &a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#offsetAtPoint

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QAccessibleQuickItem::offsetAtPoint(const QPoint &a0) const
    ritual = 'ritual_ZNK20QAccessibleQuickItem13offsetAtPointERK6QPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleQuickItem13offsetAtPointERK6QPoint')
    return self.uglySide.call(ritual, self._valueOf(a0))

  def textDocument(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QAccessibleQuickItem::textDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#textDocument

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QAccessibleQuickItem::textDocument() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickItem12textDocumentEv',
    )
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  @overload(QAccessible.Attribute)
  def attributeValue(self, key: QAccessible.Attribute) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAccessibleQuickItem::attributeValue(QAccessible::Attribute key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#attributeValue

    Parameters
    ----------

    key : QAccessible.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickItem::attributeValue(QAccessible::Attribute
    #      key) const
    ritual = (
        'ritual_ZNK20QAccessibleQuickItem14attributeValueEN11QAccessible9At'
        'tributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleQuickItem14attributeValueEN11QAccessi'
          'ble9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def item(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QAccessibleQuickItem::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#item

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QAccessibleQuickItem::item() const
    address = self.uglySide.call('ritual_ZNK20QAccessibleQuickItem4itemEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, a0: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::setText(QAccessible::Text a0,
    const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#setText

    Parameters
    ----------

    a0 : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleQuickItem::setText(QAccessible::Text a0, const QString
    #      &text)
    ritual = (
        'ritual_ZN20QAccessibleQuickItem7setTextEN11QAccessible4TextERK7QSt'
        'ring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAccessibleQuickItem7setTextEN11QAccessible4TextE'
          'RK7QString')
    self.uglySide.call(ritual, a0.value, text)

  @overload(QVariant)
  def setCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::setCurrentValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#setCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAccessibleQuickItem::setCurrentValue(const QVariant &value)
    ritual = 'ritual_ZN20QAccessibleQuickItem15setCurrentValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAccessibleQuickItem15setCurrentValueERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(value))

  @overload(int, int, int)
  def setSelection(
      self,
      selectionIndex: int,
      startOffset: int,
      endOffset: int,
  ) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::setSelection(int selectionIndex,
    int startOffset, int endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#setSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleQuickItem::setSelection(int selectionIndex, int
    #      startOffset, int endOffset)
    ritual = 'ritual_ZN20QAccessibleQuickItem12setSelectionEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleQuickItem12setSelectionEiii'
    self.uglySide.call(ritual, selectionIndex, startOffset, endOffset)

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::setCursorPosition(int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAccessibleQuickItem::setCursorPosition(int position)
    ritual = 'ritual_ZN20QAccessibleQuickItem17setCursorPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleQuickItem17setCursorPositionEi'
    self.uglySide.call(ritual, position)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickItem::QAccessibleQuickItem(QQuickItem *item)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#QAccessibleQuickItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickItem::QAccessibleQuickItem(QQuickItem *item)
    self._noteCreation(QAccessibleQuickItem, lambda: Rituals.call(
        'ritual_ZN20QAccessibleQuickItemC1EP10QQuickItem',
        self._addressOf(item),
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

  @overload(str)
  def doAction(self, actionName: str) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::doAction(const QString
    &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickitem.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleQuickItem::doAction(const QString &actionName)
    ritual = 'ritual_ZN20QAccessibleQuickItem8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleQuickItem8doActionERK7QString'
    self.uglySide.call(ritual, actionName)

  @overload(int, int)
  def addSelection(self, startOffset: int, endOffset: int) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::addSelection(int startOffset, int
    endOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#addSelection

    Parameters
    ----------

    startOffset : int
      Passed on as it is.

    endOffset : int
      Passed on as it is.
    """
    #  void QAccessibleQuickItem::addSelection(int startOffset, int
    #      endOffset)
    ritual = 'ritual_ZN20QAccessibleQuickItem12addSelectionEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleQuickItem12addSelectionEii'
    self.uglySide.call(ritual, startOffset, endOffset)

  @overload(int)
  def removeSelection(self, selectionIndex: int) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::removeSelection(int
    selectionIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#removeSelection

    Parameters
    ----------

    selectionIndex : int
      Passed on as it is.
    """
    #  void QAccessibleQuickItem::removeSelection(int selectionIndex)
    ritual = 'ritual_ZN20QAccessibleQuickItem15removeSelectionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleQuickItem15removeSelectionEi'
    self.uglySide.call(ritual, selectionIndex)

  @overload(int, int)
  def scrollToSubstring(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QAccessibleQuickItem::scrollToSubstring(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickitem.html#scrollToSubstring

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QAccessibleQuickItem::scrollToSubstring(int a0, int a1)
    ritual = 'ritual_ZN20QAccessibleQuickItem17scrollToSubstringEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleQuickItem17scrollToSubstringEii'
    self.uglySide.call(ritual, a0, a1)
