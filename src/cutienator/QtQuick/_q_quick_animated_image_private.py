"""
QQuickAnimatedImagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAnimatedImagePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickImagePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QMovie
  from ..QtQml import QQmlEngine
  from . import QQuickAnimatedImage, QQuickPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMovie = WAIT['QMovie']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatedImagePrivate(QQuickImagePrivate):
  """
  The cute side of Qt's QQuickAnimatedImagePrivate: a plain Python object
  standing in front of one C++ QQuickAnimatedImagePrivate.

  It is built on the cute 'QQuickImagePrivate', as Qt's
  QQuickAnimatedImagePrivate is built on Qt's QQuickImagePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatedImagePrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func',
  'infoForCurrentFrame', 'setMovie', 'clearCache', 'handleLoopCompletion'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAnimatedImage *QQuickAnimatedImagePrivate::q_func()
    const': takes in Python what 'QQuickAnimatedImage
    *QQuickAnimatedImagePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickAnimatedImagePrivate is created at the first use, not by
    'QQuickAnimatedImagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatedImagePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatedImagePrivate'

  #  A C++ QQuickAnimatedImagePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimatedImagePrivate'

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

  @overload(QMovie)
  @overload(NoneType)
  def setMovie(self, movie: Optional[QMovie]) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImagePrivate::setMovie(QMovie *movie)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimageprivate.html#setMovie

    Parameters
    ----------

    movie : Optional[QMovie]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatedImagePrivate::setMovie(QMovie *movie)
    self.uglySide.call(
        'ritual_ZN26QQuickAnimatedImagePrivate8setMovieEP6QMovie',
        self._addressOf(movie),
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
    'QQuickAnimatedImagePrivate::QQuickAnimatedImagePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimageprivate.html
    """
    #  QQuickAnimatedImagePrivate::QQuickAnimatedImagePrivate()
    self._noteCreation(QQuickAnimatedImagePrivate, lambda: Rituals.call(
        'ritual_ZN26QQuickAnimatedImagePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickAnimatedImage]:
    """
    Calls Qt's 'QQuickAnimatedImage *QQuickAnimatedImagePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimageprivate.html#q_func

    Returns
    -------

    Optional[QQuickAnimatedImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatedImage *QQuickAnimatedImagePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QQuickAnimatedImagePrivate6q_funcEv',
    )
    from . import QQuickAnimatedImage
    return QQuickAnimatedImage._cuteAt(address)

  @overload(QQmlEngine)
  @overload(NoneType)
  def infoForCurrentFrame(
      self,
      engine: Optional[QQmlEngine],
  ) -> Optional[QQuickPixmap]:
    """
    Calls Qt's 'QQuickPixmap
    *QQuickAnimatedImagePrivate::infoForCurrentFrame(QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimageprivate.html

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPixmap
    #      *QQuickAnimatedImagePrivate::infoForCurrentFrame(QQmlEngine
    #      *engine)
    address = self.uglySide.call(
        'ritual_ZN26QQuickAnimatedImagePrivate19infoForCurrentFrameEP10QQml'
        'Engine',
        self._addressOf(engine),
    )
    from . import QQuickPixmap
    return QQuickPixmap._cuteAt(address)

  def clearCache(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImagePrivate::clearCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimageprivate.html#clearCache
    """
    #  void QQuickAnimatedImagePrivate::clearCache()
    self.uglySide.call('ritual_ZN26QQuickAnimatedImagePrivate10clearCacheEv')

  def handleLoopCompletion(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImagePrivate::handleLoopCompletion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimageprivate.html
    """
    #  void QQuickAnimatedImagePrivate::handleLoopCompletion()
    self.uglySide.call(
        'ritual_ZN26QQuickAnimatedImagePrivate20handleLoopCompletionEv',
    )
