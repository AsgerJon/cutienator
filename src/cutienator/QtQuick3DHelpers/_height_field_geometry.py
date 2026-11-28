"""
HeightFieldGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/heightfieldgeometry_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means HeightFieldGeometry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class HeightFieldGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HeightFieldGeometry: a plain Python object standing
  in front of one C++ HeightFieldGeometry.

  What exists
  -----------

  Every function of Qt's HeightFieldGeometry that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'smoothShading', 'setSmoothShading', 'extents', 'setExtents',
  'sourceChanged', 'smoothShadingChanged', 'extentsChanged', 'updateData'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *HeightFieldGeometry::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int HeightFieldGeometry::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ HeightFieldGeometry is created at the first use, not by
    'HeightFieldGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ HeightFieldGeometry.
  - Qt tells when it has removed the C++ HeightFieldGeometry. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString HeightFieldGeometry::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/heightfieldgeometry.html#tr

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
    #  QString HeightFieldGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19HeightFieldGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HeightFieldGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *HeightFieldGeometry::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *HeightFieldGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19HeightFieldGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'const QUrl &HeightFieldGeometry::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/heightfieldgeometry.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  const QUrl &HeightFieldGeometry::source() const
    address = self.uglySide.call('ritual_ZNK19HeightFieldGeometry6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def smoothShading(self) -> bool:
    """
    Calls Qt's 'bool HeightFieldGeometry::smoothShading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#smoothShading
    """
    #  bool HeightFieldGeometry::smoothShading() const
    return self.uglySide.call(
        'ritual_ZNK19HeightFieldGeometry13smoothShadingEv',
    )

  def extents(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &HeightFieldGeometry::extents() const'.

    Qt's own words: https://doc.qt.io/qt-6/heightfieldgeometry.html#extents

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &HeightFieldGeometry::extents() const
    address = self.uglySide.call('ritual_ZNK19HeightFieldGeometry7extentsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, newSource: QUrl) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::setSource(const QUrl &newSource)'.

    Qt's own words: https://doc.qt.io/qt-6/heightfieldgeometry.html#setSource

    Parameters
    ----------

    newSource : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void HeightFieldGeometry::setSource(const QUrl &newSource)
    self.uglySide.call(
        'ritual_ZN19HeightFieldGeometry9setSourceERK4QUrl',
        self._valueOf(newSource),
    )

  @overload(bool)
  def setSmoothShading(self, smooth: bool) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::setSmoothShading(bool smooth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#setSmoothShading

    Parameters
    ----------

    smooth : bool
      Passed on as it is.
    """
    #  void HeightFieldGeometry::setSmoothShading(bool smooth)
    self.uglySide.call(
        'ritual_ZN19HeightFieldGeometry16setSmoothShadingEb', smooth,
    )

  @overload(QVector3D)
  def setExtents(self, newExtents: QVector3D) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::setExtents(const QVector3D
    &newExtents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#setExtents

    Parameters
    ----------

    newExtents : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void HeightFieldGeometry::setExtents(const QVector3D &newExtents)
    self.uglySide.call(
        'ritual_ZN19HeightFieldGeometry10setExtentsERK9QVector3D',
        self._valueOf(newExtents),
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
    Notes what was given, for Qt's
    'HeightFieldGeometry::HeightFieldGeometry()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#HeightFieldGeometry
    """
    #  HeightFieldGeometry::HeightFieldGeometry()
    self._noteCreation(HeightFieldGeometry, lambda: Rituals.call(
        'ritual_ZN19HeightFieldGeometryC1Ev',
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#sourceChanged
    """
    #  void HeightFieldGeometry::sourceChanged()
    self.uglySide.call('ritual_ZN19HeightFieldGeometry13sourceChangedEv')

  def smoothShadingChanged(self) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::smoothShadingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#smoothShadingChanged
    """
    #  void HeightFieldGeometry::smoothShadingChanged()
    self.uglySide.call(
        'ritual_ZN19HeightFieldGeometry20smoothShadingChangedEv',
    )

  def extentsChanged(self) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::extentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#extentsChanged
    """
    #  void HeightFieldGeometry::extentsChanged()
    self.uglySide.call('ritual_ZN19HeightFieldGeometry14extentsChangedEv')

  def updateData(self) -> None:
    """
    Calls Qt's 'void HeightFieldGeometry::updateData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/heightfieldgeometry.html#updateData
    """
    #  void HeightFieldGeometry::updateData()
    self.uglySide.call('ritual_ZN19HeightFieldGeometry10updateDataEv')
