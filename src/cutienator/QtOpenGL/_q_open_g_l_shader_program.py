"""
QOpenGLShaderProgram binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglshaderprogram.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QOpenGLShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QPoint, QPointF, QSize
  from ..QtCore import QSizeF
  from ..QtGui import QColor, QMatrix4x4, QOpenGLContext, QTransform
  from ..QtGui import QVector2D, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QOpenGLContext = WAIT['QOpenGLContext']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']
  QTransform = WAIT['QTransform']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLShaderProgram(QObject):
  """
  The cute side of Qt's QOpenGLShaderProgram: a plain Python object standing
  in front of one C++ QOpenGLShaderProgram.

  It is built on the cute 'QObject', as Qt's QOpenGLShaderProgram is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLShaderProgram that has a ritual and that
  Python can call so far, 33 names in all: 'metaObject', 'tr', 'addShader',
  'removeShader', 'shaders', 'addShaderFromSourceCode',
  'addShaderFromSourceFile', 'addCacheableShaderFromSourceCode',
  'addCacheableShaderFromSourceFile', 'removeAllShaders', 'link', 'isLinked',
  'log', 'bind', 'release', 'create', 'programId',
  'maxGeometryOutputVertices', 'setPatchVertexCount', 'patchVertexCount',
  'bindAttributeLocation', 'attributeLocation', 'setAttributeValue',
  'setAttributeArray', 'setAttributeBuffer', 'enableAttributeArray',
  'disableAttributeArray', 'uniformLocation', 'setUniformValue',
  'setUniformValueArray', 'hasOpenGLShaderPrograms', 'shaderDestroyed',
  'init'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLShaderProgram::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QOpenGLShaderProgram::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLShaderProgram::~QOpenGLShaderProgram()': the destructor:
    Python never removes a C++ QOpenGLShaderProgram.
  - Qt's 'bool
    QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderType
    type, const QString &source)': takes in Python what 'bool
    QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderType
    type, const char *source)' takes.
  - Qt's 'bool
    QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader::
    ShaderType type, const QString &source)': takes in Python what 'bool
    QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader::
    ShaderType type, const char *source)' takes.
  - Qt's 'void QOpenGLShaderProgram::setDefaultOuterTessellationLevels(const
    QList<float> &levels)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<float> QOpenGLShaderProgram::defaultOuterTessellationLevels()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QOpenGLShaderProgram::setDefaultInnerTessellationLevels(const
    QList<float> &levels)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<float> QOpenGLShaderProgram::defaultInnerTessellationLevels()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QOpenGLShaderProgram::bindAttributeLocation(const QString
    &name, int location)': takes in Python what 'void
    QOpenGLShaderProgram::bindAttributeLocation(const char *name, int
    location)' takes.
  - Qt's 'int QOpenGLShaderProgram::attributeLocation(const QString &name)
    const': takes in Python what 'int
    QOpenGLShaderProgram::attributeLocation(const char *name) const' takes.
  - Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location, const
    GLfloat *values, int columns, int rows)': names 'GLfloat', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char *name,
    const GLfloat *values, int columns, int rows)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setAttributeArray(int location, const
    GLfloat *values, int tupleSize, int stride)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setAttributeArray(int location, GLenum
    type, const void *values, int tupleSize, int stride)': names 'void',
    which has no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setAttributeArray(const char *name,
    const GLfloat *values, int tupleSize, int stride)': names 'GLfloat',
    which has no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setAttributeArray(const char *name,
    GLenum type, const void *values, int tupleSize, int stride)': names
    'void', which has no cute class yet.
  - Qt's 'int QOpenGLShaderProgram::uniformLocation(const QString &name)
    const': takes in Python what 'int
    QOpenGLShaderProgram::uniformLocation(const char *name) const' takes.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, GLuint
    value)': takes in Python what 'void
    QOpenGLShaderProgram::setUniformValue(int location, GLint value)' takes.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix2x2 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix2x3 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix2x4 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix3x2 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix3x3 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix3x4 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix4x2 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(int location, const
    QMatrix4x3 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, GLuint
    value)': takes in Python what 'void
    QOpenGLShaderProgram::setUniformValue(const char *name, GLint value)'
    takes.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix2x2 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix2x3 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix2x4 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix3x2 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix3x3 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix3x4 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix4x2 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name, const
    QMatrix4x3 &value)': takes a type Python has no way to hand over yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    GLfloat *values, int count, int tupleSize)': names 'GLfloat', which has
    no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    GLint *values, int count)': names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    GLuint *values, int count)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix2x2 *values, int count)': names 'QMatrix2x2', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix2x3 *values, int count)': names 'QMatrix2x3', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix2x4 *values, int count)': names 'QMatrix2x4', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix3x2 *values, int count)': names 'QMatrix3x2', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix3x3 *values, int count)': names 'QMatrix3x3', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix3x4 *values, int count)': names 'QMatrix3x4', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix4x2 *values, int count)': names 'QMatrix4x2', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location, const
    QMatrix4x3 *values, int count)': names 'QMatrix4x3', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const GLfloat *values, int count, int tupleSize)': names 'GLfloat', which
    has no cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const GLint *values, int count)': names 'GLint', which has no cute class
    yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const GLuint *values, int count)': names 'GLuint', which has no cute
    class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix2x2 *values, int count)': names 'QMatrix2x2', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix2x3 *values, int count)': names 'QMatrix2x3', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix2x4 *values, int count)': names 'QMatrix2x4', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix3x2 *values, int count)': names 'QMatrix3x2', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix3x3 *values, int count)': names 'QMatrix3x3', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix3x4 *values, int count)': names 'QMatrix3x4', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix4x2 *values, int count)': names 'QMatrix4x2', which has no
    cute class yet.
  - Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    const QMatrix4x3 *values, int count)': names 'QMatrix4x3', which has no
    cute class yet.
  - Qt's 'QOpenGLShaderProgramPrivate *QOpenGLShaderProgram::d_func()': gives
    'QOpenGLShaderProgramPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLShaderProgramPrivate *QOpenGLShaderProgram::d_func()
    const': gives 'QOpenGLShaderProgramPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  10 of the 168 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLShaderProgram is created at the first use, not by
    'QOpenGLShaderProgram(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLShaderProgram.
  - Qt tells when it has removed the C++ QOpenGLShaderProgram. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpenGLShaderProgram that has no cute function yet,
    'defaultInnerTessellationLevels', 'defaultOuterTessellationLevels',
    'setDefaultInnerTessellationLevels', 'setDefaultOuterTessellationLevels',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QOpenGLShaderProgram::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#tr

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
    #  QString QOpenGLShaderProgram::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QOpenGLShaderProgram2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload()
  @overload(QOpenGLContext)
  @overload(NoneType)
  def hasOpenGLShaderPrograms(
      context: Optional[QOpenGLContext] = None,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::hasOpenGLShaderPrograms(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#hasOpenGLShaderPrograms

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QOpenGLShaderProgram::hasOpenGLShaderPrograms(QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN20QOpenGLShaderProgram23hasOpenGLShaderProgramsEP14QOpenG'
        'LContext',
        CuteMixin._addressOf(context),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLShaderProgram'

  #  A C++ QOpenGLShaderProgram Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLShaderProgram'

  #  The functions Qt calls itself that QOpenGLShaderProgram is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'link': (
          ('_ZN20QOpenGLShaderProgram4linkEv',
           ('bool', 'number', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QOpenGLShaderProgram::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLShaderProgram::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shaders(self) -> QList[QOpenGLShader]:
    """
    Calls Qt's 'QList<QOpenGLShader *> QOpenGLShaderProgram::shaders()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#shaders

    Returns
    -------

    QList[QOpenGLShader]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpenGLShader *> QOpenGLShaderProgram::shaders() const
    address = self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram7shadersEv',
    )
    return QList[QOpenGLShader]._cuteOwning(address)

  def isLinked(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLShaderProgram::isLinked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#isLinked
    """
    #  bool QOpenGLShaderProgram::isLinked() const
    return self.uglySide.call('ritual_ZNK20QOpenGLShaderProgram8isLinkedEv')

  def log(self) -> str:
    """
    Calls Qt's 'QString QOpenGLShaderProgram::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpenGLShaderProgram::log() const
    return self.uglySide.call('ritual_ZNK20QOpenGLShaderProgram3logEv')

  def programId(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLShaderProgram::programId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#programId
    """
    #  GLuint QOpenGLShaderProgram::programId() const
    return self.uglySide.call('ritual_ZNK20QOpenGLShaderProgram9programIdEv')

  def maxGeometryOutputVertices(self) -> int:
    """
    Calls Qt's 'int QOpenGLShaderProgram::maxGeometryOutputVertices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html
    """
    #  int QOpenGLShaderProgram::maxGeometryOutputVertices() const
    return self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram25maxGeometryOutputVerticesEv',
    )

  def patchVertexCount(self) -> int:
    """
    Calls Qt's 'int QOpenGLShaderProgram::patchVertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#patchVertexCount
    """
    #  int QOpenGLShaderProgram::patchVertexCount() const
    return self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram16patchVertexCountEv',
    )

  @overload(str)
  @overload(NoneType)
  def attributeLocation(self, name: Optional[str]) -> int:
    """
    Calls Qt's 'int QOpenGLShaderProgram::attributeLocation(const char *name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QOpenGLShaderProgram::attributeLocation(const char *name) const
    return self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram17attributeLocationEPKc',
        self._bytesOf(name),
    )

  @overload(QByteArray)
  def attributeLocation(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QOpenGLShaderProgram::attributeLocation(const QByteArray
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#attributeLocation

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QOpenGLShaderProgram::attributeLocation(const QByteArray &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram17attributeLocationERK10QByteArray',
        self._valueOf(name),
    )

  @overload(str)
  @overload(NoneType)
  def uniformLocation(self, name: Optional[str]) -> int:
    """
    Calls Qt's 'int QOpenGLShaderProgram::uniformLocation(const char *name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QOpenGLShaderProgram::uniformLocation(const char *name) const
    return self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram15uniformLocationEPKc',
        self._bytesOf(name),
    )

  @overload(QByteArray)
  def uniformLocation(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QOpenGLShaderProgram::uniformLocation(const QByteArray
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#uniformLocation

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QOpenGLShaderProgram::uniformLocation(const QByteArray &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QOpenGLShaderProgram15uniformLocationERK10QByteArray',
        self._valueOf(name),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPatchVertexCount(self, count: int) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setPatchVertexCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setPatchVertexCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setPatchVertexCount(int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram19setPatchVertexCountEi', count,
    )

  @overload(int, float)
  def setAttributeValue(self, location: int, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    GLfloat value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat
    #      value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEif',
        location, value,
    )

  @overload(int, float, float)
  def setAttributeValue(self, location: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat x,
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiff',
        location, x, y,
    )

  @overload(int, float, float, float)
  def setAttributeValue(
      self,
      location: int,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEifff',
        location, x, y, z,
    )

  @overload(int, float, float, float, float)
  def setAttributeValue(
      self,
      location: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, GLfloat x,
    #      GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiffff',
        location, x, y, z, w,
    )

  @overload(int, QVector2D)
  def setAttributeValue(self, location: int, value: QVector2D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    const QVector2D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, const
    #      QVector2D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK9QVector2D',
        location, self._valueOf(value),
    )

  @overload(int, QVector3D)
  def setAttributeValue(self, location: int, value: QVector3D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    const QVector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, const
    #      QVector3D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK9QVector3D',
        location, self._valueOf(value),
    )

  @overload(int, QVector4D)
  def setAttributeValue(self, location: int, value: QVector4D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    const QVector4D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, const
    #      QVector4D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK9QVector4D',
        location, self._valueOf(value),
    )

  @overload(int, QColor)
  def setAttributeValue(self, location: int, value: QColor) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(int location,
    const QColor &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(int location, const
    #      QColor &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEiRK6QColor',
        location, self._valueOf(value),
    )

  @overload(str, float)
  @overload(NoneType, float)
  def setAttributeValue(self, name: Optional[str], value: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, GLfloat value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat
    #      value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcf',
        self._bytesOf(name), value,
    )

  @overload(str, float, float)
  @overload(NoneType, float, float)
  def setAttributeValue(
      self,
      name: Optional[str],
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat
    #      x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcff',
        self._bytesOf(name), x, y,
    )

  @overload(str, float, float, float)
  @overload(NoneType, float, float, float)
  def setAttributeValue(
      self,
      name: Optional[str],
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat
    #      x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcfff',
        self._bytesOf(name), x, y, z,
    )

  @overload(str, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def setAttributeValue(
      self,
      name: Optional[str],
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, GLfloat
    #      x, GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcffff',
        self._bytesOf(name), x, y, z, w,
    )

  @overload(str, QVector2D)
  @overload(NoneType, QVector2D)
  def setAttributeValue(self, name: Optional[str], value: QVector2D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, const QVector2D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
    #      QVector2D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK9QVector2D',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QVector3D)
  @overload(NoneType, QVector3D)
  def setAttributeValue(self, name: Optional[str], value: QVector3D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, const QVector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
    #      QVector3D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK9QVector3D',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QVector4D)
  @overload(NoneType, QVector4D)
  def setAttributeValue(self, name: Optional[str], value: QVector4D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, const QVector4D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
    #      QVector4D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK9QVector4D',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QColor)
  @overload(NoneType, QColor)
  def setAttributeValue(self, name: Optional[str], value: QColor) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeValue(const char
    *name, const QColor &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setAttributeValue(const char *name, const
    #      QColor &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeValueEPKcRK6QColor',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(int, QVector2D)
  @overload(int, NoneType)
  @overload(int, QVector2D, int)
  @overload(int, NoneType, int)
  def setAttributeArray(
      self,
      location: int,
      values: Optional[QVector2D],
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeArray(int location,
    const QVector2D *values, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QVector2D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeArray(int location, const
    #      QVector2D *values, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPK9QVector2Di',
        location, self._addressOf(values), stride,
    )

  @overload(int, QVector3D)
  @overload(int, QVector3D, int)
  def setAttributeArray(
      self,
      location: int,
      values: Optional[QVector3D],
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeArray(int location,
    const QVector3D *values, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeArray(int location, const
    #      QVector3D *values, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPK9QVector3Di',
        location, self._addressOf(values), stride,
    )

  @overload(int, QVector4D)
  @overload(int, QVector4D, int)
  def setAttributeArray(
      self,
      location: int,
      values: Optional[QVector4D],
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeArray(int location,
    const QVector4D *values, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QVector4D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeArray(int location, const
    #      QVector4D *values, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEiPK9QVector4Di',
        location, self._addressOf(values), stride,
    )

  @overload(str, QVector2D)
  @overload(str, NoneType)
  @overload(NoneType, QVector2D)
  @overload(NoneType, NoneType)
  @overload(str, QVector2D, int)
  @overload(str, NoneType, int)
  @overload(NoneType, QVector2D, int)
  @overload(NoneType, NoneType, int)
  def setAttributeArray(
      self,
      name: Optional[str],
      values: Optional[QVector2D],
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeArray(const char
    *name, const QVector2D *values, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QVector2D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
    #      QVector2D *values, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPK9QVector2D'
        'i',
        self._bytesOf(name), self._addressOf(values), stride,
    )

  @overload(str, QVector3D)
  @overload(NoneType, QVector3D)
  @overload(str, QVector3D, int)
  @overload(NoneType, QVector3D, int)
  def setAttributeArray(
      self,
      name: Optional[str],
      values: Optional[QVector3D],
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeArray(const char
    *name, const QVector3D *values, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
    #      QVector3D *values, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPK9QVector3D'
        'i',
        self._bytesOf(name), self._addressOf(values), stride,
    )

  @overload(str, QVector4D)
  @overload(NoneType, QVector4D)
  @overload(str, QVector4D, int)
  @overload(NoneType, QVector4D, int)
  def setAttributeArray(
      self,
      name: Optional[str],
      values: Optional[QVector4D],
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeArray(const char
    *name, const QVector4D *values, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QVector4D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeArray(const char *name, const
    #      QVector4D *values, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram17setAttributeArrayEPKcPK9QVector4D'
        'i',
        self._bytesOf(name), self._addressOf(values), stride,
    )

  @overload(int, int, int, int)
  @overload(int, int, int, int, int)
  def setAttributeBuffer(
      self,
      location: int,
      type: int,
      offset: int,
      tupleSize: int,
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeBuffer(int location,
    GLenum type, int offset, int tupleSize, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer

    Parameters
    ----------

    location : int
      Passed on as it is.

    type : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    tupleSize : int
      Passed on as it is.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeBuffer(int location, GLenum
    #      type, int offset, int tupleSize, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram18setAttributeBufferEijiii',
        location, type, offset, tupleSize, stride,
    )

  @overload(str, int, int, int)
  @overload(NoneType, int, int, int)
  @overload(str, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  def setAttributeBuffer(
      self,
      name: Optional[str],
      type: int,
      offset: int,
      tupleSize: int,
      stride: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setAttributeBuffer(const char
    *name, GLenum type, int offset, int tupleSize, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setAttributeBuffer

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    tupleSize : int
      Passed on as it is.

    stride : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLShaderProgram::setAttributeBuffer(const char *name, GLenum
    #      type, int offset, int tupleSize, int stride)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram18setAttributeBufferEPKcjiii',
        self._bytesOf(name), type, offset, tupleSize, stride,
    )

  @overload(int, float)
  def setUniformValue(self, location: int, value: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    GLfloat value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat
    #      value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEif',
        location, value,
    )

  @overload(int, int)
  def setUniformValue(self, location: int, value: int) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, GLint value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEii',
        location, value,
    )

  @overload(int, float, float)
  def setUniformValue(self, location: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat x,
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiff',
        location, x, y,
    )

  @overload(int, float, float, float)
  def setUniformValue(
      self,
      location: int,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat x,
    #      GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEifff',
        location, x, y, z,
    )

  @overload(int, float, float, float, float)
  def setUniformValue(
      self,
      location: int,
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, GLfloat x,
    #      GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiffff',
        location, x, y, z, w,
    )

  @overload(int, QVector2D)
  def setUniformValue(self, location: int, value: QVector2D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QVector2D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const
    #      QVector2D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK9QVector2D',
        location, self._valueOf(value),
    )

  @overload(int, QVector3D)
  def setUniformValue(self, location: int, value: QVector3D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QVector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const
    #      QVector3D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK9QVector3D',
        location, self._valueOf(value),
    )

  @overload(int, QVector4D)
  def setUniformValue(self, location: int, value: QVector4D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QVector4D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const
    #      QVector4D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK9QVector4D',
        location, self._valueOf(value),
    )

  @overload(int, QColor)
  def setUniformValue(self, location: int, color: QColor) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK6QColor',
        location, self._valueOf(color),
    )

  @overload(int, QPoint)
  def setUniformValue(self, location: int, point: QPoint) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const QPoint
    #      &point)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK6QPoint',
        location, self._valueOf(point),
    )

  @overload(int, QPointF)
  def setUniformValue(self, location: int, point: QPointF) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QPointF &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const QPointF
    #      &point)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK7QPointF',
        location, self._valueOf(point, 'QPointF'),
    )

  @overload(int, QSize)
  def setUniformValue(self, location: int, size: QSize) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const QSize
    #      &size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK5QSize',
        location, self._valueOf(size),
    )

  @overload(int, QSizeF)
  def setUniformValue(self, location: int, size: QSizeF) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QSizeF &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const QSizeF
    #      &size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK6QSizeF',
        location, self._valueOf(size),
    )

  @overload(int, QMatrix4x4)
  def setUniformValue(self, location: int, value: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QMatrix4x4 &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const
    #      QMatrix4x4 &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK10QMatrix4x4',
        location, self._valueOf(value),
    )

  @overload(int, QTransform)
  def setUniformValue(self, location: int, value: QTransform) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(int location,
    const QTransform &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    location : int
      Passed on as it is.

    value : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(int location, const
    #      QTransform &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEiRK10QTransform',
        location, self._valueOf(value),
    )

  @overload(str, float)
  @overload(NoneType, float)
  def setUniformValue(self, name: Optional[str], value: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    GLfloat value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat
    #      value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcf',
        self._bytesOf(name), value,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def setUniformValue(self, name: Optional[str], value: int) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    GLint value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, GLint
    #      value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKci',
        self._bytesOf(name), value,
    )

  @overload(str, float, float)
  @overload(NoneType, float, float)
  def setUniformValue(self, name: Optional[str], x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    GLfloat x, GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat
    #      x, GLfloat y)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcff',
        self._bytesOf(name), x, y,
    )

  @overload(str, float, float, float)
  @overload(NoneType, float, float, float)
  def setUniformValue(
      self,
      name: Optional[str],
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    GLfloat x, GLfloat y, GLfloat z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat
    #      x, GLfloat y, GLfloat z)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcfff',
        self._bytesOf(name), x, y, z,
    )

  @overload(str, float, float, float, float)
  @overload(NoneType, float, float, float, float)
  def setUniformValue(
      self,
      name: Optional[str],
      x: float,
      y: float,
      z: float,
      w: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    GLfloat x, GLfloat y, GLfloat z, GLfloat w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, GLfloat
    #      x, GLfloat y, GLfloat z, GLfloat w)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcffff',
        self._bytesOf(name), x, y, z, w,
    )

  @overload(str, QVector2D)
  @overload(NoneType, QVector2D)
  def setUniformValue(self, name: Optional[str], value: QVector2D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QVector2D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QVector2D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK9QVector2D',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QVector3D)
  @overload(NoneType, QVector3D)
  def setUniformValue(self, name: Optional[str], value: QVector3D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QVector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QVector3D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK9QVector3D',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QVector4D)
  @overload(NoneType, QVector4D)
  def setUniformValue(self, name: Optional[str], value: QVector4D) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QVector4D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QVector4D &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK9QVector4D',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QColor)
  @overload(NoneType, QColor)
  def setUniformValue(self, name: Optional[str], color: QColor) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QColor &color)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK6QColor',
        self._bytesOf(name), self._valueOf(color),
    )

  @overload(str, QPoint)
  @overload(NoneType, QPoint)
  def setUniformValue(self, name: Optional[str], point: QPoint) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QPoint &point)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK6QPoint',
        self._bytesOf(name), self._valueOf(point),
    )

  @overload(str, QPointF)
  @overload(NoneType, QPointF)
  def setUniformValue(self, name: Optional[str], point: QPointF) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QPointF &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QPointF &point)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK7QPointF',
        self._bytesOf(name), self._valueOf(point, 'QPointF'),
    )

  @overload(str, QSize)
  @overload(NoneType, QSize)
  def setUniformValue(self, name: Optional[str], size: QSize) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QSize &size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK5QSize',
        self._bytesOf(name), self._valueOf(size),
    )

  @overload(str, QSizeF)
  @overload(NoneType, QSizeF)
  def setUniformValue(self, name: Optional[str], size: QSizeF) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QSizeF &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QSizeF &size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK6QSizeF',
        self._bytesOf(name), self._valueOf(size),
    )

  @overload(str, QMatrix4x4)
  @overload(NoneType, QMatrix4x4)
  def setUniformValue(self, name: Optional[str], value: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QMatrix4x4 &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QMatrix4x4 &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK10QMatrix4x4',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(str, QTransform)
  @overload(NoneType, QTransform)
  def setUniformValue(self, name: Optional[str], value: QTransform) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValue(const char *name,
    const QTransform &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValue

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QOpenGLShaderProgram::setUniformValue(const char *name, const
    #      QTransform &value)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram15setUniformValueEPKcRK10QTransform',
        self._bytesOf(name), self._valueOf(value),
    )

  @overload(int, QVector2D, int)
  @overload(int, NoneType, int)
  def setUniformValueArray(
      self,
      location: int,
      values: Optional[QVector2D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location,
    const QVector2D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QVector2D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(int location, const
    #      QVector2D *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK9QVector2'
        'Di',
        location, self._addressOf(values), count,
    )

  @overload(int, QVector3D, int)
  def setUniformValueArray(
      self,
      location: int,
      values: Optional[QVector3D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location,
    const QVector3D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(int location, const
    #      QVector3D *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK9QVector3'
        'Di',
        location, self._addressOf(values), count,
    )

  @overload(int, QVector4D, int)
  def setUniformValueArray(
      self,
      location: int,
      values: Optional[QVector4D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location,
    const QVector4D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QVector4D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(int location, const
    #      QVector4D *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK9QVector4'
        'Di',
        location, self._addressOf(values), count,
    )

  @overload(int, QMatrix4x4, int)
  def setUniformValueArray(
      self,
      location: int,
      values: Optional[QMatrix4x4],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(int location,
    const QMatrix4x4 *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    location : int
      Passed on as it is.

    values : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(int location, const
    #      QMatrix4x4 *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEiPK10QMatrix'
        '4x4i',
        location, self._addressOf(values), count,
    )

  @overload(str, QVector2D, int)
  @overload(str, NoneType, int)
  @overload(NoneType, QVector2D, int)
  @overload(NoneType, NoneType, int)
  def setUniformValueArray(
      self,
      name: Optional[str],
      values: Optional[QVector2D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char
    *name, const QVector2D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QVector2D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    #      const QVector2D *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK9QVecto'
        'r2Di',
        self._bytesOf(name), self._addressOf(values), count,
    )

  @overload(str, QVector3D, int)
  @overload(NoneType, QVector3D, int)
  def setUniformValueArray(
      self,
      name: Optional[str],
      values: Optional[QVector3D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char
    *name, const QVector3D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    #      const QVector3D *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK9QVecto'
        'r3Di',
        self._bytesOf(name), self._addressOf(values), count,
    )

  @overload(str, QVector4D, int)
  @overload(NoneType, QVector4D, int)
  def setUniformValueArray(
      self,
      name: Optional[str],
      values: Optional[QVector4D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char
    *name, const QVector4D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QVector4D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    #      const QVector4D *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK9QVecto'
        'r4Di',
        self._bytesOf(name), self._addressOf(values), count,
    )

  @overload(str, QMatrix4x4, int)
  @overload(NoneType, QMatrix4x4, int)
  def setUniformValueArray(
      self,
      name: Optional[str],
      values: Optional[QMatrix4x4],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::setUniformValueArray(const char
    *name, const QMatrix4x4 *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#setUniformValueArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    values : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::setUniformValueArray(const char *name,
    #      const QMatrix4x4 *values, int count)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20setUniformValueArrayEPKcPK10QMatr'
        'ix4x4i',
        self._bytesOf(name), self._addressOf(values), count,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLShaderProgram::QOpenGLShaderProgram(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#QOpenGLShaderProgram

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLShaderProgram::QOpenGLShaderProgram(QObject *parent)
    self._noteCreation(QOpenGLShaderProgram, lambda: Rituals.call(
        'ritual_ZN20QOpenGLShaderProgramC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QOpenGLShader)
  @overload(NoneType)
  def addShader(self, shader: Optional[QOpenGLShader]) -> bool:
    """
    Calls Qt's 'bool QOpenGLShaderProgram::addShader(QOpenGLShader *shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShader

    Parameters
    ----------

    shader : Optional[QOpenGLShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLShaderProgram::addShader(QOpenGLShader *shader)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram9addShaderEP13QOpenGLShader',
        self._addressOf(shader),
    )

  @overload(QOpenGLShader)
  @overload(NoneType)
  def removeShader(self, shader: Optional[QOpenGLShader]) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::removeShader(QOpenGLShader
    *shader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeShader

    Parameters
    ----------

    shader : Optional[QOpenGLShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLShaderProgram::removeShader(QOpenGLShader *shader)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram12removeShaderEP13QOpenGLShader',
        self._addressOf(shader),
    )

  @overload(QOpenGLShader.ShaderType, str)
  @overload(QOpenGLShader.ShaderType, NoneType)
  def addShaderFromSourceCode(
      self,
      type: QOpenGLShader.ShaderType,
      source: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderType
    type, const char *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode

    Parameters
    ----------

    type : QOpenGLShader.ShaderType
      Passed on as its number.

    source : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::
    #      ShaderType type, const char *source)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceCodeE6QFlagsIN'
        '13QOpenGLShader13ShaderTypeBitEEPKc',
        type.value, self._bytesOf(source),
    )

  @overload(QOpenGLShader.ShaderType, QByteArray)
  def addShaderFromSourceCode(
      self,
      type: QOpenGLShader.ShaderType,
      source: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::ShaderType
    type, const QByteArray &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceCode

    Parameters
    ----------

    type : QOpenGLShader.ShaderType
      Passed on as its number.

    source : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpenGLShaderProgram::addShaderFromSourceCode(QOpenGLShader::
    #      ShaderType type, const QByteArray &source)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceCodeE6QFlagsIN'
        '13QOpenGLShader13ShaderTypeBitEERK10QByteArray',
        type.value, self._valueOf(source),
    )

  @overload(QOpenGLShader.ShaderType, str)
  def addShaderFromSourceFile(
      self,
      type: QOpenGLShader.ShaderType,
      fileName: str,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::addShaderFromSourceFile(QOpenGLShader::ShaderType
    type, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#addShaderFromSourceFile

    Parameters
    ----------

    type : QOpenGLShader.ShaderType
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpenGLShaderProgram::addShaderFromSourceFile(QOpenGLShader::
    #      ShaderType type, const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram23addShaderFromSourceFileE6QFlagsIN'
        '13QOpenGLShader13ShaderTypeBitEERK7QString',
        type.value, fileName,
    )

  @overload(QOpenGLShader.ShaderType, str)
  @overload(QOpenGLShader.ShaderType, NoneType)
  def addCacheableShaderFromSourceCode(
      self,
      type: QOpenGLShader.ShaderType,
      source: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader::
    ShaderType type, const char *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html

    Parameters
    ----------

    type : QOpenGLShader.ShaderType
      Passed on as its number.

    source : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode(
    #      QOpenGLShader::ShaderType type, const char *source)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceCodeE'
        '6QFlagsIN13QOpenGLShader13ShaderTypeBitEEPKc',
        type.value, self._bytesOf(source),
    )

  @overload(QOpenGLShader.ShaderType, QByteArray)
  def addCacheableShaderFromSourceCode(
      self,
      type: QOpenGLShader.ShaderType,
      source: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::addCacheableShaderFromSourceCode(QOpenGLShader::
    ShaderType type, const QByteArray &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html

    Parameters
    ----------

    type : QOpenGLShader.ShaderType
      Passed on as its number.

    source : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpenGLShaderProgram::addCacheableShaderFromSourceCode(
    #      QOpenGLShader::ShaderType type, const QByteArray &source)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceCodeE'
        '6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK10QByteArray',
        type.value, self._valueOf(source),
    )

  @overload(QOpenGLShader.ShaderType, str)
  def addCacheableShaderFromSourceFile(
      self,
      type: QOpenGLShader.ShaderType,
      fileName: str,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLShaderProgram::addCacheableShaderFromSourceFile(QOpenGLShader::
    ShaderType type, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html

    Parameters
    ----------

    type : QOpenGLShader.ShaderType
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpenGLShaderProgram::addCacheableShaderFromSourceFile(
    #      QOpenGLShader::ShaderType type, const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram32addCacheableShaderFromSourceFileE'
        '6QFlagsIN13QOpenGLShader13ShaderTypeBitEERK7QString',
        type.value, fileName,
    )

  def removeAllShaders(self) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::removeAllShaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#removeAllShaders
    """
    #  void QOpenGLShaderProgram::removeAllShaders()
    self.uglySide.call('ritual_ZN20QOpenGLShaderProgram16removeAllShadersEv')

  def link(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLShaderProgram::link()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#link
    """
    #  bool QOpenGLShaderProgram::link()
    ritual = 'ritual_ZN20QOpenGLShaderProgram4linkEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QOpenGLShaderProgram4linkEv'
    return self.uglySide.call(ritual)

  def bind(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLShaderProgram::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#bind
    """
    #  bool QOpenGLShaderProgram::bind()
    return self.uglySide.call('ritual_ZN20QOpenGLShaderProgram4bindEv')

  def release(self) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::release()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#release
    """
    #  void QOpenGLShaderProgram::release()
    self.uglySide.call('ritual_ZN20QOpenGLShaderProgram7releaseEv')

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLShaderProgram::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#create
    """
    #  bool QOpenGLShaderProgram::create()
    return self.uglySide.call('ritual_ZN20QOpenGLShaderProgram6createEv')

  @overload(str, int)
  @overload(NoneType, int)
  def bindAttributeLocation(
      self,
      name: Optional[str],
      location: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::bindAttributeLocation(const char
    *name, int location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    location : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::bindAttributeLocation(const char *name, int
    #      location)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram21bindAttributeLocationEPKci',
        self._bytesOf(name), location,
    )

  @overload(QByteArray, int)
  def bindAttributeLocation(self, name: QByteArray, location: int) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::bindAttributeLocation(const
    QByteArray &name, int location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#bindAttributeLocation

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    location : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::bindAttributeLocation(const QByteArray
    #      &name, int location)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram21bindAttributeLocationERK10QByteAr'
        'rayi',
        self._valueOf(name), location,
    )

  @overload(int)
  def enableAttributeArray(self, location: int) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::enableAttributeArray(int
    location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray

    Parameters
    ----------

    location : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::enableAttributeArray(int location)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20enableAttributeArrayEi', location,
    )

  @overload(str)
  @overload(NoneType)
  def enableAttributeArray(self, name: Optional[str]) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::enableAttributeArray(const char
    *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#enableAttributeArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QOpenGLShaderProgram::enableAttributeArray(const char *name)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram20enableAttributeArrayEPKc',
        self._bytesOf(name),
    )

  @overload(int)
  def disableAttributeArray(self, location: int) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::disableAttributeArray(int
    location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray

    Parameters
    ----------

    location : int
      Passed on as it is.
    """
    #  void QOpenGLShaderProgram::disableAttributeArray(int location)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram21disableAttributeArrayEi', location,
    )

  @overload(str)
  @overload(NoneType)
  def disableAttributeArray(self, name: Optional[str]) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::disableAttributeArray(const char
    *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#disableAttributeArray

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QOpenGLShaderProgram::disableAttributeArray(const char *name)
    self.uglySide.call(
        'ritual_ZN20QOpenGLShaderProgram21disableAttributeArrayEPKc',
        self._bytesOf(name),
    )

  def shaderDestroyed(self) -> None:
    """
    Calls Qt's 'void QOpenGLShaderProgram::shaderDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshaderprogram.html#shaderDestroyed
    """
    #  void QOpenGLShaderProgram::shaderDestroyed()
    self.uglySide.call('ritual_ZN20QOpenGLShaderProgram15shaderDestroyedEv')

  def init(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLShaderProgram::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshaderprogram.html#init
    """
    #  bool QOpenGLShaderProgram::init()
    return self.uglySide.call('ritual_ZN20QOpenGLShaderProgram4initEv')

  @staticmethod
  def defaultInnerTessellationLevels(*__, **_) -> Never:
    """
    Qt's 'QList<float> QOpenGLShaderProgram::defaultInnerTessellationLevels()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLShaderProgram.defaultInnerTessellationLevels' has no cute "
        "function yet. Qt's 'QList<float> "
        "QOpenGLShaderProgram::defaultInnerTessellationLevels() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def defaultOuterTessellationLevels(*__, **_) -> Never:
    """
    Qt's 'QList<float> QOpenGLShaderProgram::defaultOuterTessellationLevels()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLShaderProgram.defaultOuterTessellationLevels' has no cute "
        "function yet. Qt's 'QList<float> "
        "QOpenGLShaderProgram::defaultOuterTessellationLevels() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setDefaultInnerTessellationLevels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLShaderProgram::setDefaultInnerTessellationLevels(const
    QList<float> &levels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLShaderProgram.setDefaultInnerTessellationLevels' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLShaderProgram::setDefaultInnerTessellationLevels(const "
        "QList<float> &levels)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setDefaultOuterTessellationLevels(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLShaderProgram::setDefaultOuterTessellationLevels(const
    QList<float> &levels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLShaderProgram.setDefaultOuterTessellationLevels' has no "
        "cute function yet. Qt's 'void "
        "QOpenGLShaderProgram::setDefaultOuterTessellationLevels(const "
        "QList<float> &levels)': takes a type Python has no way to hand "
        "over yet.")
