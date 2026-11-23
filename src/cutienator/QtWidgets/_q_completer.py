"""
QCompleter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcompleter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QEvent, QMetaObject, QModelIndex
  from ..QtCore import QRect
  from . import QAbstractItemView, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QAbstractItemView = WAIT['QAbstractItemView']
  QEvent = WAIT['QEvent']
  QModelIndex = WAIT['QModelIndex']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCompleter(QObject):
  """
  The cute side of Qt's QCompleter: a plain Python object standing in front
  of one C++ QCompleter.

  It is built on the cute 'QObject', as Qt's QCompleter is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCompleter that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'setWidget', 'widget',
  'setModel', 'model', 'setCompletionMode', 'completionMode',
  'setFilterMode', 'filterMode', 'popup', 'setPopup', 'setCaseSensitivity',
  'caseSensitivity', 'setModelSorting', 'modelSorting',
  'setCompletionColumn', 'completionColumn', 'setCompletionRole',
  'completionRole', 'wrapAround', 'maxVisibleItems', 'setMaxVisibleItems',
  'completionCount', 'setCurrentRow', 'currentRow', 'currentIndex',
  'currentCompletion', 'completionModel', 'completionPrefix',
  'setCompletionPrefix', 'complete', 'setWrapAround', 'pathFromIndex',
  'splitPath', 'eventFilter', 'event'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCompleter::~QCompleter()': the destructor: Python never removes a
    C++ QCompleter.

  What has no ritual
  ------------------

  12 of the 53 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 4 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QCompleter is created at the first use, not by 'QCompleter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCompleter.
  - Qt tells when it has removed the C++ QCompleter. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QCompleter, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CompletionMode(CuteNum):
    """
    The enum 'QCompleter::CompletionMode' of Qt, with the 3 names Qt gives in
    it.
    """

    PopupCompletion = Kee[int](0)
    UnfilteredPopupCompletion = Kee[int](1)
    InlineCompletion = Kee[int](2)

  class ModelSorting(CuteNum):
    """
    The enum 'QCompleter::ModelSorting' of Qt, with the 3 names Qt gives in
    it.
    """

    UnsortedModel = Kee[int](0)
    CaseSensitivelySortedModel = Kee[int](1)
    CaseInsensitivelySortedModel = Kee[int](2)

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
    Calls Qt's 'QString QCompleter::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#tr

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
    #  QString QCompleter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QCompleter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCompleter'

  #  A C++ QCompleter Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCompleter'

  #  The functions Qt calls itself that QCompleter is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'splitPath': (
          'QStringList QCompleter::splitPath(const QString &) const',
      ),
  }

  #  The functions Qt calls itself that QCompleter is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'pathFromIndex': (
          ('_ZNK10QCompleter13pathFromIndexERK11QModelIndex',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCompleter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCompleter::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QCompleter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QCompleter::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QCompleter::widget() const
    address = self.uglySide.call('ritual_ZNK10QCompleter6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QCompleter::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QCompleter::model() const
    address = self.uglySide.call('ritual_ZNK10QCompleter5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def completionMode(self) -> CompletionMode:
    """
    Calls Qt's 'CompletionMode QCompleter::completionMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#completionMode

    Returns
    -------

    CompletionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompletionMode(number)'
      gives.
    """
    #  CompletionMode QCompleter::completionMode() const
    return QCompleter.CompletionMode(self.uglySide.call(
        'ritual_ZNK10QCompleter14completionModeEv',
    ))

  def filterMode(self) -> Qt.MatchFlags:
    """
    Calls Qt's 'Qt::MatchFlags QCompleter::filterMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#filterMode

    Returns
    -------

    Qt.MatchFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::MatchFlags QCompleter::filterMode() const
    return Qt.MatchFlags(self.uglySide.call(
        'ritual_ZNK10QCompleter10filterModeEv',
    ))

  def popup(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QCompleter::popup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#popup

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QCompleter::popup() const
    address = self.uglySide.call('ritual_ZNK10QCompleter5popupEv')
    from . import QAbstractItemView
    return QAbstractItemView._cuteAt(address)

  def caseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity QCompleter::caseSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#caseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QCompleter::caseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK10QCompleter15caseSensitivityEv',
    ))

  def modelSorting(self) -> ModelSorting:
    """
    Calls Qt's 'ModelSorting QCompleter::modelSorting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#modelSorting

    Returns
    -------

    ModelSorting
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ModelSorting(number)'
      gives.
    """
    #  ModelSorting QCompleter::modelSorting() const
    return QCompleter.ModelSorting(self.uglySide.call(
        'ritual_ZNK10QCompleter12modelSortingEv',
    ))

  def completionColumn(self) -> int:
    """
    Calls Qt's 'int QCompleter::completionColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#completionColumn
    """
    #  int QCompleter::completionColumn() const
    return self.uglySide.call('ritual_ZNK10QCompleter16completionColumnEv')

  def completionRole(self) -> int:
    """
    Calls Qt's 'int QCompleter::completionRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#completionRole
    """
    #  int QCompleter::completionRole() const
    return self.uglySide.call('ritual_ZNK10QCompleter14completionRoleEv')

  def wrapAround(self) -> bool:
    """
    Calls Qt's 'bool QCompleter::wrapAround() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#wrapAround
    """
    #  bool QCompleter::wrapAround() const
    return self.uglySide.call('ritual_ZNK10QCompleter10wrapAroundEv')

  def maxVisibleItems(self) -> int:
    """
    Calls Qt's 'int QCompleter::maxVisibleItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#maxVisibleItems
    """
    #  int QCompleter::maxVisibleItems() const
    return self.uglySide.call('ritual_ZNK10QCompleter15maxVisibleItemsEv')

  def completionCount(self) -> int:
    """
    Calls Qt's 'int QCompleter::completionCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#completionCount
    """
    #  int QCompleter::completionCount() const
    return self.uglySide.call('ritual_ZNK10QCompleter15completionCountEv')

  def currentRow(self) -> int:
    """
    Calls Qt's 'int QCompleter::currentRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#currentRow
    """
    #  int QCompleter::currentRow() const
    return self.uglySide.call('ritual_ZNK10QCompleter10currentRowEv')

  def currentIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCompleter::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#currentIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QCompleter::currentIndex() const
    address = self.uglySide.call('ritual_ZNK10QCompleter12currentIndexEv')
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def currentCompletion(self) -> str:
    """
    Calls Qt's 'QString QCompleter::currentCompletion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#currentCompletion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCompleter::currentCompletion() const
    return self.uglySide.call('ritual_ZNK10QCompleter17currentCompletionEv')

  def completionModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QCompleter::completionModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#completionModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QCompleter::completionModel() const
    address = self.uglySide.call('ritual_ZNK10QCompleter15completionModelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def completionPrefix(self) -> str:
    """
    Calls Qt's 'QString QCompleter::completionPrefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#completionPrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCompleter::completionPrefix() const
    return self.uglySide.call('ritual_ZNK10QCompleter16completionPrefixEv')

  @overload(QModelIndex)
  def pathFromIndex(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QCompleter::pathFromIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#pathFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCompleter::pathFromIndex(const QModelIndex &index) const
    ritual = 'ritual_ZNK10QCompleter13pathFromIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QCompleter13pathFromIndexERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(str)
  def splitPath(self, path: str) -> QStringList:
    """
    Calls Qt's 'QStringList QCompleter::splitPath(const QString &path)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#splitPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCompleter::splitPath(const QString &path) const
    address = self.uglySide.call(
        'ritual_ZNK10QCompleter9splitPathERK7QString', path,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QCompleter::setWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCompleter::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN10QCompleter9setWidgetEP7QWidget', self._addressOf(widget),
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, c: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QCompleter::setModel(QAbstractItemModel *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setModel

    Parameters
    ----------

    c : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCompleter::setModel(QAbstractItemModel *c)
    self.uglySide.call(
        'ritual_ZN10QCompleter8setModelEP18QAbstractItemModel',
        self._addressOf(c),
    )

  @overload(CompletionMode)
  def setCompletionMode(self, mode: CompletionMode) -> None:
    """
    Calls Qt's 'void QCompleter::setCompletionMode(CompletionMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setCompletionMode

    Parameters
    ----------

    mode : CompletionMode
      Passed on as its number.
    """
    #  void QCompleter::setCompletionMode(CompletionMode mode)
    self.uglySide.call(
        'ritual_ZN10QCompleter17setCompletionModeENS_14CompletionModeE',
        mode.value,
    )

  @overload(Qt.MatchFlags)
  def setFilterMode(self, filterMode: Qt.MatchFlags) -> None:
    """
    Calls Qt's 'void QCompleter::setFilterMode(Qt::MatchFlags filterMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setFilterMode

    Parameters
    ----------

    filterMode : Qt.MatchFlags
      Passed on as its number.
    """
    #  void QCompleter::setFilterMode(Qt::MatchFlags filterMode)
    self.uglySide.call(
        'ritual_ZN10QCompleter13setFilterModeE6QFlagsIN2Qt9MatchFlagEE',
        filterMode.value,
    )

  @overload(QAbstractItemView)
  @overload(NoneType)
  def setPopup(self, popup: Optional[QAbstractItemView]) -> None:
    """
    Calls Qt's 'void QCompleter::setPopup(QAbstractItemView *popup)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setPopup

    Parameters
    ----------

    popup : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCompleter::setPopup(QAbstractItemView *popup)
    self.uglySide.call(
        'ritual_ZN10QCompleter8setPopupEP17QAbstractItemView',
        self._addressOf(popup),
    )

  @overload(Qt.CaseSensitivity)
  def setCaseSensitivity(self, caseSensitivity: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void QCompleter::setCaseSensitivity(Qt::CaseSensitivity
    caseSensitivity)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setCaseSensitivity

    Parameters
    ----------

    caseSensitivity : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QCompleter::setCaseSensitivity(Qt::CaseSensitivity
    #      caseSensitivity)
    self.uglySide.call(
        'ritual_ZN10QCompleter18setCaseSensitivityEN2Qt15CaseSensitivityE',
        caseSensitivity.value,
    )

  @overload(ModelSorting)
  def setModelSorting(self, sorting: ModelSorting) -> None:
    """
    Calls Qt's 'void QCompleter::setModelSorting(ModelSorting sorting)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setModelSorting

    Parameters
    ----------

    sorting : ModelSorting
      Passed on as its number.
    """
    #  void QCompleter::setModelSorting(ModelSorting sorting)
    self.uglySide.call(
        'ritual_ZN10QCompleter15setModelSortingENS_12ModelSortingE',
        sorting.value,
    )

  @overload(int)
  def setCompletionColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QCompleter::setCompletionColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleter.html#setCompletionColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QCompleter::setCompletionColumn(int column)
    self.uglySide.call(
        'ritual_ZN10QCompleter19setCompletionColumnEi', column,
    )

  @overload(int)
  def setCompletionRole(self, role: int) -> None:
    """
    Calls Qt's 'void QCompleter::setCompletionRole(int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setCompletionRole

    Parameters
    ----------

    role : int
      Passed on as it is.
    """
    #  void QCompleter::setCompletionRole(int role)
    self.uglySide.call('ritual_ZN10QCompleter17setCompletionRoleEi', role)

  @overload(int)
  def setMaxVisibleItems(self, maxItems: int) -> None:
    """
    Calls Qt's 'void QCompleter::setMaxVisibleItems(int maxItems)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setMaxVisibleItems

    Parameters
    ----------

    maxItems : int
      Passed on as it is.
    """
    #  void QCompleter::setMaxVisibleItems(int maxItems)
    self.uglySide.call(
        'ritual_ZN10QCompleter18setMaxVisibleItemsEi', maxItems,
    )

  @overload(int)
  def setCurrentRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QCompleter::setCurrentRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setCurrentRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QCompleter::setCurrentRow(int row)
    return self.uglySide.call('ritual_ZN10QCompleter13setCurrentRowEi', row)

  @overload(str)
  def setCompletionPrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QCompleter::setCompletionPrefix(const QString &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleter.html#setCompletionPrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCompleter::setCompletionPrefix(const QString &prefix)
    self.uglySide.call(
        'ritual_ZN10QCompleter19setCompletionPrefixERK7QString', prefix,
    )

  @overload(bool)
  def setWrapAround(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QCompleter::setWrapAround(bool wrap)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#setWrapAround

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QCompleter::setWrapAround(bool wrap)
    self.uglySide.call('ritual_ZN10QCompleter13setWrapAroundEb', wrap)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(QAbstractItemModel, QObject)
  @overload(QAbstractItemModel, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      model: Optional[QAbstractItemModel],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCompleter::QCompleter(QAbstractItemModel
    *model, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#QCompleter

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCompleter::QCompleter(QAbstractItemModel *model, QObject *parent)
    self._noteCreation(QCompleter, lambda: Rituals.call(
        'ritual_ZN10QCompleterC1EP18QAbstractItemModelP7QObject',
        self._addressOf(model), self._addressOf(parent),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QCompleter::QCompleter(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#QCompleter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCompleter::QCompleter(QObject *parent)
    self._noteCreation(QCompleter, lambda: Rituals.call(
        'ritual_ZN10QCompleterC1EP7QObject', self._addressOf(parent),
    ))

  @overload(QStringList)
  @overload(QStringList, QObject)
  @overload(QStringList, NoneType)
  def __init__(
      self,
      completions: QStringList,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCompleter::QCompleter(const QStringList
    &completions, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#QCompleter

    Parameters
    ----------

    completions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCompleter::QCompleter(const QStringList &completions, QObject
    #      *parent)
    self._noteCreation(QCompleter, lambda: Rituals.call(
        'ritual_ZN10QCompleterC1ERK5QListI7QStringEP7QObject',
        self._valueOf(completions), self._addressOf(parent),
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

  @overload()
  @overload(QRect)
  def complete(self, rect: Optional[QRect] = None) -> None:
    """
    Calls Qt's 'void QCompleter::complete(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#complete

    Parameters
    ----------

    rect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QCompleter::complete(const QRect &rect)
    if rect is None:
      from ..QtCore import QRect
      rect = QRect()
    self.uglySide.call(
        'ritual_ZN10QCompleter8completeERK5QRect', self._valueOf(rect),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCompleter::eventFilter(QObject *o, QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#eventFilter

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCompleter::eventFilter(QObject *o, QEvent *e)
    ritual = 'ritual_ZN10QCompleter11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QCompleter11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(o), self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCompleter::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleter.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCompleter::event(QEvent *a0)
    ritual = 'ritual_ZN10QCompleter5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QCompleter5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))
