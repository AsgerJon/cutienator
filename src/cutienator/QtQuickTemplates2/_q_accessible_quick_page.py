"""
QAccessibleQuickPage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickpage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickPage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QList
from ..QtGui import QAccessibleInterface
from . import QAccessibleQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick import QQuickItem
  from . import QQuickPage

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickPage(QAccessibleQuickControl):
  """
  The cute side of Qt's QAccessibleQuickPage: a plain Python object standing
  in front of one C++ QAccessibleQuickPage.

  It is built on the cute 'QAccessibleQuickControl', as Qt's
  QAccessibleQuickPage is built on Qt's QAccessibleQuickControl, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickPage that has a ritual and that
  Python can call so far, 4 names in all: 'child', 'indexOfChild', 'page',
  'orderedChildItems'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleQuickControl.

  What to expect
  --------------

  - The C++ QAccessibleQuickPage is created at the first use, not by
    'QAccessibleQuickPage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickPage.
  - Each name of Qt's QAccessibleQuickPage that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickPage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleQuickPage::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickpage.html#child

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
    #  QAccessibleInterface *QAccessibleQuickPage::child(int index) const
    ritual = 'ritual_ZNK20QAccessibleQuickPage5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleQuickPage5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleQuickPage::indexOfChild(const
    QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickpage.html#indexOfChild

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleQuickPage::indexOfChild(const QAccessibleInterface
    #      *iface) const
    ritual = (
        'ritual_ZNK20QAccessibleQuickPage12indexOfChildEPK20QAccessibleInte'
        'rface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAccessibleQuickPage12indexOfChildEPK20QAccessib'
          'leInterface')
    return self.uglySide.call(
        ritual, self._addressOf(iface, 'QAccessibleInterface'),
    )

  def page(self) -> Optional[QQuickPage]:
    """
    Calls Qt's 'QQuickPage *QAccessibleQuickPage::page() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickpage.html#page

    Returns
    -------

    Optional[QQuickPage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPage *QAccessibleQuickPage::page() const
    address = self.uglySide.call('ritual_ZNK20QAccessibleQuickPage4pageEv')
    from . import QQuickPage
    return QQuickPage._cuteAt(address)

  def orderedChildItems(self) -> QList[QQuickItem]:
    """
    Calls Qt's 'QList<QQuickItem *> QAccessibleQuickPage::orderedChildItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickpage.html#orderedChildItems

    Returns
    -------

    QList[QQuickItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickItem *> QAccessibleQuickPage::orderedChildItems() const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleQuickPage17orderedChildItemsEv',
    )
    from ..QtQuick import QQuickItem
    return QList[QQuickItem]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAccessibleQuickPage::QAccessibleQuickPage(QQuickPage *page)':
    leans on 'non-virtual thunk to QAccessibleQuickControl::attributeKeys()
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleQuickPage.__init__' has no cute function yet. Qt's "
        "'QAccessibleQuickPage::QAccessibleQuickPage(QQuickPage *page)': "
        "leans on 'non-virtual thunk to "
        "QAccessibleQuickControl::attributeKeys() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
