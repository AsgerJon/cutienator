"""
QAccessibleTableCell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleTableCell to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from ..QtGui import QAccessible, QAccessibleActionInterface
from ..QtGui import QAccessibleInterface, QAccessibleTableCellInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QModelIndex, QObject, QRect
  from . import QAbstractItemView, QHeaderView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemView = WAIT['QAbstractItemView']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTableCell(QAccessibleInterface, QAccessibleTableCellInterface, QAccessibleActionInterface):
  """
  The cute side of Qt's QAccessibleTableCell: a plain Python object standing
  in front of one C++ QAccessibleTableCell.

  It is built on the cute 'QAccessibleInterface', as Qt's
  QAccessibleTableCell is built on Qt's QAccessibleInterface, and has
  everything that class has. It is built on the cute
  'QAccessibleTableCellInterface' as well, as Qt's QAccessibleTableCell is
  built on Qt's QAccessibleTableCellInterface too, and has everything that
  class has. It is built on the cute 'QAccessibleActionInterface' as well, as
  Qt's QAccessibleTableCell is built on Qt's QAccessibleActionInterface too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTableCell that has a ritual and that
  Python can call so far, 27 names in all: 'object', 'role', 'state', 'rect',
  'isValid', 'childAt', 'childCount', 'indexOfChild', 'text', 'setText',
  'parent', 'child', 'columnExtent', 'columnHeaderCells', 'columnIndex',
  'rowExtent', 'rowHeaderCells', 'rowIndex', 'isSelected', 'table',
  'actionNames', 'doAction', 'keyBindingsForAction', 'verticalHeader',
  'horizontalHeader', 'selectCell', 'unselectCell'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleTableCell::interface_cast(QAccessible::InterfaceType t)':
    gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleTableCell is created at the first use, not by
    'QAccessibleTableCell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTableCell.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTableCell'

  #  Qt's QAccessibleTableCell is built on more than one class. The part of a
  #  C++ QAccessibleTableCell that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleTableCellInterface':
          'ritual_cast_QAccessibleTableCell_QAccessibleTableCellInterface',
      'QAccessibleActionInterface':
          'ritual_cast_QAccessibleTableCell_QAccessibleActionInterface',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleTableCell::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleTableCell::object() const
    ritual = 'ritual_ZNK20QAccessibleTableCell6objectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell6objectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleTableCell::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleTableCell::role() const
    ritual = 'ritual_ZNK20QAccessibleTableCell4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleTableCell::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleTableCell::state() const
    ritual = 'ritual_ZNK20QAccessibleTableCell5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleTableCell::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleTableCell::rect() const
    ritual = 'ritual_ZNK20QAccessibleTableCell4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableCell::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#isValid
    """
    #  bool QAccessibleTableCell::isValid() const
    ritual = 'ritual_ZNK20QAccessibleTableCell7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell7isValidEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, a0: int, a1: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCell::childAt(int a0,
    int a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#childAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCell::childAt(int a0, int a1)
    #      const
    ritual = 'ritual_ZNK20QAccessibleTableCell7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell7childAtEii'
    address = self.uglySide.call(ritual, a0, a1)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCell::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#childCount
    """
    #  int QAccessibleTableCell::childCount() const
    ritual = 'ritual_ZNK20QAccessibleTableCell10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleTableCell::indexOfChild(const
    QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleTableCell::indexOfChild(const QAccessibleInterface *a0)
    #      const
    ritual = (
        'ritual_ZNK20QAccessibleTableCell12indexOfChildEPK20QAccessibleInte'
        'rface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleTableCell12indexOfChildEPK20QAccessib'
          'leInterface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleTableCell::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTableCell::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK20QAccessibleTableCell4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleTableCell4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCell::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCell::parent() const
    ritual = 'ritual_ZNK20QAccessibleTableCell6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, a0: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCell::child(int a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#child

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCell::child(int a0) const
    ritual = 'ritual_ZNK20QAccessibleTableCell5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell5childEi'
    address = self.uglySide.call(ritual, a0)
    return QAccessibleInterface._cuteAt(address)

  def columnExtent(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCell::columnExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#columnExtent
    """
    #  int QAccessibleTableCell::columnExtent() const
    ritual = 'ritual_ZNK20QAccessibleTableCell12columnExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell12columnExtentEv'
    return self.uglySide.call(ritual)

  def columnHeaderCells(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTableCell::columnHeaderCells() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#columnHeaderCells

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *>
    #      QAccessibleTableCell::columnHeaderCells() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleTableCell17columnHeaderCellsEv',
    )
    return QList[QAccessibleInterface]._cuteOwning(address)

  def columnIndex(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCell::columnIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#columnIndex
    """
    #  int QAccessibleTableCell::columnIndex() const
    ritual = 'ritual_ZNK20QAccessibleTableCell11columnIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell11columnIndexEv'
    return self.uglySide.call(ritual)

  def rowExtent(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCell::rowExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#rowExtent
    """
    #  int QAccessibleTableCell::rowExtent() const
    ritual = 'ritual_ZNK20QAccessibleTableCell9rowExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell9rowExtentEv'
    return self.uglySide.call(ritual)

  def rowHeaderCells(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTableCell::rowHeaderCells() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#rowHeaderCells

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *> QAccessibleTableCell::rowHeaderCells()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleTableCell14rowHeaderCellsEv',
    )
    return QList[QAccessibleInterface]._cuteOwning(address)

  def rowIndex(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableCell::rowIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#rowIndex
    """
    #  int QAccessibleTableCell::rowIndex() const
    ritual = 'ritual_ZNK20QAccessibleTableCell8rowIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell8rowIndexEv'
    return self.uglySide.call(ritual)

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableCell::isSelected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#isSelected
    """
    #  bool QAccessibleTableCell::isSelected() const
    ritual = 'ritual_ZNK20QAccessibleTableCell10isSelectedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell10isSelectedEv'
    return self.uglySide.call(ritual)

  def table(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableCell::table() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#table

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableCell::table() const
    ritual = 'ritual_ZNK20QAccessibleTableCell5tableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleTableCell5tableEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def actionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleTableCell::actionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#actionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleTableCell::actionNames() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleTableCell11actionNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def keyBindingsForAction(self, actionName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QAccessibleTableCell::keyBindingsForAction(const
    QString &actionName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#keyBindingsForAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAccessibleTableCell::keyBindingsForAction(const QString
    #      &actionName) const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleTableCell20keyBindingsForActionERK7QString',
        actionName,
    )
    return QStringList._cuteOwning(address)

  def verticalHeader(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QAccessibleTableCell::verticalHeader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#verticalHeader

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QAccessibleTableCell::verticalHeader() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleTableCell14verticalHeaderEv',
    )
    from . import QHeaderView
    return QHeaderView._cuteAt(address)

  def horizontalHeader(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QAccessibleTableCell::horizontalHeader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#horizontalHeader

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QAccessibleTableCell::horizontalHeader() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleTableCell16horizontalHeaderEv',
    )
    from . import QHeaderView
    return QHeaderView._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleTableCell::setText(QAccessible::Text t, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTableCell::setText(QAccessible::Text t, const QString
    #      &text)
    ritual = (
        'ritual_ZN20QAccessibleTableCell7setTextEN11QAccessible4TextERK7QSt'
        'ring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAccessibleTableCell7setTextEN11QAccessible4TextE'
          'RK7QString')
    self.uglySide.call(ritual, t.value, text)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemView, QModelIndex, QAccessible.Role)
  @overload(NoneType, QModelIndex, QAccessible.Role)
  def __init__(
      self,
      view: Optional[QAbstractItemView],
      m_index: QModelIndex,
      role: QAccessible.Role,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTableCell::QAccessibleTableCell(QAbstractItemView *view,
    const QModelIndex &m_index, QAccessible::Role role)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#QAccessibleTableCell

    Parameters
    ----------

    view : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m_index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : QAccessible.Role
      Passed on as its number.
    """
    #  QAccessibleTableCell::QAccessibleTableCell(QAbstractItemView *view,
    #      const QModelIndex &m_index, QAccessible::Role role)
    self._noteCreation(QAccessibleTableCell, lambda: Rituals.call(
        'ritual_ZN20QAccessibleTableCellC1EP17QAbstractItemViewRK11QModelIn'
        'dexN11QAccessible4RoleE',
        self._addressOf(view), self._valueOf(m_index), role.value,
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
    Calls Qt's 'void QAccessibleTableCell::doAction(const QString
    &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletablecell.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTableCell::doAction(const QString &actionName)
    ritual = 'ritual_ZN20QAccessibleTableCell8doActionERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccessibleTableCell8doActionERK7QString'
    self.uglySide.call(ritual, actionName)

  def selectCell(self) -> None:
    """
    Calls Qt's 'void QAccessibleTableCell::selectCell()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#selectCell
    """
    #  void QAccessibleTableCell::selectCell()
    self.uglySide.call('ritual_ZN20QAccessibleTableCell10selectCellEv')

  def unselectCell(self) -> None:
    """
    Calls Qt's 'void QAccessibleTableCell::unselectCell()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletablecell.html#unselectCell
    """
    #  void QAccessibleTableCell::unselectCell()
    self.uglySide.call('ritual_ZN20QAccessibleTableCell12unselectCellEv')
