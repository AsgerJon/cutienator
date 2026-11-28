"""
QCtfTracePointEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qctf_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QCtfTracePointEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QCtfTracePointProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCtfTracePointProvider = WAIT['QCtfTracePointProvider']


class QCtfTracePointEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCtfTracePointEvent: a plain Python object standing
  in front of one C++ QCtfTracePointEvent.

  C++ hands a QCtfTracePointEvent around as a copy, so every C++
  QCtfTracePointEvent behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QCtfTracePointEvent yet. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCtfTracePointEvent::~QCtfTracePointEvent()': the destructor:
    Python removes its C++ QCtfTracePointEvent by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCtfTracePointEvent is created at the first use, not by
    'QCtfTracePointEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCtfTracePointEvent back gives a copy the ritual made
    for Python, in a new cute QCtfTracePointEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCtfTracePointEvent'

  #  Qt's '~QCtfTracePointEvent()'. Naming it makes this a value class:
  #  Python owns every C++ QCtfTracePointEvent behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCtfTracePointEventD1Ev'

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

  @overload(QCtfTracePointProvider, str, str, int, bool)
  def __init__(
      self,
      provider: QCtfTracePointProvider,
      name: str,
      metadata: str,
      size: int,
      variableSize: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCtfTracePointEvent::QCtfTracePointEvent(const QCtfTracePointProvider
    &provider, const QString &name, const QString &metadata, int size, bool
    variableSize)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qctftracepointevent.html#QCtfTracePointEvent

    Parameters
    ----------

    provider : QCtfTracePointProvider
      Passed on as a value: Qt reads the C++ QCtfTracePointProvider, which
      stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    metadata : str
      Passed on as it is: a QString is made of it for the call.

    size : int
      Passed on as it is.

    variableSize : bool
      Passed on as it is.
    """
    #  QCtfTracePointEvent::QCtfTracePointEvent(const QCtfTracePointProvider
    #      &provider, const QString &name, const QString &metadata, int size,
    #      bool variableSize)
    self._noteCreation(QCtfTracePointEvent, lambda: Rituals.call(
        'ritual_ZN19QCtfTracePointEventC1ERK22QCtfTracePointProviderRK7QStr'
        'ingS5_ib',
        self._valueOf(provider), name, metadata, size, variableSize,
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
