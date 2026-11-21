"""
QItemSelectionModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QItemSelectionModelSelectionFlag, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractItemModel, QItemSelection, QMetaObject, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemSelectionModel(QObject):
  """
  The cute side of Qt's QItemSelectionModel: a plain Python object standing
  in front of one C++ QItemSelectionModel.

  It is built on the cute 'QObject', as Qt's QItemSelectionModel is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QItemSelectionModel that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr',
  'currentIndex', 'isSelected', 'isRowSelected', 'isColumnSelected',
  'rowIntersectsSelection', 'columnIntersectsSelection', 'hasSelection',
  'selection', 'model', 'setModel', 'setCurrentIndex', 'select', 'clear',
  'reset', 'clearSelection', 'clearCurrentIndex'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QItemSelectionModel::~QItemSelectionModel()': the destructor:
    Python never removes a C++ QItemSelectionModel.
  - Qt's 'QAbstractItemModel *QItemSelectionModel::model()': takes in Python
    what 'const QAbstractItemModel *QItemSelectionModel::model() const'
    takes.

  What has no ritual
  ------------------

  19 of the 42 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 5 a signal; 3 private; 2 protected; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QItemSelectionModel is created at the first use, not by
    'QItemSelectionModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemSelectionModel.
  - Qt tells when it has removed the C++ QItemSelectionModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QItemSelectionModel, and the names Qt has for
  #  the combinations of its flags enums.
  SelectionFlag = QItemSelectionModelSelectionFlag
  SelectionFlags = QItemSelectionModelSelectionFlag

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
    Calls Qt's 'QString QItemSelectionModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#tr

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
    #  QString QItemSelectionModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QItemSelectionModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemSelectionModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QItemSelectionModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QItemSelectionModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QItemSelectionModel::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#currentIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QItemSelectionModel::currentIndex() const
    address = self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel12currentIndexEv',
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def isSelected(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QItemSelectionModel::isSelected(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#isSelected

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QItemSelectionModel::isSelected(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel10isSelectedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def isRowSelected(
      self,
      row: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QItemSelectionModel::isRowSelected(int row, const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#isRowSelected

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QItemSelectionModel::isRowSelected(int row, const QModelIndex
    #      &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel13isRowSelectedEiRK11QModelIndex',
        row, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def isColumnSelected(
      self,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QItemSelectionModel::isColumnSelected(int column, const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#isColumnSelected

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QItemSelectionModel::isColumnSelected(int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel16isColumnSelectedEiRK11QModelIndex',
        column, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def rowIntersectsSelection(
      self,
      row: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QItemSelectionModel::rowIntersectsSelection(int row,
    const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#rowIntersectsSelection

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QItemSelectionModel::rowIntersectsSelection(int row, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel22rowIntersectsSelectionEiRK11QMode'
        'lIndex',
        row, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def columnIntersectsSelection(
      self,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QItemSelectionModel::columnIntersectsSelection(int
    column, const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#columnIntersectsSelection

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QItemSelectionModel::columnIntersectsSelection(int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel25columnIntersectsSelectionEiRK11QM'
        'odelIndex',
        column, self._valueOf(parent),
    )

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QItemSelectionModel::hasSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#hasSelection
    """
    #  bool QItemSelectionModel::hasSelection() const
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel12hasSelectionEv',
    )

  def selection(self) -> QItemSelection:
    """
    Calls Qt's 'const QItemSelection QItemSelectionModel::selection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#selection

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  const QItemSelection QItemSelectionModel::selection() const
    address = self.uglySide.call(
        'ritual_ZNK19QItemSelectionModel9selectionEv',
    )
    from . import QItemSelection
    return QItemSelection._cuteOwning(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel *QItemSelectionModel::model()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QItemSelectionModel::model() const
    address = self.uglySide.call('ritual_ZNK19QItemSelectionModel5modelEv')
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::setModel(QAbstractItemModel
    *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemSelectionModel::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN19QItemSelectionModel8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QModelIndex, SelectionFlags)
  def setCurrentIndex(
      self,
      index: QModelIndex,
      command: SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::setCurrentIndex(const QModelIndex
    &index, QItemSelectionModel::SelectionFlags command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#setCurrentIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    command : SelectionFlags
      Passed on as its number.
    """
    #  void QItemSelectionModel::setCurrentIndex(const QModelIndex &index,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN19QItemSelectionModel15setCurrentIndexERK11QModelIndex6QF'
        'lagsINS_13SelectionFlagEE',
        self._valueOf(index), command.value,
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

  @overload()
  @overload(QAbstractItemModel)
  @overload(NoneType)
  def __init__(self, model: Optional[QAbstractItemModel] = None) -> None:
    """
    Notes what was given, for Qt's
    'QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#QItemSelectionModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model)
    self._noteCreation(QItemSelectionModel, lambda: Rituals.call(
        'ritual_ZN19QItemSelectionModelC1EP18QAbstractItemModel',
        self._addressOf(model),
    ))

  @overload(QAbstractItemModel, QObject)
  @overload(QAbstractItemModel, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      model: Optional[QAbstractItemModel],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#QItemSelectionModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model,
    #      QObject *parent)
    self._noteCreation(QItemSelectionModel, lambda: Rituals.call(
        'ritual_ZN19QItemSelectionModelC1EP18QAbstractItemModelP7QObject',
        self._addressOf(model), self._addressOf(parent),
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

  @overload(QModelIndex, SelectionFlags)
  def select(self, index: QModelIndex, command: SelectionFlags) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::select(const QModelIndex &index,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#select

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    command : SelectionFlags
      Passed on as its number.
    """
    #  void QItemSelectionModel::select(const QModelIndex &index,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN19QItemSelectionModel6selectERK11QModelIndex6QFlagsINS_13'
        'SelectionFlagEE',
        self._valueOf(index), command.value,
    )

  @overload(QItemSelection, SelectionFlags)
  def select(
      self,
      selection: QItemSelection,
      command: SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::select(const QItemSelection
    &selection, QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#select

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    command : SelectionFlags
      Passed on as its number.
    """
    #  void QItemSelectionModel::select(const QItemSelection &selection,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN19QItemSelectionModel6selectERK14QItemSelection6QFlagsINS'
        '_13SelectionFlagEE',
        self._valueOf(selection), command.value,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#clear
    """
    #  void QItemSelectionModel::clear()
    self.uglySide.call('ritual_ZN19QItemSelectionModel5clearEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionmodel.html#reset
    """
    #  void QItemSelectionModel::reset()
    self.uglySide.call('ritual_ZN19QItemSelectionModel5resetEv')

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#clearSelection
    """
    #  void QItemSelectionModel::clearSelection()
    self.uglySide.call('ritual_ZN19QItemSelectionModel14clearSelectionEv')

  def clearCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QItemSelectionModel::clearCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionmodel.html#clearCurrentIndex
    """
    #  void QItemSelectionModel::clearCurrentIndex()
    self.uglySide.call('ritual_ZN19QItemSelectionModel17clearCurrentIndexEv')
