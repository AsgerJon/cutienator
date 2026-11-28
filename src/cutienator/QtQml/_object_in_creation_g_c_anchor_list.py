"""
ObjectInCreationGCAnchorList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means ObjectInCreationGCAnchorList to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ObjectInCreationGCAnchorList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ObjectInCreationGCAnchorList: a plain Python object
  standing in front of one C++ ObjectInCreationGCAnchorList.

  C++ hands a ObjectInCreationGCAnchorList around as a copy, so every C++
  ObjectInCreationGCAnchorList behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's ObjectInCreationGCAnchorList that has a ritual and
  that Python can call so far, 2 names in all: 'trackObject', 'canTrack'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ObjectInCreationGCAnchorList::ObjectInCreationGCAnchorList(const
    QV4::Scope &scope)': takes a type Python has no way to hand over yet.
  - Qt's 'ObjectInCreationGCAnchorList::~ObjectInCreationGCAnchorList()': the
    destructor: Python removes its C++ ObjectInCreationGCAnchorList by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ ObjectInCreationGCAnchorList is created at the first use, not by
    'ObjectInCreationGCAnchorList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ObjectInCreationGCAnchorList back gives a copy the
    ritual made for Python, in a new cute ObjectInCreationGCAnchorList.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ObjectInCreationGCAnchorList'

  #  Qt's '~ObjectInCreationGCAnchorList()'. Naming it makes this a value
  #  class: Python owns every C++ ObjectInCreationGCAnchorList behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28ObjectInCreationGCAnchorListD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canTrack(self) -> bool:
    """
    Calls Qt's 'bool ObjectInCreationGCAnchorList::canTrack() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/objectincreationgcanchorlist.html#canTrack
    """
    #  bool ObjectInCreationGCAnchorList::canTrack() const
    return self.uglySide.call(
        'ritual_ZNK28ObjectInCreationGCAnchorList8canTrackEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'ObjectInCreationGCAnchorList::ObjectInCreationGCAnchorList()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/objectincreationgcanchorlist.html
    """
    #  ObjectInCreationGCAnchorList::ObjectInCreationGCAnchorList()
    self._noteCreation(ObjectInCreationGCAnchorList, lambda: Rituals.call(
        'ritual_ZN28ObjectInCreationGCAnchorListC1Ev',
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

  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def trackObject(
      self,
      engine: Optional[QV4.ExecutionEngine],
      instance: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    ObjectInCreationGCAnchorList::trackObject(QV4::ExecutionEngine *engine,
    QObject *instance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/objectincreationgcanchorlist.html#trackObject

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ObjectInCreationGCAnchorList::trackObject(QV4::ExecutionEngine
    #      *engine, QObject *instance)
    self.uglySide.call(
        'ritual_ZN28ObjectInCreationGCAnchorList11trackObjectEPN3QV415Execu'
        'tionEngineEP7QObject',
        self._addressOf(engine), self._addressOf(instance, 'QObject'),
    )
