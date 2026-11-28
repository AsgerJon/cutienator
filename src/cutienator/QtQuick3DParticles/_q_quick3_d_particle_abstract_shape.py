"""
QQuick3DParticleAbstractShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleabstractshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleAbstractShape to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from ..QtQuick3D import QQuick3DNode

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleAbstractShape(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuick3DParticleAbstractShape: a plain Python object
  standing in front of one C++ QQuick3DParticleAbstractShape.

  It is built on the cute 'QObject', as Qt's QQuick3DParticleAbstractShape is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QQuick3DParticleAbstractShape
  is built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleAbstractShape that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'getPosition', 'getSurfaceNormal', 'componentComplete', 'classBegin',
  'parentNode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleAbstractShape::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleAbstractShape::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DParticleAbstractShape::qt_qmlMarker_anonymous()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleAbstractShape is created at the first use, not by
    'QQuick3DParticleAbstractShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleAbstractShape.
  - Qt tells when it has removed the C++ QQuick3DParticleAbstractShape. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DParticleAbstractShape::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html#tr

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
    #  QString QQuick3DParticleAbstractShape::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuick3DParticleAbstractShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleAbstractShape'

  #  Qt's QQuick3DParticleAbstractShape is built on more than one class. The
  #  part of a C++ QQuick3DParticleAbstractShape that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuick3DParticleAbstractShape_QQmlParserStatus',
  }

  #  A C++ QQuick3DParticleAbstractShape Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleAbstractShape'

  #  The functions Qt calls itself that QQuick3DParticleAbstractShape is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'getPosition': (
          ('_ZN29QQuick3DParticleAbstractShape11getPositionEi',
           ('address', 'value', 'QtGui:QVector3D'),
           (
               ('int', 'number', ''),
           )),
      ),
      'getSurfaceNormal': (
          ('_ZN29QQuick3DParticleAbstractShape16getSurfaceNormalEi',
           ('address', 'value', 'QtGui:QVector3D'),
           (
               ('int', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DParticleAbstractShape::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleAbstractShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleAbstractShape10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleAbstractShape::QQuick3DParticleAbstractShape(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleAbstractShape::QQuick3DParticleAbstractShape(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleAbstractShape, lambda: Rituals.call(
        'ritual_ZN29QQuick3DParticleAbstractShapeC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def getPosition(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleAbstractShape::getPosition(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html#getPosition

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleAbstractShape::getPosition(int
    #      particleIndex)
    address = self.uglySide.call(
        'ritual_ZN29QQuick3DParticleAbstractShape11getPositionEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def getSurfaceNormal(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleAbstractShape::getSurfaceNormal(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleAbstractShape::getSurfaceNormal(int
    #      particleIndex)
    address = self.uglySide.call(
        'ritual_ZN29QQuick3DParticleAbstractShape16getSurfaceNormalEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAbstractShape::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html
    """
    #  void QQuick3DParticleAbstractShape::componentComplete()
    ritual = 'ritual_ZN29QQuick3DParticleAbstractShape17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuick3DParticleAbstractShape17componentCompleteE'
          'v')
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAbstractShape::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html#classBegin
    """
    #  void QQuick3DParticleAbstractShape::classBegin()
    ritual = 'ritual_ZN29QQuick3DParticleAbstractShape10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QQuick3DParticleAbstractShape10classBeginEv'
    self.uglySide.call(ritual)

  def parentNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DParticleAbstractShape::parentNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleabstractshape.html#parentNode

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DParticleAbstractShape::parentNode()
    address = self.uglySide.call(
        'ritual_ZN29QQuick3DParticleAbstractShape10parentNodeEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)
