"""
QAbstractButtonPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractbutton_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractButtonPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QList
from . import QSizePolicy, QStyle, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractButton


class QAbstractButtonPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QAbstractButtonPrivate: a plain Python object
  standing in front of one C++ QAbstractButtonPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QAbstractButtonPrivate is
  built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractButtonPrivate that has a ritual and that
  Python can call so far, 13 names in all: 'q_func', 'init', 'click',
  'refresh', 'queryButtonList', 'queryCheckedButton', 'notifyChecked',
  'fixFocusPolicy', 'emitPressed', 'emitReleased', 'emitClicked',
  'emitToggled', 'styleButtonState'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractButton *QAbstractButtonPrivate::q_func() const':
    takes in Python what 'QAbstractButton *QAbstractButtonPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QAbstractButtonPrivate is created at the first use, not by
    'QAbstractButtonPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractButtonPrivate.
  - Each name of Qt's QAbstractButtonPrivate that has no cute function yet,
    'moveFocus', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QAbstractButtonPrivate'

  #  A C++ QAbstractButtonPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractButtonPrivate'

  #  The functions Qt calls itself that QAbstractButtonPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'styleButtonState': (
          ('_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QStyle'
           '9StateFlagEE',
           ('int', 'flags', 'QtWidgets:QStyle.StateFlag'),
           (
               ('int', 'flags', 'QtWidgets:QStyle.StateFlag'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def queryButtonList(self) -> QList[QAbstractButton]:
    """
    Calls Qt's 'QList<QAbstractButton *>
    QAbstractButtonPrivate::queryButtonList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#queryButtonList

    Returns
    -------

    QList[QAbstractButton]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractButton *> QAbstractButtonPrivate::queryButtonList()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstractButtonPrivate15queryButtonListEv',
    )
    from . import QAbstractButton
    return QList[QAbstractButton]._cuteOwning(address)

  def queryCheckedButton(self) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QAbstractButtonPrivate::queryCheckedButton()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#queryCheckedButton

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QAbstractButtonPrivate::queryCheckedButton() const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstractButtonPrivate18queryCheckedButtonEv',
    )
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  @overload(QStyle.State)
  def styleButtonState(self, state: QStyle.State) -> QStyle.State:
    """
    Calls Qt's 'QStyle::State
    QAbstractButtonPrivate::styleButtonState(QStyle::State state) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#styleButtonState

    Parameters
    ----------

    state : QStyle.State
      Passed on as its number.

    Returns
    -------

    QStyle.State
      The value standing for the combination Qt gave back.
    """
    #  QStyle::State QAbstractButtonPrivate::styleButtonState(QStyle::State
    #      state) const
    ritual = (
        'ritual_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlagsIN6QSt'
        'yle9StateFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAbstractButtonPrivate16styleButtonStateE6QFlags'
          'IN6QStyle9StateFlagEE')
    return QStyle.State(self.uglySide.call(ritual, state.value))

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
  @overload(QSizePolicy.ControlType)
  def __init__(
      self,
      type: QSizePolicy.ControlType = QSizePolicy.ControlType.DefaultType,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractButtonPrivate::QAbstractButtonPrivate(QSizePolicy::ControlType
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#QAbstractButtonPrivate

    Parameters
    ----------

    type : QSizePolicy.ControlType
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicy.ControlType.DefaultType.
    """
    #  QAbstractButtonPrivate::QAbstractButtonPrivate(QSizePolicy::
    #      ControlType type)
    self._noteCreation(QAbstractButtonPrivate, lambda: Rituals.call(
        'ritual_ZN22QAbstractButtonPrivateC1EN11QSizePolicy11ControlTypeE',
        type.value,
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

  def q_func(self) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QAbstractButtonPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbuttonprivate.html#q_func

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QAbstractButtonPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QAbstractButtonPrivate6q_funcEv',
    )
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbuttonprivate.html#init
    """
    #  void QAbstractButtonPrivate::init()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate4initEv')

  def click(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::click()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbuttonprivate.html#click
    """
    #  void QAbstractButtonPrivate::click()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate5clickEv')

  def refresh(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::refresh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#refresh
    """
    #  void QAbstractButtonPrivate::refresh()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate7refreshEv')

  def notifyChecked(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::notifyChecked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#notifyChecked
    """
    #  void QAbstractButtonPrivate::notifyChecked()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate13notifyCheckedEv')

  def fixFocusPolicy(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::fixFocusPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#fixFocusPolicy
    """
    #  void QAbstractButtonPrivate::fixFocusPolicy()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate14fixFocusPolicyEv')

  def emitPressed(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::emitPressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#emitPressed
    """
    #  void QAbstractButtonPrivate::emitPressed()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate11emitPressedEv')

  def emitReleased(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::emitReleased()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#emitReleased
    """
    #  void QAbstractButtonPrivate::emitReleased()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate12emitReleasedEv')

  def emitClicked(self) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::emitClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#emitClicked
    """
    #  void QAbstractButtonPrivate::emitClicked()
    self.uglySide.call('ritual_ZN22QAbstractButtonPrivate11emitClickedEv')

  @overload(bool)
  def emitToggled(self, checked: bool) -> None:
    """
    Calls Qt's 'void QAbstractButtonPrivate::emitToggled(bool checked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbuttonprivate.html#emitToggled

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QAbstractButtonPrivate::emitToggled(bool checked)
    self.uglySide.call(
        'ritual_ZN22QAbstractButtonPrivate11emitToggledEb', checked,
    )

  @staticmethod
  def moveFocus(*__, **_) -> Never:
    """
    Qt's 'void QAbstractButtonPrivate::moveFocus(int key)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'qt_tab_all_widgets'.
    """
    raise NotImplementedError(
        "'QAbstractButtonPrivate.moveFocus' has no cute function yet. Qt's "
        "'void QAbstractButtonPrivate::moveFocus(int key)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qt_tab_all_widgets'.")
