"""
QEventDispatcherGlibPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventdispatcher_glib_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QEventDispatcherGlibPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QAbstractEventDispatcherPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QEventDispatcherGlibPrivate(QAbstractEventDispatcherPrivate):
  """
  The cute side of Qt's QEventDispatcherGlibPrivate: a plain Python object
  standing in front of one C++ QEventDispatcherGlibPrivate.

  It is built on the cute 'QAbstractEventDispatcherPrivate', as Qt's
  QEventDispatcherGlibPrivate is built on Qt's
  QAbstractEventDispatcherPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEventDispatcherGlibPrivate that has a ritual and
  that Python can call so far, 1 name in all:
  'runTimersOnceWithNormalPriority'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QEventDispatcherGlibPrivate::QEventDispatcherGlibPrivate(GMainContext
    *context)': names 'GMainContext', which has no cute class yet.
  - Qt's 'QEventDispatcherGlibPrivate::~QEventDispatcherGlibPrivate()': the
    destructor: Python never removes a C++ QEventDispatcherGlibPrivate.

  What to expect
  --------------

  - The C++ QEventDispatcherGlibPrivate is created at the first use, not by
    'QEventDispatcherGlibPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventDispatcherGlibPrivate.
  - Each name of Qt's QEventDispatcherGlibPrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventDispatcherGlibPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QEventDispatcherGlibPrivate::QEventDispatcherGlibPrivate(GMainContext
    *context)': names 'GMainContext', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QEventDispatcherGlibPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QEventDispatcherGlibPrivate::QEventDispatcherGlibPrivate(GMainCont"
        "ext *context)': names 'GMainContext', which has no cute class yet.")

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

  def runTimersOnceWithNormalPriority(self) -> None:
    """
    Calls Qt's 'void
    QEventDispatcherGlibPrivate::runTimersOnceWithNormalPriority()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventdispatcherglibprivate.html
    """
    #  void QEventDispatcherGlibPrivate::runTimersOnceWithNormalPriority()
    self.uglySide.call(
        'ritual_ZN27QEventDispatcherGlibPrivate31runTimersOnceWithNormalPri'
        'orityEv',
    )
