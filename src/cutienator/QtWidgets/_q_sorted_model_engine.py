"""
QSortedModelEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSortedModelEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
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
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSortedModelEngine(QCompletionEngine):
  """
  The cute side of Qt's QSortedModelEngine: a plain Python object standing in
  front of one C++ QSortedModelEngine.

  It is built on the cute 'QCompletionEngine', as Qt's QSortedModelEngine is
  built on Qt's QCompletionEngine, and has everything that class has.

  C++ hands a QSortedModelEngine around as a copy, so every C++
  QSortedModelEngine behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSortedModelEngine that has a ritual and that Python
  can call so far, 3 names in all: 'filter', 'indexHint', 'sortOrder'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSortedModelEngine::~QSortedModelEngine()': the destructor: Python
    removes its C++ QSortedModelEngine by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSortedModelEngine is created at the first use, not by
    'QSortedModelEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSortedModelEngine back gives a copy the ritual made
    for Python, in a new cute QSortedModelEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSortedModelEngine'

  #  A C++ QSortedModelEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSortedModelEngine'

  #  Qt's '~QSortedModelEngine()'. Naming it makes this a value class: Python
  #  owns every C++ QSortedModelEngine behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSortedModelEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def sortOrder(self, a0: QModelIndex) -> Qt.SortOrder:
    """
    Calls Qt's 'Qt::SortOrder QSortedModelEngine::sortOrder(const QModelIndex
    &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsortedmodelengine.html#sortOrder

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.SortOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.SortOrder(number)'
      gives.
    """
    #  Qt::SortOrder QSortedModelEngine::sortOrder(const QModelIndex &a0)
    #      const
    return Qt.SortOrder(self.uglySide.call(
        'ritual_ZNK18QSortedModelEngine9sortOrderERK11QModelIndex',
        self._valueOf(a0),
    ))

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
    'QSortedModelEngine::QSortedModelEngine(QCompleterPrivate *c)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortedmodelengine.html#QSortedModelEngine

    Parameters
    ----------

    c : Optional[QCompleterPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSortedModelEngine::QSortedModelEngine(QCompleterPrivate *c)
    self._noteCreation(QSortedModelEngine, lambda: Rituals.call(
        'ritual_ZN18QSortedModelEngineC1EP17QCompleterPrivate',
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

  @overload(str, QModelIndex, int)
  def filter(self, a0: str, a1: QModelIndex, a2: int) -> QMatchData:
    """
    Calls Qt's 'QMatchData QSortedModelEngine::filter(const QString &a0,
    const QModelIndex &a1, int a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qsortedmodelengine.html#filter

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
    #  QMatchData QSortedModelEngine::filter(const QString &a0, const
    #      QModelIndex &a1, int a2)
    ritual = (
        'ritual_ZN18QSortedModelEngine6filterERK7QStringRK11QModelIndexi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QSortedModelEngine6filterERK7QStringRK11QModelInd'
          'exi')
    address = self.uglySide.call(ritual, a0, self._valueOf(a1), a2)
    from . import QMatchData
    return QMatchData._cuteOwning(address)

  @overload(str, QModelIndex, Qt.SortOrder)
  def indexHint(
      self,
      a0: str,
      a1: QModelIndex,
      a2: Qt.SortOrder,
  ) -> QIndexMapper:
    """
    Calls Qt's 'QIndexMapper QSortedModelEngine::indexHint(QString a0, const
    QModelIndex &a1, Qt::SortOrder a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qsortedmodelengine.html#indexHint

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : Qt.SortOrder
      Passed on as its number.

    Returns
    -------

    QIndexMapper
      A new cute QIndexMapper around the copy Qt gave back. Python owns it.
    """
    #  QIndexMapper QSortedModelEngine::indexHint(QString a0, const
    #      QModelIndex &a1, Qt::SortOrder a2)
    address = self.uglySide.call(
        'ritual_ZN18QSortedModelEngine9indexHintE7QStringRK11QModelIndexN2Q'
        't9SortOrderE',
        a0, self._valueOf(a1), a2.value,
    )
    from . import QIndexMapper
    return QIndexMapper._cuteOwning(address)
