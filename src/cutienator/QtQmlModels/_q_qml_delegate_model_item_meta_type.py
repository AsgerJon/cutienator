"""
QQmlDelegateModelItemMetaType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelItemMetaType to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlDelegateModel, QQmlTableInstanceModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDelegateModel = WAIT['QQmlDelegateModel']
  QQmlTableInstanceModel = WAIT['QQmlTableInstanceModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelItemMetaType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDelegateModelItemMetaType: a plain Python object
  standing in front of one C++ QQmlDelegateModelItemMetaType.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelItemMetaType that has a ritual and
  that Python can call so far, 6 names in all:
  'initializeAttachedMetaObject', 'initializePrototype', 'parseGroups',
  'delegateModel', 'groupCount', 'emitModelChanged'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDelegateModelItemMetaType::~QQmlDelegateModelItemMetaType()':
    the destructor: Python never removes a C++ QQmlDelegateModelItemMetaType.

  What to expect
  --------------

  - The C++ QQmlDelegateModelItemMetaType is created at the first use, not by
    'QQmlDelegateModelItemMetaType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelItemMetaType.
  """

  #  The enums Qt writes inside QQmlDelegateModelItemMetaType, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class ModelKind(CuteNum, scoped=True):
    """
    The enum 'QQmlDelegateModelItemMetaType::ModelKind' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    InstanceModel = Kee[int](0)
    DelegateModel = Kee[int](1)
    TableInstanceModel = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelItemMetaType'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def parseGroups(self, groupNames: QStringList) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelItemMetaType::parseGroups(const
    QStringList &groupNames) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html#parseGroups

    Parameters
    ----------

    groupNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QQmlDelegateModelItemMetaType::parseGroups(const QStringList
    #      &groupNames) const
    return self.uglySide.call(
        'ritual_ZNK29QQmlDelegateModelItemMetaType11parseGroupsERK5QListI7Q'
        'StringE',
        self._valueOf(groupNames),
    )

  @overload(WAIT['QV4.Value'])
  def parseGroups(self, groupNames: QV4.Value) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelItemMetaType::parseGroups(const
    QV4::Value &groupNames) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html#parseGroups

    Parameters
    ----------

    groupNames : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  int QQmlDelegateModelItemMetaType::parseGroups(const QV4::Value
    #      &groupNames) const
    return self.uglySide.call(
        'ritual_ZNK29QQmlDelegateModelItemMetaType11parseGroupsERKN3QV45Val'
        'ueE',
        self._valueOf(groupNames),
    )

  def delegateModel(self) -> Optional[QQmlDelegateModel]:
    """
    Calls Qt's 'QQmlDelegateModel
    *QQmlDelegateModelItemMetaType::delegateModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html#delegateModel

    Returns
    -------

    Optional[QQmlDelegateModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModel *QQmlDelegateModelItemMetaType::delegateModel()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQmlDelegateModelItemMetaType13delegateModelEv',
    )
    from . import QQmlDelegateModel
    return QQmlDelegateModel._cuteAt(address)

  def groupCount(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlDelegateModelItemMetaType::groupCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html#groupCount
    """
    #  qsizetype QQmlDelegateModelItemMetaType::groupCount() const
    return self.uglySide.call(
        'ritual_ZNK29QQmlDelegateModelItemMetaType10groupCountEv',
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

  @overload(WAIT['QV4.ExecutionEngine'], QQmlDelegateModel, QStringList)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QStringList)
  @overload(NoneType, QQmlDelegateModel, QStringList)
  @overload(NoneType, NoneType, QStringList)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      model: Optional[QQmlDelegateModel],
      groupNames: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelItemMetaType::QQmlDelegateModelItemMetaType(QV4::
    ExecutionEngine *engine, QQmlDelegateModel *model, const QStringList
    &groupNames)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlDelegateModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    groupNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QQmlDelegateModelItemMetaType::QQmlDelegateModelItemMetaType(
    #      QV4::ExecutionEngine *engine, QQmlDelegateModel *model, const
    #      QStringList &groupNames)
    self._noteCreation(QQmlDelegateModelItemMetaType, lambda: Rituals.call(
        'ritual_ZN29QQmlDelegateModelItemMetaTypeC1EPN3QV415ExecutionEngine'
        'EP17QQmlDelegateModelRK5QListI7QStringE',
        self._addressOf(engine), self._addressOf(model),
        self._valueOf(groupNames),
    ))

  @overload(WAIT['QV4.ExecutionEngine'], QQmlTableInstanceModel)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QQmlTableInstanceModel)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      model: Optional[QQmlTableInstanceModel],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDelegateModelItemMetaType::QQmlDelegateModelItemMetaType(QV4::
    ExecutionEngine *engine, QQmlTableInstanceModel *model)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlTableInstanceModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlDelegateModelItemMetaType::QQmlDelegateModelItemMetaType(
    #      QV4::ExecutionEngine *engine, QQmlTableInstanceModel *model)
    self._noteCreation(QQmlDelegateModelItemMetaType, lambda: Rituals.call(
        'ritual_ZN29QQmlDelegateModelItemMetaTypeC1EPN3QV415ExecutionEngine'
        'EP22QQmlTableInstanceModel',
        self._addressOf(engine), self._addressOf(model),
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

  def initializeAttachedMetaObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelItemMetaType::initializeAttachedMetaObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html
    """
    #  void QQmlDelegateModelItemMetaType::initializeAttachedMetaObject()
    self.uglySide.call(
        'ritual_ZN29QQmlDelegateModelItemMetaType28initializeAttachedMetaOb'
        'jectEv',
    )

  def initializePrototype(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItemMetaType::initializePrototype()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html
    """
    #  void QQmlDelegateModelItemMetaType::initializePrototype()
    self.uglySide.call(
        'ritual_ZN29QQmlDelegateModelItemMetaType19initializePrototypeEv',
    )

  def emitModelChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelItemMetaType::emitModelChanged()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelitemmetatype.html
    """
    #  void QQmlDelegateModelItemMetaType::emitModelChanged() const
    self.uglySide.call(
        'ritual_ZNK29QQmlDelegateModelItemMetaType16emitModelChangedEv',
    )
