"""
Qt3DCore::QGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qgeometry.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QGeometry(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QGeometry: a plain Python object standing
  in front of one C++ Qt3DCore::QGeometry.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QGeometry is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QGeometry that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr',
  'addAttribute', 'removeAttribute', 'boundingVolumePositionAttribute',
  'minExtent', 'maxExtent', 'setBoundingVolumePositionAttribute',
  'boundingVolumePositionAttributeChanged', 'minExtentChanged',
  'maxExtentChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QGeometry::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QGeometry::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QGeometry::~QGeometry()': the destructor: Python never
    removes a C++ Qt3DCore::QGeometry.
  - Qt's 'QList<QAttribute *> Qt3DCore::QGeometry::attributes() const': gives
    a type Python has no way to take yet.
  - Qt's 'Qt3DCore::QGeometry::QGeometry(QGeometryPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QGeometryPrivate *Qt3DCore::QGeometry::d_func() const': takes
    in Python what 'QGeometryPrivate *Qt3DCore::QGeometry::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QGeometry is created at the first use, not by
    'Qt3DCore::QGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QGeometry.
  - Qt tells when it has removed the C++ Qt3DCore::QGeometry. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QGeometry that has no cute function yet,
    'attributes', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString Qt3DCore::QGeometry::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#tr

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
    #  QString Qt3DCore::QGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore9QGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QGeometry'

  #  A C++ Qt3DCore::QGeometry Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore9QGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingVolumePositionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'QAttribute
    *Qt3DCore::QGeometry::boundingVolumePositionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAttribute *Qt3DCore::QGeometry::boundingVolumePositionAttribute()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore9QGeometry31boundingVolumePositionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def minExtent(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QGeometry::minExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#minExtent

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QGeometry::minExtent() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore9QGeometry9minExtentEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def maxExtent(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QGeometry::maxExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#maxExtent

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QGeometry::maxExtent() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore9QGeometry9maxExtentEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QAttribute'])
  @overload(NoneType)
  def setBoundingVolumePositionAttribute(
      self,
      boundingVolumePositionAttribute: Optional[Qt3DCore.QAttribute],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QGeometry::setBoundingVolumePositionAttribute(QAttribute
    *boundingVolumePositionAttribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html

    Parameters
    ----------

    boundingVolumePositionAttribute : Optional[Qt3DCore.QAttribute]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DCore::QGeometry::setBoundingVolumePositionAttribute(QAttribute
    #      *boundingVolumePositionAttribute)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore9QGeometry34setBoundingVolumePositionAttributeEP'
        'NS_10QAttributeE',
        self._addressOf(boundingVolumePositionAttribute),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QGeometry::QGeometry(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#QGeometry

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QGeometry::QGeometry(Qt3DCore::QNode *parent)
    self._noteCreation(QGeometry, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore9QGeometryC1EPNS_5QNodeE',
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

  @overload(WAIT['Qt3DCore.QAttribute'])
  @overload(NoneType)
  def addAttribute(self, attribute: Optional[Qt3DCore.QAttribute]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometry::addAttribute(Qt3DCore::QAttribute
    *attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#addAttribute

    Parameters
    ----------

    attribute : Optional[Qt3DCore.QAttribute]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QGeometry::addAttribute(Qt3DCore::QAttribute
    #      *attribute)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore9QGeometry12addAttributeEPNS_10QAttributeE',
        self._addressOf(attribute),
    )

  @overload(WAIT['Qt3DCore.QAttribute'])
  @overload(NoneType)
  def removeAttribute(
      self,
      attribute: Optional[Qt3DCore.QAttribute],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QGeometry::removeAttribute(Qt3DCore::QAttribute *attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#removeAttribute

    Parameters
    ----------

    attribute : Optional[Qt3DCore.QAttribute]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QGeometry::removeAttribute(Qt3DCore::QAttribute
    #      *attribute)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore9QGeometry15removeAttributeEPNS_10QAttributeE',
        self._addressOf(attribute),
    )

  @overload(WAIT['Qt3DCore.QAttribute'])
  @overload(NoneType)
  def boundingVolumePositionAttributeChanged(
      self,
      boundingVolumePositionAttribute: Optional[Qt3DCore.QAttribute],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QGeometry::boundingVolumePositionAttributeChanged(QAttribute
    *boundingVolumePositionAttribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html

    Parameters
    ----------

    boundingVolumePositionAttribute : Optional[Qt3DCore.QAttribute]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QGeometry::boundingVolumePositionAttributeChanged(
    #      QAttribute *boundingVolumePositionAttribute)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore9QGeometry38boundingVolumePositionAttributeChang'
        'edEPNS_10QAttributeE',
        self._addressOf(boundingVolumePositionAttribute),
    )

  @overload(QVector3D)
  def minExtentChanged(self, minExtent: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometry::minExtentChanged(const QVector3D
    &minExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#minExtentChanged

    Parameters
    ----------

    minExtent : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QGeometry::minExtentChanged(const QVector3D &minExtent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore9QGeometry16minExtentChangedERK9QVector3D',
        self._valueOf(minExtent),
    )

  @overload(QVector3D)
  def maxExtentChanged(self, maxExtent: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QGeometry::maxExtentChanged(const QVector3D
    &maxExtent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#maxExtentChanged

    Parameters
    ----------

    maxExtent : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QGeometry::maxExtentChanged(const QVector3D &maxExtent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore9QGeometry16maxExtentChangedERK9QVector3D',
        self._valueOf(maxExtent),
    )

  def d_func(self) -> Optional[Qt3DCore.QGeometryPrivate]:
    """
    Calls Qt's 'QGeometryPrivate *Qt3DCore::QGeometry::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qgeometry.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometryPrivate *Qt3DCore::QGeometry::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore9QGeometry6d_funcEv')
    return Qt3DCore.QGeometryPrivate._cuteAt(address)

  @staticmethod
  def attributes(*__, **_) -> Never:
    """
    Qt's 'QList<QAttribute *> Qt3DCore::QGeometry::attributes() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QGeometry.attributes' has no cute function yet. Qt's "
        "'QList<QAttribute *> Qt3DCore::QGeometry::attributes() const': "
        "gives a type Python has no way to take yet.")
