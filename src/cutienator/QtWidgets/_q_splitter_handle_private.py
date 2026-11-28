"""
QSplitterHandlePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSplitterHandlePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from . import QSplitterHandle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QSplitterHandlePrivate(QWidgetPrivate):
  """
  The cute side of Qt's QSplitterHandlePrivate: a plain Python object
  standing in front of one C++ QSplitterHandlePrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QSplitterHandlePrivate is
  built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplitterHandlePrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'pick'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSplitterHandle *QSplitterHandlePrivate::q_func() const':
    takes in Python what 'QSplitterHandle *QSplitterHandlePrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QSplitterHandlePrivate is created at the first use, not by
    'QSplitterHandlePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplitterHandlePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplitterHandlePrivate'

  #  A C++ QSplitterHandlePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSplitterHandlePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def pick(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QSplitterHandlePrivate::pick(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandleprivate.html#pick

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QSplitterHandlePrivate::pick(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK22QSplitterHandlePrivate4pickERK6QPoint',
        self._valueOf(pos),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSplitterHandlePrivate::QSplitterHandlePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandleprivate.html#QSplitterHandlePrivate
    """
    #  QSplitterHandlePrivate::QSplitterHandlePrivate()
    self._noteCreation(QSplitterHandlePrivate, lambda: Rituals.call(
        'ritual_ZN22QSplitterHandlePrivateC1Ev',
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

  def q_func(self) -> Optional[QSplitterHandle]:
    """
    Calls Qt's 'QSplitterHandle *QSplitterHandlePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandleprivate.html#q_func

    Returns
    -------

    Optional[QSplitterHandle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitterHandle *QSplitterHandlePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QSplitterHandlePrivate6q_funcEv',
    )
    from . import QSplitterHandle
    return QSplitterHandle._cuteAt(address)
