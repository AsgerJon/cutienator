"""
QQuickImagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickimage_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickImagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickImageBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QImage
  from . import QQuickImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class QQuickImagePrivate(QQuickImageBasePrivate):
  """
  The cute side of Qt's QQuickImagePrivate: a plain Python object standing in
  front of one C++ QQuickImagePrivate.

  It is built on the cute 'QQuickImageBasePrivate', as Qt's
  QQuickImagePrivate is built on Qt's QQuickImageBasePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImagePrivate that has a ritual and that Python
  can call so far, 2 names in all: 'q_func', 'setImage'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickImage *QQuickImagePrivate::q_func() const': takes in
    Python what 'QQuickImage *QQuickImagePrivate::q_func()' takes.
  - Qt's 'void QQuickImagePrivate::setPixmap(const QQuickPixmap &pixmap)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQuickImagePrivate is created at the first use, not by
    'QQuickImagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImagePrivate.
  - Each name of Qt's QQuickImagePrivate that has no cute function yet,
    'setPixmap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImagePrivate'

  #  A C++ QQuickImagePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImagePrivate'

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

  @overload(QImage)
  def setImage(self, img: QImage) -> None:
    """
    Calls Qt's 'void QQuickImagePrivate::setImage(const QImage &img)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageprivate.html#setImage

    Parameters
    ----------

    img : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickImagePrivate::setImage(const QImage &img)
    self.uglySide.call(
        'ritual_ZN18QQuickImagePrivate8setImageERK6QImage',
        self._valueOf(img),
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
    'QQuickImagePrivate::QQuickImagePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprivate.html#QQuickImagePrivate
    """
    #  QQuickImagePrivate::QQuickImagePrivate()
    self._noteCreation(QQuickImagePrivate, lambda: Rituals.call(
        'ritual_ZN18QQuickImagePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickImage]:
    """
    Calls Qt's 'QQuickImage *QQuickImagePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageprivate.html#q_func

    Returns
    -------

    Optional[QQuickImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImage *QQuickImagePrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QQuickImagePrivate6q_funcEv')
    from . import QQuickImage
    return QQuickImage._cuteAt(address)

  @staticmethod
  def setPixmap(*__, **_) -> Never:
    """
    Qt's 'void QQuickImagePrivate::setPixmap(const QQuickPixmap &pixmap)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickImagePrivate.setPixmap' has no cute function yet. Qt's "
        "'void QQuickImagePrivate::setPixmap(const QQuickPixmap &pixmap)': "
        "takes a type Python has no way to hand over yet.")
