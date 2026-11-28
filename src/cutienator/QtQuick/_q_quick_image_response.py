"""
QQuickImageResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickImageResponsePrivate, QQuickTextureFactory

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickImageResponse(QObject):
  """
  The cute side of Qt's QQuickImageResponse: a plain Python object standing
  in front of one C++ QQuickImageResponse.

  It is built on the cute 'QObject', as Qt's QQuickImageResponse is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageResponse that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr',
  'textureFactory', 'errorString', 'cancel', 'finished', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImageResponse::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickImageResponse::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickImageResponse::~QQuickImageResponse()': the destructor:
    Python never removes a C++ QQuickImageResponse.
  - Qt's 'const QQuickImageResponsePrivate *QQuickImageResponse::d_func()
    const': takes in Python what 'QQuickImageResponsePrivate
    *QQuickImageResponse::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickImageResponse is created at the first use, not by
    'QQuickImageResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageResponse.
  - Qt tells when it has removed the C++ QQuickImageResponse. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickImageResponse::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageresponse.html#tr

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
    #  QString QQuickImageResponse::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickImageResponse2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageResponse'

  #  A C++ QQuickImageResponse Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageResponse'

  #  The functions Qt calls itself that QQuickImageResponse is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'textureFactory': (
          ('_ZNK19QQuickImageResponse14textureFactoryEv',
           ('address', 'address', 'QtQuick:QQuickTextureFactory'),
           ()),
      ),
      'errorString': (
          ('_ZNK19QQuickImageResponse11errorStringEv',
           ('address', 'text', ''),
           ()),
      ),
      'cancel': (
          ('_ZN19QQuickImageResponse6cancelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickImageResponse::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageresponse.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImageResponse::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageResponse10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureFactory(self) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory *QQuickImageResponse::textureFactory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageresponse.html#textureFactory

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory *QQuickImageResponse::textureFactory() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageResponse14textureFactoryEv',
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QQuickImageResponse::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageresponse.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImageResponse::errorString() const
    ritual = 'ritual_ZNK19QQuickImageResponse11errorStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickImageResponse11errorStringEv'
    return self.uglySide.call(ritual)

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
    'QQuickImageResponse::QQuickImageResponse()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageresponse.html#QQuickImageResponse
    """
    #  QQuickImageResponse::QQuickImageResponse()
    self._noteCreation(QQuickImageResponse, lambda: Rituals.call(
        'ritual_ZN19QQuickImageResponseC1Ev',
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

  def cancel(self) -> None:
    """
    Calls Qt's 'void QQuickImageResponse::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageresponse.html#cancel
    """
    #  void QQuickImageResponse::cancel()
    ritual = 'ritual_ZN19QQuickImageResponse6cancelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickImageResponse6cancelEv'
    self.uglySide.call(ritual)

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickImageResponse::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageresponse.html#finished
    """
    #  void QQuickImageResponse::finished()
    self.uglySide.call('ritual_ZN19QQuickImageResponse8finishedEv')

  def d_func(self) -> Optional[QQuickImageResponsePrivate]:
    """
    Calls Qt's 'QQuickImageResponsePrivate *QQuickImageResponse::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageresponse.html#d_func

    Returns
    -------

    Optional[QQuickImageResponsePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickImageResponsePrivate *QQuickImageResponse::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickImageResponse6d_funcEv')
    from . import QQuickImageResponsePrivate
    return QQuickImageResponsePrivate._cuteAt(address)
