"""
QSGClipNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGBasicGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QSGClipNode(QSGBasicGeometryNode):
  """
  The cute side of Qt's QSGClipNode: a plain Python object standing in front
  of one C++ QSGClipNode.

  It is built on the cute 'QSGBasicGeometryNode', as Qt's QSGClipNode is
  built on Qt's QSGBasicGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGClipNode that has a ritual and that Python can
  call so far, 4 names in all: 'setIsRectangular', 'isRectangular',
  'setClipRect', 'clipRect'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGClipNode::~QSGClipNode()': the destructor: Python never removes
    a C++ QSGClipNode.

  What to expect
  --------------

  - The C++ QSGClipNode is created at the first use, not by
    'QSGClipNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGClipNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGClipNode'

  #  A C++ QSGClipNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGClipNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRectangular(self) -> bool:
    """
    Calls Qt's 'bool QSGClipNode::isRectangular() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgclipnode.html#isRectangular
    """
    #  bool QSGClipNode::isRectangular() const
    return self.uglySide.call('ritual_ZNK11QSGClipNode13isRectangularEv')

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGClipNode::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgclipnode.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGClipNode::clipRect() const
    address = self.uglySide.call('ritual_ZNK11QSGClipNode8clipRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsRectangular(self, rectHint: bool) -> None:
    """
    Calls Qt's 'void QSGClipNode::setIsRectangular(bool rectHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgclipnode.html#setIsRectangular

    Parameters
    ----------

    rectHint : bool
      Passed on as it is.
    """
    #  void QSGClipNode::setIsRectangular(bool rectHint)
    self.uglySide.call(
        'ritual_ZN11QSGClipNode16setIsRectangularEb', rectHint,
    )

  @overload(QRectF)
  def setClipRect(self, a0: QRectF) -> None:
    """
    Calls Qt's 'void QSGClipNode::setClipRect(const QRectF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgclipnode.html#setClipRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGClipNode::setClipRect(const QRectF &a0)
    self.uglySide.call(
        'ritual_ZN11QSGClipNode11setClipRectERK6QRectF', self._valueOf(a0),
    )

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
    Notes what was given, for Qt's 'QSGClipNode::QSGClipNode()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgclipnode.html#QSGClipNode
    """
    #  QSGClipNode::QSGClipNode()
    self._noteCreation(QSGClipNode, lambda: Rituals.call(
        'ritual_ZN11QSGClipNodeC1Ev',
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
