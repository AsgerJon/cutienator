"""
VDMListDelegateDataType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means VDMListDelegateDataType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractDynamicMetaObject, QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VDMListDelegateDataType(QAbstractDynamicMetaObject):
  """
  The cute side of Qt's VDMListDelegateDataType: a plain Python object
  standing in front of one C++ VDMListDelegateDataType.

  What exists
  -----------

  Every function of Qt's VDMListDelegateDataType that has a ritual and that
  Python can call so far, 3 names in all: 'metaObjectFromType',
  'createMissingProperties', 'createProperty'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void VDMListDelegateDataType::cleanup(QQmlAdaptorModel &a0) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'int VDMListDelegateDataType::rowCount(const QQmlAdaptorModel
    &model) const': takes a type Python has no way to hand over yet.
  - Qt's 'int VDMListDelegateDataType::columnCount(const QQmlAdaptorModel
    &model) const': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant VDMListDelegateDataType::value(const QQmlAdaptorModel
    &model, int index, const QString &role) const': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  11 of the 18 functions Qt declares: 5 a template; 4 leans on
  'QQmlDMListAccessorData; 1 cannot be called and cannot be called through
  the meta-object and cannot be copied; 1 leans on 'vtable for
  QQmlDMListAccessorData', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ VDMListDelegateDataType is created at the first use, not by
    'VDMListDelegateDataType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ VDMListDelegateDataType.
  - Each name of Qt's VDMListDelegateDataType that has no cute function yet,
    '__init__', 'createPropertyIfMissing', 'emitAllSignals', 'setValue',
    'toQString', 'toUtf8', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaType)
  def metaObjectFromType(type: QMetaType) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *VDMListDelegateDataType::metaObjectFromType(QMetaType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/vdmlistdelegatedatatype.html#metaObjectFromType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *VDMListDelegateDataType::metaObjectFromType(QMetaType type)
    address = Rituals.call(
        'ritual_ZN23VDMListDelegateDataType18metaObjectFromTypeE9QMetaType',
        CuteMixin._valueOf(type),
    )
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'VDMListDelegateDataType'

  #  Qt's VDMListDelegateDataType is built on more than one class. The part
  #  of a C++ VDMListDelegateDataType that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractDynamicMetaObject':
          'ritual_cast_VDMListDelegateDataType_QAbstractDynamicMetaObject',
  }

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'VDMListDelegateDataType::VDMListDelegateDataType(QQmlAdaptorModel
    *model)': leans on 'QQmlDMListAccessorData::modelDataChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'VDMListDelegateDataType.__init__' has no cute function yet. Qt's "
        "'VDMListDelegateDataType::VDMListDelegateDataType(QQmlAdaptorModel "
        "*model)': leans on 'QQmlDMListAccessorData::modelDataChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QVariant)
  @overload(NoneType)
  def createMissingProperties(self, row: Optional[QVariant]) -> None:
    """
    Calls Qt's 'void VDMListDelegateDataType::createMissingProperties(const
    QVariant *row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/vdmlistdelegatedatatype.html

    Parameters
    ----------

    row : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void VDMListDelegateDataType::createMissingProperties(const QVariant
    #      *row)
    self.uglySide.call(
        'ritual_ZN23VDMListDelegateDataType23createMissingPropertiesEPK8QVa'
        'riant',
        self._addressOf(row),
    )

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def createProperty(self, name: Optional[str], a1: Optional[str]) -> int:
    """
    Calls Qt's 'int VDMListDelegateDataType::createProperty(const char *name,
    const char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/vdmlistdelegatedatatype.html#createProperty

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int VDMListDelegateDataType::createProperty(const char *name, const
    #      char *a1)
    return self.uglySide.call(
        'ritual_ZN23VDMListDelegateDataType14createPropertyEPKcS1_',
        self._bytesOf(name), self._bytesOf(a1),
    )

  @staticmethod
  def createPropertyIfMissing(*__, **_) -> Never:
    """
    Qt's 'VDMListDelegateDataType::createPropertyIfMissing': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'VDMListDelegateDataType.createPropertyIfMissing' has no cute "
        "function yet. Qt's "
        "'VDMListDelegateDataType::createPropertyIfMissing': a template: a "
        "pattern and no single function.")

  @staticmethod
  def emitAllSignals(*__, **_) -> Never:
    """
    Qt's 'void VDMListDelegateDataType::emitAllSignals(QQmlDMListAccessorData
    *accessor) const': leans on 'QQmlDMListAccessorData::modelDataChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'VDMListDelegateDataType.emitAllSignals' has no cute function yet. "
        "Qt's 'void "
        "VDMListDelegateDataType::emitAllSignals(QQmlDMListAccessorData "
        "*accessor) const': leans on "
        "'QQmlDMListAccessorData::modelDataChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setValue(*__, **_) -> Never:
    """
    Qt's 'VDMListDelegateDataType::setValue': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'VDMListDelegateDataType.setValue' has no cute function yet. Qt's "
        "'VDMListDelegateDataType::setValue': a template: a pattern and no "
        "single function.")

  @staticmethod
  def toQString(*__, **_) -> Never:
    """
    Qt's 'VDMListDelegateDataType::toQString': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'VDMListDelegateDataType.toQString' has no cute function yet. Qt's "
        "'VDMListDelegateDataType::toQString': a template: a pattern and no "
        "single function.")

  @staticmethod
  def toUtf8(*__, **_) -> Never:
    """
    Qt's 'VDMListDelegateDataType::toUtf8': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'VDMListDelegateDataType.toUtf8' has no cute function yet. Qt's "
        "'VDMListDelegateDataType::toUtf8': a template: a pattern and no "
        "single function.")
