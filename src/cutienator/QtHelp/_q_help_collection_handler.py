"""
QHelpCollectionHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/6.12.0/QtHelp/private/qhelpcollectionhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHelpCollectionHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl, QVariant, QVersionNumber
  from ..QtSql import QSqlQuery
  from . import QHelpFilterData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpFilterData = WAIT['QHelpFilterData']
  QSqlQuery = WAIT['QSqlQuery']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpCollectionHandler(QObject):
  """
  The cute side of Qt's QHelpCollectionHandler: a plain Python object
  standing in front of one C++ QHelpCollectionHandler.

  It is built on the cute 'QObject', as Qt's QHelpCollectionHandler is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpCollectionHandler that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'collectionFile',
  'customFilters', 'filterAttributes', 'filters', 'availableComponents',
  'availableVersions', 'namespaceToVersion', 'filterData', 'setFilterData',
  'removeFilter', 'registeredDocumentation', 'customValue',
  'registerComponent', 'registerVersion', 'setReadOnly', 'buildQUrl',
  'error', 'namespaceVersion', 'createTables', 'closeDB',
  'recreateIndexAndNamespaceFilterTables', 'unregisterIndexTable',
  'absoluteDocPath', 'isTimeStampCorrect', 'hasTimeStampInfo', 'execVacuum'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpCollectionHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHelpCollectionHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpCollectionHandler::~QHelpCollectionHandler()': the destructor:
    Python never removes a C++ QHelpCollectionHandler.
  - Qt's 'QMap<QString, QString>
    QHelpCollectionHandler::namespaceToComponent() const': gives a type
    Python has no way to take yet.
  - Qt's 'FileInfoList QHelpCollectionHandler::registeredDocumentations()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  42 of the 75 functions Qt declares: 25 leans on 'QHelpCollectionHandler; 15
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpCollectionHandler is created at the first use, not by
    'QHelpCollectionHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpCollectionHandler.
  - Qt tells when it has removed the C++ QHelpCollectionHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHelpCollectionHandler that has no cute function yet,
    '__init__', 'addCustomFilter', 'contentsForFilter', 'copyCollectionFile',
    'createVersionFilter', 'documentsForField', 'documentsForIdentifier',
    'documentsForKeyword', 'fileData', 'fileExists', 'files',
    'filterAttributeSets', 'findFile', 'indicesForFilter', 'isDBOpened',
    'linksForField', 'namespaceForFile', 'namespaceToComponent',
    'namespacesForFilter', 'openCollectionFile', 'registerDocumentation',
    'registerFileAttributeSets', 'registerFilterAttributes',
    'registerIndexAndNamespaceFilterTables', 'registerIndexTable',
    'registerNamespace', 'registerVirtualFolder', 'registeredDocumentations',
    'removeCustomFilter', 'removeCustomValue', 'scheduleVacuum',
    'setCustomValue', 'unregisterDocumentation', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QHelpCollectionHandler, each a class in
  #  here as in C++.

  class ContentsData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpCollectionHandler::ContentsData: a plain
    Python object standing in front of one C++
    QHelpCollectionHandler::ContentsData.

    C++ hands a QHelpCollectionHandler::ContentsData around as a copy, so
    every C++ QHelpCollectionHandler::ContentsData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QHelpCollectionHandler::ContentsData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpCollectionHandler::ContentsData::~ContentsData()': the
      destructor: Python removes its C++ QHelpCollectionHandler::ContentsData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QHelpCollectionHandler::ContentsData is created at the first
      use, not by 'QHelpCollectionHandler::ContentsData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpCollectionHandler::ContentsData back gives a
      copy the ritual made for Python, in a new cute
      QHelpCollectionHandler::ContentsData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpCollectionHandler::ContentsData'

    #  Qt's '~QHelpCollectionHandler::ContentsData()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QHelpCollectionHandler::ContentsData behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN22QHelpCollectionHandler12ContentsDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class FileInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpCollectionHandler::FileInfo: a plain Python
    object standing in front of one C++ QHelpCollectionHandler::FileInfo.

    C++ hands a QHelpCollectionHandler::FileInfo around as a copy, so every
    C++ QHelpCollectionHandler::FileInfo behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QHelpCollectionHandler::FileInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpCollectionHandler::FileInfo::~FileInfo()': the destructor:
      Python removes its C++ QHelpCollectionHandler::FileInfo by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QHelpCollectionHandler::FileInfo is created at the first use,
      not by 'QHelpCollectionHandler::FileInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpCollectionHandler::FileInfo back gives a copy
      the ritual made for Python, in a new cute
      QHelpCollectionHandler::FileInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpCollectionHandler::FileInfo'

    #  Qt's '~QHelpCollectionHandler::FileInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QHelpCollectionHandler::FileInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QHelpCollectionHandler8FileInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TimeStamp(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHelpCollectionHandler::TimeStamp: a plain Python
    object standing in front of one C++ QHelpCollectionHandler::TimeStamp.

    C++ hands a QHelpCollectionHandler::TimeStamp around as a copy, so every
    C++ QHelpCollectionHandler::TimeStamp behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QHelpCollectionHandler::TimeStamp yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHelpCollectionHandler::TimeStamp::~TimeStamp()': the destructor:
      Python removes its C++ QHelpCollectionHandler::TimeStamp by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QHelpCollectionHandler::TimeStamp is created at the first use,
      not by 'QHelpCollectionHandler::TimeStamp(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHelpCollectionHandler::TimeStamp back gives a copy
      the ritual made for Python, in a new cute
      QHelpCollectionHandler::TimeStamp.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHelpCollectionHandler::TimeStamp'

    #  Qt's '~QHelpCollectionHandler::TimeStamp()'. Naming it makes this a
    #  value class: Python owns every C++ QHelpCollectionHandler::TimeStamp
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QHelpCollectionHandler9TimeStampD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str, str, str)
  def buildQUrl(ns: str, folder: str, relFileName: str, anchor: str) -> QUrl:
    """
    Calls Qt's 'QUrl QHelpCollectionHandler::buildQUrl(const QString &ns,
    const QString &folder, const QString &relFileName, const QString
    &anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#buildQUrl

    Parameters
    ----------

    ns : str
      Passed on as it is: a QString is made of it for the call.

    folder : str
      Passed on as it is: a QString is made of it for the call.

    relFileName : str
      Passed on as it is: a QString is made of it for the call.

    anchor : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHelpCollectionHandler::buildQUrl(const QString &ns, const
    #      QString &folder, const QString &relFileName, const QString
    #      &anchor)
    address = Rituals.call(
        'ritual_ZN22QHelpCollectionHandler9buildQUrlERK7QStringS2_S2_S2_',
        ns, folder, relFileName, anchor,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpCollectionHandler'

  #  A C++ QHelpCollectionHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpCollectionHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpCollectionHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpCollectionHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def collectionFile(self) -> str:
    """
    Calls Qt's 'QString QHelpCollectionHandler::collectionFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#collectionFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpCollectionHandler::collectionFile() const
    return self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler14collectionFileEv',
    )

  def customFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpCollectionHandler::customFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#customFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpCollectionHandler::customFilters() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler13customFiltersEv',
    )
    return QStringList._cuteOwning(address)

  @overload()
  def filterAttributes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpCollectionHandler::filterAttributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#filterAttributes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpCollectionHandler::filterAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler16filterAttributesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def filterAttributes(self, filterName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpCollectionHandler::filterAttributes(const
    QString &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#filterAttributes

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpCollectionHandler::filterAttributes(const QString
    #      &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler16filterAttributesERK7QString',
        filterName,
    )
    return QStringList._cuteOwning(address)

  def filters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpCollectionHandler::filters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#filters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpCollectionHandler::filters() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler7filtersEv',
    )
    return QStringList._cuteOwning(address)

  def availableComponents(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpCollectionHandler::availableComponents()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#availableComponents

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpCollectionHandler::availableComponents() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler19availableComponentsEv',
    )
    return QStringList._cuteOwning(address)

  def availableVersions(self) -> QList[QVersionNumber]:
    """
    Calls Qt's 'QList<QVersionNumber>
    QHelpCollectionHandler::availableVersions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#availableVersions

    Returns
    -------

    QList[QVersionNumber]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVersionNumber> QHelpCollectionHandler::availableVersions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler17availableVersionsEv',
    )
    from ..QtCore import QVersionNumber
    return QList[QVersionNumber]._cuteOwning(address)

  def namespaceToVersion(self) -> QMap[str, QVersionNumber]:
    """
    Calls Qt's 'QMap<QString, QVersionNumber>
    QHelpCollectionHandler::namespaceToVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#namespaceToVersion

    Returns
    -------

    QMap[str, QVersionNumber]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<QString, QVersionNumber>
    #      QHelpCollectionHandler::namespaceToVersion() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler18namespaceToVersionEv',
    )
    from ..QtCore import QVersionNumber
    return QMap[str, QVersionNumber]._cuteOwning(address)

  @overload(str)
  def filterData(self, filterName: str) -> QHelpFilterData:
    """
    Calls Qt's 'QHelpFilterData QHelpCollectionHandler::filterData(const
    QString &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#filterData

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
    #  QHelpFilterData QHelpCollectionHandler::filterData(const QString
    #      &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler10filterDataERK7QString',
        filterName,
    )
    from . import QHelpFilterData
    return QHelpFilterData._cuteOwning(address)

  @overload(str)
  def registeredDocumentation(self, namespaceName: str) -> FileInfo:
    """
    Calls Qt's 'FileInfo
    QHelpCollectionHandler::registeredDocumentation(const QString
    &namespaceName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    FileInfo
      A new cute QHelpCollectionHandler::FileInfo around the copy Qt gave
      back. Python owns it.
    """
    #  FileInfo QHelpCollectionHandler::registeredDocumentation(const QString
    #      &namespaceName) const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler23registeredDocumentationERK7QSt'
        'ring',
        namespaceName,
    )
    return QHelpCollectionHandler.FileInfo._cuteOwning(address)

  @overload(str, QVariant)
  def customValue(self, key: str, defaultValue: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QHelpCollectionHandler::customValue(const QString
    &key, const QVariant &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#customValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHelpCollectionHandler::customValue(const QString &key, const
    #      QVariant &defaultValue) const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler11customValueERK7QStringRK8QVari'
        'ant',
        key, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def namespaceVersion(self, namespaceName: str) -> str:
    """
    Calls Qt's 'QString QHelpCollectionHandler::namespaceVersion(const
    QString &namespaceName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#namespaceVersion

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpCollectionHandler::namespaceVersion(const QString
    #      &namespaceName) const
    return self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler16namespaceVersionERK7QString',
        namespaceName,
    )

  @overload(str)
  def absoluteDocPath(self, fileName: str) -> str:
    """
    Calls Qt's 'QString QHelpCollectionHandler::absoluteDocPath(const QString
    &fileName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#absoluteDocPath

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpCollectionHandler::absoluteDocPath(const QString
    #      &fileName) const
    return self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler15absoluteDocPathERK7QString',
        fileName,
    )

  @overload(TimeStamp)
  def isTimeStampCorrect(self, timeStamp: TimeStamp) -> bool:
    """
    Calls Qt's 'bool QHelpCollectionHandler::isTimeStampCorrect(const
    TimeStamp &timeStamp) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#isTimeStampCorrect

    Parameters
    ----------

    timeStamp : TimeStamp
      Passed on as a value: Qt reads the C++
      QHelpCollectionHandler::TimeStamp, which stays Python's own.
    """
    #  bool QHelpCollectionHandler::isTimeStampCorrect(const TimeStamp
    #      &timeStamp) const
    return self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler18isTimeStampCorrectERKNS_9TimeS'
        'tampE',
        self._valueOf(timeStamp),
    )

  @overload(str)
  def hasTimeStampInfo(self, nameSpace: str) -> bool:
    """
    Calls Qt's 'bool QHelpCollectionHandler::hasTimeStampInfo(const QString
    &nameSpace) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#hasTimeStampInfo

    Parameters
    ----------

    nameSpace : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpCollectionHandler::hasTimeStampInfo(const QString
    #      &nameSpace) const
    return self.uglySide.call(
        'ritual_ZNK22QHelpCollectionHandler16hasTimeStampInfoERK7QString',
        nameSpace,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QHelpFilterData)
  def setFilterData(
      self,
      filterName: str,
      filterData: QHelpFilterData,
  ) -> bool:
    """
    Calls Qt's 'bool QHelpCollectionHandler::setFilterData(const QString
    &filterName, const QHelpFilterData &filterData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#setFilterData

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    filterData : QHelpFilterData
      Passed on as a value: Qt reads the C++ QHelpFilterData, which stays
      Python's own.
    """
    #  bool QHelpCollectionHandler::setFilterData(const QString &filterName,
    #      const QHelpFilterData &filterData)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler13setFilterDataERK7QStringRK15QHe'
        'lpFilterData',
        filterName, self._valueOf(filterData),
    )

  @overload(bool)
  def setReadOnly(self, readOnly: bool) -> None:
    """
    Calls Qt's 'void QHelpCollectionHandler::setReadOnly(bool readOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#setReadOnly

    Parameters
    ----------

    readOnly : bool
      Passed on as it is.
    """
    #  void QHelpCollectionHandler::setReadOnly(bool readOnly)
    self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler11setReadOnlyEb', readOnly,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QHelpCollectionHandler::QHelpCollectionHandler(const QString
    &collectionFile, QObject *parent)': leans on
    'QHelpCollectionHandler::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.__init__' has no cute function yet. Qt's "
        "'QHelpCollectionHandler::QHelpCollectionHandler(const QString "
        "&collectionFile, QObject *parent)': leans on "
        "'QHelpCollectionHandler::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'bool QHelpCollectionHandler::removeFilter(const QString
    &filterName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#removeFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpCollectionHandler::removeFilter(const QString &filterName)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler12removeFilterERK7QString',
        filterName,
    )

  @overload(str, int)
  def registerComponent(self, componentName: str, namespaceId: int) -> int:
    """
    Calls Qt's 'int QHelpCollectionHandler::registerComponent(const QString
    &componentName, int namespaceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#registerComponent

    Parameters
    ----------

    componentName : str
      Passed on as it is: a QString is made of it for the call.

    namespaceId : int
      Passed on as it is.
    """
    #  int QHelpCollectionHandler::registerComponent(const QString
    #      &componentName, int namespaceId)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler17registerComponentERK7QStringi',
        componentName, namespaceId,
    )

  @overload(str, int)
  def registerVersion(self, version: str, namespaceId: int) -> bool:
    """
    Calls Qt's 'bool QHelpCollectionHandler::registerVersion(const QString
    &version, int namespaceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#registerVersion

    Parameters
    ----------

    version : str
      Passed on as it is: a QString is made of it for the call.

    namespaceId : int
      Passed on as it is.
    """
    #  bool QHelpCollectionHandler::registerVersion(const QString &version,
    #      int namespaceId)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler15registerVersionERK7QStringi',
        version, namespaceId,
    )

  @overload(str)
  def error(self, msg: str) -> None:
    """
    Calls Qt's 'void QHelpCollectionHandler::error(const QString &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcollectionhandler.html#error

    Parameters
    ----------

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpCollectionHandler::error(const QString &msg)
    self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler5errorERK7QString', msg,
    )

  @overload(QSqlQuery)
  @overload(NoneType)
  def createTables(self, query: Optional[QSqlQuery]) -> bool:
    """
    Calls Qt's 'bool QHelpCollectionHandler::createTables(QSqlQuery *query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#createTables

    Parameters
    ----------

    query : Optional[QSqlQuery]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHelpCollectionHandler::createTables(QSqlQuery *query)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler12createTablesEP9QSqlQuery',
        self._addressOf(query),
    )

  def closeDB(self) -> None:
    """
    Calls Qt's 'void QHelpCollectionHandler::closeDB()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#closeDB
    """
    #  void QHelpCollectionHandler::closeDB()
    self.uglySide.call('ritual_ZN22QHelpCollectionHandler7closeDBEv')

  @overload(QSqlQuery)
  @overload(NoneType)
  def recreateIndexAndNamespaceFilterTables(
      self,
      query: Optional[QSqlQuery],
  ) -> bool:
    """
    Calls Qt's 'bool
    QHelpCollectionHandler::recreateIndexAndNamespaceFilterTables(QSqlQuery
    *query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html

    Parameters
    ----------

    query : Optional[QSqlQuery]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHelpCollectionHandler::recreateIndexAndNamespaceFilterTables(
    #      QSqlQuery *query)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler37recreateIndexAndNamespaceFilter'
        'TablesEP9QSqlQuery',
        self._addressOf(query),
    )

  @overload(int, int)
  def unregisterIndexTable(self, nsId: int, vfId: int) -> bool:
    """
    Calls Qt's 'bool QHelpCollectionHandler::unregisterIndexTable(int nsId,
    int vfId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#unregisterIndexTable

    Parameters
    ----------

    nsId : int
      Passed on as it is.

    vfId : int
      Passed on as it is.
    """
    #  bool QHelpCollectionHandler::unregisterIndexTable(int nsId, int vfId)
    return self.uglySide.call(
        'ritual_ZN22QHelpCollectionHandler20unregisterIndexTableEii',
        nsId, vfId,
    )

  def execVacuum(self) -> None:
    """
    Calls Qt's 'void QHelpCollectionHandler::execVacuum()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcollectionhandler.html#execVacuum
    """
    #  void QHelpCollectionHandler::execVacuum()
    self.uglySide.call('ritual_ZN22QHelpCollectionHandler10execVacuumEv')

  @staticmethod
  def addCustomFilter(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::addCustomFilter(const QString
    &filterName, const QStringList &attributes)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.addCustomFilter' has no cute function yet. "
        "Qt's 'bool QHelpCollectionHandler::addCustomFilter(const QString "
        "&filterName, const QStringList &attributes)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def contentsForFilter(*__, **_) -> Never:
    """
    - Qt's 'QList<ContentsData>
      QHelpCollectionHandler::contentsForFilter(const QStringList
      &filterAttributes) const': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'prepareFilterQuery'.
    - Qt's 'QList<ContentsData>
      QHelpCollectionHandler::contentsForFilter(const QString &filterName)
      const': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: use of undeclared identifier
      'prepareFilterQuery'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.contentsForFilter' has no cute function "
        "yet. Qt's 'QList<ContentsData> "
        "QHelpCollectionHandler::contentsForFilter(const QStringList "
        "&filterAttributes) const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'prepareFilterQuery'. Qt's "
        "'QList<ContentsData> "
        "QHelpCollectionHandler::contentsForFilter(const QString "
        "&filterName) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'prepareFilterQuery'.")

  @staticmethod
  def copyCollectionFile(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::copyCollectionFile(const QString
    &fileName)': leans on 'QHelpCollectionHandler::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.copyCollectionFile' has no cute function "
        "yet. Qt's 'bool QHelpCollectionHandler::copyCollectionFile(const "
        "QString &fileName)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def createVersionFilter(*__, **_) -> Never:
    """
    Qt's 'void QHelpCollectionHandler::createVersionFilter(const QString
    &version)': leans on 'QHelpCollectionHandler::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.createVersionFilter' has no cute function "
        "yet. Qt's 'void QHelpCollectionHandler::createVersionFilter(const "
        "QString &version)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def documentsForField(*__, **_) -> Never:
    """
    - Qt's 'QList<QHelpLink> QHelpCollectionHandler::documentsForField(const
      QString &fieldName, const QString &fieldValue, const QStringList
      &filterAttributes) const': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'prepareFilterQuery'.
    - Qt's 'QList<QHelpLink> QHelpCollectionHandler::documentsForField(const
      QString &fieldName, const QString &fieldValue, const QString
      &filterName) const': Qt's library has no name for it, and its code in
      Qt's source does not compile apart from its file: use of undeclared
      identifier 'prepareFilterQuery'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.documentsForField' has no cute function "
        "yet. Qt's 'QList<QHelpLink> "
        "QHelpCollectionHandler::documentsForField(const QString "
        "&fieldName, const QString &fieldValue, const QStringList "
        "&filterAttributes) const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'prepareFilterQuery'. Qt's "
        "'QList<QHelpLink> QHelpCollectionHandler::documentsForField(const "
        "QString &fieldName, const QString &fieldValue, const QString "
        "&filterName) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'prepareFilterQuery'.")

  @staticmethod
  def documentsForIdentifier(*__, **_) -> Never:
    """
    - Qt's 'QList<QHelpLink>
      QHelpCollectionHandler::documentsForIdentifier(const QString &id, const
      QString &filterName) const': leans on
      'QHelpCollectionHandler::documentsForField(QString const&, QString
      const&, QString const&) const', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'QList<QHelpLink>
      QHelpCollectionHandler::documentsForIdentifier(const QString &id, const
      QStringList &filterAttributes) const': leans on
      'QHelpCollectionHandler::documentsForField(QString const&, QString
      const&, QList<QString> const&) const', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.documentsForIdentifier' has no cute "
        "function yet. Qt's 'QList<QHelpLink> "
        "QHelpCollectionHandler::documentsForIdentifier(const QString &id, "
        "const QString &filterName) const': leans on "
        "'QHelpCollectionHandler::documentsForField(QString const&, QString "
        "const&, QString const&) const', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken. "
        "Qt's 'QList<QHelpLink> "
        "QHelpCollectionHandler::documentsForIdentifier(const QString &id, "
        "const QStringList &filterAttributes) const': leans on "
        "'QHelpCollectionHandler::documentsForField(QString const&, QString "
        "const&, QList<QString> const&) const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def documentsForKeyword(*__, **_) -> Never:
    """
    - Qt's 'QList<QHelpLink>
      QHelpCollectionHandler::documentsForKeyword(const QString &keyword,
      const QString &filterName) const': leans on
      'QHelpCollectionHandler::documentsForField(QString const&, QString
      const&, QString const&) const', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'QList<QHelpLink>
      QHelpCollectionHandler::documentsForKeyword(const QString &keyword,
      const QStringList &filterAttributes) const': leans on
      'QHelpCollectionHandler::documentsForField(QString const&, QString
      const&, QList<QString> const&) const', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.documentsForKeyword' has no cute function "
        "yet. Qt's 'QList<QHelpLink> "
        "QHelpCollectionHandler::documentsForKeyword(const QString "
        "&keyword, const QString &filterName) const': leans on "
        "'QHelpCollectionHandler::documentsForField(QString const&, QString "
        "const&, QString const&) const', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken. "
        "Qt's 'QList<QHelpLink> "
        "QHelpCollectionHandler::documentsForKeyword(const QString "
        "&keyword, const QStringList &filterAttributes) const': leans on "
        "'QHelpCollectionHandler::documentsForField(QString const&, QString "
        "const&, QList<QString> const&) const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def fileData(*__, **_) -> Never:
    """
    Qt's 'QByteArray QHelpCollectionHandler::fileData(const QUrl &url)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'extractFileInfo'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.fileData' has no cute function yet. Qt's "
        "'QByteArray QHelpCollectionHandler::fileData(const QUrl &url) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'extractFileInfo'.")

  @staticmethod
  def fileExists(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::fileExists(const QUrl &url) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'extractFileInfo'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.fileExists' has no cute function yet. Qt's "
        "'bool QHelpCollectionHandler::fileExists(const QUrl &url) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'extractFileInfo'.")

  @staticmethod
  def files(*__, **_) -> Never:
    """
    - Qt's 'QStringList QHelpCollectionHandler::files(const QString
      &namespaceName, const QString &filterName, const QString
      &extensionFilter) const': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: use of undeclared
      identifier 'prepareFilterQuery'.
    - Qt's 'QStringList QHelpCollectionHandler::files(const QString
      &namespaceName, const QStringList &filterAttributes, const QString
      &extensionFilter) const': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: no matching
      function for call to 'prepareFilterQuery'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.files' has no cute function yet. Qt's "
        "'QStringList QHelpCollectionHandler::files(const QString "
        "&namespaceName, const QString &filterName, const QString "
        "&extensionFilter) const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'prepareFilterQuery'. Qt's 'QStringList "
        "QHelpCollectionHandler::files(const QString &namespaceName, const "
        "QStringList &filterAttributes, const QString &extensionFilter) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'prepareFilterQuery'.")

  @staticmethod
  def filterAttributeSets(*__, **_) -> Never:
    """
    Qt's 'QList<QStringList>
    QHelpCollectionHandler::filterAttributeSets(const QString &namespaceName)
    const': leans on 'QHelpCollectionHandler::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.filterAttributeSets' has no cute function "
        "yet. Qt's 'QList<QStringList> "
        "QHelpCollectionHandler::filterAttributeSets(const QString "
        "&namespaceName) const': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def findFile(*__, **_) -> Never:
    """
    - Qt's 'QUrl QHelpCollectionHandler::findFile(const QUrl &url, const
      QStringList &filterAttributes) const': leans on
      'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    - Qt's 'QUrl QHelpCollectionHandler::findFile(const QUrl &url, const
      QString &filterName) const': leans on
      'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.findFile' has no cute function yet. Qt's "
        "'QUrl QHelpCollectionHandler::findFile(const QUrl &url, const "
        "QStringList &filterAttributes) const': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'QUrl QHelpCollectionHandler::findFile(const QUrl "
        "&url, const QString &filterName) const': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def indicesForFilter(*__, **_) -> Never:
    """
    - Qt's 'QStringList QHelpCollectionHandler::indicesForFilter(const
      QStringList &filterAttributes) const': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file: use
      of undeclared identifier 'prepareFilterQuery'.
    - Qt's 'QStringList QHelpCollectionHandler::indicesForFilter(const
      QString &filterName) const': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'prepareFilterQuery'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.indicesForFilter' has no cute function "
        "yet. Qt's 'QStringList "
        "QHelpCollectionHandler::indicesForFilter(const QStringList "
        "&filterAttributes) const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'prepareFilterQuery'. Qt's 'QStringList "
        "QHelpCollectionHandler::indicesForFilter(const QString "
        "&filterName) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'prepareFilterQuery'.")

  @staticmethod
  def isDBOpened(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::isDBOpened() const': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.isDBOpened' has no cute function yet. Qt's "
        "'bool QHelpCollectionHandler::isDBOpened() const': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def linksForField(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QString, QUrl>
    QHelpCollectionHandler::linksForField(const QString &fieldName, const
    QString &fieldValue, const QString &filterName) const': leans on
    'QHelpCollectionHandler::documentsForField(QString const&, QString
    const&, QString const&) const', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.linksForField' has no cute function yet. "
        "Qt's 'QMultiMap<QString, QUrl> "
        "QHelpCollectionHandler::linksForField(const QString &fieldName, "
        "const QString &fieldValue, const QString &filterName) const': "
        "leans on 'QHelpCollectionHandler::documentsForField(QString "
        "const&, QString const&, QString const&) const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def namespaceForFile(*__, **_) -> Never:
    """
    - Qt's 'QString QHelpCollectionHandler::namespaceForFile(const QUrl &url,
      const QStringList &filterAttributes) const': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'prepareFilterQuery'.
    - Qt's 'QString QHelpCollectionHandler::namespaceForFile(const QUrl &url,
      const QString &filterName) const': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'extractFileInfo'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.namespaceForFile' has no cute function "
        "yet. Qt's 'QString QHelpCollectionHandler::namespaceForFile(const "
        "QUrl &url, const QStringList &filterAttributes) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'prepareFilterQuery'. Qt's 'QString "
        "QHelpCollectionHandler::namespaceForFile(const QUrl &url, const "
        "QString &filterName) const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'extractFileInfo'.")

  @staticmethod
  def namespaceToComponent(*__, **_) -> Never:
    """
    Qt's 'QMap<QString, QString>
    QHelpCollectionHandler::namespaceToComponent() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.namespaceToComponent' has no cute function "
        "yet. Qt's 'QMap<QString, QString> "
        "QHelpCollectionHandler::namespaceToComponent() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def namespacesForFilter(*__, **_) -> Never:
    """
    Qt's 'QStringList QHelpCollectionHandler::namespacesForFilter(const
    QString &filterName) const': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'prepareFilterQuery'.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.namespacesForFilter' has no cute function "
        "yet. Qt's 'QStringList "
        "QHelpCollectionHandler::namespacesForFilter(const QString "
        "&filterName) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'prepareFilterQuery'.")

  @staticmethod
  def openCollectionFile(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::openCollectionFile()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'transaction'; did you mean
    'QSqlDatabase::transaction'?.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.openCollectionFile' has no cute function "
        "yet. Qt's 'bool QHelpCollectionHandler::openCollectionFile()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'transaction'; did you mean 'QSqlDatabase::transaction'?.")

  @staticmethod
  def registerDocumentation(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::registerDocumentation(const QString
    &fileName)': leans on 'QHelpCollectionHandler::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerDocumentation' has no cute "
        "function yet. Qt's 'bool "
        "QHelpCollectionHandler::registerDocumentation(const QString "
        "&fileName)': leans on 'QHelpCollectionHandler::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def registerFileAttributeSets(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::registerFileAttributeSets(const
    QList<QStringList> &attributeSets, int nsId)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerFileAttributeSets' has no cute "
        "function yet. Qt's 'bool "
        "QHelpCollectionHandler::registerFileAttributeSets(const "
        "QList<QStringList> &attributeSets, int nsId)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def registerFilterAttributes(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::registerFilterAttributes(const
    QList<QStringList> &attributeSets, int nsId)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerFilterAttributes' has no cute "
        "function yet. Qt's 'bool "
        "QHelpCollectionHandler::registerFilterAttributes(const "
        "QList<QStringList> &attributeSets, int nsId)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def registerIndexAndNamespaceFilterTables(*__, **_) -> Never:
    """
    Qt's 'bool
    QHelpCollectionHandler::registerIndexAndNamespaceFilterTables(const
    QString &nameSpace, bool createDefaultVersionFilter)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerIndexAndNamespaceFilterTables' has "
        "no cute function yet. Qt's 'bool "
        "QHelpCollectionHandler::registerIndexAndNamespaceFilterTables(const"
        " QString &nameSpace, bool createDefaultVersionFilter)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def registerIndexTable(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::registerIndexTable(const
    QHelpDBReader::IndexTable &indexTable, int nsId, int vfId, const QString
    &fileName)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'Transaction'; did you mean 'QSqlDatabase::transaction'?.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerIndexTable' has no cute function "
        "yet. Qt's 'bool QHelpCollectionHandler::registerIndexTable(const "
        "QHelpDBReader::IndexTable &indexTable, int nsId, int vfId, const "
        "QString &fileName)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'Transaction'; did you mean "
        "'QSqlDatabase::transaction'?.")

  @staticmethod
  def registerNamespace(*__, **_) -> Never:
    """
    Qt's 'int QHelpCollectionHandler::registerNamespace(const QString
    &nspace, const QString &fileName)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerNamespace' has no cute function "
        "yet. Qt's 'int QHelpCollectionHandler::registerNamespace(const "
        "QString &nspace, const QString &fileName)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def registerVirtualFolder(*__, **_) -> Never:
    """
    Qt's 'int QHelpCollectionHandler::registerVirtualFolder(const QString
    &folderName, int namespaceId)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registerVirtualFolder' has no cute "
        "function yet. Qt's 'int "
        "QHelpCollectionHandler::registerVirtualFolder(const QString "
        "&folderName, int namespaceId)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def registeredDocumentations(*__, **_) -> Never:
    """
    Qt's 'FileInfoList QHelpCollectionHandler::registeredDocumentations()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.registeredDocumentations' has no cute "
        "function yet. Qt's 'FileInfoList "
        "QHelpCollectionHandler::registeredDocumentations() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def removeCustomFilter(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::removeCustomFilter(const QString
    &filterName)': leans on 'QHelpCollectionHandler::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.removeCustomFilter' has no cute function "
        "yet. Qt's 'bool QHelpCollectionHandler::removeCustomFilter(const "
        "QString &filterName)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def removeCustomValue(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::removeCustomValue(const QString
    &key)': leans on 'QHelpCollectionHandler::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.removeCustomValue' has no cute function "
        "yet. Qt's 'bool QHelpCollectionHandler::removeCustomValue(const "
        "QString &key)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def scheduleVacuum(*__, **_) -> Never:
    """
    Qt's 'void QHelpCollectionHandler::scheduleVacuum()': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.scheduleVacuum' has no cute function yet. "
        "Qt's 'void QHelpCollectionHandler::scheduleVacuum()': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setCustomValue(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::setCustomValue(const QString &key,
    const QVariant &value)': leans on
    'QHelpCollectionHandler::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.setCustomValue' has no cute function yet. "
        "Qt's 'bool QHelpCollectionHandler::setCustomValue(const QString "
        "&key, const QVariant &value)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def unregisterDocumentation(*__, **_) -> Never:
    """
    Qt's 'bool QHelpCollectionHandler::unregisterDocumentation(const QString
    &namespaceName)': leans on 'QHelpCollectionHandler::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QHelpCollectionHandler.unregisterDocumentation' has no cute "
        "function yet. Qt's 'bool "
        "QHelpCollectionHandler::unregisterDocumentation(const QString "
        "&namespaceName)': leans on "
        "'QHelpCollectionHandler::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
