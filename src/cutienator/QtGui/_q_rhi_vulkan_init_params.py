"""
QRhiVulkanInitParams binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi_platform.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from ..QtCore import QList
from . import QRhiInitParams

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class QRhiVulkanInitParams(QRhiInitParams):
  """
  The cute side of Qt's QRhiVulkanInitParams: a plain Python object standing
  in front of one C++ QRhiVulkanInitParams.

  It is built on the cute 'QRhiInitParams', as Qt's QRhiVulkanInitParams is
  built on Qt's QRhiInitParams, and has everything that class has.

  C++ hands a QRhiVulkanInitParams around as a copy, so every C++
  QRhiVulkanInitParams behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiVulkanInitParams that has a ritual and that
  Python can call so far, 2 names in all: 'preferredInstanceExtensions',
  'preferredExtensionsForImportedDevice'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiVulkanInitParams::~QRhiVulkanInitParams()': the destructor:
    Python removes its C++ QRhiVulkanInitParams by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRhiVulkanInitParams is created at the first use, not by
    'QRhiVulkanInitParams(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiVulkanInitParams back gives a copy the ritual
    made for Python, in a new cute QRhiVulkanInitParams.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def preferredInstanceExtensions() -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList
    QRhiVulkanInitParams::preferredInstanceExtensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkaninitparams.html

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QRhiVulkanInitParams::preferredInstanceExtensions()
    address = Rituals.call(
        'ritual_ZN20QRhiVulkanInitParams27preferredInstanceExtensionsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def preferredExtensionsForImportedDevice() -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList
    QRhiVulkanInitParams::preferredExtensionsForImportedDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivulkaninitparams.html

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList
    #      QRhiVulkanInitParams::preferredExtensionsForImportedDevice()
    address = Rituals.call(
        'ritual_ZN20QRhiVulkanInitParams36preferredExtensionsForImportedDev'
        'iceEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiVulkanInitParams'

  #  Qt's '~QRhiVulkanInitParams()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiVulkanInitParams behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QRhiVulkanInitParamsD1Ev'

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
