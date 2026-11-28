"""
DynamicRoleModelNodeMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means DynamicRoleModelNodeMetaObject to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtQml import QQmlOpenMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DynamicRoleModelNodeMetaObject(QQmlOpenMetaObject):
  """
  The cute side of Qt's DynamicRoleModelNodeMetaObject: a plain Python object
  standing in front of one C++ DynamicRoleModelNodeMetaObject.

  It is built on the cute 'QQmlOpenMetaObject', as Qt's
  DynamicRoleModelNodeMetaObject is built on Qt's QQmlOpenMetaObject, and has
  everything that class has.

  C++ hands a DynamicRoleModelNodeMetaObject around as a copy, so every C++
  DynamicRoleModelNodeMetaObject behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's DynamicRoleModelNodeMetaObject that has a ritual and
  that Python can call so far, 2 names in all: 'propertyWrite',
  'propertyWritten'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DynamicRoleModelNodeMetaObject::~DynamicRoleModelNodeMetaObject()':
    the destructor: Python removes its C++ DynamicRoleModelNodeMetaObject by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'DynamicRoleModelNode.

  What to expect
  --------------

  - The C++ DynamicRoleModelNodeMetaObject is created at the first use, not
    by 'DynamicRoleModelNodeMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a DynamicRoleModelNodeMetaObject back gives a copy the
    ritual made for Python, in a new cute DynamicRoleModelNodeMetaObject.
  - Each name of Qt's DynamicRoleModelNodeMetaObject that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'DynamicRoleModelNodeMetaObject'

  #  A C++ DynamicRoleModelNodeMetaObject Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DynamicRoleModelNodeMetaObject'

  #  Qt's '~DynamicRoleModelNodeMetaObject()'. Naming it makes this a value
  #  class: Python owns every C++ DynamicRoleModelNodeMetaObject behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30DynamicRoleModelNodeMetaObjectD1Ev'

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
    Qt's 'DynamicRoleModelNodeMetaObject::DynamicRoleModelNodeMetaObject(
    DynamicRoleModelNode *object)': leans on
    'DynamicRoleModelNode::create(QMap<QString, QVariant> const&,
    QQmlListModel*)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'DynamicRoleModelNodeMetaObject.__init__' has no cute function "
        "yet. Qt's "
        "'DynamicRoleModelNodeMetaObject::DynamicRoleModelNodeMetaObject(Dyn"
        "amicRoleModelNode *object)': leans on "
        "'DynamicRoleModelNode::create(QMap<QString, QVariant> const&, "
        "QQmlListModel*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(int)
  def propertyWrite(self, index: int) -> None:
    """
    Calls Qt's 'void DynamicRoleModelNodeMetaObject::propertyWrite(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicrolemodelnodemetaobject.html#propertyWrite

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DynamicRoleModelNodeMetaObject::propertyWrite(int index)
    ritual = 'ritual_ZN30DynamicRoleModelNodeMetaObject13propertyWriteEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30DynamicRoleModelNodeMetaObject13propertyWriteEi')
    self.uglySide.call(ritual, index)

  @overload(int)
  def propertyWritten(self, index: int) -> None:
    """
    Calls Qt's 'void DynamicRoleModelNodeMetaObject::propertyWritten(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicrolemodelnodemetaobject.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DynamicRoleModelNodeMetaObject::propertyWritten(int index)
    self.uglySide.call(
        'ritual_ZN30DynamicRoleModelNodeMetaObject15propertyWrittenEi',
        index,
    )
