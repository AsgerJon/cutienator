"""
QQuickMediaPlayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickmediaplayer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMediaPlayer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtMultimedia import QMediaPlayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMediaPlayer(QMediaPlayer):
  """
  The cute side of Qt's QQuickMediaPlayer: a plain Python object standing in
  front of one C++ QQuickMediaPlayer.

  It is built on the cute 'QMediaPlayer', as Qt's QQuickMediaPlayer is built
  on Qt's QMediaPlayer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMediaPlayer that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'autoPlay',
  'setAutoPlay', 'onMediaStatusChanged', 'autoPlayChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMediaPlayer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMediaPlayer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickMediaPlayer is created at the first use, not by
    'QQuickMediaPlayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMediaPlayer.
  - Qt tells when it has removed the C++ QQuickMediaPlayer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickMediaPlayer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmediaplayer.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMediaPlayer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickMediaPlayer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMediaPlayer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMediaPlayer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmediaplayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMediaPlayer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickMediaPlayer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def autoPlay(self) -> bool:
    """
    Calls Qt's 'bool QQuickMediaPlayer::autoPlay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmediaplayer.html#autoPlay
    """
    #  bool QQuickMediaPlayer::autoPlay() const
    return self.uglySide.call('ritual_ZNK17QQuickMediaPlayer8autoPlayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoPlay(self, autoPlay: bool) -> None:
    """
    Calls Qt's 'void QQuickMediaPlayer::setAutoPlay(bool autoPlay)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmediaplayer.html#setAutoPlay

    Parameters
    ----------

    autoPlay : bool
      Passed on as it is.
    """
    #  void QQuickMediaPlayer::setAutoPlay(bool autoPlay)
    self.uglySide.call(
        'ritual_ZN17QQuickMediaPlayer11setAutoPlayEb', autoPlay,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMediaPlayer::QQuickMediaPlayer(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmediaplayer.html#QQuickMediaPlayer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMediaPlayer::QQuickMediaPlayer(QObject *parent)
    self._noteCreation(QQuickMediaPlayer, lambda: Rituals.call(
        'ritual_ZN17QQuickMediaPlayerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QMediaPlayer.MediaStatus)
  def onMediaStatusChanged(self, status: QMediaPlayer.MediaStatus) -> None:
    """
    Calls Qt's 'void
    QQuickMediaPlayer::onMediaStatusChanged(QMediaPlayer::MediaStatus
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmediaplayer.html#onMediaStatusChanged

    Parameters
    ----------

    status : QMediaPlayer.MediaStatus
      Passed on as its number.
    """
    #  void QQuickMediaPlayer::onMediaStatusChanged(QMediaPlayer::MediaStatus
    #      status)
    self.uglySide.call(
        'ritual_ZN17QQuickMediaPlayer20onMediaStatusChangedEN12QMediaPlayer'
        '11MediaStatusE',
        status.value,
    )

  @overload(bool)
  def autoPlayChanged(self, autoPlay: bool) -> None:
    """
    Calls Qt's 'void QQuickMediaPlayer::autoPlayChanged(bool autoPlay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmediaplayer.html#autoPlayChanged

    Parameters
    ----------

    autoPlay : bool
      Passed on as it is.
    """
    #  void QQuickMediaPlayer::autoPlayChanged(bool autoPlay)
    self.uglySide.call(
        'ritual_ZN17QQuickMediaPlayer15autoPlayChangedEb', autoPlay,
    )
