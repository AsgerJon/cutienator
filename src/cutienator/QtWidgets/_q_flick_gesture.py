"""
QFlickGesture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFlickGesture to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QGesture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QFlickGesturePrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFlickGesture(QGesture):
  """
  The cute side of Qt's QFlickGesture: a plain Python object standing in
  front of one C++ QFlickGesture.

  It is built on the cute 'QGesture', as Qt's QFlickGesture is built on Qt's
  QGesture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFlickGesture that has a ritual and that Python can
  call so far, 3 names in all: 'metaObject', 'tr', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFlickGesture::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QFlickGesture::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QFlickGesturePrivate *QFlickGesture::d_func() const': takes
    in Python what 'QFlickGesturePrivate *QFlickGesture::d_func()' takes.
  - Qt's 'QFlickGesture::~QFlickGesture()': the destructor: Python never
    removes a C++ QFlickGesture.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QFlickGesture is created at the first use, not by
    'QFlickGesture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFlickGesture.
  - Qt tells when it has removed the C++ QFlickGesture. Every call on the
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
    Calls Qt's 'QString QFlickGesture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qflickgesture.html#tr

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
    #  QString QFlickGesture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QFlickGesture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFlickGesture'

  #  A C++ QFlickGesture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFlickGesture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFlickGesture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qflickgesture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFlickGesture::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QFlickGesture10metaObjectEv')
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

  @overload(QObject, Qt.MouseButton)
  @overload(NoneType, Qt.MouseButton)
  @overload(QObject, Qt.MouseButton, QObject)
  @overload(QObject, Qt.MouseButton, NoneType)
  @overload(NoneType, Qt.MouseButton, QObject)
  @overload(NoneType, Qt.MouseButton, NoneType)
  def __init__(
      self,
      receiver: Optional[QObject],
      button: Qt.MouseButton,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QFlickGesture::QFlickGesture(QObject
    *receiver, Qt::MouseButton button, QObject *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qflickgesture.html#QFlickGesture

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    button : Qt.MouseButton
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFlickGesture::QFlickGesture(QObject *receiver, Qt::MouseButton
    #      button, QObject *parent)
    self._noteCreation(QFlickGesture, lambda: Rituals.call(
        'ritual_ZN13QFlickGestureC1EP7QObjectN2Qt11MouseButtonES1_',
        self._addressOf(receiver, 'QObject'), button.value,
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

  def d_func(self) -> Optional[QFlickGesturePrivate]:
    """
    Calls Qt's 'QFlickGesturePrivate *QFlickGesture::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qflickgesture.html#d_func

    Returns
    -------

    Optional[QFlickGesturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFlickGesturePrivate *QFlickGesture::d_func()
    address = self.uglySide.call('ritual_ZN13QFlickGesture6d_funcEv')
    from . import QFlickGesturePrivate
    return QFlickGesturePrivate._cuteAt(address)
