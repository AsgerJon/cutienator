"""
QSslKeyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsslkey_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSslKeyPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QTlsPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSslKeyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslKeyPrivate: a plain Python object standing in
  front of one C++ QSslKeyPrivate.

  What exists
  -----------

  Every function of Qt's QSslKeyPrivate that has a ritual and that Python can
  call so far, 2 names in all: 'decrypt', 'encrypt'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslKeyPrivate::~QSslKeyPrivate()': the destructor: Python never
    removes a C++ QSslKeyPrivate.

  What has no ritual
  ------------------

  5 of the 8 functions Qt declares: 4 forbidden; 1 leans on 'lcSsl()', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QSslKeyPrivate is created at the first use, not by
    'QSslKeyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSslKeyPrivate.
  - Each name of Qt's QSslKeyPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTlsPrivate.Cipher, QByteArray, QByteArray, QByteArray)
  def decrypt(
      cipher: QTlsPrivate.Cipher,
      data: QByteArray,
      key: QByteArray,
      iv: QByteArray,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKeyPrivate::decrypt(Cipher cipher, const
    QByteArray &data, const QByteArray &key, const QByteArray &iv)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyprivate.html#decrypt

    Parameters
    ----------

    cipher : QTlsPrivate.Cipher
      Passed on as its number.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    iv : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKeyPrivate::decrypt(Cipher cipher, const QByteArray
    #      &data, const QByteArray &key, const QByteArray &iv)
    address = Rituals.call(
        'ritual_ZN14QSslKeyPrivate7decryptEN11QTlsPrivate6CipherERK10QByteA'
        'rrayS4_S4_',
        cipher.value, CuteMixin._valueOf(data), CuteMixin._valueOf(key),
        CuteMixin._valueOf(iv),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QTlsPrivate.Cipher, QByteArray, QByteArray, QByteArray)
  def encrypt(
      cipher: QTlsPrivate.Cipher,
      data: QByteArray,
      key: QByteArray,
      iv: QByteArray,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKeyPrivate::encrypt(Cipher cipher, const
    QByteArray &data, const QByteArray &key, const QByteArray &iv)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyprivate.html#encrypt

    Parameters
    ----------

    cipher : QTlsPrivate.Cipher
      Passed on as its number.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    iv : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKeyPrivate::encrypt(Cipher cipher, const QByteArray
    #      &data, const QByteArray &key, const QByteArray &iv)
    address = Rituals.call(
        'ritual_ZN14QSslKeyPrivate7encryptEN11QTlsPrivate6CipherERK10QByteA'
        'rrayS4_S4_',
        cipher.value, CuteMixin._valueOf(data), CuteMixin._valueOf(key),
        CuteMixin._valueOf(iv),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslKeyPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSslKeyPrivate::QSslKeyPrivate()': leans on 'lcSsl()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSslKeyPrivate.__init__' has no cute function yet. Qt's "
        "'QSslKeyPrivate::QSslKeyPrivate()': leans on 'lcSsl()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
