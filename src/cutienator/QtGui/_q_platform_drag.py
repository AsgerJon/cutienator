"""
QPlatformDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdrag.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDrag, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDrag = WAIT['QDrag']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformDrag(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformDrag: a plain Python object standing in
  front of one C++ QPlatformDrag.

  What exists
  -----------

  Every function of Qt's QPlatformDrag that has a ritual and that Python can
  call so far, 7 names in all: 'currentDrag', 'drag', 'cancelDrag',
  'updateAction', 'defaultAction', 'defaultPixmap', 'ownsDragObject'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformDragPrivate *QPlatformDrag::d_func()': gives
    'QPlatformDragPrivate', which has no cute class yet.
  - Qt's 'const QPlatformDragPrivate *QPlatformDrag::d_func() const': gives
    'QPlatformDragPrivate', which has no cute class yet.
  - Qt's 'QPlatformDrag::~QPlatformDrag()': the destructor: Python never
    removes a C++ QPlatformDrag.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPlatformDrag is created at the first use, not by
    'QPlatformDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformDrag.
  - Each name of Qt's QPlatformDrag that has no cute function yet, 'd_func',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultPixmap() -> QPixmap:
    """
    Calls Qt's 'QPixmap QPlatformDrag::defaultPixmap()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#defaultPixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QPlatformDrag::defaultPixmap()
    address = Rituals.call('ritual_ZN13QPlatformDrag13defaultPixmapEv')
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformDrag'

  #  A C++ QPlatformDrag Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformDrag'

  #  The functions Qt calls itself that QPlatformDrag is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drag': (
          ('_ZN13QPlatformDrag4dragEP5QDrag',
           ('int', 'enum', 'QtCore:Qt.DropAction'),
           (
               ('address', 'address', 'QtGui:QDrag'),
           )),
      ),
      'cancelDrag': (
          ('_ZN13QPlatformDrag10cancelDragEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'defaultAction': (
          ('_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropActionEES0'
           '_INS1_16KeyboardModifierEE',
           ('int', 'enum', 'QtCore:Qt.DropAction'),
           (
               ('int', 'flags', 'QtCore:Qt.DropAction'),
               ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           )),
      ),
      'ownsDragObject': (
          ('_ZNK13QPlatformDrag14ownsDragObjectEv',
           ('bool', 'number', ''),
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

  def currentDrag(self) -> Optional[QDrag]:
    """
    Calls Qt's 'QDrag *QPlatformDrag::currentDrag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#currentDrag

    Returns
    -------

    Optional[QDrag]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDrag *QPlatformDrag::currentDrag() const
    address = self.uglySide.call('ritual_ZNK13QPlatformDrag11currentDragEv')
    from . import QDrag
    return QDrag._cuteAt(address)

  @overload(Qt.DropActions, Qt.KeyboardModifiers)
  def defaultAction(
      self,
      possibleActions: Qt.DropActions,
      modifiers: Qt.KeyboardModifiers,
  ) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QPlatformDrag::defaultAction(Qt::DropActions
    possibleActions, Qt::KeyboardModifiers modifiers) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#defaultAction

    Parameters
    ----------

    possibleActions : Qt.DropActions
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QPlatformDrag::defaultAction(Qt::DropActions
    #      possibleActions, Qt::KeyboardModifiers modifiers) const
    ritual = (
        'ritual_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropActionE'
        'ES0_INS1_16KeyboardModifierEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropA'
          'ctionEES0_INS1_16KeyboardModifierEE')
    return Qt.DropAction(self.uglySide.call(
        ritual, possibleActions.value, modifiers.value,
    ))

  def ownsDragObject(self) -> bool:
    """
    Calls Qt's 'bool QPlatformDrag::ownsDragObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#ownsDragObject
    """
    #  bool QPlatformDrag::ownsDragObject() const
    ritual = 'ritual_ZNK13QPlatformDrag14ownsDragObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlatformDrag14ownsDragObjectEv'
    return self.uglySide.call(ritual)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPlatformDrag::QPlatformDrag()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#QPlatformDrag
    """
    #  QPlatformDrag::QPlatformDrag()
    self._noteCreation(QPlatformDrag, lambda: Rituals.call(
        'ritual_ZN13QPlatformDragC1Ev',
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

  @overload(QDrag)
  @overload(NoneType)
  def drag(self, m_drag: Optional[QDrag]) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QPlatformDrag::drag(QDrag *m_drag)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#drag

    Parameters
    ----------

    m_drag : Optional[QDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QPlatformDrag::drag(QDrag *m_drag)
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZN13QPlatformDrag4dragEP5QDrag', self._addressOf(m_drag),
    ))

  def cancelDrag(self) -> None:
    """
    Calls Qt's 'void QPlatformDrag::cancelDrag()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#cancelDrag
    """
    #  void QPlatformDrag::cancelDrag()
    ritual = 'ritual_ZN13QPlatformDrag10cancelDragEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPlatformDrag10cancelDragEv'
    self.uglySide.call(ritual)

  @overload(Qt.DropAction)
  def updateAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QPlatformDrag::updateAction(Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdrag.html#updateAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QPlatformDrag::updateAction(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN13QPlatformDrag12updateActionEN2Qt10DropActionE',
        action.value,
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QPlatformDragPrivate *QPlatformDrag::d_func()': gives
      'QPlatformDragPrivate', which has no cute class yet.
    - Qt's 'const QPlatformDragPrivate *QPlatformDrag::d_func() const': gives
      'QPlatformDragPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformDrag.d_func' has no cute function yet. Qt's "
        "'QPlatformDragPrivate *QPlatformDrag::d_func()': gives "
        "'QPlatformDragPrivate', which has no cute class yet. Qt's 'const "
        "QPlatformDragPrivate *QPlatformDrag::d_func() const': gives "
        "'QPlatformDragPrivate', which has no cute class yet.")
