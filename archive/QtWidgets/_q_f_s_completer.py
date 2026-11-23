"""
QFSCompleter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfscompleter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFSCompleter to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QCompleter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QModelIndex
  from ..QtGui import QFileSystemModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileSystemModel = WAIT['QFileSystemModel']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFSCompleter(QCompleter):
  """
  The cute side of Qt's QFSCompleter: a plain Python object standing in front
  of one C++ QFSCompleter.

  It is built on the cute 'QCompleter', as Qt's QFSCompleter is built on Qt's
  QCompleter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFSCompleter that has a ritual and that Python can
  call so far, 2 names in all: 'pathFromIndex', 'splitPath'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QFSCompleter is created at the first use, not by
    'QFSCompleter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFSCompleter.
  - Qt tells when it has removed the C++ QFSCompleter. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFSCompleter'

  #  A C++ QFSCompleter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFSCompleter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def pathFromIndex(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFSCompleter::pathFromIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfscompleter.html#pathFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFSCompleter::pathFromIndex(const QModelIndex &index) const
    ritual = 'ritual_ZNK12QFSCompleter13pathFromIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QFSCompleter13pathFromIndexERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(str)
  def splitPath(self, path: str) -> QStringList:
    """
    Calls Qt's 'QStringList QFSCompleter::splitPath(const QString &path)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfscompleter.html#splitPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFSCompleter::splitPath(const QString &path) const
    address = self.uglySide.call(
        'ritual_ZNK12QFSCompleter9splitPathERK7QString', path,
    )
    return QStringList._cuteOwning(address)

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

  @overload(QFileSystemModel)
  @overload(NoneType)
  @overload(QFileSystemModel, QObject)
  @overload(QFileSystemModel, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      model: Optional[QFileSystemModel],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QFSCompleter::QFSCompleter(QFileSystemModel *model, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfscompleter.html#QFSCompleter

    Parameters
    ----------

    model : Optional[QFileSystemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFSCompleter::QFSCompleter(QFileSystemModel *model, QObject *parent)
    self._noteCreation(QFSCompleter, lambda: Rituals.call(
        'ritual_ZN12QFSCompleterC1EP16QFileSystemModelP7QObject',
        self._addressOf(model), self._addressOf(parent, 'QObject'),
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
