"""
QQuick3DAudioEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudioengine_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DAudioEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuick3DAudioEngine(QObject):
  """
  The cute side of Qt's QQuick3DAudioEngine: a plain Python object standing
  in front of one C++ QQuick3DAudioEngine.

  It is built on the cute 'QObject', as Qt's QQuick3DAudioEngine is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DAudioEngine that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'outputModeChanged',
  'outputDeviceChanged', 'masterVolumeChanged', 'distanceScaleChanged'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DAudioEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DAudioEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DAudioEngine::~QQuick3DAudioEngine()': the destructor:
    Python never removes a C++ QQuick3DAudioEngine.

  What has no ritual
  ------------------

  13 of the 21 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QQuick3DAudioEngine.

  What to expect
  --------------

  - The C++ QQuick3DAudioEngine is created at the first use, not by
    'QQuick3DAudioEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DAudioEngine.
  - Qt tells when it has removed the C++ QQuick3DAudioEngine. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DAudioEngine that has no cute function yet,
    '__init__', 'distanceScale', 'getEngine', 'masterVolume', 'outputDevice',
    'outputMode', 'setDistanceScale', 'setMasterVolume', 'setOutputDevice',
    'setOutputMode', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DAudioEngine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class OutputMode(CuteNum):
    """
    The enum 'QQuick3DAudioEngine::OutputMode' of Qt, with the 3 names Qt
    gives in it.
    """

    Surround = Kee[int](0)
    Stereo = Kee[int](1)
    Headphone = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DAudioEngine'

  #  A C++ QQuick3DAudioEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DAudioEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DAudioEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DAudioEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DAudioEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuick3DAudioEngine::QQuick3DAudioEngine()': leans on
    'QQuick3DAudioEngine::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.__init__' has no cute function yet. Qt's "
        "'QQuick3DAudioEngine::QQuick3DAudioEngine()': leans on "
        "'QQuick3DAudioEngine::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def outputModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioEngine::outputModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioengine.html#outputModeChanged
    """
    #  void QQuick3DAudioEngine::outputModeChanged()
    self.uglySide.call('ritual_ZN19QQuick3DAudioEngine17outputModeChangedEv')

  def outputDeviceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioEngine::outputDeviceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioengine.html#outputDeviceChanged
    """
    #  void QQuick3DAudioEngine::outputDeviceChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DAudioEngine19outputDeviceChangedEv',
    )

  def masterVolumeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioEngine::masterVolumeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioengine.html#masterVolumeChanged
    """
    #  void QQuick3DAudioEngine::masterVolumeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DAudioEngine19masterVolumeChangedEv',
    )

  def distanceScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioEngine::distanceScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioengine.html#distanceScaleChanged
    """
    #  void QQuick3DAudioEngine::distanceScaleChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DAudioEngine20distanceScaleChangedEv',
    )

  @staticmethod
  def distanceScale(*__, **_) -> Never:
    """
    Qt's 'float QQuick3DAudioEngine::distanceScale() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.distanceScale' has no cute function yet. Qt's "
        "'float QQuick3DAudioEngine::distanceScale() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'globalEngine'.")

  @staticmethod
  def getEngine(*__, **_) -> Never:
    """
    Qt's 'QAudioEngine *QQuick3DAudioEngine::getEngine()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.getEngine' has no cute function yet. Qt's "
        "'QAudioEngine *QQuick3DAudioEngine::getEngine()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'globalEngine'.")

  @staticmethod
  def masterVolume(*__, **_) -> Never:
    """
    Qt's 'float QQuick3DAudioEngine::masterVolume() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.masterVolume' has no cute function yet. Qt's "
        "'float QQuick3DAudioEngine::masterVolume() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'globalEngine'.")

  @staticmethod
  def outputDevice(*__, **_) -> Never:
    """
    Qt's 'QAudioDevice QQuick3DAudioEngine::outputDevice() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.outputDevice' has no cute function yet. Qt's "
        "'QAudioDevice QQuick3DAudioEngine::outputDevice() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'globalEngine'.")

  @staticmethod
  def outputMode(*__, **_) -> Never:
    """
    Qt's 'OutputMode QQuick3DAudioEngine::outputMode() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.outputMode' has no cute function yet. Qt's "
        "'OutputMode QQuick3DAudioEngine::outputMode() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'globalEngine'.")

  @staticmethod
  def setDistanceScale(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DAudioEngine::setDistanceScale(float scale)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.setDistanceScale' has no cute function yet. "
        "Qt's 'void QQuick3DAudioEngine::setDistanceScale(float scale)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'globalEngine'.")

  @staticmethod
  def setMasterVolume(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DAudioEngine::setMasterVolume(float volume)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.setMasterVolume' has no cute function yet. "
        "Qt's 'void QQuick3DAudioEngine::setMasterVolume(float volume)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'globalEngine'.")

  @staticmethod
  def setOutputDevice(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DAudioEngine::setOutputDevice(const QAudioDevice
    &device)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.setOutputDevice' has no cute function yet. "
        "Qt's 'void QQuick3DAudioEngine::setOutputDevice(const QAudioDevice "
        "&device)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'globalEngine'.")

  @staticmethod
  def setOutputMode(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DAudioEngine::setOutputMode(OutputMode mode)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'globalEngine'.
    """
    raise NotImplementedError(
        "'QQuick3DAudioEngine.setOutputMode' has no cute function yet. Qt's "
        "'void QQuick3DAudioEngine::setOutputMode(OutputMode mode)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'globalEngine'.")
