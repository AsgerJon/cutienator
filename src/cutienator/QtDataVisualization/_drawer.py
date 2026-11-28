"""
Drawer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/drawer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Drawer to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject
from ..QtGui import QOpenGLFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from . import AbstractObjectHelper, Q3DTheme, ShaderHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractObjectHelper = WAIT['AbstractObjectHelper']
  ShaderHelper = WAIT['ShaderHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Drawer(QObject, QOpenGLFunctions):
  """
  The cute side of Qt's Drawer: a plain Python object standing in front of
  one C++ Drawer.

  It is built on the cute 'QObject', as Qt's Drawer is built on Qt's QObject,
  and has everything that class has. It is built on the cute
  'QOpenGLFunctions' as well, as Qt's Drawer is built on Qt's
  QOpenGLFunctions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Drawer that has a ritual and that Python can call so
  far, 8 names in all: 'metaObject', 'theme', 'font', 'scaledFontSize',
  'drawSelectionObject', 'drawPoint', 'drawLine', 'drawerChanged'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Drawer::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Drawer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'Drawer::~Drawer()': the destructor: Python never removes a C++
    Drawer.

  What has no ritual
  ------------------

  12 of the 23 functions Qt declares: 4 leans on 'ShaderHelper; 3 leans on
  'Drawer; 3 leans on 'TextureHelper; 2 not a gap.

  What to expect
  --------------

  - The C++ Drawer is created at the first use, not by 'Drawer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Drawer.
  - Qt tells when it has removed the C++ Drawer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's Drawer that has no cute function yet, '__init__',
    'drawLabel', 'drawObject', 'drawPoints', 'drawSurfaceGrid',
    'generateLabelItem', 'generateSelectionLabelTexture', 'initializeOpenGL',
    'setTheme', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside Drawer, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class LabelPosition(CuteNum):
    """
    The enum 'Drawer::LabelPosition' of Qt, with the 9 names Qt gives in it.
    """

    LabelBelow = Kee[int](0)
    LabelLow = Kee[int](1)
    LabelMid = Kee[int](2)
    LabelHigh = Kee[int](3)
    LabelOver = Kee[int](4)
    LabelBottom = Kee[int](5)
    LabelTop = Kee[int](6)
    LabelLeft = Kee[int](7)
    LabelRight = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Drawer'

  #  Qt's Drawer is built on more than one class. The part of a C++ Drawer
  #  that belongs to a class after the first begins somewhere inside the
  #  object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QOpenGLFunctions': 'ritual_cast_Drawer_QOpenGLFunctions',
  }

  #  A C++ Drawer Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Drawer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Drawer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Drawer::metaObject() const
    address = self.uglySide.call('ritual_ZNK6Drawer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def theme(self) -> Optional[Q3DTheme]:
    """
    Calls Qt's 'Q3DTheme *Drawer::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#theme

    Returns
    -------

    Optional[Q3DTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DTheme *Drawer::theme() const
    address = self.uglySide.call('ritual_ZNK6Drawer5themeEv')
    from . import Q3DTheme
    return Q3DTheme._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont Drawer::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont Drawer::font() const
    address = self.uglySide.call('ritual_ZNK6Drawer4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def scaledFontSize(self) -> float:
    """
    Calls Qt's 'GLfloat Drawer::scaledFontSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#scaledFontSize
    """
    #  GLfloat Drawer::scaledFontSize() const
    return self.uglySide.call('ritual_ZNK6Drawer14scaledFontSizeEv')

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
    Qt's 'Drawer::Drawer(Q3DTheme *theme)': leans on
    'Drawer::qt_metacall(QMetaObject::Call, int, void**)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Drawer.__init__' has no cute function yet. Qt's "
        "'Drawer::Drawer(Q3DTheme *theme)': leans on "
        "'Drawer::qt_metacall(QMetaObject::Call, int, void**)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(ShaderHelper, AbstractObjectHelper)
  @overload(ShaderHelper, NoneType)
  @overload(NoneType, AbstractObjectHelper)
  @overload(NoneType, NoneType)
  def drawSelectionObject(
      self,
      shader: Optional[ShaderHelper],
      object: Optional[AbstractObjectHelper],
  ) -> None:
    """
    Calls Qt's 'void Drawer::drawSelectionObject(ShaderHelper *shader,
    AbstractObjectHelper *object)'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#drawSelectionObject

    Parameters
    ----------

    shader : Optional[ShaderHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[AbstractObjectHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Drawer::drawSelectionObject(ShaderHelper *shader,
    #      AbstractObjectHelper *object)
    self.uglySide.call(
        'ritual_ZN6Drawer19drawSelectionObjectEP12ShaderHelperP20AbstractOb'
        'jectHelper',
        self._addressOf(shader), self._addressOf(object),
    )

  @overload(ShaderHelper)
  @overload(NoneType)
  def drawPoint(self, shader: Optional[ShaderHelper]) -> None:
    """
    Calls Qt's 'void Drawer::drawPoint(ShaderHelper *shader)'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#drawPoint

    Parameters
    ----------

    shader : Optional[ShaderHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Drawer::drawPoint(ShaderHelper *shader)
    self.uglySide.call(
        'ritual_ZN6Drawer9drawPointEP12ShaderHelper',
        self._addressOf(shader),
    )

  @overload(ShaderHelper)
  @overload(NoneType)
  def drawLine(self, shader: Optional[ShaderHelper]) -> None:
    """
    Calls Qt's 'void Drawer::drawLine(ShaderHelper *shader)'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#drawLine

    Parameters
    ----------

    shader : Optional[ShaderHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Drawer::drawLine(ShaderHelper *shader)
    self.uglySide.call(
        'ritual_ZN6Drawer8drawLineEP12ShaderHelper', self._addressOf(shader),
    )

  def drawerChanged(self) -> None:
    """
    Calls Qt's 'void Drawer::drawerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/drawer.html#drawerChanged
    """
    #  void Drawer::drawerChanged()
    self.uglySide.call('ritual_ZN6Drawer13drawerChangedEv')

  @staticmethod
  def drawLabel(*__, **_) -> Never:
    """
    Qt's 'void Drawer::drawLabel(const AbstractRenderItem &item, const
    LabelItem &labelItem, const QMatrix4x4 &viewmatrix, const QMatrix4x4
    &projectionmatrix, const QVector3D &positionComp, const QQuaternion
    &rotation, GLfloat itemHeight, QAbstract3DGraph::SelectionFlags mode,
    ShaderHelper *shader, ObjectHelper *object, const Q3DCamera *camera, bool
    useDepth, bool rotateAlong, LabelPosition position, Qt::Alignment
    alignment, bool isSlicing, bool isSelecting)': leans on
    'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Drawer.drawLabel' has no cute function yet. Qt's 'void "
        "Drawer::drawLabel(const AbstractRenderItem &item, const LabelItem "
        "&labelItem, const QMatrix4x4 &viewmatrix, const QMatrix4x4 "
        "&projectionmatrix, const QVector3D &positionComp, const "
        "QQuaternion &rotation, GLfloat itemHeight, "
        "QAbstract3DGraph::SelectionFlags mode, ShaderHelper *shader, "
        "ObjectHelper *object, const Q3DCamera *camera, bool useDepth, bool "
        "rotateAlong, LabelPosition position, Qt::Alignment alignment, bool "
        "isSlicing, bool isSelecting)': leans on "
        "'ShaderHelper::setUniformValue(int, QMatrix4x4 const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def drawObject(*__, **_) -> Never:
    """
    Qt's 'void Drawer::drawObject(ShaderHelper *shader, AbstractObjectHelper
    *object, GLuint textureId, GLuint depthTextureId, GLuint textureId3D)':
    leans on 'ShaderHelper::setUniformValue(int, int)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Drawer.drawObject' has no cute function yet. Qt's 'void "
        "Drawer::drawObject(ShaderHelper *shader, AbstractObjectHelper "
        "*object, GLuint textureId, GLuint depthTextureId, GLuint "
        "textureId3D)': leans on 'ShaderHelper::setUniformValue(int, int)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def drawPoints(*__, **_) -> Never:
    """
    Qt's 'void Drawer::drawPoints(ShaderHelper *shader,
    ScatterPointBufferHelper *object, GLuint textureId)': leans on
    'ShaderHelper::setUniformValue(int, int)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Drawer.drawPoints' has no cute function yet. Qt's 'void "
        "Drawer::drawPoints(ShaderHelper *shader, ScatterPointBufferHelper "
        "*object, GLuint textureId)': leans on "
        "'ShaderHelper::setUniformValue(int, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def drawSurfaceGrid(*__, **_) -> Never:
    """
    Qt's 'void Drawer::drawSurfaceGrid(ShaderHelper *shader, SurfaceObject
    *object)': leans on 'ShaderHelper::setUniformValue(int, QVector4D
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Drawer.drawSurfaceGrid' has no cute function yet. Qt's 'void "
        "Drawer::drawSurfaceGrid(ShaderHelper *shader, SurfaceObject "
        "*object)': leans on 'ShaderHelper::setUniformValue(int, QVector4D "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def generateLabelItem(*__, **_) -> Never:
    """
    Qt's 'void Drawer::generateLabelItem(LabelItem &item, const QString
    &text, int widestLabel)': leans on 'TextureHelper::TextureHelper()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Drawer.generateLabelItem' has no cute function yet. Qt's 'void "
        "Drawer::generateLabelItem(LabelItem &item, const QString &text, "
        "int widestLabel)': leans on 'TextureHelper::TextureHelper()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def generateSelectionLabelTexture(*__, **_) -> Never:
    """
    Qt's 'void Drawer::generateSelectionLabelTexture(Abstract3DRenderer
    *item)': leans on 'TextureHelper::TextureHelper()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Drawer.generateSelectionLabelTexture' has no cute function yet. "
        "Qt's 'void "
        "Drawer::generateSelectionLabelTexture(Abstract3DRenderer *item)': "
        "leans on 'TextureHelper::TextureHelper()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def initializeOpenGL(*__, **_) -> Never:
    """
    Qt's 'void Drawer::initializeOpenGL()': leans on
    'TextureHelper::TextureHelper()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Drawer.initializeOpenGL' has no cute function yet. Qt's 'void "
        "Drawer::initializeOpenGL()': leans on "
        "'TextureHelper::TextureHelper()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setTheme(*__, **_) -> Never:
    """
    Qt's 'void Drawer::setTheme(Q3DTheme *theme)': leans on
    'Drawer::drawerChanged()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Drawer.setTheme' has no cute function yet. Qt's 'void "
        "Drawer::setTheme(Q3DTheme *theme)': leans on "
        "'Drawer::drawerChanged()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")
