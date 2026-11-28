"""
QScxmlDataModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmldatamodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScxmlDataModelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import DocumentModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QScxmlDataModel, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlDataModelPrivate(QObjectPrivate):
  """
  The cute side of Qt's QScxmlDataModelPrivate: a plain Python object
  standing in front of one C++ QScxmlDataModelPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QScxmlDataModelPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlDataModelPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'instantiateDataModel',
  'setStateMachine', 'emitStateMachineChanged',
  '_qt_property_m_stateMachine_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScxmlDataModel *QScxmlDataModelPrivate::q_func() const':
    takes in Python what 'QScxmlDataModel *QScxmlDataModelPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QScxmlDataModelPrivate is created at the first use, not by
    'QScxmlDataModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlDataModelPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(DocumentModel.Scxml.DataModelType)
  def instantiateDataModel(
      type: DocumentModel.Scxml.DataModelType,
  ) -> Optional[QScxmlDataModel]:
    """
    Calls Qt's 'QScxmlDataModel
    *QScxmlDataModelPrivate::instantiateDataModel(DocumentModel::Scxml::
    DataModelType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodelprivate.html#instantiateDataModel

    Parameters
    ----------

    type : DocumentModel.Scxml.DataModelType
      Passed on as its number.

    Returns
    -------

    Optional[QScxmlDataModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlDataModel
    #      *QScxmlDataModelPrivate::instantiateDataModel(DocumentModel::
    #      Scxml::DataModelType type)
    address = Rituals.call(
        'ritual_ZN22QScxmlDataModelPrivate20instantiateDataModelEN13Documen'
        'tModel5Scxml13DataModelTypeE',
        type.value,
    )
    from . import QScxmlDataModel
    return QScxmlDataModel._cuteAt(address)

  @staticmethod
  def _qt_property_m_stateMachine_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlDataModelPrivate::_qt_property_m_stateMachine_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodelprivate.html
    """
    #  size_t QScxmlDataModelPrivate::_qt_property_m_stateMachine_offset()
    return Rituals.call(
        'ritual_ZN22QScxmlDataModelPrivate34_qt_property_m_stateMachine_off'
        'setEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlDataModelPrivate'

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

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def setStateMachine(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlDataModelPrivate::setStateMachine(QScxmlStateMachine
    *stateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodelprivate.html#setStateMachine

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlDataModelPrivate::setStateMachine(QScxmlStateMachine
    #      *stateMachine)
    self.uglySide.call(
        'ritual_ZN22QScxmlDataModelPrivate15setStateMachineEP18QScxmlStateM'
        'achine',
        self._addressOf(stateMachine),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlDataModelPrivate::QScxmlDataModelPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodelprivate.html#QScxmlDataModelPrivate
    """
    #  QScxmlDataModelPrivate::QScxmlDataModelPrivate()
    self._noteCreation(QScxmlDataModelPrivate, lambda: Rituals.call(
        'ritual_ZN22QScxmlDataModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QScxmlDataModel]:
    """
    Calls Qt's 'QScxmlDataModel *QScxmlDataModelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmldatamodelprivate.html#q_func

    Returns
    -------

    Optional[QScxmlDataModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlDataModel *QScxmlDataModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QScxmlDataModelPrivate6q_funcEv',
    )
    from . import QScxmlDataModel
    return QScxmlDataModel._cuteAt(address)

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def emitStateMachineChanged(
      self,
      newValue: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlDataModelPrivate::emitStateMachineChanged(QScxmlStateMachine
    *newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmldatamodelprivate.html

    Parameters
    ----------

    newValue : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QScxmlDataModelPrivate::emitStateMachineChanged(QScxmlStateMachine
    #      *newValue)
    self.uglySide.call(
        'ritual_ZN22QScxmlDataModelPrivate23emitStateMachineChangedEP18QScx'
        'mlStateMachine',
        self._addressOf(newValue),
    )
