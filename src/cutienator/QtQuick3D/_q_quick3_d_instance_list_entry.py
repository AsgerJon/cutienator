"""
QQuick3DInstanceListEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DInstanceListEntry to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QQuaternion, QVector3D, QVector4D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuaternion = WAIT['QQuaternion']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DInstanceListEntry(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DInstanceListEntry: a plain Python object
  standing in front of one C++ QQuick3DInstanceListEntry.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DInstanceListEntry
  is built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DInstanceListEntry that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'position',
  'scale', 'eulerRotation', 'rotation', 'color', 'customData', 'setPosition',
  'setScale', 'setEulerRotation', 'setRotation', 'setColor', 'setCustomData',
  'positionChanged', 'scaleChanged', 'eulerRotationChanged',
  'rotationChanged', 'colorChanged', 'customDataChanged', 'changed',
  'updateSpatialNode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DInstanceListEntry::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DInstanceListEntry::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DInstanceListEntry::~QQuick3DInstanceListEntry()': the
    destructor: Python never removes a C++ QQuick3DInstanceListEntry.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DInstanceListEntry is created at the first use, not by
    'QQuick3DInstanceListEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DInstanceListEntry.
  - Qt tells when it has removed the C++ QQuick3DInstanceListEntry. Every
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
    Calls Qt's 'QString QQuick3DInstanceListEntry::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#tr

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
    #  QString QQuick3DInstanceListEntry::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuick3DInstanceListEntry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DInstanceListEntry'

  #  A C++ QQuick3DInstanceListEntry Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DInstanceListEntry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DInstanceListEntry::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DInstanceListEntry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstanceListEntry::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstanceListEntry::position() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry8positionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def scale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstanceListEntry::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#scale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstanceListEntry::scale() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry5scaleEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def eulerRotation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstanceListEntry::eulerRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#eulerRotation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstanceListEntry::eulerRotation() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry13eulerRotationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DInstanceListEntry::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DInstanceListEntry::rotation() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry8rotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DInstanceListEntry::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DInstanceListEntry::color() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def customData(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuick3DInstanceListEntry::customData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#customData

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuick3DInstanceListEntry::customData() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DInstanceListEntry10customDataEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::setPosition(QVector3D
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DInstanceListEntry::setPosition(QVector3D position)
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry11setPositionE9QVector3D',
        self._valueOf(position),
    )

  @overload(QVector3D)
  def setScale(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::setScale(QVector3D scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#setScale

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DInstanceListEntry::setScale(QVector3D scale)
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry8setScaleE9QVector3D',
        self._valueOf(scale),
    )

  @overload(QVector3D)
  def setEulerRotation(self, eulerRotation: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::setEulerRotation(QVector3D
    eulerRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#setEulerRotation

    Parameters
    ----------

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DInstanceListEntry::setEulerRotation(QVector3D
    #      eulerRotation)
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry16setEulerRotationE9QVector3D',
        self._valueOf(eulerRotation),
    )

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::setRotation(QQuaternion
    rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QQuick3DInstanceListEntry::setRotation(QQuaternion rotation)
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry11setRotationE11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::setColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DInstanceListEntry::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry8setColorE6QColor',
        self._valueOf(color),
    )

  @overload(QVector4D)
  def setCustomData(self, customData: QVector4D) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::setCustomData(QVector4D
    customData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#setCustomData

    Parameters
    ----------

    customData : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QQuick3DInstanceListEntry::setCustomData(QVector4D customData)
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry13setCustomDataE9QVector4D',
        self._valueOf(customData),
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DInstanceListEntry::QQuick3DInstanceListEntry(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DInstanceListEntry::QQuick3DInstanceListEntry(QQuick3DObject
    #      *parent)
    self._noteCreation(QQuick3DInstanceListEntry, lambda: Rituals.call(
        'ritual_ZN25QQuick3DInstanceListEntryC1EP14QQuick3DObject',
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#positionChanged
    """
    #  void QQuick3DInstanceListEntry::positionChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry15positionChangedEv',
    )

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::scaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#scaleChanged
    """
    #  void QQuick3DInstanceListEntry::scaleChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry12scaleChangedEv',
    )

  def eulerRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::eulerRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html
    """
    #  void QQuick3DInstanceListEntry::eulerRotationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry20eulerRotationChangedEv',
    )

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#rotationChanged
    """
    #  void QQuick3DInstanceListEntry::rotationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry15rotationChangedEv',
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#colorChanged
    """
    #  void QQuick3DInstanceListEntry::colorChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry12colorChangedEv',
    )

  def customDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::customDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#customDataChanged
    """
    #  void QQuick3DInstanceListEntry::customDataChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DInstanceListEntry17customDataChangedEv',
    )

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceListEntry::changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#changed
    """
    #  void QQuick3DInstanceListEntry::changed()
    self.uglySide.call('ritual_ZN25QQuick3DInstanceListEntry7changedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      a0: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DInstanceListEntry::updateSpatialNode(QSSGRenderGraphObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelistentry.html#updateSpatialNode

    Parameters
    ----------

    a0 : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject *QQuick3DInstanceListEntry::updateSpatialNode(
    #      QSSGRenderGraphObject *a0)
    ritual = (
        'ritual_ZN25QQuick3DInstanceListEntry17updateSpatialNodeEP21QSSGRen'
        'derGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuick3DInstanceListEntry17updateSpatialNodeEP21Q'
          'SSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
