"""
QSGTransformNode binding of the Qt C++
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
from . import QSGNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']


class QSGTransformNode(QSGNode):
  """
  The cute side of Qt's QSGTransformNode: a plain Python object standing in
  front of one C++ QSGTransformNode.

  It is built on the cute 'QSGNode', as Qt's QSGTransformNode is built on
  Qt's QSGNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTransformNode that has a ritual and that Python
  can call so far, 4 names in all: 'setMatrix', 'matrix',
  'setCombinedMatrix', 'combinedMatrix'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGTransformNode::~QSGTransformNode()': the destructor: Python
    never removes a C++ QSGTransformNode.

  What to expect
  --------------

  - The C++ QSGTransformNode is created at the first use, not by
    'QSGTransformNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTransformNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTransformNode'

  #  A C++ QSGTransformNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGTransformNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def matrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'const QMatrix4x4 &QSGTransformNode::matrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransformnode.html#matrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  const QMatrix4x4 &QSGTransformNode::matrix() const
    address = self._callAs(
        'QSGTransformNode', 'ritual_ZNK16QSGTransformNode6matrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def combinedMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'const QMatrix4x4 &QSGTransformNode::combinedMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtransformnode.html#combinedMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  const QMatrix4x4 &QSGTransformNode::combinedMatrix() const
    address = self._callAs(
        'QSGTransformNode', 'ritual_ZNK16QSGTransformNode14combinedMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMatrix4x4)
  def setMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QSGTransformNode::setMatrix(const QMatrix4x4 &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransformnode.html#setMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QSGTransformNode::setMatrix(const QMatrix4x4 &matrix)
    self._callAs(
        'QSGTransformNode',
        'ritual_ZN16QSGTransformNode9setMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
    )

  @overload(QMatrix4x4)
  def setCombinedMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QSGTransformNode::setCombinedMatrix(const QMatrix4x4
    &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtransformnode.html#setCombinedMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QSGTransformNode::setCombinedMatrix(const QMatrix4x4 &matrix)
    self._callAs(
        'QSGTransformNode',
        'ritual_ZN16QSGTransformNode17setCombinedMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
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
    Notes what was given, for Qt's 'QSGTransformNode::QSGTransformNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtransformnode.html#QSGTransformNode
    """
    #  QSGTransformNode::QSGTransformNode()
    self._noteCreation(QSGTransformNode, lambda: Rituals.call(
        'ritual_ZN16QSGTransformNodeC1Ev',
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
