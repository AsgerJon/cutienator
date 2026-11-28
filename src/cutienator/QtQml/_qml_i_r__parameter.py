"""
QmlIR::Parameter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Parameter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Parameter(QV4.CompiledData.Parameter):
  """
  The cute side of Qt's QmlIR::Parameter: a plain Python object standing in
  front of one C++ QmlIR::Parameter.

  It is built on the cute 'QV4::CompiledData::Parameter', as Qt's
  QmlIR::Parameter is built on Qt's QV4::CompiledData::Parameter, and has
  everything that class has.

  C++ hands a QmlIR::Parameter around as a copy, so every C++
  QmlIR::Parameter behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QmlIR::Parameter that has a ritual and that Python
  can call so far, 2 names in all: 'stringToBuiltinType', 'initType'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlIR::Parameter::~Parameter()': the destructor: Python removes its
    C++ QmlIR::Parameter by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QmlIR::Parameter is created at the first use, not by
    'QmlIR::Parameter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::Parameter back gives a copy the ritual made
    for Python, in a new cute QmlIR::Parameter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def stringToBuiltinType(typeName: str) -> QV4.CompiledData.CommonType:
    """
    Calls Qt's 'QV4::CompiledData::CommonType
    QmlIR::Parameter::stringToBuiltinType(const QString &typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-parameter.html#stringToBuiltinType

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QV4.CompiledData.CommonType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QV4.CompiledData.CommonType(number)' gives.
    """
    #  QV4::CompiledData::CommonType
    #      QmlIR::Parameter::stringToBuiltinType(const QString &typeName)
    return QV4.CompiledData.CommonType(Rituals.call(
        'ritual_ZN5QmlIR9Parameter19stringToBuiltinTypeERK7QString',
        typeName,
    ))

  @staticmethod
  @overload(
      WAIT['QV4.CompiledData.ParameterType'], str, int,
      QV4.CompiledData.ParameterType.Flag,
  )
  @overload(NoneType, str, int, QV4.CompiledData.ParameterType.Flag)
  def initType(
      paramType: Optional[QV4.CompiledData.ParameterType],
      typeName: str,
      typeNameIndex: int,
      listFlag: QV4.CompiledData.ParameterType.Flag,
  ) -> bool:
    """
    Calls Qt's 'bool
    QmlIR::Parameter::initType(QV4::CompiledData::ParameterType *paramType,
    const QString &typeName, int typeNameIndex,
    QV4::CompiledData::ParameterType::Flag listFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-parameter.html#initType

    Parameters
    ----------

    paramType : Optional[QV4.CompiledData.ParameterType]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    typeNameIndex : int
      Passed on as it is.

    listFlag : QV4.CompiledData.ParameterType.Flag
      Passed on as its number.
    """
    #  bool QmlIR::Parameter::initType(QV4::CompiledData::ParameterType
    #      *paramType, const QString &typeName, int typeNameIndex,
    #      QV4::CompiledData::ParameterType::Flag listFlag)
    return Rituals.call(
        'ritual_ZN5QmlIR9Parameter8initTypeEPN3QV412CompiledData13Parameter'
        'TypeERK7QStringiNS3_4FlagE',
        CuteMixin._addressOf(paramType), typeName, typeNameIndex,
        listFlag.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::Parameter'

  #  Qt's '~QmlIR::Parameter()'. Naming it makes this a value class: Python
  #  owns every C++ QmlIR::Parameter behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR9ParameterD1Ev'

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
