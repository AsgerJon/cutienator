"""
ScatterItemModelHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatteritemmodelhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ScatterItemModelHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import AbstractItemModelHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class ScatterItemModelHandler(AbstractItemModelHandler):
  """
  The cute side of Qt's ScatterItemModelHandler: a plain Python object
  standing in front of one C++ ScatterItemModelHandler.

  It is built on the cute 'AbstractItemModelHandler', as Qt's
  ScatterItemModelHandler is built on Qt's AbstractItemModelHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's ScatterItemModelHandler that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'handleRowsInserted',
  'handleRowsRemoved', 'resolveModel'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ScatterItemModelHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int ScatterItemModelHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'ScatterItemModelHandler::~ScatterItemModelHandler()': the
    destructor: Python never removes a C++ ScatterItemModelHandler.
  - Qt's 'void ScatterItemModelHandler::handleDataChanged(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'ScatterItemModelHandler; 1 Qt's library has no name for it, and its code
  in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ ScatterItemModelHandler is created at the first use, not by
    'ScatterItemModelHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ScatterItemModelHandler.
  - Qt tells when it has removed the C++ ScatterItemModelHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ScatterItemModelHandler that has no cute function yet,
    '__init__', 'modelPosToScatterItem', holds a function that raises
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
  __qt_class__ = 'ScatterItemModelHandler'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ ScatterItemModelHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ScatterItemModelHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ScatterItemModelHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatteritemmodelhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ScatterItemModelHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23ScatterItemModelHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'ScatterItemModelHandler::ScatterItemModelHandler(
    QItemModelScatterDataProxy *proxy, QObject *parent)': leans on
    'ScatterItemModelHandler::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'ScatterItemModelHandler.__init__' has no cute function yet. Qt's "
        "'ScatterItemModelHandler::ScatterItemModelHandler(QItemModelScatter"
        "DataProxy *proxy, QObject *parent)': leans on "
        "'ScatterItemModelHandler::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QModelIndex, int, int)
  def handleRowsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void ScatterItemModelHandler::handleRowsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatteritemmodelhandler.html#handleRowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void ScatterItemModelHandler::handleRowsInserted(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN23ScatterItemModelHandler18handleRowsInsertedERK11QModelI'
        'ndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23ScatterItemModelHandler18handleRowsInsertedERK11Q'
          'ModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int)
  def handleRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void ScatterItemModelHandler::handleRowsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatteritemmodelhandler.html#handleRowsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void ScatterItemModelHandler::handleRowsRemoved(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN23ScatterItemModelHandler17handleRowsRemovedERK11QModelIn'
        'dexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23ScatterItemModelHandler17handleRowsRemovedERK11QM'
          'odelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  def resolveModel(self) -> None:
    """
    Calls Qt's 'void ScatterItemModelHandler::resolveModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatteritemmodelhandler.html#resolveModel
    """
    #  void ScatterItemModelHandler::resolveModel()
    ritual = 'ritual_ZN23ScatterItemModelHandler12resolveModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23ScatterItemModelHandler12resolveModelEv'
    self.uglySide.call(ritual)

  @staticmethod
  def modelPosToScatterItem(*__, **_) -> Never:
    """
    Qt's 'void ScatterItemModelHandler::modelPosToScatterItem(int modelRow,
    int modelColumn, QScatterDataItem &item)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'toQuaternion'; did you mean 'QQuaternion'?.
    """
    raise NotImplementedError(
        "'ScatterItemModelHandler.modelPosToScatterItem' has no cute "
        "function yet. Qt's 'void "
        "ScatterItemModelHandler::modelPosToScatterItem(int modelRow, int "
        "modelColumn, QScatterDataItem &item)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'toQuaternion'; did you "
        "mean 'QQuaternion'?.")
