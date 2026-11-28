"""
QQuick3DInstancing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/qquick3dinstancing.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QQuaternion, QVector3D, QVector4D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DInstancingPrivate
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


class QQuick3DInstancing(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DInstancing: a plain Python object standing in
  front of one C++ QQuick3DInstancing.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DInstancing is
  built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DInstancing that has a ritual and that Python
  can call so far, 30 names in all: 'metaObject', 'tr', 'd_func',
  'instanceCountOverride', 'hasTransparency', 'depthSortingEnabled',
  'shadowBoundsMinimum', 'shadowBoundsMaximum', 'instancePosition',
  'instanceScale', 'instanceRotation', 'instanceColor', 'instanceCustomData',
  'setInstanceCountOverride', 'setHasTransparency', 'setDepthSortingEnabled',
  'setShadowBoundsMinimum', 'setShadowBoundsMaximum', 'instanceTableChanged',
  'instanceNodeDirty', 'instanceCountOverrideChanged',
  'hasTransparencyChanged', 'depthSortingEnabledChanged',
  'shadowBoundsMinimumChanged', 'shadowBoundsMaximumChanged', 'markDirty',
  'calculateTableEntry', 'calculateTableEntryFromQuaternion',
  'updateSpatialNode', 'getInstanceEntry'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DInstancing::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DInstancing::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuick3DInstancingPrivate *QQuick3DInstancing::d_func()
    const': takes in Python what 'QQuick3DInstancingPrivate
    *QQuick3DInstancing::d_func()' takes.
  - Qt's 'void QQuick3DInstancing::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QQuick3DInstancing::~QQuick3DInstancing()': the destructor: Python
    never removes a C++ QQuick3DInstancing.
  - Qt's 'QByteArray QQuick3DInstancing::instanceBuffer(int *instanceCount)':
    takes a number to change where it is.
  - Qt's 'QByteArray QQuick3DInstancing::getInstanceBuffer(int
    *instanceCount)': takes a number to change where it is.

  What has no ritual
  ------------------

  3 of the 40 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQuick3DInstancing is created at the first use, not by
    'QQuick3DInstancing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DInstancing.
  - Qt tells when it has removed the C++ QQuick3DInstancing. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DInstancing that has no cute function yet,
    '__init__', 'getInstanceBuffer', 'instanceBuffer', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuick3DInstancing, each a class in here as
  #  in C++.

  class InstanceTableEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DInstancing::InstanceTableEntry: a plain
    Python object standing in front of one C++
    QQuick3DInstancing::InstanceTableEntry.

    C++ hands a QQuick3DInstancing::InstanceTableEntry around as a copy, so
    every C++ QQuick3DInstancing::InstanceTableEntry behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuick3DInstancing::InstanceTableEntry that has a
    ritual and that Python can call so far, 4 names in all: 'getPosition',
    'getScale', 'getRotation', 'getColor'. None can be made from Python: one
    comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DInstancing::InstanceTableEntry::~InstanceTableEntry()':
      the destructor: Python removes its C++
      QQuick3DInstancing::InstanceTableEntry by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQuick3DInstancing::InstanceTableEntry is created at the first
      use, not by 'QQuick3DInstancing::InstanceTableEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DInstancing::InstanceTableEntry back gives a
      copy the ritual made for Python, in a new cute
      QQuick3DInstancing::InstanceTableEntry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DInstancing::InstanceTableEntry'

    #  Qt's '~QQuick3DInstancing::InstanceTableEntry()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QQuick3DInstancing::InstanceTableEntry behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18QQuick3DInstancing18InstanceTableEntryD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def getPosition(self) -> QVector3D:
      """
      Calls Qt's 'QVector3D
      QQuick3DInstancing::InstanceTableEntry::getPosition() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dinstancing-instancetableentry.html

      Returns
      -------

      QVector3D
        A new cute QVector3D around the copy Qt gave back. Python owns it.
      """
      #  QVector3D QQuick3DInstancing::InstanceTableEntry::getPosition()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK18QQuick3DInstancing18InstanceTableEntry11getPositionE'
          'v',
      )
      from ..QtGui import QVector3D
      return QVector3D._cuteOwning(address)

    def getScale(self) -> QVector3D:
      """
      Calls Qt's 'QVector3D
      QQuick3DInstancing::InstanceTableEntry::getScale() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dinstancing-instancetableentry.html

      Returns
      -------

      QVector3D
        A new cute QVector3D around the copy Qt gave back. Python owns it.
      """
      #  QVector3D QQuick3DInstancing::InstanceTableEntry::getScale() const
      address = self.uglySide.call(
          'ritual_ZNK18QQuick3DInstancing18InstanceTableEntry8getScaleEv',
      )
      from ..QtGui import QVector3D
      return QVector3D._cuteOwning(address)

    def getRotation(self) -> QQuaternion:
      """
      Calls Qt's 'QQuaternion
      QQuick3DInstancing::InstanceTableEntry::getRotation() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dinstancing-instancetableentry.html

      Returns
      -------

      QQuaternion
        A new cute QQuaternion around the copy Qt gave back. Python owns it.
      """
      #  QQuaternion QQuick3DInstancing::InstanceTableEntry::getRotation()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK18QQuick3DInstancing18InstanceTableEntry11getRotationE'
          'v',
      )
      from ..QtGui import QQuaternion
      return QQuaternion._cuteOwning(address)

    def getColor(self) -> QColor:
      """
      Calls Qt's 'QColor QQuick3DInstancing::InstanceTableEntry::getColor()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dinstancing-instancetableentry.html

      Returns
      -------

      QColor
        A new cute QColor around the copy Qt gave back. Python owns it.
      """
      #  QColor QQuick3DInstancing::InstanceTableEntry::getColor() const
      address = self.uglySide.call(
          'ritual_ZNK18QQuick3DInstancing18InstanceTableEntry8getColorEv',
      )
      from ..QtGui import QColor
      return QColor._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QQuick3DInstancing::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancing.html#tr

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
    #  QString QQuick3DInstancing::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuick3DInstancing2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QVector3D, QVector3D, QVector3D, QColor)
  @overload(QVector3D, QVector3D, QVector3D, QColor, QVector4D)
  def calculateTableEntry(
      position: QVector3D,
      scale: QVector3D,
      eulerRotation: QVector3D,
      color: QColor,
      customData: Optional[QVector4D] = None,
  ) -> InstanceTableEntry:
    """
    Calls Qt's 'InstanceTableEntry
    QQuick3DInstancing::calculateTableEntry(const QVector3D &position, const
    QVector3D &scale, const QVector3D &eulerRotation, const QColor &color,
    const QVector4D &customData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#calculateTableEntry

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    customData : Optional[QVector4D]
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector4D()' is then passed on.

    Returns
    -------

    InstanceTableEntry
      A new cute QQuick3DInstancing::InstanceTableEntry around the copy Qt
      gave back. Python owns it.
    """
    #  InstanceTableEntry QQuick3DInstancing::calculateTableEntry(const
    #      QVector3D &position, const QVector3D &scale, const QVector3D
    #      &eulerRotation, const QColor &color, const QVector4D &customData)
    if customData is None:
      from ..QtGui import QVector4D
      customData = QVector4D()
    address = Rituals.call(
        'ritual_ZN18QQuick3DInstancing19calculateTableEntryERK9QVector3DS2_'
        'S2_RK6QColorRK9QVector4D',
        CuteMixin._valueOf(position), CuteMixin._valueOf(scale),
        CuteMixin._valueOf(eulerRotation), CuteMixin._valueOf(color),
        CuteMixin._valueOf(customData),
    )
    return QQuick3DInstancing.InstanceTableEntry._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D, QQuaternion, QColor)
  @overload(QVector3D, QVector3D, QQuaternion, QColor, QVector4D)
  def calculateTableEntryFromQuaternion(
      position: QVector3D,
      scale: QVector3D,
      rotation: QQuaternion,
      color: QColor,
      customData: Optional[QVector4D] = None,
  ) -> InstanceTableEntry:
    """
    Calls Qt's 'InstanceTableEntry
    QQuick3DInstancing::calculateTableEntryFromQuaternion(const QVector3D
    &position, const QVector3D &scale, const QQuaternion &rotation, const
    QColor &color, const QVector4D &customData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    customData : Optional[QVector4D]
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector4D()' is then passed on.

    Returns
    -------

    InstanceTableEntry
      A new cute QQuick3DInstancing::InstanceTableEntry around the copy Qt
      gave back. Python owns it.
    """
    #  InstanceTableEntry
    #      QQuick3DInstancing::calculateTableEntryFromQuaternion(const
    #      QVector3D &position, const QVector3D &scale, const QQuaternion
    #      &rotation, const QColor &color, const QVector4D &customData)
    if customData is None:
      from ..QtGui import QVector4D
      customData = QVector4D()
    address = Rituals.call(
        'ritual_ZN18QQuick3DInstancing33calculateTableEntryFromQuaternionER'
        'K9QVector3DS2_RK11QQuaternionRK6QColorRK9QVector4D',
        CuteMixin._valueOf(position), CuteMixin._valueOf(scale),
        CuteMixin._valueOf(rotation), CuteMixin._valueOf(color),
        CuteMixin._valueOf(customData),
    )
    return QQuick3DInstancing.InstanceTableEntry._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DInstancing'

  #  A C++ QQuick3DInstancing Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DInstancing'

  #  The functions Qt calls itself that QQuick3DInstancing is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getInstanceBuffer': (
          'QByteArray QQuick3DInstancing::getInstanceBuffer(int *)',
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
    Calls Qt's 'const QMetaObject *QQuick3DInstancing::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancing.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DInstancing::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DInstancing10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def instanceCountOverride(self) -> int:
    """
    Calls Qt's 'int QQuick3DInstancing::instanceCountOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceCountOverride
    """
    #  int QQuick3DInstancing::instanceCountOverride() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DInstancing21instanceCountOverrideEv',
    )

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DInstancing::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#hasTransparency
    """
    #  bool QQuick3DInstancing::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DInstancing15hasTransparencyEv',
    )

  def depthSortingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DInstancing::depthSortingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#depthSortingEnabled
    """
    #  bool QQuick3DInstancing::depthSortingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DInstancing19depthSortingEnabledEv',
    )

  def shadowBoundsMinimum(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstancing::shadowBoundsMinimum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#shadowBoundsMinimum

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstancing::shadowBoundsMinimum() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DInstancing19shadowBoundsMinimumEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def shadowBoundsMaximum(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstancing::shadowBoundsMaximum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#shadowBoundsMaximum

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstancing::shadowBoundsMaximum() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DInstancing19shadowBoundsMaximumEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInstanceCountOverride(self, instanceCountOverride: int) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::setInstanceCountOverride(int
    instanceCountOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#setInstanceCountOverride

    Parameters
    ----------

    instanceCountOverride : int
      Passed on as it is.
    """
    #  void QQuick3DInstancing::setInstanceCountOverride(int
    #      instanceCountOverride)
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing24setInstanceCountOverrideEi',
        instanceCountOverride,
    )

  @overload(bool)
  def setHasTransparency(self, hasTransparency: bool) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::setHasTransparency(bool
    hasTransparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#setHasTransparency

    Parameters
    ----------

    hasTransparency : bool
      Passed on as it is.
    """
    #  void QQuick3DInstancing::setHasTransparency(bool hasTransparency)
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing18setHasTransparencyEb',
        hasTransparency,
    )

  @overload(bool)
  def setDepthSortingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::setDepthSortingEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#setDepthSortingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DInstancing::setDepthSortingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing22setDepthSortingEnabledEb', enabled,
    )

  @overload(QVector3D)
  def setShadowBoundsMinimum(
      self,
      newShadowBoundsMinimum: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::setShadowBoundsMinimum(const
    QVector3D &newShadowBoundsMinimum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#setShadowBoundsMinimum

    Parameters
    ----------

    newShadowBoundsMinimum : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DInstancing::setShadowBoundsMinimum(const QVector3D
    #      &newShadowBoundsMinimum)
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing22setShadowBoundsMinimumERK9QVector3D',
        self._valueOf(newShadowBoundsMinimum),
    )

  @overload(QVector3D)
  def setShadowBoundsMaximum(
      self,
      newShadowBoundsMinimum: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::setShadowBoundsMaximum(const
    QVector3D &newShadowBoundsMinimum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#setShadowBoundsMaximum

    Parameters
    ----------

    newShadowBoundsMinimum : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DInstancing::setShadowBoundsMaximum(const QVector3D
    #      &newShadowBoundsMinimum)
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing22setShadowBoundsMaximumERK9QVector3D',
        self._valueOf(newShadowBoundsMinimum),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuick3DInstancing::QQuick3DInstancing(QQuick3DObject *parent)':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQuick3DInstancing.__init__' has no cute function yet. Qt's "
        "'QQuick3DInstancing::QQuick3DInstancing(QQuick3DObject *parent)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QQuick3DInstancingPrivate]:
    """
    Calls Qt's 'QQuick3DInstancingPrivate *QQuick3DInstancing::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancing.html#d_func

    Returns
    -------

    Optional[QQuick3DInstancingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstancingPrivate *QQuick3DInstancing::d_func()
    address = self.uglySide.call('ritual_ZN18QQuick3DInstancing6d_funcEv')
    from . import QQuick3DInstancingPrivate
    return QQuick3DInstancingPrivate._cuteAt(address)

  @overload(int)
  def instancePosition(self, index: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstancing::instancePosition(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instancePosition

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstancing::instancePosition(int index)
    address = self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing16instancePositionEi', index,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def instanceScale(self, index: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DInstancing::instanceScale(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceScale

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DInstancing::instanceScale(int index)
    address = self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing13instanceScaleEi', index,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def instanceRotation(self, index: int) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DInstancing::instanceRotation(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceRotation

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DInstancing::instanceRotation(int index)
    address = self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing16instanceRotationEi', index,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(int)
  def instanceColor(self, index: int) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DInstancing::instanceColor(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DInstancing::instanceColor(int index)
    address = self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing13instanceColorEi', index,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(int)
  def instanceCustomData(self, index: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuick3DInstancing::instanceCustomData(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceCustomData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuick3DInstancing::instanceCustomData(int index)
    address = self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing18instanceCustomDataEi', index,
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def instanceTableChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::instanceTableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceTableChanged
    """
    #  void QQuick3DInstancing::instanceTableChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing20instanceTableChangedEv',
    )

  def instanceNodeDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::instanceNodeDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#instanceNodeDirty
    """
    #  void QQuick3DInstancing::instanceNodeDirty()
    self.uglySide.call('ritual_ZN18QQuick3DInstancing17instanceNodeDirtyEv')

  def instanceCountOverrideChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::instanceCountOverrideChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html
    """
    #  void QQuick3DInstancing::instanceCountOverrideChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing28instanceCountOverrideChangedEv',
    )

  def hasTransparencyChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::hasTransparencyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#hasTransparencyChanged
    """
    #  void QQuick3DInstancing::hasTransparencyChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing22hasTransparencyChangedEv',
    )

  def depthSortingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::depthSortingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#depthSortingEnabledChanged
    """
    #  void QQuick3DInstancing::depthSortingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing26depthSortingEnabledChangedEv',
    )

  def shadowBoundsMinimumChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::shadowBoundsMinimumChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#shadowBoundsMinimumChanged
    """
    #  void QQuick3DInstancing::shadowBoundsMinimumChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing26shadowBoundsMinimumChangedEv',
    )

  def shadowBoundsMaximumChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::shadowBoundsMaximumChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#shadowBoundsMaximumChanged
    """
    #  void QQuick3DInstancing::shadowBoundsMaximumChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing26shadowBoundsMaximumChangedEv',
    )

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstancing::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancing.html#markDirty
    """
    #  void QQuick3DInstancing::markDirty()
    self.uglySide.call('ritual_ZN18QQuick3DInstancing9markDirtyEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN18QQuick3DInstancing17updateSpatialNodeEP21QSSGRenderGrap'
        'hObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuick3DInstancing17updateSpatialNodeEP21QSSGRend'
          'erGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(int)
  def getInstanceEntry(self, index: int) -> Optional[InstanceTableEntry]:
    """
    Calls Qt's 'const InstanceTableEntry
    *QQuick3DInstancing::getInstanceEntry(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancing.html#getInstanceEntry

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[InstanceTableEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const InstanceTableEntry *QQuick3DInstancing::getInstanceEntry(int
    #      index)
    address = self.uglySide.call(
        'ritual_ZN18QQuick3DInstancing16getInstanceEntryEi', index,
    )
    return QQuick3DInstancing.InstanceTableEntry._cuteAt(address)

  @staticmethod
  def getInstanceBuffer(*__, **_) -> Never:
    """
    Qt's 'QByteArray QQuick3DInstancing::getInstanceBuffer(int
    *instanceCount)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuick3DInstancing.getInstanceBuffer' has no cute function yet. "
        "Qt's 'QByteArray QQuick3DInstancing::getInstanceBuffer(int "
        "*instanceCount)': takes a number to change where it is.")

  @staticmethod
  def instanceBuffer(*__, **_) -> Never:
    """
    Qt's 'QByteArray QQuick3DInstancing::instanceBuffer(int *instanceCount)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuick3DInstancing.instanceBuffer' has no cute function yet. Qt's "
        "'QByteArray QQuick3DInstancing::instanceBuffer(int "
        "*instanceCount)': takes a number to change where it is.")
