"""
QColorSpace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QDebug, QPointF
  from . import QColorTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QPointF = WAIT['QPointF']


class QColorSpace(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorSpace: a plain Python object standing in front
  of one C++ QColorSpace.

  C++ hands a QColorSpace around as a copy, so every C++ QColorSpace behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorSpace that has a ritual and that Python can
  call so far, 24 names in all: 'primaries', 'transferFunction', 'gamma',
  'description', 'setDescription', 'setTransferFunction',
  'withTransferFunction', 'setPrimaries', 'setWhitePoint', 'whitePoint',
  'setPrimaryPoints', 'primaryPoints', 'transformModel', 'colorModel',
  'detach', 'isValid', 'isValidTarget', '__eq__', '__ne__', 'fromIccProfile',
  'iccProfile', 'transformationToColorSpace', 'equals', '__rlshift__'. It can
  be made from Python, in 8 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorSpace::QColorSpace(QPointF whitePoint, const QList<uint16_t>
    &transferFunctionTable)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QColorSpace::QColorSpace(Primaries primaries, const QList<uint16_t>
    &transferFunctionTable)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QColorSpace::QColorSpace(const QPointF &whitePoint, const QPointF
    &redPoint, const QPointF &greenPoint, const QPointF &bluePoint, const
    QList<uint16_t> &transferFunctionTable)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QColorSpace::QColorSpace(const QPointF &whitePoint, const QPointF
    &redPoint, const QPointF &greenPoint, const QPointF &bluePoint, const
    QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QColorSpace::~QColorSpace()': the destructor: Python removes its
    C++ QColorSpace by it, and has no other use for it.
  - Qt's 'QColorSpace &QColorSpace::operator=(const QColorSpace
    &colorSpace)': assignment: Python binds a name and has no operator for
    it.
  - Qt's 'QColorSpace::QColorSpace(QColorSpace &&colorSpace)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QColorSpace &QColorSpace::operator=(QColorSpace &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QColorSpace::swap(QColorSpace &colorSpace)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QColorSpace::setTransferFunction(const QList<uint16_t>
    &transferFunctionTable)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QColorSpace::setTransferFunctions(const QList<uint16_t>
    &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QColorSpace QColorSpace::withTransferFunction(const QList<uint16_t>
    &transferFunctionTable) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QColorSpace QColorSpace::withTransferFunctions(const
    QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QVariant QColorSpace::operator QVariant() const': an operator
    Python has no name for.

  What has no ritual
  ------------------

  3 of the 50 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QColorSpace is created at the first use, not by
    'QColorSpace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorSpace back gives a copy the ritual made for
    Python, in a new cute QColorSpace.
  - Each name of Qt's QColorSpace that has no cute function yet,
    'setTransferFunctions', 'swap', 'withTransferFunctions', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QColorSpace, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ColorModel(CuteNum, scoped=True):
    """
    The enum 'QColorSpace::ColorModel' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Undefined = Kee[int](0)
    Rgb = Kee[int](1)
    Gray = Kee[int](2)
    Cmyk = Kee[int](3)

  class NamedColorSpace(CuteNum):
    """
    The enum 'QColorSpace::NamedColorSpace' of Qt, with the 8 names Qt gives
    in it.
    """

    SRgb = Kee[int](1)
    SRgbLinear = Kee[int](2)
    AdobeRgb = Kee[int](3)
    DisplayP3 = Kee[int](4)
    ProPhotoRgb = Kee[int](5)
    Bt2020 = Kee[int](6)
    Bt2100Pq = Kee[int](7)
    Bt2100Hlg = Kee[int](8)

  class Primaries(CuteNum, scoped=True):
    """
    The enum 'QColorSpace::Primaries' of Qt, with the 6 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Custom = Kee[int](0)
    SRgb = Kee[int](1)
    AdobeRgb = Kee[int](2)
    DciP3D65 = Kee[int](3)
    ProPhotoRgb = Kee[int](4)
    Bt2020 = Kee[int](5)

  class TransferFunction(CuteNum, scoped=True):
    """
    The enum 'QColorSpace::TransferFunction' of Qt, with the 8 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Custom = Kee[int](0)
    Linear = Kee[int](1)
    Gamma = Kee[int](2)
    SRgb = Kee[int](3)
    ProPhotoRgb = Kee[int](4)
    Bt2020 = Kee[int](5)
    St2084 = Kee[int](6)
    Hlg = Kee[int](7)

  class TransformModel(CuteNum, scoped=True):
    """
    The enum 'QColorSpace::TransformModel' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    ThreeComponentMatrix = Kee[int](0)
    ElementListProcessing = Kee[int](1)

  #  The classes Qt writes inside QColorSpace, each a class in here as in
  #  C++.

  class PrimaryPoints(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QColorSpace::PrimaryPoints: a plain Python object
    standing in front of one C++ QColorSpace::PrimaryPoints.

    C++ hands a QColorSpace::PrimaryPoints around as a copy, so every C++
    QColorSpace::PrimaryPoints behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QColorSpace::PrimaryPoints that has a ritual and
    that Python can call so far, 1 name in all: 'isValid'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'PrimaryPoints QColorSpace::PrimaryPoints::fromPrimaries(Primaries
      primaries)': names the enum 'QColorSpace::Primaries', whose class
      cannot be named here.
    - Qt's 'QColorSpace::PrimaryPoints::~PrimaryPoints()': the destructor:
      Python removes its C++ QColorSpace::PrimaryPoints by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QColorSpace::PrimaryPoints is created at the first use, not by
      'QColorSpace::PrimaryPoints(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QColorSpace::PrimaryPoints back gives a copy the
      ritual made for Python, in a new cute QColorSpace::PrimaryPoints.
    - Each name of Qt's QColorSpace::PrimaryPoints that has no cute function
      yet, 'fromPrimaries', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QColorSpace::PrimaryPoints'

    #  Qt's '~QColorSpace::PrimaryPoints()'. Naming it makes this a value
    #  class: Python owns every C++ QColorSpace::PrimaryPoints behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QColorSpace13PrimaryPointsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QColorSpace::PrimaryPoints::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcolorspace-primarypoints.html#isValid
      """
      #  bool QColorSpace::PrimaryPoints::isValid() const
      return self.uglySide.call(
          'ritual_ZNK11QColorSpace13PrimaryPoints7isValidEv',
      )

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

    @staticmethod
    def fromPrimaries(*__, **_) -> Never:
      """
      Qt's 'PrimaryPoints QColorSpace::PrimaryPoints::fromPrimaries(Primaries
      primaries)': names the enum 'QColorSpace::Primaries', whose class
      cannot be named here.
      """
      raise NotImplementedError(
          "'QColorSpace.PrimaryPoints.fromPrimaries' has no cute function "
          "yet. Qt's 'PrimaryPoints "
          "QColorSpace::PrimaryPoints::fromPrimaries(Primaries primaries)': "
          "names the enum 'QColorSpace::Primaries', whose class cannot be "
          "named here.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def fromIccProfile(iccProfile: QByteArray) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QColorSpace::fromIccProfile(const QByteArray
    &iccProfile)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#fromIccProfile

    Parameters
    ----------

    iccProfile : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QColorSpace::fromIccProfile(const QByteArray &iccProfile)
    address = Rituals.call(
        'ritual_ZN11QColorSpace14fromIccProfileERK10QByteArray',
        CuteMixin._valueOf(iccProfile),
    )
    return QColorSpace._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorSpace'

  #  Qt's '~QColorSpace()'. Naming it makes this a value class: Python owns
  #  every C++ QColorSpace behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QColorSpaceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def primaries(self) -> Primaries:
    """
    Calls Qt's 'Primaries QColorSpace::primaries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#primaries

    Returns
    -------

    Primaries
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Primaries(number)' gives.
    """
    #  Primaries QColorSpace::primaries() const
    return QColorSpace.Primaries(self.uglySide.call(
        'ritual_ZNK11QColorSpace9primariesEv',
    ))

  def transferFunction(self) -> TransferFunction:
    """
    Calls Qt's 'TransferFunction QColorSpace::transferFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#transferFunction

    Returns
    -------

    TransferFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransferFunction(number)'
      gives.
    """
    #  TransferFunction QColorSpace::transferFunction() const
    return QColorSpace.TransferFunction(self.uglySide.call(
        'ritual_ZNK11QColorSpace16transferFunctionEv',
    ))

  def gamma(self) -> float:
    """
    Calls Qt's 'float QColorSpace::gamma() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#gamma
    """
    #  float QColorSpace::gamma() const
    return self.uglySide.call('ritual_ZNK11QColorSpace5gammaEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QColorSpace::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QColorSpace::description() const
    return self.uglySide.call('ritual_ZNK11QColorSpace11descriptionEv')

  @overload(TransferFunction)
  @overload(TransferFunction, float)
  def withTransferFunction(
      self,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace
    QColorSpace::withTransferFunction(TransferFunction transferFunction,
    float gamma) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspace.html#withTransferFunction

    Parameters
    ----------

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QColorSpace::withTransferFunction(TransferFunction
    #      transferFunction, float gamma) const
    address = self.uglySide.call(
        'ritual_ZNK11QColorSpace20withTransferFunctionENS_16TransferFunctio'
        'nEf',
        transferFunction.value, gamma,
    )
    return QColorSpace._cuteOwning(address)

  def whitePoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QColorSpace::whitePoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#whitePoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QColorSpace::whitePoint() const
    address = self.uglySide.call('ritual_ZNK11QColorSpace10whitePointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def primaryPoints(self) -> PrimaryPoints:
    """
    Calls Qt's 'PrimaryPoints QColorSpace::primaryPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#primaryPoints

    Returns
    -------

    PrimaryPoints
      A new cute QColorSpace::PrimaryPoints around the copy Qt gave back.
      Python owns it.
    """
    #  PrimaryPoints QColorSpace::primaryPoints() const
    address = self.uglySide.call('ritual_ZNK11QColorSpace13primaryPointsEv')
    return QColorSpace.PrimaryPoints._cuteOwning(address)

  def transformModel(self) -> TransformModel:
    """
    Calls Qt's 'TransformModel QColorSpace::transformModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#transformModel

    Returns
    -------

    TransformModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransformModel(number)'
      gives.
    """
    #  TransformModel QColorSpace::transformModel() const
    return QColorSpace.TransformModel(self.uglySide.call(
        'ritual_ZNK11QColorSpace14transformModelEv',
    ))

  def colorModel(self) -> ColorModel:
    """
    Calls Qt's 'ColorModel QColorSpace::colorModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#colorModel

    Returns
    -------

    ColorModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorModel(number)'
      gives.
    """
    #  ColorModel QColorSpace::colorModel() const
    return QColorSpace.ColorModel(self.uglySide.call(
        'ritual_ZNK11QColorSpace10colorModelEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColorSpace::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#isValid
    """
    #  bool QColorSpace::isValid() const
    return self.uglySide.call('ritual_ZNK11QColorSpace7isValidEv')

  def isValidTarget(self) -> bool:
    """
    Calls Qt's 'bool QColorSpace::isValidTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#isValidTarget
    """
    #  bool QColorSpace::isValidTarget() const
    return self.uglySide.call('ritual_ZNK11QColorSpace13isValidTargetEv')

  def iccProfile(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QColorSpace::iccProfile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#iccProfile

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QColorSpace::iccProfile() const
    address = self.uglySide.call('ritual_ZNK11QColorSpace10iccProfileEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(THIS)
  def transformationToColorSpace(
      self,
      colorspace: QColorSpace,
  ) -> QColorTransform:
    """
    Calls Qt's 'QColorTransform QColorSpace::transformationToColorSpace(const
    QColorSpace &colorspace) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspace.html#transformationToColorSpace

    Parameters
    ----------

    colorspace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.

    Returns
    -------

    QColorTransform
      A new cute QColorTransform around the copy Qt gave back. Python owns
      it.
    """
    #  QColorTransform QColorSpace::transformationToColorSpace(const
    #      QColorSpace &colorspace) const
    address = self.uglySide.call(
        'ritual_ZNK11QColorSpace26transformationToColorSpaceERKS_',
        self._valueOf(colorspace),
    )
    from . import QColorTransform
    return QColorTransform._cuteOwning(address)

  @overload(THIS)
  def equals(self, other: QColorSpace) -> bool:
    """
    Calls Qt's 'bool QColorSpace::equals(const QColorSpace &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#equals

    Parameters
    ----------

    other : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  bool QColorSpace::equals(const QColorSpace &other) const
    return self.uglySide.call(
        'ritual_ZNK11QColorSpace6equalsERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QColorSpace::setDescription(const QString
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QColorSpace::setDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN11QColorSpace14setDescriptionERK7QString', description,
    )

  @overload(TransferFunction)
  @overload(TransferFunction, float)
  def setTransferFunction(
      self,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Calls Qt's 'void QColorSpace::setTransferFunction(TransferFunction
    transferFunction, float gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorspace.html#setTransferFunction

    Parameters
    ----------

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QColorSpace::setTransferFunction(TransferFunction
    #      transferFunction, float gamma)
    self.uglySide.call(
        'ritual_ZN11QColorSpace19setTransferFunctionENS_16TransferFunctionE'
        'f',
        transferFunction.value, gamma,
    )

  @overload(Primaries)
  def setPrimaries(self, primariesId: Primaries) -> None:
    """
    Calls Qt's 'void QColorSpace::setPrimaries(Primaries primariesId)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setPrimaries

    Parameters
    ----------

    primariesId : Primaries
      Passed on as its number.
    """
    #  void QColorSpace::setPrimaries(Primaries primariesId)
    self.uglySide.call(
        'ritual_ZN11QColorSpace12setPrimariesENS_9PrimariesE',
        primariesId.value,
    )

  @overload(QPointF, QPointF, QPointF, QPointF)
  def setPrimaries(
      self,
      whitePoint: QPointF,
      redPoint: QPointF,
      greenPoint: QPointF,
      bluePoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QColorSpace::setPrimaries(const QPointF &whitePoint,
    const QPointF &redPoint, const QPointF &greenPoint, const QPointF
    &bluePoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setPrimaries

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    redPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    greenPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    bluePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QColorSpace::setPrimaries(const QPointF &whitePoint, const
    #      QPointF &redPoint, const QPointF &greenPoint, const QPointF
    #      &bluePoint)
    self.uglySide.call(
        'ritual_ZN11QColorSpace12setPrimariesERK7QPointFS2_S2_S2_',
        self._valueOf(whitePoint, 'QPointF'), self._valueOf(redPoint,
        'QPointF'), self._valueOf(greenPoint, 'QPointF'),
        self._valueOf(bluePoint, 'QPointF'),
    )

  @overload(QPointF)
  def setWhitePoint(self, whitePoint: QPointF) -> None:
    """
    Calls Qt's 'void QColorSpace::setWhitePoint(QPointF whitePoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setWhitePoint

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QColorSpace::setWhitePoint(QPointF whitePoint)
    self.uglySide.call(
        'ritual_ZN11QColorSpace13setWhitePointE7QPointF',
        self._valueOf(whitePoint, 'QPointF'),
    )

  @overload(PrimaryPoints)
  def setPrimaryPoints(self, primaryPoints: PrimaryPoints) -> None:
    """
    Calls Qt's 'void QColorSpace::setPrimaryPoints(const PrimaryPoints
    &primaryPoints)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#setPrimaryPoints

    Parameters
    ----------

    primaryPoints : PrimaryPoints
      Passed on as a value: Qt reads the C++ QColorSpace::PrimaryPoints,
      which stays Python's own.
    """
    #  void QColorSpace::setPrimaryPoints(const PrimaryPoints &primaryPoints)
    self.uglySide.call(
        'ritual_ZN11QColorSpace16setPrimaryPointsERKNS_13PrimaryPointsE',
        self._valueOf(primaryPoints),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, colorSpace2: QColorSpace) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorSpace &colorSpace1, const
    QColorSpace &colorSpace2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#operator==

    Parameters
    ----------

    colorSpace2 : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  bool operator==(const QColorSpace &colorSpace1, const QColorSpace
    #      &colorSpace2)
    return Rituals.call(
        'ritual_ZeqRK11QColorSpaceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(colorSpace2),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, colorSpace2: QColorSpace) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorSpace &colorSpace1, const
    QColorSpace &colorSpace2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#operator!=

    Parameters
    ----------

    colorSpace2 : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  bool operator!=(const QColorSpace &colorSpace1, const QColorSpace
    #      &colorSpace2)
    return Rituals.call(
        'ritual_ZneRK11QColorSpaceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(colorSpace2),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QColorSpace
    &colorSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QColorSpace &colorSpace)
    address = Rituals.call(
        'ritual_Zls6QDebugRK11QColorSpace',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace
    """
    #  QColorSpace::QColorSpace()
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1Ev',
    ))

  @overload(NamedColorSpace)
  def __init__(self, namedColorSpace: NamedColorSpace) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(NamedColorSpace
    namedColorSpace)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    namedColorSpace : NamedColorSpace
      Passed on as its number.
    """
    #  QColorSpace::QColorSpace(NamedColorSpace namedColorSpace)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ENS_15NamedColorSpaceE',
        namedColorSpace.value,
    ))

  @overload(QPointF, TransferFunction)
  @overload(QPointF, TransferFunction, float)
  def __init__(
      self,
      whitePoint: QPointF,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(QPointF
    whitePoint, TransferFunction transferFunction, float gamma)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(QPointF whitePoint, TransferFunction
    #      transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1E7QPointFNS_16TransferFunctionEf',
        self._valueOf(whitePoint, 'QPointF'), transferFunction.value, gamma,
    ))

  @overload(Primaries, TransferFunction)
  @overload(Primaries, TransferFunction, float)
  def __init__(
      self,
      primaries: Primaries,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(Primaries
    primaries, TransferFunction transferFunction, float gamma)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    primaries : Primaries
      Passed on as its number.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(Primaries primaries, TransferFunction
    #      transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ENS_9PrimariesENS_16TransferFunctionEf',
        primaries.value, transferFunction.value, gamma,
    ))

  @overload(Primaries, float)
  def __init__(self, primaries: Primaries, gamma: float) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(Primaries
    primaries, float gamma)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    primaries : Primaries
      Passed on as its number.

    gamma : float
      Passed on as it is.
    """
    #  QColorSpace::QColorSpace(Primaries primaries, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ENS_9PrimariesEf', primaries.value, gamma,
    ))

  @overload(QPointF, QPointF, QPointF, QPointF, TransferFunction)
  @overload(QPointF, QPointF, QPointF, QPointF, TransferFunction, float)
  def __init__(
      self,
      whitePoint: QPointF,
      redPoint: QPointF,
      greenPoint: QPointF,
      bluePoint: QPointF,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(const QPointF
    &whitePoint, const QPointF &redPoint, const QPointF &greenPoint, const
    QPointF &bluePoint, TransferFunction transferFunction, float gamma)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    whitePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    redPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    greenPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    bluePoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(const QPointF &whitePoint, const QPointF
    #      &redPoint, const QPointF &greenPoint, const QPointF &bluePoint,
    #      TransferFunction transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ERK7QPointFS2_S2_S2_NS_16TransferFunctionE'
        'f',
        self._valueOf(whitePoint, 'QPointF'), self._valueOf(redPoint,
        'QPointF'), self._valueOf(greenPoint, 'QPointF'),
        self._valueOf(bluePoint, 'QPointF'), transferFunction.value, gamma,
    ))

  @overload(PrimaryPoints, TransferFunction)
  @overload(PrimaryPoints, TransferFunction, float)
  def __init__(
      self,
      primaryPoints: PrimaryPoints,
      transferFunction: TransferFunction,
      gamma: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(const
    PrimaryPoints &primaryPoints, TransferFunction transferFunction, float
    gamma)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    primaryPoints : PrimaryPoints
      Passed on as a value: Qt reads the C++ QColorSpace::PrimaryPoints,
      which stays Python's own.

    transferFunction : TransferFunction
      Passed on as its number.

    gamma : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorSpace::QColorSpace(const PrimaryPoints &primaryPoints,
    #      TransferFunction transferFunction, float gamma)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ERKNS_13PrimaryPointsENS_16TransferFunctio'
        'nEf',
        self._valueOf(primaryPoints), transferFunction.value, gamma,
    ))

  @overload(THIS)
  def __init__(self, colorSpace: QColorSpace) -> None:
    """
    Notes what was given, for Qt's 'QColorSpace::QColorSpace(const
    QColorSpace &colorSpace)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#QColorSpace

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  QColorSpace::QColorSpace(const QColorSpace &colorSpace)
    self._noteCreation(QColorSpace, lambda: Rituals.call(
        'ritual_ZN11QColorSpaceC1ERKS_', self._valueOf(colorSpace),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QColorSpace::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorspace.html#detach
    """
    #  void QColorSpace::detach()
    self.uglySide.call('ritual_ZN11QColorSpace6detachEv')

  @staticmethod
  def setTransferFunctions(*__, **_) -> Never:
    """
    Qt's 'void QColorSpace::setTransferFunctions(const QList<uint16_t>
    &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QColorSpace.setTransferFunctions' has no cute function yet. Qt's "
        "'void QColorSpace::setTransferFunctions(const QList<uint16_t> "
        "&redTransferFunctionTable, const QList<uint16_t> "
        "&greenTransferFunctionTable, const QList<uint16_t> "
        "&blueTransferFunctionTable)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QColorSpace::swap(QColorSpace &colorSpace)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QColorSpace.swap' has no cute function yet. Qt's 'void "
        "QColorSpace::swap(QColorSpace &colorSpace)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def withTransferFunctions(*__, **_) -> Never:
    """
    Qt's 'QColorSpace QColorSpace::withTransferFunctions(const
    QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t>
    &greenTransferFunctionTable, const QList<uint16_t>
    &blueTransferFunctionTable) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QColorSpace.withTransferFunctions' has no cute function yet. Qt's "
        "'QColorSpace QColorSpace::withTransferFunctions(const "
        "QList<uint16_t> &redTransferFunctionTable, const QList<uint16_t> "
        "&greenTransferFunctionTable, const QList<uint16_t> "
        "&blueTransferFunctionTable) const': takes a type Python has no way "
        "to hand over yet.")
