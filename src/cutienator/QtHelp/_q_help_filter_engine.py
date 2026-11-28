"""
QHelpFilterEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpfilterengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVersionNumber
  from . import QHelpCollectionHandler, QHelpEngineCore, QHelpFilterData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpCollectionHandler = WAIT['QHelpCollectionHandler']
  QHelpEngineCore = WAIT['QHelpEngineCore']
  QHelpFilterData = WAIT['QHelpFilterData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpFilterEngine(QObject):
  """
  The cute side of Qt's QHelpFilterEngine: a plain Python object standing in
  front of one C++ QHelpFilterEngine.

  It is built on the cute 'QObject', as Qt's QHelpFilterEngine is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpFilterEngine that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'namespaceToVersion',
  'filters', 'activeFilter', 'setActiveFilter', 'availableComponents',
  'availableVersions', 'filterData', 'setFilterData', 'removeFilter',
  'namespacesForFilter', 'indices', 'filterActivated',
  'setCollectionHandler'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpFilterEngine::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpFilterEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QMap<QString, QString> QHelpFilterEngine::namespaceToComponent()
    const': gives a type Python has no way to take yet.
  - Qt's 'QHelpFilterEngine::~QHelpFilterEngine()': the destructor: Python
    never removes a C++ QHelpFilterEngine.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpFilterEngine is created at the first use, not by
    'QHelpFilterEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpFilterEngine.
  - Qt tells when it has removed the C++ QHelpFilterEngine. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHelpFilterEngine that has no cute function yet,
    'namespaceToComponent', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QHelpFilterEngine::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterengine.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpFilterEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QHelpFilterEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpFilterEngine'

  #  A C++ QHelpFilterEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpFilterEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpFilterEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpFilterEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def namespaceToVersion(self) -> QMap[str, QVersionNumber]:
    """
    Calls Qt's 'QMap<QString, QVersionNumber>
    QHelpFilterEngine::namespaceToVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#namespaceToVersion

    Returns
    -------

    QMap[str, QVersionNumber]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<QString, QVersionNumber> QHelpFilterEngine::namespaceToVersion()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine18namespaceToVersionEv',
    )
    from ..QtCore import QVersionNumber
    return QMap[str, QVersionNumber]._cuteOwning(address)

  def filters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpFilterEngine::filters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterengine.html#filters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpFilterEngine::filters() const
    address = self.uglySide.call('ritual_ZNK17QHelpFilterEngine7filtersEv')
    return QStringList._cuteOwning(address)

  def activeFilter(self) -> str:
    """
    Calls Qt's 'QString QHelpFilterEngine::activeFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#activeFilter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpFilterEngine::activeFilter() const
    return self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine12activeFilterEv',
    )

  def availableComponents(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpFilterEngine::availableComponents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#availableComponents

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpFilterEngine::availableComponents() const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine19availableComponentsEv',
    )
    return QStringList._cuteOwning(address)

  def availableVersions(self) -> QList[QVersionNumber]:
    """
    Calls Qt's 'QList<QVersionNumber> QHelpFilterEngine::availableVersions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#availableVersions

    Returns
    -------

    QList[QVersionNumber]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVersionNumber> QHelpFilterEngine::availableVersions() const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine17availableVersionsEv',
    )
    from ..QtCore import QVersionNumber
    return QList[QVersionNumber]._cuteOwning(address)

  @overload(str)
  def filterData(self, filterName: str) -> QHelpFilterData:
    """
    Calls Qt's 'QHelpFilterData QHelpFilterEngine::filterData(const QString
    &filterName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterengine.html#filterData

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QHelpFilterData
      A new cute QHelpFilterData around the copy Qt gave back. Python owns
      it.
    """
    #  QHelpFilterData QHelpFilterEngine::filterData(const QString
    #      &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine10filterDataERK7QString', filterName,
    )
    from . import QHelpFilterData
    return QHelpFilterData._cuteOwning(address)

  @overload(str)
  def namespacesForFilter(self, filterName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpFilterEngine::namespacesForFilter(const
    QString &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#namespacesForFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpFilterEngine::namespacesForFilter(const QString
    #      &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine19namespacesForFilterERK7QString',
        filterName,
    )
    return QStringList._cuteOwning(address)

  @overload()
  def indices(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpFilterEngine::indices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterengine.html#indices

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpFilterEngine::indices() const
    address = self.uglySide.call('ritual_ZNK17QHelpFilterEngine7indicesEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def indices(self, filterName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpFilterEngine::indices(const QString
    &filterName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterengine.html#indices

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpFilterEngine::indices(const QString &filterName)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpFilterEngine7indicesERK7QString', filterName,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setActiveFilter(self, filterName: str) -> bool:
    """
    Calls Qt's 'bool QHelpFilterEngine::setActiveFilter(const QString
    &filterName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#setActiveFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpFilterEngine::setActiveFilter(const QString &filterName)
    return self.uglySide.call(
        'ritual_ZN17QHelpFilterEngine15setActiveFilterERK7QString',
        filterName,
    )

  @overload(str, QHelpFilterData)
  def setFilterData(
      self,
      filterName: str,
      filterData: QHelpFilterData,
  ) -> bool:
    """
    Calls Qt's 'bool QHelpFilterEngine::setFilterData(const QString
    &filterName, const QHelpFilterData &filterData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#setFilterData

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    filterData : QHelpFilterData
      Passed on as a value: Qt reads the C++ QHelpFilterData, which stays
      Python's own.
    """
    #  bool QHelpFilterEngine::setFilterData(const QString &filterName, const
    #      QHelpFilterData &filterData)
    return self.uglySide.call(
        'ritual_ZN17QHelpFilterEngine13setFilterDataERK7QStringRK15QHelpFil'
        'terData',
        filterName, self._valueOf(filterData),
    )

  @overload(QHelpCollectionHandler)
  @overload(NoneType)
  def setCollectionHandler(
      self,
      collectionHandler: Optional[QHelpCollectionHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QHelpFilterEngine::setCollectionHandler(QHelpCollectionHandler
    *collectionHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#setCollectionHandler

    Parameters
    ----------

    collectionHandler : Optional[QHelpCollectionHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHelpFilterEngine::setCollectionHandler(QHelpCollectionHandler
    #      *collectionHandler)
    self.uglySide.call(
        'ritual_ZN17QHelpFilterEngine20setCollectionHandlerEP22QHelpCollect'
        'ionHandler',
        self._addressOf(collectionHandler),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHelpEngineCore)
  @overload(NoneType)
  def __init__(self, helpEngine: Optional[QHelpEngineCore]) -> None:
    """
    Notes what was given, for Qt's
    'QHelpFilterEngine::QHelpFilterEngine(QHelpEngineCore *helpEngine)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#QHelpFilterEngine

    Parameters
    ----------

    helpEngine : Optional[QHelpEngineCore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHelpFilterEngine::QHelpFilterEngine(QHelpEngineCore *helpEngine)
    self._noteCreation(QHelpFilterEngine, lambda: Rituals.call(
        'ritual_ZN17QHelpFilterEngineC1EP15QHelpEngineCore',
        self._addressOf(helpEngine),
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

  @overload(str)
  def removeFilter(self, filterName: str) -> bool:
    """
    Calls Qt's 'bool QHelpFilterEngine::removeFilter(const QString
    &filterName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#removeFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpFilterEngine::removeFilter(const QString &filterName)
    return self.uglySide.call(
        'ritual_ZN17QHelpFilterEngine12removeFilterERK7QString', filterName,
    )

  @overload(str)
  def filterActivated(self, newFilter: str) -> None:
    """
    Calls Qt's 'void QHelpFilterEngine::filterActivated(const QString
    &newFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterengine.html#filterActivated

    Parameters
    ----------

    newFilter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpFilterEngine::filterActivated(const QString &newFilter)
    self.uglySide.call(
        'ritual_ZN17QHelpFilterEngine15filterActivatedERK7QString',
        newFilter,
    )

  @staticmethod
  def namespaceToComponent(*__, **_) -> Never:
    """
    Qt's 'QMap<QString, QString> QHelpFilterEngine::namespaceToComponent()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpFilterEngine.namespaceToComponent' has no cute function yet. "
        "Qt's 'QMap<QString, QString> "
        "QHelpFilterEngine::namespaceToComponent() const': gives a type "
        "Python has no way to take yet.")
