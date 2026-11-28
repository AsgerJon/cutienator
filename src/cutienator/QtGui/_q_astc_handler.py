"""
QAstcHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qastchandler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QAstcHandler to be private: it declares the class in a header it
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


class QAstcHandler(QTextureFileHandler):
  """
  The cute side of Qt's QAstcHandler: a plain Python object standing in front
  of one C++ QAstcHandler.

  It is built on the cute 'QTextureFileHandler', as Qt's QAstcHandler is
  built on Qt's QTextureFileHandler, and has everything that class has.

  C++ hands a QAstcHandler around as a copy, so every C++ QAstcHandler behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAstcHandler that has a ritual and that Python can
  call so far, 3 names in all: 'canRead', 'read', 'astcGLFormat'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAstcHandler::~QAstcHandler()': the destructor: Python removes its
    C++ QAstcHandler by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QAstcHandler is created at the first use, not by
    'QAstcHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAstcHandler back gives a copy the ritual made for
    Python, in a new cute QAstcHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QByteArray)
  def canRead(suffix: QByteArray, block: QByteArray) -> bool:
    """
    Calls Qt's 'bool QAstcHandler::canRead(const QByteArray &suffix, const
    QByteArray &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qastchandler.html#canRead

    Parameters
    ----------

    suffix : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    block : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QAstcHandler::canRead(const QByteArray &suffix, const QByteArray
    #      &block)
    return Rituals.call(
        'ritual_ZN12QAstcHandler7canReadERK10QByteArrayS2_',
        CuteMixin._valueOf(suffix), CuteMixin._valueOf(block),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAstcHandler'

  #  A C++ QAstcHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAstcHandler'

  #  Qt's '~QAstcHandler()'. Naming it makes this a value class: Python owns
  #  every C++ QAstcHandler behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QAstcHandlerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def astcGLFormat(self, xBlockDim: int, yBlockDim: int) -> int:
    """
    Calls Qt's 'quint32 QAstcHandler::astcGLFormat(quint8 xBlockDim, quint8
    yBlockDim) const'.

    Qt's own words: https://doc.qt.io/qt-6/qastchandler.html#astcGLFormat

    Parameters
    ----------

    xBlockDim : int
      Passed on as it is.

    yBlockDim : int
      Passed on as it is.
    """
    #  quint32 QAstcHandler::astcGLFormat(quint8 xBlockDim, quint8 yBlockDim)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QAstcHandler12astcGLFormatEhh', xBlockDim, yBlockDim,
    )

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
    Calls Qt's 'QTextureFileData QAstcHandler::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qastchandler.html#read

    Returns
    -------

    QTextureFileData
      A new cute QTextureFileData around the copy Qt gave back. Python owns
      it.
    """
    #  QTextureFileData QAstcHandler::read()
    address = self.uglySide.call('ritual_ZN12QAstcHandler4readEv')
    from . import QTextureFileData
    return QTextureFileData._cuteOwning(address)
