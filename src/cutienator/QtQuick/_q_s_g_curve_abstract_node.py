"""
QSGCurveAbstractNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcurveabstractnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGCurveAbstractNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QSGCurveAbstractNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGCurveAbstractNode: a plain Python object standing
  in front of one C++ QSGCurveAbstractNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGCurveAbstractNode is
  built on Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCurveAbstractNode that has a ritual and that
  Python can call so far, 3 names in all: 'setColor', 'cookGeometry',
  'setUseStandardDerivatives'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QSGCurveAbstractNode is created at the first use, not by
    'QSGCurveAbstractNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCurveAbstractNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCurveAbstractNode'

  #  A C++ QSGCurveAbstractNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCurveAbstractNode'

  #  The functions Qt calls itself that QSGCurveAbstractNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setColor': (
          ('_ZN20QSGCurveAbstractNode8setColorE6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'cookGeometry': (
          ('_ZN20QSGCurveAbstractNode12cookGeometryEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setUseStandardDerivatives': (
          ('_ZN20QSGCurveAbstractNode25setUseStandardDerivativesEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
  }

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

  @overload(QColor)
  def setColor(self, col: QColor) -> None:
    """
    Calls Qt's 'void QSGCurveAbstractNode::setColor(QColor col)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveabstractnode.html#setColor

    Parameters
    ----------

    col : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGCurveAbstractNode::setColor(QColor col)
    self._callAs(
        'QSGCurveAbstractNode',
        'ritual_ZN20QSGCurveAbstractNode8setColorE6QColor',
        self._valueOf(col),
    )

  @overload(bool)
  def setUseStandardDerivatives(self, useStandardDerivatives: bool) -> None:
    """
    Calls Qt's 'void QSGCurveAbstractNode::setUseStandardDerivatives(bool
    useStandardDerivatives)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveabstractnode.html

    Parameters
    ----------

    useStandardDerivatives : bool
      Passed on as it is.
    """
    #  void QSGCurveAbstractNode::setUseStandardDerivatives(bool
    #      useStandardDerivatives)
    self._callAs(
        'QSGCurveAbstractNode',
        'ritual_ZN20QSGCurveAbstractNode25setUseStandardDerivativesEb',
        useStandardDerivatives,
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

  def cookGeometry(self) -> None:
    """
    Calls Qt's 'void QSGCurveAbstractNode::cookGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveabstractnode.html#cookGeometry
    """
    #  void QSGCurveAbstractNode::cookGeometry()
    self._callAs(
        'QSGCurveAbstractNode',
        'ritual_ZN20QSGCurveAbstractNode12cookGeometryEv',
    )
