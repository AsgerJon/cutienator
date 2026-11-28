"""
QSGTextureReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgtexturereader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGTextureReader to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice
  from . import QQuickTextureFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGTextureReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGTextureReader: a plain Python object standing in
  front of one C++ QSGTextureReader.

  C++ hands a QSGTextureReader around as a copy, so every C++
  QSGTextureReader behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGTextureReader that has a ritual and that Python
  can call so far, 3 names in all: 'read', 'isTexture',
  'supportedFileFormats'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGTextureReader::~QSGTextureReader()': the destructor: Python
    removes its C++ QSGTextureReader by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGTextureReader is created at the first use, not by
    'QSGTextureReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGTextureReader back gives a copy the ritual made
    for Python, in a new cute QSGTextureReader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def supportedFileFormats() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSGTextureReader::supportedFileFormats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexturereader.html#supportedFileFormats

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSGTextureReader::supportedFileFormats()
    address = Rituals.call(
        'ritual_ZN16QSGTextureReader20supportedFileFormatsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTextureReader'

  #  Qt's '~QSGTextureReader()'. Naming it makes this a value class: Python
  #  owns every C++ QSGTextureReader behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGTextureReaderD1Ev'

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

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, str)
  @overload(NoneType, str)
  def __init__(
      self,
      device: Optional[QIODevice],
      fileName: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSGTextureReader::QSGTextureReader(QIODevice *device, const QString
    &fileName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtexturereader.html#QSGTextureReader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSGTextureReader::QSGTextureReader(QIODevice *device, const QString
    #      &fileName)
    self._noteCreation(QSGTextureReader, lambda: Rituals.call(
        'ritual_ZN16QSGTextureReaderC1EP9QIODeviceRK7QString',
        self._addressOf(device), fileName,
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

  def read(self) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory *QSGTextureReader::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexturereader.html#read

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory *QSGTextureReader::read()
    address = self.uglySide.call('ritual_ZN16QSGTextureReader4readEv')
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  def isTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGTextureReader::isTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtexturereader.html#isTexture
    """
    #  bool QSGTextureReader::isTexture()
    return self.uglySide.call('ritual_ZN16QSGTextureReader9isTextureEv')
