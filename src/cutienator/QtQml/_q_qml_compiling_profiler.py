"""
QQmlCompilingProfiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlCompilingProfiler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlProfilerHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlDataBlob, QQmlProfiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDataBlob = WAIT['QQmlDataBlob']
  QQmlProfiler = WAIT['QQmlProfiler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlCompilingProfiler(QQmlProfilerHelper):
  """
  The cute side of Qt's QQmlCompilingProfiler: a plain Python object standing
  in front of one C++ QQmlCompilingProfiler.

  It is built on the cute 'QQmlProfilerHelper', as Qt's QQmlCompilingProfiler
  is built on Qt's QQmlProfilerHelper, and has everything that class has.

  C++ hands a QQmlCompilingProfiler around as a copy, so every C++
  QQmlCompilingProfiler behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlCompilingProfiler yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlCompilingProfiler::~QQmlCompilingProfiler()': the destructor:
    Python removes its C++ QQmlCompilingProfiler by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlCompilingProfiler is created at the first use, not by
    'QQmlCompilingProfiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlCompilingProfiler back gives a copy the ritual
    made for Python, in a new cute QQmlCompilingProfiler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCompilingProfiler'

  #  Qt's '~QQmlCompilingProfiler()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlCompilingProfiler behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQmlCompilingProfilerD1Ev'

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

  @overload(QQmlProfiler, QQmlDataBlob)
  @overload(QQmlProfiler, NoneType)
  @overload(NoneType, QQmlDataBlob)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      profiler: Optional[QQmlProfiler],
      blob: Optional[QQmlDataBlob],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlCompilingProfiler::QQmlCompilingProfiler(QQmlProfiler *profiler,
    QQmlDataBlob *blob)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompilingprofiler.html#QQmlCompilingProfiler

    Parameters
    ----------

    profiler : Optional[QQmlProfiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    blob : Optional[QQmlDataBlob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlCompilingProfiler::QQmlCompilingProfiler(QQmlProfiler *profiler,
    #      QQmlDataBlob *blob)
    self._noteCreation(QQmlCompilingProfiler, lambda: Rituals.call(
        'ritual_ZN21QQmlCompilingProfilerC1EP12QQmlProfilerP12QQmlDataBlob',
        self._addressOf(profiler), self._addressOf(blob),
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
