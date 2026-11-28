"""
AbstractItemModelHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/abstractitemmodelhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means AbstractItemModelHandler to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractItemModel, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex, QPersistentModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractItemModelHandler(QObject):
  """
  The cute side of Qt's AbstractItemModelHandler: a plain Python object
  standing in front of one C++ AbstractItemModelHandler.

  It is built on the cute 'QObject', as Qt's AbstractItemModelHandler is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AbstractItemModelHandler that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'setItemModel',
  'itemModel', 'handleColumnsInserted', 'handleColumnsMoved',
  'handleColumnsRemoved', 'handleLayoutChanged', 'handleModelReset',
  'handleRowsInserted', 'handleRowsMoved', 'handleRowsRemoved',
  'handleMappingChanged', 'handlePendingResolve', 'itemModelChanged',
  'resolveModel'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AbstractItemModelHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int AbstractItemModelHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'AbstractItemModelHandler::~AbstractItemModelHandler()': the
    destructor: Python never removes a C++ AbstractItemModelHandler.
  - Qt's 'void AbstractItemModelHandler::handleDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 25 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'AbstractItemModelHandler.

  What to expect
  --------------

  - The C++ AbstractItemModelHandler is created at the first use, not by
    'AbstractItemModelHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AbstractItemModelHandler.
  - Qt tells when it has removed the C++ AbstractItemModelHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's AbstractItemModelHandler that has no cute function yet,
    '__init__', 'handleDataChanged', holds a function that raises
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
  __qt_class__ = 'AbstractItemModelHandler'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ AbstractItemModelHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AbstractItemModelHandler'

  #  The functions Qt calls itself that AbstractItemModelHandler is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'handleDataChanged': (
          'void AbstractItemModelHandler::handleDataChanged(const '
          'QModelIndex &, const QModelIndex &, const QList<int> &)',
      ),
      'handleLayoutChanged': (
          'void AbstractItemModelHandler::handleLayoutChanged(const '
          'QList<QPersistentModelIndex> &, '
          'QAbstractItemModel::LayoutChangeHint)',
      ),
  }

  #  The functions Qt calls itself that AbstractItemModelHandler is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setItemModel': (
          ('_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItemMod'
           'el',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QAbstractItemModel'),
           )),
      ),
      'itemModel': (
          ('_ZNK24AbstractItemModelHandler9itemModelEv',
           ('address', 'address', 'QtCore:QAbstractItemModel'),
           ()),
      ),
      'handleColumnsInserted': (
          ('_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QModel'
           'Indexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'handleColumnsMoved': (
          ('_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModelInd'
           'exiiS2_i',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'handleColumnsRemoved': (
          ('_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QModelI'
           'ndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'handleModelReset': (
          ('_ZN24AbstractItemModelHandler16handleModelResetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleRowsInserted': (
          ('_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModelInd'
           'exii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'handleRowsMoved': (
          ('_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelIndexi'
           'iS2_i',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'handleRowsRemoved': (
          ('_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelInde'
           'xii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'handleMappingChanged': (
          ('_ZN24AbstractItemModelHandler20handleMappingChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handlePendingResolve': (
          ('_ZN24AbstractItemModelHandler20handlePendingResolveEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resolveModel': (
          ('_ZN24AbstractItemModelHandler12resolveModelEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *AbstractItemModelHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AbstractItemModelHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24AbstractItemModelHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def itemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *AbstractItemModelHandler::itemModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#itemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *AbstractItemModelHandler::itemModel() const
    ritual = 'ritual_ZNK24AbstractItemModelHandler9itemModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24AbstractItemModelHandler9itemModelEv'
    address = self.uglySide.call(ritual)
    return QAbstractItemModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setItemModel(self, itemModel: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void
    AbstractItemModelHandler::setItemModel(QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#setItemModel

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractItemModelHandler::setItemModel(QAbstractItemModel
    #      *itemModel)
    self.uglySide.call(
        'ritual_ZN24AbstractItemModelHandler12setItemModelEP18QAbstractItem'
        'Model',
        self._addressOf(itemModel),
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
    Qt's 'AbstractItemModelHandler::AbstractItemModelHandler(QObject
    *parent)': leans on
    'AbstractItemModelHandler::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'AbstractItemModelHandler.__init__' has no cute function yet. Qt's "
        "'AbstractItemModelHandler::AbstractItemModelHandler(QObject "
        "*parent)': leans on "
        "'AbstractItemModelHandler::qt_metacall(QMetaObject::Call, int, "
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

  @overload(QModelIndex, int, int)
  def handleColumnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleColumnsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void AbstractItemModelHandler::handleColumnsInserted(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN24AbstractItemModelHandler21handleColumnsInsertedERK11QMo'
        'delIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler21handleColumnsInsertedER'
          'K11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int, QModelIndex, int)
  def handleColumnsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destinationParent: QModelIndex,
      destinationColumn: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleColumnsMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destinationParent, int destinationColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleColumnsMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationColumn : int
      Passed on as it is.
    """
    #  void AbstractItemModelHandler::handleColumnsMoved(const QModelIndex
    #      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    #      &destinationParent, int destinationColumn)
    ritual = (
        'ritual_ZN24AbstractItemModelHandler18handleColumnsMovedERK11QModel'
        'IndexiiS2_i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler18handleColumnsMovedERK11'
          'QModelIndexiiS2_i')
    self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destinationParent), destinationColumn,
    )

  @overload(QModelIndex, int, int)
  def handleColumnsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleColumnsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleColumnsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void AbstractItemModelHandler::handleColumnsRemoved(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN24AbstractItemModelHandler20handleColumnsRemovedERK11QMod'
        'elIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler20handleColumnsRemovedERK'
          '11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QList[QPersistentModelIndex])
  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def handleLayoutChanged(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint = (
          QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint),
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleLayoutChanged(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleLayoutChanged

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint.
    """
    #  void AbstractItemModelHandler::handleLayoutChanged(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN24AbstractItemModelHandler19handleLayoutChangedERK5QListI'
        '21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(parents), hint.value,
    )

  def handleModelReset(self) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleModelReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleModelReset
    """
    #  void AbstractItemModelHandler::handleModelReset()
    ritual = 'ritual_ZN24AbstractItemModelHandler16handleModelResetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24AbstractItemModelHandler16handleModelResetEv'
    self.uglySide.call(ritual)

  @overload(QModelIndex, int, int)
  def handleRowsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleRowsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleRowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void AbstractItemModelHandler::handleRowsInserted(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN24AbstractItemModelHandler18handleRowsInsertedERK11QModel'
        'Indexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler18handleRowsInsertedERK11'
          'QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int, QModelIndex, int)
  def handleRowsMoved(
      self,
      sourceParent: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destinationParent: QModelIndex,
      destinationRow: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleRowsMoved(const
    QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
    QModelIndex &destinationParent, int destinationRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleRowsMoved

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationRow : int
      Passed on as it is.
    """
    #  void AbstractItemModelHandler::handleRowsMoved(const QModelIndex
    #      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
    #      &destinationParent, int destinationRow)
    ritual = (
        'ritual_ZN24AbstractItemModelHandler15handleRowsMovedERK11QModelInd'
        'exiiS2_i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler15handleRowsMovedERK11QMo'
          'delIndexiiS2_i')
    self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceStart, sourceEnd,
        self._valueOf(destinationParent), destinationRow,
    )

  @overload(QModelIndex, int, int)
  def handleRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleRowsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleRowsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void AbstractItemModelHandler::handleRowsRemoved(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN24AbstractItemModelHandler17handleRowsRemovedERK11QModelI'
        'ndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler17handleRowsRemovedERK11Q'
          'ModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  def handleMappingChanged(self) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handleMappingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handleMappingChanged
    """
    #  void AbstractItemModelHandler::handleMappingChanged()
    ritual = 'ritual_ZN24AbstractItemModelHandler20handleMappingChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler20handleMappingChangedEv')
    self.uglySide.call(ritual)

  def handlePendingResolve(self) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::handlePendingResolve()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#handlePendingResolve
    """
    #  void AbstractItemModelHandler::handlePendingResolve()
    ritual = 'ritual_ZN24AbstractItemModelHandler20handlePendingResolveEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24AbstractItemModelHandler20handlePendingResolveEv')
    self.uglySide.call(ritual)

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def itemModelChanged(
      self,
      itemModel: Optional[QAbstractItemModel],
  ) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::itemModelChanged(const
    QAbstractItemModel *itemModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#itemModelChanged

    Parameters
    ----------

    itemModel : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractItemModelHandler::itemModelChanged(const
    #      QAbstractItemModel *itemModel)
    self.uglySide.call(
        'ritual_ZN24AbstractItemModelHandler16itemModelChangedEPK18QAbstrac'
        'tItemModel',
        self._addressOf(itemModel),
    )

  def resolveModel(self) -> None:
    """
    Calls Qt's 'void AbstractItemModelHandler::resolveModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractitemmodelhandler.html#resolveModel
    """
    #  void AbstractItemModelHandler::resolveModel()
    self.uglySide.call('ritual_ZN24AbstractItemModelHandler12resolveModelEv')

  @staticmethod
  def handleDataChanged(*__, **_) -> Never:
    """
    Qt's 'void AbstractItemModelHandler::handleDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'AbstractItemModelHandler.handleDataChanged' has no cute function "
        "yet. Qt's 'void AbstractItemModelHandler::handleDataChanged(const "
        "QModelIndex &topLeft, const QModelIndex &bottomRight, const "
        "QList<int> &roles)': takes a type Python has no way to hand over "
        "yet.")
