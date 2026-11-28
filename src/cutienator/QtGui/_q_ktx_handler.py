"""
QKtxHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qktxhandler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QKtxHandler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextureFileHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QTextureFileData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QKtxHandler(QTextureFileHandler):
  """
  The cute side of Qt's QKtxHandler: a plain Python object standing in front
  of one C++ QKtxHandler.

  It is built on the cute 'QTextureFileHandler', as Qt's QKtxHandler is built
  on Qt's QTextureFileHandler, and has everything that class has.

  C++ hands a QKtxHandler around as a copy, so every C++ QKtxHandler behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QKtxHandler that has a ritual and that Python can
  call so far, 3 names in all: 'canRead', 'read', 'decode'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKtxHandler::~QKtxHandler()': the destructor: Python removes its
    C++ QKtxHandler by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QKtxHandler is created at the first use, not by
    'QKtxHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QKtxHandler back gives a copy the ritual made for
    Python, in a new cute QKtxHandler.
  - Each name of Qt's QKtxHandler that has no cute function yet,
    'checkHeader', 'decodeKeyValues', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QByteArray)
  def canRead(suffix: QByteArray, block: QByteArray) -> bool:
    """
    Calls Qt's 'bool QKtxHandler::canRead(const QByteArray &suffix, const
    QByteArray &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qktxhandler.html#canRead

    Parameters
    ----------

    suffix : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    block : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QKtxHandler::canRead(const QByteArray &suffix, const QByteArray
    #      &block)
    return Rituals.call(
        'ritual_ZN11QKtxHandler7canReadERK10QByteArrayS2_',
        CuteMixin._valueOf(suffix), CuteMixin._valueOf(block),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKtxHandler'

  #  A C++ QKtxHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QKtxHandler'

  #  Qt's '~QKtxHandler()'. Naming it makes this a value class: Python owns
  #  every C++ QKtxHandler behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QKtxHandlerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def decode(self, val: int) -> int:
    """
    Calls Qt's 'quint32 QKtxHandler::decode(quint32 val) const'.

    Qt's own words: https://doc.qt.io/qt-6/qktxhandler.html#decode

    Parameters
    ----------

    val : int
      Passed on as it is.
    """
    #  quint32 QKtxHandler::decode(quint32 val) const
    return self.uglySide.call('ritual_ZNK11QKtxHandler6decodeEj', val)

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
    Calls Qt's 'QTextureFileData QKtxHandler::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qktxhandler.html#read

    Returns
    -------

    QTextureFileData
      A new cute QTextureFileData around the copy Qt gave back. Python owns
      it.
    """
    #  QTextureFileData QKtxHandler::read()
    address = self.uglySide.call('ritual_ZN11QKtxHandler4readEv')
    from . import QTextureFileData
    return QTextureFileData._cuteOwning(address)

  @staticmethod
  def checkHeader(*__, **_) -> Never:
    """
    Qt's 'bool QKtxHandler::checkHeader(const KTXHeader &header)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    KTXHeader'.
    """
    raise NotImplementedError(
        "'QKtxHandler.checkHeader' has no cute function yet. Qt's 'bool "
        "QKtxHandler::checkHeader(const KTXHeader &header)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "KTXHeader'.")

  @staticmethod
  def decodeKeyValues(*__, **_) -> Never:
    """
    Qt's 'std::optional<QMap<QByteArray, QByteArray>>
    QKtxHandler::decodeKeyValues(QByteArrayView view) const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'safeView'.
    """
    raise NotImplementedError(
        "'QKtxHandler.decodeKeyValues' has no cute function yet. Qt's "
        "'std::optional<QMap<QByteArray, QByteArray>> "
        "QKtxHandler::decodeKeyValues(QByteArrayView view) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'safeView'.")
