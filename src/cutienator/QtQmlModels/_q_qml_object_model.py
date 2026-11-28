"""
QQmlObjectModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlobjectmodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlObjectModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlIncubator
from . import QQmlInstanceModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QQmlObjectModelAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlObjectModel(QQmlInstanceModel):
  """
  The cute side of Qt's QQmlObjectModel: a plain Python object standing in
  front of one C++ QQmlObjectModel.

  It is built on the cute 'QQmlInstanceModel', as Qt's QQmlObjectModel is
  built on Qt's QQmlInstanceModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlObjectModel that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'count', 'isValid',
  'object', 'release', 'variantValue', 'setWatchedRoles', 'incubationStatus',
  'indexOf', 'qmlAttachedProperties', 'get', 'append', 'insert', 'move',
  'remove', 'clear', 'childrenChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlObjectModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlObjectModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlObjectModelPrivate *QQmlObjectModel::d_func()': gives
    'QQmlObjectModelPrivate', which has no cute class yet.
  - Qt's 'const QQmlObjectModelPrivate *QQmlObjectModel::d_func() const':
    gives 'QQmlObjectModelPrivate', which has no cute class yet.
  - Qt's 'void QQmlObjectModel::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQmlObjectModel::~QQmlObjectModel()': the destructor: Python never
    removes a C++ QQmlObjectModel.
  - Qt's 'QQmlListProperty<QObject> QQmlObjectModel::children()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlObjectModel is created at the first use, not by
    'QQmlObjectModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlObjectModel.
  - Qt tells when it has removed the C++ QQmlObjectModel. Every call on the
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
    Calls Qt's 'QString QQmlObjectModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#tr

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
    #  QString QQmlObjectModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlObjectModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQmlObjectModelAttached]:
    """
    Calls Qt's 'QQmlObjectModelAttached
    *QQmlObjectModel::qmlAttachedProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectmodel.html#qmlAttachedProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlObjectModelAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlObjectModelAttached
    #      *QQmlObjectModel::qmlAttachedProperties(QObject *obj)
    address = Rituals.call(
        'ritual_ZN15QQmlObjectModel21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    from . import QQmlObjectModelAttached
    return QQmlObjectModelAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlObjectModel'

  #  A C++ QQmlObjectModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlObjectModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlObjectModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlObjectModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlObjectModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlObjectModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#count
    """
    #  int QQmlObjectModel::count() const
    ritual = 'ritual_ZNK15QQmlObjectModel5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQmlObjectModel5countEv'
    return self.uglySide.call(ritual)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlObjectModel::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#isValid
    """
    #  bool QQmlObjectModel::isValid() const
    ritual = 'ritual_ZNK15QQmlObjectModel7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQmlObjectModel7isValidEv'
    return self.uglySide.call(ritual)

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
    Calls Qt's 'int QQmlObjectModel::indexOf(QObject *object, QObject
    *objectContext) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#indexOf

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectContext : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlObjectModel::indexOf(QObject *object, QObject *objectContext)
    #      const
    ritual = 'ritual_ZNK15QQmlObjectModel7indexOfEP7QObjectS1_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQmlObjectModel7indexOfEP7QObjectS1_'
    return self.uglySide.call(
        ritual,
        self._addressOf(object, 'QObject'), self._addressOf(objectContext,
        'QObject'),
    )

  @overload(int)
  def get(self, index: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectModel::get(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectModel::get(int index) const
    address = self.uglySide.call('ritual_ZNK15QQmlObjectModel3getEi', index)
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QByteArray])
  def setWatchedRoles(self, a0: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::setWatchedRoles(const QList<QByteArray>
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectmodel.html#setWatchedRoles

    Parameters
    ----------

    a0 : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlObjectModel::setWatchedRoles(const QList<QByteArray> &a0)
    self.uglySide.call(
        'ritual_ZN15QQmlObjectModel15setWatchedRolesERK5QListI10QByteArrayE',
        self._valueOf(a0),
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
    Notes what was given, for Qt's 'QQmlObjectModel::QQmlObjectModel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectmodel.html#QQmlObjectModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlObjectModel::QQmlObjectModel(QObject *parent)
    self._noteCreation(QQmlObjectModel, lambda: Rituals.call(
        'ritual_ZN15QQmlObjectModelC1EP7QObject',
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
  @overload(int, QQmlIncubator.IncubationMode)
  def object(
      self,
      index: int,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectModel::object(int index,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#object

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
    #  QObject *QQmlObjectModel::object(int index,
    #      QQmlIncubator::IncubationMode incubationMode)
    ritual = (
        'ritual_ZN15QQmlObjectModel6objectEiN13QQmlIncubator14IncubationMod'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQmlObjectModel6objectEiN13QQmlIncubator14Incubat'
          'ionModeE')
    address = self.uglySide.call(ritual, index, incubationMode.value)
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QQmlInstanceModel.ReusableFlag)
  @overload(NoneType, QQmlInstanceModel.ReusableFlag)
  def release(
      self,
      object: Optional[QObject],
      reusable: QQmlInstanceModel.ReusableFlag = (
          QQmlInstanceModel.ReusableFlag.NotReusable),
  ) -> QQmlInstanceModel.ReleaseFlags:
    """
    Calls Qt's 'ReleaseFlags QQmlObjectModel::release(QObject *object,
    ReusableFlag reusable)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#release

    Parameters
    ----------

    object : Optional[QObject]
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
    #  ReleaseFlags QQmlObjectModel::release(QObject *object, ReusableFlag
    #      reusable)
    ritual = (
        'ritual_ZN15QQmlObjectModel7releaseEP7QObjectN17QQmlInstanceModel12'
        'ReusableFlagE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQmlObjectModel7releaseEP7QObjectN17QQmlInstanceM'
          'odel12ReusableFlagE')
    return QQmlInstanceModel.ReleaseFlags(self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), reusable.value,
    ))

  @overload(int, str)
  def variantValue(self, index: int, role: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlObjectModel::variantValue(int index, const
    QString &role)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#variantValue

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
    #  QVariant QQmlObjectModel::variantValue(int index, const QString &role)
    ritual = 'ritual_ZN15QQmlObjectModel12variantValueEiRK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlObjectModel12variantValueEiRK7QString'
    address = self.uglySide.call(ritual, index, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def incubationStatus(self, index: int) -> QQmlIncubator.Status:
    """
    Calls Qt's 'QQmlIncubator::Status QQmlObjectModel::incubationStatus(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectmodel.html#incubationStatus

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
    #  QQmlIncubator::Status QQmlObjectModel::incubationStatus(int index)
    ritual = 'ritual_ZN15QQmlObjectModel16incubationStatusEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlObjectModel16incubationStatusEi'
    return QQmlIncubator.Status(self.uglySide.call(ritual, index))

  @overload(QObject)
  @overload(NoneType)
  def append(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::append(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#append

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectModel::append(QObject *object)
    self.uglySide.call(
        'ritual_ZN15QQmlObjectModel6appendEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def insert(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::insert(int index, QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectModel::insert(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN15QQmlObjectModel6insertEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, int)
  @overload(int, int, int)
  def move(self, from_: int, to: int, n: int = 1) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::move(int from, int to, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#move

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QQmlObjectModel::move(int from, int to, int n)
    self.uglySide.call('ritual_ZN15QQmlObjectModel4moveEiii', from_, to, n)

  @overload(int)
  @overload(int, int)
  def remove(self, index: int, n: int = 1) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::remove(int index, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QQmlObjectModel::remove(int index, int n)
    self.uglySide.call('ritual_ZN15QQmlObjectModel6removeEii', index, n)

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectmodel.html#clear
    """
    #  void QQmlObjectModel::clear()
    self.uglySide.call('ritual_ZN15QQmlObjectModel5clearEv')

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void QQmlObjectModel::childrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectmodel.html#childrenChanged
    """
    #  void QQmlObjectModel::childrenChanged()
    self.uglySide.call('ritual_ZN15QQmlObjectModel15childrenChangedEv')
