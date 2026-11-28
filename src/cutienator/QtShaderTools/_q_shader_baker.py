"""
QShaderBaker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtShaderTools/6.12.0/QtShaderTools/rhi/qshaderbaker.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QShader, QShaderDescription

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderBaker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderBaker: a plain Python object standing in front
  of one C++ QShaderBaker.

  What exists
  -----------

  Every function of Qt's QShaderBaker that has a ritual and that Python can
  call so far, 14 names in all: 'setSourceFileName', 'setSourceDevice',
  'setSourceString', 'setPreamble',
  'setBatchableVertexShaderExtraInputLocation', 'setPerTargetCompilation',
  'setBreakOnShaderTranslationError', 'setTessellationMode',
  'setTessellationOutputVertexCount', 'setMultiViewCount', 'setSpirvOptions',
  'setGlslOptions', 'bake', 'errorMessage'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShaderBaker::~QShaderBaker()': the destructor: Python never
    removes a C++ QShaderBaker.
  - Qt's 'void QShaderBaker::setGeneratedShaders(const QList<GeneratedShader>
    &v)': takes a type Python has no way to hand over yet.
  - Qt's 'void QShaderBaker::setGeneratedShaderVariants(const
    QList<QShader::Variant> &v)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QShaderBaker is created at the first use, not by
    'QShaderBaker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QShaderBaker.
  - Each name of Qt's QShaderBaker that has no cute function yet,
    'setGeneratedShaderVariants', 'setGeneratedShaders', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QShaderBaker, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class GlslOption(CuteFlags, scoped=True):
    """
    The flags enum 'QShaderBaker::GlslOption' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QShaderBaker::GlslOptions'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    GlslEsFragDefaultFloatPrecisionMedium = 0x1

  GlslOptions = GlslOption

  class SpirvOption(CuteFlags, scoped=True):
    """
    The flags enum 'QShaderBaker::SpirvOption' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QShaderBaker::SpirvOptions'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    GenerateFullDebugInfo = 0x1
    StripDebugAndVarInfo = 0x2

  SpirvOptions = SpirvOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderBaker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorMessage(self) -> str:
    """
    Calls Qt's 'QString QShaderBaker::errorMessage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#errorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QShaderBaker::errorMessage() const
    return self.uglySide.call('ritual_ZNK12QShaderBaker12errorMessageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSourceFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QShaderBaker::setSourceFileName(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setSourceFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QShaderBaker::setSourceFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker17setSourceFileNameERK7QString', fileName,
    )

  @overload(str, QShader.Stage)
  def setSourceFileName(self, fileName: str, stage: QShader.Stage) -> None:
    """
    Calls Qt's 'void QShaderBaker::setSourceFileName(const QString &fileName,
    QShader::Stage stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setSourceFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    stage : QShader.Stage
      Passed on as its number.
    """
    #  void QShaderBaker::setSourceFileName(const QString &fileName,
    #      QShader::Stage stage)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker17setSourceFileNameERK7QStringN7QShader5Sta'
        'geE',
        fileName, stage.value,
    )

  @overload(QIODevice, QShader.Stage)
  @overload(NoneType, QShader.Stage)
  @overload(QIODevice, QShader.Stage, str)
  @overload(NoneType, QShader.Stage, str)
  def setSourceDevice(
      self,
      device: Optional[QIODevice],
      stage: QShader.Stage,
      fileName: str = '',
  ) -> None:
    """
    Calls Qt's 'void QShaderBaker::setSourceDevice(QIODevice *device,
    QShader::Stage stage, const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#setSourceDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stage : QShader.Stage
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QShaderBaker::setSourceDevice(QIODevice *device, QShader::Stage
    #      stage, const QString &fileName)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker15setSourceDeviceEP9QIODeviceN7QShader5Stag'
        'eERK7QString',
        self._addressOf(device), stage.value, fileName,
    )

  @overload(QByteArray, QShader.Stage)
  @overload(QByteArray, QShader.Stage, str)
  def setSourceString(
      self,
      sourceString: QByteArray,
      stage: QShader.Stage,
      fileName: str = '',
  ) -> None:
    """
    Calls Qt's 'void QShaderBaker::setSourceString(const QByteArray
    &sourceString, QShader::Stage stage, const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#setSourceString

    Parameters
    ----------

    sourceString : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    stage : QShader.Stage
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QShaderBaker::setSourceString(const QByteArray &sourceString,
    #      QShader::Stage stage, const QString &fileName)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker15setSourceStringERK10QByteArrayN7QShader5S'
        'tageERK7QString',
        self._valueOf(sourceString), stage.value, fileName,
    )

  @overload(QByteArray)
  def setPreamble(self, preamble: QByteArray) -> None:
    """
    Calls Qt's 'void QShaderBaker::setPreamble(const QByteArray &preamble)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#setPreamble

    Parameters
    ----------

    preamble : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QShaderBaker::setPreamble(const QByteArray &preamble)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker11setPreambleERK10QByteArray',
        self._valueOf(preamble),
    )

  @overload(int)
  def setBatchableVertexShaderExtraInputLocation(
      self,
      location: int,
  ) -> None:
    """
    Calls Qt's 'void
    QShaderBaker::setBatchableVertexShaderExtraInputLocation(int location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html

    Parameters
    ----------

    location : int
      Passed on as it is.
    """
    #  void QShaderBaker::setBatchableVertexShaderExtraInputLocation(int
    #      location)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker42setBatchableVertexShaderExtraInputLocatio'
        'nEi',
        location,
    )

  @overload(bool)
  def setPerTargetCompilation(self, enable: bool) -> None:
    """
    Calls Qt's 'void QShaderBaker::setPerTargetCompilation(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setPerTargetCompilation

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QShaderBaker::setPerTargetCompilation(bool enable)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker23setPerTargetCompilationEb', enable,
    )

  @overload(bool)
  def setBreakOnShaderTranslationError(self, enable: bool) -> None:
    """
    Calls Qt's 'void QShaderBaker::setBreakOnShaderTranslationError(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setBreakOnShaderTranslationError

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QShaderBaker::setBreakOnShaderTranslationError(bool enable)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker32setBreakOnShaderTranslationErrorEb',
        enable,
    )

  @overload(QShaderDescription.TessellationMode)
  def setTessellationMode(
      self,
      mode: QShaderDescription.TessellationMode,
  ) -> None:
    """
    Calls Qt's 'void
    QShaderBaker::setTessellationMode(QShaderDescription::TessellationMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setTessellationMode

    Parameters
    ----------

    mode : QShaderDescription.TessellationMode
      Passed on as its number.
    """
    #  void QShaderBaker::setTessellationMode(QShaderDescription::
    #      TessellationMode mode)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker19setTessellationModeEN18QShaderDescription'
        '16TessellationModeE',
        mode.value,
    )

  @overload(int)
  def setTessellationOutputVertexCount(self, count: int) -> None:
    """
    Calls Qt's 'void QShaderBaker::setTessellationOutputVertexCount(int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setTessellationOutputVertexCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QShaderBaker::setTessellationOutputVertexCount(int count)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker32setTessellationOutputVertexCountEi', count,
    )

  @overload(int)
  def setMultiViewCount(self, count: int) -> None:
    """
    Calls Qt's 'void QShaderBaker::setMultiViewCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderbaker.html#setMultiViewCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QShaderBaker::setMultiViewCount(int count)
    self.uglySide.call('ritual_ZN12QShaderBaker17setMultiViewCountEi', count)

  @overload(SpirvOptions)
  def setSpirvOptions(self, options: SpirvOptions) -> None:
    """
    Calls Qt's 'void QShaderBaker::setSpirvOptions(SpirvOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#setSpirvOptions

    Parameters
    ----------

    options : SpirvOptions
      Passed on as its number.
    """
    #  void QShaderBaker::setSpirvOptions(SpirvOptions options)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker15setSpirvOptionsE6QFlagsINS_11SpirvOptionE'
        'E',
        options.value,
    )

  @overload(GlslOptions)
  def setGlslOptions(self, options: GlslOptions) -> None:
    """
    Calls Qt's 'void QShaderBaker::setGlslOptions(GlslOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#setGlslOptions

    Parameters
    ----------

    options : GlslOptions
      Passed on as its number.
    """
    #  void QShaderBaker::setGlslOptions(GlslOptions options)
    self.uglySide.call(
        'ritual_ZN12QShaderBaker14setGlslOptionsE6QFlagsINS_10GlslOptionEE',
        options.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QShaderBaker::QShaderBaker()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#QShaderBaker
    """
    #  QShaderBaker::QShaderBaker()
    self._noteCreation(QShaderBaker, lambda: Rituals.call(
        'ritual_ZN12QShaderBakerC1Ev',
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

  def bake(self) -> QShader:
    """
    Calls Qt's 'QShader QShaderBaker::bake()'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderbaker.html#bake

    Returns
    -------

    QShader
      A new cute QShader around the copy Qt gave back. Python owns it.
    """
    #  QShader QShaderBaker::bake()
    address = self.uglySide.call('ritual_ZN12QShaderBaker4bakeEv')
    return QShader._cuteOwning(address)

  @staticmethod
  def setGeneratedShaderVariants(*__, **_) -> Never:
    """
    Qt's 'void QShaderBaker::setGeneratedShaderVariants(const
    QList<QShader::Variant> &v)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QShaderBaker.setGeneratedShaderVariants' has no cute function "
        "yet. Qt's 'void QShaderBaker::setGeneratedShaderVariants(const "
        "QList<QShader::Variant> &v)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setGeneratedShaders(*__, **_) -> Never:
    """
    Qt's 'void QShaderBaker::setGeneratedShaders(const QList<GeneratedShader>
    &v)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QShaderBaker.setGeneratedShaders' has no cute function yet. Qt's "
        "'void QShaderBaker::setGeneratedShaders(const "
        "QList<GeneratedShader> &v)': takes a type Python has no way to "
        "hand over yet.")
