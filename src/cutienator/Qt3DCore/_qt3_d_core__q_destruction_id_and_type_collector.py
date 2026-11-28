"""
Qt3DCore::QDestructionIdAndTypeCollector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qdestructionidandtypecollector_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DCore::QDestructionIdAndTypeCollector to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDestructionIdAndTypeCollector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QDestructionIdAndTypeCollector: a plain
  Python object standing in front of one C++
  Qt3DCore::QDestructionIdAndTypeCollector.

  C++ hands a Qt3DCore::QDestructionIdAndTypeCollector around as a copy, so
  every C++ Qt3DCore::QDestructionIdAndTypeCollector behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QDestructionIdAndTypeCollector that has a
  ritual and that Python can call so far, 1 name in all: 'collectIdAndType'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QNodeIdTypePair>
    Qt3DCore::QDestructionIdAndTypeCollector::subtreeIdsAndTypes() const':
    gives a type Python has no way to take yet.
  - Qt's 'Qt3DCore::QDestructionIdAndTypeCollector::
    ~QDestructionIdAndTypeCollector()': the destructor: Python removes its
    C++ Qt3DCore::QDestructionIdAndTypeCollector by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DCore::QDestructionIdAndTypeCollector is created at the first
    use, not by 'Qt3DCore::QDestructionIdAndTypeCollector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QDestructionIdAndTypeCollector back gives a
    copy the ritual made for Python, in a new cute
    Qt3DCore::QDestructionIdAndTypeCollector.
  - Each name of Qt's Qt3DCore::QDestructionIdAndTypeCollector that has no
    cute function yet, 'subtreeIdsAndTypes', holds a function that raises
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
  __qt_class__ = 'Qt3DCore::QDestructionIdAndTypeCollector'

  #  Qt's '~Qt3DCore::QDestructionIdAndTypeCollector()'. Naming it makes this
  #  a value class: Python owns every C++
  #  Qt3DCore::QDestructionIdAndTypeCollector behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN8Qt3DCore30QDestructionIdAndTypeCollectorD1Ev')

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

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def __init__(self, rootNode: Optional[Qt3DCore.QNode]) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QDestructionIdAndTypeCollector::
    QDestructionIdAndTypeCollector(QNode *rootNode)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdestructionidandtypecollector.html

    Parameters
    ----------

    rootNode : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DCore::QDestructionIdAndTypeCollector::
    #      QDestructionIdAndTypeCollector(QNode *rootNode)
    self._noteCreation(QDestructionIdAndTypeCollector, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore30QDestructionIdAndTypeCollectorC1EPNS_5QNodeE',
        self._addressOf(rootNode),
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

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def collectIdAndType(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QDestructionIdAndTypeCollector::collectIdAndType(QNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdestructionidandtypecollector.html

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QDestructionIdAndTypeCollector::collectIdAndType(QNode
    #      *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore30QDestructionIdAndTypeCollector16collectIdAndTy'
        'peEPNS_5QNodeE',
        self._addressOf(node),
    )

  @staticmethod
  def subtreeIdsAndTypes(*__, **_) -> Never:
    """
    Qt's 'QList<QNodeIdTypePair>
    Qt3DCore::QDestructionIdAndTypeCollector::subtreeIdsAndTypes() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QDestructionIdAndTypeCollector.subtreeIdsAndTypes' has "
        "no cute function yet. Qt's 'QList<QNodeIdTypePair> "
        "Qt3DCore::QDestructionIdAndTypeCollector::subtreeIdsAndTypes() "
        "const': gives a type Python has no way to take yet.")
