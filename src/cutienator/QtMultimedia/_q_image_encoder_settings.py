"""
QImageEncoderSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformimagecapture_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QImageEncoderSettings to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QImageCapture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QImageEncoderSettings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QImageEncoderSettings: a plain Python object standing
  in front of one C++ QImageEncoderSettings.

  C++ hands a QImageEncoderSettings around as a copy, so every C++
  QImageEncoderSettings behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QImageEncoderSettings that has a ritual and that
  Python can call so far, 8 names in all: '__eq__', '__ne__', 'format',
  'setFormat', 'resolution', 'setResolution', 'quality', 'setQuality'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageEncoderSettings::~QImageEncoderSettings()': the destructor:
    Python removes its C++ QImageEncoderSettings by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QImageEncoderSettings is created at the first use, not by
    'QImageEncoderSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QImageEncoderSettings back gives a copy the ritual
    made for Python, in a new cute QImageEncoderSettings.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageEncoderSettings'

  #  Qt's '~QImageEncoderSettings()'. Naming it makes this a value class:
  #  Python owns every C++ QImageEncoderSettings behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QImageEncoderSettingsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QImageCapture.FileFormat:
    """
    Calls Qt's 'QImageCapture::FileFormat QImageEncoderSettings::format()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageencodersettings.html#format

    Returns
    -------

    QImageCapture.FileFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QImageCapture.FileFormat(number)' gives.
    """
    #  QImageCapture::FileFormat QImageEncoderSettings::format() const
    return QImageCapture.FileFormat(self.uglySide.call(
        'ritual_ZNK21QImageEncoderSettings6formatEv',
    ))

  def resolution(self) -> QSize:
    """
    Calls Qt's 'QSize QImageEncoderSettings::resolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#resolution

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QImageEncoderSettings::resolution() const
    address = self.uglySide.call(
        'ritual_ZNK21QImageEncoderSettings10resolutionEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def quality(self) -> QImageCapture.Quality:
    """
    Calls Qt's 'QImageCapture::Quality QImageEncoderSettings::quality()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageencodersettings.html#quality

    Returns
    -------

    QImageCapture.Quality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QImageCapture.Quality(number)' gives.
    """
    #  QImageCapture::Quality QImageEncoderSettings::quality() const
    return QImageCapture.Quality(self.uglySide.call(
        'ritual_ZNK21QImageEncoderSettings7qualityEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QImageCapture.FileFormat)
  def setFormat(self, f: QImageCapture.FileFormat) -> None:
    """
    Calls Qt's 'void
    QImageEncoderSettings::setFormat(QImageCapture::FileFormat f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#setFormat

    Parameters
    ----------

    f : QImageCapture.FileFormat
      Passed on as its number.
    """
    #  void QImageEncoderSettings::setFormat(QImageCapture::FileFormat f)
    self.uglySide.call(
        'ritual_ZN21QImageEncoderSettings9setFormatEN13QImageCapture10FileF'
        'ormatE',
        f.value,
    )

  @overload(QSize)
  def setResolution(self, s: QSize) -> None:
    """
    Calls Qt's 'void QImageEncoderSettings::setResolution(const QSize &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#setResolution

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QImageEncoderSettings::setResolution(const QSize &s)
    self.uglySide.call(
        'ritual_ZN21QImageEncoderSettings13setResolutionERK5QSize',
        self._valueOf(s),
    )

  @overload(int, int)
  def setResolution(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QImageEncoderSettings::setResolution(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#setResolution

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QImageEncoderSettings::setResolution(int width, int height)
    self.uglySide.call(
        'ritual_ZN21QImageEncoderSettings13setResolutionEii', width, height,
    )

  @overload(QImageCapture.Quality)
  def setQuality(self, quality: QImageCapture.Quality) -> None:
    """
    Calls Qt's 'void QImageEncoderSettings::setQuality(QImageCapture::Quality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#setQuality

    Parameters
    ----------

    quality : QImageCapture.Quality
      Passed on as its number.
    """
    #  void QImageEncoderSettings::setQuality(QImageCapture::Quality quality)
    self.uglySide.call(
        'ritual_ZN21QImageEncoderSettings10setQualityEN13QImageCapture7Qual'
        'ityE',
        quality.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QImageEncoderSettings) -> bool:
    """
    Calls Qt's 'bool QImageEncoderSettings::operator==(const
    QImageEncoderSettings &other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#operator==

    Parameters
    ----------

    other : QImageEncoderSettings
      Passed on as a value: Qt reads the C++ QImageEncoderSettings, which
      stays Python's own.
    """
    #  bool QImageEncoderSettings::operator==(const QImageEncoderSettings
    #      &other)
    return self.uglySide.call(
        'ritual_ZN21QImageEncoderSettingseqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QImageEncoderSettings) -> bool:
    """
    Calls Qt's 'bool QImageEncoderSettings::operator!=(const
    QImageEncoderSettings &other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qimageencodersettings.html#operator!=

    Parameters
    ----------

    other : QImageEncoderSettings
      Passed on as a value: Qt reads the C++ QImageEncoderSettings, which
      stays Python's own.
    """
    #  bool QImageEncoderSettings::operator!=(const QImageEncoderSettings
    #      &other)
    return self.uglySide.call(
        'ritual_ZN21QImageEncoderSettingsneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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
