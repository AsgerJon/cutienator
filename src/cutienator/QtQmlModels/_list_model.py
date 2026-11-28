"""
ListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means ListModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import ListLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlListModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlListModel = WAIT['QQmlListModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ListModel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ListModel: a plain Python object standing in front of
  one C++ ListModel.

  What exists
  -----------

  Every function of Qt's ListModel that has a ritual and that Python can call
  so far, 6 names in all: 'updateTranslations', 'roleCount',
  'getExistingRole', 'elementCount', 'move', 'updateCacheIndices'. It can be
  made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  20 of the 27 functions Qt declares: 8 leans on 'ListLayout; 8 leans on
  'ListElement; 3 a template; 1 leans on 'ModelNodeMetaObject.

  What to expect
  --------------

  - The C++ ListModel is created at the first use, not by 'ListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ListModel.
  - Each name of Qt's ListModel that has no cute function yet, 'append',
    'appendElement', 'destroy', 'getListProperty', 'getOrCreateListRole',
    'getOrCreateModelObject', 'getProperty', 'insert', 'insertElement',
    'newElement', 'remove', 'resolveSubModel', 'set', 'setArrayLike',
    'setArrayLikeFast', 'setExistingProperty', 'setOrCreateProperty', 'sync',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside ListModel, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SetElement(CuteNum, scoped=True):
    """
    The enum 'ListModel::SetElement' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    WasJustInserted = Kee[int](0)
    IsCurrentlyUpdated = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def roleCount(self) -> int:
    """
    Calls Qt's 'int ListModel::roleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#roleCount
    """
    #  int ListModel::roleCount() const
    return self.uglySide.call('ritual_ZNK9ListModel9roleCountEv')

  @overload(int)
  def getExistingRole(self, index: int) -> ListLayout.Role:
    """
    Calls Qt's 'const ListLayout::Role &ListModel::getExistingRole(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#getExistingRole

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    ListLayout.Role
      A new cute ListLayout::Role around the copy Qt gave back. Python owns
      it.
    """
    #  const ListLayout::Role &ListModel::getExistingRole(int index) const
    address = self.uglySide.call(
        'ritual_ZNK9ListModel15getExistingRoleEi', index,
    )
    return ListLayout.Role._cuteOwning(address)

  def elementCount(self) -> int:
    """
    Calls Qt's 'int ListModel::elementCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#elementCount
    """
    #  int ListModel::elementCount() const
    return self.uglySide.call('ritual_ZNK9ListModel12elementCountEv')

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

  @overload(ListLayout, QQmlListModel)
  @overload(ListLayout, NoneType)
  @overload(NoneType, QQmlListModel)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      layout: Optional[ListLayout],
      modelCache: Optional[QQmlListModel],
  ) -> None:
    """
    Notes what was given, for Qt's 'ListModel::ListModel(ListLayout *layout,
    QQmlListModel *modelCache)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#ListModel

    Parameters
    ----------

    layout : Optional[ListLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    modelCache : Optional[QQmlListModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ListModel::ListModel(ListLayout *layout, QQmlListModel *modelCache)
    self._noteCreation(ListModel, lambda: Rituals.call(
        'ritual_ZN9ListModelC1EP10ListLayoutP13QQmlListModel',
        self._addressOf(layout), self._addressOf(modelCache),
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

  def updateTranslations(self) -> None:
    """
    Calls Qt's 'void ListModel::updateTranslations()'.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#updateTranslations
    """
    #  void ListModel::updateTranslations()
    self.uglySide.call('ritual_ZN9ListModel18updateTranslationsEv')

  @overload(int, int, int)
  def move(self, from_: int, to: int, n: int) -> None:
    """
    Calls Qt's 'void ListModel::move(int from, int to, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#move

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    n : int
      Passed on as it is.
    """
    #  void ListModel::move(int from, int to, int n)
    self.uglySide.call('ritual_ZN9ListModel4moveEiii', from_, to, n)

  @overload()
  @overload(int)
  @overload(int, int)
  def updateCacheIndices(self, start: int = 0, end: int = -1) -> None:
    """
    Calls Qt's 'void ListModel::updateCacheIndices(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/listmodel.html#updateCacheIndices

    Parameters
    ----------

    start : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    end : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void ListModel::updateCacheIndices(int start, int end)
    self.uglySide.call(
        'ritual_ZN9ListModel18updateCacheIndicesEii', start, end,
    )

  @staticmethod
  def append(*__, **_) -> Never:
    """
    Qt's 'int ListModel::append(QV4::Object *object)': leans on
    'ListLayout::getRoleOrCreate(QV4::String*, ListLayout::Role::DataType)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.append' has no cute function yet. Qt's 'int "
        "ListModel::append(QV4::Object *object)': leans on "
        "'ListLayout::getRoleOrCreate(QV4::String*, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def appendElement(*__, **_) -> Never:
    """
    Qt's 'int ListModel::appendElement()': leans on
    'ListElement::ListElement()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.appendElement' has no cute function yet. Qt's 'int "
        "ListModel::appendElement()': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def destroy(*__, **_) -> Never:
    """
    Qt's 'void ListModel::destroy()': leans on 'ListElement::ListElement()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.destroy' has no cute function yet. Qt's 'void "
        "ListModel::destroy()': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def getListProperty(*__, **_) -> Never:
    """
    Qt's 'ListModel *ListModel::getListProperty(int elementIndex, const
    ListLayout::Role &role)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.getListProperty' has no cute function yet. Qt's "
        "'ListModel *ListModel::getListProperty(int elementIndex, const "
        "ListLayout::Role &role)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def getOrCreateListRole(*__, **_) -> Never:
    """
    Qt's 'const ListLayout::Role &ListModel::getOrCreateListRole(const
    QString &name)': leans on 'ListLayout::getRoleOrCreate(QString const&,
    ListLayout::Role::DataType)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.getOrCreateListRole' has no cute function yet. Qt's "
        "'const ListLayout::Role &ListModel::getOrCreateListRole(const "
        "QString &name)': leans on 'ListLayout::getRoleOrCreate(QString "
        "const&, ListLayout::Role::DataType)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def getOrCreateModelObject(*__, **_) -> Never:
    """
    Qt's 'QObject *ListModel::getOrCreateModelObject(QQmlListModel *model,
    int elementIndex)': leans on
    'ModelNodeMetaObject::toDynamicMetaObject(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'ListModel.getOrCreateModelObject' has no cute function yet. Qt's "
        "'QObject *ListModel::getOrCreateModelObject(QQmlListModel *model, "
        "int elementIndex)': leans on "
        "'ModelNodeMetaObject::toDynamicMetaObject(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def getProperty(*__, **_) -> Never:
    """
    Qt's 'QVariant ListModel::getProperty(int elementIndex, int roleIndex,
    const QQmlListModel *owner, QV4::ExecutionEngine *eng)': leans on
    'ListElement::getProperty(ListLayout::Role const&, QQmlListModel const*,
    QV4::ExecutionEngine*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.getProperty' has no cute function yet. Qt's 'QVariant "
        "ListModel::getProperty(int elementIndex, int roleIndex, const "
        "QQmlListModel *owner, QV4::ExecutionEngine *eng)': leans on "
        "'ListElement::getProperty(ListLayout::Role const&, QQmlListModel "
        "const*, QV4::ExecutionEngine*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    Qt's 'void ListModel::insert(int elementIndex, QV4::Object *object)':
    leans on 'ListLayout::getRoleOrCreate(QV4::String*,
    ListLayout::Role::DataType)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.insert' has no cute function yet. Qt's 'void "
        "ListModel::insert(int elementIndex, QV4::Object *object)': leans "
        "on 'ListLayout::getRoleOrCreate(QV4::String*, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def insertElement(*__, **_) -> Never:
    """
    Qt's 'void ListModel::insertElement(int index)': leans on
    'ListElement::ListElement()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.insertElement' has no cute function yet. Qt's 'void "
        "ListModel::insertElement(int index)': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def newElement(*__, **_) -> Never:
    """
    Qt's 'void ListModel::newElement(int index)': leans on
    'ListElement::ListElement()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.newElement' has no cute function yet. Qt's 'void "
        "ListModel::newElement(int index)': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    Qt's 'QList<std::function<void ()>> ListModel::remove(int index, int
    count)': leans on 'ListElement::ListElement()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.remove' has no cute function yet. Qt's "
        "'QList<std::function<void ()>> ListModel::remove(int index, int "
        "count)': leans on 'ListElement::ListElement()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def resolveSubModel(*__, **_) -> Never:
    """
    Qt's 'ListModel::resolveSubModel': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'ListModel.resolveSubModel' has no cute function yet. Qt's "
        "'ListModel::resolveSubModel': a template: a pattern and no single "
        "function.")

  @staticmethod
  def set(*__, **_) -> Never:
    """
    - Qt's 'void ListModel::set(int elementIndex, QV4::Object *object,
      QList<int> *roles)': leans on
      'ListLayout::getRoleOrCreate(QV4::String*,
      ListLayout::Role::DataType)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'void ListModel::set(int elementIndex, QV4::Object *object,
      SetElement reason)': leans on
      'ListLayout::getRoleOrCreate(QV4::String*,
      ListLayout::Role::DataType)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.set' has no cute function yet. Qt's 'void "
        "ListModel::set(int elementIndex, QV4::Object *object, QList<int> "
        "*roles)': leans on 'ListLayout::getRoleOrCreate(QV4::String*, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken. Qt's "
        "'void ListModel::set(int elementIndex, QV4::Object *object, "
        "SetElement reason)': leans on "
        "'ListLayout::getRoleOrCreate(QV4::String*, "
        "ListLayout::Role::DataType)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setArrayLike(*__, **_) -> Never:
    """
    Qt's 'ListModel::setArrayLike': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'ListModel.setArrayLike' has no cute function yet. Qt's "
        "'ListModel::setArrayLike': a template: a pattern and no single "
        "function.")

  @staticmethod
  def setArrayLikeFast(*__, **_) -> Never:
    """
    Qt's 'ListModel::setArrayLikeFast': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'ListModel.setArrayLikeFast' has no cute function yet. Qt's "
        "'ListModel::setArrayLikeFast': a template: a pattern and no single "
        "function.")

  @staticmethod
  def setExistingProperty(*__, **_) -> Never:
    """
    Qt's 'int ListModel::setExistingProperty(int uid, const QString &key,
    const QV4::Value &data, QV4::ExecutionEngine *eng)': leans on
    'ListLayout::getExistingRole(QString const&) const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'ListModel.setExistingProperty' has no cute function yet. Qt's "
        "'int ListModel::setExistingProperty(int uid, const QString &key, "
        "const QV4::Value &data, QV4::ExecutionEngine *eng)': leans on "
        "'ListLayout::getExistingRole(QString const&) const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setOrCreateProperty(*__, **_) -> Never:
    """
    Qt's 'int ListModel::setOrCreateProperty(int elementIndex, const QString
    &key, const QVariant &data)': leans on
    'ListLayout::getRoleOrCreate(QString const&, QVariant const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.setOrCreateProperty' has no cute function yet. Qt's "
        "'int ListModel::setOrCreateProperty(int elementIndex, const "
        "QString &key, const QVariant &data)': leans on "
        "'ListLayout::getRoleOrCreate(QString const&, QVariant const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'bool ListModel::sync(ListModel *src, ListModel *target)': leans on
    'ListElement::getProperty(ListLayout::Role const&, QQmlListModel const*,
    QV4::ExecutionEngine*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListModel.sync' has no cute function yet. Qt's 'bool "
        "ListModel::sync(ListModel *src, ListModel *target)': leans on "
        "'ListElement::getProperty(ListLayout::Role const&, QQmlListModel "
        "const*, QV4::ExecutionEngine*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
