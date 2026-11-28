"""
SelectionPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/selectionpointer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SelectionPointer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..QtGui import QOpenGLFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect
  from ..QtGui import QQuaternion, QVector3D, QVector4D
  from . import ObjectHelper, Q3DScene
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ObjectHelper = WAIT['ObjectHelper']
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QQuaternion = WAIT['QQuaternion']
  QRect = WAIT['QRect']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SelectionPointer(QObject, QOpenGLFunctions):
  """
  The cute side of Qt's SelectionPointer: a plain Python object standing in
  front of one C++ SelectionPointer.

  It is built on the cute 'QObject', as Qt's SelectionPointer is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QOpenGLFunctions' as well, as Qt's SelectionPointer is built on Qt's
  QOpenGLFunctions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's SelectionPointer that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'setPosition',
  'setPointerObject', 'setLabelObject', 'updateBoundingRect', 'updateScene',
  'updateSliceData', 'setHighlightColor', 'setRotation'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *SelectionPointer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int SelectionPointer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'SelectionPointer::~SelectionPointer()': the destructor: Python
    never removes a C++ SelectionPointer.

  What has no ritual
  ------------------

  10 of the 22 functions Qt declares: 3 leans on 'TextureHelper; 2 not a gap;
  2 leans on 'SelectionPointer; 1 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file; 1 leans on
  'ShaderHelper; 1 leans on 'Utils.

  What to expect
  --------------

  - The C++ SelectionPointer is created at the first use, not by
    'SelectionPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SelectionPointer.
  - Qt tells when it has removed the C++ SelectionPointer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's SelectionPointer that has no cute function yet,
    '__init__', 'handleDrawerChange', 'initShaders', 'initializeOpenGL',
    'renderSelectionLabel', 'renderSelectionPointer', 'setLabel', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SelectionPointer'

  #  Qt's SelectionPointer is built on more than one class. The part of a C++
  #  SelectionPointer that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QOpenGLFunctions': 'ritual_cast_SelectionPointer_QOpenGLFunctions',
  }

  #  A C++ SelectionPointer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SelectionPointer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *SelectionPointer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/selectionpointer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *SelectionPointer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16SelectionPointer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void SelectionPointer::setPosition(const QVector3D
    &position)'.

    Qt's own words: https://doc.qt.io/qt-6/selectionpointer.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void SelectionPointer::setPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer11setPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(ObjectHelper)
  @overload(NoneType)
  def setPointerObject(self, object: Optional[ObjectHelper]) -> None:
    """
    Calls Qt's 'void SelectionPointer::setPointerObject(ObjectHelper
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/selectionpointer.html#setPointerObject

    Parameters
    ----------

    object : Optional[ObjectHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SelectionPointer::setPointerObject(ObjectHelper *object)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer16setPointerObjectEP12ObjectHelper',
        self._addressOf(object),
    )

  @overload(ObjectHelper)
  @overload(NoneType)
  def setLabelObject(self, object: Optional[ObjectHelper]) -> None:
    """
    Calls Qt's 'void SelectionPointer::setLabelObject(ObjectHelper *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/selectionpointer.html#setLabelObject

    Parameters
    ----------

    object : Optional[ObjectHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SelectionPointer::setLabelObject(ObjectHelper *object)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer14setLabelObjectEP12ObjectHelper',
        self._addressOf(object),
    )

  @overload(QVector4D)
  def setHighlightColor(self, colorVector: QVector4D) -> None:
    """
    Calls Qt's 'void SelectionPointer::setHighlightColor(const QVector4D
    &colorVector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/selectionpointer.html#setHighlightColor

    Parameters
    ----------

    colorVector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void SelectionPointer::setHighlightColor(const QVector4D &colorVector)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer17setHighlightColorERK9QVector4D',
        self._valueOf(colorVector),
    )

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void SelectionPointer::setRotation(const QQuaternion
    &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/selectionpointer.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void SelectionPointer::setRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer11setRotationERK11QQuaternion',
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
    Qt's 'SelectionPointer::SelectionPointer(Drawer *drawer)': leans on
    'SelectionPointer::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'SelectionPointer.__init__' has no cute function yet. Qt's "
        "'SelectionPointer::SelectionPointer(Drawer *drawer)': leans on "
        "'SelectionPointer::qt_metacall(QMetaObject::Call, int, void**)', "
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

  @overload(QRect)
  def updateBoundingRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void SelectionPointer::updateBoundingRect(const QRect
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/selectionpointer.html#updateBoundingRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void SelectionPointer::updateBoundingRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer18updateBoundingRectERK5QRect',
        self._valueOf(rect),
    )

  @overload(Q3DScene)
  @overload(NoneType)
  def updateScene(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void SelectionPointer::updateScene(Q3DScene *scene)'.

    Qt's own words: https://doc.qt.io/qt-6/selectionpointer.html#updateScene

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SelectionPointer::updateScene(Q3DScene *scene)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer11updateSceneEP8Q3DScene',
        self._addressOf(scene),
    )

  @overload(bool, float)
  def updateSliceData(
      self,
      sliceActivated: bool,
      autoScaleAdjustment: float,
  ) -> None:
    """
    Calls Qt's 'void SelectionPointer::updateSliceData(bool sliceActivated,
    GLfloat autoScaleAdjustment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/selectionpointer.html#updateSliceData

    Parameters
    ----------

    sliceActivated : bool
      Passed on as it is.

    autoScaleAdjustment : float
      Passed on as it is.
    """
    #  void SelectionPointer::updateSliceData(bool sliceActivated, GLfloat
    #      autoScaleAdjustment)
    self.uglySide.call(
        'ritual_ZN16SelectionPointer15updateSliceDataEbf',
        sliceActivated, autoScaleAdjustment,
    )

  @staticmethod
  def handleDrawerChange(*__, **_) -> Never:
    """
    Qt's 'void SelectionPointer::handleDrawerChange()': leans on
    'TextureHelper::TextureHelper()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SelectionPointer.handleDrawerChange' has no cute function yet. "
        "Qt's 'void SelectionPointer::handleDrawerChange()': leans on "
        "'TextureHelper::TextureHelper()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def initShaders(*__, **_) -> Never:
    """
    Qt's 'void SelectionPointer::initShaders()': leans on
    'Utils::isOpenGLES()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SelectionPointer.initShaders' has no cute function yet. Qt's "
        "'void SelectionPointer::initShaders()': leans on "
        "'Utils::isOpenGLES()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def initializeOpenGL(*__, **_) -> Never:
    """
    Qt's 'void SelectionPointer::initializeOpenGL()': leans on
    'TextureHelper::TextureHelper()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SelectionPointer.initializeOpenGL' has no cute function yet. Qt's "
        "'void SelectionPointer::initializeOpenGL()': leans on "
        "'TextureHelper::TextureHelper()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def renderSelectionLabel(*__, **_) -> Never:
    """
    Qt's 'void SelectionPointer::renderSelectionLabel(GLuint
    defaultFboHandle, bool useOrtho)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'spSliceUnits'.
    """
    raise NotImplementedError(
        "'SelectionPointer.renderSelectionLabel' has no cute function yet. "
        "Qt's 'void SelectionPointer::renderSelectionLabel(GLuint "
        "defaultFboHandle, bool useOrtho)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'spSliceUnits'.")

  @staticmethod
  def renderSelectionPointer(*__, **_) -> Never:
    """
    Qt's 'void SelectionPointer::renderSelectionPointer(GLuint
    defaultFboHandle, bool useOrtho)': leans on
    'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'SelectionPointer.renderSelectionPointer' has no cute function "
        "yet. Qt's 'void SelectionPointer::renderSelectionPointer(GLuint "
        "defaultFboHandle, bool useOrtho)': leans on "
        "'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setLabel(*__, **_) -> Never:
    """
    Qt's 'void SelectionPointer::setLabel(const QString &label, bool
    themeChange)': leans on 'TextureHelper::TextureHelper()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'SelectionPointer.setLabel' has no cute function yet. Qt's 'void "
        "SelectionPointer::setLabel(const QString &label, bool "
        "themeChange)': leans on 'TextureHelper::TextureHelper()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
