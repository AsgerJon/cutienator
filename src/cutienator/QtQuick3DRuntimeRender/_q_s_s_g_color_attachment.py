"""
QSSGColorAttachment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGColorAttachment to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSSGCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from ..QtQuick3DUtils import QSSGRenderTextureFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSSGColorAttachment(QSSGCommand):
  """
  The cute side of Qt's QSSGColorAttachment: a plain Python object standing
  in front of one C++ QSSGColorAttachment.

  It is built on the cute 'QSSGCommand', as Qt's QSSGColorAttachment is built
  on Qt's QSSGCommand, and has everything that class has.

  C++ hands a QSSGColorAttachment around as a copy, so every C++
  QSSGColorAttachment behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGColorAttachment that has a ritual and that
  Python can call so far, 1 name in all: 'format'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGColorAttachment::addDebug(QDebug &stream) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGColorAttachment::QSSGColorAttachment(const QByteArray &name,
    CommandType type)': names the enum 'CommandType', whose class cannot be
    named here.
  - Qt's 'QSSGColorAttachment::~QSSGColorAttachment()': the destructor:
    Python removes its C++ QSSGColorAttachment by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGColorAttachment is created at the first use, not by
    'QSSGColorAttachment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGColorAttachment back gives a copy the ritual made
    for Python, in a new cute QSSGColorAttachment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGColorAttachment'

  #  Qt's '~QSSGColorAttachment()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGColorAttachment behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGColorAttachmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QSSGRenderTextureFormat:
    """
    Calls Qt's 'QSSGRenderTextureFormat QSSGColorAttachment::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgcolorattachment.html#format

    Returns
    -------

    QSSGRenderTextureFormat
      A new cute QSSGRenderTextureFormat around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderTextureFormat QSSGColorAttachment::format() const
    address = self.uglySide.call('ritual_ZNK19QSSGColorAttachment6formatEv')
    from ..QtQuick3DUtils import QSSGRenderTextureFormat
    return QSSGRenderTextureFormat._cuteOwning(address)

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

  @overload(QByteArray)
  def __init__(self, name: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QSSGColorAttachment::QSSGColorAttachment(const QByteArray &name)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgcolorattachment.html#QSSGColorAttachment

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QSSGColorAttachment::QSSGColorAttachment(const QByteArray &name)
    self._noteCreation(QSSGColorAttachment, lambda: Rituals.call(
        'ritual_ZN19QSSGColorAttachmentC1ERK10QByteArray',
        self._valueOf(name),
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
