"""
QSortFilterProxyModelHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSortFilterProxyModelHelper to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractProxyModel, QModelIndex, QVariant
  from . import QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSortFilterProxyModelHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSortFilterProxyModelHelper: a plain Python object
  standing in front of one C++ QSortFilterProxyModelHelper.

  What exists
  -----------

  Every function of Qt's QSortFilterProxyModelHelper that has a ritual and
  that Python can call so far, 29 names in all: 'setProperties',
  'can_create_mapping', 'remove_from_mapping', 'clearSourceIndexMapping',
  'source_to_proxy', 'proxy_to_source', 'updateChildrenMapping',
  'filter_changed', 'source_items_inserted',
  'source_items_about_to_be_removed', 'source_items_removed', 'sort',
  'proxyModel', 'beginInsertRows', 'beginInsertColumns', 'endInsertRows',
  'endInsertColumns', 'beginRemoveRows', 'beginRemoveColumns',
  'endRemoveRows', 'endRemoveColumns', 'beginResetModel', 'endResetModel',
  'changePersistentIndexList', 'filterAcceptsRowInternal',
  'filterAcceptsRow', 'filterAcceptsColumnInternal', 'filterAcceptsColumn',
  'lessThan'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSortFilterProxyModelHelper::~QSortFilterProxyModelHelper()': the
    destructor: Python never removes a C++ QSortFilterProxyModelHelper.
  - Qt's 'QSet<int> QSortFilterProxyModelHelper::qListToSet(const QList<int>
    &vector)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSortFilterProxyModelHelper::build_source_to_proxy_mapping(QList<int>
    &proxy_to_source, QList<int> &source_to_proxy, int start) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSortFilterProxyModelHelper::proxy_item_range(const QList<int>
    &source_to_proxy, const QList<int> &source_items, int &proxy_low, int
    &proxy_high) const': takes a type Python has no way to hand over yet.
  - Qt's 'QModelIndexPairList
    QSortFilterProxyModelHelper::store_persistent_indexes() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QSortFilterProxyModelHelper::update_persistent_indexes(const
    QModelIndexPairList &source_indexes)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSet<int>
    QSortFilterProxyModelHelper::handle_filter_changed(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, const QModelIndex
    &source_parent, Direction direction)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSortFilterProxyModelHelper::insert_source_items(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, const QList<int>
    &source_items, const QModelIndex &source_parent, Direction direction,
    bool emit_signal)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSortFilterProxyModelHelper::remove_source_items(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, const QList<int>
    &source_items, const QModelIndex &source_parent, Direction direction,
    bool emit_signal)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSortFilterProxyModelHelper::remove_proxy_interval(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, int proxy_start, int
    proxy_end, const QModelIndex &proxy_parent, Direction direction, bool
    emit_signal)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<std::pair<int, int>>
    QSortFilterProxyModelHelper::proxy_intervals_for_source_items(const
    QList<int> &source_to_proxy, const QList<int> &source_items) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<std::pair<int, QList<int>>>
    QSortFilterProxyModelHelper::proxy_intervals_for_source_items_to_add(
    const QList<int> &a0, const QList<int> &a1, const QModelIndex &a2,
    Direction a3) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSortFilterProxyModelHelper::sort_source_rows(QList<int> &a0,
    const QModelIndex &a1) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 4 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QSortFilterProxyModelHelper is created at the first use, not by
    'QSortFilterProxyModelHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSortFilterProxyModelHelper.
  - Each name of Qt's QSortFilterProxyModelHelper that has no cute function
    yet, 'build_source_to_proxy_mapping', 'createIndex', 'create_mapping',
    'create_mapping_recursive', 'handle_filter_changed', 'index_to_iterator',
    'insert_source_items', 'proxy_intervals_for_source_items',
    'proxy_intervals_for_source_items_to_add', 'proxy_item_range',
    'qListToSet', 'remove_proxy_interval', 'remove_source_items',
    'sort_source_rows', 'store_persistent_indexes',
    'update_persistent_indexes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSortFilterProxyModelHelper, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Direction(CuteNum):
    """
    The enum 'QSortFilterProxyModelHelper::Direction' of Qt, with the 3 names
    Qt gives in it.
    """

    Rows = Kee[int](1)
    Columns = Kee[int](2)
    Both = Kee[int](3)

  #  The classes Qt writes inside QSortFilterProxyModelHelper, each a class
  #  in here as in C++.

  class Mapping(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSortFilterProxyModelHelper::Mapping: a plain
    Python object standing in front of one C++
    QSortFilterProxyModelHelper::Mapping.

    C++ hands a QSortFilterProxyModelHelper::Mapping around as a copy, so
    every C++ QSortFilterProxyModelHelper::Mapping behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSortFilterProxyModelHelper::Mapping yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSortFilterProxyModelHelper::Mapping::~Mapping()': the
      destructor: Python removes its C++ QSortFilterProxyModelHelper::Mapping
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSortFilterProxyModelHelper::Mapping is created at the first
      use, not by 'QSortFilterProxyModelHelper::Mapping(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSortFilterProxyModelHelper::Mapping back gives a
      copy the ritual made for Python, in a new cute
      QSortFilterProxyModelHelper::Mapping.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSortFilterProxyModelHelper::Mapping'

    #  Qt's '~QSortFilterProxyModelHelper::Mapping()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QSortFilterProxyModelHelper::Mapping behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN27QSortFilterProxyModelHelper7MappingD1Ev'

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
  @overload(QVariant, QQmlSortFilterProxyModel, QModelIndex)
  @overload(QVariant, NoneType, QModelIndex)
  @overload(NoneType, QQmlSortFilterProxyModel, QModelIndex)
  @overload(NoneType, NoneType, QModelIndex)
  def setProperties(
      target: Optional[QVariant],
      proxyModel: Optional[QQmlSortFilterProxyModel],
      sourceIndex: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::setProperties(QVariant
    *target, const QQmlSortFilterProxyModel *proxyModel, const QModelIndex
    &sourceIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#setProperties

    Parameters
    ----------

    target : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QSortFilterProxyModelHelper::setProperties(QVariant *target,
    #      const QQmlSortFilterProxyModel *proxyModel, const QModelIndex
    #      &sourceIndex)
    Rituals.call(
        'ritual_ZN27QSortFilterProxyModelHelper13setPropertiesEP8QVariantPK'
        '24QQmlSortFilterProxyModelRK11QModelIndex',
        CuteMixin._addressOf(target), CuteMixin._addressOf(proxyModel),
        CuteMixin._valueOf(sourceIndex),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSortFilterProxyModelHelper'

  #  A C++ QSortFilterProxyModelHelper Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSortFilterProxyModelHelper'

  #  The functions Qt calls itself that QSortFilterProxyModelHelper is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'handle_filter_changed': (
          'QSet<int> '
          'QSortFilterProxyModelHelper::handle_filter_changed(QList<int> '
          '&, QList<int> &, const QModelIndex &, Direction)',
      ),
      'insert_source_items': (
          'void '
          'QSortFilterProxyModelHelper::insert_source_items(QList<int> &, '
          'QList<int> &, const QList<int> &, const QModelIndex &, '
          'Direction, bool)',
      ),
      'remove_source_items': (
          'void '
          'QSortFilterProxyModelHelper::remove_source_items(QList<int> &, '
          'QList<int> &, const QList<int> &, const QModelIndex &, '
          'Direction, bool)',
      ),
      'remove_proxy_interval': (
          'void '
          'QSortFilterProxyModelHelper::remove_proxy_interval(QList<int> '
          '&, QList<int> &, int, int, const QModelIndex &, Direction, bool)',
      ),
      'proxy_intervals_for_source_items': (
          'QList<std::pair<int, int>> '
          'QSortFilterProxyModelHelper::proxy_intervals_for_source_items(co'
          'nst QList<int> &, const QList<int> &) const',
      ),
      'proxy_intervals_for_source_items_to_add': (
          'QList<std::pair<int, QList<int>>> '
          'QSortFilterProxyModelHelper::proxy_intervals_for_source_items_to'
          '_add(const QList<int> &, const QList<int> &, const QModelIndex '
          '&, Direction) const',
      ),
      'createIndex': (
          'QModelIndex QSortFilterProxyModelHelper::createIndex(int, int, '
          'IndexMap::const_iterator) const',
      ),
      'changePersistentIndexList': (
          'void '
          'QSortFilterProxyModelHelper::changePersistentIndexList(const '
          'QModelIndexList &, const QModelIndexList &)',
      ),
      'sort_source_rows': (
          'void QSortFilterProxyModelHelper::sort_source_rows(QList<int> '
          '&, const QModelIndex &) const',
      ),
  }

  #  The functions Qt calls itself that QSortFilterProxyModelHelper is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'filter_changed': (
          ('_ZN27QSortFilterProxyModelHelper14filter_changedENS_9DirectionE'
           'RK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtQmlModels:QSortFilterProxyModelHelper.Direction'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'source_items_inserted': (
          ('_ZN27QSortFilterProxyModelHelper21source_items_insertedERK11QMo'
           'delIndexiiNS_9DirectionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'enum',
                'QtQmlModels:QSortFilterProxyModelHelper.Direction'),
           )),
      ),
      'source_items_about_to_be_removed': (
          ('_ZN27QSortFilterProxyModelHelper32source_items_about_to_be_remo'
           'vedERK11QModelIndexiiNS_9DirectionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'enum',
                'QtQmlModels:QSortFilterProxyModelHelper.Direction'),
           )),
      ),
      'source_items_removed': (
          ('_ZN27QSortFilterProxyModelHelper20source_items_removedERK11QMod'
           'elIndexiiNS_9DirectionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'enum',
                'QtQmlModels:QSortFilterProxyModelHelper.Direction'),
           )),
      ),
      'sort': (
          ('_ZN27QSortFilterProxyModelHelper4sortEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'proxyModel': (
          ('_ZNK27QSortFilterProxyModelHelper10proxyModelEv',
           ('address', 'address', 'QtCore:QAbstractProxyModel'),
           ()),
      ),
      'beginInsertRows': (
          ('_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11QModelInd'
           'exii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'beginInsertColumns': (
          ('_ZN27QSortFilterProxyModelHelper18beginInsertColumnsERK11QModel'
           'Indexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'endInsertRows': (
          ('_ZN27QSortFilterProxyModelHelper13endInsertRowsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endInsertColumns': (
          ('_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'beginRemoveRows': (
          ('_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11QModelInd'
           'exii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'beginRemoveColumns': (
          ('_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsERK11QModel'
           'Indexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'endRemoveRows': (
          ('_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endRemoveColumns': (
          ('_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'beginResetModel': (
          ('_ZN27QSortFilterProxyModelHelper15beginResetModelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endResetModel': (
          ('_ZN27QSortFilterProxyModelHelper13endResetModelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'filterAcceptsRowInternal': (
          ('_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInternalEiRK'
           '11QModelIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'filterAcceptsRow': (
          ('_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiRK11QModel'
           'Index',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'filterAcceptsColumnInternal': (
          ('_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumnInternalE'
           'iRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'filterAcceptsColumn': (
          ('_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumnEiRK11QMo'
           'delIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'lessThan': (
          ('_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelIndexS2_',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
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

  @overload(QModelIndex)
  def can_create_mapping(self, source_parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModelHelper::can_create_mapping(const
    QModelIndex &source_parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModelHelper::can_create_mapping(const QModelIndex
    #      &source_parent) const
    return self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZNK27QSortFilterProxyModelHelper18can_create_mappingERK11QM'
        'odelIndex',
        self._valueOf(source_parent),
    )

  @overload(QModelIndex)
  def source_to_proxy(self, source_index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    QSortFilterProxyModelHelper::source_to_proxy(const QModelIndex
    &source_index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#source_to_proxy

    Parameters
    ----------

    source_index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QSortFilterProxyModelHelper::source_to_proxy(const
    #      QModelIndex &source_index) const
    address = self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZNK27QSortFilterProxyModelHelper15source_to_proxyERK11QMode'
        'lIndex',
        self._valueOf(source_index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def proxy_to_source(self, proxy_index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    QSortFilterProxyModelHelper::proxy_to_source(const QModelIndex
    &proxy_index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#proxy_to_source

    Parameters
    ----------

    proxy_index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QSortFilterProxyModelHelper::proxy_to_source(const
    #      QModelIndex &proxy_index) const
    address = self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZNK27QSortFilterProxyModelHelper15proxy_to_sourceERK11QMode'
        'lIndex',
        self._valueOf(proxy_index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def proxyModel(self) -> Optional[QAbstractProxyModel]:
    """
    Calls Qt's 'const QAbstractProxyModel
    *QSortFilterProxyModelHelper::proxyModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#proxyModel

    Returns
    -------

    Optional[QAbstractProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractProxyModel *QSortFilterProxyModelHelper::proxyModel()
    #      const
    address = self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZNK27QSortFilterProxyModelHelper10proxyModelEv',
    )
    from ..QtCore import QAbstractProxyModel
    return QAbstractProxyModel._cuteAt(address)

  @overload(int, QModelIndex)
  def filterAcceptsRowInternal(self, a0: int, a1: QModelIndex) -> bool:
    """
    Calls Qt's 'bool
    QSortFilterProxyModelHelper::filterAcceptsRowInternal(int a0, const
    QModelIndex &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModelHelper::filterAcceptsRowInternal(int a0,
    #      const QModelIndex &a1) const
    ritual = (
        'ritual_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInternalE'
        'iRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInt'
          'ernalEiRK11QModelIndex')
    return self._callAs(
        'QSortFilterProxyModelHelper', ritual, a0, self._valueOf(a1),
    )

  @overload(int, QModelIndex)
  def filterAcceptsRow(self, a0: int, a1: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModelHelper::filterAcceptsRow(int a0,
    const QModelIndex &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#filterAcceptsRow

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModelHelper::filterAcceptsRow(int a0, const
    #      QModelIndex &a1) const
    ritual = (
        'ritual_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiRK11QMo'
        'delIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiR'
          'K11QModelIndex')
    return self._callAs(
        'QSortFilterProxyModelHelper', ritual, a0, self._valueOf(a1),
    )

  @overload(int, QModelIndex)
  def filterAcceptsColumnInternal(self, a0: int, a1: QModelIndex) -> bool:
    """
    Calls Qt's 'bool
    QSortFilterProxyModelHelper::filterAcceptsColumnInternal(int a0, const
    QModelIndex &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModelHelper::filterAcceptsColumnInternal(int a0,
    #      const QModelIndex &a1) const
    ritual = (
        'ritual_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumnIntern'
        'alEiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumn'
          'InternalEiRK11QModelIndex')
    return self._callAs(
        'QSortFilterProxyModelHelper', ritual, a0, self._valueOf(a1),
    )

  @overload(int, QModelIndex)
  def filterAcceptsColumn(self, a0: int, a1: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModelHelper::filterAcceptsColumn(int a0,
    const QModelIndex &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModelHelper::filterAcceptsColumn(int a0, const
    #      QModelIndex &a1) const
    ritual = (
        'ritual_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumnEiRK11'
        'QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumn'
          'EiRK11QModelIndex')
    return self._callAs(
        'QSortFilterProxyModelHelper', ritual, a0, self._valueOf(a1),
    )

  @overload(QModelIndex, QModelIndex)
  def lessThan(self, a0: QModelIndex, a1: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSortFilterProxyModelHelper::lessThan(const QModelIndex
    &a0, const QModelIndex &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#lessThan

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSortFilterProxyModelHelper::lessThan(const QModelIndex &a0,
    #      const QModelIndex &a1) const
    ritual = (
        'ritual_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelIndexS2'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelI'
          'ndexS2_')
    return self._callAs(
        'QSortFilterProxyModelHelper', ritual,
        self._valueOf(a0), self._valueOf(a1),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSortFilterProxyModelHelper::QSortFilterProxyModelHelper()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html
    """
    #  QSortFilterProxyModelHelper::QSortFilterProxyModelHelper()
    self._noteCreation(QSortFilterProxyModelHelper, lambda: Rituals.call(
        'ritual_ZN27QSortFilterProxyModelHelperC1Ev',
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

  @overload(QModelIndex)
  def remove_from_mapping(self, source_parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::remove_from_mapping(const
    QModelIndex &source_parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QSortFilterProxyModelHelper::remove_from_mapping(const
    #      QModelIndex &source_parent)
    self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZN27QSortFilterProxyModelHelper19remove_from_mappingERK11QM'
        'odelIndex',
        self._valueOf(source_parent),
    )

  def clearSourceIndexMapping(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::clearSourceIndexMapping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html
    """
    #  void QSortFilterProxyModelHelper::clearSourceIndexMapping()
    self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZN27QSortFilterProxyModelHelper23clearSourceIndexMappingEv',
    )

  @overload(QModelIndex, Mapping, Direction, int, int, int, bool)
  @overload(QModelIndex, NoneType, Direction, int, int, int, bool)
  def updateChildrenMapping(
      self,
      source_parent: QModelIndex,
      parent_mapping: Optional[Mapping],
      direction: Direction,
      start: int,
      end: int,
      delta_item_count: int,
      remove: bool,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::updateChildrenMapping(const
    QModelIndex &source_parent, Mapping *parent_mapping, Direction direction,
    int start, int end, int delta_item_count, bool remove)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    parent_mapping : Optional[Mapping]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    direction : Direction
      Passed on as its number.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    delta_item_count : int
      Passed on as it is.

    remove : bool
      Passed on as it is.
    """
    #  void QSortFilterProxyModelHelper::updateChildrenMapping(const
    #      QModelIndex &source_parent, Mapping *parent_mapping, Direction
    #      direction, int start, int end, int delta_item_count, bool remove)
    self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZN27QSortFilterProxyModelHelper21updateChildrenMappingERK11'
        'QModelIndexPNS_7MappingENS_9DirectionEiiib',
        self._valueOf(source_parent), self._addressOf(parent_mapping),
        direction.value, start, end, delta_item_count, remove,
    )

  @overload()
  @overload(Direction)
  @overload(Direction, QModelIndex)
  def filter_changed(
      self,
      dir: Direction = Direction.Both,
      source_parent: Optional[QModelIndex] = None,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::filter_changed(Direction
    dir, const QModelIndex &source_parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#filter_changed

    Parameters
    ----------

    dir : Direction
      Passed on as its number. May be left out, as in Qt: it is then
      Direction.Both.

    source_parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  void QSortFilterProxyModelHelper::filter_changed(Direction dir, const
    #      QModelIndex &source_parent)
    if source_parent is None:
      from ..QtCore import QModelIndex
      source_parent = QModelIndex()
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper14filter_changedENS_9Directi'
        'onERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper14filter_changedENS_9D'
          'irectionERK11QModelIndex')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual,
        dir.value, self._valueOf(source_parent),
    )

  @overload(QModelIndex, int, int, Direction)
  def source_items_inserted(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
      direction: Direction,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::source_items_inserted(const
    QModelIndex &source_parent, int start, int end, Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    direction : Direction
      Passed on as its number.
    """
    #  void QSortFilterProxyModelHelper::source_items_inserted(const
    #      QModelIndex &source_parent, int start, int end, Direction
    #      direction)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper21source_items_insertedERK11'
        'QModelIndexiiNS_9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper21source_items_inserte'
          'dERK11QModelIndexiiNS_9DirectionE')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual,
        self._valueOf(source_parent), start, end, direction.value,
    )

  @overload(QModelIndex, int, int, Direction)
  def source_items_about_to_be_removed(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
      direction: Direction,
  ) -> None:
    """
    Calls Qt's 'void
    QSortFilterProxyModelHelper::source_items_about_to_be_removed(const
    QModelIndex &source_parent, int start, int end, Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    direction : Direction
      Passed on as its number.
    """
    #  void QSortFilterProxyModelHelper::source_items_about_to_be_removed(
    #      const QModelIndex &source_parent, int start, int end, Direction
    #      direction)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper32source_items_about_to_be_r'
        'emovedERK11QModelIndexiiNS_9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper32source_items_about_t'
          'o_be_removedERK11QModelIndexiiNS_9DirectionE')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual,
        self._valueOf(source_parent), start, end, direction.value,
    )

  @overload(QModelIndex, int, int, Direction)
  def source_items_removed(
      self,
      source_parent: QModelIndex,
      start: int,
      end: int,
      direction: Direction,
  ) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::source_items_removed(const
    QModelIndex &source_parent, int start, int end, Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    source_parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    direction : Direction
      Passed on as its number.
    """
    #  void QSortFilterProxyModelHelper::source_items_removed(const
    #      QModelIndex &source_parent, int start, int end, Direction
    #      direction)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper20source_items_removedERK11Q'
        'ModelIndexiiNS_9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper20source_items_removed'
          'ERK11QModelIndexiiNS_9DirectionE')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual,
        self._valueOf(source_parent), start, end, direction.value,
    )

  def sort(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::sort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#sort
    """
    #  void QSortFilterProxyModelHelper::sort()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper4sortEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QSortFilterProxyModelHelper4sortEv'
    self._callAs('QSortFilterProxyModelHelper', ritual)

  @overload(QModelIndex, int, int)
  def beginInsertRows(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::beginInsertRows(const
    QModelIndex &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#beginInsertRows

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModelHelper::beginInsertRows(const QModelIndex
    #      &a0, int a1, int a2)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11QModel'
        'Indexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11'
          'QModelIndexii')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual, self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int)
  def beginInsertColumns(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::beginInsertColumns(const
    QModelIndex &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModelHelper::beginInsertColumns(const QModelIndex
    #      &a0, int a1, int a2)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper18beginInsertColumnsERK11QMo'
        'delIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper18beginInsertColumnsER'
          'K11QModelIndexii')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual, self._valueOf(a0), a1, a2,
    )

  def endInsertRows(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::endInsertRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#endInsertRows
    """
    #  void QSortFilterProxyModelHelper::endInsertRows()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper13endInsertRowsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QSortFilterProxyModelHelper13endInsertRowsEv'
    self._callAs('QSortFilterProxyModelHelper', ritual)

  def endInsertColumns(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::endInsertColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#endInsertColumns
    """
    #  void QSortFilterProxyModelHelper::endInsertColumns()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv')
    self._callAs('QSortFilterProxyModelHelper', ritual)

  @overload(QModelIndex, int, int)
  def beginRemoveRows(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::beginRemoveRows(const
    QModelIndex &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#beginRemoveRows

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModelHelper::beginRemoveRows(const QModelIndex
    #      &a0, int a1, int a2)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11QModel'
        'Indexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11'
          'QModelIndexii')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual, self._valueOf(a0), a1, a2,
    )

  @overload(QModelIndex, int, int)
  def beginRemoveColumns(self, a0: QModelIndex, a1: int, a2: int) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::beginRemoveColumns(const
    QModelIndex &a0, int a1, int a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  void QSortFilterProxyModelHelper::beginRemoveColumns(const QModelIndex
    #      &a0, int a1, int a2)
    ritual = (
        'ritual_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsERK11QMo'
        'delIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsER'
          'K11QModelIndexii')
    self._callAs(
        'QSortFilterProxyModelHelper', ritual, self._valueOf(a0), a1, a2,
    )

  def endRemoveRows(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::endRemoveRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#endRemoveRows
    """
    #  void QSortFilterProxyModelHelper::endRemoveRows()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv'
    self._callAs('QSortFilterProxyModelHelper', ritual)

  def endRemoveColumns(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::endRemoveColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#endRemoveColumns
    """
    #  void QSortFilterProxyModelHelper::endRemoveColumns()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv')
    self._callAs('QSortFilterProxyModelHelper', ritual)

  def beginResetModel(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::beginResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#beginResetModel
    """
    #  void QSortFilterProxyModelHelper::beginResetModel()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper15beginResetModelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSortFilterProxyModelHelper15beginResetModelEv')
    self._callAs('QSortFilterProxyModelHelper', ritual)

  def endResetModel(self) -> None:
    """
    Calls Qt's 'void QSortFilterProxyModelHelper::endResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html#endResetModel
    """
    #  void QSortFilterProxyModelHelper::endResetModel()
    ritual = 'ritual_ZN27QSortFilterProxyModelHelper13endResetModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QSortFilterProxyModelHelper13endResetModelEv'
    self._callAs('QSortFilterProxyModelHelper', ritual)

  @overload(QList[QModelIndex], QList[QModelIndex])
  def changePersistentIndexList(
      self,
      a0: QList[QModelIndex],
      a1: QList[QModelIndex],
  ) -> None:
    """
    Calls Qt's 'void
    QSortFilterProxyModelHelper::changePersistentIndexList(const
    QModelIndexList &a0, const QModelIndexList &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsortfilterproxymodelhelper.html

    Parameters
    ----------

    a0 : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    a1 : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSortFilterProxyModelHelper::changePersistentIndexList(const
    #      QModelIndexList &a0, const QModelIndexList &a1)
    self._callAs(
        'QSortFilterProxyModelHelper',
        'ritual_ZN27QSortFilterProxyModelHelper25changePersistentIndexListE'
        'RK5QListI11QModelIndexES4_',
        self._valueOf(a0), self._valueOf(a1),
    )

  @staticmethod
  def build_source_to_proxy_mapping(*__, **_) -> Never:
    """
    Qt's 'void
    QSortFilterProxyModelHelper::build_source_to_proxy_mapping(QList<int>
    &proxy_to_source, QList<int> &source_to_proxy, int start) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.build_source_to_proxy_mapping' has no "
        "cute function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::build_source_to_proxy_mapping(QList<in"
        "t> &proxy_to_source, QList<int> &source_to_proxy, int start) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createIndex(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QSortFilterProxyModelHelper::createIndex(int a0, int
    a1, IndexMap::const_iterator a2) const': the compiler refuses its ritual
    as it would be written here: use of undeclared identifier 'IndexMap'; did
    you mean 'CuteQSortFilterProxyModelHelper::IndexMap'?.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.createIndex' has no cute function "
        "yet. Qt's 'QModelIndex "
        "QSortFilterProxyModelHelper::createIndex(int a0, int a1, "
        "IndexMap::const_iterator a2) const': the compiler refuses its "
        "ritual as it would be written here: use of undeclared identifier "
        "'IndexMap'; did you mean "
        "'CuteQSortFilterProxyModelHelper::IndexMap'?.")

  @staticmethod
  def create_mapping(*__, **_) -> Never:
    """
    Qt's 'IndexMap::const_iterator
    QSortFilterProxyModelHelper::create_mapping(const QModelIndex
    &source_parent) const': the compiler refuses its ritual as it would be
    written here: use of undeclared identifier 'IndexMap'; did you mean
    'CuteQSortFilterProxyModelHelper::IndexMap'?.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.create_mapping' has no cute function "
        "yet. Qt's 'IndexMap::const_iterator "
        "QSortFilterProxyModelHelper::create_mapping(const QModelIndex "
        "&source_parent) const': the compiler refuses its ritual as it "
        "would be written here: use of undeclared identifier 'IndexMap'; "
        "did you mean 'CuteQSortFilterProxyModelHelper::IndexMap'?.")

  @staticmethod
  def create_mapping_recursive(*__, **_) -> Never:
    """
    Qt's 'IndexMap::const_iterator
    QSortFilterProxyModelHelper::create_mapping_recursive(const QModelIndex
    &source_parent) const': the compiler refuses its ritual as it would be
    written here: use of undeclared identifier 'IndexMap'; did you mean
    'CuteQSortFilterProxyModelHelper::IndexMap'?.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.create_mapping_recursive' has no cute "
        "function yet. Qt's 'IndexMap::const_iterator "
        "QSortFilterProxyModelHelper::create_mapping_recursive(const "
        "QModelIndex &source_parent) const': the compiler refuses its "
        "ritual as it would be written here: use of undeclared identifier "
        "'IndexMap'; did you mean "
        "'CuteQSortFilterProxyModelHelper::IndexMap'?.")

  @staticmethod
  def handle_filter_changed(*__, **_) -> Never:
    """
    Qt's 'QSet<int>
    QSortFilterProxyModelHelper::handle_filter_changed(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, const QModelIndex
    &source_parent, Direction direction)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.handle_filter_changed' has no cute "
        "function yet. Qt's 'QSet<int> "
        "QSortFilterProxyModelHelper::handle_filter_changed(QList<int> "
        "&source_to_proxy, QList<int> &proxy_to_source, const QModelIndex "
        "&source_parent, Direction direction)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def index_to_iterator(*__, **_) -> Never:
    """
    Qt's 'IndexMap::const_iterator
    QSortFilterProxyModelHelper::index_to_iterator(const QModelIndex
    &proxy_index) const': the compiler refuses its ritual as it would be
    written here: use of undeclared identifier 'IndexMap'; did you mean
    'CuteQSortFilterProxyModelHelper::IndexMap'?.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.index_to_iterator' has no cute "
        "function yet. Qt's 'IndexMap::const_iterator "
        "QSortFilterProxyModelHelper::index_to_iterator(const QModelIndex "
        "&proxy_index) const': the compiler refuses its ritual as it would "
        "be written here: use of undeclared identifier 'IndexMap'; did you "
        "mean 'CuteQSortFilterProxyModelHelper::IndexMap'?.")

  @staticmethod
  def insert_source_items(*__, **_) -> Never:
    """
    Qt's 'void QSortFilterProxyModelHelper::insert_source_items(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, const QList<int>
    &source_items, const QModelIndex &source_parent, Direction direction,
    bool emit_signal)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.insert_source_items' has no cute "
        "function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::insert_source_items(QList<int> "
        "&source_to_proxy, QList<int> &proxy_to_source, const QList<int> "
        "&source_items, const QModelIndex &source_parent, Direction "
        "direction, bool emit_signal)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def proxy_intervals_for_source_items(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<int, int>>
    QSortFilterProxyModelHelper::proxy_intervals_for_source_items(const
    QList<int> &source_to_proxy, const QList<int> &source_items) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.proxy_intervals_for_source_items' has "
        "no cute function yet. Qt's 'QList<std::pair<int, int>> "
        "QSortFilterProxyModelHelper::proxy_intervals_for_source_items(const"
        " QList<int> &source_to_proxy, const QList<int> &source_items) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def proxy_intervals_for_source_items_to_add(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<int, QList<int>>>
    QSortFilterProxyModelHelper::proxy_intervals_for_source_items_to_add(
    const QList<int> &a0, const QList<int> &a1, const QModelIndex &a2,
    Direction a3) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.proxy_intervals_for_source_items_to_ad"
        "d' has no cute function yet. Qt's 'QList<std::pair<int, "
        "QList<int>>> "
        "QSortFilterProxyModelHelper::proxy_intervals_for_source_items_to_ad"
        "d(const QList<int> &a0, const QList<int> &a1, const QModelIndex "
        "&a2, Direction a3) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def proxy_item_range(*__, **_) -> Never:
    """
    Qt's 'void QSortFilterProxyModelHelper::proxy_item_range(const QList<int>
    &source_to_proxy, const QList<int> &source_items, int &proxy_low, int
    &proxy_high) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.proxy_item_range' has no cute "
        "function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::proxy_item_range(const QList<int> "
        "&source_to_proxy, const QList<int> &source_items, int &proxy_low, "
        "int &proxy_high) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def qListToSet(*__, **_) -> Never:
    """
    Qt's 'QSet<int> QSortFilterProxyModelHelper::qListToSet(const QList<int>
    &vector)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.qListToSet' has no cute function yet. "
        "Qt's 'QSet<int> QSortFilterProxyModelHelper::qListToSet(const "
        "QList<int> &vector)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def remove_proxy_interval(*__, **_) -> Never:
    """
    Qt's 'void QSortFilterProxyModelHelper::remove_proxy_interval(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, int proxy_start, int
    proxy_end, const QModelIndex &proxy_parent, Direction direction, bool
    emit_signal)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.remove_proxy_interval' has no cute "
        "function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::remove_proxy_interval(QList<int> "
        "&source_to_proxy, QList<int> &proxy_to_source, int proxy_start, "
        "int proxy_end, const QModelIndex &proxy_parent, Direction "
        "direction, bool emit_signal)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def remove_source_items(*__, **_) -> Never:
    """
    Qt's 'void QSortFilterProxyModelHelper::remove_source_items(QList<int>
    &source_to_proxy, QList<int> &proxy_to_source, const QList<int>
    &source_items, const QModelIndex &source_parent, Direction direction,
    bool emit_signal)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.remove_source_items' has no cute "
        "function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::remove_source_items(QList<int> "
        "&source_to_proxy, QList<int> &proxy_to_source, const QList<int> "
        "&source_items, const QModelIndex &source_parent, Direction "
        "direction, bool emit_signal)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def sort_source_rows(*__, **_) -> Never:
    """
    Qt's 'void QSortFilterProxyModelHelper::sort_source_rows(QList<int> &a0,
    const QModelIndex &a1) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.sort_source_rows' has no cute "
        "function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::sort_source_rows(QList<int> &a0, "
        "const QModelIndex &a1) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def store_persistent_indexes(*__, **_) -> Never:
    """
    Qt's 'QModelIndexPairList
    QSortFilterProxyModelHelper::store_persistent_indexes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.store_persistent_indexes' has no cute "
        "function yet. Qt's 'QModelIndexPairList "
        "QSortFilterProxyModelHelper::store_persistent_indexes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def update_persistent_indexes(*__, **_) -> Never:
    """
    Qt's 'void QSortFilterProxyModelHelper::update_persistent_indexes(const
    QModelIndexPairList &source_indexes)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSortFilterProxyModelHelper.update_persistent_indexes' has no "
        "cute function yet. Qt's 'void "
        "QSortFilterProxyModelHelper::update_persistent_indexes(const "
        "QModelIndexPairList &source_indexes)': takes a type Python has no "
        "way to hand over yet.")
