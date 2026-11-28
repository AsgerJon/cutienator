"""
QWavefrontMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsWavefrontMesh/6.12.0/QtLabsWavefrontMesh/private/qwavefrontmesh_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWavefrontMesh to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject, QRectF, QUrl
  from ..QtGui import QVector3D
  from ..QtQuick import QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']
  QUrl = WAIT['QUrl']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWavefrontMesh(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWavefrontMesh: a plain Python object standing in
  front of one C++ QWavefrontMesh.

  What exists
  -----------

  Every function of Qt's QWavefrontMesh that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'source', 'setSource',
  'lastError', 'setLastError', 'updateGeometry', 'log', 'projectionPlaneV',
  'setProjectionPlaneV', 'projectionPlaneW', 'setProjectionPlaneW',
  'sourceChanged', 'lastErrorChanged', 'projectionPlaneVChanged',
  'projectionPlaneWChanged', 'readData'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWavefrontMesh::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWavefrontMesh::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWavefrontMesh::~QWavefrontMesh()': the destructor: Python never
    removes a C++ QWavefrontMesh.
  - Qt's 'bool QWavefrontMesh::validateAttributes(const QList<QByteArray>
    &attributes, int *posIndex)': takes a number to change where it is.
  - Qt's 'QWavefrontMeshPrivate *QWavefrontMesh::d_func()': gives
    'QWavefrontMeshPrivate', which has no cute class yet.
  - Qt's 'const QWavefrontMeshPrivate *QWavefrontMesh::d_func() const': gives
    'QWavefrontMeshPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWavefrontMesh is created at the first use, not by
    'QWavefrontMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWavefrontMesh.
  - Qt tells when it has removed the C++ QWavefrontMesh. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWavefrontMesh, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QWavefrontMesh::Error' of Qt, with the 11 names Qt gives in it.
    """

    NoError = Kee[int](0)
    InvalidSourceError = Kee[int](1)
    UnsupportedFaceShapeError = Kee[int](2)
    UnsupportedIndexSizeError = Kee[int](3)
    FileNotFoundError = Kee[int](4)
    NoAttributesError = Kee[int](5)
    MissingPositionAttributeError = Kee[int](6)
    MissingTextureCoordinateAttributeError = Kee[int](7)
    MissingPositionAndTextureCoordinateAttributesError = Kee[int](8)
    TooManyAttributesError = Kee[int](9)
    InvalidPlaneDefinitionError = Kee[int](10)

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
    Calls Qt's 'QString QWavefrontMesh::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#tr

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
    #  QString QWavefrontMesh::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWavefrontMesh2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWavefrontMesh'

  #  A C++ QWavefrontMesh Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWavefrontMesh'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWavefrontMesh::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWavefrontMesh::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWavefrontMesh10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWavefrontMesh::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWavefrontMesh::source() const
    address = self.uglySide.call('ritual_ZNK14QWavefrontMesh6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def lastError(self) -> Error:
    """
    Calls Qt's 'Error QWavefrontMesh::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#lastError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QWavefrontMesh::lastError() const
    return QWavefrontMesh.Error(self.uglySide.call(
        'ritual_ZNK14QWavefrontMesh9lastErrorEv',
    ))

  def log(self) -> str:
    """
    Calls Qt's 'QString QWavefrontMesh::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWavefrontMesh::log() const
    ritual = 'ritual_ZNK14QWavefrontMesh3logEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QWavefrontMesh3logEv'
    return self.uglySide.call(ritual)

  def projectionPlaneV(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QWavefrontMesh::projectionPlaneV() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#projectionPlaneV

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QWavefrontMesh::projectionPlaneV() const
    address = self.uglySide.call(
        'ritual_ZNK14QWavefrontMesh16projectionPlaneVEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def projectionPlaneW(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QWavefrontMesh::projectionPlaneW() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#projectionPlaneW

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QWavefrontMesh::projectionPlaneW() const
    address = self.uglySide.call(
        'ritual_ZNK14QWavefrontMesh16projectionPlaneWEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWavefrontMesh::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QWavefrontMesh9setSourceERK4QUrl', self._valueOf(url),
    )

  @overload(Error)
  def setLastError(self, lastError: Error) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::setLastError(Error lastError)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#setLastError

    Parameters
    ----------

    lastError : Error
      Passed on as its number.
    """
    #  void QWavefrontMesh::setLastError(Error lastError)
    self.uglySide.call(
        'ritual_ZN14QWavefrontMesh12setLastErrorENS_5ErrorE',
        lastError.value,
    )

  @overload(QVector3D)
  def setProjectionPlaneV(self, projectionPlaneV: QVector3D) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::setProjectionPlaneV(const QVector3D
    &projectionPlaneV)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#setProjectionPlaneV

    Parameters
    ----------

    projectionPlaneV : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QWavefrontMesh::setProjectionPlaneV(const QVector3D
    #      &projectionPlaneV)
    self.uglySide.call(
        'ritual_ZN14QWavefrontMesh19setProjectionPlaneVERK9QVector3D',
        self._valueOf(projectionPlaneV),
    )

  @overload(QVector3D)
  def setProjectionPlaneW(self, projectionPlaneW: QVector3D) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::setProjectionPlaneW(const QVector3D
    &projectionPlaneW)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#setProjectionPlaneW

    Parameters
    ----------

    projectionPlaneW : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QWavefrontMesh::setProjectionPlaneW(const QVector3D
    #      &projectionPlaneW)
    self.uglySide.call(
        'ritual_ZN14QWavefrontMesh19setProjectionPlaneWERK9QVector3D',
        self._valueOf(projectionPlaneW),
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
    Notes what was given, for Qt's 'QWavefrontMesh::QWavefrontMesh(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#QWavefrontMesh

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWavefrontMesh::QWavefrontMesh(QObject *parent)
    self._noteCreation(QWavefrontMesh, lambda: Rituals.call(
        'ritual_ZN14QWavefrontMeshC1EP7QObject',
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
    Calls Qt's 'QSGGeometry *QWavefrontMesh::updateGeometry(QSGGeometry
    *geometry, int attrCount, int posIndex, const QRectF &srcRect, const
    QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#updateGeometry

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
    #  QSGGeometry *QWavefrontMesh::updateGeometry(QSGGeometry *geometry, int
    #      attrCount, int posIndex, const QRectF &srcRect, const QRectF
    #      &rect)
    ritual = (
        'ritual_ZN14QWavefrontMesh14updateGeometryEP11QSGGeometryiiRK6QRect'
        'FS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QWavefrontMesh14updateGeometryEP11QSGGeometryiiRK'
          '6QRectFS4_')
    address = self.uglySide.call(
        ritual,
        self._addressOf(geometry), attrCount, posIndex,
        self._valueOf(srcRect), self._valueOf(rect),
    )
    from ..QtQuick import QSGGeometry
    return QSGGeometry._cuteAt(address)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#sourceChanged
    """
    #  void QWavefrontMesh::sourceChanged()
    self.uglySide.call('ritual_ZN14QWavefrontMesh13sourceChangedEv')

  def lastErrorChanged(self) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::lastErrorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#lastErrorChanged
    """
    #  void QWavefrontMesh::lastErrorChanged()
    self.uglySide.call('ritual_ZN14QWavefrontMesh16lastErrorChangedEv')

  def projectionPlaneVChanged(self) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::projectionPlaneVChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#projectionPlaneVChanged
    """
    #  void QWavefrontMesh::projectionPlaneVChanged()
    self.uglySide.call(
        'ritual_ZN14QWavefrontMesh23projectionPlaneVChangedEv',
    )

  def projectionPlaneWChanged(self) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::projectionPlaneWChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwavefrontmesh.html#projectionPlaneWChanged
    """
    #  void QWavefrontMesh::projectionPlaneWChanged()
    self.uglySide.call(
        'ritual_ZN14QWavefrontMesh23projectionPlaneWChangedEv',
    )

  def readData(self) -> None:
    """
    Calls Qt's 'void QWavefrontMesh::readData()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavefrontmesh.html#readData
    """
    #  void QWavefrontMesh::readData()
    self.uglySide.call('ritual_ZN14QWavefrontMesh8readDataEv')
