"""
QQuickAsyncImageProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickImageProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QQuickImageResponse
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QQuickAsyncImageProvider(QQuickImageProvider):
  """
  The cute side of Qt's QQuickAsyncImageProvider: a plain Python object
  standing in front of one C++ QQuickAsyncImageProvider.

  It is built on the cute 'QQuickImageProvider', as Qt's
  QQuickAsyncImageProvider is built on Qt's QQuickImageProvider, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAsyncImageProvider that has a ritual and that
  Python can call so far, 1 name in all: 'requestImageResponse'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickAsyncImageProvider::~QQuickAsyncImageProvider()': the
    destructor: Python never removes a C++ QQuickAsyncImageProvider.

  What to expect
  --------------

  - The C++ QQuickAsyncImageProvider is created at the first use, not by
    'QQuickAsyncImageProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAsyncImageProvider.
  - Qt tells when it has removed the C++ QQuickAsyncImageProvider. Every call
    on the cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'QQuickAsyncImageProvider'

  #  A C++ QQuickAsyncImageProvider Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAsyncImageProvider'

  #  The functions Qt calls itself that QQuickAsyncImageProvider is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'requestImageResponse': (
          ('_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStringR'
           'K5QSize',
           ('address', 'address', 'QtQuick:QQuickImageResponse'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
  }

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAsyncImageProvider::QQuickAsyncImageProvider()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickasyncimageprovider.html
    """
    #  QQuickAsyncImageProvider::QQuickAsyncImageProvider()
    self._noteCreation(QQuickAsyncImageProvider, lambda: Rituals.call(
        'ritual_ZN24QQuickAsyncImageProviderC1Ev',
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

  @overload(str, QSize)
  def requestImageResponse(
      self,
      id: str,
      requestedSize: QSize,
  ) -> Optional[QQuickImageResponse]:
    """
    Calls Qt's 'QQuickImageResponse
    *QQuickAsyncImageProvider::requestImageResponse(const QString &id, const
    QSize &requestedSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickasyncimageprovider.html#requestImageResponse

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    Optional[QQuickImageResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageResponse
    #      *QQuickAsyncImageProvider::requestImageResponse(const QString &id,
    #      const QSize &requestedSize)
    address = self.uglySide.call(
        'ritual_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStri'
        'ngRK5QSize',
        id, self._valueOf(requestedSize),
    )
    from . import QQuickImageResponse
    return QQuickImageResponse._cuteAt(address)
