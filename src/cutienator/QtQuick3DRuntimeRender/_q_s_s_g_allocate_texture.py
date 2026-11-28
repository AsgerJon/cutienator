"""
QSSGAllocateTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAllocateTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSSGCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtQuick3DUtils import QSSGRenderTextureFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderTextureFormat = WAIT['QSSGRenderTextureFormat']


class QSSGAllocateTexture(QSSGCommand):
  """
  The cute side of Qt's QSSGAllocateTexture: a plain Python object standing
  in front of one C++ QSSGAllocateTexture.

  It is built on the cute 'QSSGCommand', as Qt's QSSGAllocateTexture is built
  on Qt's QSSGCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGAllocateTexture that has a ritual and that
  Python can call so far, 2 names in all: 'format', 'setFormat'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSSGManagedRhiTexturePtr &QSSGAllocateTexture::texture()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QSSGAllocateTexture::setTexture(const QSSGManagedRhiTexturePtr
    &tex)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGAllocateTexture::addDebug(QDebug &stream) const': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSSGAllocateTexture is created at the first use, not by
    'QSSGAllocateTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGAllocateTexture.
  - Each name of Qt's QSSGAllocateTexture that has no cute function yet,
    'setTexture', 'texture', holds a function that raises
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
  __qt_class__ = 'QSSGAllocateTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QSSGRenderTextureFormat:
    """
    Calls Qt's 'QSSGRenderTextureFormat QSSGAllocateTexture::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgallocatetexture.html#format

    Returns
    -------

    QSSGRenderTextureFormat
      A new cute QSSGRenderTextureFormat around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderTextureFormat QSSGAllocateTexture::format() const
    address = self.uglySide.call('ritual_ZNK19QSSGAllocateTexture6formatEv')
    from ..QtQuick3DUtils import QSSGRenderTextureFormat
    return QSSGRenderTextureFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGRenderTextureFormat)
  def setFormat(self, format: QSSGRenderTextureFormat) -> None:
    """
    Calls Qt's 'void QSSGAllocateTexture::setFormat(QSSGRenderTextureFormat
    format)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgallocatetexture.html#setFormat

    Parameters
    ----------

    format : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.
    """
    #  void QSSGAllocateTexture::setFormat(QSSGRenderTextureFormat format)
    self.uglySide.call(
        'ritual_ZN19QSSGAllocateTexture9setFormatE23QSSGRenderTextureFormat',
        self._valueOf(format),
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
    Notes what was given, for Qt's
    'QSSGAllocateTexture::QSSGAllocateTexture()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatetexture.html#QSSGAllocateTexture
    """
    #  QSSGAllocateTexture::QSSGAllocateTexture()
    self._noteCreation(QSSGAllocateTexture, lambda: Rituals.call(
        'ritual_ZN19QSSGAllocateTextureC1Ev',
    ))

  @overload(QSSGRenderTextureFormat)
  def __init__(self, inFormat: QSSGRenderTextureFormat) -> None:
    """
    Notes what was given, for Qt's
    'QSSGAllocateTexture::QSSGAllocateTexture(QSSGRenderTextureFormat
    inFormat)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatetexture.html#QSSGAllocateTexture

    Parameters
    ----------

    inFormat : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.
    """
    #  QSSGAllocateTexture::QSSGAllocateTexture(QSSGRenderTextureFormat
    #      inFormat)
    self._noteCreation(QSSGAllocateTexture, lambda: Rituals.call(
        'ritual_ZN19QSSGAllocateTextureC1E23QSSGRenderTextureFormat',
        self._valueOf(inFormat),
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
  def setTexture(*__, **_) -> Never:
    """
    Qt's 'void QSSGAllocateTexture::setTexture(const QSSGManagedRhiTexturePtr
    &tex)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGAllocateTexture.setTexture' has no cute function yet. Qt's "
        "'void QSSGAllocateTexture::setTexture(const "
        "QSSGManagedRhiTexturePtr &tex)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def texture(*__, **_) -> Never:
    """
    Qt's 'const QSSGManagedRhiTexturePtr &QSSGAllocateTexture::texture()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGAllocateTexture.texture' has no cute function yet. Qt's "
        "'const QSSGManagedRhiTexturePtr &QSSGAllocateTexture::texture() "
        "const': gives a type Python has no way to take yet.")
