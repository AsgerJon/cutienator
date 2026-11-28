"""
QQmlAdaptorModelEngineData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodelenginedata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlAdaptorModelEngineData to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObjectBuilder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObjectBuilder = WAIT['QMetaObjectBuilder']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAdaptorModelEngineData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlAdaptorModelEngineData: a plain Python object
  standing in front of one C++ QQmlAdaptorModelEngineData.

  C++ hands a QQmlAdaptorModelEngineData around as a copy, so every C++
  QQmlAdaptorModelEngineData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlAdaptorModelEngineData that has a ritual and
  that Python can call so far, 1 name in all: 'addProperty'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlAdaptorModelEngineData::~QQmlAdaptorModelEngineData()': the
    destructor: Python removes its C++ QQmlAdaptorModelEngineData by it, and
    has no other use for it.

  What has no ritual
  ------------------

  4 of the 6 functions Qt declares: 3 leans on 'QQmlDelegateModelItemObject;
  1 a template.

  What to expect
  --------------

  - The C++ QQmlAdaptorModelEngineData is created at the first use, not by
    'QQmlAdaptorModelEngineData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlAdaptorModelEngineData back gives a copy the
    ritual made for Python, in a new cute QQmlAdaptorModelEngineData.
  - Each name of Qt's QQmlAdaptorModelEngineData that has no cute function
    yet, '__init__', 'get', 'get_index', 'setModelDataType', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaObjectBuilder, int, QByteArray, QByteArray, bool)
  @overload(NoneType, int, QByteArray, QByteArray, bool)
  def addProperty(
      builder: Optional[QMetaObjectBuilder],
      propertyId: int,
      propertyName: QByteArray,
      propertyType: QByteArray,
      isWritable: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlAdaptorModelEngineData::addProperty(QMetaObjectBuilder *builder, int
    propertyId, const QByteArray &propertyName, const QByteArray
    &propertyType, bool isWritable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmladaptormodelenginedata.html#addProperty

    Parameters
    ----------

    builder : Optional[QMetaObjectBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyId : int
      Passed on as it is.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    propertyType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    isWritable : bool
      Passed on as it is.
    """
    #  void QQmlAdaptorModelEngineData::addProperty(QMetaObjectBuilder
    #      *builder, int propertyId, const QByteArray &propertyName, const
    #      QByteArray &propertyType, bool isWritable)
    Rituals.call(
        'ritual_ZN26QQmlAdaptorModelEngineData11addPropertyEP18QMetaObjectB'
        'uilderiRK10QByteArrayS4_b',
        CuteMixin._addressOf(builder), propertyId,
        CuteMixin._valueOf(propertyName), CuteMixin._valueOf(propertyType),
        isWritable,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAdaptorModelEngineData'

  #  Qt's '~QQmlAdaptorModelEngineData()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlAdaptorModelEngineData behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQmlAdaptorModelEngineDataD1Ev'

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
    Qt's 'QQmlAdaptorModelEngineData::QQmlAdaptorModelEngineData(QV4::
    ExecutionEngine *v4)': leans on
    'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlAdaptorModelEngineData.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlAdaptorModelEngineData::QQmlAdaptorModelEngineData(QV4::Execut"
        "ionEngine *v4)': leans on "
        "'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def get(*__, **_) -> Never:
    """
    Qt's 'QQmlAdaptorModelEngineData
    *QQmlAdaptorModelEngineData::get(QV4::ExecutionEngine *engine)': leans on
    'QQmlDelegateModelItemObject::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlAdaptorModelEngineData.get' has no cute function yet. Qt's "
        "'QQmlAdaptorModelEngineData "
        "*QQmlAdaptorModelEngineData::get(QV4::ExecutionEngine *engine)': "
        "leans on 'QQmlDelegateModelItemObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def get_index(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlAdaptorModelEngineData::get_index(const
    QV4::FunctionObject *f, const QV4::Value *thisObject, const QV4::Value
    *a2, int a3)': leans on 'QQmlDelegateModelItemObject::static_vtbl', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQmlAdaptorModelEngineData.get_index' has no cute function yet. "
        "Qt's 'QV4::ReturnedValue "
        "QQmlAdaptorModelEngineData::get_index(const QV4::FunctionObject "
        "*f, const QV4::Value *thisObject, const QV4::Value *a2, int a3)': "
        "leans on 'QQmlDelegateModelItemObject::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setModelDataType(*__, **_) -> Never:
    """
    Qt's 'QQmlAdaptorModelEngineData::setModelDataType': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlAdaptorModelEngineData.setModelDataType' has no cute function "
        "yet. Qt's 'QQmlAdaptorModelEngineData::setModelDataType': a "
        "template: a pattern and no single function.")
