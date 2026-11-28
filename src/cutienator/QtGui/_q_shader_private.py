"""
QShaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qshader_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QShaderPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderPrivate: a plain Python object standing in
  front of one C++ QShaderPrivate.

  C++ hands a QShaderPrivate around as a copy, so every C++ QShaderPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShaderPrivate that has a ritual and that Python can
  call so far, 2 names in all: 'get', 'qtQsbVersion'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QShaderPrivate *QShaderPrivate::get(const QShader *s)': takes
    in Python what 'QShaderPrivate *QShaderPrivate::get(QShader *s)' takes.
  - Qt's 'bool QShaderPrivate::readCount(QDataStream *stream, int *count)':
    takes a number to change where it is.
  - Qt's 'QShaderPrivate::~QShaderPrivate()': the destructor: Python removes
    its C++ QShaderPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QShaderPrivate is created at the first use, not by
    'QShaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShaderPrivate back gives a copy the ritual made for
    Python, in a new cute QShaderPrivate.
  - Each name of Qt's QShaderPrivate that has no cute function yet,
    'readCount', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QShaderPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class MslNativeShaderInfoExtraBufferBindings(CuteNum):
    """
    The enum 'QShaderPrivate::MslNativeShaderInfoExtraBufferBindings' of Qt,
    with the 8 names Qt gives in it.
    """

    MslTessVertIndicesBufferBinding = Kee[int](0)
    MslTessVertTescOutputBufferBinding = Kee[int](1)
    MslTessTescTessLevelBufferBinding = Kee[int](2)
    MslTessTescPatchOutputBufferBinding = Kee[int](3)
    MslTessTescParamsBufferBinding = Kee[int](4)
    MslTessTescInputBufferBinding = Kee[int](5)
    MslBufferSizeBufferBinding = Kee[int](6)
    MslMultiViewMaskBufferBinding = Kee[int](7)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QShader)
  @overload(NoneType)
  def get(s: Optional[QShader]) -> Optional[QShaderPrivate]:
    """
    Calls Qt's 'QShaderPrivate *QShaderPrivate::get(QShader *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderprivate.html#get

    Parameters
    ----------

    s : Optional[QShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QShaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShaderPrivate *QShaderPrivate::get(QShader *s)
    address = Rituals.call(
        'ritual_ZN14QShaderPrivate3getEP7QShader', CuteMixin._addressOf(s),
    )
    return QShaderPrivate._cuteAt(address)

  @staticmethod
  @overload(QShader.SerializedFormatVersion)
  def qtQsbVersion(qtVersion: QShader.SerializedFormatVersion) -> int:
    """
    Calls Qt's 'int
    QShaderPrivate::qtQsbVersion(QShader::SerializedFormatVersion
    qtVersion)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderprivate.html#qtQsbVersion

    Parameters
    ----------

    qtVersion : QShader.SerializedFormatVersion
      Passed on as its number.
    """
    #  int QShaderPrivate::qtQsbVersion(QShader::SerializedFormatVersion
    #      qtVersion)
    return Rituals.call(
        'ritual_ZN14QShaderPrivate12qtQsbVersionEN7QShader23SerializedForma'
        'tVersionE',
        qtVersion.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderPrivate'

  #  Qt's '~QShaderPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QShaderPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QShaderPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QShaderPrivate::QShaderPrivate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderprivate.html#QShaderPrivate
    """
    #  QShaderPrivate::QShaderPrivate()
    self._noteCreation(QShaderPrivate, lambda: Rituals.call(
        'ritual_ZN14QShaderPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QShaderPrivate) -> None:
    """
    Notes what was given, for Qt's 'QShaderPrivate::QShaderPrivate(const
    QShaderPrivate &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderprivate.html#QShaderPrivate

    Parameters
    ----------

    other : QShaderPrivate
      Passed on as a value: Qt reads the C++ QShaderPrivate, which stays
      Python's own.
    """
    #  QShaderPrivate::QShaderPrivate(const QShaderPrivate &other)
    self._noteCreation(QShaderPrivate, lambda: Rituals.call(
        'ritual_ZN14QShaderPrivateC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def readCount(*__, **_) -> Never:
    """
    Qt's 'bool QShaderPrivate::readCount(QDataStream *stream, int *count)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QShaderPrivate.readCount' has no cute function yet. Qt's 'bool "
        "QShaderPrivate::readCount(QDataStream *stream, int *count)': takes "
        "a number to change where it is.")
