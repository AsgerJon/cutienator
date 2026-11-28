"""
QScxmlInternal::GeneratedTableData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmltabledata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScxmlInternal::GeneratedTableData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QScxmlExecutableContent, QScxmlTableData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QScxmlInvokableServiceFactory


class GeneratedTableData(QScxmlTableData):
  """
  The cute side of Qt's QScxmlInternal::GeneratedTableData: a plain Python
  object standing in front of one C++ QScxmlInternal::GeneratedTableData.

  It is built on the cute 'QScxmlTableData', as Qt's
  QScxmlInternal::GeneratedTableData is built on Qt's QScxmlTableData, and
  has everything that class has.

  C++ hands a QScxmlInternal::GeneratedTableData around as a copy, so every
  C++ QScxmlInternal::GeneratedTableData behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QScxmlInternal::GeneratedTableData that has a ritual
  and that Python can call so far, 7 names in all: 'string', 'evaluatorInfo',
  'assignmentInfo', 'foreachInfo', 'initialSetup', 'name', 'serviceFactory'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QScxmlInternal::GeneratedTableData::build(DocumentModel::ScxmlDocument
    *doc, GeneratedTableData *table, MetaDataInfo *metaDataInfo,
    DataModelInfo *dataModelInfo, CreateFactoryId func)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QString QScxmlInternal::GeneratedTableData::toString(const int
    *stateMachineTable)': names 'int', which has no cute class yet.
  - Qt's 'const qint32
    *QScxmlInternal::GeneratedTableData::stateMachineTable() const': gives
    'int', which has no cute class yet.
  - Qt's 'QScxmlInternal::GeneratedTableData::~GeneratedTableData()': the
    destructor: Python removes its C++ QScxmlInternal::GeneratedTableData by
    it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QScxmlInternal::GeneratedTableData is created at the first use,
    not by 'QScxmlInternal::GeneratedTableData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlInternal::GeneratedTableData back gives a copy
    the ritual made for Python, in a new cute
    QScxmlInternal::GeneratedTableData.
  - Each name of Qt's QScxmlInternal::GeneratedTableData that has no cute
    function yet, 'build', 'toString', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QScxmlInternal::GeneratedTableData, each a
  #  class in here as in C++.

  class DataModelInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlInternal::GeneratedTableData::DataModelInfo:
    a plain Python object standing in front of one C++
    QScxmlInternal::GeneratedTableData::DataModelInfo.

    C++ hands a QScxmlInternal::GeneratedTableData::DataModelInfo around as a
    copy, so every C++ QScxmlInternal::GeneratedTableData::DataModelInfo
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QScxmlInternal::GeneratedTableData::DataModelInfo
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QScxmlInternal::GeneratedTableData::DataModelInfo::~DataModelInfo()':
      the destructor: Python removes its C++
      QScxmlInternal::GeneratedTableData::DataModelInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QScxmlInternal::GeneratedTableData::DataModelInfo is created at
      the first use, not by
      'QScxmlInternal::GeneratedTableData::DataModelInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlInternal::GeneratedTableData::DataModelInfo
      back gives a copy the ritual made for Python, in a new cute
      QScxmlInternal::GeneratedTableData::DataModelInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlInternal::GeneratedTableData::DataModelInfo'

    #  Qt's '~QScxmlInternal::GeneratedTableData::DataModelInfo()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QScxmlInternal::GeneratedTableData::DataModelInfo behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN14QScxmlInternal18GeneratedTableData13DataModelInfoD1Ev')

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

  class MetaDataInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlInternal::GeneratedTableData::MetaDataInfo: a
    plain Python object standing in front of one C++
    QScxmlInternal::GeneratedTableData::MetaDataInfo.

    C++ hands a QScxmlInternal::GeneratedTableData::MetaDataInfo around as a
    copy, so every C++ QScxmlInternal::GeneratedTableData::MetaDataInfo
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QScxmlInternal::GeneratedTableData::MetaDataInfo yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QScxmlInternal::GeneratedTableData::MetaDataInfo::~MetaDataInfo()':
      the destructor: Python removes its C++
      QScxmlInternal::GeneratedTableData::MetaDataInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QScxmlInternal::GeneratedTableData::MetaDataInfo is created at
      the first use, not by
      'QScxmlInternal::GeneratedTableData::MetaDataInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlInternal::GeneratedTableData::MetaDataInfo
      back gives a copy the ritual made for Python, in a new cute
      QScxmlInternal::GeneratedTableData::MetaDataInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlInternal::GeneratedTableData::MetaDataInfo'

    #  Qt's '~QScxmlInternal::GeneratedTableData::MetaDataInfo()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QScxmlInternal::GeneratedTableData::MetaDataInfo behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN14QScxmlInternal18GeneratedTableData12MetaDataInfoD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInternal::GeneratedTableData'

  #  A C++ QScxmlInternal::GeneratedTableData Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlInternal_GeneratedTableData'

  #  Qt's '~QScxmlInternal::GeneratedTableData()'. Naming it makes this a
  #  value class: Python owns every C++ QScxmlInternal::GeneratedTableData
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN14QScxmlInternal18GeneratedTableDataD1Ev'

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
    QScxmlInternal::GeneratedTableData::string(QScxmlExecutableContent::
    StringId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html#string

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlInternal::GeneratedTableData::string(
    #      QScxmlExecutableContent::StringId id) const
    return self.uglySide.call(
        'ritual_ZNK14QScxmlInternal18GeneratedTableData6stringEi', id,
    )

  @overload(int)
  def evaluatorInfo(
      self,
      evaluatorId: int,
  ) -> QScxmlExecutableContent.EvaluatorInfo:
    """
    Calls Qt's 'QScxmlExecutableContent::EvaluatorInfo
    QScxmlInternal::GeneratedTableData::evaluatorInfo(
    QScxmlExecutableContent::EvaluatorId evaluatorId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html

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
    #      QScxmlInternal::GeneratedTableData::evaluatorInfo(
    #      QScxmlExecutableContent::EvaluatorId evaluatorId) const
    address = self.uglySide.call(
        'ritual_ZNK14QScxmlInternal18GeneratedTableData13evaluatorInfoEi',
        evaluatorId,
    )
    return QScxmlExecutableContent.EvaluatorInfo._cuteOwning(address)

  @overload(int)
  def assignmentInfo(
      self,
      assignmentId: int,
  ) -> QScxmlExecutableContent.AssignmentInfo:
    """
    Calls Qt's 'QScxmlExecutableContent::AssignmentInfo
    QScxmlInternal::GeneratedTableData::assignmentInfo(
    QScxmlExecutableContent::EvaluatorId assignmentId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html

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
    #      QScxmlInternal::GeneratedTableData::assignmentInfo(
    #      QScxmlExecutableContent::EvaluatorId assignmentId) const
    address = self.uglySide.call(
        'ritual_ZNK14QScxmlInternal18GeneratedTableData14assignmentInfoEi',
        assignmentId,
    )
    return QScxmlExecutableContent.AssignmentInfo._cuteOwning(address)

  @overload(int)
  def foreachInfo(
      self,
      foreachId: int,
  ) -> QScxmlExecutableContent.ForeachInfo:
    """
    Calls Qt's 'QScxmlExecutableContent::ForeachInfo
    QScxmlInternal::GeneratedTableData::foreachInfo(
    QScxmlExecutableContent::EvaluatorId foreachId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html#foreachInfo

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
    #      QScxmlInternal::GeneratedTableData::foreachInfo(
    #      QScxmlExecutableContent::EvaluatorId foreachId) const
    address = self.uglySide.call(
        'ritual_ZNK14QScxmlInternal18GeneratedTableData11foreachInfoEi',
        foreachId,
    )
    return QScxmlExecutableContent.ForeachInfo._cuteOwning(address)

  def initialSetup(self) -> int:
    """
    Calls Qt's 'QScxmlExecutableContent::ContainerId
    QScxmlInternal::GeneratedTableData::initialSetup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html
    """
    #  QScxmlExecutableContent::ContainerId
    #      QScxmlInternal::GeneratedTableData::initialSetup() const
    return self.uglySide.call(
        'ritual_ZNK14QScxmlInternal18GeneratedTableData12initialSetupEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QScxmlInternal::GeneratedTableData::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlInternal::GeneratedTableData::name() const
    return self.uglySide.call(
        'ritual_ZNK14QScxmlInternal18GeneratedTableData4nameEv',
    )

  @overload(int)
  def serviceFactory(
      self,
      id: int,
  ) -> Optional[QScxmlInvokableServiceFactory]:
    """
    Calls Qt's 'QScxmlInvokableServiceFactory
    *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-generatedtabledata.html

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
    #      *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const
    ritual = (
        'ritual_ZNK14QScxmlInternal18GeneratedTableData14serviceFactoryEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QScxmlInternal18GeneratedTableData14serviceFacto'
          'ryEi')
    address = self.uglySide.call(ritual, id)
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
  def build(*__, **_) -> Never:
    """
    Qt's 'void
    QScxmlInternal::GeneratedTableData::build(DocumentModel::ScxmlDocument
    *doc, GeneratedTableData *table, MetaDataInfo *metaDataInfo,
    DataModelInfo *dataModelInfo, CreateFactoryId func)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlInternal.GeneratedTableData.build' has no cute function "
        "yet. Qt's 'void "
        "QScxmlInternal::GeneratedTableData::build(DocumentModel::ScxmlDocum"
        "ent *doc, GeneratedTableData *table, MetaDataInfo *metaDataInfo, "
        "DataModelInfo *dataModelInfo, CreateFactoryId func)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'QString QScxmlInternal::GeneratedTableData::toString(const int
    *stateMachineTable)': names 'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScxmlInternal.GeneratedTableData.toString' has no cute function "
        "yet. Qt's 'QString "
        "QScxmlInternal::GeneratedTableData::toString(const int "
        "*stateMachineTable)': names 'int', which has no cute class yet.")
