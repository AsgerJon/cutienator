"""
QQuickImageProviderOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickImageProviderOptions to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
  from ..QtGui import QColorSpace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorSpace = WAIT['QColorSpace']
  QRectF = WAIT['QRectF']


class QQuickImageProviderOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickImageProviderOptions: a plain Python object
  standing in front of one C++ QQuickImageProviderOptions.

  C++ hands a QQuickImageProviderOptions around as a copy, so every C++
  QQuickImageProviderOptions behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickImageProviderOptions that has a ritual and
  that Python can call so far, 11 names in all: '__eq__', 'autoTransform',
  'setAutoTransform', 'preserveAspectRatioCrop',
  'setPreserveAspectRatioCrop', 'preserveAspectRatioFit',
  'setPreserveAspectRatioFit', 'targetColorSpace', 'setTargetColorSpace',
  'sourceClipRect', 'setSourceClipRect'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickImageProviderOptions::~QQuickImageProviderOptions()': the
    destructor: Python removes its C++ QQuickImageProviderOptions by it, and
    has no other use for it.
  - Qt's 'QQuickImageProviderOptions
    &QQuickImageProviderOptions::operator=(const QQuickImageProviderOptions
    &a0)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QQuickImageProviderOptions is created at the first use, not by
    'QQuickImageProviderOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickImageProviderOptions back gives a copy the
    ritual made for Python, in a new cute QQuickImageProviderOptions.
  """

  #  The enums Qt writes inside QQuickImageProviderOptions, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class AutoTransform(CuteNum):
    """
    The enum 'QQuickImageProviderOptions::AutoTransform' of Qt, with the 3
    names Qt gives in it.
    """

    UsePluginDefaultTransform = Kee[int](-1)
    ApplyTransform = Kee[int](0)
    DoNotApplyTransform = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickImageProviderOptions'

  #  Qt's '~QQuickImageProviderOptions()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickImageProviderOptions behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuickImageProviderOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def autoTransform(self) -> AutoTransform:
    """
    Calls Qt's 'AutoTransform QQuickImageProviderOptions::autoTransform()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html#autoTransform

    Returns
    -------

    AutoTransform
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AutoTransform(number)'
      gives.
    """
    #  AutoTransform QQuickImageProviderOptions::autoTransform() const
    return QQuickImageProviderOptions.AutoTransform(self.uglySide.call(
        'ritual_ZNK26QQuickImageProviderOptions13autoTransformEv',
    ))

  def preserveAspectRatioCrop(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageProviderOptions::preserveAspectRatioCrop()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html
    """
    #  bool QQuickImageProviderOptions::preserveAspectRatioCrop() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickImageProviderOptions23preserveAspectRatioCropEv',
    )

  def preserveAspectRatioFit(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageProviderOptions::preserveAspectRatioFit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html
    """
    #  bool QQuickImageProviderOptions::preserveAspectRatioFit() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickImageProviderOptions22preserveAspectRatioFitEv',
    )

  def targetColorSpace(self) -> QColorSpace:
    """
    Calls Qt's 'QColorSpace QQuickImageProviderOptions::targetColorSpace()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html#targetColorSpace

    Returns
    -------

    QColorSpace
      A new cute QColorSpace around the copy Qt gave back. Python owns it.
    """
    #  QColorSpace QQuickImageProviderOptions::targetColorSpace() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickImageProviderOptions16targetColorSpaceEv',
    )
    from ..QtGui import QColorSpace
    return QColorSpace._cuteOwning(address)

  def sourceClipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickImageProviderOptions::sourceClipRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html#sourceClipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickImageProviderOptions::sourceClipRect() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickImageProviderOptions14sourceClipRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AutoTransform)
  def setAutoTransform(self, autoTransform: AutoTransform) -> None:
    """
    Calls Qt's 'void
    QQuickImageProviderOptions::setAutoTransform(AutoTransform
    autoTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html#setAutoTransform

    Parameters
    ----------

    autoTransform : AutoTransform
      Passed on as its number.
    """
    #  void QQuickImageProviderOptions::setAutoTransform(AutoTransform
    #      autoTransform)
    self.uglySide.call(
        'ritual_ZN26QQuickImageProviderOptions16setAutoTransformENS_13AutoT'
        'ransformE',
        autoTransform.value,
    )

  @overload(bool)
  def setPreserveAspectRatioCrop(
      self,
      preserveAspectRatioCrop: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickImageProviderOptions::setPreserveAspectRatioCrop(bool
    preserveAspectRatioCrop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html

    Parameters
    ----------

    preserveAspectRatioCrop : bool
      Passed on as it is.
    """
    #  void QQuickImageProviderOptions::setPreserveAspectRatioCrop(bool
    #      preserveAspectRatioCrop)
    self.uglySide.call(
        'ritual_ZN26QQuickImageProviderOptions26setPreserveAspectRatioCropE'
        'b',
        preserveAspectRatioCrop,
    )

  @overload(bool)
  def setPreserveAspectRatioFit(self, preserveAspectRatioFit: bool) -> None:
    """
    Calls Qt's 'void
    QQuickImageProviderOptions::setPreserveAspectRatioFit(bool
    preserveAspectRatioFit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html

    Parameters
    ----------

    preserveAspectRatioFit : bool
      Passed on as it is.
    """
    #  void QQuickImageProviderOptions::setPreserveAspectRatioFit(bool
    #      preserveAspectRatioFit)
    self.uglySide.call(
        'ritual_ZN26QQuickImageProviderOptions25setPreserveAspectRatioFitEb',
        preserveAspectRatioFit,
    )

  @overload(QColorSpace)
  def setTargetColorSpace(self, colorSpace: QColorSpace) -> None:
    """
    Calls Qt's 'void QQuickImageProviderOptions::setTargetColorSpace(const
    QColorSpace &colorSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html

    Parameters
    ----------

    colorSpace : QColorSpace
      Passed on as a value: Qt reads the C++ QColorSpace, which stays
      Python's own.
    """
    #  void QQuickImageProviderOptions::setTargetColorSpace(const QColorSpace
    #      &colorSpace)
    self.uglySide.call(
        'ritual_ZN26QQuickImageProviderOptions19setTargetColorSpaceERK11QCo'
        'lorSpace',
        self._valueOf(colorSpace),
    )

  @overload(QRectF)
  def setSourceClipRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickImageProviderOptions::setSourceClipRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html#setSourceClipRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickImageProviderOptions::setSourceClipRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN26QQuickImageProviderOptions17setSourceClipRectERK6QRectF',
        self._valueOf(rect),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QQuickImageProviderOptions) -> bool:
    """
    Calls Qt's 'bool QQuickImageProviderOptions::operator==(const
    QQuickImageProviderOptions &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html#operator==

    Parameters
    ----------

    a0 : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.
    """
    #  bool QQuickImageProviderOptions::operator==(const
    #      QQuickImageProviderOptions &a0) const
    return self.uglySide.call(
        'ritual_ZNK26QQuickImageProviderOptionseqERKS_', self._valueOf(a0),
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
    'QQuickImageProviderOptions::QQuickImageProviderOptions()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html
    """
    #  QQuickImageProviderOptions::QQuickImageProviderOptions()
    self._noteCreation(QQuickImageProviderOptions, lambda: Rituals.call(
        'ritual_ZN26QQuickImageProviderOptionsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QQuickImageProviderOptions) -> None:
    """
    Notes what was given, for Qt's
    'QQuickImageProviderOptions::QQuickImageProviderOptions(const
    QQuickImageProviderOptions &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageprovideroptions.html

    Parameters
    ----------

    a0 : QQuickImageProviderOptions
      Passed on as a value: Qt reads the C++ QQuickImageProviderOptions,
      which stays Python's own.
    """
    #  QQuickImageProviderOptions::QQuickImageProviderOptions(const
    #      QQuickImageProviderOptions &a0)
    self._noteCreation(QQuickImageProviderOptions, lambda: Rituals.call(
        'ritual_ZN26QQuickImageProviderOptionsC1ERKS_', self._valueOf(a0),
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
