"""
QCollisionDebugMeshBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qcollisiondebugmeshbuilder_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCollisionDebugMeshBuilder to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QCollisionDebugMeshBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCollisionDebugMeshBuilder: a plain Python object
  standing in front of one C++ QCollisionDebugMeshBuilder.

  C++ hands a QCollisionDebugMeshBuilder around as a copy, so every C++
  QCollisionDebugMeshBuilder behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QCollisionDebugMeshBuilder that has a ritual and
  that Python can call so far, 3 names in all: 'reset', 'addLine',
  'generateVertexArray'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCollisionDebugMeshBuilder::~QCollisionDebugMeshBuilder()': the
    destructor: Python removes its C++ QCollisionDebugMeshBuilder by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QCollisionDebugMeshBuilder is created at the first use, not by
    'QCollisionDebugMeshBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCollisionDebugMeshBuilder back gives a copy the
    ritual made for Python, in a new cute QCollisionDebugMeshBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCollisionDebugMeshBuilder'

  #  Qt's '~QCollisionDebugMeshBuilder()'. Naming it makes this a value
  #  class: Python owns every C++ QCollisionDebugMeshBuilder behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QCollisionDebugMeshBuilderD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCollisionDebugMeshBuilder::QCollisionDebugMeshBuilder()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollisiondebugmeshbuilder.html
    """
    #  QCollisionDebugMeshBuilder::QCollisionDebugMeshBuilder()
    self._noteCreation(QCollisionDebugMeshBuilder, lambda: Rituals.call(
        'ritual_ZN26QCollisionDebugMeshBuilderC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QCollisionDebugMeshBuilder::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollisiondebugmeshbuilder.html#reset
    """
    #  void QCollisionDebugMeshBuilder::reset()
    self.uglySide.call('ritual_ZN26QCollisionDebugMeshBuilder5resetEv')

  @overload(QVector3D, QVector3D)
  @overload(QVector3D, QVector3D, QVector3D)
  def addLine(
      self,
      start: QVector3D,
      end: QVector3D,
      normal: Optional[QVector3D] = None,
  ) -> None:
    """
    Calls Qt's 'void QCollisionDebugMeshBuilder::addLine(const QVector3D
    &start, const QVector3D &end, const QVector3D &normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollisiondebugmeshbuilder.html#addLine

    Parameters
    ----------

    start : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    end : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    normal : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D(0, 0, 1)' is then
      passed on.
    """
    #  void QCollisionDebugMeshBuilder::addLine(const QVector3D &start, const
    #      QVector3D &end, const QVector3D &normal)
    if normal is None:
      from ..QtGui import QVector3D
      normal = QVector3D(0, 0, 1)
    self.uglySide.call(
        'ritual_ZN26QCollisionDebugMeshBuilder7addLineERK9QVector3DS2_S2_',
        self._valueOf(start), self._valueOf(end), self._valueOf(normal),
    )

  def generateVertexArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QCollisionDebugMeshBuilder::generateVertexArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollisiondebugmeshbuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCollisionDebugMeshBuilder::generateVertexArray()
    address = self.uglySide.call(
        'ritual_ZN26QCollisionDebugMeshBuilder19generateVertexArrayEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)
