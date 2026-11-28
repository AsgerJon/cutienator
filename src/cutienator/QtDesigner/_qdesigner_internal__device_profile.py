"""
qdesigner_internal::DeviceProfile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/deviceprofile_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::DeviceProfile to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
  from ..QtWidgets import QWidget
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QString = WAIT['QString']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeviceProfile(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::DeviceProfile: a plain Python
  object standing in front of one C++ qdesigner_internal::DeviceProfile.

  C++ hands a qdesigner_internal::DeviceProfile around as a copy, so every
  C++ qdesigner_internal::DeviceProfile behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DeviceProfile that has a ritual
  and that Python can call so far, 22 names in all: 'clear', 'name',
  'setName', 'isEmpty', 'fontFamily', 'setFontFamily', 'fontPointSize',
  'setFontPointSize', 'dpiX', 'setDpiX', 'dpiY', 'setDpiY', 'style',
  'setStyle', 'fromSystem', 'apply', 'applyDPI', 'toString', 'toXml',
  'fromXml', '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DeviceProfile &qdesigner_internal::DeviceProfile::operator=(const
    DeviceProfile &a0)': assignment: Python binds a name and has no operator
    for it.
  - Qt's 'qdesigner_internal::DeviceProfile::~DeviceProfile()': the
    destructor: Python removes its C++ qdesigner_internal::DeviceProfile by
    it, and has no other use for it.
  - Qt's 'void qdesigner_internal::DeviceProfile::systemResolution(int *dpiX,
    int *dpiY)': takes a number to change where it is.
  - Qt's 'void qdesigner_internal::DeviceProfile::widgetResolution(const
    QWidget *w, int *dpiX, int *dpiY)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ qdesigner_internal::DeviceProfile is created at the first use,
    not by 'qdesigner_internal::DeviceProfile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::DeviceProfile back gives a copy
    the ritual made for Python, in a new cute
    qdesigner_internal::DeviceProfile.
  - Each name of Qt's qdesigner_internal::DeviceProfile that has no cute
    function yet, 'systemResolution', 'widgetResolution', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::DeviceProfile, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ApplyMode(CuteNum):
    """
    The enum 'qdesigner_internal::DeviceProfile::ApplyMode' of Qt, with the 2
    names Qt gives in it.
    """

    ApplyFormParent = Kee[int](0)
    ApplyPreview = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int, QWidget)
  @overload(int, int, NoneType)
  def applyDPI(dpiX: int, dpiY: int, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::applyDPI(int dpiX,
    int dpiY, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#applyDPI

    Parameters
    ----------

    dpiX : int
      Passed on as it is.

    dpiY : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::DeviceProfile::applyDPI(int dpiX, int dpiY,
    #      QWidget *widget)
    Rituals.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile8applyDPIEiiP7QWidget',
        dpiX, dpiY, CuteMixin._addressOf(widget),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DeviceProfile'

  #  Qt's '~qdesigner_internal::DeviceProfile()'. Naming it makes this a
  #  value class: Python owns every C++ qdesigner_internal::DeviceProfile
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal13DeviceProfileD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::DeviceProfile::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DeviceProfile::name() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile4nameEv',
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::DeviceProfile::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#isEmpty
    """
    #  bool qdesigner_internal::DeviceProfile::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile7isEmptyEv',
    )

  def fontFamily(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::DeviceProfile::fontFamily()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#fontFamily

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DeviceProfile::fontFamily() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile10fontFamilyEv',
    )

  def fontPointSize(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::DeviceProfile::fontPointSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html
    """
    #  int qdesigner_internal::DeviceProfile::fontPointSize() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile13fontPointSizeEv',
    )

  def dpiX(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::DeviceProfile::dpiX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#dpiX
    """
    #  int qdesigner_internal::DeviceProfile::dpiX() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile4dpiXEv',
    )

  def dpiY(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::DeviceProfile::dpiY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#dpiY
    """
    #  int qdesigner_internal::DeviceProfile::dpiY() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile4dpiYEv',
    )

  def style(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::DeviceProfile::style() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#style

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DeviceProfile::style() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile5styleEv',
    )

  def toString(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::DeviceProfile::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DeviceProfile::toString() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile8toStringEv',
    )

  def toXml(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::DeviceProfile::toXml() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#toXml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DeviceProfile::toXml() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile5toXmlEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, a0: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::setName(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#setName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::DeviceProfile::setName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile7setNameERK7QString',
        a0,
    )

  @overload(str)
  def setFontFamily(self, a0: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::setFontFamily(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::DeviceProfile::setFontFamily(const QString
    #      &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile13setFontFamilyERK7QSt'
        'ring',
        a0,
    )

  @overload(int)
  def setFontPointSize(self, p: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::setFontPointSize(int
    p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html

    Parameters
    ----------

    p : int
      Passed on as it is.
    """
    #  void qdesigner_internal::DeviceProfile::setFontPointSize(int p)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile16setFontPointSizeEi',
        p,
    )

  @overload(int)
  def setDpiX(self, d: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::setDpiX(int d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#setDpiX

    Parameters
    ----------

    d : int
      Passed on as it is.
    """
    #  void qdesigner_internal::DeviceProfile::setDpiX(int d)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile7setDpiXEi', d,
    )

  @overload(int)
  def setDpiY(self, d: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::setDpiY(int d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#setDpiY

    Parameters
    ----------

    d : int
      Passed on as it is.
    """
    #  void qdesigner_internal::DeviceProfile::setDpiY(int d)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile7setDpiYEi', d,
    )

  @overload(str)
  def setStyle(self, a0: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::setStyle(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#setStyle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::DeviceProfile::setStyle(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile8setStyleERK7QString',
        a0,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: DeviceProfile) -> bool:
    """
    Calls Qt's 'bool operator==(const DeviceProfile &lhs, const DeviceProfile
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#operator==

    Parameters
    ----------

    rhs : DeviceProfile
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DeviceProfile, which stays Python's own.
    """
    #  bool operator==(const DeviceProfile &lhs, const DeviceProfile &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_13DeviceProfileES2_',
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

  @overload(THIS)
  def __ne__(self, rhs: DeviceProfile) -> bool:
    """
    Calls Qt's 'bool operator!=(const DeviceProfile &lhs, const DeviceProfile
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#operator!=

    Parameters
    ----------

    rhs : DeviceProfile
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DeviceProfile, which stays Python's own.
    """
    #  bool operator!=(const DeviceProfile &lhs, const DeviceProfile &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_13DeviceProfileES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    'qdesigner_internal::DeviceProfile::DeviceProfile()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html
    """
    #  qdesigner_internal::DeviceProfile::DeviceProfile()
    self._noteCreation(DeviceProfile, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal13DeviceProfileC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: DeviceProfile) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DeviceProfile::DeviceProfile(const DeviceProfile
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html

    Parameters
    ----------

    a0 : DeviceProfile
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DeviceProfile, which stays Python's own.
    """
    #  qdesigner_internal::DeviceProfile::DeviceProfile(const DeviceProfile
    #      &a0)
    self._noteCreation(DeviceProfile, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal13DeviceProfileC1ERKS0_',
        self._valueOf(a0),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#clear
    """
    #  void qdesigner_internal::DeviceProfile::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile5clearEv',
    )

  def fromSystem(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::fromSystem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#fromSystem
    """
    #  void qdesigner_internal::DeviceProfile::fromSystem()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile10fromSystemEv',
    )

  @overload(QDesignerFormEditorInterface, QWidget, ApplyMode)
  @overload(QDesignerFormEditorInterface, NoneType, ApplyMode)
  @overload(NoneType, QWidget, ApplyMode)
  @overload(NoneType, NoneType, ApplyMode)
  def apply(
      self,
      core: Optional[QDesignerFormEditorInterface],
      widget: Optional[QWidget],
      am: ApplyMode,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeviceProfile::apply(const
    QDesignerFormEditorInterface *core, QWidget *widget, ApplyMode am)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#apply

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    am : ApplyMode
      Passed on as its number.
    """
    #  void qdesigner_internal::DeviceProfile::apply(const
    #      QDesignerFormEditorInterface *core, QWidget *widget, ApplyMode am)
    #      const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13DeviceProfile5applyEPK28QDesignerF'
        'ormEditorInterfaceP7QWidgetNS0_9ApplyModeE',
        self._addressOf(core), self._addressOf(widget), am.value,
    )

  @overload(str, QString)
  @overload(str, NoneType)
  def fromXml(self, xml: str, errorMessage: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::DeviceProfile::fromXml(const QString
    &xml, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deviceprofile.html#fromXml

    Parameters
    ----------

    xml : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::DeviceProfile::fromXml(const QString &xml,
    #      QString *errorMessage)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal13DeviceProfile7fromXmlERK7QStringPS1'
        '_',
        xml, self._addressOf(errorMessage),
    )

  @staticmethod
  def systemResolution(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::DeviceProfile::systemResolution(int *dpiX,
    int *dpiY)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DeviceProfile.systemResolution' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::DeviceProfile::systemResolution(int *dpiX, int "
        "*dpiY)': takes a number to change where it is.")

  @staticmethod
  def widgetResolution(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::DeviceProfile::widgetResolution(const
    QWidget *w, int *dpiX, int *dpiY)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DeviceProfile.widgetResolution' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::DeviceProfile::widgetResolution(const QWidget "
        "*w, int *dpiX, int *dpiY)': takes a number to change where it is.")
