"""
QTextureFileHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtexturefilehandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextureFileHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice
  from . import QTextureFileData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureFileHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextureFileHandler: a plain Python object standing
  in front of one C++ QTextureFileHandler.

  What exists
  -----------

  Every function of Qt's QTextureFileHandler that has a ritual and that
  Python can call so far, 3 names in all: 'read', 'device', 'logName'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextureFileHandler::~QTextureFileHandler()': the destructor:
    Python never removes a C++ QTextureFileHandler.

  What to expect
  --------------

  - The C++ QTextureFileHandler is created at the first use, not by
    'QTextureFileHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextureFileHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextureFileHandler'

  #  A C++ QTextureFileHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextureFileHandler'

  #  The functions Qt calls itself that QTextureFileHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'read': (
          ('_ZN19QTextureFileHandler4readEv',
           ('address', 'value', 'QtGui:QTextureFileData'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QTextureFileHandler::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefilehandler.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QTextureFileHandler::device() const
    address = self.uglySide.call('ritual_ZNK19QTextureFileHandler6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def logName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextureFileHandler::logName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefilehandler.html#logName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextureFileHandler::logName() const
    address = self.uglySide.call('ritual_ZNK19QTextureFileHandler7logNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  def __init__(
      self,
      device: Optional[QIODevice],
      logName: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextureFileHandler::QTextureFileHandler(QIODevice *device, const
    QByteArray &logName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefilehandler.html#QTextureFileHandler

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    logName : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QTextureFileHandler::QTextureFileHandler(QIODevice *device, const
    #      QByteArray &logName)
    if logName is None:
      from ..QtCore import QByteArray
      logName = QByteArray()
    self._noteCreation(QTextureFileHandler, lambda: Rituals.call(
        'ritual_ZN19QTextureFileHandlerC1EP9QIODeviceRK10QByteArray',
        self._addressOf(device), self._valueOf(logName),
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

  def read(self) -> QTextureFileData:
    """
    Calls Qt's 'QTextureFileData QTextureFileHandler::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefilehandler.html#read

    Returns
    -------

    QTextureFileData
      A new cute QTextureFileData around the copy Qt gave back. Python owns
      it.
    """
    #  QTextureFileData QTextureFileHandler::read()
    address = self.uglySide.call('ritual_ZN19QTextureFileHandler4readEv')
    from . import QTextureFileData
    return QTextureFileData._cuteOwning(address)
