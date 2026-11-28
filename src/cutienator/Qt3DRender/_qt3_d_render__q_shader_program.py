"""
Qt3DRender::QShaderProgram binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qshaderprogram.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderProgram(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QShaderProgram: a plain Python object
  standing in front of one C++ Qt3DRender::QShaderProgram.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::QShaderProgram is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderProgram that has a ritual and
  that Python can call so far, 31 names in all: 'metaObject', 'tr',
  'vertexShaderCode', 'tessellationControlShaderCode',
  'tessellationEvaluationShaderCode', 'geometryShaderCode',
  'fragmentShaderCode', 'computeShaderCode', 'setShaderCode', 'shaderCode',
  'log', 'status', 'setFormat', 'format', 'loadSource',
  'setVertexShaderCode', 'setTessellationControlShaderCode',
  'setTessellationEvaluationShaderCode', 'setGeometryShaderCode',
  'setFragmentShaderCode', 'setComputeShaderCode', 'vertexShaderCodeChanged',
  'tessellationControlShaderCodeChanged',
  'tessellationEvaluationShaderCodeChanged', 'geometryShaderCodeChanged',
  'fragmentShaderCodeChanged', 'computeShaderCodeChanged', 'logChanged',
  'statusChanged', 'formatChanged', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QShaderProgram::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QShaderProgram::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QShaderProgram::~QShaderProgram()': the destructor:
    Python never removes a C++ Qt3DRender::QShaderProgram.
  - Qt's 'Qt3DRender::QShaderProgram::QShaderProgram(QShaderProgramPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QShaderProgramPrivate *Qt3DRender::QShaderProgram::d_func()
    const': takes in Python what 'QShaderProgramPrivate
    *Qt3DRender::QShaderProgram::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderProgram is created at the first use, not by
    'Qt3DRender::QShaderProgram(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QShaderProgram.
  - Qt tells when it has removed the C++ Qt3DRender::QShaderProgram. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QShaderProgram, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Format(CuteNum):
    """
    The enum 'Qt3DRender::QShaderProgram::Format' of Qt, with the 2 names Qt
    gives in it.
    """

    GLSL = Kee[int](0)
    SPIRV = Kee[int](1)

  class ShaderType(CuteNum):
    """
    The enum 'Qt3DRender::QShaderProgram::ShaderType' of Qt, with the 6 names
    Qt gives in it.
    """

    Vertex = Kee[int](0)
    Fragment = Kee[int](1)
    TessellationControl = Kee[int](2)
    TessellationEvaluation = Kee[int](3)
    Geometry = Kee[int](4)
    Compute = Kee[int](5)

  class Status(CuteNum):
    """
    The enum 'Qt3DRender::QShaderProgram::Status' of Qt, with the 3 names Qt
    gives in it.
    """

    NotReady = Kee[int](0)
    Ready = Kee[int](1)
    Error = Kee[int](2)

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
    Calls Qt's 'QString Qt3DRender::QShaderProgram::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#tr

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
    #  QString Qt3DRender::QShaderProgram::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QShaderProgram2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QUrl)
  def loadSource(sourceUrl: QUrl) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QShaderProgram::loadSource(const QUrl
    &sourceUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#loadSource

    Parameters
    ----------

    sourceUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::loadSource(const QUrl
    #      &sourceUrl)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender14QShaderProgram10loadSourceERK4QUrl',
        CuteMixin._valueOf(sourceUrl),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QShaderProgram'

  #  A C++ Qt3DRender::QShaderProgram Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QShaderProgram'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QShaderProgram::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QShaderProgram::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def vertexShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QShaderProgram::vertexShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#vertexShaderCode

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::vertexShaderCode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram16vertexShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def tessellationControlShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgram::tessellationControlShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::tessellationControlShaderCode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram29tessellationControlShaderC'
        'odeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def tessellationEvaluationShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgram::tessellationEvaluationShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DRender::QShaderProgram::tessellationEvaluationShaderCode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram32tessellationEvaluationShad'
        'erCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def geometryShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QShaderProgram::geometryShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#geometryShaderCode

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::geometryShaderCode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram18geometryShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def fragmentShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QShaderProgram::fragmentShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#fragmentShaderCode

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::fragmentShaderCode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram18fragmentShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def computeShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QShaderProgram::computeShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#computeShaderCode

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::computeShaderCode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram17computeShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(ShaderType)
  def shaderCode(self, type: ShaderType) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QShaderProgram::shaderCode(ShaderType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#shaderCode

    Parameters
    ----------

    type : ShaderType
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgram::shaderCode(ShaderType type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram10shaderCodeENS0_10ShaderTyp'
        'eE',
        type.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def log(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QShaderProgram::log() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#log

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QShaderProgram::log() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender14QShaderProgram3logEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DRender::QShaderProgram::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DRender::QShaderProgram::status() const
    return QShaderProgram.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram6statusEv',
    ))

  def format(self) -> Format:
    """
    Calls Qt's 'Format Qt3DRender::QShaderProgram::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format Qt3DRender::QShaderProgram::format() const
    return QShaderProgram.Format(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QShaderProgram6formatEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ShaderType, QByteArray)
  def setShaderCode(self, type: ShaderType, shaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::setShaderCode(ShaderType
    type, const QByteArray &shaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#setShaderCode

    Parameters
    ----------

    type : ShaderType
      Passed on as its number.

    shaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::setShaderCode(ShaderType type, const
    #      QByteArray &shaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram13setShaderCodeENS0_10ShaderT'
        'ypeERK10QByteArray',
        type.value, self._valueOf(shaderCode),
    )

  @overload(Format)
  def setFormat(self, format: Format) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::setFormat(Format format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#setFormat

    Parameters
    ----------

    format : Format
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderProgram::setFormat(Format format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram9setFormatENS0_6FormatE',
        format.value,
    )

  @overload(QByteArray)
  def setVertexShaderCode(self, vertexShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::setVertexShaderCode(const
    QByteArray &vertexShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#setVertexShaderCode

    Parameters
    ----------

    vertexShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::setVertexShaderCode(const QByteArray
    #      &vertexShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram19setVertexShaderCodeERK10QBy'
        'teArray',
        self._valueOf(vertexShaderCode),
    )

  @overload(QByteArray)
  def setTessellationControlShaderCode(
      self,
      tessellationControlShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::setTessellationControlShaderCode(const
    QByteArray &tessellationControlShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    tessellationControlShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void
    #      Qt3DRender::QShaderProgram::setTessellationControlShaderCode(const
    #      QByteArray &tessellationControlShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram32setTessellationControlShade'
        'rCodeERK10QByteArray',
        self._valueOf(tessellationControlShaderCode),
    )

  @overload(QByteArray)
  def setTessellationEvaluationShaderCode(
      self,
      tessellationEvaluationShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::setTessellationEvaluationShaderCode(const
    QByteArray &tessellationEvaluationShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    tessellationEvaluationShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::setTessellationEvaluationShaderCode(
    #      const QByteArray &tessellationEvaluationShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram35setTessellationEvaluationSh'
        'aderCodeERK10QByteArray',
        self._valueOf(tessellationEvaluationShaderCode),
    )

  @overload(QByteArray)
  def setGeometryShaderCode(self, geometryShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::setGeometryShaderCode(const
    QByteArray &geometryShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    geometryShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::setGeometryShaderCode(const
    #      QByteArray &geometryShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram21setGeometryShaderCodeERK10Q'
        'ByteArray',
        self._valueOf(geometryShaderCode),
    )

  @overload(QByteArray)
  def setFragmentShaderCode(self, fragmentShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::setFragmentShaderCode(const
    QByteArray &fragmentShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    fragmentShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::setFragmentShaderCode(const
    #      QByteArray &fragmentShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram21setFragmentShaderCodeERK10Q'
        'ByteArray',
        self._valueOf(fragmentShaderCode),
    )

  @overload(QByteArray)
  def setComputeShaderCode(self, computeShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::setComputeShaderCode(const
    QByteArray &computeShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    computeShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::setComputeShaderCode(const QByteArray
    #      &computeShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram20setComputeShaderCodeERK10QB'
        'yteArray',
        self._valueOf(computeShaderCode),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QShaderProgram::QShaderProgram(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#QShaderProgram

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QShaderProgram::QShaderProgram(Qt3DCore::QNode *parent)
    self._noteCreation(QShaderProgram, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QShaderProgramC1EPN8Qt3DCore5QNodeE',
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

  @overload(QByteArray)
  def vertexShaderCodeChanged(self, vertexShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::vertexShaderCodeChanged(const QByteArray
    &vertexShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    vertexShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::vertexShaderCodeChanged(const
    #      QByteArray &vertexShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram23vertexShaderCodeChangedERK1'
        '0QByteArray',
        self._valueOf(vertexShaderCode),
    )

  @overload(QByteArray)
  def tessellationControlShaderCodeChanged(
      self,
      tessellationControlShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::tessellationControlShaderCodeChanged(const
    QByteArray &tessellationControlShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    tessellationControlShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::tessellationControlShaderCodeChanged(
    #      const QByteArray &tessellationControlShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram36tessellationControlShaderCo'
        'deChangedERK10QByteArray',
        self._valueOf(tessellationControlShaderCode),
    )

  @overload(QByteArray)
  def tessellationEvaluationShaderCodeChanged(
      self,
      tessellationEvaluationShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::tessellationEvaluationShaderCodeChanged(const
    QByteArray &tessellationEvaluationShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    tessellationEvaluationShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::
    #      tessellationEvaluationShaderCodeChanged(const QByteArray
    #      &tessellationEvaluationShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram39tessellationEvaluationShade'
        'rCodeChangedERK10QByteArray',
        self._valueOf(tessellationEvaluationShaderCode),
    )

  @overload(QByteArray)
  def geometryShaderCodeChanged(
      self,
      geometryShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::geometryShaderCodeChanged(const QByteArray
    &geometryShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    geometryShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::geometryShaderCodeChanged(const
    #      QByteArray &geometryShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram25geometryShaderCodeChangedER'
        'K10QByteArray',
        self._valueOf(geometryShaderCode),
    )

  @overload(QByteArray)
  def fragmentShaderCodeChanged(
      self,
      fragmentShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::fragmentShaderCodeChanged(const QByteArray
    &fragmentShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    fragmentShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::fragmentShaderCodeChanged(const
    #      QByteArray &fragmentShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram25fragmentShaderCodeChangedER'
        'K10QByteArray',
        self._valueOf(fragmentShaderCode),
    )

  @overload(QByteArray)
  def computeShaderCodeChanged(self, computeShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgram::computeShaderCodeChanged(const QByteArray
    &computeShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html

    Parameters
    ----------

    computeShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgram::computeShaderCodeChanged(const
    #      QByteArray &computeShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram24computeShaderCodeChangedERK'
        '10QByteArray',
        self._valueOf(computeShaderCode),
    )

  @overload(str)
  def logChanged(self, log: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::logChanged(const QString
    &log)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#logChanged

    Parameters
    ----------

    log : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QShaderProgram::logChanged(const QString &log)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram10logChangedERK7QString', log,
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::statusChanged(Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderProgram::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram13statusChangedENS0_6StatusE',
        status.value,
    )

  @overload(Format)
  def formatChanged(self, format: Format) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgram::formatChanged(Format
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#formatChanged

    Parameters
    ----------

    format : Format
      Passed on as its number.
    """
    #  void Qt3DRender::QShaderProgram::formatChanged(Format format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram13formatChangedENS0_6FormatE',
        format.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QShaderProgramPrivate]:
    """
    Calls Qt's 'QShaderProgramPrivate *Qt3DRender::QShaderProgram::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogram.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QShaderProgramPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderProgramPrivate *Qt3DRender::QShaderProgram::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QShaderProgram6d_funcEv',
    )
    return Qt3DRender.QShaderProgramPrivate._cuteAt(address)
