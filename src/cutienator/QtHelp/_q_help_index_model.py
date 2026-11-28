"""
QHelpIndexModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpindexwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringListModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QHelpEngineCore
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpEngineCore = WAIT['QHelpEngineCore']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpIndexModel(QStringListModel):
  """
  The cute side of Qt's QHelpIndexModel: a plain Python object standing in
  front of one C++ QHelpIndexModel.

  It is built on the cute 'QStringListModel', as Qt's QHelpIndexModel is
  built on Qt's QStringListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpIndexModel that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr',
  'createIndexForCurrentFilter', 'createIndex', 'filter', 'isCreatingIndex',
  'helpEngine', 'indexCreationStarted', 'indexCreated', 'insertIndices'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpIndexModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpIndexModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpIndexModel::~QHelpIndexModel()': the destructor: Python never
    removes a C++ QHelpIndexModel.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpIndexModel is created at the first use, not by
    'QHelpIndexModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpIndexModel.
  - Qt tells when it has removed the C++ QHelpIndexModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QHelpIndexModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#tr

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
    #  QString QHelpIndexModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QHelpIndexModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpIndexModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpIndexModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpIndexModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QHelpIndexModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isCreatingIndex(self) -> bool:
    """
    Calls Qt's 'bool QHelpIndexModel::isCreatingIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexmodel.html#isCreatingIndex
    """
    #  bool QHelpIndexModel::isCreatingIndex() const
    return self.uglySide.call(
        'ritual_ZNK15QHelpIndexModel15isCreatingIndexEv',
    )

  def helpEngine(self) -> Optional[QHelpEngineCore]:
    """
    Calls Qt's 'QHelpEngineCore *QHelpIndexModel::helpEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#helpEngine

    Returns
    -------

    Optional[QHelpEngineCore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpEngineCore *QHelpIndexModel::helpEngine() const
    address = self.uglySide.call('ritual_ZNK15QHelpIndexModel10helpEngineEv')
    from . import QHelpEngineCore
    return QHelpEngineCore._cuteAt(address)

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

  @overload(QHelpEngineCore)
  @overload(NoneType)
  def __init__(self, helpEngine: Optional[QHelpEngineCore]) -> None:
    """
    Notes what was given, for Qt's
    'QHelpIndexModel::QHelpIndexModel(QHelpEngineCore *helpEngine)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexmodel.html#QHelpIndexModel

    Parameters
    ----------

    helpEngine : Optional[QHelpEngineCore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHelpIndexModel::QHelpIndexModel(QHelpEngineCore *helpEngine)
    self._noteCreation(QHelpIndexModel, lambda: Rituals.call(
        'ritual_ZN15QHelpIndexModelC1EP15QHelpEngineCore',
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

  def createIndexForCurrentFilter(self) -> None:
    """
    Calls Qt's 'void QHelpIndexModel::createIndexForCurrentFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexmodel.html#createIndexForCurrentFilter
    """
    #  void QHelpIndexModel::createIndexForCurrentFilter()
    self.uglySide.call(
        'ritual_ZN15QHelpIndexModel27createIndexForCurrentFilterEv',
    )

  @overload(str)
  def createIndex(self, customFilterName: str) -> None:
    """
    Calls Qt's 'void QHelpIndexModel::createIndex(const QString
    &customFilterName)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#createIndex

    Parameters
    ----------

    customFilterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpIndexModel::createIndex(const QString &customFilterName)
    self.uglySide.call(
        'ritual_ZN15QHelpIndexModel11createIndexERK7QString',
        customFilterName,
    )

  @overload(str)
  @overload(str, str)
  def filter(self, filter: str, wildcard: str = '') -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHelpIndexModel::filter(const QString &filter,
    const QString &wildcard)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#filter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.

    wildcard : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QHelpIndexModel::filter(const QString &filter, const
    #      QString &wildcard)
    address = self.uglySide.call(
        'ritual_ZN15QHelpIndexModel6filterERK7QStringS2_', filter, wildcard,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def indexCreationStarted(self) -> None:
    """
    Calls Qt's 'void QHelpIndexModel::indexCreationStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpindexmodel.html#indexCreationStarted
    """
    #  void QHelpIndexModel::indexCreationStarted()
    self.uglySide.call('ritual_ZN15QHelpIndexModel20indexCreationStartedEv')

  def indexCreated(self) -> None:
    """
    Calls Qt's 'void QHelpIndexModel::indexCreated()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#indexCreated
    """
    #  void QHelpIndexModel::indexCreated()
    self.uglySide.call('ritual_ZN15QHelpIndexModel12indexCreatedEv')

  def insertIndices(self) -> None:
    """
    Calls Qt's 'void QHelpIndexModel::insertIndices()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpindexmodel.html#insertIndices
    """
    #  void QHelpIndexModel::insertIndices()
    self.uglySide.call('ritual_ZN15QHelpIndexModel13insertIndicesEv')
