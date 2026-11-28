"""
QAccessibleDockWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleDockWidget to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtGui import QAccessible, QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from . import QDockWidget, QDockWidgetLayout

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleDockWidget(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleDockWidget: a plain Python object standing
  in front of one C++ QAccessibleDockWidget.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleDockWidget is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleDockWidget that has a ritual and that
  Python can call so far, 8 names in all: 'child', 'indexOfChild',
  'childCount', 'rect', 'text', 'role', 'dockWidget', 'dockWidgetLayout'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 leans on 'QAccessibleDockWidget.

  What to expect
  --------------

  - The C++ QAccessibleDockWidget is created at the first use, not by
    'QAccessibleDockWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleDockWidget.
  - Each name of Qt's QAccessibleDockWidget that has no cute function yet,
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
  __qt_class__ = 'QAccessibleDockWidget'

  #  A C++ QAccessibleDockWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleDockWidget'

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
    Calls Qt's 'QAccessibleInterface *QAccessibleDockWidget::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledockwidget.html#child

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
    #  QAccessibleInterface *QAccessibleDockWidget::child(int index) const
    ritual = 'ritual_ZNK21QAccessibleDockWidget5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleDockWidget5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleDockWidget::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledockwidget.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleDockWidget::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK21QAccessibleDockWidget12indexOfChildEPK20QAccessibleInt'
        'erface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAccessibleDockWidget12indexOfChildEPK20QAccessi'
          'bleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleDockWidget::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledockwidget.html#childCount
    """
    #  int QAccessibleDockWidget::childCount() const
    ritual = 'ritual_ZNK21QAccessibleDockWidget10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleDockWidget10childCountEv'
    return self.uglySide.call(ritual)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleDockWidget::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledockwidget.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleDockWidget::rect() const
    ritual = 'ritual_ZNK21QAccessibleDockWidget4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleDockWidget4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleDockWidget::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledockwidget.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleDockWidget::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK21QAccessibleDockWidget4textEN11QAccessible4TextE',
        t.value,
    )

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleDockWidget::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledockwidget.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleDockWidget::role() const
    ritual = 'ritual_ZNK21QAccessibleDockWidget4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAccessibleDockWidget4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def dockWidget(self) -> Optional[QDockWidget]:
    """
    Calls Qt's 'QDockWidget *QAccessibleDockWidget::dockWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledockwidget.html#dockWidget

    Returns
    -------

    Optional[QDockWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockWidget *QAccessibleDockWidget::dockWidget() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleDockWidget10dockWidgetEv',
    )
    from . import QDockWidget
    return QDockWidget._cuteAt(address)

  def dockWidgetLayout(self) -> Optional[QDockWidgetLayout]:
    """
    Calls Qt's 'QDockWidgetLayout *QAccessibleDockWidget::dockWidgetLayout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledockwidget.html#dockWidgetLayout

    Returns
    -------

    Optional[QDockWidgetLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDockWidgetLayout *QAccessibleDockWidget::dockWidgetLayout() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleDockWidget16dockWidgetLayoutEv',
    )
    from . import QDockWidgetLayout
    return QDockWidgetLayout._cuteAt(address)

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
    Qt's 'QAccessibleDockWidget::QAccessibleDockWidget(QWidget *widget)':
    leans on 'QAccessibleDockWidget::text(QAccessible::Text) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleDockWidget.__init__' has no cute function yet. Qt's "
        "'QAccessibleDockWidget::QAccessibleDockWidget(QWidget *widget)': "
        "leans on 'QAccessibleDockWidget::text(QAccessible::Text) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
