"""
QQmlObjectCreatorRecursionWatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlObjectCreatorRecursionWatcher to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlObjectCreator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlObjectCreator = WAIT['QQmlObjectCreator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlObjectCreatorRecursionWatcher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlObjectCreatorRecursionWatcher: a plain Python
  object standing in front of one C++ QQmlObjectCreatorRecursionWatcher.

  C++ hands a QQmlObjectCreatorRecursionWatcher around as a copy, so every
  C++ QQmlObjectCreatorRecursionWatcher behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQmlObjectCreatorRecursionWatcher that has a ritual
  and that Python can call so far, 1 name in all: 'hasRecursed'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQmlObjectCreatorRecursionWatcher::~QQmlObjectCreatorRecursionWatcher(
    )': the destructor: Python removes its C++
    QQmlObjectCreatorRecursionWatcher by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlObjectCreatorRecursionWatcher is created at the first use,
    not by 'QQmlObjectCreatorRecursionWatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlObjectCreatorRecursionWatcher back gives a copy
    the ritual made for Python, in a new cute
    QQmlObjectCreatorRecursionWatcher.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlObjectCreatorRecursionWatcher'

  #  Qt's '~QQmlObjectCreatorRecursionWatcher()'. Naming it makes this a
  #  value class: Python owns every C++ QQmlObjectCreatorRecursionWatcher
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QQmlObjectCreatorRecursionWatcherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasRecursed(self) -> bool:
    """
    Calls Qt's 'bool QQmlObjectCreatorRecursionWatcher::hasRecursed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreatorrecursionwatcher.html#hasRecursed
    """
    #  bool QQmlObjectCreatorRecursionWatcher::hasRecursed() const
    return self.uglySide.call(
        'ritual_ZNK33QQmlObjectCreatorRecursionWatcher11hasRecursedEv',
    )

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

  @overload(QQmlObjectCreator)
  @overload(NoneType)
  def __init__(self, creator: Optional[QQmlObjectCreator]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlObjectCreatorRecursionWatcher::QQmlObjectCreatorRecursionWatcher(
    QQmlObjectCreator *creator)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreatorrecursionwatcher.html

    Parameters
    ----------

    creator : Optional[QQmlObjectCreator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlObjectCreatorRecursionWatcher::
    #      QQmlObjectCreatorRecursionWatcher(QQmlObjectCreator *creator)
    self._noteCreation(
        QQmlObjectCreatorRecursionWatcher, lambda: Rituals.call(
            'ritual_ZN33QQmlObjectCreatorRecursionWatcherC1EP17QQmlObjectCr'
            'eator',
            self._addressOf(creator),
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
