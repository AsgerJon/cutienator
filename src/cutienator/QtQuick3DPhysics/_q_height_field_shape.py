"""
QHeightFieldShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qheightfieldshape_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QHeightFieldShape to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractCollisionShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QVector3D
  from ..QtQuick import QQuickImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickImage = WAIT['QQuickImage']
  QUrl = WAIT['QUrl']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHeightFieldShape(QAbstractCollisionShape):
  """
  The cute side of Qt's QHeightFieldShape: a plain Python object standing in
  front of one C++ QHeightFieldShape.

  It is built on the cute 'QAbstractCollisionShape', as Qt's
  QHeightFieldShape is built on Qt's QAbstractCollisionShape, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHeightFieldShape that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'hfOffset', 'extents', 'setExtents', 'isStaticShape', 'image',
  'setImage', 'sourceChanged', 'extentsChanged', 'imageChanged',
  'imageDestroyed', 'imageGeometryChanged', 'updatePhysXGeometry',
  'updateExtents'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHeightFieldShape::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHeightFieldShape::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHeightFieldShape::~QHeightFieldShape()': the destructor: Python
    never removes a C++ QHeightFieldShape.
  - Qt's 'physx::PxGeometry *QHeightFieldShape::getPhysXGeometry()': gives
    'physx::PxGeometry', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QHeightFieldShape is created at the first use, not by
    'QHeightFieldShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHeightFieldShape.
  - Qt tells when it has removed the C++ QHeightFieldShape. Every call on the
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
    Calls Qt's 'QString QHeightFieldShape::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#tr

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
    #  QString QHeightFieldShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QHeightFieldShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHeightFieldShape'

  #  A C++ QHeightFieldShape Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHeightFieldShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHeightFieldShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHeightFieldShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHeightFieldShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'const QUrl &QHeightFieldShape::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  const QUrl &QHeightFieldShape::source() const
    address = self.uglySide.call('ritual_ZNK17QHeightFieldShape6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def hfOffset(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QHeightFieldShape::hfOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#hfOffset

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QHeightFieldShape::hfOffset() const
    address = self.uglySide.call('ritual_ZNK17QHeightFieldShape8hfOffsetEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def extents(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QHeightFieldShape::extents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#extents

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QHeightFieldShape::extents() const
    address = self.uglySide.call('ritual_ZNK17QHeightFieldShape7extentsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isStaticShape(self) -> bool:
    """
    Calls Qt's 'bool QHeightFieldShape::isStaticShape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#isStaticShape
    """
    #  bool QHeightFieldShape::isStaticShape() const
    ritual = 'ritual_ZNK17QHeightFieldShape13isStaticShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHeightFieldShape13isStaticShapeEv'
    return self.uglySide.call(ritual)

  def image(self) -> Optional[QQuickImage]:
    """
    Calls Qt's 'QQuickImage *QHeightFieldShape::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#image

    Returns
    -------

    Optional[QQuickImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImage *QHeightFieldShape::image() const
    address = self.uglySide.call('ritual_ZNK17QHeightFieldShape5imageEv')
    from ..QtQuick import QQuickImage
    return QQuickImage._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, newSource: QUrl) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::setSource(const QUrl &newSource)'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#setSource

    Parameters
    ----------

    newSource : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHeightFieldShape::setSource(const QUrl &newSource)
    self.uglySide.call(
        'ritual_ZN17QHeightFieldShape9setSourceERK4QUrl',
        self._valueOf(newSource),
    )

  @overload(QVector3D)
  def setExtents(self, newExtents: QVector3D) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::setExtents(const QVector3D
    &newExtents)'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#setExtents

    Parameters
    ----------

    newExtents : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QHeightFieldShape::setExtents(const QVector3D &newExtents)
    self.uglySide.call(
        'ritual_ZN17QHeightFieldShape10setExtentsERK9QVector3D',
        self._valueOf(newExtents),
    )

  @overload(QQuickImage)
  @overload(NoneType)
  def setImage(self, newImage: Optional[QQuickImage]) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::setImage(QQuickImage *newImage)'.

    Qt's own words: https://doc.qt.io/qt-6/qheightfieldshape.html#setImage

    Parameters
    ----------

    newImage : Optional[QQuickImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHeightFieldShape::setImage(QQuickImage *newImage)
    self.uglySide.call(
        'ritual_ZN17QHeightFieldShape8setImageEP11QQuickImage',
        self._addressOf(newImage),
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
    Notes what was given, for Qt's 'QHeightFieldShape::QHeightFieldShape()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#QHeightFieldShape
    """
    #  QHeightFieldShape::QHeightFieldShape()
    self._noteCreation(QHeightFieldShape, lambda: Rituals.call(
        'ritual_ZN17QHeightFieldShapeC1Ev',
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
    Calls Qt's 'void QHeightFieldShape::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#sourceChanged
    """
    #  void QHeightFieldShape::sourceChanged()
    self.uglySide.call('ritual_ZN17QHeightFieldShape13sourceChangedEv')

  def extentsChanged(self) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::extentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#extentsChanged
    """
    #  void QHeightFieldShape::extentsChanged()
    self.uglySide.call('ritual_ZN17QHeightFieldShape14extentsChangedEv')

  def imageChanged(self) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::imageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#imageChanged
    """
    #  void QHeightFieldShape::imageChanged()
    self.uglySide.call('ritual_ZN17QHeightFieldShape12imageChangedEv')

  @overload(QObject)
  @overload(NoneType)
  def imageDestroyed(self, image: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::imageDestroyed(QObject *image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#imageDestroyed

    Parameters
    ----------

    image : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHeightFieldShape::imageDestroyed(QObject *image)
    self.uglySide.call(
        'ritual_ZN17QHeightFieldShape14imageDestroyedEP7QObject',
        self._addressOf(image, 'QObject'),
    )

  def imageGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::imageGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#imageGeometryChanged
    """
    #  void QHeightFieldShape::imageGeometryChanged()
    self.uglySide.call(
        'ritual_ZN17QHeightFieldShape20imageGeometryChangedEv',
    )

  def updatePhysXGeometry(self) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::updatePhysXGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#updatePhysXGeometry
    """
    #  void QHeightFieldShape::updatePhysXGeometry()
    self.uglySide.call('ritual_ZN17QHeightFieldShape19updatePhysXGeometryEv')

  def updateExtents(self) -> None:
    """
    Calls Qt's 'void QHeightFieldShape::updateExtents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightfieldshape.html#updateExtents
    """
    #  void QHeightFieldShape::updateExtents()
    self.uglySide.call('ritual_ZN17QHeightFieldShape13updateExtentsEv')
