"""
QPAEventDispatcherGlibPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qeventdispatcher_glib_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPAEventDispatcherGlibPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QEventDispatcherGlibPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPAEventDispatcherGlib


class QPAEventDispatcherGlibPrivate(QEventDispatcherGlibPrivate):
  """
  The cute side of Qt's QPAEventDispatcherGlibPrivate: a plain Python object
  standing in front of one C++ QPAEventDispatcherGlibPrivate.

  It is built on the cute 'QEventDispatcherGlibPrivate', as Qt's
  QPAEventDispatcherGlibPrivate is built on Qt's QEventDispatcherGlibPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPAEventDispatcherGlibPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPAEventDispatcherGlib
    *QPAEventDispatcherGlibPrivate::q_func() const': takes in Python what
    'QPAEventDispatcherGlib *QPAEventDispatcherGlibPrivate::q_func()' takes.
  - Qt's 'QPAEventDispatcherGlibPrivate::~QPAEventDispatcherGlibPrivate()':
    the destructor: Python never removes a C++ QPAEventDispatcherGlibPrivate.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPAEventDispatcherGlibPrivate is created at the first use, not by
    'QPAEventDispatcherGlibPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPAEventDispatcherGlibPrivate.
  - Each name of Qt's QPAEventDispatcherGlibPrivate that has no cute function
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
  __qt_class__ = 'QPAEventDispatcherGlibPrivate'

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
    Qt's 'QPAEventDispatcherGlibPrivate::QPAEventDispatcherGlibPrivate(
    GMainContext *context)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'GSource'; did you mean 'QOpenGLDebugMessage::Source'?.
    """
    raise NotImplementedError(
        "'QPAEventDispatcherGlibPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QPAEventDispatcherGlibPrivate::QPAEventDispatcherGlibPrivate(GMain"
        "Context *context)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: unknown type "
        "name 'GSource'; did you mean 'QOpenGLDebugMessage::Source'?.")

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

  def q_func(self) -> Optional[QPAEventDispatcherGlib]:
    """
    Calls Qt's 'QPAEventDispatcherGlib
    *QPAEventDispatcherGlibPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaeventdispatcherglibprivate.html#q_func

    Returns
    -------

    Optional[QPAEventDispatcherGlib]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPAEventDispatcherGlib *QPAEventDispatcherGlibPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QPAEventDispatcherGlibPrivate6q_funcEv',
    )
    from . import QPAEventDispatcherGlib
    return QPAEventDispatcherGlib._cuteAt(address)
