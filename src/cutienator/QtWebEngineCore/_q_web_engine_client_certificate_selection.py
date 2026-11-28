"""
QWebEngineClientCertificateSelection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineclientcertificateselection.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
  from ..QtNetwork import QSslCertificate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslCertificate = WAIT['QSslCertificate']


class QWebEngineClientCertificateSelection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineClientCertificateSelection: a plain Python
  object standing in front of one C++ QWebEngineClientCertificateSelection.

  C++ hands a QWebEngineClientCertificateSelection around as a copy, so every
  C++ QWebEngineClientCertificateSelection behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineClientCertificateSelection that has a
  ritual and that Python can call so far, 4 names in all: 'host', 'select',
  'selectNone', 'certificates'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineClientCertificateSelection::
    ~QWebEngineClientCertificateSelection()': the destructor: Python removes
    its C++ QWebEngineClientCertificateSelection by it, and has no other use
    for it.
  - Qt's 'QWebEngineClientCertificateSelection
    &QWebEngineClientCertificateSelection::operator=(const
    QWebEngineClientCertificateSelection &a0)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QWebEngineClientCertificateSelection::
    QWebEngineClientCertificateSelection(QSharedPointer<QtWebEngineCore::
    ClientCertSelectController> a0)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QWebEngineClientCertificateSelection is created at the first use,
    not by 'QWebEngineClientCertificateSelection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineClientCertificateSelection back gives a
    copy the ritual made for Python, in a new cute
    QWebEngineClientCertificateSelection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineClientCertificateSelection'

  #  Qt's '~QWebEngineClientCertificateSelection()'. Naming it makes this a
  #  value class: Python owns every C++ QWebEngineClientCertificateSelection
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN36QWebEngineClientCertificateSelectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def host(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineClientCertificateSelection::host() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificateselection.html#host

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineClientCertificateSelection::host() const
    address = self.uglySide.call(
        'ritual_ZNK36QWebEngineClientCertificateSelection4hostEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def certificates(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QWebEngineClientCertificateSelection::certificates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificateselection.html

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate>
    #      QWebEngineClientCertificateSelection::certificates() const
    address = self.uglySide.call(
        'ritual_ZNK36QWebEngineClientCertificateSelection12certificatesEv',
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

  @overload(THIS)
  def __init__(self, a0: QWebEngineClientCertificateSelection) -> None:
    """
    Notes what was given, for Qt's 'QWebEngineClientCertificateSelection::
    QWebEngineClientCertificateSelection(const
    QWebEngineClientCertificateSelection &a0)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificateselection.html

    Parameters
    ----------

    a0 : QWebEngineClientCertificateSelection
      Passed on as a value: Qt reads the C++
      QWebEngineClientCertificateSelection, which stays Python's own.
    """
    #  QWebEngineClientCertificateSelection::
    #      QWebEngineClientCertificateSelection(const
    #      QWebEngineClientCertificateSelection &a0)
    self._noteCreation(
        QWebEngineClientCertificateSelection, lambda: Rituals.call(
            'ritual_ZN36QWebEngineClientCertificateSelectionC1ERKS_',
            self._valueOf(a0),
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

  @overload(QSslCertificate)
  def select(self, certificate: QSslCertificate) -> None:
    """
    Calls Qt's 'void QWebEngineClientCertificateSelection::select(const
    QSslCertificate &certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificateselection.html#select

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QWebEngineClientCertificateSelection::select(const
    #      QSslCertificate &certificate)
    self.uglySide.call(
        'ritual_ZN36QWebEngineClientCertificateSelection6selectERK15QSslCer'
        'tificate',
        self._valueOf(certificate),
    )

  def selectNone(self) -> None:
    """
    Calls Qt's 'void QWebEngineClientCertificateSelection::selectNone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineclientcertificateselection.html
    """
    #  void QWebEngineClientCertificateSelection::selectNone()
    self.uglySide.call(
        'ritual_ZN36QWebEngineClientCertificateSelection10selectNoneEv',
    )
