"""
QQuickItemViewChangeSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickItemViewChangeSet to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtQmlModels import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlChangeSet = WAIT['QQmlChangeSet']


class QQuickItemViewChangeSet(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemViewChangeSet: a plain Python object
  standing in front of one C++ QQuickItemViewChangeSet.

  C++ hands a QQuickItemViewChangeSet around as a copy, so every C++
  QQuickItemViewChangeSet behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickItemViewChangeSet that has a ritual and that
  Python can call so far, 5 names in all: 'hasPendingChanges', 'prepare',
  'reset', 'applyChanges', 'applyBufferedChanges'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickItemViewChangeSet::~QQuickItemViewChangeSet()': the
    destructor: Python removes its C++ QQuickItemViewChangeSet by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QQuickItemViewChangeSet is created at the first use, not by
    'QQuickItemViewChangeSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickItemViewChangeSet back gives a copy the ritual
    made for Python, in a new cute QQuickItemViewChangeSet.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewChangeSet'

  #  Qt's '~QQuickItemViewChangeSet()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickItemViewChangeSet behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQuickItemViewChangeSetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasPendingChanges(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewChangeSet::hasPendingChanges() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewchangeset.html#hasPendingChanges
    """
    #  bool QQuickItemViewChangeSet::hasPendingChanges() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickItemViewChangeSet17hasPendingChangesEv',
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
    'QQuickItemViewChangeSet::QQuickItemViewChangeSet()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewchangeset.html
    """
    #  QQuickItemViewChangeSet::QQuickItemViewChangeSet()
    self._noteCreation(QQuickItemViewChangeSet, lambda: Rituals.call(
        'ritual_ZN23QQuickItemViewChangeSetC1Ev',
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

  @overload(int, int)
  def prepare(self, currentIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickItemViewChangeSet::prepare(int currentIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewchangeset.html#prepare

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickItemViewChangeSet::prepare(int currentIndex, int count)
    self.uglySide.call(
        'ritual_ZN23QQuickItemViewChangeSet7prepareEii', currentIndex, count,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewChangeSet::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewchangeset.html#reset
    """
    #  void QQuickItemViewChangeSet::reset()
    self.uglySide.call('ritual_ZN23QQuickItemViewChangeSet5resetEv')

  @overload(QQmlChangeSet)
  def applyChanges(self, changeSet: QQmlChangeSet) -> None:
    """
    Calls Qt's 'void QQuickItemViewChangeSet::applyChanges(const
    QQmlChangeSet &changeSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewchangeset.html#applyChanges

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.
    """
    #  void QQuickItemViewChangeSet::applyChanges(const QQmlChangeSet
    #      &changeSet)
    self.uglySide.call(
        'ritual_ZN23QQuickItemViewChangeSet12applyChangesERK13QQmlChangeSet',
        self._valueOf(changeSet),
    )

  @overload(THIS)
  def applyBufferedChanges(self, other: QQuickItemViewChangeSet) -> None:
    """
    Calls Qt's 'void QQuickItemViewChangeSet::applyBufferedChanges(const
    QQuickItemViewChangeSet &other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewchangeset.html#applyBufferedChanges

    Parameters
    ----------

    other : QQuickItemViewChangeSet
      Passed on as a value: Qt reads the C++ QQuickItemViewChangeSet, which
      stays Python's own.
    """
    #  void QQuickItemViewChangeSet::applyBufferedChanges(const
    #      QQuickItemViewChangeSet &other)
    self.uglySide.call(
        'ritual_ZN23QQuickItemViewChangeSet20applyBufferedChangesERKS_',
        self._valueOf(other),
    )
