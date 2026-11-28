"""
QAbstractCollisionShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qabstractcollisionshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstractCollisionShape to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractCollisionShape(QQuick3DNode):
  """
  The cute side of Qt's QAbstractCollisionShape: a plain Python object
  standing in front of one C++ QAbstractCollisionShape.

  It is built on the cute 'QQuick3DNode', as Qt's QAbstractCollisionShape is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractCollisionShape that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr',
  'enableDebugDraw', 'isStaticShape', 'setEnableDebugDraw',
  'enableDebugDrawChanged', 'needsRebuild', 'handleScaleChange'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractCollisionShape::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractCollisionShape::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QAbstractCollisionShape::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QAbstractCollisionShape::~QAbstractCollisionShape()': the
    destructor: Python never removes a C++ QAbstractCollisionShape.
  - Qt's 'physx::PxGeometry *QAbstractCollisionShape::getPhysXGeometry()':
    gives 'physx::PxGeometry', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractCollisionShape is created at the first use, not by
    'QAbstractCollisionShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractCollisionShape.
  - Qt tells when it has removed the C++ QAbstractCollisionShape. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractCollisionShape that has no cute function yet,
    'getPhysXGeometry', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QAbstractCollisionShape::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractcollisionshape.html#tr

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
    #  QString QAbstractCollisionShape::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QAbstractCollisionShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractCollisionShape'

  #  A C++ QAbstractCollisionShape Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractCollisionShape'

  #  The functions Qt calls itself that QAbstractCollisionShape is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getPhysXGeometry': (
          'physx::PxGeometry *QAbstractCollisionShape::getPhysXGeometry()',
      ),
  }

  #  The functions Qt calls itself that QAbstractCollisionShape is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isStaticShape': (
          ('_ZNK23QAbstractCollisionShape13isStaticShapeEv',
           ('bool', 'number', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QAbstractCollisionShape::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractCollisionShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstractCollisionShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enableDebugDraw(self) -> bool:
    """
    Calls Qt's 'bool QAbstractCollisionShape::enableDebugDraw() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html#enableDebugDraw
    """
    #  bool QAbstractCollisionShape::enableDebugDraw() const
    return self.uglySide.call(
        'ritual_ZNK23QAbstractCollisionShape15enableDebugDrawEv',
    )

  def isStaticShape(self) -> bool:
    """
    Calls Qt's 'bool QAbstractCollisionShape::isStaticShape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html#isStaticShape
    """
    #  bool QAbstractCollisionShape::isStaticShape() const
    return self.uglySide.call(
        'ritual_ZNK23QAbstractCollisionShape13isStaticShapeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnableDebugDraw(self, enableDebugDraw: bool) -> None:
    """
    Calls Qt's 'void QAbstractCollisionShape::setEnableDebugDraw(bool
    enableDebugDraw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html#setEnableDebugDraw

    Parameters
    ----------

    enableDebugDraw : bool
      Passed on as it is.
    """
    #  void QAbstractCollisionShape::setEnableDebugDraw(bool enableDebugDraw)
    self.uglySide.call(
        'ritual_ZN23QAbstractCollisionShape18setEnableDebugDrawEb',
        enableDebugDraw,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractCollisionShape::QAbstractCollisionShape(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractCollisionShape::QAbstractCollisionShape(QQuick3DNode *parent)
    self._noteCreation(QAbstractCollisionShape, lambda: Rituals.call(
        'ritual_ZN23QAbstractCollisionShapeC1EP12QQuick3DNode',
        self._addressOf(parent),
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

  @overload(bool)
  def enableDebugDrawChanged(self, enableDebugDraw: bool) -> None:
    """
    Calls Qt's 'void QAbstractCollisionShape::enableDebugDrawChanged(bool
    enableDebugDraw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html

    Parameters
    ----------

    enableDebugDraw : bool
      Passed on as it is.
    """
    #  void QAbstractCollisionShape::enableDebugDrawChanged(bool
    #      enableDebugDraw)
    self.uglySide.call(
        'ritual_ZN23QAbstractCollisionShape22enableDebugDrawChangedEb',
        enableDebugDraw,
    )

  @overload(QObject)
  @overload(NoneType)
  def needsRebuild(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAbstractCollisionShape::needsRebuild(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html#needsRebuild

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractCollisionShape::needsRebuild(QObject *a0)
    self.uglySide.call(
        'ritual_ZN23QAbstractCollisionShape12needsRebuildEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  def handleScaleChange(self) -> None:
    """
    Calls Qt's 'void QAbstractCollisionShape::handleScaleChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractcollisionshape.html#handleScaleChange
    """
    #  void QAbstractCollisionShape::handleScaleChange()
    self.uglySide.call(
        'ritual_ZN23QAbstractCollisionShape17handleScaleChangeEv',
    )

  @staticmethod
  def getPhysXGeometry(*__, **_) -> Never:
    """
    Qt's 'physx::PxGeometry *QAbstractCollisionShape::getPhysXGeometry()':
    gives 'physx::PxGeometry', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractCollisionShape.getPhysXGeometry' has no cute function "
        "yet. Qt's 'physx::PxGeometry "
        "*QAbstractCollisionShape::getPhysXGeometry()': gives "
        "'physx::PxGeometry', which has no cute class yet.")
