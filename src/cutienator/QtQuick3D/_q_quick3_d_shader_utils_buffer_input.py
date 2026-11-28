"""
QQuick3DShaderUtilsBufferInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsBufferInput to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DShaderUtilsRenderCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGCommand
  from . import QQuick3DShaderUtilsBuffer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DShaderUtilsBuffer = WAIT['QQuick3DShaderUtilsBuffer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsBufferInput(QQuick3DShaderUtilsRenderCommand):
  """
  The cute side of Qt's QQuick3DShaderUtilsBufferInput: a plain Python object
  standing in front of one C++ QQuick3DShaderUtilsBufferInput.

  It is built on the cute 'QQuick3DShaderUtilsRenderCommand', as Qt's
  QQuick3DShaderUtilsBufferInput is built on Qt's
  QQuick3DShaderUtilsRenderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsBufferInput that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'cloneCommand', 'bufferCount', 'bufferAt', 'buffer', 'setBuffer'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsBufferInput::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DShaderUtilsBufferInput::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsBufferInput::~QQuick3DShaderUtilsBufferInput()':
    the destructor: Python never removes a C++
    QQuick3DShaderUtilsBufferInput.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsBufferInput is created at the first use, not
    by 'QQuick3DShaderUtilsBufferInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsBufferInput.
  - Qt tells when it has removed the C++ QQuick3DShaderUtilsBufferInput.
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
    Calls Qt's 'QString QQuick3DShaderUtilsBufferInput::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#tr

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
    #  QString QQuick3DShaderUtilsBufferInput::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QQuick3DShaderUtilsBufferInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsBufferInput'

  #  A C++ QQuick3DShaderUtilsBufferInput Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsBufferInput'

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
    *QQuick3DShaderUtilsBufferInput::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DShaderUtilsBufferInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DShaderUtilsBufferInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bufferCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DShaderUtilsBufferInput::bufferCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#bufferCount
    """
    #  int QQuick3DShaderUtilsBufferInput::bufferCount() const
    ritual = 'ritual_ZNK30QQuick3DShaderUtilsBufferInput11bufferCountEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuick3DShaderUtilsBufferInput11bufferCountEv')
    return self.uglySide.call(ritual)

  @overload(int)
  def bufferAt(self, idx: int) -> Optional[QQuick3DShaderUtilsBuffer]:
    """
    Calls Qt's 'QQuick3DShaderUtilsBuffer
    *QQuick3DShaderUtilsBufferInput::bufferAt(int idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#bufferAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuick3DShaderUtilsBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DShaderUtilsBuffer
    #      *QQuick3DShaderUtilsBufferInput::bufferAt(int idx) const
    ritual = 'ritual_ZNK30QQuick3DShaderUtilsBufferInput8bufferAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QQuick3DShaderUtilsBufferInput8bufferAtEi'
    address = self.uglySide.call(ritual, idx)
    from . import QQuick3DShaderUtilsBuffer
    return QQuick3DShaderUtilsBuffer._cuteAt(address)

  def buffer(self) -> Optional[QQuick3DShaderUtilsBuffer]:
    """
    Calls Qt's 'QQuick3DShaderUtilsBuffer
    *QQuick3DShaderUtilsBufferInput::buffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#buffer

    Returns
    -------

    Optional[QQuick3DShaderUtilsBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DShaderUtilsBuffer *QQuick3DShaderUtilsBufferInput::buffer()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DShaderUtilsBufferInput6bufferEv',
    )
    from . import QQuick3DShaderUtilsBuffer
    return QQuick3DShaderUtilsBuffer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DShaderUtilsBuffer)
  @overload(NoneType)
  def setBuffer(self, buffer: Optional[QQuick3DShaderUtilsBuffer]) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsBufferInput::setBuffer(QQuick3DShaderUtilsBuffer
    *buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#setBuffer

    Parameters
    ----------

    buffer : Optional[QQuick3DShaderUtilsBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DShaderUtilsBufferInput::setBuffer(
    #      QQuick3DShaderUtilsBuffer *buffer)
    self.uglySide.call(
        'ritual_ZN30QQuick3DShaderUtilsBufferInput9setBufferEP25QQuick3DSha'
        'derUtilsBuffer',
        self._addressOf(buffer),
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
    'QQuick3DShaderUtilsBufferInput::QQuick3DShaderUtilsBufferInput()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html
    """
    #  QQuick3DShaderUtilsBufferInput::QQuick3DShaderUtilsBufferInput()
    self._noteCreation(QQuick3DShaderUtilsBufferInput, lambda: Rituals.call(
        'ritual_ZN30QQuick3DShaderUtilsBufferInputC1Ev',
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

  def cloneCommand(self) -> Optional[QSSGCommand]:
    """
    Calls Qt's 'QSSGCommand *QQuick3DShaderUtilsBufferInput::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbufferinput.html#cloneCommand

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsBufferInput::cloneCommand()
    ritual = 'ritual_ZN30QQuick3DShaderUtilsBufferInput12cloneCommandEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DShaderUtilsBufferInput12cloneCommandEv')
    address = self.uglySide.call(ritual)
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)
