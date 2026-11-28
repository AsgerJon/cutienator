"""
SeriesRenderCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/seriesrendercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SeriesRenderCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QImage, QQuaternion, QVector4D
  from . import ObjectHelper, QAbstract3DSeries, TextureHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  TextureHelper = WAIT['TextureHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SeriesRenderCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's SeriesRenderCache: a plain Python object standing in
  front of one C++ SeriesRenderCache.

  C++ hands a SeriesRenderCache around as a copy, so every C++
  SeriesRenderCache behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's SeriesRenderCache that has a ritual and that Python
  can call so far, 23 names in all: 'populate', 'cleanup', 'series',
  'meshRotation', 'setMeshRotation', 'object', 'baseColor',
  'baseUniformTexture', 'baseGradientTexture', 'gradientImage',
  'singleHighlightColor', 'singleHighlightGradientTexture',
  'multiHighlightColor', 'multiHighlightGradientTexture', 'name',
  'itemLabel', 'setValid', 'isValid', 'isVisible', 'setDataDirty',
  'dataDirty', 'setStaticObjectUVDirty', 'staticObjectUVDirty'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SeriesRenderCache::~SeriesRenderCache()': the destructor: Python
    removes its C++ SeriesRenderCache by it, and has no other use for it.
  - Qt's 'const QAbstract3DSeries::Mesh &SeriesRenderCache::mesh() const':
    gives a type Python has no way to take yet.
  - Qt's 'const Q3DTheme::ColorStyle &SeriesRenderCache::colorStyle() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 27 functions Qt declares: 1 leans on 'SeriesRenderCache.

  What to expect
  --------------

  - The C++ SeriesRenderCache is created at the first use, not by
    'SeriesRenderCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a SeriesRenderCache back gives a copy the ritual made
    for Python, in a new cute SeriesRenderCache.
  - Each name of Qt's SeriesRenderCache that has no cute function yet,
    '__init__', 'colorStyle', 'mesh', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SeriesRenderCache'

  #  A C++ SeriesRenderCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SeriesRenderCache'

  #  The functions Qt calls itself that SeriesRenderCache is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'populate': (
          ('_ZN17SeriesRenderCache8populateEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'cleanup': (
          ('_ZN17SeriesRenderCache7cleanupEP13TextureHelper',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:TextureHelper'),
           )),
      ),
  }

  #  Qt's '~SeriesRenderCache()'. Naming it makes this a value class: Python
  #  owns every C++ SeriesRenderCache behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17SeriesRenderCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def series(self) -> Optional[QAbstract3DSeries]:
    """
    Calls Qt's 'QAbstract3DSeries *SeriesRenderCache::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#series

    Returns
    -------

    Optional[QAbstract3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DSeries *SeriesRenderCache::series() const
    address = self.uglySide.call('ritual_ZNK17SeriesRenderCache6seriesEv')
    from . import QAbstract3DSeries
    return QAbstract3DSeries._cuteAt(address)

  def meshRotation(self) -> QQuaternion:
    """
    Calls Qt's 'const QQuaternion &SeriesRenderCache::meshRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#meshRotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  const QQuaternion &SeriesRenderCache::meshRotation() const
    address = self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache12meshRotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def object(self) -> Optional[ObjectHelper]:
    """
    Calls Qt's 'ObjectHelper *SeriesRenderCache::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#object

    Returns
    -------

    Optional[ObjectHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ObjectHelper *SeriesRenderCache::object() const
    address = self.uglySide.call('ritual_ZNK17SeriesRenderCache6objectEv')
    from . import ObjectHelper
    return ObjectHelper._cuteAt(address)

  def baseColor(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &SeriesRenderCache::baseColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#baseColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &SeriesRenderCache::baseColor() const
    address = self.uglySide.call('ritual_ZNK17SeriesRenderCache9baseColorEv')
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def baseUniformTexture(self) -> int:
    """
    Calls Qt's 'const GLuint &SeriesRenderCache::baseUniformTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#baseUniformTexture
    """
    #  const GLuint &SeriesRenderCache::baseUniformTexture() const
    return self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache18baseUniformTextureEv',
    )

  def baseGradientTexture(self) -> int:
    """
    Calls Qt's 'const GLuint &SeriesRenderCache::baseGradientTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#baseGradientTexture
    """
    #  const GLuint &SeriesRenderCache::baseGradientTexture() const
    return self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache19baseGradientTextureEv',
    )

  def gradientImage(self) -> QImage:
    """
    Calls Qt's 'const QImage &SeriesRenderCache::gradientImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#gradientImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  const QImage &SeriesRenderCache::gradientImage() const
    address = self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache13gradientImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def singleHighlightColor(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &SeriesRenderCache::singleHighlightColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#singleHighlightColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &SeriesRenderCache::singleHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache20singleHighlightColorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def singleHighlightGradientTexture(self) -> int:
    """
    Calls Qt's 'const GLuint
    &SeriesRenderCache::singleHighlightGradientTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html
    """
    #  const GLuint &SeriesRenderCache::singleHighlightGradientTexture()
    #      const
    return self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache30singleHighlightGradientTextureEv',
    )

  def multiHighlightColor(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &SeriesRenderCache::multiHighlightColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#multiHighlightColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &SeriesRenderCache::multiHighlightColor() const
    address = self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache19multiHighlightColorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def multiHighlightGradientTexture(self) -> int:
    """
    Calls Qt's 'const GLuint
    &SeriesRenderCache::multiHighlightGradientTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html
    """
    #  const GLuint &SeriesRenderCache::multiHighlightGradientTexture() const
    return self.uglySide.call(
        'ritual_ZNK17SeriesRenderCache29multiHighlightGradientTextureEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'const QString &SeriesRenderCache::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &SeriesRenderCache::name() const
    return self.uglySide.call('ritual_ZNK17SeriesRenderCache4nameEv')

  def itemLabel(self) -> str:
    """
    Calls Qt's 'const QString &SeriesRenderCache::itemLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#itemLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &SeriesRenderCache::itemLabel() const
    return self.uglySide.call('ritual_ZNK17SeriesRenderCache9itemLabelEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool SeriesRenderCache::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#isValid
    """
    #  bool SeriesRenderCache::isValid() const
    return self.uglySide.call('ritual_ZNK17SeriesRenderCache7isValidEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool SeriesRenderCache::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#isVisible
    """
    #  bool SeriesRenderCache::isVisible() const
    return self.uglySide.call('ritual_ZNK17SeriesRenderCache9isVisibleEv')

  def dataDirty(self) -> bool:
    """
    Calls Qt's 'bool SeriesRenderCache::dataDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#dataDirty
    """
    #  bool SeriesRenderCache::dataDirty() const
    return self.uglySide.call('ritual_ZNK17SeriesRenderCache9dataDirtyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuaternion)
  def setMeshRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void SeriesRenderCache::setMeshRotation(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#setMeshRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void SeriesRenderCache::setMeshRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN17SeriesRenderCache15setMeshRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(bool)
  def setValid(self, valid: bool) -> None:
    """
    Calls Qt's 'void SeriesRenderCache::setValid(bool valid)'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#setValid

    Parameters
    ----------

    valid : bool
      Passed on as it is.
    """
    #  void SeriesRenderCache::setValid(bool valid)
    self.uglySide.call('ritual_ZN17SeriesRenderCache8setValidEb', valid)

  @overload(bool)
  def setDataDirty(self, state: bool) -> None:
    """
    Calls Qt's 'void SeriesRenderCache::setDataDirty(bool state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#setDataDirty

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void SeriesRenderCache::setDataDirty(bool state)
    self.uglySide.call('ritual_ZN17SeriesRenderCache12setDataDirtyEb', state)

  @overload(bool)
  def setStaticObjectUVDirty(self, state: bool) -> None:
    """
    Calls Qt's 'void SeriesRenderCache::setStaticObjectUVDirty(bool state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#setStaticObjectUVDirty

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void SeriesRenderCache::setStaticObjectUVDirty(bool state)
    self.uglySide.call(
        'ritual_ZN17SeriesRenderCache22setStaticObjectUVDirtyEb', state,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'SeriesRenderCache::SeriesRenderCache(QAbstract3DSeries *series,
    Abstract3DRenderer *renderer)': leans on
    'SeriesRenderCache::populate(bool)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'SeriesRenderCache.__init__' has no cute function yet. Qt's "
        "'SeriesRenderCache::SeriesRenderCache(QAbstract3DSeries *series, "
        "Abstract3DRenderer *renderer)': leans on "
        "'SeriesRenderCache::populate(bool)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(bool)
  def populate(self, newSeries: bool) -> None:
    """
    Calls Qt's 'void SeriesRenderCache::populate(bool newSeries)'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#populate

    Parameters
    ----------

    newSeries : bool
      Passed on as it is.
    """
    #  void SeriesRenderCache::populate(bool newSeries)
    self.uglySide.call('ritual_ZN17SeriesRenderCache8populateEb', newSeries)

  @overload(TextureHelper)
  @overload(NoneType)
  def cleanup(self, texHelper: Optional[TextureHelper]) -> None:
    """
    Calls Qt's 'void SeriesRenderCache::cleanup(TextureHelper *texHelper)'.

    Qt's own words: https://doc.qt.io/qt-6/seriesrendercache.html#cleanup

    Parameters
    ----------

    texHelper : Optional[TextureHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SeriesRenderCache::cleanup(TextureHelper *texHelper)
    self.uglySide.call(
        'ritual_ZN17SeriesRenderCache7cleanupEP13TextureHelper',
        self._addressOf(texHelper),
    )

  def staticObjectUVDirty(self) -> bool:
    """
    Calls Qt's 'bool SeriesRenderCache::staticObjectUVDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/seriesrendercache.html#staticObjectUVDirty
    """
    #  bool SeriesRenderCache::staticObjectUVDirty()
    return self.uglySide.call(
        'ritual_ZN17SeriesRenderCache19staticObjectUVDirtyEv',
    )

  @staticmethod
  def colorStyle(*__, **_) -> Never:
    """
    Qt's 'const Q3DTheme::ColorStyle &SeriesRenderCache::colorStyle() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SeriesRenderCache.colorStyle' has no cute function yet. Qt's "
        "'const Q3DTheme::ColorStyle &SeriesRenderCache::colorStyle() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def mesh(*__, **_) -> Never:
    """
    Qt's 'const QAbstract3DSeries::Mesh &SeriesRenderCache::mesh() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SeriesRenderCache.mesh' has no cute function yet. Qt's 'const "
        "QAbstract3DSeries::Mesh &SeriesRenderCache::mesh() const': gives a "
        "type Python has no way to take yet.")
