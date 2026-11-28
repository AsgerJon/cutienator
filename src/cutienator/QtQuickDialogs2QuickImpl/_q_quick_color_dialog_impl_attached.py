"""
QQuickColorDialogImplAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickColorDialogImplAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAbstractColorPicker
  from . import QQuickColorDialogImplAttachedPrivate, QQuickColorInputs
  from ..QtQuickTemplates2 import QQuickAbstractButton, QQuickDialogButtonBox
  from ..QtQuickTemplates2 import QQuickSlider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickAbstractColorPicker = WAIT['QQuickAbstractColorPicker']
  QQuickColorInputs = WAIT['QQuickColorInputs']
  QQuickDialogButtonBox = WAIT['QQuickDialogButtonBox']
  QQuickSlider = WAIT['QQuickSlider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorDialogImplAttached(QObject):
  """
  The cute side of Qt's QQuickColorDialogImplAttached: a plain Python object
  standing in front of one C++ QQuickColorDialogImplAttached.

  It is built on the cute 'QObject', as Qt's QQuickColorDialogImplAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickColorDialogImplAttached that has a ritual and
  that Python can call so far, 18 names in all: 'metaObject', 'tr',
  'buttonBox', 'setButtonBox', 'eyeDropperButton', 'setEyeDropperButton',
  'colorPicker', 'setColorPicker', 'colorInputs', 'setColorInputs',
  'alphaSlider', 'setAlphaSlider', 'buttonBoxChanged',
  'eyeDropperButtonChanged', 'colorPickerChanged', 'colorInputsChanged',
  'alphaSliderChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorDialogImplAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickColorDialogImplAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickColorDialogImplAttachedPrivate
    *QQuickColorDialogImplAttached::d_func() const': takes in Python what
    'QQuickColorDialogImplAttachedPrivate
    *QQuickColorDialogImplAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickColorDialogImplAttached is created at the first use, not by
    'QQuickColorDialogImplAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorDialogImplAttached.
  - Qt tells when it has removed the C++ QQuickColorDialogImplAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickColorDialogImplAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickColorDialogImplAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuickColorDialogImplAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorDialogImplAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickColorDialogImplAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorDialogImplAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickColorDialogImplAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buttonBox(self) -> Optional[QQuickDialogButtonBox]:
    """
    Calls Qt's 'QQuickDialogButtonBox
    *QQuickColorDialogImplAttached::buttonBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#buttonBox

    Returns
    -------

    Optional[QQuickDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBox *QQuickColorDialogImplAttached::buttonBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickColorDialogImplAttached9buttonBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickDialogButtonBox
    return QQuickDialogButtonBox._cuteAt(address)

  def eyeDropperButton(self) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton
    *QQuickColorDialogImplAttached::eyeDropperButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton
    #      *QQuickColorDialogImplAttached::eyeDropperButton() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickColorDialogImplAttached16eyeDropperButtonEv',
    )
    from ..QtQuickTemplates2 import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def colorPicker(self) -> Optional[QQuickAbstractColorPicker]:
    """
    Calls Qt's 'QQuickAbstractColorPicker
    *QQuickColorDialogImplAttached::colorPicker() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#colorPicker

    Returns
    -------

    Optional[QQuickAbstractColorPicker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractColorPicker
    #      *QQuickColorDialogImplAttached::colorPicker() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickColorDialogImplAttached11colorPickerEv',
    )
    from . import QQuickAbstractColorPicker
    return QQuickAbstractColorPicker._cuteAt(address)

  def colorInputs(self) -> Optional[QQuickColorInputs]:
    """
    Calls Qt's 'QQuickColorInputs
    *QQuickColorDialogImplAttached::colorInputs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#colorInputs

    Returns
    -------

    Optional[QQuickColorInputs]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorInputs *QQuickColorDialogImplAttached::colorInputs() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickColorDialogImplAttached11colorInputsEv',
    )
    from . import QQuickColorInputs
    return QQuickColorInputs._cuteAt(address)

  def alphaSlider(self) -> Optional[QQuickSlider]:
    """
    Calls Qt's 'QQuickSlider *QQuickColorDialogImplAttached::alphaSlider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#alphaSlider

    Returns
    -------

    Optional[QQuickSlider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSlider *QQuickColorDialogImplAttached::alphaSlider() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickColorDialogImplAttached11alphaSliderEv',
    )
    from ..QtQuickTemplates2 import QQuickSlider
    return QQuickSlider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDialogButtonBox)
  @overload(NoneType)
  def setButtonBox(self, buttonBox: Optional[QQuickDialogButtonBox]) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    *buttonBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#setButtonBox

    Parameters
    ----------

    buttonBox : Optional[QQuickDialogButtonBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    #      *buttonBox)
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached12setButtonBoxEP21QQuickDi'
        'alogButtonBox',
        self._addressOf(buttonBox),
    )

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def setEyeDropperButton(
      self,
      eyeDropperButton: Optional[QQuickAbstractButton],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplAttached::setEyeDropperButton(QQuickAbstractButton
    *eyeDropperButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html

    Parameters
    ----------

    eyeDropperButton : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialogImplAttached::setEyeDropperButton(
    #      QQuickAbstractButton *eyeDropperButton)
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached19setEyeDropperButtonEP20Q'
        'QuickAbstractButton',
        self._addressOf(eyeDropperButton),
    )

  @overload(QQuickAbstractColorPicker)
  @overload(NoneType)
  def setColorPicker(
      self,
      colorPicker: Optional[QQuickAbstractColorPicker],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplAttached::setColorPicker(QQuickAbstractColorPicker
    *colorPicker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#setColorPicker

    Parameters
    ----------

    colorPicker : Optional[QQuickAbstractColorPicker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialogImplAttached::setColorPicker(
    #      QQuickAbstractColorPicker *colorPicker)
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached14setColorPickerEP25QQuick'
        'AbstractColorPicker',
        self._addressOf(colorPicker),
    )

  @overload(QQuickColorInputs)
  @overload(NoneType)
  def setColorInputs(self, colorInputs: Optional[QQuickColorInputs]) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplAttached::setColorInputs(QQuickColorInputs
    *colorInputs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#setColorInputs

    Parameters
    ----------

    colorInputs : Optional[QQuickColorInputs]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialogImplAttached::setColorInputs(QQuickColorInputs
    #      *colorInputs)
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached14setColorInputsEP17QQuick'
        'ColorInputs',
        self._addressOf(colorInputs),
    )

  @overload(QQuickSlider)
  @overload(NoneType)
  def setAlphaSlider(self, alphaSlider: Optional[QQuickSlider]) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplAttached::setAlphaSlider(QQuickSlider
    *alphaSlider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#setAlphaSlider

    Parameters
    ----------

    alphaSlider : Optional[QQuickSlider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialogImplAttached::setAlphaSlider(QQuickSlider
    #      *alphaSlider)
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached14setAlphaSliderEP12QQuick'
        'Slider',
        self._addressOf(alphaSlider),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickColorDialogImplAttached::QQuickColorDialogImplAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorDialogImplAttached::QQuickColorDialogImplAttached(QObject
    #      *parent)
    self._noteCreation(QQuickColorDialogImplAttached, lambda: Rituals.call(
        'ritual_ZN29QQuickColorDialogImplAttachedC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def buttonBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplAttached::buttonBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html
    """
    #  void QQuickColorDialogImplAttached::buttonBoxChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached16buttonBoxChangedEv',
    )

  def eyeDropperButtonChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialogImplAttached::eyeDropperButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html
    """
    #  void QQuickColorDialogImplAttached::eyeDropperButtonChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached23eyeDropperButtonChangedE'
        'v',
    )

  def colorPickerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplAttached::colorPickerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html
    """
    #  void QQuickColorDialogImplAttached::colorPickerChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached18colorPickerChangedEv',
    )

  def colorInputsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplAttached::colorInputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html
    """
    #  void QQuickColorDialogImplAttached::colorInputsChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached18colorInputsChangedEv',
    )

  def alphaSliderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialogImplAttached::alphaSliderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html
    """
    #  void QQuickColorDialogImplAttached::alphaSliderChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached18alphaSliderChangedEv',
    )

  def d_func(self) -> Optional[QQuickColorDialogImplAttachedPrivate]:
    """
    Calls Qt's 'QQuickColorDialogImplAttachedPrivate
    *QQuickColorDialogImplAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialogimplattached.html#d_func

    Returns
    -------

    Optional[QQuickColorDialogImplAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImplAttachedPrivate
    #      *QQuickColorDialogImplAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN29QQuickColorDialogImplAttached6d_funcEv',
    )
    from . import QQuickColorDialogImplAttachedPrivate
    return QQuickColorDialogImplAttachedPrivate._cuteAt(address)
