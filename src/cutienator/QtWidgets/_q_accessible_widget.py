"""
QAccessibleWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleActionInterface
from ..QtGui import QAccessibleInterface, QAccessibleObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from ..QtGui import QColor, QWindow
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleWidget(QAccessibleObject, QAccessibleActionInterface):
  """
  The cute side of Qt's QAccessibleWidget: a plain Python object standing in
  front of one C++ QAccessibleWidget.

  It is built on the cute 'QAccessibleObject', as Qt's QAccessibleWidget is
  built on Qt's QAccessibleObject, and has everything that class has. It is
  built on the cute 'QAccessibleActionInterface' as well, as Qt's
  QAccessibleWidget is built on Qt's QAccessibleActionInterface too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleWidget that has a ritual and that Python
  can call so far, 14 names in all: 'isValid', 'window', 'childCount',
  'indexOfChild', 'focusChild', 'rect', 'parent', 'child', 'text', 'role',
  'state', 'foregroundColor', 'backgroundColor', 'doAction'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has no ritual
  ------------------

  10 of the 27 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 4 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QAccessibleWidget is created at the first use, not by
    'QAccessibleWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleWidget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleWidget'

  #  Qt's QAccessibleWidget is built on more than one class. The part of a
  #  C++ QAccessibleWidget that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleActionInterface':
          'ritual_cast_QAccessibleWidget_QAccessibleActionInterface',
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
    Calls Qt's 'bool QAccessibleWidget::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#isValid
    """
    #  bool QAccessibleWidget::isValid() const
    return self.uglySide.call('ritual_ZNK17QAccessibleWidget7isValidEv')

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QAccessibleWidget::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QAccessibleWidget::window() const
    address = self.uglySide.call('ritual_ZNK17QAccessibleWidget6windowEv')
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleWidget::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#childCount
    """
    #  int QAccessibleWidget::childCount() const
    return self.uglySide.call('ritual_ZNK17QAccessibleWidget10childCountEv')

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleWidget::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidget.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleWidget::indexOfChild(const QAccessibleInterface *child)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget12indexOfChildEPK20QAccessibleInterfa'
        'ce',
        self._addressOf(child),
    )

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleWidget::focusChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleWidget::focusChild() const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget10focusChildEv',
    )
    return QAccessibleInterface._cuteAt(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleWidget::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleWidget::rect() const
    address = self.uglySide.call('ritual_ZNK17QAccessibleWidget4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleWidget::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleWidget::parent() const
    address = self.uglySide.call('ritual_ZNK17QAccessibleWidget6parentEv')
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleWidget::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#child

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
    #  QAccessibleInterface *QAccessibleWidget::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleWidget::text(QAccessible::Text t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleWidget::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget4textEN11QAccessible4TextE', t.value,
    )

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleWidget::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleWidget::role() const
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget4roleEv',
    ))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleWidget::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleWidget::state() const
    address = self.uglySide.call('ritual_ZNK17QAccessibleWidget5stateEv')
    return QAccessible.State._cuteOwning(address)

  def foregroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAccessibleWidget::foregroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidget.html#foregroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAccessibleWidget::foregroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget15foregroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAccessibleWidget::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidget.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAccessibleWidget::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QAccessibleWidget15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, QAccessible.Role)
  @overload(NoneType, QAccessible.Role)
  def __init__(
      self,
      o: Optional[QWidget],
      r: QAccessible.Role = QAccessible.Role.Client,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidget.html#QAccessibleWidget

    Parameters
    ----------

    o : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : QAccessible.Role
      Passed on as its number. May be left out, as in Qt: it is then
      QAccessible.Role.Client.
    """
    #  QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r)
    self._noteCreation(QAccessibleWidget, lambda: Rituals.call(
        'ritual_ZN17QAccessibleWidgetC1EP7QWidgetN11QAccessible4RoleE',
        self._addressOf(o), r.value,
    ))

  @overload(QWidget, QAccessible.Role, str)
  @overload(NoneType, QAccessible.Role, str)
  def __init__(
      self,
      o: Optional[QWidget],
      r: QAccessible.Role,
      name: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r,
    const QString &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidget.html#QAccessibleWidget

    Parameters
    ----------

    o : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : QAccessible.Role
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleWidget::QAccessibleWidget(QWidget *o, QAccessible::Role r,
    #      const QString &name)
    self._noteCreation(QAccessibleWidget, lambda: Rituals.call(
        'ritual_ZN17QAccessibleWidgetC1EP7QWidgetN11QAccessible4RoleERK7QSt'
        'ring',
        self._addressOf(o), r.value, name,
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
    Calls Qt's 'void QAccessibleWidget::doAction(const QString &actionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblewidget.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleWidget::doAction(const QString &actionName)
    self.uglySide.call(
        'ritual_ZN17QAccessibleWidget8doActionERK7QString', actionName,
    )
