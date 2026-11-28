"""
QLottieTrimPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieTrimPath to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonObject
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QPainterPath = WAIT['QPainterPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieTrimPath(QLottieShape):
  """
  The cute side of Qt's QLottieTrimPath: a plain Python object standing in
  front of one C++ QLottieTrimPath.

  It is built on the cute 'QLottieShape', as Qt's QLottieTrimPath is built on
  Qt's QLottieShape, and has everything that class has.

  C++ hands a QLottieTrimPath around as a copy, so every C++ QLottieTrimPath
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieTrimPath that has a ritual and that Python
  can call so far, 10 names in all: 'clone', 'parse', 'updateProperties',
  'acceptsTrim', 'applyTrim', 'start', 'end', 'offset', 'isParallel', 'trim'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieTrimPath::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieProperty<qreal> QLottieTrimPath::startProperty() const':
    gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieTrimPath::endProperty() const': gives
    a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieTrimPath::offsetProperty() const':
    gives a type Python has no way to take yet.
  - Qt's 'QLottieTrimPath::~QLottieTrimPath()': the destructor: Python
    removes its C++ QLottieTrimPath by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 18 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QLottieTrimPath is created at the first use, not by
    'QLottieTrimPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieTrimPath back gives a copy the ritual made for
    Python, in a new cute QLottieTrimPath.
  - Each name of Qt's QLottieTrimPath that has no cute function yet,
    'endProperty', 'inherit', 'offsetProperty', 'startProperty', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieTrimPath'

  #  A C++ QLottieTrimPath Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieTrimPath'

  #  Qt's '~QLottieTrimPath()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieTrimPath behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QLottieTrimPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieTrimPath::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieTrimPath::clone() const
    ritual = 'ritual_ZNK15QLottieTrimPath5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottieTrimPath5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieTrimPath::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#acceptsTrim
    """
    #  bool QLottieTrimPath::acceptsTrim() const
    ritual = 'ritual_ZNK15QLottieTrimPath11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QLottieTrimPath11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def start(self) -> float:
    """
    Calls Qt's 'qreal QLottieTrimPath::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#start
    """
    #  qreal QLottieTrimPath::start() const
    return self.uglySide.call('ritual_ZNK15QLottieTrimPath5startEv')

  def end(self) -> float:
    """
    Calls Qt's 'qreal QLottieTrimPath::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#end
    """
    #  qreal QLottieTrimPath::end() const
    return self.uglySide.call('ritual_ZNK15QLottieTrimPath3endEv')

  def offset(self) -> float:
    """
    Calls Qt's 'qreal QLottieTrimPath::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#offset
    """
    #  qreal QLottieTrimPath::offset() const
    return self.uglySide.call('ritual_ZNK15QLottieTrimPath6offsetEv')

  def isParallel(self) -> bool:
    """
    Calls Qt's 'bool QLottieTrimPath::isParallel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#isParallel
    """
    #  bool QLottieTrimPath::isParallel() const
    return self.uglySide.call('ritual_ZNK15QLottieTrimPath10isParallelEv')

  @overload(QPainterPath)
  def trim(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QLottieTrimPath::trim(const QPainterPath &path)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#trim

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QLottieTrimPath::trim(const QPainterPath &path) const
    address = self.uglySide.call(
        'ritual_ZNK15QLottieTrimPath4trimERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, other: QLottieTrimPath) -> None:
    """
    Notes what was given, for Qt's 'QLottieTrimPath::QLottieTrimPath(const
    QLottieTrimPath &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottietrimpath.html#QLottieTrimPath

    Parameters
    ----------

    other : QLottieTrimPath
      Passed on as a value: Qt reads the C++ QLottieTrimPath, which stays
      Python's own.
    """
    #  QLottieTrimPath::QLottieTrimPath(const QLottieTrimPath &other)
    self._noteCreation(QLottieTrimPath, lambda: Rituals.call(
        'ritual_ZN15QLottieTrimPathC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieTrimPath::QLottieTrimPath(QLottieBase *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottietrimpath.html#QLottieTrimPath

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieTrimPath::QLottieTrimPath(QLottieBase *parent)
    self._noteCreation(QLottieTrimPath, lambda: Rituals.call(
        'ritual_ZN15QLottieTrimPathC1EP11QLottieBase',
        self._addressOf(parent),
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieTrimPath::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieTrimPath::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN15QLottieTrimPath5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieTrimPath5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieTrimPath::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottietrimpath.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieTrimPath::updateProperties(int frame)
    ritual = 'ritual_ZN15QLottieTrimPath16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieTrimPath16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(THIS)
  def applyTrim(self, trimmer: QLottieTrimPath) -> None:
    """
    Calls Qt's 'void QLottieTrimPath::applyTrim(const QLottieTrimPath
    &trimmer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietrimpath.html#applyTrim

    Parameters
    ----------

    trimmer : QLottieTrimPath
      Passed on as a value: Qt reads the C++ QLottieTrimPath, which stays
      Python's own.
    """
    #  void QLottieTrimPath::applyTrim(const QLottieTrimPath &trimmer)
    ritual = 'ritual_ZN15QLottieTrimPath9applyTrimERKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QLottieTrimPath9applyTrimERKS_'
    self.uglySide.call(ritual, self._valueOf(trimmer))

  @staticmethod
  def endProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieTrimPath::endProperty() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieTrimPath.endProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieTrimPath::endProperty() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def inherit(*__, **_) -> Never:
    """
    Qt's 'void QLottieTrimPath::inherit(const QLottieTrimPath &other)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QLottieTrimPath.inherit' has no cute function yet. Qt's 'void "
        "QLottieTrimPath::inherit(const QLottieTrimPath &other)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def offsetProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieTrimPath::offsetProperty() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieTrimPath.offsetProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieTrimPath::offsetProperty() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def startProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieTrimPath::startProperty() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieTrimPath.startProperty' has no cute function yet. Qt's "
        "'QLottieProperty<qreal> QLottieTrimPath::startProperty() const': "
        "gives a type Python has no way to take yet.")
