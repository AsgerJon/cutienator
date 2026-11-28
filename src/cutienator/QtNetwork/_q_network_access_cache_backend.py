"""
QNetworkAccessCacheBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscachebackend_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QNetworkAccessCacheBackend to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QNetworkAccessBackend


class QNetworkAccessCacheBackend(QNetworkAccessBackend):
  """
  The cute side of Qt's QNetworkAccessCacheBackend: a plain Python object
  standing in front of one C++ QNetworkAccessCacheBackend.

  It is built on the cute 'QNetworkAccessBackend', as Qt's
  QNetworkAccessCacheBackend is built on Qt's QNetworkAccessBackend, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessCacheBackend that has a ritual and
  that Python can call so far, 5 names in all: 'open', 'close', 'start',
  'bytesAvailable', 'sendCacheContents'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkAccessCacheBackend::~QNetworkAccessCacheBackend()': the
    destructor: Python never removes a C++ QNetworkAccessCacheBackend.
  - Qt's 'qint64 QNetworkAccessCacheBackend::read(char *data, qint64
    maxlen)': names 'char', which has no cute class yet.

  What to expect
  --------------

  - The C++ QNetworkAccessCacheBackend is created at the first use, not by
    'QNetworkAccessCacheBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessCacheBackend.
  - Qt tells when it has removed the C++ QNetworkAccessCacheBackend. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessCacheBackend'

  #  A C++ QNetworkAccessCacheBackend Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessCacheBackend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkAccessCacheBackend::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscachebackend.html#bytesAvailable
    """
    #  qint64 QNetworkAccessCacheBackend::bytesAvailable() const
    ritual = 'ritual_ZNK26QNetworkAccessCacheBackend14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QNetworkAccessCacheBackend14bytesAvailableEv'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAccessCacheBackend::QNetworkAccessCacheBackend()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscachebackend.html
    """
    #  QNetworkAccessCacheBackend::QNetworkAccessCacheBackend()
    self._noteCreation(QNetworkAccessCacheBackend, lambda: Rituals.call(
        'ritual_ZN26QNetworkAccessCacheBackendC1Ev',
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

  def open(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessCacheBackend::open()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscachebackend.html#open
    """
    #  void QNetworkAccessCacheBackend::open()
    ritual = 'ritual_ZN26QNetworkAccessCacheBackend4openEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QNetworkAccessCacheBackend4openEv'
    self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessCacheBackend::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscachebackend.html#close
    """
    #  void QNetworkAccessCacheBackend::close()
    ritual = 'ritual_ZN26QNetworkAccessCacheBackend5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QNetworkAccessCacheBackend5closeEv'
    self.uglySide.call(ritual)

  def start(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessCacheBackend::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscachebackend.html#start
    """
    #  bool QNetworkAccessCacheBackend::start()
    ritual = 'ritual_ZN26QNetworkAccessCacheBackend5startEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QNetworkAccessCacheBackend5startEv'
    return self.uglySide.call(ritual)

  def sendCacheContents(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessCacheBackend::sendCacheContents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccesscachebackend.html#sendCacheContents
    """
    #  bool QNetworkAccessCacheBackend::sendCacheContents()
    return self.uglySide.call(
        'ritual_ZN26QNetworkAccessCacheBackend17sendCacheContentsEv',
    )
