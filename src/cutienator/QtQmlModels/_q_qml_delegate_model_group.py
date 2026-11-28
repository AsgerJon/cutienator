"""
QQmlDelegateModelGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelGroup to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QJSValue, QQmlV4Function
  from . import QQmlDelegateModel, QQmlDelegateModelGroupPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QQmlDelegateModel = WAIT['QQmlDelegateModel']
  QQmlV4Function = WAIT['QQmlV4Function']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelGroup(QObject):
  """
  The cute side of Qt's QQmlDelegateModelGroup: a plain Python object
  standing in front of one C++ QQmlDelegateModelGroup.

  It is built on the cute 'QObject', as Qt's QQmlDelegateModelGroup is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelGroup that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr', 'name',
  'setName', 'count', 'defaultInclude', 'setDefaultInclude', 'get', 'insert',
  'create', 'resolve', 'remove', 'addGroups', 'removeGroups', 'setGroups',
  'move', 'countChanged', 'nameChanged', 'defaultIncludeChanged', 'changed',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelegateModelGroup::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlDelegateModelGroup::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDelegateModelGroup::~QQmlDelegateModelGroup()': the destructor:
    Python never removes a C++ QQmlDelegateModelGroup.
  - Qt's 'const QQmlDelegateModelGroupPrivate
    *QQmlDelegateModelGroup::d_func() const': takes in Python what
    'QQmlDelegateModelGroupPrivate *QQmlDelegateModelGroup::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlDelegateModelGroup is created at the first use, not by
    'QQmlDelegateModelGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelGroup.
  - Qt tells when it has removed the C++ QQmlDelegateModelGroup. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlDelegateModelGroup::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#tr

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
    #  QString QQmlDelegateModelGroup::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQmlDelegateModelGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelGroup'

  #  A C++ QQmlDelegateModelGroup Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModelGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDelegateModelGroup::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelegateModelGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlDelegateModelGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlDelegateModelGroup::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDelegateModelGroup::name() const
    return self.uglySide.call('ritual_ZNK22QQmlDelegateModelGroup4nameEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelGroup::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#count
    """
    #  int QQmlDelegateModelGroup::count() const
    return self.uglySide.call('ritual_ZNK22QQmlDelegateModelGroup5countEv')

  def defaultInclude(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelGroup::defaultInclude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#defaultInclude
    """
    #  bool QQmlDelegateModelGroup::defaultInclude() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlDelegateModelGroup14defaultIncludeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::setName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDelegateModelGroup::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup7setNameERK7QString', name,
    )

  @overload(bool)
  def setDefaultInclude(self, include: bool) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::setDefaultInclude(bool
    include)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#setDefaultInclude

    Parameters
    ----------

    include : bool
      Passed on as it is.
    """
    #  void QQmlDelegateModelGroup::setDefaultInclude(bool include)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup17setDefaultIncludeEb', include,
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def setGroups(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::setGroups(QQmlV4FunctionPtr
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#setGroups

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::setGroups(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup9setGroupsEP14QQmlV4Function',
        self._addressOf(a0),
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
    'QQmlDelegateModelGroup::QQmlDelegateModelGroup(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#QQmlDelegateModelGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlDelegateModelGroup::QQmlDelegateModelGroup(QObject *parent)
    self._noteCreation(QQmlDelegateModelGroup, lambda: Rituals.call(
        'ritual_ZN22QQmlDelegateModelGroupC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QQmlDelegateModel, int)
  @overload(str, NoneType, int)
  @overload(str, QQmlDelegateModel, int, QObject)
  @overload(str, QQmlDelegateModel, int, NoneType)
  @overload(str, NoneType, int, QObject)
  @overload(str, NoneType, int, NoneType)
  def __init__(
      self,
      name: str,
      model: Optional[QQmlDelegateModel],
      compositorType: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelGroup::QQmlDelegateModelGroup(const QString &name,
    QQmlDelegateModel *model, int compositorType, QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#QQmlDelegateModelGroup

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    model : Optional[QQmlDelegateModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    compositorType : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlDelegateModelGroup::QQmlDelegateModelGroup(const QString &name,
    #      QQmlDelegateModel *model, int compositorType, QObject *parent)
    self._noteCreation(QQmlDelegateModelGroup, lambda: Rituals.call(
        'ritual_ZN22QQmlDelegateModelGroupC1ERK7QStringP17QQmlDelegateModel'
        'iP7QObject',
        name, self._addressOf(model), compositorType, self._addressOf(parent,
        'QObject'),
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
  def get(self, index: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlDelegateModelGroup::get(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlDelegateModelGroup::get(int index)
    address = self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup3getEi', index,
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def insert(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::insert(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#insert

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::insert(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup6insertEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def create(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::create(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#create

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::create(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup6createEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def resolve(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::resolve(QQmlV4FunctionPtr a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#resolve

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::resolve(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup7resolveEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def remove(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::remove(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#remove

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::remove(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup6removeEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def addGroups(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::addGroups(QQmlV4FunctionPtr
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#addGroups

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::addGroups(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup9addGroupsEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def removeGroups(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::removeGroups(QQmlV4FunctionPtr
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#removeGroups

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::removeGroups(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup12removeGroupsEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def move(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::move(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#move

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroup::move(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup4moveEP14QQmlV4Function',
        self._addressOf(a0),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#countChanged
    """
    #  void QQmlDelegateModelGroup::countChanged()
    self.uglySide.call('ritual_ZN22QQmlDelegateModelGroup12countChangedEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#nameChanged
    """
    #  void QQmlDelegateModelGroup::nameChanged()
    self.uglySide.call('ritual_ZN22QQmlDelegateModelGroup11nameChangedEv')

  def defaultIncludeChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::defaultIncludeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#defaultIncludeChanged
    """
    #  void QQmlDelegateModelGroup::defaultIncludeChanged()
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup21defaultIncludeChangedEv',
    )

  @overload(QJSValue, QJSValue)
  def changed(self, removed: QJSValue, inserted: QJSValue) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroup::changed(const QJSValue &removed,
    const QJSValue &inserted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#changed

    Parameters
    ----------

    removed : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    inserted : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQmlDelegateModelGroup::changed(const QJSValue &removed, const
    #      QJSValue &inserted)
    self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup7changedERK8QJSValueS2_',
        self._valueOf(removed), self._valueOf(inserted),
    )

  def d_func(self) -> Optional[QQmlDelegateModelGroupPrivate]:
    """
    Calls Qt's 'QQmlDelegateModelGroupPrivate
    *QQmlDelegateModelGroup::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelegatemodelgroup.html#d_func

    Returns
    -------

    Optional[QQmlDelegateModelGroupPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelGroupPrivate *QQmlDelegateModelGroup::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QQmlDelegateModelGroup6d_funcEv',
    )
    from . import QQmlDelegateModelGroupPrivate
    return QQmlDelegateModelGroupPrivate._cuteAt(address)
