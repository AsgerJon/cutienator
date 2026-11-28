"""
QCameraFormatPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qcameradevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCameraFormatPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QVideoFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCameraFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCameraFormat = WAIT['QCameraFormat']


class QCameraFormatPrivate(QSharedData):
  """
  The cute side of Qt's QCameraFormatPrivate: a plain Python object standing
  in front of one C++ QCameraFormatPrivate.

  It is built on the cute 'QSharedData', as Qt's QCameraFormatPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QCameraFormatPrivate around as a copy, so every C++
  QCameraFormatPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCameraFormatPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'getColorRange', 'getColorSpace',
  'handle', 'create'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCameraFormatPrivate::~QCameraFormatPrivate()': the destructor:
    Python removes its C++ QCameraFormatPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCameraFormatPrivate is created at the first use, not by
    'QCameraFormatPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCameraFormatPrivate back gives a copy the ritual
    made for Python, in a new cute QCameraFormatPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCameraFormat)
  def getColorRange(format: QCameraFormat) -> QVideoFrameFormat.ColorRange:
    """
    Calls Qt's 'QVideoFrameFormat::ColorRange
    QCameraFormatPrivate::getColorRange(const QCameraFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcameraformatprivate.html#getColorRange

    Parameters
    ----------

    format : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.

    Returns
    -------

    QVideoFrameFormat.ColorRange
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrameFormat.ColorRange(number)' gives.
    """
    #  QVideoFrameFormat::ColorRange
    #      QCameraFormatPrivate::getColorRange(const QCameraFormat &format)
    return QVideoFrameFormat.ColorRange(Rituals.call(
        'ritual_ZN20QCameraFormatPrivate13getColorRangeERK13QCameraFormat',
        CuteMixin._valueOf(format),
    ))

  @staticmethod
  @overload(QCameraFormat)
  def getColorSpace(format: QCameraFormat) -> QVideoFrameFormat.ColorSpace:
    """
    Calls Qt's 'QVideoFrameFormat::ColorSpace
    QCameraFormatPrivate::getColorSpace(const QCameraFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcameraformatprivate.html#getColorSpace

    Parameters
    ----------

    format : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.

    Returns
    -------

    QVideoFrameFormat.ColorSpace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QVideoFrameFormat.ColorSpace(number)' gives.
    """
    #  QVideoFrameFormat::ColorSpace
    #      QCameraFormatPrivate::getColorSpace(const QCameraFormat &format)
    return QVideoFrameFormat.ColorSpace(Rituals.call(
        'ritual_ZN20QCameraFormatPrivate13getColorSpaceERK13QCameraFormat',
        CuteMixin._valueOf(format),
    ))

  @staticmethod
  @overload(QCameraFormat)
  def handle(format: QCameraFormat) -> Optional[QCameraFormatPrivate]:
    """
    Calls Qt's 'const QCameraFormatPrivate
    *QCameraFormatPrivate::handle(const QCameraFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformatprivate.html#handle

    Parameters
    ----------

    format : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.

    Returns
    -------

    Optional[QCameraFormatPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCameraFormatPrivate *QCameraFormatPrivate::handle(const
    #      QCameraFormat &format)
    address = Rituals.call(
        'ritual_ZN20QCameraFormatPrivate6handleERK13QCameraFormat',
        CuteMixin._valueOf(format),
    )
    return QCameraFormatPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCameraFormatPrivate'

  #  Qt's '~QCameraFormatPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCameraFormatPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QCameraFormatPrivateD1Ev'

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

  def create(self) -> QCameraFormat:
    """
    Calls Qt's 'QCameraFormat QCameraFormatPrivate::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qcameraformatprivate.html#create

    Returns
    -------

    QCameraFormat
      A new cute QCameraFormat around the copy Qt gave back. Python owns it.
    """
    #  QCameraFormat QCameraFormatPrivate::create()
    address = self.uglySide.call('ritual_ZN20QCameraFormatPrivate6createEv')
    from . import QCameraFormat
    return QCameraFormat._cuteOwning(address)
