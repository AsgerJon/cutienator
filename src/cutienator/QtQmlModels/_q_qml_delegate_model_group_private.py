"""
QQmlDelegateModelGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelGroupPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlDelegateModelGroup, QQuickPackage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDelegateModelGroup = WAIT['QQmlDelegateModelGroup']
  QQuickPackage = WAIT['QQuickPackage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelGroupPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQmlDelegateModelGroupPrivate: a plain Python object
  standing in front of one C++ QQmlDelegateModelGroupPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQmlDelegateModelGroupPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelGroupPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'get',
  'isChangedConnected', 'emitModelUpdated', 'createdPackage'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlDelegateModelGroup
    *QQmlDelegateModelGroupPrivate::q_func() const': takes in Python what
    'QQmlDelegateModelGroup *QQmlDelegateModelGroupPrivate::q_func()' takes.
  - Qt's 'void QQmlDelegateModelGroupPrivate::setModel(QQmlDelegateModel
    *model, Compositor::Group group)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QQmlDelegateModelItemObject.

  What to expect
  --------------

  - The C++ QQmlDelegateModelGroupPrivate is created at the first use, not by
    'QQmlDelegateModelGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelGroupPrivate.
  - Each name of Qt's QQmlDelegateModelGroupPrivate that has no cute function
    yet, 'destroyingPackage', 'emitChanges', 'initPackage', 'parseGroupArgs',
    'parseIndex', 'setModel', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlDelegateModelGroup)
  @overload(NoneType)
  def get(
      group: Optional[QQmlDelegateModelGroup],
  ) -> Optional[QQmlDelegateModelGroupPrivate]:
    """
    Calls Qt's 'QQmlDelegateModelGroupPrivate
    *QQmlDelegateModelGroupPrivate::get(QQmlDelegateModelGroup *group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupprivate.html#get

    Parameters
    ----------

    group : Optional[QQmlDelegateModelGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlDelegateModelGroupPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelGroupPrivate
    #      *QQmlDelegateModelGroupPrivate::get(QQmlDelegateModelGroup *group)
    address = Rituals.call(
        'ritual_ZN29QQmlDelegateModelGroupPrivate3getEP22QQmlDelegateModelG'
        'roup',
        CuteMixin._addressOf(group),
    )
    return QQmlDelegateModelGroupPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelGroupPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQmlDelegateModelGroupPrivate::QQmlDelegateModelGroupPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupprivate.html
    """
    #  QQmlDelegateModelGroupPrivate::QQmlDelegateModelGroupPrivate()
    self._noteCreation(QQmlDelegateModelGroupPrivate, lambda: Rituals.call(
        'ritual_ZN29QQmlDelegateModelGroupPrivateC1Ev',
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

  def q_func(self) -> Optional[QQmlDelegateModelGroup]:
    """
    Calls Qt's 'QQmlDelegateModelGroup
    *QQmlDelegateModelGroupPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupprivate.html#q_func

    Returns
    -------

    Optional[QQmlDelegateModelGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModelGroup *QQmlDelegateModelGroupPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QQmlDelegateModelGroupPrivate6q_funcEv',
    )
    from . import QQmlDelegateModelGroup
    return QQmlDelegateModelGroup._cuteAt(address)

  def isChangedConnected(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelGroupPrivate::isChangedConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupprivate.html
    """
    #  bool QQmlDelegateModelGroupPrivate::isChangedConnected()
    return self.uglySide.call(
        'ritual_ZN29QQmlDelegateModelGroupPrivate18isChangedConnectedEv',
    )

  @overload(bool)
  def emitModelUpdated(self, reset: bool) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroupPrivate::emitModelUpdated(bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupprivate.html

    Parameters
    ----------

    reset : bool
      Passed on as it is.
    """
    #  void QQmlDelegateModelGroupPrivate::emitModelUpdated(bool reset)
    self.uglySide.call(
        'ritual_ZN29QQmlDelegateModelGroupPrivate16emitModelUpdatedEb',
        reset,
    )

  @overload(int, QQuickPackage)
  @overload(int, NoneType)
  def createdPackage(
      self,
      index: int,
      package: Optional[QQuickPackage],
  ) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroupPrivate::createdPackage(int index,
    QQuickPackage *package)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupprivate.html#createdPackage

    Parameters
    ----------

    index : int
      Passed on as it is.

    package : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroupPrivate::createdPackage(int index,
    #      QQuickPackage *package)
    self.uglySide.call(
        'ritual_ZN29QQmlDelegateModelGroupPrivate14createdPackageEiP13QQuic'
        'kPackage',
        index, self._addressOf(package),
    )

  @staticmethod
  def destroyingPackage(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelGroupPrivate::destroyingPackage(QQuickPackage
    *package)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name
    'GroupEmitterListIt'.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelGroupPrivate.destroyingPackage' has no cute "
        "function yet. Qt's 'void "
        "QQmlDelegateModelGroupPrivate::destroyingPackage(QQuickPackage "
        "*package)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'GroupEmitterListIt'.")

  @staticmethod
  def emitChanges(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateModelGroupPrivate::emitChanges(QV4::ExecutionEngine
    *engine)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'qdmEngineData'.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelGroupPrivate.emitChanges' has no cute function "
        "yet. Qt's 'void "
        "QQmlDelegateModelGroupPrivate::emitChanges(QV4::ExecutionEngine "
        "*engine)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qdmEngineData'.")

  @staticmethod
  def initPackage(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelGroupPrivate::initPackage(int index,
    QQuickPackage *package)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: unknown type name
    'GroupEmitterListIt'.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelGroupPrivate.initPackage' has no cute function "
        "yet. Qt's 'void QQmlDelegateModelGroupPrivate::initPackage(int "
        "index, QQuickPackage *package)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'GroupEmitterListIt'.")

  @staticmethod
  def parseGroupArgs(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlDelegateModelGroupPrivate::parseGroupArgs(QQmlV4FunctionPtr args,
    Compositor::Group *group, int *index, int *count, int *groups) const':
    leans on 'QQmlDelegateModelItemObject::static_vtbl', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelGroupPrivate.parseGroupArgs' has no cute "
        "function yet. Qt's 'bool "
        "QQmlDelegateModelGroupPrivate::parseGroupArgs(QQmlV4FunctionPtr "
        "args, Compositor::Group *group, int *index, int *count, int "
        "*groups) const': leans on "
        "'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseIndex(*__, **_) -> Never:
    """
    Qt's 'bool QQmlDelegateModelGroupPrivate::parseIndex(const QV4::Value
    &value, int *index, Compositor::Group *group) const': leans on
    'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelGroupPrivate.parseIndex' has no cute function "
        "yet. Qt's 'bool QQmlDelegateModelGroupPrivate::parseIndex(const "
        "QV4::Value &value, int *index, Compositor::Group *group) const': "
        "leans on 'QQmlDelegateModelItemObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setModel(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelGroupPrivate::setModel(QQmlDelegateModel
    *model, Compositor::Group group)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelGroupPrivate.setModel' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelGroupPrivate::setModel(QQmlDelegateModel *model, "
        "Compositor::Group group)': takes a type Python has no way to hand "
        "over yet.")
