"""
QMeshShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qmeshshape_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QMeshShape to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractCollisionShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQuick3D import QQuick3DGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DGeometry = WAIT['QQuick3DGeometry']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMeshShape(QAbstractCollisionShape):
  """
  The cute side of Qt's QMeshShape: a plain Python object standing in front
  of one C++ QMeshShape.

  It is built on the cute 'QAbstractCollisionShape', as Qt's QMeshShape is
  built on Qt's QAbstractCollisionShape, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMeshShape that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'shapeType', 'source',
  'setSource', 'geometry', 'setGeometry', 'sourceChanged', 'geometryChanged',
  'geometryDestroyed', 'geometryContentChanged', 'updatePhysXGeometry'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMeshShape::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMeshShape::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QMeshShape::qt_qmlMarker_uncreatable()': one of Qt's own inner
    workings.
  - Qt's 'QMeshShape::~QMeshShape()': the destructor: Python never removes a
    C++ QMeshShape.
  - Qt's 'physx::PxGeometry *QMeshShape::getPhysXGeometry()': gives
    'physx::PxGeometry', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QMeshShape is created at the first use, not by 'QMeshShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMeshShape.
  - Qt tells when it has removed the C++ QMeshShape. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QMeshShape, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class MeshType(CuteNum, scoped=True):
    """
    The enum 'QMeshShape::MeshType' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    TRIANGLE = Kee[int](0)
    CONVEX = Kee[int](1)

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
    Calls Qt's 'QString QMeshShape::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#tr

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
    #  QString QMeshShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QMeshShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMeshShape'

  #  A C++ QMeshShape Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMeshShape'

  #  The functions Qt calls itself that QMeshShape is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'shapeType': (
          ('_ZNK10QMeshShape9shapeTypeEv',
           ('int', 'enum', 'QtQuick3DPhysics:QMeshShape.MeshType'),
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
    Calls Qt's 'const QMetaObject *QMeshShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMeshShape::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QMeshShape10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shapeType(self) -> MeshType:
    """
    Calls Qt's 'MeshType QMeshShape::shapeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#shapeType

    Returns
    -------

    MeshType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MeshType(number)' gives.
    """
    #  MeshType QMeshShape::shapeType() const
    return QMeshShape.MeshType(self.uglySide.call(
        'ritual_ZNK10QMeshShape9shapeTypeEv',
    ))

  def source(self) -> QUrl:
    """
    Calls Qt's 'const QUrl &QMeshShape::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  const QUrl &QMeshShape::source() const
    address = self.uglySide.call('ritual_ZNK10QMeshShape6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def geometry(self) -> Optional[QQuick3DGeometry]:
    """
    Calls Qt's 'QQuick3DGeometry *QMeshShape::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#geometry

    Returns
    -------

    Optional[QQuick3DGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DGeometry *QMeshShape::geometry() const
    address = self.uglySide.call('ritual_ZNK10QMeshShape8geometryEv')
    from ..QtQuick3D import QQuick3DGeometry
    return QQuick3DGeometry._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, newSource: QUrl) -> None:
    """
    Calls Qt's 'void QMeshShape::setSource(const QUrl &newSource)'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#setSource

    Parameters
    ----------

    newSource : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QMeshShape::setSource(const QUrl &newSource)
    self.uglySide.call(
        'ritual_ZN10QMeshShape9setSourceERK4QUrl', self._valueOf(newSource),
    )

  @overload(QQuick3DGeometry)
  @overload(NoneType)
  def setGeometry(self, newGeometry: Optional[QQuick3DGeometry]) -> None:
    """
    Calls Qt's 'void QMeshShape::setGeometry(QQuick3DGeometry *newGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#setGeometry

    Parameters
    ----------

    newGeometry : Optional[QQuick3DGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMeshShape::setGeometry(QQuick3DGeometry *newGeometry)
    self.uglySide.call(
        'ritual_ZN10QMeshShape11setGeometryEP16QQuick3DGeometry',
        self._addressOf(newGeometry),
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QMeshShape::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#sourceChanged
    """
    #  void QMeshShape::sourceChanged()
    self.uglySide.call('ritual_ZN10QMeshShape13sourceChangedEv')

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QMeshShape::geometryChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#geometryChanged
    """
    #  void QMeshShape::geometryChanged()
    self.uglySide.call('ritual_ZN10QMeshShape15geometryChangedEv')

  @overload(QObject)
  @overload(NoneType)
  def geometryDestroyed(self, geometry: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMeshShape::geometryDestroyed(QObject *geometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qmeshshape.html#geometryDestroyed

    Parameters
    ----------

    geometry : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMeshShape::geometryDestroyed(QObject *geometry)
    self.uglySide.call(
        'ritual_ZN10QMeshShape17geometryDestroyedEP7QObject',
        self._addressOf(geometry, 'QObject'),
    )

  def geometryContentChanged(self) -> None:
    """
    Calls Qt's 'void QMeshShape::geometryContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmeshshape.html#geometryContentChanged
    """
    #  void QMeshShape::geometryContentChanged()
    self.uglySide.call('ritual_ZN10QMeshShape22geometryContentChangedEv')

  def updatePhysXGeometry(self) -> None:
    """
    Calls Qt's 'void QMeshShape::updatePhysXGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmeshshape.html#updatePhysXGeometry
    """
    #  void QMeshShape::updatePhysXGeometry()
    self.uglySide.call('ritual_ZN10QMeshShape19updatePhysXGeometryEv')
