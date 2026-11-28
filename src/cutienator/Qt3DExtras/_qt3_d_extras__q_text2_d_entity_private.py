"""
Qt3DExtras::QText2DEntityPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qtext2dentity_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DExtras::QText2DEntityPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QText2DEntityPrivate(Qt3DCore.QEntityPrivate):
  """
  The cute side of Qt's Qt3DExtras::QText2DEntityPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QText2DEntityPrivate.

  It is built on the cute 'Qt3DCore::QEntityPrivate', as Qt's
  Qt3DExtras::QText2DEntityPrivate is built on Qt's Qt3DCore::QEntityPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QText2DEntityPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'q_func', 'setScene',
  'computeActualScale'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DExtras::QText2DEntityPrivate::~QText2DEntityPrivate()': the
    destructor: Python never removes a C++ Qt3DExtras::QText2DEntityPrivate.
  - Qt's 'const QText2DEntity *Qt3DExtras::QText2DEntityPrivate::q_func()
    const': takes in Python what 'QText2DEntity
    *Qt3DExtras::QText2DEntityPrivate::q_func()' takes.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 3 leans on 'Qt3DExtras; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file.

  What to expect
  --------------

  - The C++ Qt3DExtras::QText2DEntityPrivate is created at the first use, not
    by 'Qt3DExtras::QText2DEntityPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QText2DEntityPrivate.
  - Each name of Qt's Qt3DExtras::QText2DEntityPrivate that has no cute
    function yet, '__init__', 'clearCurrentGlyphRuns', 'setCurrentGlyphRuns',
    'updateGlyphs', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside Qt3DExtras::QText2DEntityPrivate, each a
  #  class in here as in C++.

  class CacheEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DExtras::QText2DEntityPrivate::CacheEntry: a
    plain Python object standing in front of one C++
    Qt3DExtras::QText2DEntityPrivate::CacheEntry.

    C++ hands a Qt3DExtras::QText2DEntityPrivate::CacheEntry around as a
    copy, so every C++ Qt3DExtras::QText2DEntityPrivate::CacheEntry behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DExtras::QText2DEntityPrivate::CacheEntry yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DExtras::QText2DEntityPrivate::CacheEntry::~CacheEntry()': the
      destructor: Python removes its C++
      Qt3DExtras::QText2DEntityPrivate::CacheEntry by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DExtras::QText2DEntityPrivate::CacheEntry is created at the
      first use, not by 'Qt3DExtras::QText2DEntityPrivate::CacheEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DExtras::QText2DEntityPrivate::CacheEntry back
      gives a copy the ritual made for Python, in a new cute
      Qt3DExtras::QText2DEntityPrivate::CacheEntry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DExtras::QText2DEntityPrivate::CacheEntry'

    #  Qt's '~Qt3DExtras::QText2DEntityPrivate::CacheEntry()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DExtras::QText2DEntityPrivate::CacheEntry behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DExtras20QText2DEntityPrivate10CacheEntryD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QText2DEntityPrivate'

  #  A C++ Qt3DExtras::QText2DEntityPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QText2DEntityPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def computeActualScale(self) -> float:
    """
    Calls Qt's 'qreal Qt3DExtras::QText2DEntityPrivate::computeActualScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentityprivate.html
    """
    #  qreal Qt3DExtras::QText2DEntityPrivate::computeActualScale() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras20QText2DEntityPrivate18computeActualScaleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QScene'])
  @overload(NoneType)
  def setScene(self, scene: Optional[Qt3DCore.QScene]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QText2DEntityPrivate::setScene(Qt3DCore::QScene *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentityprivate.html#setScene

    Parameters
    ----------

    scene : Optional[Qt3DCore.QScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QText2DEntityPrivate::setScene(Qt3DCore::QScene
    #      *scene)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras20QText2DEntityPrivate8setSceneEPN8Qt3DCore6Q'
        'SceneE',
        self._addressOf(scene),
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
    Qt's 'Qt3DExtras::QText2DEntityPrivate::QText2DEntityPrivate()': leans on
    'Qt3DExtras::QText2DEntityPrivate::m_glyphCacheInstances', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QText2DEntityPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DExtras::QText2DEntityPrivate::QText2DEntityPrivate()': leans "
        "on 'Qt3DExtras::QText2DEntityPrivate::m_glyphCacheInstances', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[Qt3DExtras.QText2DEntity]:
    """
    Calls Qt's 'QText2DEntity *Qt3DExtras::QText2DEntityPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentityprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QText2DEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QText2DEntity *Qt3DExtras::QText2DEntityPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras20QText2DEntityPrivate6q_funcEv',
    )
    return Qt3DExtras.QText2DEntity._cuteAt(address)

  @staticmethod
  def clearCurrentGlyphRuns(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QText2DEntityPrivate::clearCurrentGlyphRuns()':
    leans on 'Qt3DExtras::QDistanceFieldGlyphCache::derefGlyphs(QGlyphRun
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QText2DEntityPrivate.clearCurrentGlyphRuns' has no "
        "cute function yet. Qt's 'void "
        "Qt3DExtras::QText2DEntityPrivate::clearCurrentGlyphRuns()': leans "
        "on 'Qt3DExtras::QDistanceFieldGlyphCache::derefGlyphs(QGlyphRun "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setCurrentGlyphRuns(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QText2DEntityPrivate::setCurrentGlyphRuns(const
    QList<QGlyphRun> &runs)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'RenderData'; did you mean 'renderData'?.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QText2DEntityPrivate.setCurrentGlyphRuns' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::QText2DEntityPrivate::setCurrentGlyphRuns(const "
        "QList<QGlyphRun> &runs)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'RenderData'; did you mean 'renderData'?.")

  @staticmethod
  def updateGlyphs(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QText2DEntityPrivate::updateGlyphs()': leans on
    'Qt3DExtras::QDistanceFieldGlyphCache::derefGlyphs(QGlyphRun const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QText2DEntityPrivate.updateGlyphs' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::QText2DEntityPrivate::updateGlyphs()': leans on "
        "'Qt3DExtras::QDistanceFieldGlyphCache::derefGlyphs(QGlyphRun "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
