"""
QQuickGridMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGridMesh to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickShaderEffectMesh

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from . import QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridMesh(QQuickShaderEffectMesh):
  """
  The cute side of Qt's QQuickGridMesh: a plain Python object standing in
  front of one C++ QQuickGridMesh.

  It is built on the cute 'QQuickShaderEffectMesh', as Qt's QQuickGridMesh is
  built on Qt's QQuickShaderEffectMesh, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGridMesh that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'updateGeometry', 'log',
  'setResolution', 'resolution', 'resolutionChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGridMesh::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickGridMesh::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'bool QQuickGridMesh::validateAttributes(const QList<QByteArray>
    &attributes, int *posIndex)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGridMesh is created at the first use, not by
    'QQuickGridMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGridMesh.
  - Qt tells when it has removed the C++ QQuickGridMesh. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickGridMesh::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#tr

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
    #  QString QQuickGridMesh::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickGridMesh2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridMesh'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGridMesh::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGridMesh::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickGridMesh10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def log(self) -> str:
    """
    Calls Qt's 'QString QQuickGridMesh::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGridMesh::log() const
    ritual = 'ritual_ZNK14QQuickGridMesh3logEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickGridMesh3logEv'
    return self.uglySide.call(ritual)

  def resolution(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickGridMesh::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#resolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickGridMesh::resolution() const
    address = self.uglySide.call('ritual_ZNK14QQuickGridMesh10resolutionEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setResolution(self, res: QSize) -> None:
    """
    Calls Qt's 'void QQuickGridMesh::setResolution(const QSize &res)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#setResolution

    Parameters
    ----------

    res : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickGridMesh::setResolution(const QSize &res)
    self.uglySide.call(
        'ritual_ZN14QQuickGridMesh13setResolutionERK5QSize',
        self._valueOf(res),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickGridMesh::QQuickGridMesh(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#QQuickGridMesh

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGridMesh::QQuickGridMesh(QObject *parent)
    self._noteCreation(QQuickGridMesh, lambda: Rituals.call(
        'ritual_ZN14QQuickGridMeshC1EP7QObject',
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

  @overload(QSGGeometry, int, int, QRectF, QRectF)
  @overload(NoneType, int, int, QRectF, QRectF)
  def updateGeometry(
      self,
      geometry: Optional[QSGGeometry],
      attrCount: int,
      posIndex: int,
      srcRect: QRectF,
      rect: QRectF,
  ) -> Optional[QSGGeometry]:
    """
    Calls Qt's 'QSGGeometry *QQuickGridMesh::updateGeometry(QSGGeometry
    *geometry, int attrCount, int posIndex, const QRectF &srcRect, const
    QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridmesh.html#updateGeometry

    Parameters
    ----------

    geometry : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrCount : int
      Passed on as it is.

    posIndex : int
      Passed on as it is.

    srcRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    Optional[QSGGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGeometry *QQuickGridMesh::updateGeometry(QSGGeometry *geometry, int
    #      attrCount, int posIndex, const QRectF &srcRect, const QRectF
    #      &rect)
    ritual = (
        'ritual_ZN14QQuickGridMesh14updateGeometryEP11QSGGeometryiiRK6QRect'
        'FS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickGridMesh14updateGeometryEP11QSGGeometryiiRK'
          '6QRectFS4_')
    address = self.uglySide.call(
        ritual,
        self._addressOf(geometry), attrCount, posIndex,
        self._valueOf(srcRect), self._valueOf(rect),
    )
    from . import QSGGeometry
    return QSGGeometry._cuteAt(address)

  def resolutionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridMesh::resolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridmesh.html#resolutionChanged
    """
    #  void QQuickGridMesh::resolutionChanged()
    self.uglySide.call('ritual_ZN14QQuickGridMesh17resolutionChangedEv')
