"""
QOpcUaContentFilterElementResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuacontentfilterelementresult.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpcUaContentFilterElementResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaContentFilterElementResult: a plain Python
  object standing in front of one C++ QOpcUaContentFilterElementResult.

  C++ hands a QOpcUaContentFilterElementResult around as a copy, so every C++
  QOpcUaContentFilterElementResult behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaContentFilterElementResult that has a ritual
  and that Python can call so far, 2 names in all: 'statusCode',
  'setStatusCode'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaContentFilterElementResult
    &QOpcUaContentFilterElementResult::operator=(const
    QOpcUaContentFilterElementResult &a0)': assignment: Python binds a name
    and has no operator for it.
  - Qt's
    'QOpcUaContentFilterElementResult::~QOpcUaContentFilterElementResult()':
    the destructor: Python removes its C++ QOpcUaContentFilterElementResult
    by it, and has no other use for it.
  - Qt's 'QList<QOpcUa::UaStatusCode>
    QOpcUaContentFilterElementResult::operandStatusCodes() const': gives a
    type Python has no way to take yet.
  - Qt's 'QList<QOpcUa::UaStatusCode>
    &QOpcUaContentFilterElementResult::operandStatusCodesRef()': gives a type
    Python has no way to take yet.
  - Qt's 'void QOpcUaContentFilterElementResult::setOperandStatusCodes(const
    QList<QOpcUa::UaStatusCode> &operandStatusCodes)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaContentFilterElementResult is created at the first use, not
    by 'QOpcUaContentFilterElementResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaContentFilterElementResult back gives a copy
    the ritual made for Python, in a new cute
    QOpcUaContentFilterElementResult.
  - Each name of Qt's QOpcUaContentFilterElementResult that has no cute
    function yet, 'operandStatusCodes', 'operandStatusCodesRef',
    'setOperandStatusCodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaContentFilterElementResult'

  #  Qt's '~QOpcUaContentFilterElementResult()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaContentFilterElementResult behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QOpcUaContentFilterElementResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode
    QOpcUaContentFilterElementResult::statusCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelementresult.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaContentFilterElementResult::statusCode()
    #      const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK32QOpcUaContentFilterElementResult10statusCodeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void
    QOpcUaContentFilterElementResult::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelementresult.html

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaContentFilterElementResult::setStatusCode(QOpcUa::
    #      UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN32QOpcUaContentFilterElementResult13setStatusCodeEN6QOpcU'
        'a12UaStatusCodeE',
        statusCode.value,
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
    'QOpcUaContentFilterElementResult::QOpcUaContentFilterElementResult()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelementresult.html
    """
    #  QOpcUaContentFilterElementResult::QOpcUaContentFilterElementResult()
    self._noteCreation(
        QOpcUaContentFilterElementResult, lambda: Rituals.call(
            'ritual_ZN32QOpcUaContentFilterElementResultC1Ev',
        ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaContentFilterElementResult) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaContentFilterElementResult::QOpcUaContentFilterElementResult(const
    QOpcUaContentFilterElementResult &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelementresult.html

    Parameters
    ----------

    a0 : QOpcUaContentFilterElementResult
      Passed on as a value: Qt reads the C++
      QOpcUaContentFilterElementResult, which stays Python's own.
    """
    #  QOpcUaContentFilterElementResult::
    #      QOpcUaContentFilterElementResult(const
    #      QOpcUaContentFilterElementResult &a0)
    self._noteCreation(
        QOpcUaContentFilterElementResult, lambda: Rituals.call(
            'ritual_ZN32QOpcUaContentFilterElementResultC1ERKS_',
            self._valueOf(a0),
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

  @staticmethod
  def operandStatusCodes(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUa::UaStatusCode>
    QOpcUaContentFilterElementResult::operandStatusCodes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaContentFilterElementResult.operandStatusCodes' has no cute "
        "function yet. Qt's 'QList<QOpcUa::UaStatusCode> "
        "QOpcUaContentFilterElementResult::operandStatusCodes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def operandStatusCodesRef(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUa::UaStatusCode>
    &QOpcUaContentFilterElementResult::operandStatusCodesRef()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaContentFilterElementResult.operandStatusCodesRef' has no "
        "cute function yet. Qt's 'QList<QOpcUa::UaStatusCode> "
        "&QOpcUaContentFilterElementResult::operandStatusCodesRef()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setOperandStatusCodes(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaContentFilterElementResult::setOperandStatusCodes(const
    QList<QOpcUa::UaStatusCode> &operandStatusCodes)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaContentFilterElementResult.setOperandStatusCodes' has no "
        "cute function yet. Qt's 'void "
        "QOpcUaContentFilterElementResult::setOperandStatusCodes(const "
        "QList<QOpcUa::UaStatusCode> &operandStatusCodes)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QOpcUaContentFilterElementResult>': the list of
#  QOpcUaContentFilterElementResult, which
#  'QList[QOpcUaContentFilterElementResult]' gives. It is made here, so that
#  there is one as soon as there can be a QOpcUaContentFilterElementResult.
QList.createKind(
    QOpcUaContentFilterElementResult, 'value',
    make='ritual_list_make_QOpcUaContentFilterElementResult',
    add='ritual_list_add_QOpcUaContentFilterElementResult',
    size='ritual_list_size_QOpcUaContentFilterElementResult',
    at='ritual_list_at_QOpcUaContentFilterElementResult',
    drop='ritual_list_drop_QOpcUaContentFilterElementResult',
)
