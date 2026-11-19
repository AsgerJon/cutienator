"""
QDesktopServices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qdesktopservices.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QObject
from ..QtCore import QUrl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesktopServices(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesktopServices: a plain Python object standing in
  front of one C++ QDesktopServices.

  C++ hands a QDesktopServices around as a copy, so every C++
  QDesktopServices behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDesktopServices that has a ritual and that Python
  can call so far, 3 names in all: 'openUrl', 'setUrlHandler',
  'unsetUrlHandler'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesktopServices::~QDesktopServices()': the destructor: Python
    removes its C++ QDesktopServices by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDesktopServices is created at the first use, not by
    'QDesktopServices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDesktopServices back gives a copy the ritual made
    for Python, in a new cute QDesktopServices.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUrl)
  def openUrl(url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDesktopServices::openUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesktopservices.html#openUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDesktopServices::openUrl(const QUrl &url)
    return Rituals.call(
        'ritual_ZN16QDesktopServices7openUrlERK4QUrl',
        CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(str, QObject, str)
  @overload(str, QObject, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  def setUrlHandler(
      scheme: str,
      receiver: Optional[QObject],
      method: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QDesktopServices::setUrlHandler(const QString &scheme,
    QObject *receiver, const char *method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopservices.html#setUrlHandler

    Parameters
    ----------

    scheme : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QDesktopServices::setUrlHandler(const QString &scheme, QObject
    #      *receiver, const char *method)
    Rituals.call(
        'ritual_ZN16QDesktopServices13setUrlHandlerERK7QStringP7QObjectPKc',
        scheme, CuteMixin._addressOf(receiver), CuteMixin._bytesOf(method),
    )

  @staticmethod
  @overload(str)
  def unsetUrlHandler(scheme: str) -> None:
    """
    Calls Qt's 'void QDesktopServices::unsetUrlHandler(const QString
    &scheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesktopservices.html#unsetUrlHandler

    Parameters
    ----------

    scheme : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesktopServices::unsetUrlHandler(const QString &scheme)
    Rituals.call(
        'ritual_ZN16QDesktopServices15unsetUrlHandlerERK7QString', scheme,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesktopServices'

  #  Qt's '~QDesktopServices()'. Naming it makes this a value class: Python
  #  owns every C++ QDesktopServices behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDesktopServicesD1Ev'

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
