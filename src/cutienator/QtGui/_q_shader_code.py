"""
QShaderCode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QShaderCode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderCode: a plain Python object standing in front
  of one C++ QShaderCode.

  C++ hands a QShaderCode around as a copy, so every C++ QShaderCode behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShaderCode that has a ritual and that Python can
  call so far, 4 names in all: 'shader', 'setShader', 'entryPoint',
  'setEntryPoint'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShaderCode::~QShaderCode()': the destructor: Python removes its
    C++ QShaderCode by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QShaderCode is created at the first use, not by
    'QShaderCode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShaderCode back gives a copy the ritual made for
    Python, in a new cute QShaderCode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderCode'

  #  Qt's '~QShaderCode()'. Naming it makes this a value class: Python owns
  #  every C++ QShaderCode behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QShaderCodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shader(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QShaderCode::shader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshadercode.html#shader

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QShaderCode::shader() const
    address = self.uglySide.call('ritual_ZNK11QShaderCode6shaderEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def entryPoint(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QShaderCode::entryPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshadercode.html#entryPoint

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QShaderCode::entryPoint() const
    address = self.uglySide.call('ritual_ZNK11QShaderCode10entryPointEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setShader(self, code: QByteArray) -> None:
    """
    Calls Qt's 'void QShaderCode::setShader(const QByteArray &code)'.

    Qt's own words: https://doc.qt.io/qt-6/qshadercode.html#setShader

    Parameters
    ----------

    code : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QShaderCode::setShader(const QByteArray &code)
    self.uglySide.call(
        'ritual_ZN11QShaderCode9setShaderERK10QByteArray',
        self._valueOf(code),
    )

  @overload(QByteArray)
  def setEntryPoint(self, entry: QByteArray) -> None:
    """
    Calls Qt's 'void QShaderCode::setEntryPoint(const QByteArray &entry)'.

    Qt's own words: https://doc.qt.io/qt-6/qshadercode.html#setEntryPoint

    Parameters
    ----------

    entry : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QShaderCode::setEntryPoint(const QByteArray &entry)
    self.uglySide.call(
        'ritual_ZN11QShaderCode13setEntryPointERK10QByteArray',
        self._valueOf(entry),
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
    Notes what was given, for Qt's 'QShaderCode::QShaderCode()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshadercode.html#QShaderCode
    """
    #  QShaderCode::QShaderCode()
    self._noteCreation(QShaderCode, lambda: Rituals.call(
        'ritual_ZN11QShaderCodeC1Ev',
    ))

  @overload(QByteArray)
  @overload(QByteArray, QByteArray)
  def __init__(
      self,
      code: QByteArray,
      entry: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QShaderCode::QShaderCode(const QByteArray
    &code, const QByteArray &entry)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshadercode.html#QShaderCode

    Parameters
    ----------

    code : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    entry : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QShaderCode::QShaderCode(const QByteArray &code, const QByteArray
    #      &entry)
    if entry is None:
      from ..QtCore import QByteArray
      entry = QByteArray()
    self._noteCreation(QShaderCode, lambda: Rituals.call(
        'ritual_ZN11QShaderCodeC1ERK10QByteArrayS2_',
        self._valueOf(code), self._valueOf(entry),
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
