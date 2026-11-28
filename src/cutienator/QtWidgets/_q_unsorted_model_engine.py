"""
QUnsortedModelEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QUnsortedModelEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QCompletionEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QModelIndex
  from . import QCompleterPrivate, QIndexMapper, QMatchData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCompleterPrivate = WAIT['QCompleterPrivate']
  QIndexMapper = WAIT['QIndexMapper']
  QMatchData = WAIT['QMatchData']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUnsortedModelEngine(QCompletionEngine):
  """
  The cute side of Qt's QUnsortedModelEngine: a plain Python object standing
  in front of one C++ QUnsortedModelEngine.

  It is built on the cute 'QCompletionEngine', as Qt's QUnsortedModelEngine
  is built on Qt's QCompletionEngine, and has everything that class has.

  C++ hands a QUnsortedModelEngine around as a copy, so every C++
  QUnsortedModelEngine behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUnsortedModelEngine that has a ritual and that
  Python can call so far, 3 names in all: 'filterOnDemand', 'filter',
  'buildIndices'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUnsortedModelEngine::~QUnsortedModelEngine()': the destructor:
    Python removes its C++ QUnsortedModelEngine by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QUnsortedModelEngine is created at the first use, not by
    'QUnsortedModelEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUnsortedModelEngine back gives a copy the ritual
    made for Python, in a new cute QUnsortedModelEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUnsortedModelEngine'

  #  Qt's '~QUnsortedModelEngine()'. Naming it makes this a value class:
  #  Python owns every C++ QUnsortedModelEngine behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QUnsortedModelEngineD1Ev'

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

  @overload(QCompleterPrivate)
  @overload(NoneType)
  def __init__(self, c: Optional[QCompleterPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QUnsortedModelEngine::QUnsortedModelEngine(QCompleterPrivate *c)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qunsortedmodelengine.html#QUnsortedModelEngine

    Parameters
    ----------

    c : Optional[QCompleterPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QUnsortedModelEngine::QUnsortedModelEngine(QCompleterPrivate *c)
    self._noteCreation(QUnsortedModelEngine, lambda: Rituals.call(
        'ritual_ZN20QUnsortedModelEngineC1EP17QCompleterPrivate',
        self._addressOf(c),
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

  @overload(int)
  def filterOnDemand(self, a0: int) -> None:
    """
    Calls Qt's 'void QUnsortedModelEngine::filterOnDemand(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunsortedmodelengine.html#filterOnDemand

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QUnsortedModelEngine::filterOnDemand(int a0)
    ritual = 'ritual_ZN20QUnsortedModelEngine14filterOnDemandEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QUnsortedModelEngine14filterOnDemandEi'
    self.uglySide.call(ritual, a0)

  @overload(str, QModelIndex, int)
  def filter(self, a0: str, a1: QModelIndex, a2: int) -> QMatchData:
    """
    Calls Qt's 'QMatchData QUnsortedModelEngine::filter(const QString &a0,
    const QModelIndex &a1, int a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qunsortedmodelengine.html#filter

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : int
      Passed on as it is.

    Returns
    -------

    QMatchData
      A new cute QMatchData around the copy Qt gave back. Python owns it.
    """
    #  QMatchData QUnsortedModelEngine::filter(const QString &a0, const
    #      QModelIndex &a1, int a2)
    ritual = (
        'ritual_ZN20QUnsortedModelEngine6filterERK7QStringRK11QModelIndexi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QUnsortedModelEngine6filterERK7QStringRK11QModelI'
          'ndexi')
    address = self.uglySide.call(ritual, a0, self._valueOf(a1), a2)
    from . import QMatchData
    return QMatchData._cuteOwning(address)

  @overload(str, QModelIndex, int, QIndexMapper, QMatchData)
  @overload(str, QModelIndex, int, QIndexMapper, NoneType)
  def buildIndices(
      self,
      str: str,
      parent: QModelIndex,
      n: int,
      iv: QIndexMapper,
      m: Optional[QMatchData],
  ) -> int:
    """
    Calls Qt's 'int QUnsortedModelEngine::buildIndices(const QString &str,
    const QModelIndex &parent, int n, const QIndexMapper &iv, QMatchData
    *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunsortedmodelengine.html#buildIndices

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    n : int
      Passed on as it is.

    iv : QIndexMapper
      Passed on as a value: Qt reads the C++ QIndexMapper, which stays
      Python's own.

    m : Optional[QMatchData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QUnsortedModelEngine::buildIndices(const QString &str, const
    #      QModelIndex &parent, int n, const QIndexMapper &iv, QMatchData *m)
    return self.uglySide.call(
        'ritual_ZN20QUnsortedModelEngine12buildIndicesERK7QStringRK11QModel'
        'IndexiRK12QIndexMapperP10QMatchData',
        str, self._valueOf(parent), n, self._valueOf(iv), self._addressOf(m),
    )
