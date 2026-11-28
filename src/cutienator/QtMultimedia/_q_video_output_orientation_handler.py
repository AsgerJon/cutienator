"""
QVideoOutputOrientationHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideooutputorientationhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QVideoOutputOrientationHandler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoOutputOrientationHandler(QObject):
  """
  The cute side of Qt's QVideoOutputOrientationHandler: a plain Python object
  standing in front of one C++ QVideoOutputOrientationHandler.

  It is built on the cute 'QObject', as Qt's QVideoOutputOrientationHandler
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoOutputOrientationHandler that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'currentOrientation', 'setIsRecording', 'isRecording',
  'orientationChanged', 'screenOrientationChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVideoOutputOrientationHandler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QVideoOutputOrientationHandler::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVideoOutputOrientationHandler is created at the first use, not
    by 'QVideoOutputOrientationHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoOutputOrientationHandler.
  - Qt tells when it has removed the C++ QVideoOutputOrientationHandler.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QVideoOutputOrientationHandler::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html#tr

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
    #  QString QVideoOutputOrientationHandler::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QVideoOutputOrientationHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(bool)
  def setIsRecording(isRecording: bool) -> None:
    """
    Calls Qt's 'void QVideoOutputOrientationHandler::setIsRecording(bool
    isRecording)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html#setIsRecording

    Parameters
    ----------

    isRecording : bool
      Passed on as it is.
    """
    #  void QVideoOutputOrientationHandler::setIsRecording(bool isRecording)
    Rituals.call(
        'ritual_ZN30QVideoOutputOrientationHandler14setIsRecordingEb',
        isRecording,
    )

  @staticmethod
  def isRecording() -> bool:
    """
    Calls Qt's 'bool QVideoOutputOrientationHandler::isRecording()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html#isRecording
    """
    #  bool QVideoOutputOrientationHandler::isRecording()
    return Rituals.call(
        'ritual_ZN30QVideoOutputOrientationHandler11isRecordingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoOutputOrientationHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QVideoOutputOrientationHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVideoOutputOrientationHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QVideoOutputOrientationHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentOrientation(self) -> int:
    """
    Calls Qt's 'int QVideoOutputOrientationHandler::currentOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html
    """
    #  int QVideoOutputOrientationHandler::currentOrientation() const
    return self.uglySide.call(
        'ritual_ZNK30QVideoOutputOrientationHandler18currentOrientationEv',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QVideoOutputOrientationHandler::QVideoOutputOrientationHandler(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVideoOutputOrientationHandler::QVideoOutputOrientationHandler(QObject
    #      *parent)
    self._noteCreation(QVideoOutputOrientationHandler, lambda: Rituals.call(
        'ritual_ZN30QVideoOutputOrientationHandlerC1EP7QObject',
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

  @overload(int)
  def orientationChanged(self, angle: int) -> None:
    """
    Calls Qt's 'void QVideoOutputOrientationHandler::orientationChanged(int
    angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void QVideoOutputOrientationHandler::orientationChanged(int angle)
    self.uglySide.call(
        'ritual_ZN30QVideoOutputOrientationHandler18orientationChangedEi',
        angle,
    )

  @overload(Qt.ScreenOrientation)
  def screenOrientationChanged(
      self,
      orientation: Qt.ScreenOrientation,
  ) -> None:
    """
    Calls Qt's 'void
    QVideoOutputOrientationHandler::screenOrientationChanged(Qt::
    ScreenOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideooutputorientationhandler.html

    Parameters
    ----------

    orientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  void QVideoOutputOrientationHandler::screenOrientationChanged(Qt::
    #      ScreenOrientation orientation)
    self.uglySide.call(
        'ritual_ZN30QVideoOutputOrientationHandler24screenOrientationChange'
        'dEN2Qt17ScreenOrientationE',
        orientation.value,
    )
