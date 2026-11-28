"""
QQuick3DSkin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dskin_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DSkin to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSkin(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DSkin: a plain Python object standing in front
  of one C++ QQuick3DSkin.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DSkin is built on
  Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSkin that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'inverseBindPoses',
  'setInverseBindPoses', 'inverseBindPosesChanged', 'updateSpatialNode'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSkin::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DSkin::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DSkin::~QQuick3DSkin()': the destructor: Python never
    removes a C++ QQuick3DSkin.
  - Qt's 'QQmlListProperty<QQuick3DNode> QQuick3DSkin::joints()': gives a
    type Python has no way to take yet.
  - Qt's 'void QQuick3DSkin::qmlAppendJoint(QQmlListProperty<QQuick3DNode>
    *list, QQuick3DNode *joint)': names 'QQmlListProperty<QQuick3DNode>',
    which has no cute class yet.
  - Qt's 'QQuick3DNode
    *QQuick3DSkin::qmlJointAt(QQmlListProperty<QQuick3DNode> *list, qsizetype
    index)': names 'QQmlListProperty<QQuick3DNode>', which has no cute class
    yet.
  - Qt's 'qsizetype
    QQuick3DSkin::qmlJointsCount(QQmlListProperty<QQuick3DNode> *list)':
    names 'QQmlListProperty<QQuick3DNode>', which has no cute class yet.
  - Qt's 'void QQuick3DSkin::qmlClearJoints(QQmlListProperty<QQuick3DNode>
    *list)': names 'QQmlListProperty<QQuick3DNode>', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DSkin is created at the first use, not by
    'QQuick3DSkin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSkin.
  - Qt tells when it has removed the C++ QQuick3DSkin. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuick3DSkin that has no cute function yet, 'joints',
    'qmlAppendJoint', 'qmlClearJoints', 'qmlJointAt', 'qmlJointsCount', holds
    a function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuick3DSkin::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dskin.html#tr

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
    #  QString QQuick3DSkin::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuick3DSkin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSkin'

  #  A C++ QQuick3DSkin Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DSkin'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DSkin::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dskin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSkin::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DSkin10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inverseBindPoses(self) -> QList[QMatrix4x4]:
    """
    Calls Qt's 'QList<QMatrix4x4> QQuick3DSkin::inverseBindPoses() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dskin.html#inverseBindPoses

    Returns
    -------

    QList[QMatrix4x4]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMatrix4x4> QQuick3DSkin::inverseBindPoses() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DSkin16inverseBindPosesEv',
    )
    from ..QtGui import QMatrix4x4
    return QList[QMatrix4x4]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QMatrix4x4])
  def setInverseBindPoses(self, poses: QList[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QQuick3DSkin::setInverseBindPoses(const
    QList<QMatrix4x4> &poses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskin.html#setInverseBindPoses

    Parameters
    ----------

    poses : QList[QMatrix4x4]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuick3DSkin::setInverseBindPoses(const QList<QMatrix4x4> &poses)
    self.uglySide.call(
        'ritual_ZN12QQuick3DSkin19setInverseBindPosesERK5QListI10QMatrix4x4'
        'E',
        self._valueOf(poses),
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
    Notes what was given, for Qt's 'QQuick3DSkin::QQuick3DSkin(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dskin.html#QQuick3DSkin

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DSkin::QQuick3DSkin(QQuick3DObject *parent)
    self._noteCreation(QQuick3DSkin, lambda: Rituals.call(
        'ritual_ZN12QQuick3DSkinC1EP14QQuick3DObject',
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

  def inverseBindPosesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkin::inverseBindPosesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskin.html#inverseBindPosesChanged
    """
    #  void QQuick3DSkin::inverseBindPosesChanged()
    self.uglySide.call('ritual_ZN12QQuick3DSkin23inverseBindPosesChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DSkin::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskin.html#updateSpatialNode

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
    #      *QQuick3DSkin::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN12QQuick3DSkin17updateSpatialNodeEP21QSSGRenderGraphObjec'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuick3DSkin17updateSpatialNodeEP21QSSGRenderGrap'
          'hObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @staticmethod
  def joints(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DNode> QQuick3DSkin::joints()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSkin.joints' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DNode> QQuick3DSkin::joints()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def qmlAppendJoint(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSkin::qmlAppendJoint(QQmlListProperty<QQuick3DNode>
    *list, QQuick3DNode *joint)': names 'QQmlListProperty<QQuick3DNode>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DSkin.qmlAppendJoint' has no cute function yet. Qt's 'void "
        "QQuick3DSkin::qmlAppendJoint(QQmlListProperty<QQuick3DNode> *list, "
        "QQuick3DNode *joint)': names 'QQmlListProperty<QQuick3DNode>', "
        "which has no cute class yet.")

  @staticmethod
  def qmlClearJoints(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSkin::qmlClearJoints(QQmlListProperty<QQuick3DNode>
    *list)': names 'QQmlListProperty<QQuick3DNode>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DSkin.qmlClearJoints' has no cute function yet. Qt's 'void "
        "QQuick3DSkin::qmlClearJoints(QQmlListProperty<QQuick3DNode> "
        "*list)': names 'QQmlListProperty<QQuick3DNode>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlJointAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DNode
    *QQuick3DSkin::qmlJointAt(QQmlListProperty<QQuick3DNode> *list, qsizetype
    index)': names 'QQmlListProperty<QQuick3DNode>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DSkin.qmlJointAt' has no cute function yet. Qt's "
        "'QQuick3DNode "
        "*QQuick3DSkin::qmlJointAt(QQmlListProperty<QQuick3DNode> *list, "
        "qsizetype index)': names 'QQmlListProperty<QQuick3DNode>', which "
        "has no cute class yet.")

  @staticmethod
  def qmlJointsCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuick3DSkin::qmlJointsCount(QQmlListProperty<QQuick3DNode> *list)':
    names 'QQmlListProperty<QQuick3DNode>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DSkin.qmlJointsCount' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuick3DSkin::qmlJointsCount(QQmlListProperty<QQuick3DNode> "
        "*list)': names 'QQmlListProperty<QQuick3DNode>', which has no cute "
        "class yet.")
