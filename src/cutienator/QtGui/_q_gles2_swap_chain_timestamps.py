"""
QGles2SwapChainTimestamps binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2SwapChainTimestamps to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiGles2
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiGles2 = WAIT['QRhiGles2']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGles2SwapChainTimestamps(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGles2SwapChainTimestamps: a plain Python object
  standing in front of one C++ QGles2SwapChainTimestamps.

  C++ hands a QGles2SwapChainTimestamps around as a copy, so every C++
  QGles2SwapChainTimestamps behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGles2SwapChainTimestamps that has a ritual and that
  Python can call so far, 2 names in all: 'prepare', 'destroy'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QGles2SwapChainTimestamps::tryQueryTimestamps(int pairIndex,
    QRhiGles2 *rhiD, double *elapsedSec)': takes a number to change where it
    is.
  - Qt's 'QGles2SwapChainTimestamps::~QGles2SwapChainTimestamps()': the
    destructor: Python removes its C++ QGles2SwapChainTimestamps by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QGles2SwapChainTimestamps is created at the first use, not by
    'QGles2SwapChainTimestamps(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGles2SwapChainTimestamps back gives a copy the
    ritual made for Python, in a new cute QGles2SwapChainTimestamps.
  - Each name of Qt's QGles2SwapChainTimestamps that has no cute function
    yet, 'tryQueryTimestamps', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2SwapChainTimestamps'

  #  Qt's '~QGles2SwapChainTimestamps()'. Naming it makes this a value class:
  #  Python owns every C++ QGles2SwapChainTimestamps behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QGles2SwapChainTimestampsD1Ev'

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

  @overload(QRhiGles2)
  @overload(NoneType)
  def prepare(self, rhiD: Optional[QRhiGles2]) -> None:
    """
    Calls Qt's 'void QGles2SwapChainTimestamps::prepare(QRhiGles2 *rhiD)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchaintimestamps.html#prepare

    Parameters
    ----------

    rhiD : Optional[QRhiGles2]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGles2SwapChainTimestamps::prepare(QRhiGles2 *rhiD)
    self.uglySide.call(
        'ritual_ZN25QGles2SwapChainTimestamps7prepareEP9QRhiGles2',
        self._addressOf(rhiD),
    )

  @overload(QRhiGles2)
  @overload(NoneType)
  def destroy(self, rhiD: Optional[QRhiGles2]) -> None:
    """
    Calls Qt's 'void QGles2SwapChainTimestamps::destroy(QRhiGles2 *rhiD)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2swapchaintimestamps.html#destroy

    Parameters
    ----------

    rhiD : Optional[QRhiGles2]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGles2SwapChainTimestamps::destroy(QRhiGles2 *rhiD)
    self.uglySide.call(
        'ritual_ZN25QGles2SwapChainTimestamps7destroyEP9QRhiGles2',
        self._addressOf(rhiD),
    )

  @staticmethod
  def tryQueryTimestamps(*__, **_) -> Never:
    """
    Qt's 'bool QGles2SwapChainTimestamps::tryQueryTimestamps(int pairIndex,
    QRhiGles2 *rhiD, double *elapsedSec)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QGles2SwapChainTimestamps.tryQueryTimestamps' has no cute "
        "function yet. Qt's 'bool "
        "QGles2SwapChainTimestamps::tryQueryTimestamps(int pairIndex, "
        "QRhiGles2 *rhiD, double *elapsedSec)': takes a number to change "
        "where it is.")
