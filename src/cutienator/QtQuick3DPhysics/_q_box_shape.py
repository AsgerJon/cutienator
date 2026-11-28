"""
QBoxShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qboxshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBoxShape to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractCollisionShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxShape(QAbstractCollisionShape):
  """
  The cute side of Qt's QBoxShape: a plain Python object standing in front of
  one C++ QBoxShape.

  It is built on the cute 'QAbstractCollisionShape', as Qt's QBoxShape is
  built on Qt's QAbstractCollisionShape, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxShape that has a ritual and that Python can call
  so far, 7 names in all: 'metaObject', 'tr', 'extents', 'isStaticShape',
  'setExtents', 'extentsChanged', 'updatePhysXGeometry'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxShape::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBoxShape::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBoxShape::~QBoxShape()': the destructor: Python never removes a
    C++ QBoxShape.
  - Qt's 'physx::PxGeometry *QBoxShape::getPhysXGeometry()': gives
    'physx::PxGeometry', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBoxShape is created at the first use, not by 'QBoxShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxShape.
  - Qt tells when it has removed the C++ QBoxShape. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QBoxShape::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBoxShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QBoxShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxShape'

  #  A C++ QBoxShape Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBoxShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxShape::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QBoxShape10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def extents(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QBoxShape::extents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#extents

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QBoxShape::extents() const
    address = self.uglySide.call('ritual_ZNK9QBoxShape7extentsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isStaticShape(self) -> bool:
    """
    Calls Qt's 'bool QBoxShape::isStaticShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#isStaticShape
    """
    #  bool QBoxShape::isStaticShape() const
    ritual = 'ritual_ZNK9QBoxShape13isStaticShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QBoxShape13isStaticShapeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setExtents(self, extents: QVector3D) -> None:
    """
    Calls Qt's 'void QBoxShape::setExtents(QVector3D extents)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#setExtents

    Parameters
    ----------

    extents : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QBoxShape::setExtents(QVector3D extents)
    self.uglySide.call(
        'ritual_ZN9QBoxShape10setExtentsE9QVector3D', self._valueOf(extents),
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
    Notes what was given, for Qt's 'QBoxShape::QBoxShape()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#QBoxShape
    """
    #  QBoxShape::QBoxShape()
    self._noteCreation(QBoxShape, lambda: Rituals.call(
        'ritual_ZN9QBoxShapeC1Ev',
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

  @overload(QVector3D)
  def extentsChanged(self, extents: QVector3D) -> None:
    """
    Calls Qt's 'void QBoxShape::extentsChanged(QVector3D extents)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#extentsChanged

    Parameters
    ----------

    extents : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QBoxShape::extentsChanged(QVector3D extents)
    self.uglySide.call(
        'ritual_ZN9QBoxShape14extentsChangedE9QVector3D',
        self._valueOf(extents),
    )

  def updatePhysXGeometry(self) -> None:
    """
    Calls Qt's 'void QBoxShape::updatePhysXGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxshape.html#updatePhysXGeometry
    """
    #  void QBoxShape::updatePhysXGeometry()
    self.uglySide.call('ritual_ZN9QBoxShape19updatePhysXGeometryEv')
