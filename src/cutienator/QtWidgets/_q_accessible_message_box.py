"""
QAccessibleMessageBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleMessageBox to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMessageBox, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleMessageBox(QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleMessageBox: a plain Python object standing
  in front of one C++ QAccessibleMessageBox.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's
  QAccessibleMessageBox is built on Qt's QAccessibleWidgetV2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleMessageBox that has a ritual and that
  Python can call so far, 2 names in all: 'text', 'messageBox'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QAccessibleMessageBox is created at the first use, not by
    'QAccessibleMessageBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleMessageBox.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleMessageBox'

  #  A C++ QAccessibleMessageBox Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleMessageBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text)
  def text(self, t: QAccessible.Text) -> str:
    """
    Calls Qt's 'QString QAccessibleMessageBox::text(QAccessible::Text t)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblemessagebox.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleMessageBox::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK21QAccessibleMessageBox4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAccessibleMessageBox4textEN11QAccessible4TextE')
    return self.uglySide.call(ritual, t.value)

  def messageBox(self) -> Optional[QMessageBox]:
    """
    Calls Qt's 'QMessageBox *QAccessibleMessageBox::messageBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemessagebox.html#messageBox

    Returns
    -------

    Optional[QMessageBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMessageBox *QAccessibleMessageBox::messageBox() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccessibleMessageBox10messageBoxEv',
    )
    from . import QMessageBox
    return QMessageBox._cuteAt(address)

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
  def __init__(self, widget: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleMessageBox::QAccessibleMessageBox(QWidget *widget)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblemessagebox.html#QAccessibleMessageBox

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleMessageBox::QAccessibleMessageBox(QWidget *widget)
    self._noteCreation(QAccessibleMessageBox, lambda: Rituals.call(
        'ritual_ZN21QAccessibleMessageBoxC1EP7QWidget',
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
