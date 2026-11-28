"""
Qt3DRender::QShaderProgramBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qshaderprogrambuilder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
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


class QShaderProgramBuilder(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QShaderProgramBuilder: a plain Python
  object standing in front of one C++ Qt3DRender::QShaderProgramBuilder.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::QShaderProgramBuilder is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderProgramBuilder that has a ritual
  and that Python can call so far, 39 names in all: 'metaObject', 'tr',
  'shaderProgram', 'enabledLayers', 'vertexShaderGraph',
  'tessellationControlShaderGraph', 'tessellationEvaluationShaderGraph',
  'geometryShaderGraph', 'fragmentShaderGraph', 'computeShaderGraph',
  'vertexShaderCode', 'tessellationControlShaderCode',
  'tessellationEvaluationShaderCode', 'geometryShaderCode',
  'fragmentShaderCode', 'computeShaderCode', 'setShaderProgram',
  'setEnabledLayers', 'setVertexShaderGraph',
  'setTessellationControlShaderGraph',
  'setTessellationEvaluationShaderGraph', 'setGeometryShaderGraph',
  'setFragmentShaderGraph', 'setComputeShaderGraph', 'shaderProgramChanged',
  'enabledLayersChanged', 'vertexShaderGraphChanged',
  'tessellationControlShaderGraphChanged',
  'tessellationEvaluationShaderGraphChanged', 'geometryShaderGraphChanged',
  'fragmentShaderGraphChanged', 'computeShaderGraphChanged',
  'vertexShaderCodeChanged', 'tessellationControlShaderCodeChanged',
  'tessellationEvaluationShaderCodeChanged', 'geometryShaderCodeChanged',
  'fragmentShaderCodeChanged', 'computeShaderCodeChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QShaderProgramBuilder::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QShaderProgramBuilder::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QShaderProgramBuilder::~QShaderProgramBuilder()': the
    destructor: Python never removes a C++ Qt3DRender::QShaderProgramBuilder.
  - Qt's 'Qt3DRender::QShaderProgramBuilder::QShaderProgramBuilder(
    QShaderProgramBuilderPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QShaderProgramBuilderPrivate
    *Qt3DRender::QShaderProgramBuilder::d_func() const': takes in Python what
    'QShaderProgramBuilderPrivate
    *Qt3DRender::QShaderProgramBuilder::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 47 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderProgramBuilder is created at the first use,
    not by 'Qt3DRender::QShaderProgramBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QShaderProgramBuilder.
  - Qt tells when it has removed the C++ Qt3DRender::QShaderProgramBuilder.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QShaderProgramBuilder::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html#tr

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
    #  QString Qt3DRender::QShaderProgramBuilder::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QShaderProgramBuilder'

  #  A C++ Qt3DRender::QShaderProgramBuilder Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QShaderProgramBuilder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::QShaderProgramBuilder::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QShaderProgramBuilder::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shaderProgram(self) -> Optional[Qt3DRender.QShaderProgram]:
    """
    Calls Qt's 'QShaderProgram
    *Qt3DRender::QShaderProgramBuilder::shaderProgram() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    Optional[Qt3DRender.QShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderProgram *Qt3DRender::QShaderProgramBuilder::shaderProgram()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder13shaderProgramEv',
    )
    return Qt3DRender.QShaderProgram._cuteAt(address)

  def enabledLayers(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::QShaderProgramBuilder::enabledLayers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QShaderProgramBuilder::enabledLayers() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder13enabledLayersEv',
    )
    return QStringList._cuteOwning(address)

  def vertexShaderGraph(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QShaderProgramBuilder::vertexShaderGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QShaderProgramBuilder::vertexShaderGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder17vertexShaderGraphEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def tessellationControlShaderGraph(self) -> QUrl:
    """
    Calls Qt's 'QUrl
    Qt3DRender::QShaderProgramBuilder::tessellationControlShaderGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl
    #      Qt3DRender::QShaderProgramBuilder::tessellationControlShaderGraph(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder30tessellationControl'
        'ShaderGraphEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def tessellationEvaluationShaderGraph(self) -> QUrl:
    """
    Calls Qt's 'QUrl
    Qt3DRender::QShaderProgramBuilder::tessellationEvaluationShaderGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QShaderProgramBuilder::
    #      tessellationEvaluationShaderGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder33tessellationEvaluat'
        'ionShaderGraphEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def geometryShaderGraph(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QShaderProgramBuilder::geometryShaderGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QShaderProgramBuilder::geometryShaderGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder19geometryShaderGraph'
        'Ev',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def fragmentShaderGraph(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QShaderProgramBuilder::fragmentShaderGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QShaderProgramBuilder::fragmentShaderGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder19fragmentShaderGraph'
        'Ev',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def computeShaderGraph(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QShaderProgramBuilder::computeShaderGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QShaderProgramBuilder::computeShaderGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder18computeShaderGraphE'
        'v',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def vertexShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramBuilder::vertexShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramBuilder::vertexShaderCode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder16vertexShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def tessellationControlShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramBuilder::tessellationControlShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DRender::QShaderProgramBuilder::tessellationControlShaderCode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder29tessellationControl'
        'ShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def tessellationEvaluationShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramBuilder::tessellationEvaluationShaderCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramBuilder::
    #      tessellationEvaluationShaderCode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder32tessellationEvaluat'
        'ionShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def geometryShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramBuilder::geometryShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramBuilder::geometryShaderCode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder18geometryShaderCodeE'
        'v',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def fragmentShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramBuilder::fragmentShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramBuilder::fragmentShaderCode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder18fragmentShaderCodeE'
        'v',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def computeShaderCode(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::QShaderProgramBuilder::computeShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QShaderProgramBuilder::computeShaderCode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QShaderProgramBuilder17computeShaderCodeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QShaderProgram'])
  @overload(NoneType)
  def setShaderProgram(
      self,
      program: Optional[Qt3DRender.QShaderProgram],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setShaderProgram(Qt3DRender::
    QShaderProgram *program)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    program : Optional[Qt3DRender.QShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QShaderProgramBuilder::setShaderProgram(Qt3DRender::
    #      QShaderProgram *program)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder16setShaderProgramEPNS'
        '_14QShaderProgramE',
        self._addressOf(program),
    )

  @overload(QStringList)
  def setEnabledLayers(self, layers: QStringList) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setEnabledLayers(const QStringList
    &layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    layers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QShaderProgramBuilder::setEnabledLayers(const
    #      QStringList &layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder16setEnabledLayersERK5'
        'QListI7QStringE',
        self._valueOf(layers),
    )

  @overload(QUrl)
  def setVertexShaderGraph(self, vertexShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setVertexShaderGraph(const QUrl
    &vertexShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    vertexShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::setVertexShaderGraph(const
    #      QUrl &vertexShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder20setVertexShaderGraph'
        'ERK4QUrl',
        self._valueOf(vertexShaderGraph),
    )

  @overload(QUrl)
  def setTessellationControlShaderGraph(
      self,
      tessellationControlShaderGraph: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setTessellationControlShaderGraph(
    const QUrl &tessellationControlShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    tessellationControlShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::
    #      setTessellationControlShaderGraph(const QUrl
    #      &tessellationControlShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder33setTessellationContr'
        'olShaderGraphERK4QUrl',
        self._valueOf(tessellationControlShaderGraph),
    )

  @overload(QUrl)
  def setTessellationEvaluationShaderGraph(
      self,
      tessellationEvaluationShaderGraph: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setTessellationEvaluationShaderGraph(
    const QUrl &tessellationEvaluationShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    tessellationEvaluationShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::
    #      setTessellationEvaluationShaderGraph(const QUrl
    #      &tessellationEvaluationShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder36setTessellationEvalu'
        'ationShaderGraphERK4QUrl',
        self._valueOf(tessellationEvaluationShaderGraph),
    )

  @overload(QUrl)
  def setGeometryShaderGraph(self, geometryShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setGeometryShaderGraph(const QUrl
    &geometryShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    geometryShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::setGeometryShaderGraph(const
    #      QUrl &geometryShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder22setGeometryShaderGra'
        'phERK4QUrl',
        self._valueOf(geometryShaderGraph),
    )

  @overload(QUrl)
  def setFragmentShaderGraph(self, fragmentShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setFragmentShaderGraph(const QUrl
    &fragmentShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    fragmentShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::setFragmentShaderGraph(const
    #      QUrl &fragmentShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder22setFragmentShaderGra'
        'phERK4QUrl',
        self._valueOf(fragmentShaderGraph),
    )

  @overload(QUrl)
  def setComputeShaderGraph(self, computeShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::setComputeShaderGraph(const QUrl
    &computeShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    computeShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::setComputeShaderGraph(const
    #      QUrl &computeShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder21setComputeShaderGrap'
        'hERK4QUrl',
        self._valueOf(computeShaderGraph),
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
    'Qt3DRender::QShaderProgramBuilder::QShaderProgramBuilder(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QShaderProgramBuilder::QShaderProgramBuilder(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QShaderProgramBuilder, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilderC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DRender.QShaderProgram'])
  @overload(NoneType)
  def shaderProgramChanged(
      self,
      shaderProgram: Optional[Qt3DRender.QShaderProgram],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::shaderProgramChanged(Qt3DRender::
    QShaderProgram *shaderProgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    shaderProgram : Optional[Qt3DRender.QShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QShaderProgramBuilder::shaderProgramChanged(
    #      Qt3DRender::QShaderProgram *shaderProgram)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder20shaderProgramChanged'
        'EPNS_14QShaderProgramE',
        self._addressOf(shaderProgram),
    )

  @overload(QStringList)
  def enabledLayersChanged(self, layers: QStringList) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::enabledLayersChanged(const QStringList
    &layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    layers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QShaderProgramBuilder::enabledLayersChanged(const
    #      QStringList &layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder20enabledLayersChanged'
        'ERK5QListI7QStringE',
        self._valueOf(layers),
    )

  @overload(QUrl)
  def vertexShaderGraphChanged(self, vertexShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::vertexShaderGraphChanged(const QUrl
    &vertexShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    vertexShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::vertexShaderGraphChanged(const
    #      QUrl &vertexShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder24vertexShaderGraphCha'
        'ngedERK4QUrl',
        self._valueOf(vertexShaderGraph),
    )

  @overload(QUrl)
  def tessellationControlShaderGraphChanged(
      self,
      tessellationControlShaderGraph: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::tessellationControlShaderGraphChanged(
    const QUrl &tessellationControlShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    tessellationControlShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::
    #      tessellationControlShaderGraphChanged(const QUrl
    #      &tessellationControlShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder37tessellationControlS'
        'haderGraphChangedERK4QUrl',
        self._valueOf(tessellationControlShaderGraph),
    )

  @overload(QUrl)
  def tessellationEvaluationShaderGraphChanged(
      self,
      tessellationEvaluationShaderGraph: QUrl,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgramBuilder::
    tessellationEvaluationShaderGraphChanged(const QUrl
    &tessellationEvaluationShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    tessellationEvaluationShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::
    #      tessellationEvaluationShaderGraphChanged(const QUrl
    #      &tessellationEvaluationShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder40tessellationEvaluati'
        'onShaderGraphChangedERK4QUrl',
        self._valueOf(tessellationEvaluationShaderGraph),
    )

  @overload(QUrl)
  def geometryShaderGraphChanged(self, geometryShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::geometryShaderGraphChanged(const QUrl
    &geometryShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    geometryShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::geometryShaderGraphChanged(
    #      const QUrl &geometryShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder26geometryShaderGraphC'
        'hangedERK4QUrl',
        self._valueOf(geometryShaderGraph),
    )

  @overload(QUrl)
  def fragmentShaderGraphChanged(self, fragmentShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::fragmentShaderGraphChanged(const QUrl
    &fragmentShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    fragmentShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::fragmentShaderGraphChanged(
    #      const QUrl &fragmentShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder26fragmentShaderGraphC'
        'hangedERK4QUrl',
        self._valueOf(fragmentShaderGraph),
    )

  @overload(QUrl)
  def computeShaderGraphChanged(self, computeShaderGraph: QUrl) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::computeShaderGraphChanged(const QUrl
    &computeShaderGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    computeShaderGraph : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void
    #      Qt3DRender::QShaderProgramBuilder::computeShaderGraphChanged(const
    #      QUrl &computeShaderGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder25computeShaderGraphCh'
        'angedERK4QUrl',
        self._valueOf(computeShaderGraph),
    )

  @overload(QByteArray)
  def vertexShaderCodeChanged(self, vertexShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::vertexShaderCodeChanged(const
    QByteArray &vertexShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    vertexShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::vertexShaderCodeChanged(const
    #      QByteArray &vertexShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder23vertexShaderCodeChan'
        'gedERK10QByteArray',
        self._valueOf(vertexShaderCode),
    )

  @overload(QByteArray)
  def tessellationControlShaderCodeChanged(
      self,
      tessellationControlShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::tessellationControlShaderCodeChanged(
    const QByteArray &tessellationControlShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    tessellationControlShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::
    #      tessellationControlShaderCodeChanged(const QByteArray
    #      &tessellationControlShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder36tessellationControlS'
        'haderCodeChangedERK10QByteArray',
        self._valueOf(tessellationControlShaderCode),
    )

  @overload(QByteArray)
  def tessellationEvaluationShaderCodeChanged(
      self,
      tessellationEvaluationShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderProgramBuilder::
    tessellationEvaluationShaderCodeChanged(const QByteArray
    &tessellationEvaluationShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    tessellationEvaluationShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::
    #      tessellationEvaluationShaderCodeChanged(const QByteArray
    #      &tessellationEvaluationShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder39tessellationEvaluati'
        'onShaderCodeChangedERK10QByteArray',
        self._valueOf(tessellationEvaluationShaderCode),
    )

  @overload(QByteArray)
  def geometryShaderCodeChanged(
      self,
      geometryShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::geometryShaderCodeChanged(const
    QByteArray &geometryShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    geometryShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void
    #      Qt3DRender::QShaderProgramBuilder::geometryShaderCodeChanged(const
    #      QByteArray &geometryShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder25geometryShaderCodeCh'
        'angedERK10QByteArray',
        self._valueOf(geometryShaderCode),
    )

  @overload(QByteArray)
  def fragmentShaderCodeChanged(
      self,
      fragmentShaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::fragmentShaderCodeChanged(const
    QByteArray &fragmentShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    fragmentShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void
    #      Qt3DRender::QShaderProgramBuilder::fragmentShaderCodeChanged(const
    #      QByteArray &fragmentShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder25fragmentShaderCodeCh'
        'angedERK10QByteArray',
        self._valueOf(fragmentShaderCode),
    )

  @overload(QByteArray)
  def computeShaderCodeChanged(self, computeShaderCode: QByteArray) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QShaderProgramBuilder::computeShaderCodeChanged(const
    QByteArray &computeShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html

    Parameters
    ----------

    computeShaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderProgramBuilder::computeShaderCodeChanged(const
    #      QByteArray &computeShaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder24computeShaderCodeCha'
        'ngedERK10QByteArray',
        self._valueOf(computeShaderCode),
    )

  def d_func(self) -> Optional[Qt3DRender.QShaderProgramBuilderPrivate]:
    """
    Calls Qt's 'QShaderProgramBuilderPrivate
    *Qt3DRender::QShaderProgramBuilder::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshaderprogrambuilder.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QShaderProgramBuilderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderProgramBuilderPrivate
    #      *Qt3DRender::QShaderProgramBuilder::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QShaderProgramBuilder6d_funcEv',
    )
    return Qt3DRender.QShaderProgramBuilderPrivate._cuteAt(address)
