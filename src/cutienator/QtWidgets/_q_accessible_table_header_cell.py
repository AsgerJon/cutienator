"""
QAccessibleTableHeaderCell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleTableHeaderCell to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible, QAccessibleInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRect
  from . import QAbstractItemView, QHeaderView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemView = WAIT['QAbstractItemView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTableHeaderCell(QAccessibleInterface):
  """
  The cute side of Qt's QAccessibleTableHeaderCell: a plain Python object
  standing in front of one C++ QAccessibleTableHeaderCell.

  It is built on the cute 'QAccessibleInterface', as Qt's
  QAccessibleTableHeaderCell is built on Qt's QAccessibleInterface, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTableHeaderCell that has a ritual and
  that Python can call so far, 13 names in all: 'object', 'role', 'state',
  'rect', 'isValid', 'childAt', 'childCount', 'indexOfChild', 'text',
  'setText', 'parent', 'child', 'headerView'. It can be made from Python, in
  1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleTableHeaderCell is created at the first use, not by
    'QAccessibleTableHeaderCell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTableHeaderCell.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTableHeaderCell'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleTableHeaderCell::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleTableHeaderCell::object() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell6objectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell6objectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleTableHeaderCell::role() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleTableHeaderCell::role() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleTableHeaderCell::state()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleTableHeaderCell::state() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleTableHeaderCell::rect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleTableHeaderCell::rect() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTableHeaderCell::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#isValid
    """
    #  bool QAccessibleTableHeaderCell::isValid() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell7isValidEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def childAt(self, a0: int, a1: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableHeaderCell::childAt(int
    a0, int a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#childAt

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
    #  QAccessibleInterface *QAccessibleTableHeaderCell::childAt(int a0, int
    #      a1) const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell7childAtEii'
    address = self.uglySide.call(ritual, a0, a1)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTableHeaderCell::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#childCount
    """
    #  int QAccessibleTableHeaderCell::childCount() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleTableHeaderCell::indexOfChild(const
    QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleTableHeaderCell::indexOfChild(const
    #      QAccessibleInterface *a0) const
    ritual = (
        'ritual_ZNK26QAccessibleTableHeaderCell12indexOfChildEPK20QAccessib'
        'leInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleTableHeaderCell12indexOfChildEPK20QAc'
          'cessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleTableHeaderCell::text(QAccessible::Text t)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTableHeaderCell::text(QAccessible::Text t) const
    ritual = (
        'ritual_ZNK26QAccessibleTableHeaderCell4textEN11QAccessible4TextE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QAccessibleTableHeaderCell4textEN11QAccessible4T'
          'extE')
    return self.uglySide.call(ritual, t.value)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableHeaderCell::parent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTableHeaderCell::parent() const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTableHeaderCell::child(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#child

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
    #  QAccessibleInterface *QAccessibleTableHeaderCell::child(int index)
    #      const
    ritual = 'ritual_ZNK26QAccessibleTableHeaderCell5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QAccessibleTableHeaderCell5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  def headerView(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QAccessibleTableHeaderCell::headerView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#headerView

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QAccessibleTableHeaderCell::headerView() const
    address = self.uglySide.call(
        'ritual_ZNK26QAccessibleTableHeaderCell10headerViewEv',
    )
    from . import QHeaderView
    return QHeaderView._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleTableHeaderCell::setText(QAccessible::Text t,
    const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleTableHeaderCell::setText(QAccessible::Text t, const
    #      QString &text)
    ritual = (
        'ritual_ZN26QAccessibleTableHeaderCell7setTextEN11QAccessible4TextE'
        'RK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAccessibleTableHeaderCell7setTextEN11QAccessible'
          '4TextERK7QString')
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

  @overload(QAbstractItemView, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def __init__(
      self,
      view: Optional[QAbstractItemView],
      index: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleTableHeaderCell::QAccessibleTableHeaderCell(QAbstractItemView
    *view, int index, Qt::Orientation orientation)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletableheadercell.html

    Parameters
    ----------

    view : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  QAccessibleTableHeaderCell::QAccessibleTableHeaderCell(
    #      QAbstractItemView *view, int index, Qt::Orientation orientation)
    self._noteCreation(QAccessibleTableHeaderCell, lambda: Rituals.call(
        'ritual_ZN26QAccessibleTableHeaderCellC1EP17QAbstractItemViewiN2Qt1'
        '1OrientationE',
        self._addressOf(view), index, orientation.value,
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
