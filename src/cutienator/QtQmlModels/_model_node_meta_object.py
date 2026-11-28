"""
ModelNodeMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means ModelNodeMetaObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from ..QtQml import QQmlOpenMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ModelNodeMetaObject(QQmlOpenMetaObject):
  """
  The cute side of Qt's ModelNodeMetaObject: a plain Python object standing
  in front of one C++ ModelNodeMetaObject.

  It is built on the cute 'QQmlOpenMetaObject', as Qt's ModelNodeMetaObject
  is built on Qt's QQmlOpenMetaObject, and has everything that class has.

  C++ hands a ModelNodeMetaObject around as a copy, so every C++
  ModelNodeMetaObject behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ModelNodeMetaObject that has a ritual and that
  Python can call so far, 6 names in all: 'toDynamicMetaObject', 'get',
  'updateValues', 'initialized', 'propertyWritten', 'initialize'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ModelNodeMetaObject::~ModelNodeMetaObject()': the destructor:
    Python removes its C++ ModelNodeMetaObject by it, and has no other use
    for it.
  - Qt's 'void ModelNodeMetaObject::updateValues(const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void ModelNodeMetaObject::emitDirectNotifies(const int
    *changedRoles, int roleCount)': names 'int', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 leans on 'ModelNodeMetaObject.

  What to expect
  --------------

  - The C++ ModelNodeMetaObject is created at the first use, not by
    'ModelNodeMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ModelNodeMetaObject back gives a copy the ritual made
    for Python, in a new cute ModelNodeMetaObject.
  - Each name of Qt's ModelNodeMetaObject that has no cute function yet,
    '__init__', 'emitDirectNotifies', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def get(obj: Optional[QObject]) -> Optional[ModelNodeMetaObject]:
    """
    Calls Qt's 'ModelNodeMetaObject *ModelNodeMetaObject::get(QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/modelnodemetaobject.html#get

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ModelNodeMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ModelNodeMetaObject *ModelNodeMetaObject::get(QObject *obj)
    address = Rituals.call(
        'ritual_ZN19ModelNodeMetaObject3getEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    return ModelNodeMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ModelNodeMetaObject'

  #  A C++ ModelNodeMetaObject Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ModelNodeMetaObject'

  #  Qt's '~ModelNodeMetaObject()'. Naming it makes this a value class:
  #  Python owns every C++ ModelNodeMetaObject behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19ModelNodeMetaObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool ModelNodeMetaObject::initialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/modelnodemetaobject.html#initialized
    """
    #  bool ModelNodeMetaObject::initialized() const
    return self.uglySide.call(
        'ritual_ZNK19ModelNodeMetaObject11initializedEv',
    )

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
    Qt's 'ModelNodeMetaObject::ModelNodeMetaObject(QObject *object,
    QQmlListModel *model, int elementIndex)': leans on
    'ModelNodeMetaObject::toDynamicMetaObject(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'ModelNodeMetaObject.__init__' has no cute function yet. Qt's "
        "'ModelNodeMetaObject::ModelNodeMetaObject(QObject *object, "
        "QQmlListModel *model, int elementIndex)': leans on "
        "'ModelNodeMetaObject::toDynamicMetaObject(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QObject)
  @overload(NoneType)
  def toDynamicMetaObject(
      self,
      object: Optional[QObject],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'QMetaObject *ModelNodeMetaObject::toDynamicMetaObject(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/modelnodemetaobject.html#toDynamicMetaObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetaObject *ModelNodeMetaObject::toDynamicMetaObject(QObject *object)
    address = self.uglySide.call(
        'ritual_ZN19ModelNodeMetaObject19toDynamicMetaObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )
    return QMetaObject._cuteAt(address)

  def updateValues(self) -> None:
    """
    Calls Qt's 'void ModelNodeMetaObject::updateValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/modelnodemetaobject.html#updateValues
    """
    #  void ModelNodeMetaObject::updateValues()
    self.uglySide.call('ritual_ZN19ModelNodeMetaObject12updateValuesEv')

  @overload(int)
  def propertyWritten(self, index: int) -> None:
    """
    Calls Qt's 'void ModelNodeMetaObject::propertyWritten(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/modelnodemetaobject.html#propertyWritten

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void ModelNodeMetaObject::propertyWritten(int index)
    self.uglySide.call(
        'ritual_ZN19ModelNodeMetaObject15propertyWrittenEi', index,
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void ModelNodeMetaObject::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/modelnodemetaobject.html#initialize
    """
    #  void ModelNodeMetaObject::initialize()
    self.uglySide.call('ritual_ZN19ModelNodeMetaObject10initializeEv')

  @staticmethod
  def emitDirectNotifies(*__, **_) -> Never:
    """
    Qt's 'void ModelNodeMetaObject::emitDirectNotifies(const int
    *changedRoles, int roleCount)': names 'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'ModelNodeMetaObject.emitDirectNotifies' has no cute function yet. "
        "Qt's 'void ModelNodeMetaObject::emitDirectNotifies(const int "
        "*changedRoles, int roleCount)': names 'int', which has no cute "
        "class yet.")
