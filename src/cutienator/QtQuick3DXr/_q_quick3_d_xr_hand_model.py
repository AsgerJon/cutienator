"""
QQuick3DXrHandModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandmodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrHandModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtQuick3D import QQuick3DModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuick3DXrHandModel(QQuick3DModel):
  """
  The cute side of Qt's QQuick3DXrHandModel: a plain Python object standing
  in front of one C++ QQuick3DXrHandModel.

  It is built on the cute 'QQuick3DModel', as Qt's QQuick3DXrHandModel is
  built on Qt's QQuick3DModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrHandModel that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'componentComplete',
  'hand', 'handChanged', 'handTrackerChanged', 'updatePose'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrHandModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrHandModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QQuick3DXrHandModel; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file; 1 leans on 'vtable for
  QQuick3DXrHandModel', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuick3DXrHandModel is created at the first use, not by
    'QQuick3DXrHandModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrHandModel.
  - Qt tells when it has removed the C++ QQuick3DXrHandModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrHandModel that has no cute function yet,
    '__init__', 'setHand', 'setupModel', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DXrHandModel, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Hand(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrHandModel::Hand' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    LeftHand = Kee[int](0)
    RightHand = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrHandModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrHandModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrHandModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hand(self) -> Hand:
    """
    Calls Qt's 'Hand QQuick3DXrHandModel::hand() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrhandmodel.html#hand

    Returns
    -------

    Hand
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Hand(number)' gives.
    """
    #  Hand QQuick3DXrHandModel::hand() const
    return QQuick3DXrHandModel.Hand(self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandModel4handEv',
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
    Qt's 'QQuick3DXrHandModel::QQuick3DXrHandModel(QQuick3DNode *parent)':
    leans on 'vtable for QQuick3DXrHandModel', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandModel.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrHandModel::QQuick3DXrHandModel(QQuick3DNode *parent)': "
        "leans on 'vtable for QQuick3DXrHandModel', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandmodel.html#componentComplete
    """
    #  void QQuick3DXrHandModel::componentComplete()
    self.uglySide.call('ritual_ZN19QQuick3DXrHandModel17componentCompleteEv')

  def handChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandModel::handChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandmodel.html#handChanged
    """
    #  void QQuick3DXrHandModel::handChanged()
    self.uglySide.call('ritual_ZN19QQuick3DXrHandModel11handChangedEv')

  def handTrackerChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandModel::handTrackerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandmodel.html#handTrackerChanged
    """
    #  void QQuick3DXrHandModel::handTrackerChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandModel18handTrackerChangedEv',
    )

  def updatePose(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandModel::updatePose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandmodel.html#updatePose
    """
    #  void QQuick3DXrHandModel::updatePose()
    self.uglySide.call('ritual_ZN19QQuick3DXrHandModel10updatePoseEv')

  @staticmethod
  def setHand(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHandModel::setHand(Hand newHand)': leans on
    'QQuick3DXrHandModel::handChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandModel.setHand' has no cute function yet. Qt's 'void "
        "QQuick3DXrHandModel::setHand(Hand newHand)': leans on "
        "'QQuick3DXrHandModel::handChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setupModel(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHandModel::setupModel()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    incomplete type 'QQuick3DXrInputManagerPrivate' named in nested name
    specifier.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandModel.setupModel' has no cute function yet. Qt's "
        "'void QQuick3DXrHandModel::setupModel()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: incomplete type 'QQuick3DXrInputManagerPrivate' named in "
        "nested name specifier.")
