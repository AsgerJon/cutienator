"""
QQmlJS::AotStats binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJS::AotStats to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QJsonDocument


class AotStats(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AotStats: a plain Python object standing in
  front of one C++ QQmlJS::AotStats.

  C++ hands a QQmlJS::AotStats around as a copy, so every C++
  QQmlJS::AotStats behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::AotStats that has a ritual and that Python
  can call so far, 5 names in all: 'registerFile', 'addEntry', 'insert',
  'saveToDisk', 'toJsonDocument'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHash<QString, QHash<QString, QList<AotStatsEntry>>>
    &QQmlJS::AotStats::entries() const': gives a type Python has no way to
    take yet.
  - Qt's 'std::optional<QStringList> QQmlJS::AotStats::readAllLines(const
    QString &path)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<AotStats> QQmlJS::AotStats::parseAotstatsFile(const
    QString &aotstatsPath)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<AotStats>
    QQmlJS::AotStats::aggregateAotstatsList(const QString
    &aotstatsListPath)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<AotStats> QQmlJS::AotStats::fromJsonDocument(const
    QJsonDocument &a0)': gives a type Python has no way to take yet.
  - Qt's 'QQmlJS::AotStats::~AotStats()': the destructor: Python removes its
    C++ QQmlJS::AotStats by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJS::AotStats is created at the first use, not by
    'QQmlJS::AotStats(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::AotStats back gives a copy the ritual made
    for Python, in a new cute QQmlJS::AotStats.
  - Each name of Qt's QQmlJS::AotStats that has no cute function yet,
    'aggregateAotstatsList', 'entries', 'fromJsonDocument',
    'parseAotstatsFile', 'readAllLines', holds a function that raises
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
  __qt_class__ = 'QQmlJS::AotStats'

  #  Qt's '~QQmlJS::AotStats()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJS::AotStats behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS8AotStatsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def saveToDisk(self, filepath: str) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AotStats::saveToDisk(const QString &filepath)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-aotstats.html#saveToDisk

    Parameters
    ----------

    filepath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJS::AotStats::saveToDisk(const QString &filepath) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS8AotStats10saveToDiskERK7QString', filepath,
    )

  def toJsonDocument(self) -> QJsonDocument:
    """
    Calls Qt's 'QJsonDocument QQmlJS::AotStats::toJsonDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-aotstats.html#toJsonDocument

    Returns
    -------

    QJsonDocument
      A new cute QJsonDocument around the copy Qt gave back. Python owns it.
    """
    #  QJsonDocument QQmlJS::AotStats::toJsonDocument() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS8AotStats14toJsonDocumentEv',
    )
    from ..QtCore import QJsonDocument
    return QJsonDocument._cuteOwning(address)

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

  @overload(str, str)
  def registerFile(self, moduleId: str, filepath: str) -> None:
    """
    Calls Qt's 'void QQmlJS::AotStats::registerFile(const QString &moduleId,
    const QString &filepath)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-aotstats.html#registerFile

    Parameters
    ----------

    moduleId : str
      Passed on as it is: a QString is made of it for the call.

    filepath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJS::AotStats::registerFile(const QString &moduleId, const
    #      QString &filepath)
    self.uglySide.call(
        'ritual_ZN6QQmlJS8AotStats12registerFileERK7QStringS3_',
        moduleId, filepath,
    )

  @overload(str, str, WAIT['QQmlJS.AotStatsEntry'])
  def addEntry(
      self,
      moduleId: str,
      filepath: str,
      entry: QQmlJS.AotStatsEntry,
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AotStats::addEntry(const QString &moduleId,
    const QString &filepath, const AotStatsEntry &entry)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-aotstats.html#addEntry

    Parameters
    ----------

    moduleId : str
      Passed on as it is: a QString is made of it for the call.

    filepath : str
      Passed on as it is: a QString is made of it for the call.

    entry : QQmlJS.AotStatsEntry
      Passed on as a value: Qt reads the C++ QQmlJS::AotStatsEntry, which
      stays Python's own.
    """
    #  void QQmlJS::AotStats::addEntry(const QString &moduleId, const QString
    #      &filepath, const AotStatsEntry &entry)
    self.uglySide.call(
        'ritual_ZN6QQmlJS8AotStats8addEntryERK7QStringS3_RKNS_13AotStatsEnt'
        'ryE',
        moduleId, filepath, self._valueOf(entry),
    )

  @overload(THIS)
  def insert(self, other: AotStats) -> None:
    """
    Calls Qt's 'void QQmlJS::AotStats::insert(const AotStats &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-aotstats.html#insert

    Parameters
    ----------

    other : AotStats
      Passed on as a value: Qt reads the C++ QQmlJS::AotStats, which stays
      Python's own.
    """
    #  void QQmlJS::AotStats::insert(const AotStats &other)
    self.uglySide.call(
        'ritual_ZN6QQmlJS8AotStats6insertERKS0_', self._valueOf(other),
    )

  @staticmethod
  def aggregateAotstatsList(*__, **_) -> Never:
    """
    Qt's 'std::optional<AotStats>
    QQmlJS::AotStats::aggregateAotstatsList(const QString
    &aotstatsListPath)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AotStats.aggregateAotstatsList' has no cute function yet. "
        "Qt's 'std::optional<AotStats> "
        "QQmlJS::AotStats::aggregateAotstatsList(const QString "
        "&aotstatsListPath)': gives a type Python has no way to take yet.")

  @staticmethod
  def entries(*__, **_) -> Never:
    """
    Qt's 'const QHash<QString, QHash<QString, QList<AotStatsEntry>>>
    &QQmlJS::AotStats::entries() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AotStats.entries' has no cute function yet. Qt's 'const "
        "QHash<QString, QHash<QString, QList<AotStatsEntry>>> "
        "&QQmlJS::AotStats::entries() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def fromJsonDocument(*__, **_) -> Never:
    """
    Qt's 'std::optional<AotStats> QQmlJS::AotStats::fromJsonDocument(const
    QJsonDocument &a0)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AotStats.fromJsonDocument' has no cute function yet. Qt's "
        "'std::optional<AotStats> QQmlJS::AotStats::fromJsonDocument(const "
        "QJsonDocument &a0)': gives a type Python has no way to take yet.")

  @staticmethod
  def parseAotstatsFile(*__, **_) -> Never:
    """
    Qt's 'std::optional<AotStats> QQmlJS::AotStats::parseAotstatsFile(const
    QString &aotstatsPath)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AotStats.parseAotstatsFile' has no cute function yet. Qt's "
        "'std::optional<AotStats> QQmlJS::AotStats::parseAotstatsFile(const "
        "QString &aotstatsPath)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def readAllLines(*__, **_) -> Never:
    """
    Qt's 'std::optional<QStringList> QQmlJS::AotStats::readAllLines(const
    QString &path)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AotStats.readAllLines' has no cute function yet. Qt's "
        "'std::optional<QStringList> QQmlJS::AotStats::readAllLines(const "
        "QString &path)': gives a type Python has no way to take yet.")
