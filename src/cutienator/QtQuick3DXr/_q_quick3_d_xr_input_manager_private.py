"""
QQuick3DXrInputManagerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_visionos_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrInputManagerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtQuick3DXr

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QQuaternion, QVector3D
  from . import QQuick3DXrController, QQuick3DXrHandInput
  from . import QQuick3DXrHandModel, QQuick3DXrInputManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QQuick3DXrController = WAIT['QQuick3DXrController']
  QQuick3DXrHandModel = WAIT['QQuick3DXrHandModel']
  QQuick3DXrInputManager = WAIT['QQuick3DXrInputManager']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrInputManagerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DXrInputManagerPrivate: a plain Python object
  standing in front of one C++ QQuick3DXrInputManagerPrivate.

  C++ hands a QQuick3DXrInputManagerPrivate around as a copy, so every C++
  QQuick3DXrInputManagerPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuick3DXrInputManagerPrivate that has a ritual and
  that Python can call so far, 11 names in all: 'q_func', 'teardown',
  'isValid', 'get', 'setPosePositionAndRotation', 'registerController',
  'unregisterController', 'isPoseInUse', 'leftHandInput', 'rightHandInput',
  'setupHandModel'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuick3DXrInputManager
    *QQuick3DXrInputManagerPrivate::q_func() const': takes in Python what
    'QQuick3DXrInputManager *QQuick3DXrInputManagerPrivate::q_func()' takes.
  - Qt's 'QQuick3DXrInputManagerPrivate::QQuick3DXrInputManagerPrivate(
    QQuick3DXrInputManager &manager)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQuick3DXrInputManagerPrivate::~QQuick3DXrInputManagerPrivate()':
    the destructor: Python removes its C++ QQuick3DXrInputManagerPrivate by
    it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 19 functions Qt declares: 5 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuick3DXrInputManagerPrivate is created at the first use, not by
    'QQuick3DXrInputManagerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DXrInputManagerPrivate back gives a copy the
    ritual made for Python, in a new cute QQuick3DXrInputManagerPrivate.
  - Each name of Qt's QQuick3DXrInputManagerPrivate that has no cute function
    yet, '__init__', 'getPokeJointIndex', 'initHandtracking',
    'prepareHandtracking', 'processSpatialEvents', 'updateHandtracking',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuick3DXrInputManager)
  @overload(NoneType)
  def get(
      inputManager: Optional[QQuick3DXrInputManager],
  ) -> Optional[QQuick3DXrInputManagerPrivate]:
    """
    Calls Qt's 'QQuick3DXrInputManagerPrivate
    *QQuick3DXrInputManagerPrivate::get(QQuick3DXrInputManager
    *inputManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#get

    Parameters
    ----------

    inputManager : Optional[QQuick3DXrInputManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DXrInputManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrInputManagerPrivate
    #      *QQuick3DXrInputManagerPrivate::get(QQuick3DXrInputManager
    #      *inputManager)
    address = Rituals.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate3getEP22QQuick3DXrInputMan'
        'ager',
        CuteMixin._addressOf(inputManager),
    )
    return QQuick3DXrInputManagerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrInputManagerPrivate'

  #  Qt's '~QQuick3DXrInputManagerPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QQuick3DXrInputManagerPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QQuick3DXrInputManagerPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrInputManagerPrivate::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#isValid
    """
    #  bool QQuick3DXrInputManagerPrivate::isValid() const
    return self.uglySide.call(
        'ritual_ZNK29QQuick3DXrInputManagerPrivate7isValidEv',
    )

  def leftHandInput(self) -> Optional[QQuick3DXrHandInput]:
    """
    Calls Qt's 'QQuick3DXrHandInput
    *QQuick3DXrInputManagerPrivate::leftHandInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#leftHandInput

    Returns
    -------

    Optional[QQuick3DXrHandInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrHandInput *QQuick3DXrInputManagerPrivate::leftHandInput()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DXrInputManagerPrivate13leftHandInputEv',
    )
    from . import QQuick3DXrHandInput
    return QQuick3DXrHandInput._cuteAt(address)

  def rightHandInput(self) -> Optional[QQuick3DXrHandInput]:
    """
    Calls Qt's 'QQuick3DXrHandInput
    *QQuick3DXrInputManagerPrivate::rightHandInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#rightHandInput

    Returns
    -------

    Optional[QQuick3DXrHandInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrHandInput *QQuick3DXrInputManagerPrivate::rightHandInput()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DXrInputManagerPrivate14rightHandInputEv',
    )
    from . import QQuick3DXrHandInput
    return QQuick3DXrHandInput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      QtQuick3DXr.Handedness, QtQuick3DXr.HandPoseSpace, QVector3D,
      QQuaternion,
  )
  def setPosePositionAndRotation(
      self,
      handedness: QtQuick3DXr.Handedness,
      poseSpace: QtQuick3DXr.HandPoseSpace,
      position: QVector3D,
      rotation: QQuaternion,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrInputManagerPrivate::setPosePositionAndRotation(Handedness
    handedness, HandPoseSpace poseSpace, const QVector3D &position, const
    QQuaternion &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html

    Parameters
    ----------

    handedness : QtQuick3DXr.Handedness
      Passed on as its number.

    poseSpace : QtQuick3DXr.HandPoseSpace
      Passed on as its number.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QQuick3DXrInputManagerPrivate::setPosePositionAndRotation(
    #      Handedness handedness, HandPoseSpace poseSpace, const QVector3D
    #      &position, const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate26setPosePositionAndRotati'
        'onEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceERK9QVector3DRK11'
        'QQuaternion',
        handedness.value, poseSpace.value, self._valueOf(position),
        self._valueOf(rotation),
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
    Qt's 'QQuick3DXrInputManagerPrivate::QQuick3DXrInputManagerPrivate(
    QQuick3DXrInputManager &manager)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManagerPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QQuick3DXrInputManagerPrivate::QQuick3DXrInputManagerPrivate(QQuic"
        "k3DXrInputManager &manager)': takes a type Python has no way to "
        "hand over yet.")

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

  def q_func(self) -> Optional[QQuick3DXrInputManager]:
    """
    Calls Qt's 'QQuick3DXrInputManager
    *QQuick3DXrInputManagerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#q_func

    Returns
    -------

    Optional[QQuick3DXrInputManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrInputManager *QQuick3DXrInputManagerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate6q_funcEv',
    )
    from . import QQuick3DXrInputManager
    return QQuick3DXrInputManager._cuteAt(address)

  def teardown(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrInputManagerPrivate::teardown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#teardown
    """
    #  void QQuick3DXrInputManagerPrivate::teardown()
    self.uglySide.call('ritual_ZN29QQuick3DXrInputManagerPrivate8teardownEv')

  @overload(QQuick3DXrController)
  @overload(NoneType)
  def registerController(
      self,
      controller: Optional[QQuick3DXrController],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrInputManagerPrivate::registerController(QQuick3DXrController
    *controller)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html

    Parameters
    ----------

    controller : Optional[QQuick3DXrController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrInputManagerPrivate::registerController(
    #      QQuick3DXrController *controller)
    self.uglySide.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate18registerControllerEP20QQ'
        'uick3DXrController',
        self._addressOf(controller),
    )

  @overload(QQuick3DXrController)
  @overload(NoneType)
  def unregisterController(
      self,
      controller: Optional[QQuick3DXrController],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrInputManagerPrivate::unregisterController(QQuick3DXrController
    *controller)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html

    Parameters
    ----------

    controller : Optional[QQuick3DXrController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrInputManagerPrivate::unregisterController(
    #      QQuick3DXrController *controller)
    self.uglySide.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate20unregisterControllerEP20'
        'QQuick3DXrController',
        self._addressOf(controller),
    )

  @overload(QtQuick3DXr.Handedness, QtQuick3DXr.HandPoseSpace)
  def isPoseInUse(
      self,
      handedness: QtQuick3DXr.Handedness,
      poseSpace: QtQuick3DXr.HandPoseSpace,
  ) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrInputManagerPrivate::isPoseInUse(Handedness
    handedness, HandPoseSpace poseSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#isPoseInUse

    Parameters
    ----------

    handedness : QtQuick3DXr.Handedness
      Passed on as its number.

    poseSpace : QtQuick3DXr.HandPoseSpace
      Passed on as its number.
    """
    #  bool QQuick3DXrInputManagerPrivate::isPoseInUse(Handedness handedness,
    #      HandPoseSpace poseSpace)
    return self.uglySide.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate11isPoseInUseEN11QtQuick3D'
        'Xr10HandednessENS0_13HandPoseSpaceE',
        handedness.value, poseSpace.value,
    )

  @overload(QQuick3DXrHandModel)
  @overload(NoneType)
  def setupHandModel(self, model: Optional[QQuick3DXrHandModel]) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrInputManagerPrivate::setupHandModel(QQuick3DXrHandModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanagerprivate.html#setupHandModel

    Parameters
    ----------

    model : Optional[QQuick3DXrHandModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrInputManagerPrivate::setupHandModel(QQuick3DXrHandModel
    #      *model)
    self.uglySide.call(
        'ritual_ZN29QQuick3DXrInputManagerPrivate14setupHandModelEP19QQuick'
        '3DXrHandModel',
        self._addressOf(model),
    )

  @staticmethod
  def getPokeJointIndex(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DXrInputManagerPrivate::getPokeJointIndex()
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManagerPrivate.getPokeJointIndex' has no cute "
        "function yet. Qt's 'qsizetype "
        "QQuick3DXrInputManagerPrivate::getPokeJointIndex() const': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def initHandtracking(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputManagerPrivate::initHandtracking()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManagerPrivate.initHandtracking' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrInputManagerPrivate::initHandtracking()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def prepareHandtracking(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrInputManagerPrivate::prepareHandtracking(ar_data_providers_t
    dataProviders)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManagerPrivate.prepareHandtracking' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrInputManagerPrivate::prepareHandtracking(ar_data_provider"
        "s_t dataProviders)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def processSpatialEvents(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputManagerPrivate::processSpatialEvents(const
    QQuick3DViewport &vrViewport, const QJsonObject &events)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManagerPrivate.processSpatialEvents' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrInputManagerPrivate::processSpatialEvents(const "
        "QQuick3DViewport &vrViewport, const QJsonObject &events)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def updateHandtracking(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrInputManagerPrivate::updateHandtracking()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManagerPrivate.updateHandtracking' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrInputManagerPrivate::updateHandtracking()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
