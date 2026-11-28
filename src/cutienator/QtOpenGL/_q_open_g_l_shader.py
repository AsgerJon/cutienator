"""
QOpenGLShader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglshaderprogram.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtGui import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLShader(QObject):
  """
  The cute side of Qt's QOpenGLShader: a plain Python object standing in
  front of one C++ QOpenGLShader.

  It is built on the cute 'QObject', as Qt's QOpenGLShader is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLShader that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'shaderType',
  'compileSourceCode', 'compileSourceFile', 'sourceCode', 'isCompiled',
  'log', 'shaderId', 'hasOpenGLShaders'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLShader::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpenGLShader::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLShader::~QOpenGLShader()': the destructor: Python never
    removes a C++ QOpenGLShader.
  - Qt's 'bool QOpenGLShader::compileSourceCode(const QString &source)':
    takes in Python what 'bool QOpenGLShader::compileSourceCode(const char
    *source)' takes.
  - Qt's 'QOpenGLShaderPrivate *QOpenGLShader::d_func()': gives
    'QOpenGLShaderPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLShaderPrivate *QOpenGLShader::d_func() const': gives
    'QOpenGLShaderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLShader is created at the first use, not by
    'QOpenGLShader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLShader.
  - Qt tells when it has removed the C++ QOpenGLShader. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLShader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ShaderTypeBit(CuteFlags):
    """
    The flags enum 'QOpenGLShader::ShaderTypeBit' of Qt, with the 6 names Qt
    gives in it. Qt names the type of its combinations
    'QOpenGLShader::ShaderType'.
    """

    Vertex = 0x1
    Fragment = 0x2
    Geometry = 0x4
    TessellationControl = 0x8
    TessellationEvaluation = 0x10
    Compute = 0x20

  ShaderType = ShaderTypeBit

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
    Calls Qt's 'QString QOpenGLShader::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#tr

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
    #  QString QOpenGLShader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QOpenGLShader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(ShaderType)
  @overload(ShaderType, QOpenGLContext)
  @overload(ShaderType, NoneType)
  def hasOpenGLShaders(
      type: ShaderType,
      context: Optional[QOpenGLContext] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QOpenGLShader::hasOpenGLShaders(ShaderType type,
    QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshader.html#hasOpenGLShaders

    Parameters
    ----------

    type : ShaderType
      Passed on as its number.

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QOpenGLShader::hasOpenGLShaders(ShaderType type, QOpenGLContext
    #      *context)
    return Rituals.call(
        'ritual_ZN13QOpenGLShader16hasOpenGLShadersE6QFlagsINS_13ShaderType'
        'BitEEP14QOpenGLContext',
        type.value, CuteMixin._addressOf(context),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLShader'

  #  A C++ QOpenGLShader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLShader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLShader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLShader::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLShader10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shaderType(self) -> ShaderType:
    """
    Calls Qt's 'QOpenGLShader::ShaderType QOpenGLShader::shaderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#shaderType

    Returns
    -------

    ShaderType
      The value standing for the combination Qt gave back.
    """
    #  QOpenGLShader::ShaderType QOpenGLShader::shaderType() const
    return QOpenGLShader.ShaderType(self.uglySide.call(
        'ritual_ZNK13QOpenGLShader10shaderTypeEv',
    ))

  def sourceCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOpenGLShader::sourceCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#sourceCode

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpenGLShader::sourceCode() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLShader10sourceCodeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isCompiled(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLShader::isCompiled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#isCompiled
    """
    #  bool QOpenGLShader::isCompiled() const
    return self.uglySide.call('ritual_ZNK13QOpenGLShader10isCompiledEv')

  def log(self) -> str:
    """
    Calls Qt's 'QString QOpenGLShader::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpenGLShader::log() const
    return self.uglySide.call('ritual_ZNK13QOpenGLShader3logEv')

  def shaderId(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLShader::shaderId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#shaderId
    """
    #  GLuint QOpenGLShader::shaderId() const
    return self.uglySide.call('ritual_ZNK13QOpenGLShader8shaderIdEv')

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

  @overload(ShaderType)
  @overload(ShaderType, QObject)
  @overload(ShaderType, NoneType)
  def __init__(
      self,
      type: ShaderType,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLShader::QOpenGLShader(QOpenGLShader::ShaderType type, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglshader.html#QOpenGLShader

    Parameters
    ----------

    type : ShaderType
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLShader::QOpenGLShader(QOpenGLShader::ShaderType type, QObject
    #      *parent)
    self._noteCreation(QOpenGLShader, lambda: Rituals.call(
        'ritual_ZN13QOpenGLShaderC1E6QFlagsINS_13ShaderTypeBitEEP7QObject',
        type.value, self._addressOf(parent, 'QObject'),
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

  @overload(str)
  @overload(NoneType)
  def compileSourceCode(self, source: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QOpenGLShader::compileSourceCode(const char *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshader.html#compileSourceCode

    Parameters
    ----------

    source : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QOpenGLShader::compileSourceCode(const char *source)
    return self.uglySide.call(
        'ritual_ZN13QOpenGLShader17compileSourceCodeEPKc',
        self._bytesOf(source),
    )

  @overload(QByteArray)
  def compileSourceCode(self, source: QByteArray) -> bool:
    """
    Calls Qt's 'bool QOpenGLShader::compileSourceCode(const QByteArray
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshader.html#compileSourceCode

    Parameters
    ----------

    source : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpenGLShader::compileSourceCode(const QByteArray &source)
    return self.uglySide.call(
        'ritual_ZN13QOpenGLShader17compileSourceCodeERK10QByteArray',
        self._valueOf(source),
    )

  @overload(str)
  def compileSourceFile(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QOpenGLShader::compileSourceFile(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglshader.html#compileSourceFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QOpenGLShader::compileSourceFile(const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN13QOpenGLShader17compileSourceFileERK7QString', fileName,
    )


#  Qt's 'QList<QOpenGLShader *>': the list of QOpenGLShader, which
#  'QList[QOpenGLShader]' gives. It is made here, so that there is one as
#  soon as there can be a QOpenGLShader.
QList.createKind(
    QOpenGLShader, 'address',
    make='ritual_list_make_QOpenGLShader_ptr',
    add='ritual_list_add_QOpenGLShader_ptr',
    size='ritual_list_size_QOpenGLShader_ptr',
    at='ritual_list_at_QOpenGLShader_ptr',
    drop='ritual_list_drop_QOpenGLShader_ptr',
)
