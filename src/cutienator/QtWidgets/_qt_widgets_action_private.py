"""
QtWidgetsActionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qaction_widgets_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtWidgetsActionPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QActionPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from ..QtGui import QAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtWidgetsActionPrivate(QActionPrivate):
  """
  The cute side of Qt's QtWidgetsActionPrivate: a plain Python object
  standing in front of one C++ QtWidgetsActionPrivate.

  It is built on the cute 'QActionPrivate', as Qt's QtWidgetsActionPrivate is
  built on Qt's QActionPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtWidgetsActionPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'destroy', 'menu',
  'setMenu'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAction *QtWidgetsActionPrivate::q_func() const': takes in
    Python what 'QAction *QtWidgetsActionPrivate::q_func()' takes.
  - Qt's 'QtWidgetsActionPrivate::~QtWidgetsActionPrivate()': the destructor:
    Python never removes a C++ QtWidgetsActionPrivate.
  - Qt's 'QShortcutMap::ContextMatcher
    QtWidgetsActionPrivate::contextMatcher() const': gives a type Python has
    no way to take yet.

  What to expect
  --------------

  - The C++ QtWidgetsActionPrivate is created at the first use, not by
    'QtWidgetsActionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWidgetsActionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWidgetsActionPrivate'

  #  A C++ QtWidgetsActionPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWidgetsActionPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def menu(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtWidgetsActionPrivate::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtwidgetsactionprivate.html#menu

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtWidgetsActionPrivate::menu() const
    ritual = 'ritual_ZNK22QtWidgetsActionPrivate4menuEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QtWidgetsActionPrivate4menuEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QtWidgetsActionPrivate::setMenu(QObject *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwidgetsactionprivate.html#setMenu

    Parameters
    ----------

    menu : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWidgetsActionPrivate::setMenu(QObject *menu)
    ritual = 'ritual_ZN22QtWidgetsActionPrivate7setMenuEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QtWidgetsActionPrivate7setMenuEP7QObject'
    self.uglySide.call(ritual, self._addressOf(menu, 'QObject'))

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
    'QtWidgetsActionPrivate::QtWidgetsActionPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwidgetsactionprivate.html#QtWidgetsActionPrivate
    """
    #  QtWidgetsActionPrivate::QtWidgetsActionPrivate()
    self._noteCreation(QtWidgetsActionPrivate, lambda: Rituals.call(
        'ritual_ZN22QtWidgetsActionPrivateC1Ev',
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

  def q_func(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QtWidgetsActionPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtwidgetsactionprivate.html#q_func

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QtWidgetsActionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QtWidgetsActionPrivate6q_funcEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QtWidgetsActionPrivate::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwidgetsactionprivate.html#destroy
    """
    #  void QtWidgetsActionPrivate::destroy()
    ritual = 'ritual_ZN22QtWidgetsActionPrivate7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QtWidgetsActionPrivate7destroyEv'
    self.uglySide.call(ritual)
