"""
QBlendStyleAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBlendStyleAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QStyleAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlendStyleAnimation(QStyleAnimation):
  """
  The cute side of Qt's QBlendStyleAnimation: a plain Python object standing
  in front of one C++ QBlendStyleAnimation.

  It is built on the cute 'QStyleAnimation', as Qt's QBlendStyleAnimation is
  built on Qt's QStyleAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBlendStyleAnimation that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'startImage',
  'setStartImage', 'endImage', 'setEndImage', 'currentImage',
  'updateCurrentTime'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBlendStyleAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBlendStyleAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBlendStyleAnimation is created at the first use, not by
    'QBlendStyleAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBlendStyleAnimation.
  - Qt tells when it has removed the C++ QBlendStyleAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBlendStyleAnimation, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QBlendStyleAnimation::Type' of Qt, with the 2 names Qt gives in
    it.
    """

    Transition = Kee[int](0)
    Pulse = Kee[int](1)

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
    Calls Qt's 'QString QBlendStyleAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qblendstyleanimation.html#tr

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
    #  QString QBlendStyleAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QBlendStyleAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBlendStyleAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBlendStyleAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBlendStyleAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QBlendStyleAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def startImage(self) -> QImage:
    """
    Calls Qt's 'QImage QBlendStyleAnimation::startImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#startImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QBlendStyleAnimation::startImage() const
    address = self.uglySide.call(
        'ritual_ZNK20QBlendStyleAnimation10startImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def endImage(self) -> QImage:
    """
    Calls Qt's 'QImage QBlendStyleAnimation::endImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblendstyleanimation.html#endImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QBlendStyleAnimation::endImage() const
    address = self.uglySide.call(
        'ritual_ZNK20QBlendStyleAnimation8endImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def currentImage(self) -> QImage:
    """
    Calls Qt's 'QImage QBlendStyleAnimation::currentImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#currentImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QBlendStyleAnimation::currentImage() const
    address = self.uglySide.call(
        'ritual_ZNK20QBlendStyleAnimation12currentImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QImage)
  def setStartImage(self, image: QImage) -> None:
    """
    Calls Qt's 'void QBlendStyleAnimation::setStartImage(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#setStartImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QBlendStyleAnimation::setStartImage(const QImage &image)
    self.uglySide.call(
        'ritual_ZN20QBlendStyleAnimation13setStartImageERK6QImage',
        self._valueOf(image),
    )

  @overload(QImage)
  def setEndImage(self, image: QImage) -> None:
    """
    Calls Qt's 'void QBlendStyleAnimation::setEndImage(const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#setEndImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QBlendStyleAnimation::setEndImage(const QImage &image)
    self.uglySide.call(
        'ritual_ZN20QBlendStyleAnimation11setEndImageERK6QImage',
        self._valueOf(image),
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

  @overload(Type, QObject)
  @overload(Type, NoneType)
  def __init__(self, type: Type, target: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QBlendStyleAnimation::QBlendStyleAnimation(Type type, QObject *target)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#QBlendStyleAnimation

    Parameters
    ----------

    type : Type
      Passed on as its number.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBlendStyleAnimation::QBlendStyleAnimation(Type type, QObject *target)
    self._noteCreation(QBlendStyleAnimation, lambda: Rituals.call(
        'ritual_ZN20QBlendStyleAnimationC1ENS_4TypeEP7QObject',
        type.value, self._addressOf(target, 'QObject'),
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
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QBlendStyleAnimation::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendstyleanimation.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QBlendStyleAnimation::updateCurrentTime(int time)
    ritual = 'ritual_ZN20QBlendStyleAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QBlendStyleAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, time)
