"""
QQmlInstanceModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlobjectmodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlInstanceModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlIncubator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QByteArray, QMetaObject, QVariant
  from . import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlInstanceModel(QObject):
  """
  The cute side of Qt's QQmlInstanceModel: a plain Python object standing in
  front of one C++ QQmlInstanceModel.

  It is built on the cute 'QObject', as Qt's QQmlInstanceModel is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlInstanceModel that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'count', 'isValid',
  'object', 'release', 'cancel', 'stringValue', 'variantValue',
  'setWatchedRoles', 'incubationStatus', 'drainReusableItemsPool',
  'poolSize', 'indexOf', 'abstractItemModel', 'setRequiredProperty',
  'countChanged', 'modelUpdated', 'createdItem', 'initItem',
  'updateItemProperties', 'destroyingItem', 'itemPooled', 'itemReused'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlInstanceModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlInstanceModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlInstanceModel::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  5 of the 32 functions Qt declares: 2 not a gap; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QQmlInstanceModel is created at the first use, not by
    'QQmlInstanceModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlInstanceModel.
  - Qt tells when it has removed the C++ QQmlInstanceModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlInstanceModel that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQmlInstanceModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ReleaseFlag(CuteFlags):
    """
    The flags enum 'QQmlInstanceModel::ReleaseFlag' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QQmlInstanceModel::ReleaseFlags'.
    """

    Referenced = 0x1
    Destroyed = 0x2
    Pooled = 0x4

  ReleaseFlags = ReleaseFlag

  class ReusableFlag(CuteNum):
    """
    The enum 'QQmlInstanceModel::ReusableFlag' of Qt, with the 2 names Qt
    gives in it.
    """

    NotReusable = Kee[int](0)
    Reusable = Kee[int](1)

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
    Calls Qt's 'QString QQmlInstanceModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#tr

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
    #  QString QQmlInstanceModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQmlInstanceModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInstanceModel'

  #  The functions Qt calls itself that QQmlInstanceModel is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setWatchedRoles': (
          'void QQmlInstanceModel::setWatchedRoles(const QList<QByteArray> '
          '&)',
      ),
  }

  #  The functions Qt calls itself that QQmlInstanceModel is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'count': (
          ('_ZNK17QQmlInstanceModel5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'isValid': (
          ('_ZNK17QQmlInstanceModel7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'object': (
          ('_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationMode'
           'E',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtQml:QQmlIncubator.IncubationMode'),
           )),
      ),
      'release': (
          ('_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE',
           ('int', 'flags', 'QtQmlModels:QQmlInstanceModel.ReleaseFlag'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('int', 'enum', 'QtQmlModels:QQmlInstanceModel.ReusableFlag'),
           )),
      ),
      'cancel': (
          ('_ZN17QQmlInstanceModel6cancelEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'variantValue': (
          ('_ZN17QQmlInstanceModel12variantValueEiRK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'incubationStatus': (
          ('_ZN17QQmlInstanceModel16incubationStatusEi',
           ('int', 'enum', 'QtQml:QQmlIncubator.Status'),
           (
               ('int', 'number', ''),
           )),
      ),
      'drainReusableItemsPool': (
          ('_ZN17QQmlInstanceModel22drainReusableItemsPoolEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'poolSize': (
          ('_ZN17QQmlInstanceModel8poolSizeEv',
           ('int', 'number', ''),
           ()),
      ),
      'indexOf': (
          ('_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'abstractItemModel': (
          ('_ZNK17QQmlInstanceModel17abstractItemModelEv',
           ('address', 'address', 'QtCore:QAbstractItemModel'),
           ()),
      ),
      'setRequiredProperty': (
          ('_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QVari'
           'ant',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
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
    Calls Qt's 'const QMetaObject *QQmlInstanceModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlInstanceModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlInstanceModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlInstanceModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#count
    """
    #  int QQmlInstanceModel::count() const
    return self.uglySide.call('ritual_ZNK17QQmlInstanceModel5countEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlInstanceModel::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#isValid
    """
    #  bool QQmlInstanceModel::isValid() const
    return self.uglySide.call('ritual_ZNK17QQmlInstanceModel7isValidEv')

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def indexOf(
      self,
      object: Optional[QObject],
      objectContext: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'int QQmlInstanceModel::indexOf(QObject *object, QObject
    *objectContext) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#indexOf

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectContext : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlInstanceModel::indexOf(QObject *object, QObject
    #      *objectContext) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_',
        self._addressOf(object, 'QObject'), self._addressOf(objectContext,
        'QObject'),
    )

  def abstractItemModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel
    *QQmlInstanceModel::abstractItemModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#abstractItemModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QQmlInstanceModel::abstractItemModel() const
    ritual = 'ritual_ZNK17QQmlInstanceModel17abstractItemModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQmlInstanceModel17abstractItemModelEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QByteArray])
  def setWatchedRoles(self, roles: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::setWatchedRoles(const
    QList<QByteArray> &roles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#setWatchedRoles

    Parameters
    ----------

    roles : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlInstanceModel::setWatchedRoles(const QList<QByteArray>
    #      &roles)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel15setWatchedRolesERK5QListI10QByteArra'
        'yE',
        self._valueOf(roles),
    )

  @overload(int, str, QVariant)
  def setRequiredProperty(
      self,
      index: int,
      name: str,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlInstanceModel::setRequiredProperty(int index, const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#setRequiredProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlInstanceModel::setRequiredProperty(int index, const QString
    #      &name, const QVariant &value)
    ritual = (
        'ritual_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QV'
        'ariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStrin'
          'gRK8QVariant')
    return self.uglySide.call(ritual, index, name, self._valueOf(value))

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
    Qt's 'QQmlInstanceModel::QQmlInstanceModel(QObjectPrivate &dd, QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlInstanceModel.__init__' has no cute function yet. Qt's "
        "'QQmlInstanceModel::QQmlInstanceModel(QObjectPrivate &dd, QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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
  @overload(int, QQmlIncubator.IncubationMode)
  def object(
      self,
      index: int,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlInstanceModel::object(int index,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#object

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
    #  QObject *QQmlInstanceModel::object(int index,
    #      QQmlIncubator::IncubationMode incubationMode)
    address = self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationM'
        'odeE',
        index, incubationMode.value,
    )
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, ReusableFlag)
  @overload(NoneType, ReusableFlag)
  def release(
      self,
      object: Optional[QObject],
      reusableFlag: ReusableFlag = ReusableFlag.NotReusable,
  ) -> ReleaseFlags:
    """
    Calls Qt's 'ReleaseFlags QQmlInstanceModel::release(QObject *object,
    ReusableFlag reusableFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#release

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reusableFlag : ReusableFlag
      Passed on as its number. May be left out, as in Qt: it is then
      ReusableFlag.NotReusable.

    Returns
    -------

    ReleaseFlags
      The value standing for the combination Qt gave back.
    """
    #  ReleaseFlags QQmlInstanceModel::release(QObject *object, ReusableFlag
    #      reusableFlag)
    return QQmlInstanceModel.ReleaseFlags(self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE',
        self._addressOf(object, 'QObject'), reusableFlag.value,
    ))

  @overload(int)
  def cancel(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::cancel(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#cancel

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlInstanceModel::cancel(int a0)
    ritual = 'ritual_ZN17QQmlInstanceModel6cancelEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlInstanceModel6cancelEi'
    self.uglySide.call(ritual, a0)

  @overload(int, str)
  def stringValue(self, index: int, role: str) -> str:
    """
    Calls Qt's 'QString QQmlInstanceModel::stringValue(int index, const
    QString &role)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#stringValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    role : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlInstanceModel::stringValue(int index, const QString &role)
    return self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel11stringValueEiRK7QString', index, role,
    )

  @overload(int, str)
  def variantValue(self, a0: int, a1: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlInstanceModel::variantValue(int a0, const
    QString &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#variantValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlInstanceModel::variantValue(int a0, const QString &a1)
    address = self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel12variantValueEiRK7QString', a0, a1,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def incubationStatus(self, index: int) -> QQmlIncubator.Status:
    """
    Calls Qt's 'QQmlIncubator::Status QQmlInstanceModel::incubationStatus(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#incubationStatus

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
    #  QQmlIncubator::Status QQmlInstanceModel::incubationStatus(int index)
    return QQmlIncubator.Status(self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel16incubationStatusEi', index,
    ))

  @overload(int)
  def drainReusableItemsPool(self, maxPoolTime: int) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::drainReusableItemsPool(int
    maxPoolTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#drainReusableItemsPool

    Parameters
    ----------

    maxPoolTime : int
      Passed on as it is.
    """
    #  void QQmlInstanceModel::drainReusableItemsPool(int maxPoolTime)
    ritual = 'ritual_ZN17QQmlInstanceModel22drainReusableItemsPoolEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlInstanceModel22drainReusableItemsPoolEi'
    self.uglySide.call(ritual, maxPoolTime)

  def poolSize(self) -> int:
    """
    Calls Qt's 'int QQmlInstanceModel::poolSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#poolSize
    """
    #  int QQmlInstanceModel::poolSize()
    ritual = 'ritual_ZN17QQmlInstanceModel8poolSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlInstanceModel8poolSizeEv'
    return self.uglySide.call(ritual)

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#countChanged
    """
    #  void QQmlInstanceModel::countChanged()
    self.uglySide.call('ritual_ZN17QQmlInstanceModel12countChangedEv')

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::modelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQmlInstanceModel::modelUpdated(const QQmlChangeSet &changeSet,
    #      bool reset)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel12modelUpdatedERK13QQmlChangeSetb',
        self._valueOf(changeSet), reset,
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def createdItem(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::createdItem(int index, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#createdItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstanceModel::createdItem(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel11createdItemEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::initItem(int index, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#initItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstanceModel::initItem(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel8initItemEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject, bool)
  @overload(int, NoneType, bool)
  def updateItemProperties(
      self,
      index: int,
      object: Optional[QObject],
      init: bool,
  ) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::updateItemProperties(int index,
    QObject *object, bool init)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#updateItemProperties

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    init : bool
      Passed on as it is.
    """
    #  void QQmlInstanceModel::updateItemProperties(int index, QObject
    #      *object, bool init)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel20updateItemPropertiesEiP7QObjectb',
        index, self._addressOf(object, 'QObject'), init,
    )

  @overload(QObject)
  @overload(NoneType)
  def destroyingItem(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::destroyingItem(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstancemodel.html#destroyingItem

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstanceModel::destroyingItem(QObject *object)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel14destroyingItemEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def itemPooled(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::itemPooled(int index, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#itemPooled

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstanceModel::itemPooled(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel10itemPooledEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def itemReused(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstanceModel::itemReused(int index, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstancemodel.html#itemReused

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstanceModel::itemReused(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN17QQmlInstanceModel10itemReusedEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )
