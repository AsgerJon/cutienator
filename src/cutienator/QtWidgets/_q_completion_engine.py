"""
QCompletionEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCompletionEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QModelIndex
  from . import QCompleterPrivate, QMatchData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCompleterPrivate = WAIT['QCompleterPrivate']
  QMatchData = WAIT['QMatchData']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCompletionEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCompletionEngine: a plain Python object standing in
  front of one C++ QCompletionEngine.

  What exists
  -----------

  Every function of Qt's QCompletionEngine that has a ritual and that Python
  can call so far, 7 names in all: 'filter', 'filterHistory', 'matchHint',
  'saveInCache', 'lookupCache', 'filterOnDemand', 'matchCount'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCompletionEngine::~QCompletionEngine()': the destructor: Python
    never removes a C++ QCompletionEngine.

  What to expect
  --------------

  - The C++ QCompletionEngine is created at the first use, not by
    'QCompletionEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCompletionEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCompletionEngine'

  #  A C++ QCompletionEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCompletionEngine'

  #  The functions Qt calls itself that QCompletionEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'filterOnDemand': (
          ('_ZN17QCompletionEngine14filterOnDemandEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'filter': (
          ('_ZN17QCompletionEngine6filterERK7QStringRK11QModelIndexi',
           ('address', 'value', 'QtWidgets:QMatchData'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QModelIndex, QMatchData)
  @overload(str, QModelIndex, NoneType)
  def matchHint(
      self,
      part: str,
      parent: QModelIndex,
      m: Optional[QMatchData],
  ) -> bool:
    """
    Calls Qt's 'bool QCompletionEngine::matchHint(const QString &part, const
    QModelIndex &parent, QMatchData *m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionengine.html#matchHint

    Parameters
    ----------

    part : str
      Passed on as it is: a QString is made of it for the call.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    m : Optional[QMatchData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCompletionEngine::matchHint(const QString &part, const
    #      QModelIndex &parent, QMatchData *m) const
    return self.uglySide.call(
        'ritual_ZNK17QCompletionEngine9matchHintERK7QStringRK11QModelIndexP'
        '10QMatchData',
        part, self._valueOf(parent), self._addressOf(m),
    )

  @overload(str, QModelIndex, QMatchData)
  @overload(str, QModelIndex, NoneType)
  def lookupCache(
      self,
      part: str,
      parent: QModelIndex,
      m: Optional[QMatchData],
  ) -> bool:
    """
    Calls Qt's 'bool QCompletionEngine::lookupCache(const QString &part,
    const QModelIndex &parent, QMatchData *m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionengine.html#lookupCache

    Parameters
    ----------

    part : str
      Passed on as it is: a QString is made of it for the call.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    m : Optional[QMatchData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCompletionEngine::lookupCache(const QString &part, const
    #      QModelIndex &parent, QMatchData *m) const
    return self.uglySide.call(
        'ritual_ZNK17QCompletionEngine11lookupCacheERK7QStringRK11QModelInd'
        'exP10QMatchData',
        part, self._valueOf(parent), self._addressOf(m),
    )

  def matchCount(self) -> int:
    """
    Calls Qt's 'int QCompletionEngine::matchCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionengine.html#matchCount
    """
    #  int QCompletionEngine::matchCount() const
    return self.uglySide.call('ritual_ZNK17QCompletionEngine10matchCountEv')

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
    'QCompletionEngine::QCompletionEngine(QCompleterPrivate *c)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionengine.html#QCompletionEngine

    Parameters
    ----------

    c : Optional[QCompleterPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCompletionEngine::QCompletionEngine(QCompleterPrivate *c)
    self._noteCreation(QCompletionEngine, lambda: Rituals.call(
        'ritual_ZN17QCompletionEngineC1EP17QCompleterPrivate',
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

  @overload(QStringList)
  def filter(self, parts: QStringList) -> None:
    """
    Calls Qt's 'void QCompletionEngine::filter(const QStringList &parts)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionengine.html#filter

    Parameters
    ----------

    parts : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCompletionEngine::filter(const QStringList &parts)
    self.uglySide.call(
        'ritual_ZN17QCompletionEngine6filterERK5QListI7QStringE',
        self._valueOf(parts),
    )

  @overload(str, QModelIndex, int)
  def filter(self, a0: str, a1: QModelIndex, a2: int) -> QMatchData:
    """
    Calls Qt's 'QMatchData QCompletionEngine::filter(const QString &a0, const
    QModelIndex &a1, int a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionengine.html#filter

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
    #  QMatchData QCompletionEngine::filter(const QString &a0, const
    #      QModelIndex &a1, int a2)
    address = self.uglySide.call(
        'ritual_ZN17QCompletionEngine6filterERK7QStringRK11QModelIndexi',
        a0, self._valueOf(a1), a2,
    )
    from . import QMatchData
    return QMatchData._cuteOwning(address)

  def filterHistory(self) -> QMatchData:
    """
    Calls Qt's 'QMatchData QCompletionEngine::filterHistory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionengine.html#filterHistory

    Returns
    -------

    QMatchData
      A new cute QMatchData around the copy Qt gave back. Python owns it.
    """
    #  QMatchData QCompletionEngine::filterHistory()
    address = self.uglySide.call(
        'ritual_ZN17QCompletionEngine13filterHistoryEv',
    )
    from . import QMatchData
    return QMatchData._cuteOwning(address)

  @overload(str, QModelIndex, QMatchData)
  def saveInCache(self, a0: str, a1: QModelIndex, a2: QMatchData) -> None:
    """
    Calls Qt's 'void QCompletionEngine::saveInCache(QString a0, const
    QModelIndex &a1, const QMatchData &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompletionengine.html#saveInCache

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a2 : QMatchData
      Passed on as a value: Qt reads the C++ QMatchData, which stays Python's
      own.
    """
    #  void QCompletionEngine::saveInCache(QString a0, const QModelIndex &a1,
    #      const QMatchData &a2)
    self.uglySide.call(
        'ritual_ZN17QCompletionEngine11saveInCacheE7QStringRK11QModelIndexR'
        'K10QMatchData',
        a0, self._valueOf(a1), self._valueOf(a2),
    )

  @overload(int)
  def filterOnDemand(self, a0: int) -> None:
    """
    Calls Qt's 'void QCompletionEngine::filterOnDemand(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompletionengine.html#filterOnDemand

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCompletionEngine::filterOnDemand(int a0)
    ritual = 'ritual_ZN17QCompletionEngine14filterOnDemandEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QCompletionEngine14filterOnDemandEi'
    self.uglySide.call(ritual, a0)
