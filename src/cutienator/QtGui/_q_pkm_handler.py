"""
QPkmHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpkmhandler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPkmHandler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextureFileHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QTextureFileData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QPkmHandler(QTextureFileHandler):
  """
  The cute side of Qt's QPkmHandler: a plain Python object standing in front
  of one C++ QPkmHandler.

  It is built on the cute 'QTextureFileHandler', as Qt's QPkmHandler is built
  on Qt's QTextureFileHandler, and has everything that class has.

  C++ hands a QPkmHandler around as a copy, so every C++ QPkmHandler behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPkmHandler that has a ritual and that Python can
  call so far, 2 names in all: 'canRead', 'read'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPkmHandler::~QPkmHandler()': the destructor: Python removes its
    C++ QPkmHandler by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPkmHandler is created at the first use, not by
    'QPkmHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPkmHandler back gives a copy the ritual made for
    Python, in a new cute QPkmHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QByteArray)
  def canRead(suffix: QByteArray, block: QByteArray) -> bool:
    """
    Calls Qt's 'bool QPkmHandler::canRead(const QByteArray &suffix, const
    QByteArray &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qpkmhandler.html#canRead

    Parameters
    ----------

    suffix : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    block : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QPkmHandler::canRead(const QByteArray &suffix, const QByteArray
    #      &block)
    return Rituals.call(
        'ritual_ZN11QPkmHandler7canReadERK10QByteArrayS2_',
        CuteMixin._valueOf(suffix), CuteMixin._valueOf(block),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPkmHandler'

  #  A C++ QPkmHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPkmHandler'

  #  Qt's '~QPkmHandler()'. Naming it makes this a value class: Python owns
  #  every C++ QPkmHandler behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QPkmHandlerD1Ev'

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
    Calls Qt's 'QTextureFileData QPkmHandler::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qpkmhandler.html#read

    Returns
    -------

    QTextureFileData
      A new cute QTextureFileData around the copy Qt gave back. Python owns
      it.
    """
    #  QTextureFileData QPkmHandler::read()
    address = self.uglySide.call('ritual_ZN11QPkmHandler4readEv')
    from . import QTextureFileData
    return QTextureFileData._cuteOwning(address)
