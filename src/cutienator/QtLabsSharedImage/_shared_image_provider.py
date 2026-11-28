"""
SharedImageProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qsharedimageprovider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SharedImageProvider to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QImage
  from ..QtQuick import QQuickImageProviderOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickImageProviderOptions = WAIT['QQuickImageProviderOptions']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SharedImageProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's SharedImageProvider: a plain Python object standing
  in front of one C++ SharedImageProvider.

  What exists
  -----------

  Every function of Qt's SharedImageProvider that has a ritual and that
  Python can call so far, 1 name in all: 'requestImage'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ SharedImageProvider is created at the first use, not by
    'SharedImageProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SharedImageProvider.
  - Qt tells when it has removed the C++ SharedImageProvider. Every call on
    the cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'SharedImageProvider'

  #  A C++ SharedImageProvider Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SharedImageProvider'

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
    'SharedImageProvider::SharedImageProvider()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/sharedimageprovider.html#SharedImageProvider
    """
    #  SharedImageProvider::SharedImageProvider()
    self._noteCreation(SharedImageProvider, lambda: Rituals.call(
        'ritual_ZN19SharedImageProviderC1Ev',
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

  @overload(str, QSize, QSize, QQuickImageProviderOptions)
  @overload(str, NoneType, QSize, QQuickImageProviderOptions)
  def requestImage(
      self,
      id: str,
      size: Optional[QSize],
      requestedSize: QSize,
      options: QQuickImageProviderOptions,
  ) -> QImage:
    """
    Calls Qt's 'QImage SharedImageProvider::requestImage(const QString &id,
    QSize *size, const QSize &requestedSize, const QQuickImageProviderOptions
    &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/sharedimageprovider.html#requestImage

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : Optional[QSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage SharedImageProvider::requestImage(const QString &id, QSize
    #      *size, const QSize &requestedSize, const
    #      QQuickImageProviderOptions &options)
    ritual = (
        'ritual_ZN19SharedImageProvider12requestImageERK7QStringP5QSizeRKS3'
        '_RK26QQuickImageProviderOptions')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19SharedImageProvider12requestImageERK7QStringP5QSi'
          'zeRKS3_RK26QQuickImageProviderOptions')
    address = self.uglySide.call(
        ritual,
        id, self._addressOf(size), self._valueOf(requestedSize),
        self._valueOf(options),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)
