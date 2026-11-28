"""
QQmlJS::QQmlJSAotCompilerStats binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJS::QQmlJSAotCompilerStats to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QQmlJSAotCompilerStats(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::QQmlJSAotCompilerStats: a plain Python object
  standing in front of one C++ QQmlJS::QQmlJSAotCompilerStats.

  C++ hands a QQmlJS::QQmlJSAotCompilerStats around as a copy, so every C++
  QQmlJS::QQmlJSAotCompilerStats behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::QQmlJSAotCompilerStats that has a ritual and
  that Python can call so far, 7 names in all: 'instance', 'recordAotStats',
  'setRecordAotStats', 'moduleId', 'setModuleId', 'registerFile', 'addEntry'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::QQmlJSAotCompilerStats::~QQmlJSAotCompilerStats()': the
    destructor: Python removes its C++ QQmlJS::QQmlJSAotCompilerStats by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJS::QQmlJSAotCompilerStats is created at the first use, not
    by 'QQmlJS::QQmlJSAotCompilerStats(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::QQmlJSAotCompilerStats back gives a copy the
    ritual made for Python, in a new cute QQmlJS::QQmlJSAotCompilerStats.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QQmlJS.AotStats]:
    """
    Calls Qt's 'AotStats *QQmlJS::QQmlJSAotCompilerStats::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html#instance

    Returns
    -------

    Optional[QQmlJS.AotStats]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AotStats *QQmlJS::QQmlJSAotCompilerStats::instance()
    address = Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats8instanceEv',
    )
    return QQmlJS.AotStats._cuteAt(address)

  @staticmethod
  def recordAotStats() -> bool:
    """
    Calls Qt's 'bool QQmlJS::QQmlJSAotCompilerStats::recordAotStats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html#recordAotStats
    """
    #  bool QQmlJS::QQmlJSAotCompilerStats::recordAotStats()
    return Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats14recordAotStatsEv',
    )

  @staticmethod
  @overload(bool)
  def setRecordAotStats(recordAotStats: bool) -> None:
    """
    Calls Qt's 'void QQmlJS::QQmlJSAotCompilerStats::setRecordAotStats(bool
    recordAotStats)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html

    Parameters
    ----------

    recordAotStats : bool
      Passed on as it is.
    """
    #  void QQmlJS::QQmlJSAotCompilerStats::setRecordAotStats(bool
    #      recordAotStats)
    Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats17setRecordAotStatsEb',
        recordAotStats,
    )

  @staticmethod
  def moduleId() -> str:
    """
    Calls Qt's 'QString QQmlJS::QQmlJSAotCompilerStats::moduleId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html#moduleId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::QQmlJSAotCompilerStats::moduleId()
    return Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats8moduleIdEv',
    )

  @staticmethod
  @overload(str)
  def setModuleId(moduleId: str) -> None:
    """
    Calls Qt's 'void QQmlJS::QQmlJSAotCompilerStats::setModuleId(const
    QString &moduleId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html#setModuleId

    Parameters
    ----------

    moduleId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJS::QQmlJSAotCompilerStats::setModuleId(const QString
    #      &moduleId)
    Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats11setModuleIdERK7QString',
        moduleId,
    )

  @staticmethod
  @overload(str)
  def registerFile(filepath: str) -> None:
    """
    Calls Qt's 'void QQmlJS::QQmlJSAotCompilerStats::registerFile(const
    QString &filepath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html#registerFile

    Parameters
    ----------

    filepath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJS::QQmlJSAotCompilerStats::registerFile(const QString
    #      &filepath)
    Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats12registerFileERK7QString',
        filepath,
    )

  @staticmethod
  @overload(str, WAIT['QQmlJS.AotStatsEntry'])
  def addEntry(filepath: str, entry: QQmlJS.AotStatsEntry) -> None:
    """
    Calls Qt's 'void QQmlJS::QQmlJSAotCompilerStats::addEntry(const QString
    &filepath, const QQmlJS::AotStatsEntry &entry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-qqmljsaotcompilerstats.html#addEntry

    Parameters
    ----------

    filepath : str
      Passed on as it is: a QString is made of it for the call.

    entry : QQmlJS.AotStatsEntry
      Passed on as a value: Qt reads the C++ QQmlJS::AotStatsEntry, which
      stays Python's own.
    """
    #  void QQmlJS::QQmlJSAotCompilerStats::addEntry(const QString &filepath,
    #      const QQmlJS::AotStatsEntry &entry)
    Rituals.call(
        'ritual_ZN6QQmlJS22QQmlJSAotCompilerStats8addEntryERK7QStringRKNS_1'
        '3AotStatsEntryE',
        filepath, CuteMixin._valueOf(entry),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::QQmlJSAotCompilerStats'

  #  Qt's '~QQmlJS::QQmlJSAotCompilerStats()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlJS::QQmlJSAotCompilerStats behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS22QQmlJSAotCompilerStatsD1Ev'

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
