"""
QScxmlTableData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmltabledata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QScxmlInvokableServiceFactory


class QScxmlTableData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlTableData: a plain Python object standing in
  front of one C++ QScxmlTableData.

  What exists
  -----------

  Every function of Qt's QScxmlTableData that has a ritual and that Python
  can call so far, 7 names in all: 'string', 'evaluatorInfo',
  'assignmentInfo', 'foreachInfo', 'initialSetup', 'name', 'serviceFactory'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlTableData::~QScxmlTableData()': the destructor: Python never
    removes a C++ QScxmlTableData.
  - Qt's 'const qint32 *QScxmlTableData::stateMachineTable() const': gives
    'int', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QScxmlTableData is created at the first use, not by
    'QScxmlTableData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlTableData.
  - Each name of Qt's QScxmlTableData that has no cute function yet,
    'dataNames', 'instructions', 'stateMachineTable', holds a function that
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
  __qt_class__ = 'QScxmlTableData'

  #  A C++ QScxmlTableData Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlTableData'

  #  The functions Qt calls itself that QScxmlTableData is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'instructions': (
          'QScxmlExecutableContent::InstructionId '
          '*QScxmlTableData::instructions() const',
      ),
      'dataNames': (
          'QScxmlExecutableContent::StringId '
          '*QScxmlTableData::dataNames(int *) const',
      ),
      'stateMachineTable': (
          'const qint32 *QScxmlTableData::stateMachineTable() const',
      ),
  }

  #  The functions Qt calls itself that QScxmlTableData is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'string': (
          ('_ZNK15QScxmlTableData6stringEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'evaluatorInfo': (
          ('_ZNK15QScxmlTableData13evaluatorInfoEi',
           ('address', 'value',
            'QtScxml:QScxmlExecutableContent.EvaluatorInfo'),
           (
               ('int', 'number', ''),
           )),
      ),
      'assignmentInfo': (
          ('_ZNK15QScxmlTableData14assignmentInfoEi',
           ('address', 'value',
            'QtScxml:QScxmlExecutableContent.AssignmentInfo'),
           (
               ('int', 'number', ''),
           )),
      ),
      'foreachInfo': (
          ('_ZNK15QScxmlTableData11foreachInfoEi',
           ('address', 'value',
            'QtScxml:QScxmlExecutableContent.ForeachInfo'),
           (
               ('int', 'number', ''),
           )),
      ),
      'initialSetup': (
          ('_ZNK15QScxmlTableData12initialSetupEv',
           ('int', 'number', ''),
           ()),
      ),
      'name': (
          ('_ZNK15QScxmlTableData4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'serviceFactory': (
          ('_ZNK15QScxmlTableData14serviceFactoryEi',
           ('address', 'address', 'QtScxml:QScxmlInvokableServiceFactory'),
           (
               ('int', 'number', ''),
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

  @overload(int)
  def string(self, id: int) -> str:
    """
    Calls Qt's 'QString
    QScxmlTableData::string(QScxmlExecutableContent::StringId id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmltabledata.html#string

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlTableData::string(QScxmlExecutableContent::StringId id)
    #      const
    return self.uglySide.call('ritual_ZNK15QScxmlTableData6stringEi', id)

  @overload(int)
  def evaluatorInfo(
      self,
      evaluatorId: int,
  ) -> QScxmlExecutableContent.EvaluatorInfo:
    """
    Calls Qt's 'QScxmlExecutableContent::EvaluatorInfo
    QScxmlTableData::evaluatorInfo(QScxmlExecutableContent::EvaluatorId
    evaluatorId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmltabledata.html#evaluatorInfo

    Parameters
    ----------

    evaluatorId : int
      Passed on as it is.

    Returns
    -------

    QScxmlExecutableContent.EvaluatorInfo
      A new cute QScxmlExecutableContent::EvaluatorInfo around the copy Qt
      gave back. Python owns it.
    """
    #  QScxmlExecutableContent::EvaluatorInfo
    #      QScxmlTableData::evaluatorInfo(QScxmlExecutableContent::
    #      EvaluatorId evaluatorId) const
    address = self.uglySide.call(
        'ritual_ZNK15QScxmlTableData13evaluatorInfoEi', evaluatorId,
    )
    return QScxmlExecutableContent.EvaluatorInfo._cuteOwning(address)

  @overload(int)
  def assignmentInfo(
      self,
      assignmentId: int,
  ) -> QScxmlExecutableContent.AssignmentInfo:
    """
    Calls Qt's 'QScxmlExecutableContent::AssignmentInfo
    QScxmlTableData::assignmentInfo(QScxmlExecutableContent::EvaluatorId
    assignmentId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmltabledata.html#assignmentInfo

    Parameters
    ----------

    assignmentId : int
      Passed on as it is.

    Returns
    -------

    QScxmlExecutableContent.AssignmentInfo
      A new cute QScxmlExecutableContent::AssignmentInfo around the copy Qt
      gave back. Python owns it.
    """
    #  QScxmlExecutableContent::AssignmentInfo
    #      QScxmlTableData::assignmentInfo(QScxmlExecutableContent::
    #      EvaluatorId assignmentId) const
    address = self.uglySide.call(
        'ritual_ZNK15QScxmlTableData14assignmentInfoEi', assignmentId,
    )
    return QScxmlExecutableContent.AssignmentInfo._cuteOwning(address)

  @overload(int)
  def foreachInfo(
      self,
      foreachId: int,
  ) -> QScxmlExecutableContent.ForeachInfo:
    """
    Calls Qt's 'QScxmlExecutableContent::ForeachInfo
    QScxmlTableData::foreachInfo(QScxmlExecutableContent::EvaluatorId
    foreachId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmltabledata.html#foreachInfo

    Parameters
    ----------

    foreachId : int
      Passed on as it is.

    Returns
    -------

    QScxmlExecutableContent.ForeachInfo
      A new cute QScxmlExecutableContent::ForeachInfo around the copy Qt gave
      back. Python owns it.
    """
    #  QScxmlExecutableContent::ForeachInfo
    #      QScxmlTableData::foreachInfo(QScxmlExecutableContent::EvaluatorId
    #      foreachId) const
    address = self.uglySide.call(
        'ritual_ZNK15QScxmlTableData11foreachInfoEi', foreachId,
    )
    return QScxmlExecutableContent.ForeachInfo._cuteOwning(address)

  def initialSetup(self) -> int:
    """
    Calls Qt's 'QScxmlExecutableContent::ContainerId
    QScxmlTableData::initialSetup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmltabledata.html#initialSetup
    """
    #  QScxmlExecutableContent::ContainerId QScxmlTableData::initialSetup()
    #      const
    return self.uglySide.call('ritual_ZNK15QScxmlTableData12initialSetupEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QScxmlTableData::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmltabledata.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlTableData::name() const
    return self.uglySide.call('ritual_ZNK15QScxmlTableData4nameEv')

  @overload(int)
  def serviceFactory(
      self,
      id: int,
  ) -> Optional[QScxmlInvokableServiceFactory]:
    """
    Calls Qt's 'QScxmlInvokableServiceFactory
    *QScxmlTableData::serviceFactory(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmltabledata.html#serviceFactory

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
    #  QScxmlInvokableServiceFactory *QScxmlTableData::serviceFactory(int id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QScxmlTableData14serviceFactoryEi', id,
    )
    from . import QScxmlInvokableServiceFactory
    return QScxmlInvokableServiceFactory._cuteAt(address)

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

  @staticmethod
  def dataNames(*__, **_) -> Never:
    """
    Qt's 'QScxmlExecutableContent::StringId *QScxmlTableData::dataNames(int
    *count) const': takes or gives a type that cannot be passed yet:
    QScxmlExecutableContent::StringId *.
    """
    raise NotImplementedError(
        "'QScxmlTableData.dataNames' has no cute function yet. Qt's "
        "'QScxmlExecutableContent::StringId *QScxmlTableData::dataNames(int "
        "*count) const': takes or gives a type that cannot be passed yet: "
        "QScxmlExecutableContent::StringId *.")

  @staticmethod
  def instructions(*__, **_) -> Never:
    """
    Qt's 'QScxmlExecutableContent::InstructionId
    *QScxmlTableData::instructions() const': takes or gives a type that
    cannot be passed yet: QScxmlExecutableContent::InstructionId *.
    """
    raise NotImplementedError(
        "'QScxmlTableData.instructions' has no cute function yet. Qt's "
        "'QScxmlExecutableContent::InstructionId "
        "*QScxmlTableData::instructions() const': takes or gives a type "
        "that cannot be passed yet: QScxmlExecutableContent::InstructionId "
        "*.")

  @staticmethod
  def stateMachineTable(*__, **_) -> Never:
    """
    Qt's 'const qint32 *QScxmlTableData::stateMachineTable() const': gives
    'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScxmlTableData.stateMachineTable' has no cute function yet. Qt's "
        "'const qint32 *QScxmlTableData::stateMachineTable() const': gives "
        "'int', which has no cute class yet.")
