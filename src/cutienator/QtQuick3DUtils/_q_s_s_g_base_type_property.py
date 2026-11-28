"""
QSSGBaseTypeProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSSGBaseTypeProperty to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSSGRenderShaderValue

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVariant = WAIT['QVariant']


class QSSGBaseTypeProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGBaseTypeProperty: a plain Python object standing
  in front of one C++ QSSGBaseTypeProperty.

  C++ hands a QSSGBaseTypeProperty around as a copy, so every C++
  QSSGBaseTypeProperty behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGBaseTypeProperty yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGBaseTypeProperty::~QSSGBaseTypeProperty()': the destructor:
    Python removes its C++ QSSGBaseTypeProperty by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGBaseTypeProperty is created at the first use, not by
    'QSSGBaseTypeProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGBaseTypeProperty back gives a copy the ritual
    made for Python, in a new cute QSSGBaseTypeProperty.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGBaseTypeProperty'

  #  Qt's '~QSSGBaseTypeProperty()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGBaseTypeProperty behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSSGBaseTypePropertyD1Ev'

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
    'QSSGBaseTypeProperty::QSSGBaseTypeProperty()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbasetypeproperty.html#QSSGBaseTypeProperty
    """
    #  QSSGBaseTypeProperty::QSSGBaseTypeProperty()
    self._noteCreation(QSSGBaseTypeProperty, lambda: Rituals.call(
        'ritual_ZN20QSSGBaseTypePropertyC1Ev',
    ))

  @overload(QByteArray, QByteArray, QVariant, QSSGRenderShaderValue.Type)
  @overload(
      QByteArray, QByteArray, QVariant, QSSGRenderShaderValue.Type, int,
  )
  def __init__(
      self,
      name: QByteArray,
      typeName: QByteArray,
      value: QVariant,
      shaderDataType: QSSGRenderShaderValue.Type,
      pid: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGBaseTypeProperty::QSSGBaseTypeProperty(const QByteArray &name, const
    QByteArray &typeName, const QVariant &value, QSSGRenderShaderValue::Type
    shaderDataType, int pid)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbasetypeproperty.html#QSSGBaseTypeProperty

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    typeName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    shaderDataType : QSSGRenderShaderValue.Type
      Passed on as its number.

    pid : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QSSGBaseTypeProperty::QSSGBaseTypeProperty(const QByteArray &name,
    #      const QByteArray &typeName, const QVariant &value,
    #      QSSGRenderShaderValue::Type shaderDataType, int pid)
    self._noteCreation(QSSGBaseTypeProperty, lambda: Rituals.call(
        'ritual_ZN20QSSGBaseTypePropertyC1ERK10QByteArrayS2_RK8QVariantN21Q'
        'SSGRenderShaderValue4TypeEi',
        self._valueOf(name), self._valueOf(typeName), self._valueOf(value),
        shaderDataType.value, pid,
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
