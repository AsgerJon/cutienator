"""
QPushButtonPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpushbutton_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPushButtonPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QAbstractButtonPrivate, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from . import QDialog, QPushButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPushButton = WAIT['QPushButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPushButtonPrivate(QAbstractButtonPrivate):
  """
  The cute side of Qt's QPushButtonPrivate: a plain Python object standing in
  front of one C++ QPushButtonPrivate.

  It is built on the cute 'QAbstractButtonPrivate', as Qt's
  QPushButtonPrivate is built on Qt's QAbstractButtonPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPushButtonPrivate that has a ritual and that Python
  can call so far, 8 names in all: 'q_func', 'init', 'get',
  'adjustedMenuPosition', 'resetLayoutItemMargins', 'popupPressed',
  'styleButtonState', 'dialogParent'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPushButton *QPushButtonPrivate::q_func() const': takes in
    Python what 'QPushButton *QPushButtonPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QPushButtonPrivate is created at the first use, not by
    'QPushButtonPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPushButtonPrivate.
  """

  #  The enums Qt writes inside QPushButtonPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AutoDefaultValue(CuteNum):
    """
    The enum 'QPushButtonPrivate::AutoDefaultValue' of Qt, with the 3 names
    Qt gives in it.
    """

    Off = Kee[int](0)
    On = Kee[int](1)
    Auto = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPushButton)
  @overload(NoneType)
  def get(b: Optional[QPushButton]) -> Optional[QPushButtonPrivate]:
    """
    Calls Qt's 'QPushButtonPrivate *QPushButtonPrivate::get(QPushButton *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbuttonprivate.html#get

    Parameters
    ----------

    b : Optional[QPushButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPushButtonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButtonPrivate *QPushButtonPrivate::get(QPushButton *b)
    address = Rituals.call(
        'ritual_ZN18QPushButtonPrivate3getEP11QPushButton',
        CuteMixin._addressOf(b),
    )
    return QPushButtonPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPushButtonPrivate'

  #  A C++ QPushButtonPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPushButtonPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStyle.State)
  def styleButtonState(self, state: QStyle.State) -> QStyle.State:
    """
    Calls Qt's 'QStyle::State
    QPushButtonPrivate::styleButtonState(QStyle::State state) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpushbuttonprivate.html#styleButtonState

    Parameters
    ----------

    state : QStyle.State
      Passed on as its number.

    Returns
    -------

    QStyle.State
      The value standing for the combination Qt gave back.
    """
    #  QStyle::State QPushButtonPrivate::styleButtonState(QStyle::State
    #      state) const
    ritual = (
        'ritual_ZNK18QPushButtonPrivate16styleButtonStateE6QFlagsIN6QStyle9'
        'StateFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QPushButtonPrivate16styleButtonStateE6QFlagsIN6Q'
          'Style9StateFlagEE')
    return QStyle.State(self.uglySide.call(ritual, state.value))

  def dialogParent(self) -> Optional[QDialog]:
    """
    Calls Qt's 'QDialog *QPushButtonPrivate::dialogParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpushbuttonprivate.html#dialogParent

    Returns
    -------

    Optional[QDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialog *QPushButtonPrivate::dialogParent() const
    address = self.uglySide.call(
        'ritual_ZNK18QPushButtonPrivate12dialogParentEv',
    )
    from . import QDialog
    return QDialog._cuteAt(address)

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
    Notes what was given, for Qt's
    'QPushButtonPrivate::QPushButtonPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpushbuttonprivate.html#QPushButtonPrivate
    """
    #  QPushButtonPrivate::QPushButtonPrivate()
    self._noteCreation(QPushButtonPrivate, lambda: Rituals.call(
        'ritual_ZN18QPushButtonPrivateC1Ev',
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

  def q_func(self) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QPushButtonPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbuttonprivate.html#q_func

    Returns
    -------

    Optional[QPushButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButton *QPushButtonPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QPushButtonPrivate6q_funcEv')
    from . import QPushButton
    return QPushButton._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QPushButtonPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qpushbuttonprivate.html#init
    """
    #  void QPushButtonPrivate::init()
    self.uglySide.call('ritual_ZN18QPushButtonPrivate4initEv')

  def adjustedMenuPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPushButtonPrivate::adjustedMenuPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpushbuttonprivate.html#adjustedMenuPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPushButtonPrivate::adjustedMenuPosition()
    address = self.uglySide.call(
        'ritual_ZN18QPushButtonPrivate20adjustedMenuPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def resetLayoutItemMargins(self) -> None:
    """
    Calls Qt's 'void QPushButtonPrivate::resetLayoutItemMargins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpushbuttonprivate.html#resetLayoutItemMargins
    """
    #  void QPushButtonPrivate::resetLayoutItemMargins()
    self.uglySide.call(
        'ritual_ZN18QPushButtonPrivate22resetLayoutItemMarginsEv',
    )

  def popupPressed(self) -> None:
    """
    Calls Qt's 'void QPushButtonPrivate::popupPressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpushbuttonprivate.html#popupPressed
    """
    #  void QPushButtonPrivate::popupPressed()
    self.uglySide.call('ritual_ZN18QPushButtonPrivate12popupPressedEv')
