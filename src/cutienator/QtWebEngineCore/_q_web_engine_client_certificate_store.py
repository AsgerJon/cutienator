"""
QWebEngineClientCertificateStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineclientcertificatestore.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtNetwork import QSslCertificate, QSslKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslCertificate = WAIT['QSslCertificate']
  QSslKey = WAIT['QSslKey']


class QWebEngineClientCertificateStore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineClientCertificateStore: a plain Python
  object standing in front of one C++ QWebEngineClientCertificateStore.

  What exists
  -----------

  Every function of Qt's QWebEngineClientCertificateStore that has a ritual
  and that Python can call so far, 4 names in all: 'add', 'certificates',
  'remove', 'clear'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineClientCertificateStore::QWebEngineClientCertificateStore(
    QtWebEngineCore::ClientCertificateStoreData *storeData)': names
    'QtWebEngineCore::ClientCertificateStoreData', which has no cute class
    yet.
  - Qt's
    'QWebEngineClientCertificateStore::~QWebEngineClientCertificateStore()':
    the destructor: Python never removes a C++
    QWebEngineClientCertificateStore.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineClientCertificateStore is created at the first use, not
    by 'QWebEngineClientCertificateStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineClientCertificateStore.
  - Each name of Qt's QWebEngineClientCertificateStore that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineClientCertificateStore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def certificates(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QWebEngineClientCertificateStore::certificates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificatestore.html#certificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate>
    #      QWebEngineClientCertificateStore::certificates() const
    address = self.uglySide.call(
        'ritual_ZNK32QWebEngineClientCertificateStore12certificatesEv',
    )
    from ..QtNetwork import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

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
    Qt's 'QWebEngineClientCertificateStore::QWebEngineClientCertificateStore(
    QtWebEngineCore::ClientCertificateStoreData *storeData)': names
    'QtWebEngineCore::ClientCertificateStoreData', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QWebEngineClientCertificateStore.__init__' has no cute function "
        "yet. Qt's "
        "'QWebEngineClientCertificateStore::QWebEngineClientCertificateStore"
        "(QtWebEngineCore::ClientCertificateStoreData *storeData)': names "
        "'QtWebEngineCore::ClientCertificateStoreData', which has no cute "
        "class yet.")

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

  @overload(QSslCertificate, QSslKey)
  def add(self, certificate: QSslCertificate, privateKey: QSslKey) -> None:
    """
    Calls Qt's 'void QWebEngineClientCertificateStore::add(const
    QSslCertificate &certificate, const QSslKey &privateKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificatestore.html#add

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.

    privateKey : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  void QWebEngineClientCertificateStore::add(const QSslCertificate
    #      &certificate, const QSslKey &privateKey)
    self.uglySide.call(
        'ritual_ZN32QWebEngineClientCertificateStore3addERK15QSslCertificat'
        'eRK7QSslKey',
        self._valueOf(certificate), self._valueOf(privateKey),
    )

  @overload(QSslCertificate)
  def remove(self, certificate: QSslCertificate) -> None:
    """
    Calls Qt's 'void QWebEngineClientCertificateStore::remove(const
    QSslCertificate &certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificatestore.html#remove

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QWebEngineClientCertificateStore::remove(const QSslCertificate
    #      &certificate)
    self.uglySide.call(
        'ritual_ZN32QWebEngineClientCertificateStore6removeERK15QSslCertifi'
        'cate',
        self._valueOf(certificate),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QWebEngineClientCertificateStore::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificatestore.html#clear
    """
    #  void QWebEngineClientCertificateStore::clear()
    self.uglySide.call('ritual_ZN32QWebEngineClientCertificateStore5clearEv')
