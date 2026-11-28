"""
QQuickTextureFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QImage
  from . import QQuickWindow, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextureFactory(QObject):
  """
  The cute side of Qt's QQuickTextureFactory: a plain Python object standing
  in front of one C++ QQuickTextureFactory.

  It is built on the cute 'QObject', as Qt's QQuickTextureFactory is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextureFactory that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr',
  'createTexture', 'textureSize', 'textureByteCount', 'image',
  'textureFactoryForImage'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextureFactory::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTextureFactory::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTextureFactory::~QQuickTextureFactory()': the destructor:
    Python never removes a C++ QQuickTextureFactory.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTextureFactory is created at the first use, not by
    'QQuickTextureFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextureFactory.
  - Qt tells when it has removed the C++ QQuickTextureFactory. Every call on
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
    Calls Qt's 'QString QQuickTextureFactory::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexturefactory.html#tr

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
    #  QString QQuickTextureFactory::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickTextureFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QImage)
  def textureFactoryForImage(
      image: QImage,
  ) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory
    *QQuickTextureFactory::textureFactoryForImage(const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexturefactory.html#textureFactoryForImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory
    #      *QQuickTextureFactory::textureFactoryForImage(const QImage &image)
    address = Rituals.call(
        'ritual_ZN20QQuickTextureFactory22textureFactoryForImageERK6QImage',
        CuteMixin._valueOf(image),
    )
    return QQuickTextureFactory._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextureFactory'

  #  A C++ QQuickTextureFactory Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextureFactory'

  #  The functions Qt calls itself that QQuickTextureFactory is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createTexture': (
          ('_ZNK20QQuickTextureFactory13createTextureEP12QQuickWindow',
           ('address', 'address', 'QtQuick:QSGTexture'),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'textureSize': (
          ('_ZNK20QQuickTextureFactory11textureSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
      'textureByteCount': (
          ('_ZNK20QQuickTextureFactory16textureByteCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'image': (
          ('_ZNK20QQuickTextureFactory5imageEv',
           ('address', 'value', 'QtGui:QImage'),
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
    Calls Qt's 'const QMetaObject *QQuickTextureFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexturefactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextureFactory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickTextureFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QQuickWindow)
  @overload(NoneType)
  def createTexture(
      self,
      window: Optional[QQuickWindow],
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QQuickTextureFactory::createTexture(QQuickWindow
    *window) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexturefactory.html#createTexture

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QQuickTextureFactory::createTexture(QQuickWindow *window)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickTextureFactory13createTextureEP12QQuickWindow',
        self._addressOf(window),
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickTextureFactory::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexturefactory.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickTextureFactory::textureSize() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickTextureFactory11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def textureByteCount(self) -> int:
    """
    Calls Qt's 'int QQuickTextureFactory::textureByteCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexturefactory.html#textureByteCount
    """
    #  int QQuickTextureFactory::textureByteCount() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickTextureFactory16textureByteCountEv',
    )

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickTextureFactory::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktexturefactory.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickTextureFactory::image() const
    ritual = 'ritual_ZNK20QQuickTextureFactory5imageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickTextureFactory5imageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

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
    'QQuickTextureFactory::QQuickTextureFactory()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktexturefactory.html#QQuickTextureFactory
    """
    #  QQuickTextureFactory::QQuickTextureFactory()
    self._noteCreation(QQuickTextureFactory, lambda: Rituals.call(
        'ritual_ZN20QQuickTextureFactoryC1Ev',
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
