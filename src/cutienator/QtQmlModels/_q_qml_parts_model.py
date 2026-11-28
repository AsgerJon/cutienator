"""
QQmlPartsModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPartsModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from ..QtQml import QQmlIncubator
from . import QQmlDelegateModelGroupEmitter, QQmlInstanceModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QQmlChangeSet, QQuickPackage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQuickPackage = WAIT['QQuickPackage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPartsModel(QQmlInstanceModel, QQmlDelegateModelGroupEmitter):
  """
  The cute side of Qt's QQmlPartsModel: a plain Python object standing in
  front of one C++ QQmlPartsModel.

  It is built on the cute 'QQmlInstanceModel', as Qt's QQmlPartsModel is
  built on Qt's QQmlInstanceModel, and has everything that class has. It is
  built on the cute 'QQmlDelegateModelGroupEmitter' as well, as Qt's
  QQmlPartsModel is built on Qt's QQmlDelegateModelGroupEmitter too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPartsModel that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'filterGroup',
  'updateFilterGroup', 'count', 'isValid', 'object', 'release',
  'variantValue', 'watchedRoles', 'setWatchedRoles', 'incubationStatus',
  'indexOf', 'emitModelUpdated', 'createdPackage', 'initPackage',
  'destroyingPackage', 'filterGroupChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlPartsModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlPartsModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlPartsModel::~QQmlPartsModel()': the destructor: Python never
    removes a C++ QQmlPartsModel.

  What has no ritual
  ------------------

  7 of the 27 functions Qt declares: 5 leans on 'QQmlPartsModel; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlPartsModel is created at the first use, not by
    'QQmlPartsModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPartsModel.
  - Qt tells when it has removed the C++ QQmlPartsModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlPartsModel that has no cute function yet,
    '__init__', 'resetFilterGroup', 'setFilterGroup', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPartsModel'

  #  Qt's QQmlPartsModel is built on more than one class. The part of a C++
  #  QQmlPartsModel that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlDelegateModelGroupEmitter':
          'ritual_cast_QQmlPartsModel_QQmlDelegateModelGroupEmitter',
  }

  #  A C++ QQmlPartsModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlPartsModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlPartsModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlPartsModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlPartsModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def filterGroup(self) -> str:
    """
    Calls Qt's 'QString QQmlPartsModel::filterGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#filterGroup

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPartsModel::filterGroup() const
    return self.uglySide.call('ritual_ZNK14QQmlPartsModel11filterGroupEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlPartsModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#count
    """
    #  int QQmlPartsModel::count() const
    ritual = 'ritual_ZNK14QQmlPartsModel5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlPartsModel5countEv'
    return self.uglySide.call(ritual)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlPartsModel::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#isValid
    """
    #  bool QQmlPartsModel::isValid() const
    ritual = 'ritual_ZNK14QQmlPartsModel7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlPartsModel7isValidEv'
    return self.uglySide.call(ritual)

  def watchedRoles(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QQmlPartsModel::watchedRoles() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#watchedRoles

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QQmlPartsModel::watchedRoles() const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlPartsModel12watchedRolesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def indexOf(
      self,
      item: Optional[QObject],
      objectContext: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'int QQmlPartsModel::indexOf(QObject *item, QObject
    *objectContext) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#indexOf

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectContext : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlPartsModel::indexOf(QObject *item, QObject *objectContext)
    #      const
    ritual = 'ritual_ZNK14QQmlPartsModel7indexOfEP7QObjectS1_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQmlPartsModel7indexOfEP7QObjectS1_'
    return self.uglySide.call(
        ritual,
        self._addressOf(item, 'QObject'), self._addressOf(objectContext,
        'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QByteArray])
  def setWatchedRoles(self, roles: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::setWatchedRoles(const QList<QByteArray>
    &roles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpartsmodel.html#setWatchedRoles

    Parameters
    ----------

    roles : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlPartsModel::setWatchedRoles(const QList<QByteArray> &roles)
    self.uglySide.call(
        'ritual_ZN14QQmlPartsModel15setWatchedRolesERK5QListI10QByteArrayE',
        self._valueOf(roles),
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
    Qt's 'QQmlPartsModel::QQmlPartsModel(QQmlDelegateModel *model, const
    QString &part, QObject *parent)': leans on
    'QQmlPartsModel::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlPartsModel.__init__' has no cute function yet. Qt's "
        "'QQmlPartsModel::QQmlPartsModel(QQmlDelegateModel *model, const "
        "QString &part, QObject *parent)': leans on "
        "'QQmlPartsModel::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def updateFilterGroup(self) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::updateFilterGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpartsmodel.html#updateFilterGroup
    """
    #  void QQmlPartsModel::updateFilterGroup()
    self.uglySide.call('ritual_ZN14QQmlPartsModel17updateFilterGroupEv')

  @overload(int)
  @overload(int, QQmlIncubator.IncubationMode)
  def object(
      self,
      index: int,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlPartsModel::object(int index,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#object

    Parameters
    ----------

    index : int
      Passed on as it is.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlIncubator.IncubationMode.AsynchronousIfNested.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlPartsModel::object(int index,
    #      QQmlIncubator::IncubationMode incubationMode)
    address = self.uglySide.call(
        'ritual_ZN14QQmlPartsModel6objectEiN13QQmlIncubator14IncubationMode'
        'E',
        index, incubationMode.value,
    )
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QQmlInstanceModel.ReusableFlag)
  @overload(NoneType, QQmlInstanceModel.ReusableFlag)
  def release(
      self,
      item: Optional[QObject],
      reusable: QQmlInstanceModel.ReusableFlag = (
          QQmlInstanceModel.ReusableFlag.NotReusable),
  ) -> QQmlInstanceModel.ReleaseFlags:
    """
    Calls Qt's 'ReleaseFlags QQmlPartsModel::release(QObject *item,
    ReusableFlag reusable)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#release

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reusable : QQmlInstanceModel.ReusableFlag
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlInstanceModel.ReusableFlag.NotReusable.

    Returns
    -------

    QQmlInstanceModel.ReleaseFlags
      The value standing for the combination Qt gave back.
    """
    #  ReleaseFlags QQmlPartsModel::release(QObject *item, ReusableFlag
    #      reusable)
    return QQmlInstanceModel.ReleaseFlags(self.uglySide.call(
        'ritual_ZN14QQmlPartsModel7releaseEP7QObjectN17QQmlInstanceModel12R'
        'eusableFlagE',
        self._addressOf(item, 'QObject'), reusable.value,
    ))

  @overload(int, str)
  def variantValue(self, index: int, role: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPartsModel::variantValue(int index, const
    QString &role)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#variantValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPartsModel::variantValue(int index, const QString &role)
    address = self.uglySide.call(
        'ritual_ZN14QQmlPartsModel12variantValueEiRK7QString', index, role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def incubationStatus(self, index: int) -> QQmlIncubator.Status:
    """
    Calls Qt's 'QQmlIncubator::Status QQmlPartsModel::incubationStatus(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpartsmodel.html#incubationStatus

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QQmlIncubator.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlIncubator.Status(number)' gives.
    """
    #  QQmlIncubator::Status QQmlPartsModel::incubationStatus(int index)
    return QQmlIncubator.Status(self.uglySide.call(
        'ritual_ZN14QQmlPartsModel16incubationStatusEi', index,
    ))

  @overload(QQmlChangeSet, bool)
  def emitModelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::emitModelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpartsmodel.html#emitModelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQmlPartsModel::emitModelUpdated(const QQmlChangeSet &changeSet,
    #      bool reset)
    self.uglySide.call(
        'ritual_ZN14QQmlPartsModel16emitModelUpdatedERK13QQmlChangeSetb',
        self._valueOf(changeSet), reset,
    )

  @overload(int, QQuickPackage)
  @overload(int, NoneType)
  def createdPackage(
      self,
      index: int,
      package: Optional[QQuickPackage],
  ) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::createdPackage(int index, QQuickPackage
    *package)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#createdPackage

    Parameters
    ----------

    index : int
      Passed on as it is.

    package : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPartsModel::createdPackage(int index, QQuickPackage *package)
    ritual = 'ritual_ZN14QQmlPartsModel14createdPackageEiP13QQuickPackage'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQmlPartsModel14createdPackageEiP13QQuickPackage')
    self.uglySide.call(ritual, index, self._addressOf(package))

  @overload(int, QQuickPackage)
  @overload(int, NoneType)
  def initPackage(
      self,
      index: int,
      package: Optional[QQuickPackage],
  ) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::initPackage(int index, QQuickPackage
    *package)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpartsmodel.html#initPackage

    Parameters
    ----------

    index : int
      Passed on as it is.

    package : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPartsModel::initPackage(int index, QQuickPackage *package)
    ritual = 'ritual_ZN14QQmlPartsModel11initPackageEiP13QQuickPackage'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQmlPartsModel11initPackageEiP13QQuickPackage'
    self.uglySide.call(ritual, index, self._addressOf(package))

  @overload(QQuickPackage)
  @overload(NoneType)
  def destroyingPackage(self, package: Optional[QQuickPackage]) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::destroyingPackage(QQuickPackage
    *package)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpartsmodel.html#destroyingPackage

    Parameters
    ----------

    package : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPartsModel::destroyingPackage(QQuickPackage *package)
    ritual = 'ritual_ZN14QQmlPartsModel17destroyingPackageEP13QQuickPackage'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQmlPartsModel17destroyingPackageEP13QQuickPackag'
          'e')
    self.uglySide.call(ritual, self._addressOf(package))

  def filterGroupChanged(self) -> None:
    """
    Calls Qt's 'void QQmlPartsModel::filterGroupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpartsmodel.html#filterGroupChanged
    """
    #  void QQmlPartsModel::filterGroupChanged()
    self.uglySide.call('ritual_ZN14QQmlPartsModel18filterGroupChangedEv')

  @staticmethod
  def resetFilterGroup(*__, **_) -> Never:
    """
    Qt's 'void QQmlPartsModel::resetFilterGroup()': leans on
    'QQmlPartsModel::filterGroupChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlPartsModel.resetFilterGroup' has no cute function yet. Qt's "
        "'void QQmlPartsModel::resetFilterGroup()': leans on "
        "'QQmlPartsModel::filterGroupChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setFilterGroup(*__, **_) -> Never:
    """
    Qt's 'void QQmlPartsModel::setFilterGroup(const QString &group)': leans
    on 'QQmlPartsModel::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlPartsModel.setFilterGroup' has no cute function yet. Qt's "
        "'void QQmlPartsModel::setFilterGroup(const QString &group)': leans "
        "on 'QQmlPartsModel::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
