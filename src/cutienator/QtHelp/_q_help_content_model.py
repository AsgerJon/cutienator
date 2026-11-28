"""
QHelpContentModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpcontentwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractItemModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
  from . import QHelpContentItem, QHelpEngineCore
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpEngineCore = WAIT['QHelpEngineCore']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpContentModel(QAbstractItemModel):
  """
  The cute side of Qt's QHelpContentModel: a plain Python object standing in
  front of one C++ QHelpContentModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QHelpContentModel is
  built on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpContentModel that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr',
  'createContentsForCurrentFilter', 'createContents', 'contentItemAt',
  'data', 'index', 'parent', 'rowCount', 'columnCount', 'isCreatingContents',
  'contentsCreationStarted', 'contentsCreated', 'insertContents'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpContentModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpContentModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpContentModel::~QHelpContentModel()': the destructor: Python
    never removes a C++ QHelpContentModel.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpContentModel is created at the first use, not by
    'QHelpContentModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpContentModel.
  - Qt tells when it has removed the C++ QHelpContentModel. Every call on the
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
    Calls Qt's 'QString QHelpContentModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#tr

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
    #  QString QHelpContentModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QHelpContentModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpContentModel'

  #  A C++ QHelpContentModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpContentModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpContentModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpContentModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpContentModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def contentItemAt(self, index: QModelIndex) -> Optional[QHelpContentItem]:
    """
    Calls Qt's 'QHelpContentItem *QHelpContentModel::contentItemAt(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#contentItemAt

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QHelpContentItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpContentItem *QHelpContentModel::contentItemAt(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpContentModel13contentItemAtERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QHelpContentItem
    return QHelpContentItem._cuteAt(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QHelpContentModel::data(const QModelIndex &index,
    int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHelpContentModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK17QHelpContentModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHelpContentModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHelpContentModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QHelpContentModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK17QHelpContentModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHelpContentModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QHelpContentModel::parent(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#parent

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QHelpContentModel::parent(const QModelIndex &index) const
    ritual = 'ritual_ZNK17QHelpContentModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHelpContentModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QHelpContentModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QHelpContentModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK17QHelpContentModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHelpContentModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QHelpContentModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentmodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QHelpContentModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK17QHelpContentModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QHelpContentModel11columnCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  def isCreatingContents(self) -> bool:
    """
    Calls Qt's 'bool QHelpContentModel::isCreatingContents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#isCreatingContents
    """
    #  bool QHelpContentModel::isCreatingContents() const
    return self.uglySide.call(
        'ritual_ZNK17QHelpContentModel18isCreatingContentsEv',
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

  @overload(QHelpEngineCore)
  @overload(NoneType)
  def __init__(self, helpEngine: Optional[QHelpEngineCore]) -> None:
    """
    Notes what was given, for Qt's
    'QHelpContentModel::QHelpContentModel(QHelpEngineCore *helpEngine)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#QHelpContentModel

    Parameters
    ----------

    helpEngine : Optional[QHelpEngineCore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHelpContentModel::QHelpContentModel(QHelpEngineCore *helpEngine)
    self._noteCreation(QHelpContentModel, lambda: Rituals.call(
        'ritual_ZN17QHelpContentModelC1EP15QHelpEngineCore',
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

  def createContentsForCurrentFilter(self) -> None:
    """
    Calls Qt's 'void QHelpContentModel::createContentsForCurrentFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html
    """
    #  void QHelpContentModel::createContentsForCurrentFilter()
    self.uglySide.call(
        'ritual_ZN17QHelpContentModel30createContentsForCurrentFilterEv',
    )

  @overload(str)
  def createContents(self, customFilterName: str) -> None:
    """
    Calls Qt's 'void QHelpContentModel::createContents(const QString
    &customFilterName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#createContents

    Parameters
    ----------

    customFilterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpContentModel::createContents(const QString
    #      &customFilterName)
    self.uglySide.call(
        'ritual_ZN17QHelpContentModel14createContentsERK7QString',
        customFilterName,
    )

  def contentsCreationStarted(self) -> None:
    """
    Calls Qt's 'void QHelpContentModel::contentsCreationStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#contentsCreationStarted
    """
    #  void QHelpContentModel::contentsCreationStarted()
    self.uglySide.call(
        'ritual_ZN17QHelpContentModel23contentsCreationStartedEv',
    )

  def contentsCreated(self) -> None:
    """
    Calls Qt's 'void QHelpContentModel::contentsCreated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#contentsCreated
    """
    #  void QHelpContentModel::contentsCreated()
    self.uglySide.call('ritual_ZN17QHelpContentModel15contentsCreatedEv')

  def insertContents(self) -> None:
    """
    Calls Qt's 'void QHelpContentModel::insertContents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentmodel.html#insertContents
    """
    #  void QHelpContentModel::insertContents()
    self.uglySide.call('ritual_ZN17QHelpContentModel14insertContentsEv')
