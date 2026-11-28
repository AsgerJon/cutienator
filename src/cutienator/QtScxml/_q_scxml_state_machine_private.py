"""
QScxmlStateMachinePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScxmlStateMachinePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QScxmlDataModel, QScxmlEvent, QScxmlInvokableService
  from . import QScxmlInvokableServiceFactory, QScxmlStateMachine
  from . import QScxmlStateMachineInfo, QScxmlTableData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QScxmlDataModel = WAIT['QScxmlDataModel']
  QScxmlEvent = WAIT['QScxmlEvent']
  QScxmlStateMachine = WAIT['QScxmlStateMachine']
  QScxmlStateMachineInfo = WAIT['QScxmlStateMachineInfo']
  QScxmlTableData = WAIT['QScxmlTableData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlStateMachinePrivate(QObjectPrivate):
  """
  The cute side of Qt's QScxmlStateMachinePrivate: a plain Python object
  standing in front of one C++ QScxmlStateMachinePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QScxmlStateMachinePrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlStateMachinePrivate that has a ritual and that
  Python can call so far, 54 names in all: 'q_func', 'get',
  'generateSessionId', 'parserData', 'setIsInvoked', 'addService',
  'removeService', 'serviceFactory', 'executeInitialSetup', 'routeEvent',
  'postEvent', 'submitDelayedEvent', 'submitError', 'start', 'pause',
  'processEvents', 'setEvent', 'resetEvent', 'emitStateActive',
  'emitInvokedServicesChanged', 'attach', 'configuration', 'updateMetaCache',
  'exitInterpreter', 'returnDoneEvent', 'removeConflictingTransitions',
  'microstep', 'exitStates', 'executeTransitionContent', 'enterStates',
  'computeEntrySet', 'addDescendantStatesToEnter',
  'addAncestorStatesToEnter', 'hasDescendant', 'allDescendants',
  'isDescendant', 'isInFinalState', 'getTransitionDomain',
  'getEffectiveTargetStates', 'isInitializedChanged',
  '_qt_property_m_isInitialized_offset', 'initialValuesChanged',
  '_qt_property_m_initialValues_offset', 'loaderChanged',
  '_qt_property_m_loader_offset', 'setDataModel',
  '_qt_property_m_dataModel_offset', 'setTableData',
  '_qt_property_m_tableData_offset', 'invokedServicesActualCalculation',
  '_qt_property_m_invokedServicesComputedProperty_offset', 'isRunnable',
  'isPaused', 'isFinished'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScxmlStateMachine *QScxmlStateMachinePrivate::q_func()
    const': takes in Python what 'QScxmlStateMachine
    *QScxmlStateMachinePrivate::q_func()' takes.
  - Qt's 'QScxmlStateMachinePrivate::~QScxmlStateMachinePrivate()': the
    destructor: Python never removes a C++ QScxmlStateMachinePrivate.
  - Qt's 'QStringList QScxmlStateMachinePrivate::stateNames(const
    std::vector<int> &stateIndexes) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'std::vector<int> QScxmlStateMachinePrivate::historyStates(int
    stateIdx) const': gives a type Python has no way to take yet.
  - Qt's 'void QScxmlStateMachinePrivate::selectTransitions(OrderedSet
    &enabledTransitions, const std::vector<int> &configInDocumentOrder,
    QScxmlEvent *event) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QScxmlStateMachinePrivate::getProperAncestors(std::vector<int>
    *ancestors, int state1, int state2) const': names 'std::vector<int>',
    which has no cute class yet.
  - Qt's 'void QScxmlStateMachinePrivate::computeExitSet(const OrderedSet
    &enabledTransitions, OrderedSet &statesToExit) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QScxmlStateMachinePrivate::allInFinalStates(const
    std::vector<int> &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QScxmlStateMachinePrivate::someInFinalStates(const
    std::vector<int> &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'int QScxmlStateMachinePrivate::findLCCA(OrderedSet &&states)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 67 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QScxmlStateMachinePrivate is created at the first use, not by
    'QScxmlStateMachinePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlStateMachinePrivate.
  - Each name of Qt's QScxmlStateMachinePrivate that has no cute function
    yet, 'allInFinalStates', 'computeExitSet', 'findLCCA', 'getChildStates',
    'getProperAncestors', 'historyStates', 'nameMatch', 'selectTransitions',
    'someInFinalStates', 'stateNames', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QScxmlStateMachinePrivate, each a class in
  #  here as in C++.

  class HistoryContent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlStateMachinePrivate::HistoryContent: a plain
    Python object standing in front of one C++
    QScxmlStateMachinePrivate::HistoryContent.

    C++ hands a QScxmlStateMachinePrivate::HistoryContent around as a copy,
    so every C++ QScxmlStateMachinePrivate::HistoryContent behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QScxmlStateMachinePrivate::HistoryContent that has
    a ritual and that Python can call so far, 1 name in all: 'value'. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlStateMachinePrivate::HistoryContent::~HistoryContent()':
      the destructor: Python removes its C++
      QScxmlStateMachinePrivate::HistoryContent by it, and has no other use
      for it.

    What has no ritual
    ------------------

    1 of the 4 functions Qt declares: 1 takes or gives a type that cannot be
    passed yet.

    What to expect
    --------------

    - The C++ QScxmlStateMachinePrivate::HistoryContent is created at the
      first use, not by 'QScxmlStateMachinePrivate::HistoryContent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlStateMachinePrivate::HistoryContent back
      gives a copy the ritual made for Python, in a new cute
      QScxmlStateMachinePrivate::HistoryContent.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlStateMachinePrivate::HistoryContent'

    #  Qt's '~QScxmlStateMachinePrivate::HistoryContent()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QScxmlStateMachinePrivate::HistoryContent behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QScxmlStateMachinePrivate14HistoryContentD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def value(self, idx: int) -> int:
      """
      Calls Qt's 'int QScxmlStateMachinePrivate::HistoryContent::value(int
      idx) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-historycontent.html

      Parameters
      ----------

      idx : int
        Passed on as it is.
      """
      #  int QScxmlStateMachinePrivate::HistoryContent::value(int idx) const
      return self.uglySide.call(
          'ritual_ZNK25QScxmlStateMachinePrivate14HistoryContent5valueEi',
          idx,
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
      'QScxmlStateMachinePrivate::HistoryContent::HistoryContent()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-historycontent.html
      """
      #  QScxmlStateMachinePrivate::HistoryContent::HistoryContent()
      self._noteCreation(
          QScxmlStateMachinePrivate.HistoryContent, lambda: Rituals.call(
              'ritual_ZN25QScxmlStateMachinePrivate14HistoryContentC1Ev',
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

  class OrderedSet(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlStateMachinePrivate::OrderedSet: a plain
    Python object standing in front of one C++
    QScxmlStateMachinePrivate::OrderedSet.

    C++ hands a QScxmlStateMachinePrivate::OrderedSet around as a copy, so
    every C++ QScxmlStateMachinePrivate::OrderedSet behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QScxmlStateMachinePrivate::OrderedSet that has a
    ritual and that Python can call so far, 7 names in all: 'contains',
    'remove', 'removeHead', 'isEmpty', 'add', 'intersectsWith', 'clear'. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlStateMachinePrivate::OrderedSet::OrderedSet(std::
      initializer_list<int> l)': takes a type Python has no way to hand over
      yet.
    - Qt's 'std::vector<int>
      QScxmlStateMachinePrivate::OrderedSet::takeList() const': gives a type
      Python has no way to take yet.
    - Qt's 'const std::vector<int>
      &QScxmlStateMachinePrivate::OrderedSet::list() const': gives a type
      Python has no way to take yet.
    - Qt's 'const_iterator QScxmlStateMachinePrivate::OrderedSet::begin()
      const': gives a type Python has no way to take yet.
    - Qt's 'const_iterator QScxmlStateMachinePrivate::OrderedSet::end()
      const': gives a type Python has no way to take yet.
    - Qt's 'QScxmlStateMachinePrivate::OrderedSet::~OrderedSet()': the
      destructor: Python removes its C++
      QScxmlStateMachinePrivate::OrderedSet by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QScxmlStateMachinePrivate::OrderedSet is created at the first
      use, not by 'QScxmlStateMachinePrivate::OrderedSet(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlStateMachinePrivate::OrderedSet back gives a
      copy the ritual made for Python, in a new cute
      QScxmlStateMachinePrivate::OrderedSet.
    - Each name of Qt's QScxmlStateMachinePrivate::OrderedSet that has no
      cute function yet, 'begin', 'end', 'list', 'takeList', holds a function
      that raises 'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlStateMachinePrivate::OrderedSet'

    #  Qt's '~QScxmlStateMachinePrivate::OrderedSet()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QScxmlStateMachinePrivate::OrderedSet behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QScxmlStateMachinePrivate10OrderedSetD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def contains(self, i: int) -> bool:
      """
      Calls Qt's 'bool QScxmlStateMachinePrivate::OrderedSet::contains(int i)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html

      Parameters
      ----------

      i : int
        Passed on as it is.
      """
      #  bool QScxmlStateMachinePrivate::OrderedSet::contains(int i) const
      return self.uglySide.call(
          'ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet8containsEi', i,
      )

    def isEmpty(self) -> bool:
      """
      Calls Qt's 'bool QScxmlStateMachinePrivate::OrderedSet::isEmpty()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html
      """
      #  bool QScxmlStateMachinePrivate::OrderedSet::isEmpty() const
      return self.uglySide.call(
          'ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet7isEmptyEv',
      )

    @overload(THIS)
    def intersectsWith(
        self,
        other: QScxmlStateMachinePrivate.OrderedSet,
    ) -> bool:
      """
      Calls Qt's 'bool
      QScxmlStateMachinePrivate::OrderedSet::intersectsWith(const OrderedSet
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html

      Parameters
      ----------

      other : QScxmlStateMachinePrivate.OrderedSet
        Passed on as a value: Qt reads the C++
        QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.
      """
      #  bool QScxmlStateMachinePrivate::OrderedSet::intersectsWith(const
      #      OrderedSet &other) const
      return self.uglySide.call(
          'ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet14intersectsWit'
          'hERKS0_',
          self._valueOf(other),
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
      'QScxmlStateMachinePrivate::OrderedSet::OrderedSet()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html
      """
      #  QScxmlStateMachinePrivate::OrderedSet::OrderedSet()
      self._noteCreation(
          QScxmlStateMachinePrivate.OrderedSet, lambda: Rituals.call(
              'ritual_ZN25QScxmlStateMachinePrivate10OrderedSetC1Ev',
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

    @overload(int)
    def remove(self, i: int) -> bool:
      """
      Calls Qt's 'bool QScxmlStateMachinePrivate::OrderedSet::remove(int i)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html#remove

      Parameters
      ----------

      i : int
        Passed on as it is.
      """
      #  bool QScxmlStateMachinePrivate::OrderedSet::remove(int i)
      return self.uglySide.call(
          'ritual_ZN25QScxmlStateMachinePrivate10OrderedSet6removeEi', i,
      )

    def removeHead(self) -> None:
      """
      Calls Qt's 'void QScxmlStateMachinePrivate::OrderedSet::removeHead()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html
      """
      #  void QScxmlStateMachinePrivate::OrderedSet::removeHead()
      self.uglySide.call(
          'ritual_ZN25QScxmlStateMachinePrivate10OrderedSet10removeHeadEv',
      )

    @overload(int)
    def add(self, i: int) -> None:
      """
      Calls Qt's 'void QScxmlStateMachinePrivate::OrderedSet::add(int i)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html#add

      Parameters
      ----------

      i : int
        Passed on as it is.
      """
      #  void QScxmlStateMachinePrivate::OrderedSet::add(int i)
      self.uglySide.call(
          'ritual_ZN25QScxmlStateMachinePrivate10OrderedSet3addEi', i,
      )

    def clear(self) -> None:
      """
      Calls Qt's 'void QScxmlStateMachinePrivate::OrderedSet::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-orderedset.html#clear
      """
      #  void QScxmlStateMachinePrivate::OrderedSet::clear()
      self.uglySide.call(
          'ritual_ZN25QScxmlStateMachinePrivate10OrderedSet5clearEv',
      )

    @staticmethod
    def begin(*__, **_) -> Never:
      """
      Qt's 'const_iterator QScxmlStateMachinePrivate::OrderedSet::begin()
      const': gives a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QScxmlStateMachinePrivate.OrderedSet.begin' has no cute "
          "function yet. Qt's 'const_iterator "
          "QScxmlStateMachinePrivate::OrderedSet::begin() const': gives a "
          "type Python has no way to take yet.")

    @staticmethod
    def end(*__, **_) -> Never:
      """
      Qt's 'const_iterator QScxmlStateMachinePrivate::OrderedSet::end()
      const': gives a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QScxmlStateMachinePrivate.OrderedSet.end' has no cute function "
          "yet. Qt's 'const_iterator "
          "QScxmlStateMachinePrivate::OrderedSet::end() const': gives a "
          "type Python has no way to take yet.")

    @staticmethod
    def list(*__, **_) -> Never:
      """
      Qt's 'const std::vector<int>
      &QScxmlStateMachinePrivate::OrderedSet::list() const': gives a type
      Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QScxmlStateMachinePrivate.OrderedSet.list' has no cute function "
          "yet. Qt's 'const std::vector<int> "
          "&QScxmlStateMachinePrivate::OrderedSet::list() const': gives a "
          "type Python has no way to take yet.")

    @staticmethod
    def takeList(*__, **_) -> Never:
      """
      Qt's 'std::vector<int>
      QScxmlStateMachinePrivate::OrderedSet::takeList() const': gives a type
      Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QScxmlStateMachinePrivate.OrderedSet.takeList' has no cute "
          "function yet. Qt's 'std::vector<int> "
          "QScxmlStateMachinePrivate::OrderedSet::takeList() const': gives "
          "a type Python has no way to take yet.")

  class ParserData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlStateMachinePrivate::ParserData: a plain
    Python object standing in front of one C++
    QScxmlStateMachinePrivate::ParserData.

    What exists
    -----------

    No function of Qt's QScxmlStateMachinePrivate::ParserData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What to expect
    --------------

    - The C++ QScxmlStateMachinePrivate::ParserData is created at the first
      use, not by 'QScxmlStateMachinePrivate::ParserData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QScxmlStateMachinePrivate::ParserData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlStateMachinePrivate::ParserData'

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

  class Queue(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlStateMachinePrivate::Queue: a plain Python
    object standing in front of one C++ QScxmlStateMachinePrivate::Queue.

    C++ hands a QScxmlStateMachinePrivate::Queue around as a copy, so every
    C++ QScxmlStateMachinePrivate::Queue behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QScxmlStateMachinePrivate::Queue that has a ritual
    and that Python can call so far, 3 names in all: 'enqueue', 'isEmpty',
    'dequeue'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlStateMachinePrivate::Queue::~Queue()': the destructor:
      Python removes its C++ QScxmlStateMachinePrivate::Queue by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QScxmlStateMachinePrivate::Queue is created at the first use,
      not by 'QScxmlStateMachinePrivate::Queue(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlStateMachinePrivate::Queue back gives a copy
      the ritual made for Python, in a new cute
      QScxmlStateMachinePrivate::Queue.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QScxmlEvent = WAIT['QScxmlEvent']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlStateMachinePrivate::Queue'

    #  Qt's '~QScxmlStateMachinePrivate::Queue()'. Naming it makes this a
    #  value class: Python owns every C++ QScxmlStateMachinePrivate::Queue
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QScxmlStateMachinePrivate5QueueD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isEmpty(self) -> bool:
      """
      Calls Qt's 'bool QScxmlStateMachinePrivate::Queue::isEmpty() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-queue.html#isEmpty
      """
      #  bool QScxmlStateMachinePrivate::Queue::isEmpty() const
      return self.uglySide.call(
          'ritual_ZNK25QScxmlStateMachinePrivate5Queue7isEmptyEv',
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
      'QScxmlStateMachinePrivate::Queue::Queue()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-queue.html#Queue
      """
      #  QScxmlStateMachinePrivate::Queue::Queue()
      self._noteCreation(
          QScxmlStateMachinePrivate.Queue, lambda: Rituals.call(
              'ritual_ZN25QScxmlStateMachinePrivate5QueueC1Ev',
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

    @overload(QScxmlEvent)
    @overload(NoneType)
    def enqueue(self, e: Optional[QScxmlEvent]) -> None:
      """
      Calls Qt's 'void QScxmlStateMachinePrivate::Queue::enqueue(QScxmlEvent
      *e)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-queue.html#enqueue

      Parameters
      ----------

      e : Optional[QScxmlEvent]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QScxmlStateMachinePrivate::Queue::enqueue(QScxmlEvent *e)
      self.uglySide.call(
          'ritual_ZN25QScxmlStateMachinePrivate5Queue7enqueueEP11QScxmlEven'
          't',
          self._addressOf(e),
      )

    def dequeue(self) -> Optional[QScxmlEvent]:
      """
      Calls Qt's 'QScxmlEvent *QScxmlStateMachinePrivate::Queue::dequeue()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlstatemachineprivate-queue.html#dequeue

      Returns
      -------

      Optional[QScxmlEvent]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QScxmlEvent *QScxmlStateMachinePrivate::Queue::dequeue()
      address = self.uglySide.call(
          'ritual_ZN25QScxmlStateMachinePrivate5Queue7dequeueEv',
      )
      from . import QScxmlEvent
      return QScxmlEvent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def get(
      t: Optional[QScxmlStateMachine],
  ) -> Optional[QScxmlStateMachinePrivate]:
    """
    Calls Qt's 'QScxmlStateMachinePrivate
    *QScxmlStateMachinePrivate::get(QScxmlStateMachine *t)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#get

    Parameters
    ----------

    t : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QScxmlStateMachinePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachinePrivate
    #      *QScxmlStateMachinePrivate::get(QScxmlStateMachine *t)
    address = Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate3getEP18QScxmlStateMachine',
        CuteMixin._addressOf(t),
    )
    return QScxmlStateMachinePrivate._cuteAt(address)

  @staticmethod
  @overload(str)
  def generateSessionId(prefix: str) -> str:
    """
    Calls Qt's 'QString QScxmlStateMachinePrivate::generateSessionId(const
    QString &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#generateSessionId

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlStateMachinePrivate::generateSessionId(const QString
    #      &prefix)
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate17generateSessionIdERK7QString',
        prefix,
    )

  @staticmethod
  def _qt_property_m_isInitialized_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachinePrivate::_qt_property_m_isInitialized_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  size_t
    #      QScxmlStateMachinePrivate::_qt_property_m_isInitialized_offset()
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate35_qt_property_m_isInitialized'
        '_offsetEv',
    )

  @staticmethod
  def _qt_property_m_initialValues_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachinePrivate::_qt_property_m_initialValues_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  size_t
    #      QScxmlStateMachinePrivate::_qt_property_m_initialValues_offset()
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate35_qt_property_m_initialValues'
        '_offsetEv',
    )

  @staticmethod
  def _qt_property_m_loader_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachinePrivate::_qt_property_m_loader_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  size_t QScxmlStateMachinePrivate::_qt_property_m_loader_offset()
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate28_qt_property_m_loader_offset'
        'Ev',
    )

  @staticmethod
  def _qt_property_m_dataModel_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachinePrivate::_qt_property_m_dataModel_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  size_t QScxmlStateMachinePrivate::_qt_property_m_dataModel_offset()
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate31_qt_property_m_dataModel_off'
        'setEv',
    )

  @staticmethod
  def _qt_property_m_tableData_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlStateMachinePrivate::_qt_property_m_tableData_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  size_t QScxmlStateMachinePrivate::_qt_property_m_tableData_offset()
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate31_qt_property_m_tableData_off'
        'setEv',
    )

  @staticmethod
  def _qt_property_m_invokedServicesComputedProperty_offset() -> int:
    """
    Calls Qt's 'size_t QScxmlStateMachinePrivate::
    _qt_property_m_invokedServicesComputedProperty_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  size_t QScxmlStateMachinePrivate::
    #      _qt_property_m_invokedServicesComputedProperty_offset()
    return Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivate53_qt_property_m_invokedServic'
        'esComputedProperty_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlStateMachinePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def configuration(self) -> OrderedSet:
    """
    Calls Qt's 'const OrderedSet &QScxmlStateMachinePrivate::configuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#configuration

    Returns
    -------

    OrderedSet
      A new cute QScxmlStateMachinePrivate::OrderedSet around the copy Qt
      gave back. Python owns it.
    """
    #  const OrderedSet &QScxmlStateMachinePrivate::configuration() const
    address = self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate13configurationEv',
    )
    return QScxmlStateMachinePrivate.OrderedSet._cuteOwning(address)

  @overload(OrderedSet, int)
  def hasDescendant(self, statesToEnter: OrderedSet, childIdx: int) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::hasDescendant(const
    OrderedSet &statesToEnter, int childIdx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#hasDescendant

    Parameters
    ----------

    statesToEnter : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.

    childIdx : int
      Passed on as it is.
    """
    #  bool QScxmlStateMachinePrivate::hasDescendant(const OrderedSet
    #      &statesToEnter, int childIdx) const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate13hasDescendantERKNS_10Ordere'
        'dSetEi',
        self._valueOf(statesToEnter), childIdx,
    )

  @overload(OrderedSet, int)
  def allDescendants(self, statesToEnter: OrderedSet, childdx: int) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::allDescendants(const
    OrderedSet &statesToEnter, int childdx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#allDescendants

    Parameters
    ----------

    statesToEnter : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.

    childdx : int
      Passed on as it is.
    """
    #  bool QScxmlStateMachinePrivate::allDescendants(const OrderedSet
    #      &statesToEnter, int childdx) const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate14allDescendantsERKNS_10Order'
        'edSetEi',
        self._valueOf(statesToEnter), childdx,
    )

  @overload(int, int)
  def isDescendant(self, state1: int, state2: int) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::isDescendant(int state1, int
    state2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#isDescendant

    Parameters
    ----------

    state1 : int
      Passed on as it is.

    state2 : int
      Passed on as it is.
    """
    #  bool QScxmlStateMachinePrivate::isDescendant(int state1, int state2)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate12isDescendantEii',
        state1, state2,
    )

  @overload(int)
  def isInFinalState(self, stateIndex: int) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::isInFinalState(int
    stateIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#isInFinalState

    Parameters
    ----------

    stateIndex : int
      Passed on as it is.
    """
    #  bool QScxmlStateMachinePrivate::isInFinalState(int stateIndex) const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate14isInFinalStateEi',
        stateIndex,
    )

  @overload(int)
  def getTransitionDomain(self, transitionIndex: int) -> int:
    """
    Calls Qt's 'int QScxmlStateMachinePrivate::getTransitionDomain(int
    transitionIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#getTransitionDomain

    Parameters
    ----------

    transitionIndex : int
      Passed on as it is.
    """
    #  int QScxmlStateMachinePrivate::getTransitionDomain(int
    #      transitionIndex) const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate19getTransitionDomainEi',
        transitionIndex,
    )

  def invokedServicesActualCalculation(
      self,
  ) -> QList[QScxmlInvokableService]:
    """
    Calls Qt's 'QList<QScxmlInvokableService *>
    QScxmlStateMachinePrivate::invokedServicesActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Returns
    -------

    QList[QScxmlInvokableService]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScxmlInvokableService *>
    #      QScxmlStateMachinePrivate::invokedServicesActualCalculation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate32invokedServicesActualCalcul'
        'ationEv',
    )
    from . import QScxmlInvokableService
    return QList[QScxmlInvokableService]._cuteOwning(address)

  def isRunnable(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::isRunnable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#isRunnable
    """
    #  bool QScxmlStateMachinePrivate::isRunnable() const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate10isRunnableEv',
    )

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::isPaused() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#isPaused
    """
    #  bool QScxmlStateMachinePrivate::isPaused() const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate8isPausedEv',
    )

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::isFinished() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#isFinished
    """
    #  bool QScxmlStateMachinePrivate::isFinished() const
    return self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate10isFinishedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsInvoked(self, invoked: bool) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::setIsInvoked(bool invoked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#setIsInvoked

    Parameters
    ----------

    invoked : bool
      Passed on as it is.
    """
    #  void QScxmlStateMachinePrivate::setIsInvoked(bool invoked)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate12setIsInvokedEb', invoked,
    )

  @overload(QScxmlEvent)
  @overload(NoneType)
  def setEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::setEvent(QScxmlEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#setEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::setEvent(QScxmlEvent *event)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate8setEventEP11QScxmlEvent',
        self._addressOf(event),
    )

  @overload(QScxmlDataModel)
  @overload(NoneType)
  def setDataModel(self, loader: Optional[QScxmlDataModel]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::setDataModel(QScxmlDataModel
    *loader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#setDataModel

    Parameters
    ----------

    loader : Optional[QScxmlDataModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::setDataModel(QScxmlDataModel *loader)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate12setDataModelEP15QScxmlDataMo'
        'del',
        self._addressOf(loader),
    )

  @overload(QScxmlTableData)
  @overload(NoneType)
  def setTableData(self, tableData: Optional[QScxmlTableData]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::setTableData(QScxmlTableData
    *tableData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#setTableData

    Parameters
    ----------

    tableData : Optional[QScxmlTableData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::setTableData(QScxmlTableData
    #      *tableData)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate12setTableDataEP15QScxmlTableD'
        'ata',
        self._addressOf(tableData),
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

  @overload(QMetaObject)
  @overload(NoneType)
  def __init__(self, qMetaObject: Optional[QMetaObject]) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlStateMachinePrivate::QScxmlStateMachinePrivate(const QMetaObject
    *qMetaObject)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Parameters
    ----------

    qMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlStateMachinePrivate::QScxmlStateMachinePrivate(const QMetaObject
    #      *qMetaObject)
    self._noteCreation(QScxmlStateMachinePrivate, lambda: Rituals.call(
        'ritual_ZN25QScxmlStateMachinePrivateC1EPK11QMetaObject',
        self._addressOf(qMetaObject, 'QMetaObject'),
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

  def q_func(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlStateMachinePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#q_func

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlStateMachinePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate6q_funcEv',
    )
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  def parserData(self) -> Optional[ParserData]:
    """
    Calls Qt's 'ParserData *QScxmlStateMachinePrivate::parserData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#parserData

    Returns
    -------

    Optional[ParserData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ParserData *QScxmlStateMachinePrivate::parserData()
    address = self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate10parserDataEv',
    )
    return QScxmlStateMachinePrivate.ParserData._cuteAt(address)

  @overload(int)
  def addService(self, invokingState: int) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::addService(int
    invokingState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#addService

    Parameters
    ----------

    invokingState : int
      Passed on as it is.
    """
    #  void QScxmlStateMachinePrivate::addService(int invokingState)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate10addServiceEi', invokingState,
    )

  @overload(int)
  def removeService(self, invokingState: int) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::removeService(int
    invokingState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#removeService

    Parameters
    ----------

    invokingState : int
      Passed on as it is.
    """
    #  void QScxmlStateMachinePrivate::removeService(int invokingState)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate13removeServiceEi',
        invokingState,
    )

  @overload(int)
  def serviceFactory(
      self,
      id: int,
  ) -> Optional[QScxmlInvokableServiceFactory]:
    """
    Calls Qt's 'QScxmlInvokableServiceFactory
    *QScxmlStateMachinePrivate::serviceFactory(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#serviceFactory

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QScxmlInvokableServiceFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlInvokableServiceFactory
    #      *QScxmlStateMachinePrivate::serviceFactory(int id)
    address = self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate14serviceFactoryEi', id,
    )
    from . import QScxmlInvokableServiceFactory
    return QScxmlInvokableServiceFactory._cuteAt(address)

  def executeInitialSetup(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachinePrivate::executeInitialSetup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#executeInitialSetup
    """
    #  bool QScxmlStateMachinePrivate::executeInitialSetup()
    return self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate19executeInitialSetupEv',
    )

  @overload(QScxmlEvent)
  @overload(NoneType)
  def routeEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::routeEvent(QScxmlEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#routeEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::routeEvent(QScxmlEvent *event)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate10routeEventEP11QScxmlEvent',
        self._addressOf(event),
    )

  @overload(QScxmlEvent)
  @overload(NoneType)
  def postEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::postEvent(QScxmlEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#postEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::postEvent(QScxmlEvent *event)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate9postEventEP11QScxmlEvent',
        self._addressOf(event),
    )

  @overload(QScxmlEvent)
  @overload(NoneType)
  def submitDelayedEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::submitDelayedEvent(QScxmlEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#submitDelayedEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::submitDelayedEvent(QScxmlEvent *event)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate18submitDelayedEventEP11QScxml'
        'Event',
        self._addressOf(event),
    )

  @overload(str, str)
  @overload(str, str, str)
  def submitError(self, type: str, msg: str, sendid: str = '') -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::submitError(const QString
    &type, const QString &msg, const QString &sendid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#submitError

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.

    sendid : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QScxmlStateMachinePrivate::submitError(const QString &type, const
    #      QString &msg, const QString &sendid)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate11submitErrorERK7QStringS2_S2_',
        type, msg, sendid,
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#start
    """
    #  void QScxmlStateMachinePrivate::start()
    self.uglySide.call('ritual_ZN25QScxmlStateMachinePrivate5startEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::pause()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#pause
    """
    #  void QScxmlStateMachinePrivate::pause()
    self.uglySide.call('ritual_ZN25QScxmlStateMachinePrivate5pauseEv')

  def processEvents(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::processEvents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#processEvents
    """
    #  void QScxmlStateMachinePrivate::processEvents()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate13processEventsEv',
    )

  def resetEvent(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::resetEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#resetEvent
    """
    #  void QScxmlStateMachinePrivate::resetEvent()
    self.uglySide.call('ritual_ZN25QScxmlStateMachinePrivate10resetEventEv')

  @overload(int, bool)
  def emitStateActive(self, stateIndex: int, active: bool) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::emitStateActive(int
    stateIndex, bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#emitStateActive

    Parameters
    ----------

    stateIndex : int
      Passed on as it is.

    active : bool
      Passed on as it is.
    """
    #  void QScxmlStateMachinePrivate::emitStateActive(int stateIndex, bool
    #      active)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate15emitStateActiveEib',
        stateIndex, active,
    )

  def emitInvokedServicesChanged(self) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::emitInvokedServicesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  void QScxmlStateMachinePrivate::emitInvokedServicesChanged()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate26emitInvokedServicesChangedEv',
    )

  @overload(QScxmlStateMachineInfo)
  @overload(NoneType)
  def attach(self, info: Optional[QScxmlStateMachineInfo]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::attach(QScxmlStateMachineInfo
    *info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#attach

    Parameters
    ----------

    info : Optional[QScxmlStateMachineInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::attach(QScxmlStateMachineInfo *info)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate6attachEP22QScxmlStateMachineI'
        'nfo',
        self._addressOf(info),
    )

  def updateMetaCache(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::updateMetaCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#updateMetaCache
    """
    #  void QScxmlStateMachinePrivate::updateMetaCache()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate15updateMetaCacheEv',
    )

  def exitInterpreter(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::exitInterpreter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#exitInterpreter
    """
    #  void QScxmlStateMachinePrivate::exitInterpreter()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate15exitInterpreterEv',
    )

  @overload(int)
  def returnDoneEvent(self, doneData: int) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::returnDoneEvent(QScxmlExecutableContent::
    ContainerId doneData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#returnDoneEvent

    Parameters
    ----------

    doneData : int
      Passed on as it is.
    """
    #  void QScxmlStateMachinePrivate::returnDoneEvent(
    #      QScxmlExecutableContent::ContainerId doneData)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate15returnDoneEventEi', doneData,
    )

  @overload(OrderedSet)
  @overload(NoneType)
  def removeConflictingTransitions(
      self,
      enabledTransitions: Optional[OrderedSet],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::removeConflictingTransitions(OrderedSet
    *enabledTransitions) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Parameters
    ----------

    enabledTransitions : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QScxmlStateMachinePrivate::removeConflictingTransitions(OrderedSet
    #      *enabledTransitions) const
    self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate28removeConflictingTransition'
        'sEPNS_10OrderedSetE',
        self._addressOf(enabledTransitions),
    )

  @overload(OrderedSet)
  def microstep(self, enabledTransitions: OrderedSet) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::microstep(const OrderedSet
    &enabledTransitions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#microstep

    Parameters
    ----------

    enabledTransitions : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.
    """
    #  void QScxmlStateMachinePrivate::microstep(const OrderedSet
    #      &enabledTransitions)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate9microstepERKNS_10OrderedSetE',
        self._valueOf(enabledTransitions),
    )

  @overload(OrderedSet)
  def exitStates(self, enabledTransitions: OrderedSet) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::exitStates(const OrderedSet
    &enabledTransitions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#exitStates

    Parameters
    ----------

    enabledTransitions : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.
    """
    #  void QScxmlStateMachinePrivate::exitStates(const OrderedSet
    #      &enabledTransitions)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate10exitStatesERKNS_10OrderedSet'
        'E',
        self._valueOf(enabledTransitions),
    )

  @overload(OrderedSet)
  def executeTransitionContent(self, enabledTransitions: OrderedSet) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::executeTransitionContent(const OrderedSet
    &enabledTransitions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Parameters
    ----------

    enabledTransitions : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.
    """
    #  void QScxmlStateMachinePrivate::executeTransitionContent(const
    #      OrderedSet &enabledTransitions)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate24executeTransitionContentERKN'
        'S_10OrderedSetE',
        self._valueOf(enabledTransitions),
    )

  @overload(OrderedSet)
  def enterStates(self, enabledTransitions: OrderedSet) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::enterStates(const OrderedSet
    &enabledTransitions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#enterStates

    Parameters
    ----------

    enabledTransitions : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.
    """
    #  void QScxmlStateMachinePrivate::enterStates(const OrderedSet
    #      &enabledTransitions)
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate11enterStatesERKNS_10OrderedSe'
        'tE',
        self._valueOf(enabledTransitions),
    )

  @overload(OrderedSet, OrderedSet, OrderedSet, HistoryContent)
  @overload(OrderedSet, OrderedSet, OrderedSet, NoneType)
  @overload(OrderedSet, OrderedSet, NoneType, HistoryContent)
  @overload(OrderedSet, OrderedSet, NoneType, NoneType)
  @overload(OrderedSet, NoneType, OrderedSet, HistoryContent)
  @overload(OrderedSet, NoneType, OrderedSet, NoneType)
  @overload(OrderedSet, NoneType, NoneType, HistoryContent)
  @overload(OrderedSet, NoneType, NoneType, NoneType)
  def computeEntrySet(
      self,
      enabledTransitions: OrderedSet,
      statesToEnter: Optional[OrderedSet],
      statesForDefaultEntry: Optional[OrderedSet],
      defaultHistoryContent: Optional[HistoryContent],
  ) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::computeEntrySet(const
    OrderedSet &enabledTransitions, OrderedSet *statesToEnter, OrderedSet
    *statesForDefaultEntry, HistoryContent *defaultHistoryContent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#computeEntrySet

    Parameters
    ----------

    enabledTransitions : OrderedSet
      Passed on as a value: Qt reads the C++
      QScxmlStateMachinePrivate::OrderedSet, which stays Python's own.

    statesToEnter : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    statesForDefaultEntry : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    defaultHistoryContent : Optional[HistoryContent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::computeEntrySet(const OrderedSet
    #      &enabledTransitions, OrderedSet *statesToEnter, OrderedSet
    #      *statesForDefaultEntry, HistoryContent *defaultHistoryContent)
    #      const
    self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate15computeEntrySetERKNS_10Orde'
        'redSetEPS0_S3_PNS_14HistoryContentE',
        self._valueOf(enabledTransitions), self._addressOf(statesToEnter),
        self._addressOf(statesForDefaultEntry),
        self._addressOf(defaultHistoryContent),
    )

  @overload(int, OrderedSet, OrderedSet, HistoryContent)
  @overload(int, OrderedSet, OrderedSet, NoneType)
  @overload(int, OrderedSet, NoneType, HistoryContent)
  @overload(int, OrderedSet, NoneType, NoneType)
  @overload(int, NoneType, OrderedSet, HistoryContent)
  @overload(int, NoneType, OrderedSet, NoneType)
  @overload(int, NoneType, NoneType, HistoryContent)
  @overload(int, NoneType, NoneType, NoneType)
  def addDescendantStatesToEnter(
      self,
      stateIndex: int,
      statesToEnter: Optional[OrderedSet],
      statesForDefaultEntry: Optional[OrderedSet],
      defaultHistoryContent: Optional[HistoryContent],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::addDescendantStatesToEnter(int stateIndex,
    OrderedSet *statesToEnter, OrderedSet *statesForDefaultEntry,
    HistoryContent *defaultHistoryContent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Parameters
    ----------

    stateIndex : int
      Passed on as it is.

    statesToEnter : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    statesForDefaultEntry : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    defaultHistoryContent : Optional[HistoryContent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::addDescendantStatesToEnter(int
    #      stateIndex, OrderedSet *statesToEnter, OrderedSet
    #      *statesForDefaultEntry, HistoryContent *defaultHistoryContent)
    #      const
    self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate26addDescendantStatesToEnterE'
        'iPNS_10OrderedSetES1_PNS_14HistoryContentE',
        stateIndex, self._addressOf(statesToEnter),
        self._addressOf(statesForDefaultEntry),
        self._addressOf(defaultHistoryContent),
    )

  @overload(int, int, OrderedSet, OrderedSet, HistoryContent)
  @overload(int, int, OrderedSet, OrderedSet, NoneType)
  @overload(int, int, OrderedSet, NoneType, HistoryContent)
  @overload(int, int, OrderedSet, NoneType, NoneType)
  @overload(int, int, NoneType, OrderedSet, HistoryContent)
  @overload(int, int, NoneType, OrderedSet, NoneType)
  @overload(int, int, NoneType, NoneType, HistoryContent)
  @overload(int, int, NoneType, NoneType, NoneType)
  def addAncestorStatesToEnter(
      self,
      stateIndex: int,
      ancestorIndex: int,
      statesToEnter: Optional[OrderedSet],
      statesForDefaultEntry: Optional[OrderedSet],
      defaultHistoryContent: Optional[HistoryContent],
  ) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::addAncestorStatesToEnter(int
    stateIndex, int ancestorIndex, OrderedSet *statesToEnter, OrderedSet
    *statesForDefaultEntry, HistoryContent *defaultHistoryContent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Parameters
    ----------

    stateIndex : int
      Passed on as it is.

    ancestorIndex : int
      Passed on as it is.

    statesToEnter : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    statesForDefaultEntry : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    defaultHistoryContent : Optional[HistoryContent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachinePrivate::addAncestorStatesToEnter(int
    #      stateIndex, int ancestorIndex, OrderedSet *statesToEnter,
    #      OrderedSet *statesForDefaultEntry, HistoryContent
    #      *defaultHistoryContent) const
    self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate24addAncestorStatesToEnterEii'
        'PNS_10OrderedSetES1_PNS_14HistoryContentE',
        stateIndex, ancestorIndex, self._addressOf(statesToEnter),
        self._addressOf(statesForDefaultEntry),
        self._addressOf(defaultHistoryContent),
    )

  @overload(OrderedSet, int)
  @overload(NoneType, int)
  def getEffectiveTargetStates(
      self,
      targets: Optional[OrderedSet],
      transitionIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlStateMachinePrivate::getEffectiveTargetStates(OrderedSet *targets,
    int transitionIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html

    Parameters
    ----------

    targets : Optional[OrderedSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transitionIndex : int
      Passed on as it is.
    """
    #  void QScxmlStateMachinePrivate::getEffectiveTargetStates(OrderedSet
    #      *targets, int transitionIndex) const
    self.uglySide.call(
        'ritual_ZNK25QScxmlStateMachinePrivate24getEffectiveTargetStatesEPN'
        'S_10OrderedSetEi',
        self._addressOf(targets), transitionIndex,
    )

  def isInitializedChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::isInitializedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  void QScxmlStateMachinePrivate::isInitializedChanged()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate20isInitializedChangedEv',
    )

  def initialValuesChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::initialValuesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html
    """
    #  void QScxmlStateMachinePrivate::initialValuesChanged()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate20initialValuesChangedEv',
    )

  def loaderChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachinePrivate::loaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineprivate.html#loaderChanged
    """
    #  void QScxmlStateMachinePrivate::loaderChanged()
    self.uglySide.call(
        'ritual_ZN25QScxmlStateMachinePrivate13loaderChangedEv',
    )

  @staticmethod
  def allInFinalStates(*__, **_) -> Never:
    """
    Qt's 'bool QScxmlStateMachinePrivate::allInFinalStates(const
    std::vector<int> &states) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.allInFinalStates' has no cute function "
        "yet. Qt's 'bool QScxmlStateMachinePrivate::allInFinalStates(const "
        "std::vector<int> &states) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def computeExitSet(*__, **_) -> Never:
    """
    Qt's 'void QScxmlStateMachinePrivate::computeExitSet(const OrderedSet
    &enabledTransitions, OrderedSet &statesToExit) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.computeExitSet' has no cute function "
        "yet. Qt's 'void QScxmlStateMachinePrivate::computeExitSet(const "
        "OrderedSet &enabledTransitions, OrderedSet &statesToExit) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def findLCCA(*__, **_) -> Never:
    """
    Qt's 'int QScxmlStateMachinePrivate::findLCCA(OrderedSet &&states)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.findLCCA' has no cute function yet. "
        "Qt's 'int QScxmlStateMachinePrivate::findLCCA(OrderedSet &&states) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getChildStates(*__, **_) -> Never:
    """
    Qt's 'std::vector<int> QScxmlStateMachinePrivate::getChildStates(const
    StateTable::State &state) const': the compiler refuses its ritual as it
    would be written here: use of undeclared identifier 'StateTable'; did you
    mean 'QScxmlExecutableContent::StateTable'?.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.getChildStates' has no cute function "
        "yet. Qt's 'std::vector<int> "
        "QScxmlStateMachinePrivate::getChildStates(const StateTable::State "
        "&state) const': the compiler refuses its ritual as it would be "
        "written here: use of undeclared identifier 'StateTable'; did you "
        "mean 'QScxmlExecutableContent::StateTable'?.")

  @staticmethod
  def getProperAncestors(*__, **_) -> Never:
    """
    Qt's 'void QScxmlStateMachinePrivate::getProperAncestors(std::vector<int>
    *ancestors, int state1, int state2) const': names 'std::vector<int>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.getProperAncestors' has no cute "
        "function yet. Qt's 'void "
        "QScxmlStateMachinePrivate::getProperAncestors(std::vector<int> "
        "*ancestors, int state1, int state2) const': names "
        "'std::vector<int>', which has no cute class yet.")

  @staticmethod
  def historyStates(*__, **_) -> Never:
    """
    Qt's 'std::vector<int> QScxmlStateMachinePrivate::historyStates(int
    stateIdx) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.historyStates' has no cute function "
        "yet. Qt's 'std::vector<int> "
        "QScxmlStateMachinePrivate::historyStates(int stateIdx) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def nameMatch(*__, **_) -> Never:
    """
    Qt's 'bool QScxmlStateMachinePrivate::nameMatch(const StateTable::Array
    &patterns, QScxmlEvent *event) const': the compiler refuses its ritual as
    it would be written here: use of undeclared identifier 'StateTable'; did
    you mean 'QScxmlExecutableContent::StateTable'?.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.nameMatch' has no cute function yet. "
        "Qt's 'bool QScxmlStateMachinePrivate::nameMatch(const "
        "StateTable::Array &patterns, QScxmlEvent *event) const': the "
        "compiler refuses its ritual as it would be written here: use of "
        "undeclared identifier 'StateTable'; did you mean "
        "'QScxmlExecutableContent::StateTable'?.")

  @staticmethod
  def selectTransitions(*__, **_) -> Never:
    """
    Qt's 'void QScxmlStateMachinePrivate::selectTransitions(OrderedSet
    &enabledTransitions, const std::vector<int> &configInDocumentOrder,
    QScxmlEvent *event) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.selectTransitions' has no cute function "
        "yet. Qt's 'void "
        "QScxmlStateMachinePrivate::selectTransitions(OrderedSet "
        "&enabledTransitions, const std::vector<int> "
        "&configInDocumentOrder, QScxmlEvent *event) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def someInFinalStates(*__, **_) -> Never:
    """
    Qt's 'bool QScxmlStateMachinePrivate::someInFinalStates(const
    std::vector<int> &states) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.someInFinalStates' has no cute function "
        "yet. Qt's 'bool QScxmlStateMachinePrivate::someInFinalStates(const "
        "std::vector<int> &states) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def stateNames(*__, **_) -> Never:
    """
    Qt's 'QStringList QScxmlStateMachinePrivate::stateNames(const
    std::vector<int> &stateIndexes) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachinePrivate.stateNames' has no cute function yet. "
        "Qt's 'QStringList QScxmlStateMachinePrivate::stateNames(const "
        "std::vector<int> &stateIndexes) const': takes a type Python has no "
        "way to hand over yet.")
