"""
QPdfDocumentRenderOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdfdocumentrenderoptions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRect, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']


class QPdfDocumentRenderOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdfDocumentRenderOptions: a plain Python object
  standing in front of one C++ QPdfDocumentRenderOptions.

  C++ hands a QPdfDocumentRenderOptions around as a copy, so every C++
  QPdfDocumentRenderOptions behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPdfDocumentRenderOptions that has a ritual and that
  Python can call so far, 9 names in all: 'rotation', 'setRotation',
  'renderFlags', 'setRenderFlags', 'scaledClipRect', 'setScaledClipRect',
  'scaledSize', 'setScaledSize', '__eq__'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfDocumentRenderOptions::~QPdfDocumentRenderOptions()': the
    destructor: Python removes its C++ QPdfDocumentRenderOptions by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QPdfDocumentRenderOptions is created at the first use, not by
    'QPdfDocumentRenderOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfDocumentRenderOptions back gives a copy the
    ritual made for Python, in a new cute QPdfDocumentRenderOptions.
  """

  #  The enums Qt writes inside QPdfDocumentRenderOptions, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RenderFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QPdfDocumentRenderOptions::RenderFlag' of Qt, with the 8
    names Qt gives in it. Qt names the type of its combinations
    'QPdfDocumentRenderOptions::RenderFlags'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    Annotations = 0x1
    OptimizedForLcd = 0x2
    Grayscale = 0x4
    ForceHalftone = 0x8
    TextAliased = 0x10
    ImageAliased = 0x20
    PathAliased = 0x40

  RenderFlags = RenderFlag

  class Rotation(CuteNum, scoped=True):
    """
    The enum 'QPdfDocumentRenderOptions::Rotation' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Clockwise90 = Kee[int](1)
    Clockwise180 = Kee[int](2)
    Clockwise270 = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfDocumentRenderOptions'

  #  Qt's '~QPdfDocumentRenderOptions()'. Naming it makes this a value class:
  #  Python owns every C++ QPdfDocumentRenderOptions behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QPdfDocumentRenderOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rotation(self) -> Rotation:
    """
    Calls Qt's 'Rotation QPdfDocumentRenderOptions::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#rotation

    Returns
    -------

    Rotation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Rotation(number)' gives.
    """
    #  Rotation QPdfDocumentRenderOptions::rotation() const
    return QPdfDocumentRenderOptions.Rotation(self.uglySide.call(
        'ritual_ZNK25QPdfDocumentRenderOptions8rotationEv',
    ))

  def renderFlags(self) -> RenderFlags:
    """
    Calls Qt's 'RenderFlags QPdfDocumentRenderOptions::renderFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#renderFlags

    Returns
    -------

    RenderFlags
      The value standing for the combination Qt gave back.
    """
    #  RenderFlags QPdfDocumentRenderOptions::renderFlags() const
    return QPdfDocumentRenderOptions.RenderFlags(self.uglySide.call(
        'ritual_ZNK25QPdfDocumentRenderOptions11renderFlagsEv',
    ))

  def scaledClipRect(self) -> QRect:
    """
    Calls Qt's 'QRect QPdfDocumentRenderOptions::scaledClipRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#scaledClipRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPdfDocumentRenderOptions::scaledClipRect() const
    address = self.uglySide.call(
        'ritual_ZNK25QPdfDocumentRenderOptions14scaledClipRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def scaledSize(self) -> QSize:
    """
    Calls Qt's 'QSize QPdfDocumentRenderOptions::scaledSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#scaledSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPdfDocumentRenderOptions::scaledSize() const
    address = self.uglySide.call(
        'ritual_ZNK25QPdfDocumentRenderOptions10scaledSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Rotation)
  def setRotation(self, r: Rotation) -> None:
    """
    Calls Qt's 'void QPdfDocumentRenderOptions::setRotation(Rotation r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#setRotation

    Parameters
    ----------

    r : Rotation
      Passed on as its number.
    """
    #  void QPdfDocumentRenderOptions::setRotation(Rotation r)
    self.uglySide.call(
        'ritual_ZN25QPdfDocumentRenderOptions11setRotationENS_8RotationE',
        r.value,
    )

  @overload(RenderFlags)
  def setRenderFlags(self, r: RenderFlags) -> None:
    """
    Calls Qt's 'void QPdfDocumentRenderOptions::setRenderFlags(RenderFlags
    r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#setRenderFlags

    Parameters
    ----------

    r : RenderFlags
      Passed on as its number.
    """
    #  void QPdfDocumentRenderOptions::setRenderFlags(RenderFlags r)
    self.uglySide.call(
        'ritual_ZN25QPdfDocumentRenderOptions14setRenderFlagsE6QFlagsINS_10'
        'RenderFlagEE',
        r.value,
    )

  @overload(QRect)
  def setScaledClipRect(self, r: QRect) -> None:
    """
    Calls Qt's 'void QPdfDocumentRenderOptions::setScaledClipRect(const QRect
    &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#setScaledClipRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPdfDocumentRenderOptions::setScaledClipRect(const QRect &r)
    self.uglySide.call(
        'ritual_ZN25QPdfDocumentRenderOptions17setScaledClipRectERK5QRect',
        self._valueOf(r),
    )

  @overload(QSize)
  def setScaledSize(self, s: QSize) -> None:
    """
    Calls Qt's 'void QPdfDocumentRenderOptions::setScaledSize(const QSize
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#setScaledSize

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QPdfDocumentRenderOptions::setScaledSize(const QSize &s)
    self.uglySide.call(
        'ritual_ZN25QPdfDocumentRenderOptions13setScaledSizeERK5QSize',
        self._valueOf(s),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPdfDocumentRenderOptions) -> bool:
    """
    Calls Qt's 'bool operator==(const QPdfDocumentRenderOptions &lhs, const
    QPdfDocumentRenderOptions &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html#operator==

    Parameters
    ----------

    rhs : QPdfDocumentRenderOptions
      Passed on as a value: Qt reads the C++ QPdfDocumentRenderOptions, which
      stays Python's own.
    """
    #  bool operator==(const QPdfDocumentRenderOptions &lhs, const
    #      QPdfDocumentRenderOptions &rhs)
    return Rituals.call(
        'ritual_ZeqRK25QPdfDocumentRenderOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    Notes what was given, for Qt's
    'QPdfDocumentRenderOptions::QPdfDocumentRenderOptions()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocumentrenderoptions.html
    """
    #  QPdfDocumentRenderOptions::QPdfDocumentRenderOptions()
    self._noteCreation(QPdfDocumentRenderOptions, lambda: Rituals.call(
        'ritual_ZN25QPdfDocumentRenderOptionsC1Ev',
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
