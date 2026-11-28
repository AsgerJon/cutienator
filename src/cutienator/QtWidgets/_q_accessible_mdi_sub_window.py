"""
QAccessibleMdiSubWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleMdiSubWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from . import QMdiSubWindow, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMdiSubWindow(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleMdiSubWindow: a plain Python object
  standing in front of one C++ QAccessibleMdiSubWindow.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleMdiSubWindow is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMdiSubWindow that has a ritual and that
  Python can call so far, 8 names in all: 'text', 'setText', 'state',
  'childCount', 'child', 'indexOfChild', 'rect', 'mdiSubWindow'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleMdiSubWindow is created at the first use, not by
    'QAccessibleMdiSubWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMdiSubWindow.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleMdiSubWindow'

  #  A C++ QAccessibleMdiSubWindow Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMdiSubWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text)
  def text(self, textType: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleMdiSubWindow::text(QAccessible::Text
    textType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#text

    Parameters
    ----------

    textType : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleMdiSubWindow::text(QAccessible::Text textType)
    #      const
    ritual = 'ritual_ZNK23QAccessibleMdiSubWindow4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAccessibleMdiSubWindow4textEN11QAccessible4Text'
          'E')
    return self.uglySide.call(ritual, textType.value)

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleMdiSubWindow::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleMdiSubWindow::state() const
    ritual = 'ritual_ZNK23QAccessibleMdiSubWindow5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAccessibleMdiSubWindow5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleMdiSubWindow::childCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#childCount
    """
    #  int QAccessibleMdiSubWindow::childCount() const
    ritual = 'ritual_ZNK23QAccessibleMdiSubWindow10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAccessibleMdiSubWindow10childCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleMdiSubWindow::child(int
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#child

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
    #  QAccessibleInterface *QAccessibleMdiSubWindow::child(int index) const
    ritual = 'ritual_ZNK23QAccessibleMdiSubWindow5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAccessibleMdiSubWindow5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleMdiSubWindow::indexOfChild(const
    QAccessibleInterface *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#indexOfChild

    Parameters
    ----------

    child : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleMdiSubWindow::indexOfChild(const QAccessibleInterface
    #      *child) const
    ritual = (
        'ritual_ZNK23QAccessibleMdiSubWindow12indexOfChildEPK20QAccessibleI'
        'nterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAccessibleMdiSubWindow12indexOfChildEPK20QAcces'
          'sibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(child, 'QAccessibleInterface'),
    )

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleMdiSubWindow::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleMdiSubWindow::rect() const
    ritual = 'ritual_ZNK23QAccessibleMdiSubWindow4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAccessibleMdiSubWindow4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def mdiSubWindow(self) -> Optional[QMdiSubWindow]:
    """
    Calls Qt's 'QMdiSubWindow *QAccessibleMdiSubWindow::mdiSubWindow()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#mdiSubWindow

    Returns
    -------

    Optional[QMdiSubWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiSubWindow *QAccessibleMdiSubWindow::mdiSubWindow() const
    address = self.uglySide.call(
        'ritual_ZNK23QAccessibleMdiSubWindow12mdiSubWindowEv',
    )
    from . import QMdiSubWindow
    return QMdiSubWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, textType: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleMdiSubWindow::setText(QAccessible::Text
    textType, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html#setText

    Parameters
    ----------

    textType : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleMdiSubWindow::setText(QAccessible::Text textType,
    #      const QString &text)
    ritual = (
        'ritual_ZN23QAccessibleMdiSubWindow7setTextEN11QAccessible4TextERK7'
        'QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAccessibleMdiSubWindow7setTextEN11QAccessible4Te'
          'xtERK7QString')
    self.uglySide.call(ritual, textType.value, text)

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
  def __init__(self, widget: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleMdiSubWindow::QAccessibleMdiSubWindow(QWidget *widget)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemdisubwindow.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleMdiSubWindow::QAccessibleMdiSubWindow(QWidget *widget)
    self._noteCreation(QAccessibleMdiSubWindow, lambda: Rituals.call(
        'ritual_ZN23QAccessibleMdiSubWindowC1EP7QWidget',
        self._addressOf(widget),
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
