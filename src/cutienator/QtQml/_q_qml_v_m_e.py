"""
QQmlVME binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvme_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlVME to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QQmlVME(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlVME: a plain Python object standing in front of
  one C++ QQmlVME.

  C++ hands a QQmlVME around as a copy, so every C++ QQmlVME behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlVME that has a ritual and that Python can call
  so far, 3 names in all: 'enableComponentComplete',
  'disableComponentComplete', 'componentCompleteEnabled'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlVME::~QQmlVME()': the destructor: Python removes its C++
    QQmlVME by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlVME is created at the first use, not by 'QQmlVME(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlVME back gives a copy the ritual made for Python,
    in a new cute QQmlVME.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def enableComponentComplete() -> None:
    """
    Calls Qt's 'void QQmlVME::enableComponentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvme.html#enableComponentComplete
    """
    #  void QQmlVME::enableComponentComplete()
    Rituals.call('ritual_ZN7QQmlVME23enableComponentCompleteEv')

  @staticmethod
  def disableComponentComplete() -> None:
    """
    Calls Qt's 'void QQmlVME::disableComponentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvme.html#disableComponentComplete
    """
    #  void QQmlVME::disableComponentComplete()
    Rituals.call('ritual_ZN7QQmlVME24disableComponentCompleteEv')

  @staticmethod
  def componentCompleteEnabled() -> bool:
    """
    Calls Qt's 'bool QQmlVME::componentCompleteEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvme.html#componentCompleteEnabled
    """
    #  bool QQmlVME::componentCompleteEnabled()
    return Rituals.call('ritual_ZN7QQmlVME24componentCompleteEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlVME'

  #  Qt's '~QQmlVME()'. Naming it makes this a value class: Python owns every
  #  C++ QQmlVME behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QQmlVMED1Ev'

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
