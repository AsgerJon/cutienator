"""
QGStreamerInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamerinterface.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject
  from . import QAudioDevice, QCamera
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGStreamerInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGStreamerInterface: a plain Python object standing
  in front of one C++ QGStreamerInterface.

  What exists
  -----------

  Every function of Qt's QGStreamerInterface that has a ritual and that
  Python can call so far, 4 names in all: 'instance',
  'makeCustomGStreamerCamera', 'makeCustomGStreamerAudioInput',
  'makeCustomGStreamerAudioOutput'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGStreamerInterface::~QGStreamerInterface()': the destructor:
    Python never removes a C++ QGStreamerInterface.
  - Qt's 'QCamera *QGStreamerInterface::makeCustomGStreamerCamera(GstElement
    *element, QObject *parent)': names 'GstElement', which has no cute class
    yet.
  - Qt's 'GstPipeline *QGStreamerInterface::gstPipeline(QMediaPlayer *a0)':
    gives 'struct _GstPipeline', which has no cute class yet.
  - Qt's 'GstPipeline *QGStreamerInterface::gstPipeline(QMediaCaptureSession
    *a0)': gives 'struct _GstPipeline', which has no cute class yet.
  - Qt's 'GstBuffer *QGStreamerInterface::gstBuffer(const QVideoFrame
    &frame)': gives 'struct _GstBuffer', which has no cute class yet.
  - Qt's 'QVideoFrame QGStreamerInterface::createFrameFromGstBuffer(GstBuffer
    *buffer, const GstVideoInfo &videoInfo)': names 'GstBuffer', which has no
    cute class yet.
  - Qt's 'QVideoFrame QGStreamerInterface::createFrameFromGstBuffer(GstBuffer
    *buffer, const GstVideoInfoDmaDrm &videoInfo)': names 'GstBuffer', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ QGStreamerInterface is created at the first use, not by
    'QGStreamerInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGStreamerInterface.
  - Each name of Qt's QGStreamerInterface that has no cute function yet,
    'createFrameFromGstBuffer', 'gstBuffer', 'gstPipeline', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QGStreamerInterface]:
    """
    Calls Qt's 'QGStreamerInterface *QGStreamerInterface::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qgstreamerinterface.html#instance

    Returns
    -------

    Optional[QGStreamerInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGStreamerInterface *QGStreamerInterface::instance()
    address = Rituals.call('ritual_ZN19QGStreamerInterface8instanceEv')
    return QGStreamerInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGStreamerInterface'

  #  A C++ QGStreamerInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGStreamerInterface'

  #  The functions Qt calls itself that QGStreamerInterface is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'gstPipeline': (
          'GstPipeline *QGStreamerInterface::gstPipeline(QMediaPlayer *)',
          'GstPipeline '
          '*QGStreamerInterface::gstPipeline(QMediaCaptureSession *)',
      ),
      'gstBuffer': (
          'GstBuffer *QGStreamerInterface::gstBuffer(const QVideoFrame &)',
      ),
      'createFrameFromGstBuffer': (
          'QVideoFrame '
          'QGStreamerInterface::createFrameFromGstBuffer(GstBuffer *, '
          'const GstVideoInfo &)',
          'QVideoFrame '
          'QGStreamerInterface::createFrameFromGstBuffer(GstBuffer *, '
          'const GstVideoInfoDmaDrm &)',
      ),
  }

  #  The functions Qt calls itself that QGStreamerInterface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'makeCustomGStreamerCamera': (
          ('_ZN19QGStreamerInterface25makeCustomGStreamerCameraERK10QByteAr'
           'rayP7QObject',
           ('address', 'address', 'QtMultimedia:QCamera'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'makeCustomGStreamerAudioInput': (
          ('_ZN19QGStreamerInterface29makeCustomGStreamerAudioInputERK10QBy'
           'teArray',
           ('address', 'value', 'QtMultimedia:QAudioDevice'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'makeCustomGStreamerAudioOutput': (
          ('_ZN19QGStreamerInterface30makeCustomGStreamerAudioOutputERK10QB'
           'yteArray',
           ('address', 'value', 'QtMultimedia:QAudioDevice'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
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

  @overload(QByteArray, QObject)
  @overload(QByteArray, NoneType)
  def makeCustomGStreamerCamera(
      self,
      gstBinDescription: QByteArray,
      parent: Optional[QObject],
  ) -> Optional[QCamera]:
    """
    Calls Qt's 'QCamera *QGStreamerInterface::makeCustomGStreamerCamera(const
    QByteArray &gstBinDescription, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamerinterface.html#makeCustomGStreamerCamera

    Parameters
    ----------

    gstBinDescription : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCamera *QGStreamerInterface::makeCustomGStreamerCamera(const
    #      QByteArray &gstBinDescription, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN19QGStreamerInterface25makeCustomGStreamerCameraERK10QByt'
        'eArrayP7QObject',
        self._valueOf(gstBinDescription), self._addressOf(parent, 'QObject'),
    )
    from . import QCamera
    return QCamera._cuteAt(address)

  @overload(QByteArray)
  def makeCustomGStreamerAudioInput(
      self,
      gstreamerPipeline: QByteArray,
  ) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice
    QGStreamerInterface::makeCustomGStreamerAudioInput(const QByteArray
    &gstreamerPipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamerinterface.html

    Parameters
    ----------

    gstreamerPipeline : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QGStreamerInterface::makeCustomGStreamerAudioInput(const
    #      QByteArray &gstreamerPipeline)
    address = self.uglySide.call(
        'ritual_ZN19QGStreamerInterface29makeCustomGStreamerAudioInputERK10'
        'QByteArray',
        self._valueOf(gstreamerPipeline),
    )
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  @overload(QByteArray)
  def makeCustomGStreamerAudioOutput(
      self,
      gstreamerPipeline: QByteArray,
  ) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice
    QGStreamerInterface::makeCustomGStreamerAudioOutput(const QByteArray
    &gstreamerPipeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamerinterface.html

    Parameters
    ----------

    gstreamerPipeline : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QGStreamerInterface::makeCustomGStreamerAudioOutput(const
    #      QByteArray &gstreamerPipeline)
    address = self.uglySide.call(
        'ritual_ZN19QGStreamerInterface30makeCustomGStreamerAudioOutputERK1'
        '0QByteArray',
        self._valueOf(gstreamerPipeline),
    )
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  @staticmethod
  def createFrameFromGstBuffer(*__, **_) -> Never:
    """
    - Qt's 'QVideoFrame
      QGStreamerInterface::createFrameFromGstBuffer(GstBuffer *buffer, const
      GstVideoInfo &videoInfo)': names 'GstBuffer', which has no cute class
      yet.
    - Qt's 'QVideoFrame
      QGStreamerInterface::createFrameFromGstBuffer(GstBuffer *buffer, const
      GstVideoInfoDmaDrm &videoInfo)': names 'GstBuffer', which has no cute
      class yet.
    """
    raise NotImplementedError(
        "'QGStreamerInterface.createFrameFromGstBuffer' has no cute "
        "function yet. Qt's 'QVideoFrame "
        "QGStreamerInterface::createFrameFromGstBuffer(GstBuffer *buffer, "
        "const GstVideoInfo &videoInfo)': names 'GstBuffer', which has no "
        "cute class yet. Qt's 'QVideoFrame "
        "QGStreamerInterface::createFrameFromGstBuffer(GstBuffer *buffer, "
        "const GstVideoInfoDmaDrm &videoInfo)': names 'GstBuffer', which "
        "has no cute class yet.")

  @staticmethod
  def gstBuffer(*__, **_) -> Never:
    """
    Qt's 'GstBuffer *QGStreamerInterface::gstBuffer(const QVideoFrame
    &frame)': gives 'struct _GstBuffer', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGStreamerInterface.gstBuffer' has no cute function yet. Qt's "
        "'GstBuffer *QGStreamerInterface::gstBuffer(const QVideoFrame "
        "&frame)': gives 'struct _GstBuffer', which has no cute class yet.")

  @staticmethod
  def gstPipeline(*__, **_) -> Never:
    """
    - Qt's 'GstPipeline *QGStreamerInterface::gstPipeline(QMediaPlayer *a0)':
      gives 'struct _GstPipeline', which has no cute class yet.
    - Qt's 'GstPipeline
      *QGStreamerInterface::gstPipeline(QMediaCaptureSession *a0)': gives
      'struct _GstPipeline', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGStreamerInterface.gstPipeline' has no cute function yet. Qt's "
        "'GstPipeline *QGStreamerInterface::gstPipeline(QMediaPlayer *a0)': "
        "gives 'struct _GstPipeline', which has no cute class yet. Qt's "
        "'GstPipeline "
        "*QGStreamerInterface::gstPipeline(QMediaCaptureSession *a0)': "
        "gives 'struct _GstPipeline', which has no cute class yet.")
