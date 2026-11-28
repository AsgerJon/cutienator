"""
Qt3DCore::QDownloadRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qdownloadhelperservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QDownloadRequest to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QDownloadRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QDownloadRequest: a plain Python object
  standing in front of one C++ Qt3DCore::QDownloadRequest.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QDownloadRequest that has a ritual and
  that Python can call so far, 5 names in all: 'url', 'succeeded',
  'cancelled', 'onDownloaded', 'onCompleted'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QDownloadRequest::~QDownloadRequest()': the destructor:
    Python never removes a C++ Qt3DCore::QDownloadRequest.

  What to expect
  --------------

  - The C++ Qt3DCore::QDownloadRequest is created at the first use, not by
    'Qt3DCore::QDownloadRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QDownloadRequest.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QDownloadRequest'

  #  A C++ Qt3DCore::QDownloadRequest Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QDownloadRequest'

  #  The functions Qt calls itself that Qt3DCore::QDownloadRequest is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'onDownloaded': (
          ('_ZN8Qt3DCore16QDownloadRequest12onDownloadedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onCompleted': (
          ('_ZN8Qt3DCore16QDownloadRequest11onCompletedEv',
           ('nothing', 'nothing', ''),
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

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DCore::QDownloadRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qdownloadrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DCore::QDownloadRequest::url() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore16QDownloadRequest3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def succeeded(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QDownloadRequest::succeeded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadrequest.html#succeeded
    """
    #  bool Qt3DCore::QDownloadRequest::succeeded() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore16QDownloadRequest9succeededEv',
    )

  def cancelled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QDownloadRequest::cancelled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadrequest.html#cancelled
    """
    #  bool Qt3DCore::QDownloadRequest::cancelled() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore16QDownloadRequest9cancelledEv',
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

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QDownloadRequest::QDownloadRequest(const QUrl &url)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadrequest.html#QDownloadRequest

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  Qt3DCore::QDownloadRequest::QDownloadRequest(const QUrl &url)
    self._noteCreation(QDownloadRequest, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore16QDownloadRequestC1ERK4QUrl', self._valueOf(url),
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

  def onDownloaded(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QDownloadRequest::onDownloaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadrequest.html#onDownloaded
    """
    #  void Qt3DCore::QDownloadRequest::onDownloaded()
    ritual = 'ritual_ZN8Qt3DCore16QDownloadRequest12onDownloadedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore16QDownloadRequest12onDownloadedEv'
    self.uglySide.call(ritual)

  def onCompleted(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QDownloadRequest::onCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qdownloadrequest.html#onCompleted
    """
    #  void Qt3DCore::QDownloadRequest::onCompleted()
    self.uglySide.call('ritual_ZN8Qt3DCore16QDownloadRequest11onCompletedEv')
