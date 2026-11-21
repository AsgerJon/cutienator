"""
QRandomGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrandom.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QRandomGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRandomGenerator: a plain Python object standing in
  front of one C++ QRandomGenerator.

  C++ hands a QRandomGenerator around as a copy, so every C++
  QRandomGenerator behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRandomGenerator that has a ritual and that Python
  can call so far, 11 names in all: 'generate', 'generate64',
  'generateDouble', 'bounded', 'seed', 'discard', 'min', 'max', 'system',
  'global_', 'securelySeeded'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRandomGenerator::~QRandomGenerator()': the destructor: Python
    removes its C++ QRandomGenerator by it, and has no other use for it.
  - Qt's 'int QRandomGenerator::bounded(int highest)': takes in Python what
    'quint32 QRandomGenerator::bounded(quint32 highest)' takes.
  - Qt's 'int QRandomGenerator::bounded(int lowest, int highest)': takes in
    Python what 'quint32 QRandomGenerator::bounded(quint32 lowest, quint32
    highest)' takes.
  - Qt's 'quint64 QRandomGenerator::bounded(quint64 highest)': takes in
    Python what 'quint32 QRandomGenerator::bounded(quint32 highest)' takes.
  - Qt's 'quint64 QRandomGenerator::bounded(quint64 lowest, quint64
    highest)': takes in Python what 'quint32
    QRandomGenerator::bounded(quint32 lowest, quint32 highest)' takes.
  - Qt's 'qint64 QRandomGenerator::bounded(qint64 highest)': takes in Python
    what 'quint32 QRandomGenerator::bounded(quint32 highest)' takes.
  - Qt's 'qint64 QRandomGenerator::bounded(qint64 lowest, qint64 highest)':
    takes in Python what 'quint32 QRandomGenerator::bounded(quint32 lowest,
    quint32 highest)' takes.
  - Qt's 'qint64 QRandomGenerator::bounded(int lowest, qint64 highest)':
    takes in Python what 'quint32 QRandomGenerator::bounded(quint32 lowest,
    quint32 highest)' takes.
  - Qt's 'qint64 QRandomGenerator::bounded(qint64 lowest, int highest)':
    takes in Python what 'quint32 QRandomGenerator::bounded(quint32 lowest,
    quint32 highest)' takes.
  - Qt's 'quint64 QRandomGenerator::bounded(unsigned int lowest, quint64
    highest)': takes in Python what 'quint32
    QRandomGenerator::bounded(quint32 lowest, quint32 highest)' takes.
  - Qt's 'quint64 QRandomGenerator::bounded(quint64 lowest, unsigned int
    highest)': takes in Python what 'quint32
    QRandomGenerator::bounded(quint32 lowest, quint32 highest)' takes.
  - Qt's 'void QRandomGenerator::generate(quint32 *begin, quint32 *end)':
    takes a number to change where it is.
  - Qt's 'result_type QRandomGenerator::operator()()': an operator, which is
    not reflected yet.

  What has no ritual
  ------------------

  11 of the 39 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 4 a template; 1 protected; 1 private.

  What to expect
  --------------

  - The C++ QRandomGenerator is created at the first use, not by
    'QRandomGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRandomGenerator back gives a copy the ritual made
    for Python, in a new cute QRandomGenerator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def min() -> int:
    """
    Calls Qt's 'result_type QRandomGenerator::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#min
    """
    #  result_type QRandomGenerator::min()
    return Rituals.call('ritual_ZN16QRandomGenerator3minEv')

  @staticmethod
  def max() -> int:
    """
    Calls Qt's 'result_type QRandomGenerator::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#max
    """
    #  result_type QRandomGenerator::max()
    return Rituals.call('ritual_ZN16QRandomGenerator3maxEv')

  @staticmethod
  def system() -> Optional[QRandomGenerator]:
    """
    Calls Qt's 'QRandomGenerator *QRandomGenerator::system()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#system

    Returns
    -------

    Optional[QRandomGenerator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomGenerator *QRandomGenerator::system()
    address = Rituals.call('ritual_ZN16QRandomGenerator6systemEv')
    return QRandomGenerator._cuteAt(address)

  @staticmethod
  def global_() -> Optional[QRandomGenerator]:
    """
    Calls Qt's 'QRandomGenerator *QRandomGenerator::global()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#global

    Returns
    -------

    Optional[QRandomGenerator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomGenerator *QRandomGenerator::global()
    address = Rituals.call('ritual_ZN16QRandomGenerator6globalEv')
    return QRandomGenerator._cuteAt(address)

  @staticmethod
  def securelySeeded() -> QRandomGenerator:
    """
    Calls Qt's 'QRandomGenerator QRandomGenerator::securelySeeded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator.html#securelySeeded

    Returns
    -------

    QRandomGenerator
      A new cute QRandomGenerator around the copy Qt gave back. Python owns
      it.
    """
    #  QRandomGenerator QRandomGenerator::securelySeeded()
    address = Rituals.call('ritual_ZN16QRandomGenerator14securelySeededEv')
    return QRandomGenerator._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRandomGenerator'

  #  Qt's '~QRandomGenerator()'. Naming it makes this a value class: Python
  #  owns every C++ QRandomGenerator behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QRandomGeneratorD1Ev'

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
  @overload(int)
  def __init__(self, seedValue: int = 1) -> None:
    """
    Notes what was given, for Qt's
    'QRandomGenerator::QRandomGenerator(quint32 seedValue)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator.html#QRandomGenerator

    Parameters
    ----------

    seedValue : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QRandomGenerator::QRandomGenerator(quint32 seedValue)
    self._noteCreation(QRandomGenerator, lambda: Rituals.call(
        'ritual_ZN16QRandomGeneratorC1Ej', seedValue,
    ))

  @overload(THIS)
  def __init__(self, other: QRandomGenerator) -> None:
    """
    Notes what was given, for Qt's 'QRandomGenerator::QRandomGenerator(const
    QRandomGenerator &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator.html#QRandomGenerator

    Parameters
    ----------

    other : QRandomGenerator
      Passed on as a value: Qt reads the C++ QRandomGenerator, which stays
      Python's own.
    """
    #  QRandomGenerator::QRandomGenerator(const QRandomGenerator &other)
    self._noteCreation(QRandomGenerator, lambda: Rituals.call(
        'ritual_ZN16QRandomGeneratorC1ERKS_', self._valueOf(other),
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

  def generate(self) -> int:
    """
    Calls Qt's 'quint32 QRandomGenerator::generate()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#generate
    """
    #  quint32 QRandomGenerator::generate()
    return self.uglySide.call('ritual_ZN16QRandomGenerator8generateEv')

  def generate64(self) -> int:
    """
    Calls Qt's 'quint64 QRandomGenerator::generate64()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#generate64
    """
    #  quint64 QRandomGenerator::generate64()
    return self.uglySide.call('ritual_ZN16QRandomGenerator10generate64Ev')

  def generateDouble(self) -> float:
    """
    Calls Qt's 'double QRandomGenerator::generateDouble()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator.html#generateDouble
    """
    #  double QRandomGenerator::generateDouble()
    return self.uglySide.call(
        'ritual_ZN16QRandomGenerator14generateDoubleEv',
    )

  @overload(float)
  def bounded(self, highest: float) -> float:
    """
    Calls Qt's 'double QRandomGenerator::bounded(double highest)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#bounded

    Parameters
    ----------

    highest : float
      Passed on as it is.
    """
    #  double QRandomGenerator::bounded(double highest)
    return self.uglySide.call(
        'ritual_ZN16QRandomGenerator7boundedEd', highest,
    )

  @overload(int)
  def bounded(self, highest: int) -> int:
    """
    Calls Qt's 'quint32 QRandomGenerator::bounded(quint32 highest)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#bounded

    Parameters
    ----------

    highest : int
      Passed on as it is.
    """
    #  quint32 QRandomGenerator::bounded(quint32 highest)
    return self.uglySide.call(
        'ritual_ZN16QRandomGenerator7boundedEj', highest,
    )

  @overload(int, int)
  def bounded(self, lowest: int, highest: int) -> int:
    """
    Calls Qt's 'quint32 QRandomGenerator::bounded(quint32 lowest, quint32
    highest)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#bounded

    Parameters
    ----------

    lowest : int
      Passed on as it is.

    highest : int
      Passed on as it is.
    """
    #  quint32 QRandomGenerator::bounded(quint32 lowest, quint32 highest)
    return self.uglySide.call(
        'ritual_ZN16QRandomGenerator7boundedEjj', lowest, highest,
    )

  @overload()
  @overload(int)
  def seed(self, s: int = 1) -> None:
    """
    Calls Qt's 'void QRandomGenerator::seed(quint32 s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#seed

    Parameters
    ----------

    s : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QRandomGenerator::seed(quint32 s)
    self.uglySide.call('ritual_ZN16QRandomGenerator4seedEj', s)

  @overload(int)
  def discard(self, z: int) -> None:
    """
    Calls Qt's 'void QRandomGenerator::discard(unsigned long long z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator.html#discard

    Parameters
    ----------

    z : int
      Passed on as it is.
    """
    #  void QRandomGenerator::discard(unsigned long long z)
    self.uglySide.call('ritual_ZN16QRandomGenerator7discardEy', z)
