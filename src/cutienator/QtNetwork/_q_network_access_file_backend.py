"""
QNetworkAccessFileBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QNetworkAccessFileBackend to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QNetworkAccessBackend

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QNetworkAccessFileBackend(QNetworkAccessBackend):
  """
  The cute side of Qt's QNetworkAccessFileBackend: a plain Python object
  standing in front of one C++ QNetworkAccessFileBackend.

  It is built on the cute 'QNetworkAccessBackend', as Qt's
  QNetworkAccessFileBackend is built on Qt's QNetworkAccessBackend, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessFileBackend that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'open', 'close',
  'bytesAvailable', 'uploadReadyReadSlot', 'loadFileInfo'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkAccessFileBackend::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QNetworkAccessFileBackend::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkAccessFileBackend::~QNetworkAccessFileBackend()': the
    destructor: Python never removes a C++ QNetworkAccessFileBackend.
  - Qt's 'qint64 QNetworkAccessFileBackend::read(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QNetworkAccessFileBackend.

  What to expect
  --------------

  - The C++ QNetworkAccessFileBackend is created at the first use, not by
    'QNetworkAccessFileBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessFileBackend.
  - Qt tells when it has removed the C++ QNetworkAccessFileBackend. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkAccessFileBackend that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessFileBackend'

  #  A C++ QNetworkAccessFileBackend Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessFileBackend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkAccessFileBackend::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkAccessFileBackend::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QNetworkAccessFileBackend10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkAccessFileBackend::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackend.html#bytesAvailable
    """
    #  qint64 QNetworkAccessFileBackend::bytesAvailable() const
    ritual = 'ritual_ZNK25QNetworkAccessFileBackend14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QNetworkAccessFileBackend14bytesAvailableEv'
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNetworkAccessFileBackend::QNetworkAccessFileBackend()': leans on
    'QNetworkAccessFileBackend::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessFileBackend.__init__' has no cute function yet. "
        "Qt's 'QNetworkAccessFileBackend::QNetworkAccessFileBackend()': "
        "leans on "
        "'QNetworkAccessFileBackend::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def open(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessFileBackend::open()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackend.html#open
    """
    #  void QNetworkAccessFileBackend::open()
    ritual = 'ritual_ZN25QNetworkAccessFileBackend4openEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QNetworkAccessFileBackend4openEv'
    self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessFileBackend::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackend.html#close
    """
    #  void QNetworkAccessFileBackend::close()
    ritual = 'ritual_ZN25QNetworkAccessFileBackend5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QNetworkAccessFileBackend5closeEv'
    self.uglySide.call(ritual)

  def uploadReadyReadSlot(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessFileBackend::uploadReadyReadSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackend.html#uploadReadyReadSlot
    """
    #  void QNetworkAccessFileBackend::uploadReadyReadSlot()
    self.uglySide.call(
        'ritual_ZN25QNetworkAccessFileBackend19uploadReadyReadSlotEv',
    )

  def loadFileInfo(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessFileBackend::loadFileInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackend.html#loadFileInfo
    """
    #  bool QNetworkAccessFileBackend::loadFileInfo()
    return self.uglySide.call(
        'ritual_ZN25QNetworkAccessFileBackend12loadFileInfoEv',
    )
