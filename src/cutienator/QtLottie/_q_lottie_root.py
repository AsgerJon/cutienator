"""
QLottieRoot binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieroot_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieRoot to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottiePrecomposition
  from ..QtCore import QByteArray, QSize, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']


class QLottieRoot(QLottieBase):
  """
  The cute side of Qt's QLottieRoot: a plain Python object standing in front
  of one C++ QLottieRoot.

  It is built on the cute 'QLottieBase', as Qt's QLottieRoot is built on Qt's
  QLottieBase, and has everything that class has.

  C++ hands a QLottieRoot around as a copy, so every C++ QLottieRoot behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieRoot that has a ritual and that Python can
  call so far, 9 names in all: 'clone', 'updateProperties', 'layerSize',
  'parseSource', 'setStructureDumping', 'startFrame', 'endFrame',
  'frameRate', 'precompositions'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieRoot::~QLottieRoot()': the destructor: Python removes its
    C++ QLottieRoot by it, and has no other use for it.
  - Qt's 'bool QLottieRoot::resolvePrecompLayers(QLottieBase *element,
    QStack<QString> *visitedIds)': names 'QStack<QString>', which has no cute
    class yet.

  What to expect
  --------------

  - The C++ QLottieRoot is created at the first use, not by
    'QLottieRoot(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieRoot back gives a copy the ritual made for
    Python, in a new cute QLottieRoot.
  - Each name of Qt's QLottieRoot that has no cute function yet,
    'resolvePrecompLayers', holds a function that raises
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
  __qt_class__ = 'QLottieRoot'

  #  A C++ QLottieRoot Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRoot'

  #  Qt's '~QLottieRoot()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieRoot behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QLottieRootD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieRoot::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieRoot::clone() const
    ritual = 'ritual_ZNK11QLottieRoot5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieRoot5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def layerSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLottieRoot::layerSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#layerSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLottieRoot::layerSize() const
    ritual = 'ritual_ZNK11QLottieRoot9layerSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieRoot9layerSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def startFrame(self) -> int:
    """
    Calls Qt's 'int QLottieRoot::startFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#startFrame
    """
    #  int QLottieRoot::startFrame() const
    return self.uglySide.call('ritual_ZNK11QLottieRoot10startFrameEv')

  def endFrame(self) -> int:
    """
    Calls Qt's 'int QLottieRoot::endFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#endFrame
    """
    #  int QLottieRoot::endFrame() const
    return self.uglySide.call('ritual_ZNK11QLottieRoot8endFrameEv')

  def frameRate(self) -> int:
    """
    Calls Qt's 'int QLottieRoot::frameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#frameRate
    """
    #  int QLottieRoot::frameRate() const
    return self.uglySide.call('ritual_ZNK11QLottieRoot9frameRateEv')

  def precompositions(self) -> QMap[str, QLottiePrecomposition]:
    """
    Calls Qt's 'QMap<QString, QLottiePrecomposition *>
    QLottieRoot::precompositions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#precompositions

    Returns
    -------

    QMap[str, QLottiePrecomposition]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<QString, QLottiePrecomposition *> QLottieRoot::precompositions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QLottieRoot15precompositionsEv',
    )
    from . import QLottiePrecomposition
    return QMap[str, QLottiePrecomposition]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setStructureDumping(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QLottieRoot::setStructureDumping(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieroot.html#setStructureDumping

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QLottieRoot::setStructureDumping(bool enabled)
    self.uglySide.call(
        'ritual_ZN11QLottieRoot19setStructureDumpingEb', enabled,
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
    Notes what was given, for Qt's 'QLottieRoot::QLottieRoot()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#QLottieRoot
    """
    #  QLottieRoot::QLottieRoot()
    self._noteCreation(QLottieRoot, lambda: Rituals.call(
        'ritual_ZN11QLottieRootC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieRoot) -> None:
    """
    Notes what was given, for Qt's 'QLottieRoot::QLottieRoot(const
    QLottieRoot &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#QLottieRoot

    Parameters
    ----------

    other : QLottieRoot
      Passed on as a value: Qt reads the C++ QLottieRoot, which stays
      Python's own.
    """
    #  QLottieRoot::QLottieRoot(const QLottieRoot &other)
    self._noteCreation(QLottieRoot, lambda: Rituals.call(
        'ritual_ZN11QLottieRootC1ERKS_', self._valueOf(other),
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
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieRoot::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieRoot::updateProperties(int frame)
    ritual = 'ritual_ZN11QLottieRoot16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieRoot16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QByteArray, QUrl)
  def parseSource(self, jsonSource: QByteArray, fileSource: QUrl) -> int:
    """
    Calls Qt's 'int QLottieRoot::parseSource(const QByteArray &jsonSource,
    const QUrl &fileSource)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieroot.html#parseSource

    Parameters
    ----------

    jsonSource : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fileSource : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  int QLottieRoot::parseSource(const QByteArray &jsonSource, const QUrl
    #      &fileSource)
    return self.uglySide.call(
        'ritual_ZN11QLottieRoot11parseSourceERK10QByteArrayRK4QUrl',
        self._valueOf(jsonSource), self._valueOf(fileSource),
    )

  @staticmethod
  def resolvePrecompLayers(*__, **_) -> Never:
    """
    Qt's 'bool QLottieRoot::resolvePrecompLayers(QLottieBase *element,
    QStack<QString> *visitedIds)': names 'QStack<QString>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QLottieRoot.resolvePrecompLayers' has no cute function yet. Qt's "
        "'bool QLottieRoot::resolvePrecompLayers(QLottieBase *element, "
        "QStack<QString> *visitedIds)': names 'QStack<QString>', which has "
        "no cute class yet.")
