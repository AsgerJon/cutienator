"""
QAbstractFileEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractFileEnginePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractFileEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractFileEngine = WAIT['QAbstractFileEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractFileEnginePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractFileEnginePrivate: a plain Python object
  standing in front of one C++ QAbstractFileEnginePrivate.

  C++ hands a QAbstractFileEnginePrivate around as a copy, so every C++
  QAbstractFileEnginePrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QAbstractFileEnginePrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractFileEnginePrivate::~QAbstractFileEnginePrivate()': the
    destructor: Python removes its C++ QAbstractFileEnginePrivate by it, and
    has no other use for it.
  - Qt's 'const QAbstractFileEngine *QAbstractFileEnginePrivate::q_func()
    const': takes in Python what 'QAbstractFileEngine
    *QAbstractFileEnginePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QAbstractFileEnginePrivate is created at the first use, not by
    'QAbstractFileEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAbstractFileEnginePrivate back gives a copy the
    ritual made for Python, in a new cute QAbstractFileEnginePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFileEnginePrivate'

  #  Qt's '~QAbstractFileEnginePrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QAbstractFileEnginePrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QAbstractFileEnginePrivateD1Ev'

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

  @overload(QAbstractFileEngine)
  @overload(NoneType)
  def __init__(self, q: Optional[QAbstractFileEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractFileEnginePrivate::QAbstractFileEnginePrivate(
    QAbstractFileEngine *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineprivate.html

    Parameters
    ----------

    q : Optional[QAbstractFileEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractFileEnginePrivate::QAbstractFileEnginePrivate(
    #      QAbstractFileEngine *q)
    self._noteCreation(QAbstractFileEnginePrivate, lambda: Rituals.call(
        'ritual_ZN26QAbstractFileEnginePrivateC1EP19QAbstractFileEngine',
        self._addressOf(q),
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

  def q_func(self) -> Optional[QAbstractFileEngine]:
    """
    Calls Qt's 'QAbstractFileEngine *QAbstractFileEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineprivate.html#q_func

    Returns
    -------

    Optional[QAbstractFileEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileEngine *QAbstractFileEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QAbstractFileEnginePrivate6q_funcEv',
    )
    from . import QAbstractFileEngine
    return QAbstractFileEngine._cuteAt(address)
