"""
QQuickStatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickStatePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQml import QQmlGuardImpl
  from . import QQuickState, QQuickStateAction

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStatePrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickStatePrivate: a plain Python object standing in
  front of one C++ QQuickStatePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickStatePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStatePrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'generateActionList',
  'complete'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickState *QQuickStatePrivate::q_func() const': takes in
    Python what 'QQuickState *QQuickStatePrivate::q_func()' takes.
  - Qt's 'void QQuickStatePrivate::operations_append(
    QQmlListProperty<QQuickStateOperation> *prop, QQuickStateOperation *op)':
    names 'QQmlListProperty<QQuickStateOperation>', which has no cute class
    yet.
  - Qt's 'void QQuickStatePrivate::operations_clear(
    QQmlListProperty<QQuickStateOperation> *prop)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
  - Qt's 'qsizetype QQuickStatePrivate::operations_count(
    QQmlListProperty<QQuickStateOperation> *prop)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
  - Qt's 'QQuickStateOperation
    *QQuickStatePrivate::operations_at(QQmlListProperty<QQuickStateOperation>
    *prop, qsizetype index)': names 'QQmlListProperty<QQuickStateOperation>',
    which has no cute class yet.
  - Qt's 'void QQuickStatePrivate::operations_replace(
    QQmlListProperty<QQuickStateOperation> *prop, qsizetype index,
    QQuickStateOperation *op)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
  - Qt's 'void QQuickStatePrivate::operations_removeLast(
    QQmlListProperty<QQuickStateOperation> *prop)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickStatePrivate is created at the first use, not by
    'QQuickStatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStatePrivate.
  - Each name of Qt's QQuickStatePrivate that has no cute function yet,
    'operations_append', 'operations_at', 'operations_clear',
    'operations_count', 'operations_removeLast', 'operations_replace', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuickStatePrivate, each a class in here as
  #  in C++.

  class OperationGuard(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickStatePrivate::OperationGuard: a plain Python
    object standing in front of one C++ QQuickStatePrivate::OperationGuard.

    C++ hands a QQuickStatePrivate::OperationGuard around as a copy, so every
    C++ QQuickStatePrivate::OperationGuard behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQuickStatePrivate::OperationGuard that has a
    ritual and that Python can call so far, 1 name in all:
    'objectDestroyedImpl'. None can be made from Python: one comes out of a
    function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickStatePrivate::OperationGuard::OperationGuard(QObject *obj,
      QList<OperationGuard> *l)': names
      'QList<QQuickStatePrivate::OperationGuard>', which has no cute class
      yet.
    - Qt's 'QQuickStatePrivate::OperationGuard::~OperationGuard()': the
      destructor: Python removes its C++ QQuickStatePrivate::OperationGuard
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickStatePrivate::OperationGuard is created at the first use,
      not by 'QQuickStatePrivate::OperationGuard(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickStatePrivate::OperationGuard back gives a
      copy the ritual made for Python, in a new cute
      QQuickStatePrivate::OperationGuard.
    - Each name of Qt's QQuickStatePrivate::OperationGuard that has no cute
      function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlGuardImpl = WAIT['QQmlGuardImpl']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(QQmlGuardImpl)
    @overload(NoneType)
    def objectDestroyedImpl(guard: Optional[QQmlGuardImpl]) -> None:
      """
      Calls Qt's 'void
      QQuickStatePrivate::OperationGuard::objectDestroyedImpl(QQmlGuardImpl
      *guard)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickstateprivate-operationguard.html

      Parameters
      ----------

      guard : Optional[QQmlGuardImpl]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QQuickStatePrivate::OperationGuard::objectDestroyedImpl(
      #      QQmlGuardImpl *guard)
      Rituals.call(
          'ritual_ZN18QQuickStatePrivate14OperationGuard19objectDestroyedIm'
          'plEP13QQmlGuardImpl',
          CuteMixin._addressOf(guard),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickStatePrivate::OperationGuard'

    #  Qt's '~QQuickStatePrivate::OperationGuard()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickStatePrivate::OperationGuard
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQuickStatePrivate14OperationGuardD1Ev'

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QQuickStatePrivate::OperationGuard::OperationGuard(QObject *obj,
      QList<OperationGuard> *l)': names
      'QList<QQuickStatePrivate::OperationGuard>', which has no cute class
      yet.
      """
      raise NotImplementedError(
          "'QQuickStatePrivate.OperationGuard.__init__' has no cute "
          "function yet. Qt's "
          "'QQuickStatePrivate::OperationGuard::OperationGuard(QObject "
          "*obj, QList<OperationGuard> *l)': names "
          "'QList<QQuickStatePrivate::OperationGuard>', which has no cute "
          "class yet.")

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStatePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def generateActionList(self) -> QList[QQuickStateAction]:
    """
    Calls Qt's 'QQuickStateOperation::ActionList
    QQuickStatePrivate::generateActionList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateprivate.html#generateActionList

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QQuickStateOperation::ActionList
    #      QQuickStatePrivate::generateActionList() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickStatePrivate18generateActionListEv',
    )
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

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
    'QQuickStatePrivate::QQuickStatePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateprivate.html#QQuickStatePrivate
    """
    #  QQuickStatePrivate::QQuickStatePrivate()
    self._noteCreation(QQuickStatePrivate, lambda: Rituals.call(
        'ritual_ZN18QQuickStatePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickState]:
    """
    Calls Qt's 'QQuickState *QQuickStatePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateprivate.html#q_func

    Returns
    -------

    Optional[QQuickState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickState *QQuickStatePrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QQuickStatePrivate6q_funcEv')
    from . import QQuickState
    return QQuickState._cuteAt(address)

  def complete(self) -> None:
    """
    Calls Qt's 'void QQuickStatePrivate::complete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateprivate.html#complete
    """
    #  void QQuickStatePrivate::complete()
    self.uglySide.call('ritual_ZN18QQuickStatePrivate8completeEv')

  @staticmethod
  def operations_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickStatePrivate::operations_append(
    QQmlListProperty<QQuickStateOperation> *prop, QQuickStateOperation *op)':
    names 'QQmlListProperty<QQuickStateOperation>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickStatePrivate.operations_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickStatePrivate::operations_append(QQmlListProperty<QQuickStateO"
        "peration> *prop, QQuickStateOperation *op)': names "
        "'QQmlListProperty<QQuickStateOperation>', which has no cute class "
        "yet.")

  @staticmethod
  def operations_at(*__, **_) -> Never:
    """
    Qt's 'QQuickStateOperation
    *QQuickStatePrivate::operations_at(QQmlListProperty<QQuickStateOperation>
    *prop, qsizetype index)': names 'QQmlListProperty<QQuickStateOperation>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickStatePrivate.operations_at' has no cute function yet. Qt's "
        "'QQuickStateOperation "
        "*QQuickStatePrivate::operations_at(QQmlListProperty<QQuickStateOper"
        "ation> *prop, qsizetype index)': names "
        "'QQmlListProperty<QQuickStateOperation>', which has no cute class "
        "yet.")

  @staticmethod
  def operations_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickStatePrivate::operations_clear(
    QQmlListProperty<QQuickStateOperation> *prop)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickStatePrivate.operations_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuickStatePrivate::operations_clear(QQmlListProperty<QQuickStateOp"
        "eration> *prop)': names 'QQmlListProperty<QQuickStateOperation>', "
        "which has no cute class yet.")

  @staticmethod
  def operations_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickStatePrivate::operations_count(
    QQmlListProperty<QQuickStateOperation> *prop)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickStatePrivate.operations_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickStatePrivate::operations_count(QQmlListProperty<QQuickStateOp"
        "eration> *prop)': names 'QQmlListProperty<QQuickStateOperation>', "
        "which has no cute class yet.")

  @staticmethod
  def operations_removeLast(*__, **_) -> Never:
    """
    Qt's 'void QQuickStatePrivate::operations_removeLast(
    QQmlListProperty<QQuickStateOperation> *prop)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickStatePrivate.operations_removeLast' has no cute function "
        "yet. Qt's 'void "
        "QQuickStatePrivate::operations_removeLast(QQmlListProperty<QQuickSt"
        "ateOperation> *prop)': names "
        "'QQmlListProperty<QQuickStateOperation>', which has no cute class "
        "yet.")

  @staticmethod
  def operations_replace(*__, **_) -> Never:
    """
    Qt's 'void QQuickStatePrivate::operations_replace(
    QQmlListProperty<QQuickStateOperation> *prop, qsizetype index,
    QQuickStateOperation *op)': names
    'QQmlListProperty<QQuickStateOperation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickStatePrivate.operations_replace' has no cute function yet. "
        "Qt's 'void "
        "QQuickStatePrivate::operations_replace(QQmlListProperty<QQuickState"
        "Operation> *prop, qsizetype index, QQuickStateOperation *op)': "
        "names 'QQmlListProperty<QQuickStateOperation>', which has no cute "
        "class yet.")
