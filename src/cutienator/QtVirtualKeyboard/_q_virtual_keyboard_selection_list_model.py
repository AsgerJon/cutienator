"""
QVirtualKeyboardSelectionListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboardselectionlistmodel.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QVirtualKeyboardAbstractInputMethod
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QVirtualKeyboardAbstractInputMethod = WAIT['QVirtualKeyboardAbstractInputMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardSelectionListModel(QAbstractListModel):
  """
  The cute side of Qt's QVirtualKeyboardSelectionListModel: a plain Python
  object standing in front of one C++ QVirtualKeyboardSelectionListModel.

  It is built on the cute 'QAbstractListModel', as Qt's
  QVirtualKeyboardSelectionListModel is built on Qt's QAbstractListModel, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardSelectionListModel that has a ritual
  and that Python can call so far, 17 names in all: 'metaObject', 'tr',
  'setDataSource', 'dataSource', 'rowCount', 'data', 'roleNames', 'count',
  'selectItem', 'removeItem', 'dataAt', 'countChanged', 'activeItemChanged',
  'itemSelected', 'selectionListChanged', 'selectionListActiveItemChanged',
  'dataSourceDestroyed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardSelectionListModel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QVirtualKeyboardSelectionListModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QVirtualKeyboardSelectionListModelPrivate
    *QVirtualKeyboardSelectionListModel::d_func()': gives
    'QVirtualKeyboardSelectionListModelPrivate', which has no cute class yet.
  - Qt's 'const QVirtualKeyboardSelectionListModelPrivate
    *QVirtualKeyboardSelectionListModel::d_func() const': gives
    'QVirtualKeyboardSelectionListModelPrivate', which has no cute class yet.
  - Qt's 'void
    QVirtualKeyboardSelectionListModel::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's
    'QVirtualKeyboardSelectionListModel::~QVirtualKeyboardSelectionListModel(
    )': the destructor: Python never removes a C++
    QVirtualKeyboardSelectionListModel.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVirtualKeyboardSelectionListModel is created at the first use,
    not by 'QVirtualKeyboardSelectionListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardSelectionListModel.
  - Qt tells when it has removed the C++ QVirtualKeyboardSelectionListModel.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QVirtualKeyboardSelectionListModel, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DictionaryType(CuteNum, scoped=True):
    """
    The enum 'QVirtualKeyboardSelectionListModel::DictionaryType' of Qt, with
    the 2 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Default = Kee[int](0)
    User = Kee[int](1)

  class Role(CuteNum, scoped=True):
    """
    The enum 'QVirtualKeyboardSelectionListModel::Role' of Qt, with the 6
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Display = Kee[int](0)
    DisplayRole = Kee[int](0)
    WordCompletionLength = Kee[int](257)
    WordCompletionLengthRole = Kee[int](257)
    Dictionary = Kee[int](258)
    CanRemoveSuggestion = Kee[int](259)

  class Type(CuteNum, scoped=True):
    """
    The enum 'QVirtualKeyboardSelectionListModel::Type' of Qt, with the 1
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    WordCandidateList = Kee[int](0)

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
    Calls Qt's 'QString QVirtualKeyboardSelectionListModel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#tr

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
    #  QString QVirtualKeyboardSelectionListModel::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardSelectionListModel'

  #  A C++ QVirtualKeyboardSelectionListModel Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardSelectionListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QVirtualKeyboardSelectionListModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardSelectionListModel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QVirtualKeyboardSelectionListModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataSource(self) -> Optional[QVirtualKeyboardAbstractInputMethod]:
    """
    Calls Qt's 'QVirtualKeyboardAbstractInputMethod
    *QVirtualKeyboardSelectionListModel::dataSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#dataSource

    Returns
    -------

    Optional[QVirtualKeyboardAbstractInputMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardAbstractInputMethod
    #      *QVirtualKeyboardSelectionListModel::dataSource() const
    address = self.uglySide.call(
        'ritual_ZNK34QVirtualKeyboardSelectionListModel10dataSourceEv',
    )
    from . import QVirtualKeyboardAbstractInputMethod
    return QVirtualKeyboardAbstractInputMethod._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardSelectionListModel::rowCount(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QVirtualKeyboardSelectionListModel::rowCount(const QModelIndex
    #      &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK34QVirtualKeyboardSelectionListModel8rowCountERK11QModel'
        'Index')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QVirtualKeyboardSelectionListModel8rowCountERK11'
          'QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QVirtualKeyboardSelectionListModel::data(const
    QModelIndex &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVirtualKeyboardSelectionListModel::data(const QModelIndex
    #      &index, int role) const
    ritual = (
        'ritual_ZNK34QVirtualKeyboardSelectionListModel4dataERK11QModelInde'
        'xi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QVirtualKeyboardSelectionListModel4dataERK11QMod'
          'elIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QVirtualKeyboardSelectionListModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QVirtualKeyboardSelectionListModel::roleNames()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QVirtualKeyboardSelectionListModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardSelectionListModel::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#count
    """
    #  int QVirtualKeyboardSelectionListModel::count() const
    return self.uglySide.call(
        'ritual_ZNK34QVirtualKeyboardSelectionListModel5countEv',
    )

  @overload(int)
  @overload(int, Role)
  def dataAt(self, index: int, role: Role = Role.Display) -> QVariant:
    """
    Calls Qt's 'QVariant QVirtualKeyboardSelectionListModel::dataAt(int
    index, Role role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#dataAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : Role
      Passed on as its number. May be left out, as in Qt: it is then
      Role.Display.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QVirtualKeyboardSelectionListModel::dataAt(int index, Role
    #      role) const
    address = self.uglySide.call(
        'ritual_ZNK34QVirtualKeyboardSelectionListModel6dataAtEiNS_4RoleE',
        index, role.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVirtualKeyboardAbstractInputMethod, Type)
  @overload(NoneType, Type)
  def setDataSource(
      self,
      dataSource: Optional[QVirtualKeyboardAbstractInputMethod],
      type: Type,
  ) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardSelectionListModel::setDataSource(
    QVirtualKeyboardAbstractInputMethod *dataSource, Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html

    Parameters
    ----------

    dataSource : Optional[QVirtualKeyboardAbstractInputMethod]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Type
      Passed on as its number.
    """
    #  void QVirtualKeyboardSelectionListModel::setDataSource(
    #      QVirtualKeyboardAbstractInputMethod *dataSource, Type type)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel13setDataSourceEP35QV'
        'irtualKeyboardAbstractInputMethodNS_4TypeE',
        self._addressOf(dataSource), type.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QVirtualKeyboardSelectionListModel::QVirtualKeyboardSelectionListModel(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVirtualKeyboardSelectionListModel::
    #      QVirtualKeyboardSelectionListModel(QObject *parent)
    self._noteCreation(
        QVirtualKeyboardSelectionListModel, lambda: Rituals.call(
            'ritual_ZN34QVirtualKeyboardSelectionListModelC1EP7QObject',
            self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def selectItem(self, index: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardSelectionListModel::selectItem(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#selectItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardSelectionListModel::selectItem(int index)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel10selectItemEi', index,
    )

  @overload(int)
  def removeItem(self, index: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardSelectionListModel::removeItem(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html#removeItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardSelectionListModel::removeItem(int index)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel10removeItemEi', index,
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardSelectionListModel::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html
    """
    #  void QVirtualKeyboardSelectionListModel::countChanged()
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel12countChangedEv',
    )

  @overload(int)
  def activeItemChanged(self, index: int) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardSelectionListModel::activeItemChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardSelectionListModel::activeItemChanged(int index)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel17activeItemChangedEi',
        index,
    )

  @overload(int)
  def itemSelected(self, index: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardSelectionListModel::itemSelected(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardSelectionListModel::itemSelected(int index)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel12itemSelectedEi',
        index,
    )

  @overload(Type)
  def selectionListChanged(self, type: Type) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardSelectionListModel::selectionListChanged(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void QVirtualKeyboardSelectionListModel::selectionListChanged(Type
    #      type)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel20selectionListChange'
        'dENS_4TypeE',
        type.value,
    )

  @overload(Type, int)
  def selectionListActiveItemChanged(self, type: Type, index: int) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardSelectionListModel::selectionListActiveItemChanged(Type
    type, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html

    Parameters
    ----------

    type : Type
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardSelectionListModel::
    #      selectionListActiveItemChanged(Type type, int index)
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel30selectionListActive'
        'ItemChangedENS_4TypeEi',
        type.value, index,
    )

  def dataSourceDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardSelectionListModel::dataSourceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardselectionlistmodel.html
    """
    #  void QVirtualKeyboardSelectionListModel::dataSourceDestroyed()
    self.uglySide.call(
        'ritual_ZN34QVirtualKeyboardSelectionListModel19dataSourceDestroyed'
        'Ev',
    )
