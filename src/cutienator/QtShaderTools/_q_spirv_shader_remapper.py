"""
QSpirvShaderRemapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtShaderTools/6.12.0/QtShaderTools/private/qspirvshaderremap_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSpirvShaderRemapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QSpirvShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSpirvShaderRemapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSpirvShaderRemapper: a plain Python object standing
  in front of one C++ QSpirvShaderRemapper.

  C++ hands a QSpirvShaderRemapper around as a copy, so every C++
  QSpirvShaderRemapper behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSpirvShaderRemapper that has a ritual and that
  Python can call so far, 2 names in all: 'remap', 'errorMessage'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSpirvShaderRemapper::remapErrorHandler(const std::string
    &s)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSpirvShaderRemapper::remapLogHandler(const std::string &s)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSpirvShaderRemapper::~QSpirvShaderRemapper()': the destructor:
    Python removes its C++ QSpirvShaderRemapper by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSpirvShaderRemapper is created at the first use, not by
    'QSpirvShaderRemapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSpirvShaderRemapper back gives a copy the ritual
    made for Python, in a new cute QSpirvShaderRemapper.
  - Each name of Qt's QSpirvShaderRemapper that has no cute function yet,
    'remapErrorHandler', 'remapLogHandler', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpirvShaderRemapper'

  #  Qt's '~QSpirvShaderRemapper()'. Naming it makes this a value class:
  #  Python owns every C++ QSpirvShaderRemapper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSpirvShaderRemapperD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorMessage(self) -> str:
    """
    Calls Qt's 'QString QSpirvShaderRemapper::errorMessage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspirvshaderremapper.html#errorMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSpirvShaderRemapper::errorMessage() const
    return self.uglySide.call(
        'ritual_ZNK20QSpirvShaderRemapper12errorMessageEv',
    )

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

  @overload(QByteArray, QSpirvShader.RemapFlags)
  def remap(
      self,
      ir: QByteArray,
      flags: QSpirvShader.RemapFlags,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSpirvShaderRemapper::remap(const QByteArray &ir,
    QSpirvShader::RemapFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qspirvshaderremapper.html#remap

    Parameters
    ----------

    ir : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    flags : QSpirvShader.RemapFlags
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSpirvShaderRemapper::remap(const QByteArray &ir,
    #      QSpirvShader::RemapFlags flags)
    address = self.uglySide.call(
        'ritual_ZN20QSpirvShaderRemapper5remapERK10QByteArray6QFlagsIN12QSp'
        'irvShader9RemapFlagEE',
        self._valueOf(ir), flags.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def remapErrorHandler(*__, **_) -> Never:
    """
    Qt's 'void QSpirvShaderRemapper::remapErrorHandler(const std::string
    &s)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSpirvShaderRemapper.remapErrorHandler' has no cute function yet. "
        "Qt's 'void QSpirvShaderRemapper::remapErrorHandler(const "
        "std::string &s)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def remapLogHandler(*__, **_) -> Never:
    """
    Qt's 'void QSpirvShaderRemapper::remapLogHandler(const std::string &s)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSpirvShaderRemapper.remapLogHandler' has no cute function yet. "
        "Qt's 'void QSpirvShaderRemapper::remapLogHandler(const std::string "
        "&s)': takes a type Python has no way to hand over yet.")
