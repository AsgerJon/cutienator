"""
QQuickPopupTransitionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupTransitionManager to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQuick import QQuickTransitionManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickPopupPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPopupPrivate = WAIT['QQuickPopupPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupTransitionManager(QQuickTransitionManager):
  """
  The cute side of Qt's QQuickPopupTransitionManager: a plain Python object
  standing in front of one C++ QQuickPopupTransitionManager.

  It is built on the cute 'QQuickTransitionManager', as Qt's
  QQuickPopupTransitionManager is built on Qt's QQuickTransitionManager, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPopupTransitionManager that has a ritual and
  that Python can call so far, 3 names in all: 'transitionEnter',
  'transitionExit', 'finished'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QQuickPopupTransitionManager is created at the first use, not by
    'QQuickPopupTransitionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopupTransitionManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupTransitionManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QQuickPopupPrivate)
  @overload(NoneType)
  def __init__(self, popup: Optional[QQuickPopupPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPopupTransitionManager::QQuickPopupTransitionManager(
    QQuickPopupPrivate *popup)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuptransitionmanager.html

    Parameters
    ----------

    popup : Optional[QQuickPopupPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPopupTransitionManager::QQuickPopupTransitionManager(
    #      QQuickPopupPrivate *popup)
    self._noteCreation(QQuickPopupTransitionManager, lambda: Rituals.call(
        'ritual_ZN28QQuickPopupTransitionManagerC1EP18QQuickPopupPrivate',
        self._addressOf(popup),
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

  def transitionEnter(self) -> None:
    """
    Calls Qt's 'void QQuickPopupTransitionManager::transitionEnter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuptransitionmanager.html#transitionEnter
    """
    #  void QQuickPopupTransitionManager::transitionEnter()
    self.uglySide.call(
        'ritual_ZN28QQuickPopupTransitionManager15transitionEnterEv',
    )

  def transitionExit(self) -> None:
    """
    Calls Qt's 'void QQuickPopupTransitionManager::transitionExit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuptransitionmanager.html#transitionExit
    """
    #  void QQuickPopupTransitionManager::transitionExit()
    self.uglySide.call(
        'ritual_ZN28QQuickPopupTransitionManager14transitionExitEv',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickPopupTransitionManager::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopuptransitionmanager.html#finished
    """
    #  void QQuickPopupTransitionManager::finished()
    ritual = 'ritual_ZN28QQuickPopupTransitionManager8finishedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QQuickPopupTransitionManager8finishedEv'
    self.uglySide.call(ritual)
