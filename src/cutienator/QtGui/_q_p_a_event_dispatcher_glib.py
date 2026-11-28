"""
QPAEventDispatcherGlib binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qeventdispatcher_glib_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPAEventDispatcherGlib to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QEventDispatcherGlib, QEventLoop, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPAEventDispatcherGlibPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPAEventDispatcherGlib(QEventDispatcherGlib):
  """
  The cute side of Qt's QPAEventDispatcherGlib: a plain Python object
  standing in front of one C++ QPAEventDispatcherGlib.

  It is built on the cute 'QEventDispatcherGlib', as Qt's
  QPAEventDispatcherGlib is built on Qt's QEventDispatcherGlib, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPAEventDispatcherGlib that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'd_func',
  'processEvents'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPAEventDispatcherGlib::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPAEventDispatcherGlib::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QPAEventDispatcherGlibPrivate
    *QPAEventDispatcherGlib::d_func() const': takes in Python what
    'QPAEventDispatcherGlibPrivate *QPAEventDispatcherGlib::d_func()' takes.
  - Qt's 'QPAEventDispatcherGlib::~QPAEventDispatcherGlib()': the destructor:
    Python never removes a C++ QPAEventDispatcherGlib.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPAEventDispatcherGlib is created at the first use, not by
    'QPAEventDispatcherGlib(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPAEventDispatcherGlib.
  - Qt tells when it has removed the C++ QPAEventDispatcherGlib. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPAEventDispatcherGlib::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaeventdispatcherglib.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPAEventDispatcherGlib::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QPAEventDispatcherGlib2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPAEventDispatcherGlib'

  #  A C++ QPAEventDispatcherGlib Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPAEventDispatcherGlib'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPAEventDispatcherGlib::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaeventdispatcherglib.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPAEventDispatcherGlib::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QPAEventDispatcherGlib10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPAEventDispatcherGlib::QPAEventDispatcherGlib(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaeventdispatcherglib.html#QPAEventDispatcherGlib

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPAEventDispatcherGlib::QPAEventDispatcherGlib(QObject *parent)
    self._noteCreation(QPAEventDispatcherGlib, lambda: Rituals.call(
        'ritual_ZN22QPAEventDispatcherGlibC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QPAEventDispatcherGlibPrivate]:
    """
    Calls Qt's 'QPAEventDispatcherGlibPrivate
    *QPAEventDispatcherGlib::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaeventdispatcherglib.html#d_func

    Returns
    -------

    Optional[QPAEventDispatcherGlibPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPAEventDispatcherGlibPrivate *QPAEventDispatcherGlib::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QPAEventDispatcherGlib6d_funcEv',
    )
    from . import QPAEventDispatcherGlibPrivate
    return QPAEventDispatcherGlibPrivate._cuteAt(address)

  @overload(QEventLoop.ProcessEventsFlags)
  def processEvents(self, flags: QEventLoop.ProcessEventsFlags) -> bool:
    """
    Calls Qt's 'bool
    QPAEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaeventdispatcherglib.html#processEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.
    """
    #  bool QPAEventDispatcherGlib::processEvents(QEventLoop::
    #      ProcessEventsFlags flags)
    ritual = (
        'ritual_ZN22QPAEventDispatcherGlib13processEventsE6QFlagsIN10QEvent'
        'Loop17ProcessEventsFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QPAEventDispatcherGlib13processEventsE6QFlagsIN10'
          'QEventLoop17ProcessEventsFlagEE')
    return self.uglySide.call(ritual, flags.value)
