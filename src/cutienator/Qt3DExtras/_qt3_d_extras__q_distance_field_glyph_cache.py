"""
Qt3DExtras::QDistanceFieldGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qdistancefieldglyphcache_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DExtras::QDistanceFieldGlyphCache to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRawFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRawFont = WAIT['QRawFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDistanceFieldGlyphCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DExtras::QDistanceFieldGlyphCache: a plain Python
  object standing in front of one C++ Qt3DExtras::QDistanceFieldGlyphCache.

  C++ hands a Qt3DExtras::QDistanceFieldGlyphCache around as a copy, so every
  C++ Qt3DExtras::QDistanceFieldGlyphCache behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QDistanceFieldGlyphCache that has a
  ritual and that Python can call so far, 3 names in all: 'setRootNode',
  'rootNode', 'fontKey'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DExtras::QDistanceFieldGlyphCache::~QDistanceFieldGlyphCache()':
    the destructor: Python removes its C++
    Qt3DExtras::QDistanceFieldGlyphCache by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 the
  compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DExtras::QDistanceFieldGlyphCache is created at the first use,
    not by 'Qt3DExtras::QDistanceFieldGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DExtras::QDistanceFieldGlyphCache back gives a
    copy the ritual made for Python, in a new cute
    Qt3DExtras::QDistanceFieldGlyphCache.
  - Each name of Qt's Qt3DExtras::QDistanceFieldGlyphCache that has no cute
    function yet, 'derefGlyph', 'derefGlyphs', 'doubleGlyphResolution',
    'getOrCreateDistanceFieldFont', 'refGlyph', 'refGlyphs', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside Qt3DExtras::QDistanceFieldGlyphCache, each
  #  a class in here as in C++.

  class Glyph(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DExtras::QDistanceFieldGlyphCache::Glyph: a
    plain Python object standing in front of one C++
    Qt3DExtras::QDistanceFieldGlyphCache::Glyph.

    C++ hands a Qt3DExtras::QDistanceFieldGlyphCache::Glyph around as a copy,
    so every C++ Qt3DExtras::QDistanceFieldGlyphCache::Glyph behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DExtras::QDistanceFieldGlyphCache::Glyph yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DExtras::QDistanceFieldGlyphCache::Glyph::~Glyph()': the
      destructor: Python removes its C++
      Qt3DExtras::QDistanceFieldGlyphCache::Glyph by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ Qt3DExtras::QDistanceFieldGlyphCache::Glyph is created at the
      first use, not by 'Qt3DExtras::QDistanceFieldGlyphCache::Glyph(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DExtras::QDistanceFieldGlyphCache::Glyph back
      gives a copy the ritual made for Python, in a new cute
      Qt3DExtras::QDistanceFieldGlyphCache::Glyph.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DExtras::QDistanceFieldGlyphCache::Glyph'

    #  Qt's '~Qt3DExtras::QDistanceFieldGlyphCache::Glyph()'. Naming it makes
    #  this a value class: Python owns every C++
    #  Qt3DExtras::QDistanceFieldGlyphCache::Glyph behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCache5GlyphD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRawFont)
  def fontKey(font: QRawFont) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QDistanceFieldGlyphCache::fontKey(const
    QRawFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdistancefieldglyphcache.html#fontKey

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QDistanceFieldGlyphCache::fontKey(const QRawFont
    #      &font)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCache7fontKeyERK8QRawFon'
        't',
        CuteMixin._valueOf(font),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QDistanceFieldGlyphCache'

  #  Qt's '~Qt3DExtras::QDistanceFieldGlyphCache()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DExtras::QDistanceFieldGlyphCache
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rootNode(self) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'Qt3DCore::QNode
    *Qt3DExtras::QDistanceFieldGlyphCache::rootNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdistancefieldglyphcache.html#rootNode

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QNode *Qt3DExtras::QDistanceFieldGlyphCache::rootNode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDistanceFieldGlyphCache8rootNodeEv',
    )
    return Qt3DCore.QNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def setRootNode(self, rootNode: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDistanceFieldGlyphCache::setRootNode(Qt3DCore::QNode
    *rootNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdistancefieldglyphcache.html

    Parameters
    ----------

    rootNode : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QDistanceFieldGlyphCache::setRootNode(Qt3DCore::QNode
    #      *rootNode)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCache11setRootNodeEPN8Qt'
        '3DCore5QNodeE',
        self._addressOf(rootNode),
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
    'Qt3DExtras::QDistanceFieldGlyphCache::QDistanceFieldGlyphCache()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdistancefieldglyphcache.html
    """
    #  Qt3DExtras::QDistanceFieldGlyphCache::QDistanceFieldGlyphCache()
    self._noteCreation(QDistanceFieldGlyphCache, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCacheC1Ev',
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

  @staticmethod
  def derefGlyph(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QDistanceFieldGlyphCache::derefGlyph(const
    QRawFont &font, quint32 glyph)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'DistanceFieldFont'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QDistanceFieldGlyphCache.derefGlyph' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::QDistanceFieldGlyphCache::derefGlyph(const QRawFont "
        "&font, quint32 glyph)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'DistanceFieldFont'.")

  @staticmethod
  def derefGlyphs(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QDistanceFieldGlyphCache::derefGlyphs(const
    QGlyphRun &run)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'DistanceFieldFont'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QDistanceFieldGlyphCache.derefGlyphs' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::QDistanceFieldGlyphCache::derefGlyphs(const QGlyphRun "
        "&run)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'DistanceFieldFont'.")

  @staticmethod
  def doubleGlyphResolution(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DExtras::QDistanceFieldGlyphCache::doubleGlyphResolution(const
    QRawFont &font)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'DistanceFieldFont'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QDistanceFieldGlyphCache.doubleGlyphResolution' has no "
        "cute function yet. Qt's 'bool "
        "Qt3DExtras::QDistanceFieldGlyphCache::doubleGlyphResolution(const "
        "QRawFont &font)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'DistanceFieldFont'.")

  @staticmethod
  def getOrCreateDistanceFieldFont(*__, **_) -> Never:
    """
    Qt's 'DistanceFieldFont
    *Qt3DExtras::QDistanceFieldGlyphCache::getOrCreateDistanceFieldFont(const
    QRawFont &font)': the compiler refuses its ritual as it would be written
    here: unknown type name 'DistanceFieldFont'; did you mean
    'Qt3DExtras::DistanceFieldFont'?.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QDistanceFieldGlyphCache.getOrCreateDistanceFieldFont' "
        "has no cute function yet. Qt's 'DistanceFieldFont "
        "*Qt3DExtras::QDistanceFieldGlyphCache::getOrCreateDistanceFieldFont"
        "(const QRawFont &font)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'DistanceFieldFont'; did "
        "you mean 'Qt3DExtras::DistanceFieldFont'?.")

  @staticmethod
  def refGlyph(*__, **_) -> Never:
    """
    Qt's 'Glyph Qt3DExtras::QDistanceFieldGlyphCache::refGlyph(const QRawFont
    &font, quint32 glyph)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'refAndGetGlyph'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QDistanceFieldGlyphCache.refGlyph' has no cute "
        "function yet. Qt's 'Glyph "
        "Qt3DExtras::QDistanceFieldGlyphCache::refGlyph(const QRawFont "
        "&font, quint32 glyph)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'refAndGetGlyph'.")

  @staticmethod
  def refGlyphs(*__, **_) -> Never:
    """
    Qt's 'QList<Glyph> Qt3DExtras::QDistanceFieldGlyphCache::refGlyphs(const
    QGlyphRun &run)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'refAndGetGlyph'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QDistanceFieldGlyphCache.refGlyphs' has no cute "
        "function yet. Qt's 'QList<Glyph> "
        "Qt3DExtras::QDistanceFieldGlyphCache::refGlyphs(const QGlyphRun "
        "&run)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'refAndGetGlyph'.")
