"""
Q3DCameraPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dcamera_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Q3DCameraPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']


class Q3DCameraPrivate(QObject):
  """
  The cute side of Qt's Q3DCameraPrivate: a plain Python object standing in
  front of one C++ Q3DCameraPrivate.

  It is built on the cute 'QObject', as Qt's Q3DCameraPrivate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DCameraPrivate that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'setXRotation',
  'setYRotation', 'minXRotation', 'minYRotation', 'maxXRotation',
  'maxYRotation', 'viewMatrix', 'isViewMatrixAutoUpdateEnabled',
  'setBaseOrientation', 'calculatePositionRelativeToCamera',
  'minXRotationChanged', 'minYRotationChanged', 'maxXRotationChanged',
  'maxYRotationChanged', 'viewMatrixChanged', 'viewMatrixAutoUpdateChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DCameraPrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Q3DCameraPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DCameraPrivate::~Q3DCameraPrivate()': the destructor: Python
    never removes a C++ Q3DCameraPrivate.
  - Qt's 'void Q3DCameraPrivate::sync(Q3DCamera &other)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  11 of the 32 functions Qt declares: 9 leans on 'Q3DCameraPrivate; 2 not a
  gap.

  What to expect
  --------------

  - The C++ Q3DCameraPrivate is created at the first use, not by
    'Q3DCameraPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DCameraPrivate.
  - Qt tells when it has removed the C++ Q3DCameraPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Q3DCameraPrivate that has no cute function yet,
    '__init__', 'setMaxXRotation', 'setMaxYRotation', 'setMinXRotation',
    'setMinYRotation', 'setViewMatrix', 'setViewMatrixAutoUpdateEnabled',
    'sync', 'updateViewMatrix', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DCameraPrivate'

  #  A C++ Q3DCameraPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DCameraPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DCameraPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DCameraPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16Q3DCameraPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minXRotation(self) -> float:
    """
    Calls Qt's 'float Q3DCameraPrivate::minXRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#minXRotation
    """
    #  float Q3DCameraPrivate::minXRotation() const
    return self.uglySide.call('ritual_ZNK16Q3DCameraPrivate12minXRotationEv')

  def minYRotation(self) -> float:
    """
    Calls Qt's 'float Q3DCameraPrivate::minYRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#minYRotation
    """
    #  float Q3DCameraPrivate::minYRotation() const
    return self.uglySide.call('ritual_ZNK16Q3DCameraPrivate12minYRotationEv')

  def maxXRotation(self) -> float:
    """
    Calls Qt's 'float Q3DCameraPrivate::maxXRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#maxXRotation
    """
    #  float Q3DCameraPrivate::maxXRotation() const
    return self.uglySide.call('ritual_ZNK16Q3DCameraPrivate12maxXRotationEv')

  def maxYRotation(self) -> float:
    """
    Calls Qt's 'float Q3DCameraPrivate::maxYRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#maxYRotation
    """
    #  float Q3DCameraPrivate::maxYRotation() const
    return self.uglySide.call('ritual_ZNK16Q3DCameraPrivate12maxYRotationEv')

  def viewMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Q3DCameraPrivate::viewMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#viewMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Q3DCameraPrivate::viewMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK16Q3DCameraPrivate10viewMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def isViewMatrixAutoUpdateEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DCameraPrivate::isViewMatrixAutoUpdateEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html
    """
    #  bool Q3DCameraPrivate::isViewMatrixAutoUpdateEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16Q3DCameraPrivate29isViewMatrixAutoUpdateEnabledEv',
    )

  @overload(QVector3D, float, float)
  def calculatePositionRelativeToCamera(
      self,
      relativePosition: QVector3D,
      fixedRotation: float,
      distanceModifier: float,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Q3DCameraPrivate::calculatePositionRelativeToCamera(const QVector3D
    &relativePosition, float fixedRotation, float distanceModifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html

    Parameters
    ----------

    relativePosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    fixedRotation : float
      Passed on as it is.

    distanceModifier : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Q3DCameraPrivate::calculatePositionRelativeToCamera(const
    #      QVector3D &relativePosition, float fixedRotation, float
    #      distanceModifier) const
    address = self.uglySide.call(
        'ritual_ZNK16Q3DCameraPrivate33calculatePositionRelativeToCameraERK'
        '9QVector3Dff',
        self._valueOf(relativePosition), fixedRotation, distanceModifier,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::setXRotation(float rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#setXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::setXRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate12setXRotationEf', rotation,
    )

  @overload(float)
  def setYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::setYRotation(float rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcameraprivate.html#setYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::setYRotation(float rotation)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate12setYRotationEf', rotation,
    )

  @overload(QVector3D, QVector3D, QVector3D)
  def setBaseOrientation(
      self,
      defaultPosition: QVector3D,
      defaultTarget: QVector3D,
      defaultUp: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::setBaseOrientation(const QVector3D
    &defaultPosition, const QVector3D &defaultTarget, const QVector3D
    &defaultUp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#setBaseOrientation

    Parameters
    ----------

    defaultPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    defaultTarget : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    defaultUp : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DCameraPrivate::setBaseOrientation(const QVector3D
    #      &defaultPosition, const QVector3D &defaultTarget, const QVector3D
    #      &defaultUp)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate18setBaseOrientationERK9QVector3DS2_S2_',
        self._valueOf(defaultPosition), self._valueOf(defaultTarget),
        self._valueOf(defaultUp),
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
    Qt's 'Q3DCameraPrivate::Q3DCameraPrivate(Q3DCamera *q)': leans on
    'Q3DCameraPrivate::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.__init__' has no cute function yet. Qt's "
        "'Q3DCameraPrivate::Q3DCameraPrivate(Q3DCamera *q)': leans on "
        "'Q3DCameraPrivate::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(float)
  def minXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::minXRotationChanged(float rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#minXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::minXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate19minXRotationChangedEf', rotation,
    )

  @overload(float)
  def minYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::minYRotationChanged(float rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#minYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::minYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate19minYRotationChangedEf', rotation,
    )

  @overload(float)
  def maxXRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::maxXRotationChanged(float rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#maxXRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::maxXRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate19maxXRotationChangedEf', rotation,
    )

  @overload(float)
  def maxYRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::maxYRotationChanged(float rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#maxYRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::maxYRotationChanged(float rotation)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate19maxYRotationChangedEf', rotation,
    )

  @overload(QMatrix4x4)
  def viewMatrixChanged(self, viewMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::viewMatrixChanged(const QMatrix4x4
    &viewMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#viewMatrixChanged

    Parameters
    ----------

    viewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Q3DCameraPrivate::viewMatrixChanged(const QMatrix4x4 &viewMatrix)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate17viewMatrixChangedERK10QMatrix4x4',
        self._valueOf(viewMatrix),
    )

  @overload(bool)
  def viewMatrixAutoUpdateChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcameraprivate.html#viewMatrixAutoUpdateChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16Q3DCameraPrivate27viewMatrixAutoUpdateChangedEb',
        enabled,
    )

  @staticmethod
  def setMaxXRotation(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::setMaxXRotation(float rotation)': leans on
    'Q3DCameraPrivate::maxXRotationChanged(float)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.setMaxXRotation' has no cute function yet. Qt's "
        "'void Q3DCameraPrivate::setMaxXRotation(float rotation)': leans on "
        "'Q3DCameraPrivate::maxXRotationChanged(float)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setMaxYRotation(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::setMaxYRotation(float rotation)': leans on
    'Q3DCameraPrivate::maxYRotationChanged(float)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.setMaxYRotation' has no cute function yet. Qt's "
        "'void Q3DCameraPrivate::setMaxYRotation(float rotation)': leans on "
        "'Q3DCameraPrivate::maxYRotationChanged(float)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setMinXRotation(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::setMinXRotation(float rotation)': leans on
    'Q3DCameraPrivate::minXRotationChanged(float)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.setMinXRotation' has no cute function yet. Qt's "
        "'void Q3DCameraPrivate::setMinXRotation(float rotation)': leans on "
        "'Q3DCameraPrivate::minXRotationChanged(float)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setMinYRotation(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::setMinYRotation(float rotation)': leans on
    'Q3DCameraPrivate::minYRotationChanged(float)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.setMinYRotation' has no cute function yet. Qt's "
        "'void Q3DCameraPrivate::setMinYRotation(float rotation)': leans on "
        "'Q3DCameraPrivate::minYRotationChanged(float)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setViewMatrix(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::setViewMatrix(const QMatrix4x4
    &viewMatrix)': leans on 'Q3DCameraPrivate::viewMatrixChanged(QMatrix4x4
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.setViewMatrix' has no cute function yet. Qt's "
        "'void Q3DCameraPrivate::setViewMatrix(const QMatrix4x4 "
        "&viewMatrix)': leans on "
        "'Q3DCameraPrivate::viewMatrixChanged(QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setViewMatrixAutoUpdateEnabled(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::setViewMatrixAutoUpdateEnabled(bool
    isEnabled)': leans on
    'Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.setViewMatrixAutoUpdateEnabled' has no cute "
        "function yet. Qt's 'void "
        "Q3DCameraPrivate::setViewMatrixAutoUpdateEnabled(bool isEnabled)': "
        "leans on 'Q3DCameraPrivate::viewMatrixAutoUpdateChanged(bool)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::sync(Q3DCamera &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.sync' has no cute function yet. Qt's 'void "
        "Q3DCameraPrivate::sync(Q3DCamera &other)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def updateViewMatrix(*__, **_) -> Never:
    """
    Qt's 'void Q3DCameraPrivate::updateViewMatrix(float zoomAdjustment)':
    leans on 'Q3DCameraPrivate::viewMatrixChanged(QMatrix4x4 const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'Q3DCameraPrivate.updateViewMatrix' has no cute function yet. Qt's "
        "'void Q3DCameraPrivate::updateViewMatrix(float zoomAdjustment)': "
        "leans on 'Q3DCameraPrivate::viewMatrixChanged(QMatrix4x4 const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
