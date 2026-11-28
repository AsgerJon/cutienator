"""
QQuickBorderImageMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickBorderImageMesh to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QList
from . import QQuickShaderEffectMesh

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from . import QQuickScaleGrid, QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBorderImageMesh(QQuickShaderEffectMesh):
  """
  The cute side of Qt's QQuickBorderImageMesh: a plain Python object standing
  in front of one C++ QQuickBorderImageMesh.

  It is built on the cute 'QQuickShaderEffectMesh', as Qt's
  QQuickBorderImageMesh is built on Qt's QQuickShaderEffectMesh, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBorderImageMesh that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'updateGeometry',
  'border', 'size', 'horizontalTileMode', 'verticalTileMode', 'sizeChanged',
  'horizontalTileModeChanged', 'verticalTileModeChanged'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBorderImageMesh::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickBorderImageMesh::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'bool QQuickBorderImageMesh::validateAttributes(const
    QList<QByteArray> &attributes, int *posIndex)': takes a number to change
    where it is.

  What has no ritual
  ------------------

  7 of the 19 functions Qt declares: 4 leans on 'QQuickBorderImageMesh; 2 not
  a gap; 1 leans on 'vtable for QQuickBorderImageMesh', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QQuickBorderImageMesh is created at the first use, not by
    'QQuickBorderImageMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBorderImageMesh.
  - Qt tells when it has removed the C++ QQuickBorderImageMesh. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickBorderImageMesh that has no cute function yet,
    '__init__', 'setHorizontalTileMode', 'setSize', 'setVerticalTileMode',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQuickBorderImageMesh, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class TileMode(CuteNum):
    """
    The enum 'QQuickBorderImageMesh::TileMode' of Qt, with the 3 names Qt
    gives in it.
    """

    Stretch = Kee[int](0)
    Repeat = Kee[int](1)
    Round = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBorderImageMesh'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBorderImageMesh::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBorderImageMesh::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickBorderImageMesh10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def border(self) -> Optional[QQuickScaleGrid]:
    """
    Calls Qt's 'QQuickScaleGrid *QQuickBorderImageMesh::border() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimagemesh.html#border

    Returns
    -------

    Optional[QQuickScaleGrid]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScaleGrid *QQuickBorderImageMesh::border() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickBorderImageMesh6borderEv',
    )
    from . import QQuickScaleGrid
    return QQuickScaleGrid._cuteAt(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickBorderImageMesh::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickborderimagemesh.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickBorderImageMesh::size() const
    address = self.uglySide.call('ritual_ZNK21QQuickBorderImageMesh4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def horizontalTileMode(self) -> TileMode:
    """
    Calls Qt's 'TileMode QQuickBorderImageMesh::horizontalTileMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html#horizontalTileMode

    Returns
    -------

    TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TileMode(number)' gives.
    """
    #  TileMode QQuickBorderImageMesh::horizontalTileMode() const
    return QQuickBorderImageMesh.TileMode(self.uglySide.call(
        'ritual_ZNK21QQuickBorderImageMesh18horizontalTileModeEv',
    ))

  def verticalTileMode(self) -> TileMode:
    """
    Calls Qt's 'TileMode QQuickBorderImageMesh::verticalTileMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html#verticalTileMode

    Returns
    -------

    TileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TileMode(number)' gives.
    """
    #  TileMode QQuickBorderImageMesh::verticalTileMode() const
    return QQuickBorderImageMesh.TileMode(self.uglySide.call(
        'ritual_ZNK21QQuickBorderImageMesh16verticalTileModeEv',
    ))

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickBorderImageMesh::QQuickBorderImageMesh(QObject *parent)':
    leans on 'vtable for QQuickBorderImageMesh', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickBorderImageMesh.__init__' has no cute function yet. Qt's "
        "'QQuickBorderImageMesh::QQuickBorderImageMesh(QObject *parent)': "
        "leans on 'vtable for QQuickBorderImageMesh', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'QSGGeometry
    *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry, int
    attrCount, int posIndex, const QRectF &srcRect, const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html#updateGeometry

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
    #  QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry
    #      *geometry, int attrCount, int posIndex, const QRectF &srcRect,
    #      const QRectF &rect)
    ritual = (
        'ritual_ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiR'
        'K6QRectFS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeome'
          'tryiiRK6QRectFS4_')
    address = self.uglySide.call(
        ritual,
        self._addressOf(geometry), attrCount, posIndex,
        self._valueOf(srcRect), self._valueOf(rect),
    )
    from . import QSGGeometry
    return QSGGeometry._cuteAt(address)

  def sizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImageMesh::sizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html#sizeChanged
    """
    #  void QQuickBorderImageMesh::sizeChanged()
    self.uglySide.call('ritual_ZN21QQuickBorderImageMesh11sizeChangedEv')

  def horizontalTileModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImageMesh::horizontalTileModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html
    """
    #  void QQuickBorderImageMesh::horizontalTileModeChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickBorderImageMesh25horizontalTileModeChangedEv',
    )

  def verticalTileModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBorderImageMesh::verticalTileModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickborderimagemesh.html#verticalTileModeChanged
    """
    #  void QQuickBorderImageMesh::verticalTileModeChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickBorderImageMesh23verticalTileModeChangedEv',
    )

  @staticmethod
  def setHorizontalTileMode(*__, **_) -> Never:
    """
    Qt's 'void QQuickBorderImageMesh::setHorizontalTileMode(TileMode a0)':
    leans on 'QQuickBorderImageMesh::horizontalTileModeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickBorderImageMesh.setHorizontalTileMode' has no cute function "
        "yet. Qt's 'void "
        "QQuickBorderImageMesh::setHorizontalTileMode(TileMode a0)': leans "
        "on 'QQuickBorderImageMesh::horizontalTileModeChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setSize(*__, **_) -> Never:
    """
    Qt's 'void QQuickBorderImageMesh::setSize(const QSize &size)': leans on
    'QQuickBorderImageMesh::sizeChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickBorderImageMesh.setSize' has no cute function yet. Qt's "
        "'void QQuickBorderImageMesh::setSize(const QSize &size)': leans on "
        "'QQuickBorderImageMesh::sizeChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setVerticalTileMode(*__, **_) -> Never:
    """
    Qt's 'void QQuickBorderImageMesh::setVerticalTileMode(TileMode a0)':
    leans on 'QQuickBorderImageMesh::verticalTileModeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickBorderImageMesh.setVerticalTileMode' has no cute function "
        "yet. Qt's 'void "
        "QQuickBorderImageMesh::setVerticalTileMode(TileMode a0)': leans on "
        "'QQuickBorderImageMesh::verticalTileModeChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
