"""
QSSGShaderKeyTextureChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyTextureChannel to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyTextureChannel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyTextureChannel: a plain Python object
  standing in front of one C++ QSSGShaderKeyTextureChannel.

  C++ hands a QSSGShaderKeyTextureChannel around as a copy, so every C++
  QSSGShaderKeyTextureChannel behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGShaderKeyTextureChannel yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TexturChannelBits
    QSSGShaderKeyTextureChannel::getTextureChannel(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSSGShaderKeyTextureChannel::setTextureChannel(TexturChannelBits channel,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QSSGShaderKeyTextureChannel::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyTextureChannel::fromString(const QByteArray
    &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGShaderKeyTextureChannel::~QSSGShaderKeyTextureChannel()': the
    destructor: Python removes its C++ QSSGShaderKeyTextureChannel by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyTextureChannel is created at the first use, not by
    'QSSGShaderKeyTextureChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyTextureChannel back gives a copy the
    ritual made for Python, in a new cute QSSGShaderKeyTextureChannel.
  - Each name of Qt's QSSGShaderKeyTextureChannel that has no cute function
    yet, 'fromString', 'getTextureChannel', 'setTextureChannel', 'toString',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSSGShaderKeyTextureChannel, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class TexturChannelBits(CuteNum):
    """
    The enum 'QSSGShaderKeyTextureChannel::TexturChannelBits' of Qt, with the
    4 names Qt gives in it.
    """

    R = Kee[int](0)
    G = Kee[int](1)
    B = Kee[int](2)
    A = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyTextureChannel'

  #  Qt's '~QSSGShaderKeyTextureChannel()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGShaderKeyTextureChannel behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGShaderKeyTextureChannelD1Ev'

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

  @overload(str)
  @overload(NoneType)
  def __init__(self, inName: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderKeyTextureChannel::QSSGShaderKeyTextureChannel(const char
    *inName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeytexturechannel.html

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyTextureChannel::QSSGShaderKeyTextureChannel(const char
    #      *inName)
    self._noteCreation(QSSGShaderKeyTextureChannel, lambda: Rituals.call(
        'ritual_ZN27QSSGShaderKeyTextureChannelC1EPKc',
        self._bytesOf(inName),
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
  def fromString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyTextureChannel::fromString(const QByteArray
    &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyTextureChannel.fromString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyTextureChannel::fromString(const "
        "QByteArray &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getTextureChannel(*__, **_) -> Never:
    """
    Qt's 'TexturChannelBits
    QSSGShaderKeyTextureChannel::getTextureChannel(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyTextureChannel.getTextureChannel' has no cute "
        "function yet. Qt's 'TexturChannelBits "
        "QSSGShaderKeyTextureChannel::getTextureChannel(QSSGDataView<quint32"
        "> inKeySet) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setTextureChannel(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderKeyTextureChannel::setTextureChannel(TexturChannelBits channel,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyTextureChannel.setTextureChannel' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderKeyTextureChannel::setTextureChannel(TexturChannelBits "
        "channel, QSSGDataRef<quint32> inKeySet)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyTextureChannel::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyTextureChannel.toString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyTextureChannel::toString(QByteArray "
        "&ioStr, QSSGDataView<quint32> inKeySet) const': takes a type "
        "Python has no way to hand over yet.")
