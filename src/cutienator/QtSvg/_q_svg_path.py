"""
QSvgPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgPath to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QPainter, QPainterPath
  from . import QSvgExtraStates
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPainterPath = WAIT['QPainterPath']
  QSvgExtraStates = WAIT['QSvgExtraStates']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgPath(QSvgNode):
  """
  The cute side of Qt's QSvgPath: a plain Python object standing in front of
  one C++ QSvgPath.

  It is built on the cute 'QSvgNode', as Qt's QSvgPath is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgPath that has a ritual and that Python can call
  so far, 4 names in all: 'separateFillStroke', 'type',
  'requiresGroupRendering', 'path'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgPath::~QSvgPath()': the destructor: Python never removes a C++
    QSvgPath.
  - Qt's 'void QSvgPath::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgPath::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgPath::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgPath::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgPath is created at the first use, not by 'QSvgPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgPath.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgPath'

  #  A C++ QSvgPath Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgPath'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainter, QSvgExtraStates)
  @overload(NoneType, QSvgExtraStates)
  def separateFillStroke(
      self,
      a0: Optional[QPainter],
      a1: QSvgExtraStates,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgPath::separateFillStroke(const QPainter *a0, const
    QSvgExtraStates &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpath.html#separateFillStroke

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QSvgExtraStates
      Passed on as a value: Qt reads the C++ QSvgExtraStates, which stays
      Python's own.
    """
    #  bool QSvgPath::separateFillStroke(const QPainter *a0, const
    #      QSvgExtraStates &a1) const
    ritual = (
        'ritual_ZNK8QSvgPath18separateFillStrokeEPK8QPainterRK15QSvgExtraSt'
        'ates')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QSvgPath18separateFillStrokeEPK8QPainterRK15QSvgE'
          'xtraStates')
    return self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgPath::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpath.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgPath::type() const
    ritual = 'ritual_ZNK8QSvgPath4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgPath4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def requiresGroupRendering(self) -> bool:
    """
    Calls Qt's 'bool QSvgPath::requiresGroupRendering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgpath.html#requiresGroupRendering
    """
    #  bool QSvgPath::requiresGroupRendering() const
    ritual = 'ritual_ZNK8QSvgPath22requiresGroupRenderingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgPath22requiresGroupRenderingEv'
    return self.uglySide.call(ritual)

  def path(self) -> QPainterPath:
    """
    Calls Qt's 'const QPainterPath &QSvgPath::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpath.html#path

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  const QPainterPath &QSvgPath::path() const
    address = self.uglySide.call('ritual_ZNK8QSvgPath4pathEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

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

  @overload(QSvgNode, QPainterPath)
  @overload(NoneType, QPainterPath)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      qpath: QPainterPath,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgPath::QSvgPath(QSvgNode *parent,
    const QPainterPath &qpath)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpath.html#QSvgPath

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qpath : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  QSvgPath::QSvgPath(QSvgNode *parent, const QPainterPath &qpath)
    self._noteCreation(QSvgPath, lambda: Rituals.call(
        'ritual_ZN8QSvgPathC1EP8QSvgNodeRK12QPainterPath',
        self._addressOf(parent), self._valueOf(qpath),
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
