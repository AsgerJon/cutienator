"""
QColorSpacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolorspace_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QColorSpacePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QColorSpace

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QColorTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QColorSpacePrivate(QSharedData):
  """
  The cute side of Qt's QColorSpacePrivate: a plain Python object standing in
  front of one C++ QColorSpacePrivate.

  It is built on the cute 'QSharedData', as Qt's QColorSpacePrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QColorSpacePrivate around as a copy, so every C++
  QColorSpacePrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorSpacePrivate that has a ritual and that Python
  can call so far, 8 names in all: 'get', 'isValid', 'initialize',
  'setTransferFunction', 'identifyColorSpace', 'transformationToXYZ',
  'isThreeComponentMatrix', 'clearElementListProcessingForEdit'. It can be
  made from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries
    primaries, const QList<uint16_t> &transferFunctionTable)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint, const
    QList<uint16_t> &transferFunctionTable)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QColorSpacePrivate *QColorSpacePrivate::get(QColorSpace
    &colorSpace)': takes a type Python has no way to hand over yet.
  - Qt's 'void QColorSpacePrivate::setTransferFunctionTable(const
    QList<uint16_t> &transferFunctionTable)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QColorSpacePrivate::setTransferFunctionTables(const
    QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QColorSpacePrivate::~QColorSpacePrivate()': the destructor: Python
    removes its C++ QColorSpacePrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 25 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QColorSpacePrivate.

  What to expect
  --------------

  - The C++ QColorSpacePrivate is created at the first use, not by
    'QColorSpacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorSpacePrivate back gives a copy the ritual made
    for Python, in a new cute QColorSpacePrivate.
  - Each name of Qt's QColorSpacePrivate that has no cute function yet,
    'equals', 'setToXyzMatrix', 'setTransferFunctionTable',
    'setTransferFunctionTables', 'transformationToColorSpace', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QColorSpacePrivate, each a class in here as
  #  in C++.

  class LUT(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QColorSpacePrivate::LUT: a plain Python object
    standing in front of one C++ QColorSpacePrivate::LUT.

    C++ hands a QColorSpacePrivate::LUT around as a copy, so every C++
    QColorSpacePrivate::LUT behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QColorSpacePrivate::LUT yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QColorSpacePrivate::LUT::~LUT()': the destructor: Python removes
      its C++ QColorSpacePrivate::LUT by it, and has no other use for it.
    - Qt's 'std::shared_ptr<QColorTrcLut>
      &QColorSpacePrivate::LUT::operator[](int i)': gives a type Python has
      no way to take yet.
    - Qt's 'const std::shared_ptr<QColorTrcLut>
      &QColorSpacePrivate::LUT::operator[](int i) const': gives a type Python
      has no way to take yet.

    What to expect
    --------------

    - The C++ QColorSpacePrivate::LUT is created at the first use, not by
      'QColorSpacePrivate::LUT(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QColorSpacePrivate::LUT back gives a copy the
      ritual made for Python, in a new cute QColorSpacePrivate::LUT.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QColorSpacePrivate::LUT'

    #  Qt's '~QColorSpacePrivate::LUT()'. Naming it makes this a value class:
    #  Python owns every C++ QColorSpacePrivate::LUT behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QColorSpacePrivate3LUTD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QColorSpacePrivate::LUT::LUT()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcolorspaceprivate-lut.html#LUT
      """
      #  QColorSpacePrivate::LUT::LUT()
      self._noteCreation(QColorSpacePrivate.LUT, lambda: Rituals.call(
          'ritual_ZN18QColorSpacePrivate3LUTC1Ev',
      ))

    @overload(THIS)
    def __init__(self, other: QColorSpacePrivate.LUT) -> None:
      """
      Notes what was given, for Qt's 'QColorSpacePrivate::LUT::LUT(const LUT
      &other)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcolorspaceprivate-lut.html#LUT

      Parameters
      ----------

      other : QColorSpacePrivate.LUT
        Passed on as a value: Qt reads the C++ QColorSpacePrivate::LUT, which
        stays Python's own.
      """
      #  QColorSpacePrivate::LUT::LUT(const LUT &other)
      self._noteCreation(QColorSpacePrivate.LUT, lambda: Rituals.call(
          'ritual_ZN18QColorSpacePrivate3LUTC1ERKS0_', self._valueOf(other),
      ))

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

  class TransferElement(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QColorSpacePrivate::TransferElement: a plain Python
    object standing in front of one C++ QColorSpacePrivate::TransferElement.

    C++ hands a QColorSpacePrivate::TransferElement around as a copy, so
    every C++ QColorSpacePrivate::TransferElement behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QColorSpacePrivate::TransferElement yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QColorSpacePrivate::TransferElement::~TransferElement()': the
      destructor: Python removes its C++ QColorSpacePrivate::TransferElement
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QColorSpacePrivate::TransferElement is created at the first
      use, not by 'QColorSpacePrivate::TransferElement(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QColorSpacePrivate::TransferElement back gives a
      copy the ritual made for Python, in a new cute
      QColorSpacePrivate::TransferElement.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QColorSpacePrivate::TransferElement'

    #  Qt's '~QColorSpacePrivate::TransferElement()'. Naming it makes this a
    #  value class: Python owns every C++ QColorSpacePrivate::TransferElement
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QColorSpacePrivate15TransferElementD1Ev'

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
  @overload(QColorSpace)
  def get(colorSpace: QColorSpace) -> Optional[QColorSpacePrivate]:
    """
    Calls Qt's 'const QColorSpacePrivate *QColorSpacePrivate::get(const
    QColorSpace &colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspaceprivate.html#get

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.

    Returns
    -------

    Optional[QColorSpacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QColorSpacePrivate *QColorSpacePrivate::get(const QColorSpace
    #      &colorSpace)
    address = Rituals.call(
        'ritual_ZN18QColorSpacePrivate3getERK11QColorSpace',
        CuteMixin._valueOf(colorSpace),
    )
    return QColorSpacePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorSpacePrivate'

  #  Qt's '~QColorSpacePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QColorSpacePrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QColorSpacePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColorSpacePrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspaceprivate.html#isValid
    """
    #  bool QColorSpacePrivate::isValid() const
    return self.uglySide.call('ritual_ZNK18QColorSpacePrivate7isValidEv')

  def transformationToXYZ(self) -> QColorTransform:
    """
    Calls Qt's 'QColorTransform QColorSpacePrivate::transformationToXYZ()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#transformationToXYZ

    Returns
    -------

    QColorTransform
      A new cute QColorTransform around the copy Qt gave back. Python owns
      it.
    """
    #  QColorTransform QColorSpacePrivate::transformationToXYZ() const
    address = self.uglySide.call(
        'ritual_ZNK18QColorSpacePrivate19transformationToXYZEv',
    )
    from . import QColorTransform
    return QColorTransform._cuteOwning(address)

  def isThreeComponentMatrix(self) -> bool:
    """
    Calls Qt's 'bool QColorSpacePrivate::isThreeComponentMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#isThreeComponentMatrix
    """
    #  bool QColorSpacePrivate::isThreeComponentMatrix() const
    return self.uglySide.call(
        'ritual_ZNK18QColorSpacePrivate22isThreeComponentMatrixEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setTransferFunction(self) -> None:
    """
    Calls Qt's 'void QColorSpacePrivate::setTransferFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#setTransferFunction
    """
    #  void QColorSpacePrivate::setTransferFunction()
    self.uglySide.call(
        'ritual_ZN18QColorSpacePrivate19setTransferFunctionEv',
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
    'QColorSpacePrivate::QColorSpacePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#QColorSpacePrivate
    """
    #  QColorSpacePrivate::QColorSpacePrivate()
    self._noteCreation(QColorSpacePrivate, lambda: Rituals.call(
        'ritual_ZN18QColorSpacePrivateC1Ev',
    ))

  @overload(QColorSpace.NamedColorSpace)
  def __init__(self, namedColorSpace: QColorSpace.NamedColorSpace) -> None:
    """
    Notes what was given, for Qt's
    'QColorSpacePrivate::QColorSpacePrivate(QColorSpace::NamedColorSpace
    namedColorSpace)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#QColorSpacePrivate

    Parameters
    ----------

    namedColorSpace : QColorSpace.NamedColorSpace
      Passed on as its number.
    """
    #  QColorSpacePrivate::QColorSpacePrivate(QColorSpace::NamedColorSpace
    #      namedColorSpace)
    self._noteCreation(QColorSpacePrivate, lambda: Rituals.call(
        'ritual_ZN18QColorSpacePrivateC1EN11QColorSpace15NamedColorSpaceE',
        namedColorSpace.value,
    ))

  @overload(QColorSpace.Primaries, QColorSpace.TransferFunction, float)
  def __init__(
      self,
      primaries: QColorSpace.Primaries,
      transferFunction: QColorSpace.TransferFunction,
      gamma: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries primaries,
    QColorSpace::TransferFunction transferFunction, float gamma)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#QColorSpacePrivate

    Parameters
    ----------

    primaries : QColorSpace.Primaries
      Passed on as its number.

    transferFunction : QColorSpace.TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is.
    """
    #  QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries
    #      primaries, QColorSpace::TransferFunction transferFunction, float
    #      gamma)
    self._noteCreation(QColorSpacePrivate, lambda: Rituals.call(
        'ritual_ZN18QColorSpacePrivateC1EN11QColorSpace9PrimariesENS0_16Tra'
        'nsferFunctionEf',
        primaries.value, transferFunction.value, gamma,
    ))

  @overload(QColorSpace.PrimaryPoints, QColorSpace.TransferFunction, float)
  def __init__(
      self,
      primaries: QColorSpace.PrimaryPoints,
      transferFunction: QColorSpace.TransferFunction,
      gamma: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QColorSpacePrivate::QColorSpacePrivate(const QColorSpace::PrimaryPoints
    &primaries, QColorSpace::TransferFunction transferFunction, float
    gamma)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#QColorSpacePrivate

    Parameters
    ----------

    primaries : QColorSpace.PrimaryPoints
      Passed on as a value: Qt reads the C++ QColorSpace::PrimaryPoints,
      which stays Python's own.

    transferFunction : QColorSpace.TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is.
    """
    #  QColorSpacePrivate::QColorSpacePrivate(const
    #      QColorSpace::PrimaryPoints &primaries,
    #      QColorSpace::TransferFunction transferFunction, float gamma)
    self._noteCreation(QColorSpacePrivate, lambda: Rituals.call(
        'ritual_ZN18QColorSpacePrivateC1ERKN11QColorSpace13PrimaryPointsENS'
        '0_16TransferFunctionEf',
        self._valueOf(primaries), transferFunction.value, gamma,
    ))

  @overload(QPointF, QColorSpace.TransferFunction, float)
  def __init__(
      self,
      whitePoint: QPointF,
      transferFunction: QColorSpace.TransferFunction,
      gamma: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint,
    QColorSpace::TransferFunction transferFunction, float gamma)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#QColorSpacePrivate

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    transferFunction : QColorSpace.TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is.
    """
    #  QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint,
    #      QColorSpace::TransferFunction transferFunction, float gamma)
    self._noteCreation(QColorSpacePrivate, lambda: Rituals.call(
        'ritual_ZN18QColorSpacePrivateC1E7QPointFN11QColorSpace16TransferFu'
        'nctionEf',
        self._valueOf(whitePoint, 'QPointF'), transferFunction.value, gamma,
    ))

  @overload(THIS)
  def __init__(self, other: QColorSpacePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QColorSpacePrivate::QColorSpacePrivate(const QColorSpacePrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#QColorSpacePrivate

    Parameters
    ----------

    other : QColorSpacePrivate
      Passed on as a value: Qt reads the C++ QColorSpacePrivate, which stays
      Python's own.
    """
    #  QColorSpacePrivate::QColorSpacePrivate(const QColorSpacePrivate
    #      &other)
    self._noteCreation(QColorSpacePrivate, lambda: Rituals.call(
        'ritual_ZN18QColorSpacePrivateC1ERKS_', self._valueOf(other),
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QColorSpacePrivate::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspaceprivate.html#initialize
    """
    #  void QColorSpacePrivate::initialize()
    self.uglySide.call('ritual_ZN18QColorSpacePrivate10initializeEv')

  def identifyColorSpace(self) -> None:
    """
    Calls Qt's 'void QColorSpacePrivate::identifyColorSpace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html#identifyColorSpace
    """
    #  void QColorSpacePrivate::identifyColorSpace()
    self.uglySide.call('ritual_ZN18QColorSpacePrivate18identifyColorSpaceEv')

  def clearElementListProcessingForEdit(self) -> None:
    """
    Calls Qt's 'void
    QColorSpacePrivate::clearElementListProcessingForEdit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspaceprivate.html
    """
    #  void QColorSpacePrivate::clearElementListProcessingForEdit()
    self.uglySide.call(
        'ritual_ZN18QColorSpacePrivate33clearElementListProcessingForEditEv',
    )

  @staticmethod
  def equals(*__, **_) -> Never:
    """
    Qt's 'bool QColorSpacePrivate::equals(const QColorSpacePrivate *other)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'compareElements'.
    """
    raise NotImplementedError(
        "'QColorSpacePrivate.equals' has no cute function yet. Qt's 'bool "
        "QColorSpacePrivate::equals(const QColorSpacePrivate *other) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'compareElements'.")

  @staticmethod
  def setToXyzMatrix(*__, **_) -> Never:
    """
    Qt's 'void QColorSpacePrivate::setToXyzMatrix()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qColorSpacePrimaryPointsToXyzMatrix';
    did you mean 'qColorSpacePrimaryPointsAreValid'?.
    """
    raise NotImplementedError(
        "'QColorSpacePrivate.setToXyzMatrix' has no cute function yet. Qt's "
        "'void QColorSpacePrivate::setToXyzMatrix()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'qColorSpacePrimaryPointsToXyzMatrix'; did you mean "
        "'qColorSpacePrimaryPointsAreValid'?.")

  @staticmethod
  def setTransferFunctionTable(*__, **_) -> Never:
    """
    Qt's 'void QColorSpacePrivate::setTransferFunctionTable(const
    QList<uint16_t> &transferFunctionTable)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QColorSpacePrivate.setTransferFunctionTable' has no cute function "
        "yet. Qt's 'void QColorSpacePrivate::setTransferFunctionTable(const "
        "QList<uint16_t> &transferFunctionTable)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def setTransferFunctionTables(*__, **_) -> Never:
    """
    Qt's 'void QColorSpacePrivate::setTransferFunctionTables(const
    QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QColorSpacePrivate.setTransferFunctionTables' has no cute "
        "function yet. Qt's 'void "
        "QColorSpacePrivate::setTransferFunctionTables(const "
        "QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t> "
        "&greenTransferFunctionTable, const QList<uint16_t> "
        "&blueTransferFunctionTable)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def transformationToColorSpace(*__, **_) -> Never:
    """
    Qt's 'QColorTransform
    QColorSpacePrivate::transformationToColorSpace(const QColorSpacePrivate
    *out) const': leans on 'QColorSpacePrivate::equals(QColorSpacePrivate
    const*) const', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColorSpacePrivate.transformationToColorSpace' has no cute "
        "function yet. Qt's 'QColorTransform "
        "QColorSpacePrivate::transformationToColorSpace(const "
        "QColorSpacePrivate *out) const': leans on "
        "'QColorSpacePrivate::equals(QColorSpacePrivate const*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
