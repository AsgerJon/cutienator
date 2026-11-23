"""
QUnhandledException binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QUnhandledException(QException):
  """
  The cute side of Qt's QUnhandledException: a plain Python object standing
  in front of one C++ QUnhandledException.

  It is built on the cute 'QException', as Qt's QUnhandledException is built
  on Qt's QException, and has everything that class has.

  C++ hands a QUnhandledException around as a copy, so every C++
  QUnhandledException behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUnhandledException that has a ritual and that
  Python can call so far, 2 names in all: 'raise_', 'clone'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUnhandledException::~QUnhandledException()': the destructor:
    Python removes its C++ QUnhandledException by it, and has no other use
    for it.

  What has no ritual
  ------------------

  6 of the 10 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QUnhandledException is created at the first use, not by
    'QUnhandledException(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUnhandledException back gives a copy the ritual made
    for Python, in a new cute QUnhandledException.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUnhandledException'

  #  Qt's '~QUnhandledException()'. Naming it makes this a value class:
  #  Python owns every C++ QUnhandledException behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QUnhandledExceptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QUnhandledException]:
    """
    Calls Qt's 'QUnhandledException *QUnhandledException::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qunhandledexception.html#clone

    Returns
    -------

    Optional[QUnhandledException]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUnhandledException *QUnhandledException::clone() const
    address = self.uglySide.call('ritual_ZNK19QUnhandledException5cloneEv')
    return QUnhandledException._cuteAt(address)

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

  @overload(THIS)
  def __init__(self, other: QUnhandledException) -> None:
    """
    Notes what was given, for Qt's
    'QUnhandledException::QUnhandledException(const QUnhandledException
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qunhandledexception.html#QUnhandledException

    Parameters
    ----------

    other : QUnhandledException
      Passed on as a value: Qt reads the C++ QUnhandledException, which stays
      Python's own.
    """
    #  QUnhandledException::QUnhandledException(const QUnhandledException
    #      &other)
    self._noteCreation(QUnhandledException, lambda: Rituals.call(
        'ritual_ZN19QUnhandledExceptionC1ERKS_', self._valueOf(other),
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

  def raise_(self) -> None:
    """
    Calls Qt's 'void QUnhandledException::raise() const'.

    Qt's own words: https://doc.qt.io/qt-6/qunhandledexception.html#raise
    """
    #  void QUnhandledException::raise() const
    self.uglySide.call('ritual_ZNK19QUnhandledException5raiseEv')
