"""
QSpirvCompiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtShaderTools/6.12.0/QtShaderTools/private/qspirvcompiler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSpirvCompiler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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


class QSpirvCompiler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSpirvCompiler: a plain Python object standing in
  front of one C++ QSpirvCompiler.

  What exists
  -----------

  Every function of Qt's QSpirvCompiler that has a ritual and that Python can
  call so far, 8 names in all: 'setSourceFileName', 'setSourceDevice',
  'setSourceString', 'setFlags', 'setPreamble',
  'setSGBatchingVertexInputLocation', 'compileToSpirv', 'errorMessage'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSpirvCompiler::~QSpirvCompiler()': the destructor: Python never
    removes a C++ QSpirvCompiler.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSpirvCompiler is created at the first use, not by
    'QSpirvCompiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpirvCompiler.
  """

  #  The enums Qt writes inside QSpirvCompiler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QSpirvCompiler::Flag' of Qt, with the 2 names Qt gives in
    it. Qt names the type of its combinations 'QSpirvCompiler::Flags'.
    """

    RewriteToMakeBatchableForSG = 0x1
    FullDebugInfo = 0x2

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpirvCompiler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorMessage(self) -> str:
    """
    Calls Qt's 'QString QSpirvCompiler::errorMessage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvcompiler.html#errorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpirvCompiler::errorMessage() const
    return self.uglySide.call('ritual_ZNK14QSpirvCompiler12errorMessageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSourceFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QSpirvCompiler::setSourceFileName(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvcompiler.html#setSourceFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSpirvCompiler::setSourceFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler17setSourceFileNameERK7QString', fileName,
    )

  @overload(str, QShader.Stage)
  def setSourceFileName(self, fileName: str, stage: QShader.Stage) -> None:
    """
    Calls Qt's 'void QSpirvCompiler::setSourceFileName(const QString
    &fileName, QShader::Stage stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvcompiler.html#setSourceFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    stage : QShader.Stage
      Passed on as its number.
    """
    #  void QSpirvCompiler::setSourceFileName(const QString &fileName,
    #      QShader::Stage stage)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler17setSourceFileNameERK7QStringN7QShader5S'
        'tageE',
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
    Calls Qt's 'void QSpirvCompiler::setSourceDevice(QIODevice *device,
    QShader::Stage stage, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvcompiler.html#setSourceDevice

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
    #  void QSpirvCompiler::setSourceDevice(QIODevice *device, QShader::Stage
    #      stage, const QString &fileName)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler15setSourceDeviceEP9QIODeviceN7QShader5St'
        'ageERK7QString',
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
    Calls Qt's 'void QSpirvCompiler::setSourceString(const QByteArray
    &sourceString, QShader::Stage stage, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvcompiler.html#setSourceString

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
    #  void QSpirvCompiler::setSourceString(const QByteArray &sourceString,
    #      QShader::Stage stage, const QString &fileName)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler15setSourceStringERK10QByteArrayN7QShader'
        '5StageERK7QString',
        self._valueOf(sourceString), stage.value, fileName,
    )

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QSpirvCompiler::setFlags(Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvcompiler.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QSpirvCompiler::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler8setFlagsE6QFlagsINS_4FlagEE', flags.value,
    )

  @overload(QByteArray)
  def setPreamble(self, preamble: QByteArray) -> None:
    """
    Calls Qt's 'void QSpirvCompiler::setPreamble(const QByteArray
    &preamble)'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvcompiler.html#setPreamble

    Parameters
    ----------

    preamble : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSpirvCompiler::setPreamble(const QByteArray &preamble)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler11setPreambleERK10QByteArray',
        self._valueOf(preamble),
    )

  @overload(int)
  def setSGBatchingVertexInputLocation(self, location: int) -> None:
    """
    Calls Qt's 'void QSpirvCompiler::setSGBatchingVertexInputLocation(int
    location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvcompiler.html

    Parameters
    ----------

    location : int
      Passed on as it is.
    """
    #  void QSpirvCompiler::setSGBatchingVertexInputLocation(int location)
    self.uglySide.call(
        'ritual_ZN14QSpirvCompiler32setSGBatchingVertexInputLocationEi',
        location,
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
    Notes what was given, for Qt's 'QSpirvCompiler::QSpirvCompiler()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qspirvcompiler.html#QSpirvCompiler
    """
    #  QSpirvCompiler::QSpirvCompiler()
    self._noteCreation(QSpirvCompiler, lambda: Rituals.call(
        'ritual_ZN14QSpirvCompilerC1Ev',
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

  def compileToSpirv(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSpirvCompiler::compileToSpirv()'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvcompiler.html#compileToSpirv

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSpirvCompiler::compileToSpirv()
    address = self.uglySide.call(
        'ritual_ZN14QSpirvCompiler14compileToSpirvEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)
