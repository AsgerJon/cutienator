"""
QPlatformMediaFormatInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaformatinfo_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformMediaFormatInfo to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QMediaFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug


class QPlatformMediaFormatInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformMediaFormatInfo: a plain Python object
  standing in front of one C++ QPlatformMediaFormatInfo.

  C++ hands a QPlatformMediaFormatInfo around as a copy, so every C++
  QPlatformMediaFormatInfo behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformMediaFormatInfo that has a ritual and that
  Python can call so far, 2 names in all: 'isSupported', 'fixupCodecMaps'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformMediaFormatInfo::~QPlatformMediaFormatInfo()': the
    destructor: Python removes its C++ QPlatformMediaFormatInfo by it, and
    has no other use for it.
  - Qt's 'QList<QMediaFormat::FileFormat>
    QPlatformMediaFormatInfo::supportedFileFormats(const QMediaFormat
    &constraints, QMediaFormat::ConversionMode m) const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<QMediaFormat::AudioCodec>
    QPlatformMediaFormatInfo::supportedAudioCodecs(const QMediaFormat
    &constraints, QMediaFormat::ConversionMode m) const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<QMediaFormat::VideoCodec>
    QPlatformMediaFormatInfo::supportedVideoCodecs(const QMediaFormat
    &constraints, QMediaFormat::ConversionMode m) const': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QPlatformMediaFormatInfo is created at the first use, not by
    'QPlatformMediaFormatInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformMediaFormatInfo back gives a copy the ritual
    made for Python, in a new cute QPlatformMediaFormatInfo.
  - Each name of Qt's QPlatformMediaFormatInfo that has no cute function yet,
    'supportedAudioCodecs', 'supportedFileFormats', 'supportedVideoCodecs',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QPlatformMediaFormatInfo, each a class in
  #  here as in C++.

  class CodecMap(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPlatformMediaFormatInfo::CodecMap: a plain Python
    object standing in front of one C++ QPlatformMediaFormatInfo::CodecMap.

    C++ hands a QPlatformMediaFormatInfo::CodecMap around as a copy, so every
    C++ QPlatformMediaFormatInfo::CodecMap behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QPlatformMediaFormatInfo::CodecMap that has a
    ritual and that Python can call so far, 1 name in all: '__rlshift__'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPlatformMediaFormatInfo::CodecMap::~CodecMap()': the destructor:
      Python removes its C++ QPlatformMediaFormatInfo::CodecMap by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QPlatformMediaFormatInfo::CodecMap is created at the first use,
      not by 'QPlatformMediaFormatInfo::CodecMap(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPlatformMediaFormatInfo::CodecMap back gives a
      copy the ritual made for Python, in a new cute
      QPlatformMediaFormatInfo::CodecMap.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDebug = WAIT['QDebug']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPlatformMediaFormatInfo::CodecMap'

    #  Qt's '~QPlatformMediaFormatInfo::CodecMap()'. Naming it makes this a
    #  value class: Python owns every C++ QPlatformMediaFormatInfo::CodecMap
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QPlatformMediaFormatInfo8CodecMapD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QDebug)
    def __rlshift__(self, dbg: QDebug) -> QDebug:
      """
      Calls Qt's 'QDebug operator<<(QDebug dbg, const CodecMap &m)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qplatformmediaformatinfo-codecmap.html

      Parameters
      ----------

      dbg : QDebug
        Passed on as a value: Qt reads the C++ QDebug, which stays Python's
        own.

      Returns
      -------

      QDebug
        A new cute QDebug around the copy Qt gave back. Python owns it.
      """
      #  QDebug operator<<(QDebug dbg, const CodecMap &m)
      address = Rituals.call(
          'ritual_Zls6QDebugRKN24QPlatformMediaFormatInfo8CodecMapE',
          CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
      )
      from ..QtCore import QDebug
      return QDebug._cuteOwning(address)

    @overload.fallback
    def __rlshift__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMediaFormatInfo'

  #  Qt's '~QPlatformMediaFormatInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformMediaFormatInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QPlatformMediaFormatInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaFormat, QMediaFormat.ConversionMode)
  def isSupported(
      self,
      format: QMediaFormat,
      m: QMediaFormat.ConversionMode,
  ) -> bool:
    """
    Calls Qt's 'bool QPlatformMediaFormatInfo::isSupported(const QMediaFormat
    &format, QMediaFormat::ConversionMode m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaformatinfo.html#isSupported

    Parameters
    ----------

    format : QMediaFormat
      Passed on as a value: Qt reads the C++ QMediaFormat, which stays
      Python's own.

    m : QMediaFormat.ConversionMode
      Passed on as its number.
    """
    #  bool QPlatformMediaFormatInfo::isSupported(const QMediaFormat &format,
    #      QMediaFormat::ConversionMode m) const
    return self.uglySide.call(
        'ritual_ZNK24QPlatformMediaFormatInfo11isSupportedERK12QMediaFormat'
        'NS0_14ConversionModeE',
        self._valueOf(format), m.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformMediaFormatInfo::QPlatformMediaFormatInfo()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaformatinfo.html
    """
    #  QPlatformMediaFormatInfo::QPlatformMediaFormatInfo()
    self._noteCreation(QPlatformMediaFormatInfo, lambda: Rituals.call(
        'ritual_ZN24QPlatformMediaFormatInfoC1Ev',
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

  def fixupCodecMaps(self) -> None:
    """
    Calls Qt's 'void QPlatformMediaFormatInfo::fixupCodecMaps()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmediaformatinfo.html#fixupCodecMaps
    """
    #  void QPlatformMediaFormatInfo::fixupCodecMaps()
    self.uglySide.call(
        'ritual_ZN24QPlatformMediaFormatInfo14fixupCodecMapsEv',
    )

  @staticmethod
  def supportedAudioCodecs(*__, **_) -> Never:
    """
    Qt's 'QList<QMediaFormat::AudioCodec>
    QPlatformMediaFormatInfo::supportedAudioCodecs(const QMediaFormat
    &constraints, QMediaFormat::ConversionMode m) const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaFormatInfo.supportedAudioCodecs' has no cute "
        "function yet. Qt's 'QList<QMediaFormat::AudioCodec> "
        "QPlatformMediaFormatInfo::supportedAudioCodecs(const QMediaFormat "
        "&constraints, QMediaFormat::ConversionMode m) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def supportedFileFormats(*__, **_) -> Never:
    """
    Qt's 'QList<QMediaFormat::FileFormat>
    QPlatformMediaFormatInfo::supportedFileFormats(const QMediaFormat
    &constraints, QMediaFormat::ConversionMode m) const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaFormatInfo.supportedFileFormats' has no cute "
        "function yet. Qt's 'QList<QMediaFormat::FileFormat> "
        "QPlatformMediaFormatInfo::supportedFileFormats(const QMediaFormat "
        "&constraints, QMediaFormat::ConversionMode m) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def supportedVideoCodecs(*__, **_) -> Never:
    """
    Qt's 'QList<QMediaFormat::VideoCodec>
    QPlatformMediaFormatInfo::supportedVideoCodecs(const QMediaFormat
    &constraints, QMediaFormat::ConversionMode m) const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMediaFormatInfo.supportedVideoCodecs' has no cute "
        "function yet. Qt's 'QList<QMediaFormat::VideoCodec> "
        "QPlatformMediaFormatInfo::supportedVideoCodecs(const QMediaFormat "
        "&constraints, QMediaFormat::ConversionMode m) const': gives a type "
        "Python has no way to take yet.")
