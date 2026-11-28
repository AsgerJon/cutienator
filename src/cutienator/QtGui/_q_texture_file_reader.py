"""
QTextureFileReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtexturefilereader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextureFileReader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice
  from . import QTextureFileData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureFileReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextureFileReader: a plain Python object standing in
  front of one C++ QTextureFileReader.

  C++ hands a QTextureFileReader around as a copy, so every C++
  QTextureFileReader behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextureFileReader that has a ritual and that Python
  can call so far, 4 names in all: 'canRead', 'read', 'supportedFileFormats',
  'init'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextureFileReader::~QTextureFileReader()': the destructor: Python
    removes its C++ QTextureFileReader by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextureFileReader is created at the first use, not by
    'QTextureFileReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextureFileReader back gives a copy the ritual made
    for Python, in a new cute QTextureFileReader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def supportedFileFormats() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QTextureFileReader::supportedFileFormats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefilereader.html#supportedFileFormats

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QTextureFileReader::supportedFileFormats()
    address = Rituals.call(
        'ritual_ZN18QTextureFileReader20supportedFileFormatsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextureFileReader'

  #  Qt's '~QTextureFileReader()'. Naming it makes this a value class: Python
  #  owns every C++ QTextureFileReader behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QTextureFileReaderD1Ev'

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
    'QTextureFileReader::QTextureFileReader(QIODevice *device, const QString
    &fileName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefilereader.html#QTextureFileReader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QTextureFileReader::QTextureFileReader(QIODevice *device, const
    #      QString &fileName)
    self._noteCreation(QTextureFileReader, lambda: Rituals.call(
        'ritual_ZN18QTextureFileReaderC1EP9QIODeviceRK7QString',
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

  def canRead(self) -> bool:
    """
    Calls Qt's 'bool QTextureFileReader::canRead()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefilereader.html#canRead
    """
    #  bool QTextureFileReader::canRead()
    return self.uglySide.call('ritual_ZN18QTextureFileReader7canReadEv')

  def read(self) -> QTextureFileData:
    """
    Calls Qt's 'QTextureFileData QTextureFileReader::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefilereader.html#read

    Returns
    -------

    QTextureFileData
      A new cute QTextureFileData around the copy Qt gave back. Python owns
      it.
    """
    #  QTextureFileData QTextureFileReader::read()
    address = self.uglySide.call('ritual_ZN18QTextureFileReader4readEv')
    from . import QTextureFileData
    return QTextureFileData._cuteOwning(address)

  def init(self) -> bool:
    """
    Calls Qt's 'bool QTextureFileReader::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefilereader.html#init
    """
    #  bool QTextureFileReader::init()
    return self.uglySide.call('ritual_ZN18QTextureFileReader4initEv')
