"""
QAbstractItemModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractItemModelPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QHash, QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractItemModel, QByteArray, QModelIndex
  from . import QPersistentModelIndexData, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QModelIndex = WAIT['QModelIndex']
  QPersistentModelIndexData = WAIT['QPersistentModelIndexData']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemModelPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractItemModelPrivate: a plain Python object
  standing in front of one C++ QAbstractItemModelPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstractItemModelPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemModelPrivate that has a ritual and that
  Python can call so far, 23 names in all: 'q_func', 'get',
  'removePersistentIndexData', 'movePersistentIndexes',
  'rowsAboutToBeInserted', 'rowsInserted', 'rowsAboutToBeRemoved',
  'rowsRemoved', 'columnsAboutToBeInserted', 'columnsInserted',
  'columnsAboutToBeRemoved', 'columnsRemoved', 'staticEmptyModel',
  'variantLessThan', 'itemsAboutToBeMoved', 'itemsMoved', 'allowMove',
  'executePendingOperations', 'createIndex', 'indexValid',
  'invalidatePersistentIndexes', 'invalidatePersistentIndex',
  'defaultRoleNames'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractItemModel *QAbstractItemModelPrivate::q_func()
    const': takes in Python what 'QAbstractItemModel
    *QAbstractItemModelPrivate::q_func()' takes.
  - Qt's 'QAbstractItemModelPrivate::~QAbstractItemModelPrivate()': the
    destructor: Python never removes a C++ QAbstractItemModelPrivate.
  - Qt's 'bool QAbstractItemModelPrivate::dropOnItem(const QModelIndex
    &index, QDataStream &stream)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QModelIndex QAbstractItemModelPrivate::createIndex(int row, int
    column, void *data) const': names 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAbstractItemModelPrivate is created at the first use, not by
    'QAbstractItemModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemModelPrivate.
  - Each name of Qt's QAbstractItemModelPrivate that has no cute function
    yet, 'dropOnItem', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QAbstractItemModelPrivate, each a class in
  #  here as in C++.

  class Change(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractItemModelPrivate::Change: a plain Python
    object standing in front of one C++ QAbstractItemModelPrivate::Change.

    C++ hands a QAbstractItemModelPrivate::Change around as a copy, so every
    C++ QAbstractItemModelPrivate::Change behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QAbstractItemModelPrivate::Change that has a
    ritual and that Python can call so far, 1 name in all: 'isValid'. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractItemModelPrivate::Change::~Change()': the destructor:
      Python removes its C++ QAbstractItemModelPrivate::Change by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QAbstractItemModelPrivate::Change is created at the first use,
      not by 'QAbstractItemModelPrivate::Change(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractItemModelPrivate::Change back gives a copy
      the ritual made for Python, in a new cute
      QAbstractItemModelPrivate::Change.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QModelIndex = WAIT['QModelIndex']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractItemModelPrivate::Change'

    #  Qt's '~QAbstractItemModelPrivate::Change()'. Naming it makes this a
    #  value class: Python owns every C++ QAbstractItemModelPrivate::Change
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QAbstractItemModelPrivate6ChangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QAbstractItemModelPrivate::Change::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractitemmodelprivate-change.html#isValid
      """
      #  bool QAbstractItemModelPrivate::Change::isValid() const
      return self.uglySide.call(
          'ritual_ZNK25QAbstractItemModelPrivate6Change7isValidEv',
      )

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractItemModelPrivate::Change::Change()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractitemmodelprivate-change.html#Change
      """
      #  QAbstractItemModelPrivate::Change::Change()
      self._noteCreation(
          QAbstractItemModelPrivate.Change, lambda: Rituals.call(
              'ritual_ZN25QAbstractItemModelPrivate6ChangeC1Ev',
          ))

    @overload(QModelIndex, int, int)
    def __init__(self, p: QModelIndex, f: int, l: int) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractItemModelPrivate::Change::Change(const QModelIndex &p, int f,
      int l)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractitemmodelprivate-change.html#Change

      Parameters
      ----------

      p : QModelIndex
        Passed on as a value: Qt reads the C++ QModelIndex, which stays
        Python's own.

      f : int
        Passed on as it is.

      l : int
        Passed on as it is.
      """
      #  QAbstractItemModelPrivate::Change::Change(const QModelIndex &p, int
      #      f, int l)
      self._noteCreation(
          QAbstractItemModelPrivate.Change, lambda: Rituals.call(
              'ritual_ZN25QAbstractItemModelPrivate6ChangeC1ERK11QModelInde'
              'xii',
              self._valueOf(p), f, l,
          ))

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

  class Persistent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractItemModelPrivate::Persistent: a plain
    Python object standing in front of one C++
    QAbstractItemModelPrivate::Persistent.

    C++ hands a QAbstractItemModelPrivate::Persistent around as a copy, so
    every C++ QAbstractItemModelPrivate::Persistent behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QAbstractItemModelPrivate::Persistent that has a
    ritual and that Python can call so far, 1 name in all:
    'insertMultiAtEnd'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractItemModelPrivate::Persistent::~Persistent()': the
      destructor: Python removes its C++
      QAbstractItemModelPrivate::Persistent by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QAbstractItemModelPrivate::Persistent is created at the first
      use, not by 'QAbstractItemModelPrivate::Persistent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractItemModelPrivate::Persistent back gives a
      copy the ritual made for Python, in a new cute
      QAbstractItemModelPrivate::Persistent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QModelIndex = WAIT['QModelIndex']
      QPersistentModelIndexData = WAIT['QPersistentModelIndexData']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractItemModelPrivate::Persistent'

    #  Qt's '~QAbstractItemModelPrivate::Persistent()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QAbstractItemModelPrivate::Persistent behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QAbstractItemModelPrivate10PersistentD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractItemModelPrivate::Persistent::Persistent()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractitemmodelprivate-persistent.html
      """
      #  QAbstractItemModelPrivate::Persistent::Persistent()
      self._noteCreation(
          QAbstractItemModelPrivate.Persistent, lambda: Rituals.call(
              'ritual_ZN25QAbstractItemModelPrivate10PersistentC1Ev',
          ))

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

    @overload(QModelIndex, QPersistentModelIndexData)
    @overload(QModelIndex, NoneType)
    def insertMultiAtEnd(
        self,
        key: QModelIndex,
        data: Optional[QPersistentModelIndexData],
    ) -> None:
      """
      Calls Qt's 'void
      QAbstractItemModelPrivate::Persistent::insertMultiAtEnd(const
      QModelIndex &key, QPersistentModelIndexData *data)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractitemmodelprivate-persistent.html

      Parameters
      ----------

      key : QModelIndex
        Passed on as a value: Qt reads the C++ QModelIndex, which stays
        Python's own.

      data : Optional[QPersistentModelIndexData]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QAbstractItemModelPrivate::Persistent::insertMultiAtEnd(const
      #      QModelIndex &key, QPersistentModelIndexData *data)
      self.uglySide.call(
          'ritual_ZN25QAbstractItemModelPrivate10Persistent16insertMultiAtE'
          'ndERK11QModelIndexP25QPersistentModelIndexData',
          self._valueOf(key), self._addressOf(data),
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAbstractItemModel)
  @overload(NoneType)
  def get(
      model: Optional[QAbstractItemModel],
  ) -> Optional[QAbstractItemModelPrivate]:
    """
    Calls Qt's 'const QAbstractItemModelPrivate
    *QAbstractItemModelPrivate::get(const QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#get

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractItemModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModelPrivate *QAbstractItemModelPrivate::get(const
    #      QAbstractItemModel *model)
    address = Rituals.call(
        'ritual_ZN25QAbstractItemModelPrivate3getEPK18QAbstractItemModel',
        CuteMixin._addressOf(model),
    )
    return QAbstractItemModelPrivate._cuteAt(address)

  @staticmethod
  def staticEmptyModel() -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel
    *QAbstractItemModelPrivate::staticEmptyModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#staticEmptyModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QAbstractItemModelPrivate::staticEmptyModel()
    address = Rituals.call(
        'ritual_ZN25QAbstractItemModelPrivate16staticEmptyModelEv',
    )
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  @staticmethod
  @overload(QVariant, QVariant)
  def variantLessThan(v1: QVariant, v2: QVariant) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModelPrivate::variantLessThan(const
    QVariant &v1, const QVariant &v2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#variantLessThan

    Parameters
    ----------

    v1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    v2 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QAbstractItemModelPrivate::variantLessThan(const QVariant &v1,
    #      const QVariant &v2)
    return Rituals.call(
        'ritual_ZN25QAbstractItemModelPrivate15variantLessThanERK8QVariantS'
        '2_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  @staticmethod
  def defaultRoleNames() -> QHash[int, QByteArray]:
    """
    Calls Qt's 'const QHash<int, QByteArray>
    &QAbstractItemModelPrivate::defaultRoleNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#defaultRoleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  const QHash<int, QByteArray>
    #      &QAbstractItemModelPrivate::defaultRoleNames()
    address = Rituals.call(
        'ritual_ZN25QAbstractItemModelPrivate16defaultRoleNamesEv',
    )
    from . import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemModelPrivate'

  #  A C++ QAbstractItemModelPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemModelPrivate'

  #  The functions Qt calls itself that QAbstractItemModelPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'executePendingOperations': (
          ('_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv',
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

  @overload(int, int, int)
  def createIndex(self, row: int, column: int, id: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemModelPrivate::createIndex(int row,
    int column, int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#createIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    id : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemModelPrivate::createIndex(int row, int
    #      column, int id) const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelPrivate11createIndexEiii',
        row, column, id,
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def indexValid(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModelPrivate::indexValid(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#indexValid

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemModelPrivate::indexValid(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractItemModelPrivate10indexValidERK11QModelIndex',
        self._valueOf(index),
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
    'QAbstractItemModelPrivate::QAbstractItemModelPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html
    """
    #  QAbstractItemModelPrivate::QAbstractItemModelPrivate()
    self._noteCreation(QAbstractItemModelPrivate, lambda: Rituals.call(
        'ritual_ZN25QAbstractItemModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QAbstractItemModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#q_func

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QAbstractItemModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate6q_funcEv',
    )
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  @overload(QPersistentModelIndexData)
  @overload(NoneType)
  def removePersistentIndexData(
      self,
      data: Optional[QPersistentModelIndexData],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::removePersistentIndexData(
    QPersistentModelIndexData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    data : Optional[QPersistentModelIndexData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemModelPrivate::removePersistentIndexData(
    #      QPersistentModelIndexData *data)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate25removePersistentIndexDataEP2'
        '5QPersistentModelIndexData',
        self._addressOf(data),
    )

  @overload(
      QList[QPersistentModelIndexData], int, QModelIndex, Qt.Orientation,
  )
  def movePersistentIndexes(
      self,
      indexes: QList[QPersistentModelIndexData],
      change: int,
      parent: QModelIndex,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::movePersistentIndexes(const
    QList<QPersistentModelIndexData *> &indexes, int change, const
    QModelIndex &parent, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    indexes : QList[QPersistentModelIndexData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    change : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QAbstractItemModelPrivate::movePersistentIndexes(const
    #      QList<QPersistentModelIndexData *> &indexes, int change, const
    #      QModelIndex &parent, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate21movePersistentIndexesERK5QLi'
        'stIP25QPersistentModelIndexDataEiRK11QModelIndexN2Qt11OrientationE',
        self._valueOf(indexes), change, self._valueOf(parent),
        orientation.value,
    )

  @overload(QModelIndex, int, int)
  def rowsAboutToBeInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::rowsAboutToBeInserted(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::rowsAboutToBeInserted(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate21rowsAboutToBeInsertedERK11QM'
        'odelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def rowsInserted(self, parent: QModelIndex, first: int, last: int) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::rowsInserted(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#rowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::rowsInserted(const QModelIndex
    #      &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate12rowsInsertedERK11QModelIndex'
        'ii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def rowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::rowsAboutToBeRemoved(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::rowsAboutToBeRemoved(const QModelIndex
    #      &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate20rowsAboutToBeRemovedERK11QMo'
        'delIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def rowsRemoved(self, parent: QModelIndex, first: int, last: int) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::rowsRemoved(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#rowsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::rowsRemoved(const QModelIndex &parent,
    #      int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate11rowsRemovedERK11QModelIndexi'
        'i',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def columnsAboutToBeInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelPrivate::columnsAboutToBeInserted(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::columnsAboutToBeInserted(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate24columnsAboutToBeInsertedERK1'
        '1QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def columnsInserted(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::columnsInserted(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#columnsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::columnsInserted(const QModelIndex
    #      &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate15columnsInsertedERK11QModelIn'
        'dexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def columnsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::columnsAboutToBeRemoved(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::columnsAboutToBeRemoved(const
    #      QModelIndex &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate23columnsAboutToBeRemovedERK11'
        'QModelIndexii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int)
  def columnsRemoved(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::columnsRemoved(const
    QModelIndex &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#columnsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QAbstractItemModelPrivate::columnsRemoved(const QModelIndex
    #      &parent, int first, int last)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate14columnsRemovedERK11QModelInd'
        'exii',
        self._valueOf(parent), first, last,
    )

  @overload(QModelIndex, int, int, QModelIndex, int, Qt.Orientation)
  def itemsAboutToBeMoved(
      self,
      srcParent: QModelIndex,
      srcFirst: int,
      srcLast: int,
      destinationParent: QModelIndex,
      destinationChild: int,
      a5: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::itemsAboutToBeMoved(const
    QModelIndex &srcParent, int srcFirst, int srcLast, const QModelIndex
    &destinationParent, int destinationChild, Qt::Orientation a5)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#itemsAboutToBeMoved

    Parameters
    ----------

    srcParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    srcFirst : int
      Passed on as it is.

    srcLast : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.

    a5 : Qt.Orientation
      Passed on as its number.
    """
    #  void QAbstractItemModelPrivate::itemsAboutToBeMoved(const QModelIndex
    #      &srcParent, int srcFirst, int srcLast, const QModelIndex
    #      &destinationParent, int destinationChild, Qt::Orientation a5)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate19itemsAboutToBeMovedERK11QMod'
        'elIndexiiS2_iN2Qt11OrientationE',
        self._valueOf(srcParent), srcFirst, srcLast,
        self._valueOf(destinationParent), destinationChild, a5.value,
    )

  @overload(QModelIndex, int, int, QModelIndex, int, Qt.Orientation)
  def itemsMoved(
      self,
      srcParent: QModelIndex,
      srcFirst: int,
      srcLast: int,
      destinationParent: QModelIndex,
      destinationChild: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::itemsMoved(const QModelIndex
    &srcParent, int srcFirst, int srcLast, const QModelIndex
    &destinationParent, int destinationChild, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#itemsMoved

    Parameters
    ----------

    srcParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    srcFirst : int
      Passed on as it is.

    srcLast : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QAbstractItemModelPrivate::itemsMoved(const QModelIndex
    #      &srcParent, int srcFirst, int srcLast, const QModelIndex
    #      &destinationParent, int destinationChild, Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate10itemsMovedERK11QModelIndexii'
        'S2_iN2Qt11OrientationE',
        self._valueOf(srcParent), srcFirst, srcLast,
        self._valueOf(destinationParent), destinationChild,
        orientation.value,
    )

  @overload(QModelIndex, int, int, QModelIndex, int, Qt.Orientation)
  def allowMove(
      self,
      srcParent: QModelIndex,
      srcFirst: int,
      srcLast: int,
      destinationParent: QModelIndex,
      destinationChild: int,
      orientation: Qt.Orientation,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModelPrivate::allowMove(const QModelIndex
    &srcParent, int srcFirst, int srcLast, const QModelIndex
    &destinationParent, int destinationChild, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html#allowMove

    Parameters
    ----------

    srcParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    srcFirst : int
      Passed on as it is.

    srcLast : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  bool QAbstractItemModelPrivate::allowMove(const QModelIndex
    #      &srcParent, int srcFirst, int srcLast, const QModelIndex
    #      &destinationParent, int destinationChild, Qt::Orientation
    #      orientation)
    return self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate9allowMoveERK11QModelIndexiiS2'
        '_iN2Qt11OrientationE',
        self._valueOf(srcParent), srcFirst, srcLast,
        self._valueOf(destinationParent), destinationChild,
        orientation.value,
    )

  def executePendingOperations(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModelPrivate::executePendingOperations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html
    """
    #  void QAbstractItemModelPrivate::executePendingOperations() const
    ritual = (
        'ritual_ZNK25QAbstractItemModelPrivate24executePendingOperationsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QAbstractItemModelPrivate24executePendingOperati'
          'onsEv')
    self.uglySide.call(ritual)

  def invalidatePersistentIndexes(self) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelPrivate::invalidatePersistentIndexes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html
    """
    #  void QAbstractItemModelPrivate::invalidatePersistentIndexes()
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate27invalidatePersistentIndexesE'
        'v',
    )

  @overload(QModelIndex)
  def invalidatePersistentIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void
    QAbstractItemModelPrivate::invalidatePersistentIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodelprivate.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemModelPrivate::invalidatePersistentIndex(const
    #      QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN25QAbstractItemModelPrivate25invalidatePersistentIndexERK'
        '11QModelIndex',
        self._valueOf(index),
    )

  @staticmethod
  def dropOnItem(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractItemModelPrivate::dropOnItem(const QModelIndex
    &index, QDataStream &stream)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemModelPrivate.dropOnItem' has no cute function yet. "
        "Qt's 'bool QAbstractItemModelPrivate::dropOnItem(const QModelIndex "
        "&index, QDataStream &stream)': takes a type Python has no way to "
        "hand over yet.")
