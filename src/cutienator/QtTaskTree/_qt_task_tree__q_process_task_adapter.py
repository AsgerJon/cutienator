"""
QtTaskTree::QProcessTaskAdapter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qprocesstask.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QProcess
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QProcess = WAIT['QProcess']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProcessTaskAdapter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::QProcessTaskAdapter: a plain Python
  object standing in front of one C++ QtTaskTree::QProcessTaskAdapter.

  C++ hands a QtTaskTree::QProcessTaskAdapter around as a copy, so every C++
  QtTaskTree::QProcessTaskAdapter behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QProcessTaskAdapter that has a ritual
  and that Python can call so far, 1 name in all: '__call__'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::QProcessTaskAdapter::~QProcessTaskAdapter()': the
    destructor: Python removes its C++ QtTaskTree::QProcessTaskAdapter by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QtTaskTree::QProcessTaskAdapter is created at the first use, not
    by 'QtTaskTree::QProcessTaskAdapter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtTaskTree::QProcessTaskAdapter back gives a copy the
    ritual made for Python, in a new cute QtTaskTree::QProcessTaskAdapter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QProcessTaskAdapter'

  #  Qt's '~QtTaskTree::QProcessTaskAdapter()'. Naming it makes this a value
  #  class: Python owns every C++ QtTaskTree::QProcessTaskAdapter behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QtTaskTree19QProcessTaskAdapterD1Ev'

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

  @overload(QProcess, WAIT['QtTaskTree.QTaskInterface'])
  @overload(QProcess, NoneType)
  @overload(NoneType, WAIT['QtTaskTree.QTaskInterface'])
  @overload(NoneType, NoneType)
  def __call__(
      self,
      task: Optional[QProcess],
      iface: Optional[QtTaskTree.QTaskInterface],
  ) -> None:
    """
    Calls Qt's 'void QtTaskTree::QProcessTaskAdapter::operator()(QProcess
    *task, QTaskInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qprocesstaskadapter.html#operator()

    Parameters
    ----------

    task : Optional[QProcess]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iface : Optional[QtTaskTree.QTaskInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtTaskTree::QProcessTaskAdapter::operator()(QProcess *task,
    #      QTaskInterface *iface) const
    self.uglySide.call(
        'ritual_ZNK10QtTaskTree19QProcessTaskAdapterclEP8QProcessPNS_14QTas'
        'kInterfaceE',
        self._addressOf(task), self._addressOf(iface),
    )

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
