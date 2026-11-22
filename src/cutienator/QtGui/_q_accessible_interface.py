"""
QAccessibleInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QAccessible

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRect
  from . import QAccessibleActionInterface, QAccessibleAttributesInterface
  from . import QAccessibleEditableTextInterface
  from . import QAccessibleHyperlinkInterface, QAccessibleImageInterface
  from . import QAccessibleSelectionInterface, QAccessibleTableCellInterface
  from . import QAccessibleTableInterface, QAccessibleTextInterface
  from . import QAccessibleValueInterface, QAccessibleViewportInterface
  from . import QColor, QWindow

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleInterface: a plain Python object standing
  in front of one C++ QAccessibleInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleInterface that has a ritual and that
  Python can call so far, 27 names in all: 'isValid', 'object', 'window',
  'focusChild', 'childAt', 'parent', 'child', 'childCount', 'indexOfChild',
  'text', 'setText', 'rect', 'role', 'state', 'foregroundColor',
  'backgroundColor', 'textInterface', 'editableTextInterface',
  'valueInterface', 'actionInterface', 'imageInterface', 'tableInterface',
  'tableCellInterface', 'hyperlinkInterface', 'selectionInterface',
  'attributesInterface', 'viewportInterface'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  9 of the 36 functions Qt declares: 4 forbidden; 3 takes or gives a type
  that cannot be passed yet; 2 protected.

  What to expect
  --------------

  - The C++ QAccessibleInterface is created at the first use, not by
    'QAccessibleInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleInterface'

  #  A C++ QAccessibleInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleInterface'

  #  The functions Qt calls itself that QAccessibleInterface is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'relations': (
          'QList<std::pair<QAccessibleInterface *, QAccessible::Relation>> '
          'QAccessibleInterface::relations(QAccessible::Relation) const',
      ),
      'text': (
          'QString QAccessibleInterface::text(QAccessible::Text) const',
      ),
      'setText': (
          'void QAccessibleInterface::setText(QAccessible::Text, const '
          'QString &)',
      ),
      'virtual_hook': (
          'void QAccessibleInterface::virtual_hook(int, void *)',
      ),
      'interface_cast': (
          'void '
          '*QAccessibleInterface::interface_cast(QAccessible::InterfaceType'
          ')',
      ),
  }

  #  The functions Qt calls itself that QAccessibleInterface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZNK20QAccessibleInterface7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'object': (
          ('_ZNK20QAccessibleInterface6objectEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'window': (
          ('_ZNK20QAccessibleInterface6windowEv',
           ('address', 'address', 'QtGui:QWindow'),
           ()),
      ),
      'focusChild': (
          ('_ZNK20QAccessibleInterface10focusChildEv',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           ()),
      ),
      'childAt': (
          ('_ZNK20QAccessibleInterface7childAtEii',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'parent': (
          ('_ZNK20QAccessibleInterface6parentEv',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           ()),
      ),
      'child': (
          ('_ZNK20QAccessibleInterface5childEi',
           ('address', 'address', 'QtGui:QAccessibleInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'childCount': (
          ('_ZNK20QAccessibleInterface10childCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'indexOfChild': (
          ('_ZNK20QAccessibleInterface12indexOfChildEPKS_',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtGui:QAccessibleInterface'),
           )),
      ),
      'rect': (
          ('_ZNK20QAccessibleInterface4rectEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'role': (
          ('_ZNK20QAccessibleInterface4roleEv',
           ('int', 'enum', 'QtGui:QAccessible.Role'),
           ()),
      ),
      'state': (
          ('_ZNK20QAccessibleInterface5stateEv',
           ('address', 'value', 'QtGui:QAccessible.State'),
           ()),
      ),
      'foregroundColor': (
          ('_ZNK20QAccessibleInterface15foregroundColorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
      'backgroundColor': (
          ('_ZNK20QAccessibleInterface15backgroundColorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
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
    Calls Qt's 'bool QAccessibleInterface::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#isValid
    """
    #  bool QAccessibleInterface::isValid() const
    return self.uglySide.call('ritual_ZNK20QAccessibleInterface7isValidEv')

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleInterface::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleInterface::object() const
    address = self.uglySide.call('ritual_ZNK20QAccessibleInterface6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QAccessibleInterface::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QAccessibleInterface::window() const
    ritual = 'ritual_ZNK20QAccessibleInterface6windowEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleInterface6windowEv'
    address = self.uglySide.call(ritual)
    from . import QWindow
    return QWindow._cuteAt(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleInterface::focusChild()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleInterface::focusChild() const
    ritual = 'ritual_ZNK20QAccessibleInterface10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleInterface10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleInterface::childAt(int x,
    int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#childAt

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
    #  QAccessibleInterface *QAccessibleInterface::childAt(int x, int y)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleInterface7childAtEii', x, y,
    )
    return QAccessibleInterface._cuteAt(address)

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleInterface::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleInterface::parent() const
    address = self.uglySide.call('ritual_ZNK20QAccessibleInterface6parentEv')
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleInterface::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#child

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
    #  QAccessibleInterface *QAccessibleInterface::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK20QAccessibleInterface5childEi', index,
    )
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleInterface::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#childCount
    """
    #  int QAccessibleInterface::childCount() const
    return self.uglySide.call(
        'ritual_ZNK20QAccessibleInterface10childCountEv',
    )

  @overload(THIS)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleInterface::indexOfChild(const
    QAccessibleInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleInterface::indexOfChild(const QAccessibleInterface *a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QAccessibleInterface12indexOfChildEPKS_',
        self._addressOf(a0),
    )

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleInterface::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleInterface::text(QAccessible::Text t) const
    return self.uglySide.call(
        'ritual_ZNK20QAccessibleInterface4textEN11QAccessible4TextE',
        t.value,
    )

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleInterface::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleInterface::rect() const
    address = self.uglySide.call('ritual_ZNK20QAccessibleInterface4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleInterface::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleInterface::role() const
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK20QAccessibleInterface4roleEv',
    ))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleInterface::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleInterface::state() const
    address = self.uglySide.call('ritual_ZNK20QAccessibleInterface5stateEv')
    return QAccessible.State._cuteOwning(address)

  def foregroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAccessibleInterface::foregroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#foregroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAccessibleInterface::foregroundColor() const
    ritual = 'ritual_ZNK20QAccessibleInterface15foregroundColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleInterface15foregroundColorEv'
    address = self.uglySide.call(ritual)
    from . import QColor
    return QColor._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAccessibleInterface::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAccessibleInterface::backgroundColor() const
    ritual = 'ritual_ZNK20QAccessibleInterface15backgroundColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAccessibleInterface15backgroundColorEv'
    address = self.uglySide.call(ritual)
    from . import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleInterface::setText(QAccessible::Text t, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleinterface.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleInterface::setText(QAccessible::Text t, const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QSt'
        'ring',
        t.value, text,
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

  def textInterface(self) -> Optional[QAccessibleTextInterface]:
    """
    Calls Qt's 'QAccessibleTextInterface
    *QAccessibleInterface::textInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#textInterface

    Returns
    -------

    Optional[QAccessibleTextInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleTextInterface *QAccessibleInterface::textInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface13textInterfaceEv',
    )
    from . import QAccessibleTextInterface
    return QAccessibleTextInterface._cuteAt(address)

  def editableTextInterface(
      self,
  ) -> Optional[QAccessibleEditableTextInterface]:
    """
    Calls Qt's 'QAccessibleEditableTextInterface
    *QAccessibleInterface::editableTextInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#editableTextInterface

    Returns
    -------

    Optional[QAccessibleEditableTextInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleEditableTextInterface
    #      *QAccessibleInterface::editableTextInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface21editableTextInterfaceEv',
    )
    from . import QAccessibleEditableTextInterface
    return QAccessibleEditableTextInterface._cuteAt(address)

  def valueInterface(self) -> Optional[QAccessibleValueInterface]:
    """
    Calls Qt's 'QAccessibleValueInterface
    *QAccessibleInterface::valueInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#valueInterface

    Returns
    -------

    Optional[QAccessibleValueInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleValueInterface *QAccessibleInterface::valueInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface14valueInterfaceEv',
    )
    from . import QAccessibleValueInterface
    return QAccessibleValueInterface._cuteAt(address)

  def actionInterface(self) -> Optional[QAccessibleActionInterface]:
    """
    Calls Qt's 'QAccessibleActionInterface
    *QAccessibleInterface::actionInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#actionInterface

    Returns
    -------

    Optional[QAccessibleActionInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleActionInterface *QAccessibleInterface::actionInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface15actionInterfaceEv',
    )
    from . import QAccessibleActionInterface
    return QAccessibleActionInterface._cuteAt(address)

  def imageInterface(self) -> Optional[QAccessibleImageInterface]:
    """
    Calls Qt's 'QAccessibleImageInterface
    *QAccessibleInterface::imageInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#imageInterface

    Returns
    -------

    Optional[QAccessibleImageInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleImageInterface *QAccessibleInterface::imageInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface14imageInterfaceEv',
    )
    from . import QAccessibleImageInterface
    return QAccessibleImageInterface._cuteAt(address)

  def tableInterface(self) -> Optional[QAccessibleTableInterface]:
    """
    Calls Qt's 'QAccessibleTableInterface
    *QAccessibleInterface::tableInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#tableInterface

    Returns
    -------

    Optional[QAccessibleTableInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleTableInterface *QAccessibleInterface::tableInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface14tableInterfaceEv',
    )
    from . import QAccessibleTableInterface
    return QAccessibleTableInterface._cuteAt(address)

  def tableCellInterface(self) -> Optional[QAccessibleTableCellInterface]:
    """
    Calls Qt's 'QAccessibleTableCellInterface
    *QAccessibleInterface::tableCellInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#tableCellInterface

    Returns
    -------

    Optional[QAccessibleTableCellInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleTableCellInterface
    #      *QAccessibleInterface::tableCellInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface18tableCellInterfaceEv',
    )
    from . import QAccessibleTableCellInterface
    return QAccessibleTableCellInterface._cuteAt(address)

  def hyperlinkInterface(self) -> Optional[QAccessibleHyperlinkInterface]:
    """
    Calls Qt's 'QAccessibleHyperlinkInterface
    *QAccessibleInterface::hyperlinkInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#hyperlinkInterface

    Returns
    -------

    Optional[QAccessibleHyperlinkInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleHyperlinkInterface
    #      *QAccessibleInterface::hyperlinkInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface18hyperlinkInterfaceEv',
    )
    from . import QAccessibleHyperlinkInterface
    return QAccessibleHyperlinkInterface._cuteAt(address)

  def selectionInterface(self) -> Optional[QAccessibleSelectionInterface]:
    """
    Calls Qt's 'QAccessibleSelectionInterface
    *QAccessibleInterface::selectionInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#selectionInterface

    Returns
    -------

    Optional[QAccessibleSelectionInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleSelectionInterface
    #      *QAccessibleInterface::selectionInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface18selectionInterfaceEv',
    )
    from . import QAccessibleSelectionInterface
    return QAccessibleSelectionInterface._cuteAt(address)

  def attributesInterface(self) -> Optional[QAccessibleAttributesInterface]:
    """
    Calls Qt's 'QAccessibleAttributesInterface
    *QAccessibleInterface::attributesInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#attributesInterface

    Returns
    -------

    Optional[QAccessibleAttributesInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleAttributesInterface
    #      *QAccessibleInterface::attributesInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface19attributesInterfaceEv',
    )
    from . import QAccessibleAttributesInterface
    return QAccessibleAttributesInterface._cuteAt(address)

  def viewportInterface(self) -> Optional[QAccessibleViewportInterface]:
    """
    Calls Qt's 'QAccessibleViewportInterface
    *QAccessibleInterface::viewportInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleinterface.html#viewportInterface

    Returns
    -------

    Optional[QAccessibleViewportInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleViewportInterface
    #      *QAccessibleInterface::viewportInterface()
    address = self.uglySide.call(
        'ritual_ZN20QAccessibleInterface17viewportInterfaceEv',
    )
    from . import QAccessibleViewportInterface
    return QAccessibleViewportInterface._cuteAt(address)
