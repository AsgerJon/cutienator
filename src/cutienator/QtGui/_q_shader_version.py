"""
QShaderVersion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QShaderVersion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderVersion: a plain Python object standing in
  front of one C++ QShaderVersion.

  C++ hands a QShaderVersion around as a copy, so every C++ QShaderVersion
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShaderVersion that has a ritual and that Python can
  call so far, 4 names in all: 'version', 'setVersion', 'flags', 'setFlags'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShaderVersion::~QShaderVersion()': the destructor: Python removes
    its C++ QShaderVersion by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QShaderVersion is created at the first use, not by
    'QShaderVersion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShaderVersion back gives a copy the ritual made for
    Python, in a new cute QShaderVersion.
  """

  #  The enums Qt writes inside QShaderVersion, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QShaderVersion::Flag' of Qt, with the 1 names Qt gives in
    it. Qt names the type of its combinations 'QShaderVersion::Flags'.
    """

    GlslEs = 0x1

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderVersion'

  #  Qt's '~QShaderVersion()'. Naming it makes this a value class: Python
  #  owns every C++ QShaderVersion behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QShaderVersionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def version(self) -> int:
    """
    Calls Qt's 'int QShaderVersion::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderversion.html#version
    """
    #  int QShaderVersion::version() const
    return self.uglySide.call('ritual_ZNK14QShaderVersion7versionEv')

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QShaderVersion::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderversion.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QShaderVersion::flags() const
    return QShaderVersion.Flags(self.uglySide.call(
        'ritual_ZNK14QShaderVersion5flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setVersion(self, v: int) -> None:
    """
    Calls Qt's 'void QShaderVersion::setVersion(int v)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderversion.html#setVersion

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  void QShaderVersion::setVersion(int v)
    self.uglySide.call('ritual_ZN14QShaderVersion10setVersionEi', v)

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QShaderVersion::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderversion.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QShaderVersion::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN14QShaderVersion8setFlagsE6QFlagsINS_4FlagEE', f.value,
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
    Notes what was given, for Qt's 'QShaderVersion::QShaderVersion()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderversion.html#QShaderVersion
    """
    #  QShaderVersion::QShaderVersion()
    self._noteCreation(QShaderVersion, lambda: Rituals.call(
        'ritual_ZN14QShaderVersionC1Ev',
    ))

  @overload(int)
  @overload(int, Flags)
  def __init__(self, v: int, f: Flags = Flags()) -> None:
    """
    Notes what was given, for Qt's 'QShaderVersion::QShaderVersion(int v,
    Flags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderversion.html#QShaderVersion

    Parameters
    ----------

    v : int
      Passed on as it is.

    f : Flags
      Passed on as its number. May be left out, as in Qt: it is then Flags().
    """
    #  QShaderVersion::QShaderVersion(int v, Flags f)
    self._noteCreation(QShaderVersion, lambda: Rituals.call(
        'ritual_ZN14QShaderVersionC1Ei6QFlagsINS_4FlagEE', v, f.value,
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


#  Qt's 'QList<QShaderVersion>': the list of QShaderVersion, which
#  'QList[QShaderVersion]' gives. It is made here, so that there is one as
#  soon as there can be a QShaderVersion.
QList.createKind(
    QShaderVersion, 'value',
    make='ritual_list_make_QShaderVersion',
    add='ritual_list_add_QShaderVersion',
    size='ritual_list_size_QShaderVersion',
    at='ritual_list_at_QShaderVersion',
    drop='ritual_list_drop_QShaderVersion',
)
