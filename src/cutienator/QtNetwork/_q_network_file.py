"""
QNetworkFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkfile_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QNetworkFile to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QFile
from . import QHttpHeaders, QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QNetworkFile(QFile):
  """
  The cute side of Qt's QNetworkFile: a plain Python object standing in front
  of one C++ QNetworkFile.

  It is built on the cute 'QFile', as Qt's QNetworkFile is built on Qt's
  QFile, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkFile that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'open', 'close', 'finished',
  'headerRead', 'networkError'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkFile::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QNetworkFile::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 leans on 'QNetworkFile; 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkFile is created at the first use, not by
    'QNetworkFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkFile.
  - Qt tells when it has removed the C++ QNetworkFile. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QNetworkFile that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkFile'

  #  A C++ QNetworkFile Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkFile::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkfile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkFile::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QNetworkFile10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    - Qt's 'QNetworkFile::QNetworkFile()': leans on
      'QNetworkFile::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'QNetworkFile::QNetworkFile(const QString &name)': leans on
      'QNetworkFile::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QNetworkFile.__init__' has no cute function yet. Qt's "
        "'QNetworkFile::QNetworkFile()': leans on "
        "'QNetworkFile::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'QNetworkFile::QNetworkFile(const "
        "QString &name)': leans on "
        "'QNetworkFile::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void QNetworkFile::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkfile.html#open
    """
    #  void QNetworkFile::open()
    self.uglySide.call('ritual_ZN12QNetworkFile4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkFile::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkfile.html#close
    """
    #  void QNetworkFile::close()
    ritual = 'ritual_ZN12QNetworkFile5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QNetworkFile5closeEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def finished(self, ok: bool) -> None:
    """
    Calls Qt's 'void QNetworkFile::finished(bool ok)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkfile.html#finished

    Parameters
    ----------

    ok : bool
      Passed on as it is.
    """
    #  void QNetworkFile::finished(bool ok)
    self.uglySide.call('ritual_ZN12QNetworkFile8finishedEb', ok)

  @overload(QHttpHeaders.WellKnownHeader, QByteArray)
  def headerRead(
      self,
      a0: QHttpHeaders.WellKnownHeader,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QNetworkFile::headerRead(QHttpHeaders::WellKnownHeader
    a0, const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkfile.html#headerRead

    Parameters
    ----------

    a0 : QHttpHeaders.WellKnownHeader
      Passed on as its number.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkFile::headerRead(QHttpHeaders::WellKnownHeader a0, const
    #      QByteArray &value)
    self.uglySide.call(
        'ritual_ZN12QNetworkFile10headerReadEN12QHttpHeaders15WellKnownHead'
        'erERK10QByteArray',
        a0.value, self._valueOf(value),
    )

  @overload(QNetworkReply.NetworkError, str)
  def networkError(
      self,
      error: QNetworkReply.NetworkError,
      message: str,
  ) -> None:
    """
    Calls Qt's 'void QNetworkFile::networkError(QNetworkReply::NetworkError
    error, const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkfile.html#networkError

    Parameters
    ----------

    error : QNetworkReply.NetworkError
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkFile::networkError(QNetworkReply::NetworkError error,
    #      const QString &message)
    self.uglySide.call(
        'ritual_ZN12QNetworkFile12networkErrorEN13QNetworkReply12NetworkErr'
        'orERK7QString',
        error.value, message,
    )
