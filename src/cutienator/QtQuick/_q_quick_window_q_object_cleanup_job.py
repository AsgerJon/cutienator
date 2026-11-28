"""
QQuickWindowQObjectCleanupJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickWindowQObjectCleanupJob to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QRunnable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindowQObjectCleanupJob(QRunnable):
  """
  The cute side of Qt's QQuickWindowQObjectCleanupJob: a plain Python object
  standing in front of one C++ QQuickWindowQObjectCleanupJob.

  It is built on the cute 'QRunnable', as Qt's QQuickWindowQObjectCleanupJob
  is built on Qt's QRunnable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWindowQObjectCleanupJob that has a ritual and
  that Python can call so far, 2 names in all: 'run', 'schedule'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickWindowQObjectCleanupJob is created at the first use, not by
    'QQuickWindowQObjectCleanupJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWindowQObjectCleanupJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickWindow, QObject)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def schedule(
      window: Optional[QQuickWindow],
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowQObjectCleanupJob::schedule(QQuickWindow
    *window, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqobjectcleanupjob.html#schedule

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowQObjectCleanupJob::schedule(QQuickWindow *window,
    #      QObject *object)
    Rituals.call(
        'ritual_ZN29QQuickWindowQObjectCleanupJob8scheduleEP12QQuickWindowP'
        '7QObject',
        CuteMixin._addressOf(window), CuteMixin._addressOf(object,
        'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindowQObjectCleanupJob'

  #  A C++ QQuickWindowQObjectCleanupJob Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWindowQObjectCleanupJob'

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, o: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWindowQObjectCleanupJob::QQuickWindowQObjectCleanupJob(QObject
    *o)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqobjectcleanupjob.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWindowQObjectCleanupJob::QQuickWindowQObjectCleanupJob(QObject
    #      *o)
    self._noteCreation(QQuickWindowQObjectCleanupJob, lambda: Rituals.call(
        'ritual_ZN29QQuickWindowQObjectCleanupJobC1EP7QObject',
        self._addressOf(o, 'QObject'),
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

  def run(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQObjectCleanupJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqobjectcleanupjob.html#run
    """
    #  void QQuickWindowQObjectCleanupJob::run()
    ritual = 'ritual_ZN29QQuickWindowQObjectCleanupJob3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QQuickWindowQObjectCleanupJob3runEv'
    self.uglySide.call(ritual)
