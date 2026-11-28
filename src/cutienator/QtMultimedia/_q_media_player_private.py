"""
QMediaPlayerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qmediaplayer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QMediaPlayerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate
from . import QMediaPlayer, QPlatformMediaPlayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMediaMetaData, QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVideoSink = WAIT['QVideoSink']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaPlayerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QMediaPlayerPrivate: a plain Python object standing
  in front of one C++ QMediaPlayerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QMediaPlayerPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaPlayerPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'q_func', 'get', 'trackMetaData',
  'setState', 'setStatus', 'setError', 'setVideoSink'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMediaPlayer *QMediaPlayerPrivate::q_func() const': takes in
    Python what 'QMediaPlayer *QMediaPlayerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 leans on 'QtMultimediaPrivate.

  What to expect
  --------------

  - The C++ QMediaPlayerPrivate is created at the first use, not by
    'QMediaPlayerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaPlayerPrivate.
  - Each name of Qt's QMediaPlayerPrivate that has no cute function yet,
    'setMedia', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMediaPlayer)
  @overload(NoneType)
  def get(session: Optional[QMediaPlayer]) -> Optional[QMediaPlayerPrivate]:
    """
    Calls Qt's 'QMediaPlayerPrivate *QMediaPlayerPrivate::get(QMediaPlayer
    *session)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayerprivate.html#get

    Parameters
    ----------

    session : Optional[QMediaPlayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMediaPlayerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaPlayerPrivate *QMediaPlayerPrivate::get(QMediaPlayer *session)
    address = Rituals.call(
        'ritual_ZN19QMediaPlayerPrivate3getEP12QMediaPlayer',
        CuteMixin._addressOf(session),
    )
    return QMediaPlayerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaPlayerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlatformMediaPlayer.TrackType)
  def trackMetaData(
      self,
      s: QPlatformMediaPlayer.TrackType,
  ) -> QList[QMediaMetaData]:
    """
    Calls Qt's 'QList<QMediaMetaData>
    QMediaPlayerPrivate::trackMetaData(QPlatformMediaPlayer::TrackType s)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayerprivate.html#trackMetaData

    Parameters
    ----------

    s : QPlatformMediaPlayer.TrackType
      Passed on as its number.

    Returns
    -------

    QList[QMediaMetaData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMediaMetaData>
    #      QMediaPlayerPrivate::trackMetaData(QPlatformMediaPlayer::TrackType
    #      s) const
    address = self.uglySide.call(
        'ritual_ZNK19QMediaPlayerPrivate13trackMetaDataEN20QPlatformMediaPl'
        'ayer9TrackTypeE',
        s.value,
    )
    from . import QMediaMetaData
    return QList[QMediaMetaData]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaPlayer.PlaybackState)
  def setState(self, state: QMediaPlayer.PlaybackState) -> None:
    """
    Calls Qt's 'void
    QMediaPlayerPrivate::setState(QMediaPlayer::PlaybackState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayerprivate.html#setState

    Parameters
    ----------

    state : QMediaPlayer.PlaybackState
      Passed on as its number.
    """
    #  void QMediaPlayerPrivate::setState(QMediaPlayer::PlaybackState state)
    self.uglySide.call(
        'ritual_ZN19QMediaPlayerPrivate8setStateEN12QMediaPlayer13PlaybackS'
        'tateE',
        state.value,
    )

  @overload(QMediaPlayer.MediaStatus)
  def setStatus(self, status: QMediaPlayer.MediaStatus) -> None:
    """
    Calls Qt's 'void QMediaPlayerPrivate::setStatus(QMediaPlayer::MediaStatus
    status)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayerprivate.html#setStatus

    Parameters
    ----------

    status : QMediaPlayer.MediaStatus
      Passed on as its number.
    """
    #  void QMediaPlayerPrivate::setStatus(QMediaPlayer::MediaStatus status)
    self.uglySide.call(
        'ritual_ZN19QMediaPlayerPrivate9setStatusEN12QMediaPlayer11MediaSta'
        'tusE',
        status.value,
    )

  @overload(QMediaPlayer.Error, str)
  def setError(self, error: QMediaPlayer.Error, errorString: str) -> None:
    """
    Calls Qt's 'void QMediaPlayerPrivate::setError(QMediaPlayer::Error error,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayerprivate.html#setError

    Parameters
    ----------

    error : QMediaPlayer.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMediaPlayerPrivate::setError(QMediaPlayer::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN19QMediaPlayerPrivate8setErrorEN12QMediaPlayer5ErrorERK7Q'
        'String',
        error.value, errorString,
    )

  @overload(QVideoSink)
  @overload(NoneType)
  def setVideoSink(self, sink: Optional[QVideoSink]) -> None:
    """
    Calls Qt's 'void QMediaPlayerPrivate::setVideoSink(QVideoSink *sink)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayerprivate.html#setVideoSink

    Parameters
    ----------

    sink : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaPlayerPrivate::setVideoSink(QVideoSink *sink)
    self.uglySide.call(
        'ritual_ZN19QMediaPlayerPrivate12setVideoSinkEP10QVideoSink',
        self._addressOf(sink),
    )

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
    'QMediaPlayerPrivate::QMediaPlayerPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaplayerprivate.html#QMediaPlayerPrivate
    """
    #  QMediaPlayerPrivate::QMediaPlayerPrivate()
    self._noteCreation(QMediaPlayerPrivate, lambda: Rituals.call(
        'ritual_ZN19QMediaPlayerPrivateC1Ev',
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

  def q_func(self) -> Optional[QMediaPlayer]:
    """
    Calls Qt's 'QMediaPlayer *QMediaPlayerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediaplayerprivate.html#q_func

    Returns
    -------

    Optional[QMediaPlayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaPlayer *QMediaPlayerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QMediaPlayerPrivate6q_funcEv')
    return QMediaPlayer._cuteAt(address)

  @staticmethod
  def setMedia(*__, **_) -> Never:
    """
    Qt's 'void QMediaPlayerPrivate::setMedia(QUrl media, QIODevice *stream)':
    leans on 'QtMultimediaPrivate::qCopyQrcToTemporaryFile(QFile&, QUrl
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMediaPlayerPrivate.setMedia' has no cute function yet. Qt's "
        "'void QMediaPlayerPrivate::setMedia(QUrl media, QIODevice "
        "*stream)': leans on "
        "'QtMultimediaPrivate::qCopyQrcToTemporaryFile(QFile&, QUrl "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
