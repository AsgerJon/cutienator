"""
QAccessibleDisplay binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibleDisplay to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleImageInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QSize
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleDisplay(QAccessibleWidgetV2, QAccessibleImageInterface):
  """
  The cute side of Qt's QAccessibleDisplay: a plain Python object standing in
  front of one C++ QAccessibleDisplay.

  It is built on the cute 'QAccessibleWidgetV2', as Qt's QAccessibleDisplay
  is built on Qt's QAccessibleWidgetV2, and has everything that class has. It
  is built on the cute 'QAccessibleImageInterface' as well, as Qt's
  QAccessibleDisplay is built on Qt's QAccessibleImageInterface too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleDisplay that has a ritual and that Python
  can call so far, 6 names in all: 'text', 'role', 'state',
  'imageDescription', 'imageSize', 'imagePosition'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<std::pair<QAccessibleInterface *, QAccessible::Relation>>
    QAccessibleDisplay::relations(QAccessible::Relation match) const': gives
    a type Python has no way to take yet.
  - Qt's 'void *QAccessibleDisplay::interface_cast(QAccessible::InterfaceType
    t)': gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleDisplay is created at the first use, not by
    'QAccessibleDisplay(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleDisplay.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleDisplay'

  #  Qt's QAccessibleDisplay is built on more than one class. The part of a
  #  C++ QAccessibleDisplay that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleImageInterface':
          'ritual_cast_QAccessibleDisplay_QAccessibleImageInterface',
  }

  #  A C++ QAccessibleDisplay Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleDisplay'

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
    Calls Qt's 'QString QAccessibleDisplay::text(QAccessible::Text t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledisplay.html#text

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleDisplay::text(QAccessible::Text t) const
    ritual = 'ritual_ZNK18QAccessibleDisplay4textEN11QAccessible4TextE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleDisplay4textEN11QAccessible4TextE'
    return self.uglySide.call(ritual, t.value)

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleDisplay::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledisplay.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleDisplay::role() const
    ritual = 'ritual_ZNK18QAccessibleDisplay4roleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleDisplay4roleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QAccessibleDisplay::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledisplay.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QAccessibleDisplay::state() const
    ritual = 'ritual_ZNK18QAccessibleDisplay5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleDisplay5stateEv'
    address = self.uglySide.call(ritual)
    return QAccessible.State._cuteOwning(address)

  def imageDescription(self) -> str:
    """
    Calls Qt's 'QString QAccessibleDisplay::imageDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledisplay.html#imageDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleDisplay::imageDescription() const
    ritual = 'ritual_ZNK18QAccessibleDisplay16imageDescriptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleDisplay16imageDescriptionEv'
    return self.uglySide.call(ritual)

  def imageSize(self) -> QSize:
    """
    Calls Qt's 'QSize QAccessibleDisplay::imageSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibledisplay.html#imageSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAccessibleDisplay::imageSize() const
    ritual = 'ritual_ZNK18QAccessibleDisplay9imageSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleDisplay9imageSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def imagePosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAccessibleDisplay::imagePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledisplay.html#imagePosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAccessibleDisplay::imagePosition() const
    ritual = 'ritual_ZNK18QAccessibleDisplay13imagePositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAccessibleDisplay13imagePositionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

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
      w: Optional[QWidget],
      role: QAccessible.Role = QAccessible.Role.StaticText,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleDisplay::QAccessibleDisplay(QWidget *w, QAccessible::Role
    role)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibledisplay.html#QAccessibleDisplay

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : QAccessible.Role
      Passed on as its number. May be left out, as in Qt: it is then
      QAccessible.Role.StaticText.
    """
    #  QAccessibleDisplay::QAccessibleDisplay(QWidget *w, QAccessible::Role
    #      role)
    self._noteCreation(QAccessibleDisplay, lambda: Rituals.call(
        'ritual_ZN18QAccessibleDisplayC1EP7QWidgetN11QAccessible4RoleE',
        self._addressOf(w), role.value,
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
