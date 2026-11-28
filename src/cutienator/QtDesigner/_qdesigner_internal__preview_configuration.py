"""
qdesigner_internal::PreviewConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PreviewConfiguration to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDesignerSettingsInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerSettingsInterface = WAIT['QDesignerSettingsInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PreviewConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::PreviewConfiguration: a plain
  Python object standing in front of one C++
  qdesigner_internal::PreviewConfiguration.

  C++ hands a qdesigner_internal::PreviewConfiguration around as a copy, so
  every C++ qdesigner_internal::PreviewConfiguration behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PreviewConfiguration that has a
  ritual and that Python can call so far, 15 names in all: 'style',
  'setStyle', 'applicationStyleSheet', 'setApplicationStyleSheet',
  'deviceSkin', 'setDeviceSkin', 'clear', 'toSettings', 'fromSettings',
  '__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'PreviewConfiguration
    &qdesigner_internal::PreviewConfiguration::operator=(const
    PreviewConfiguration &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'qdesigner_internal::PreviewConfiguration::~PreviewConfiguration()':
    the destructor: Python removes its C++
    qdesigner_internal::PreviewConfiguration by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PreviewConfiguration is created at the first
    use, not by 'qdesigner_internal::PreviewConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PreviewConfiguration back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::PreviewConfiguration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PreviewConfiguration'

  #  Qt's '~qdesigner_internal::PreviewConfiguration()'. Naming it makes this
  #  a value class: Python owns every C++
  #  qdesigner_internal::PreviewConfiguration behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal20PreviewConfigurationD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def style(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::PreviewConfiguration::style()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html#style

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PreviewConfiguration::style() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20PreviewConfiguration5styleEv',
    )

  def applicationStyleSheet(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::PreviewConfiguration::applicationStyleSheet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::PreviewConfiguration::applicationStyleSheet()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20PreviewConfiguration21applicationS'
        'tyleSheetEv',
    )

  def deviceSkin(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::PreviewConfiguration::deviceSkin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PreviewConfiguration::deviceSkin() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20PreviewConfiguration10deviceSkinEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStyle(self, a0: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PreviewConfiguration::setStyle(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PreviewConfiguration::setStyle(const QString
    #      &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20PreviewConfiguration8setStyleERK7QS'
        'tring',
        a0,
    )

  @overload(str)
  def setApplicationStyleSheet(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewConfiguration::setApplicationStyleSheet(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PreviewConfiguration::
    #      setApplicationStyleSheet(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20PreviewConfiguration24setApplicatio'
        'nStyleSheetERK7QString',
        a0,
    )

  @overload(str)
  def setDeviceSkin(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewConfiguration::setDeviceSkin(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PreviewConfiguration::setDeviceSkin(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20PreviewConfiguration13setDeviceSkin'
        'ERK7QString',
        a0,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PreviewConfiguration) -> bool:
    """
    Calls Qt's 'bool operator==(const PreviewConfiguration &lhs, const
    PreviewConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    rhs : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  bool operator==(const PreviewConfiguration &lhs, const
    #      PreviewConfiguration &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_20PreviewConfigurationES2_',
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
  def __ne__(self, rhs: PreviewConfiguration) -> bool:
    """
    Calls Qt's 'bool operator!=(const PreviewConfiguration &lhs, const
    PreviewConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    rhs : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  bool operator!=(const PreviewConfiguration &lhs, const
    #      PreviewConfiguration &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_20PreviewConfigurationES2_',
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

  @overload(THIS)
  def __lt__(self, rhs: PreviewConfiguration) -> bool:
    """
    Calls Qt's 'bool operator<(const PreviewConfiguration &lhs, const
    PreviewConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    rhs : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  bool operator<(const PreviewConfiguration &lhs, const
    #      PreviewConfiguration &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalltERKNS_20PreviewConfigurationES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: PreviewConfiguration) -> bool:
    """
    Calls Qt's 'bool operator>(const PreviewConfiguration &lhs, const
    PreviewConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    rhs : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  bool operator>(const PreviewConfiguration &lhs, const
    #      PreviewConfiguration &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalgtERKNS_20PreviewConfigurationES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: PreviewConfiguration) -> bool:
    """
    Calls Qt's 'bool operator<=(const PreviewConfiguration &lhs, const
    PreviewConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    rhs : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  bool operator<=(const PreviewConfiguration &lhs, const
    #      PreviewConfiguration &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalleERKNS_20PreviewConfigurationES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: PreviewConfiguration) -> bool:
    """
    Calls Qt's 'bool operator>=(const PreviewConfiguration &lhs, const
    PreviewConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    rhs : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  bool operator>=(const PreviewConfiguration &lhs, const
    #      PreviewConfiguration &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalgeERKNS_20PreviewConfigurationES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
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
    'qdesigner_internal::PreviewConfiguration::PreviewConfiguration()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html
    """
    #  qdesigner_internal::PreviewConfiguration::PreviewConfiguration()
    self._noteCreation(PreviewConfiguration, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20PreviewConfigurationC1Ev',
    ))

  @overload(str)
  @overload(str, str)
  @overload(str, str, str)
  def __init__(
      self,
      style: str,
      applicationStyleSheet: str = '',
      deviceSkin: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PreviewConfiguration::PreviewConfiguration(const
    QString &style, const QString &applicationStyleSheet, const QString
    &deviceSkin)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    style : str
      Passed on as it is: a QString is made of it for the call.

    applicationStyleSheet : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    deviceSkin : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qdesigner_internal::PreviewConfiguration::PreviewConfiguration(const
    #      QString &style, const QString &applicationStyleSheet, const
    #      QString &deviceSkin)
    self._noteCreation(PreviewConfiguration, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20PreviewConfigurationC1ERK7QStringS3'
        '_S3_',
        style, applicationStyleSheet, deviceSkin,
    ))

  @overload(THIS)
  def __init__(self, a0: PreviewConfiguration) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PreviewConfiguration::PreviewConfiguration(const
    PreviewConfiguration &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    a0 : PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  qdesigner_internal::PreviewConfiguration::PreviewConfiguration(const
    #      PreviewConfiguration &a0)
    self._noteCreation(PreviewConfiguration, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20PreviewConfigurationC1ERKS0_',
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
    Calls Qt's 'void qdesigner_internal::PreviewConfiguration::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html#clear
    """
    #  void qdesigner_internal::PreviewConfiguration::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20PreviewConfiguration5clearEv',
    )

  @overload(str, QDesignerSettingsInterface)
  @overload(str, NoneType)
  def toSettings(
      self,
      prefix: str,
      settings: Optional[QDesignerSettingsInterface],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewConfiguration::toSettings(const QString
    &prefix, QDesignerSettingsInterface *settings) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    settings : Optional[QDesignerSettingsInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PreviewConfiguration::toSettings(const
    #      QString &prefix, QDesignerSettingsInterface *settings) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20PreviewConfiguration10toSettingsER'
        'K7QStringP26QDesignerSettingsInterface',
        prefix, self._addressOf(settings),
    )

  @overload(str, QDesignerSettingsInterface)
  @overload(str, NoneType)
  def fromSettings(
      self,
      prefix: str,
      settings: Optional[QDesignerSettingsInterface],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewConfiguration::fromSettings(const QString
    &prefix, const QDesignerSettingsInterface *settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewconfiguration.html

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    settings : Optional[QDesignerSettingsInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PreviewConfiguration::fromSettings(const
    #      QString &prefix, const QDesignerSettingsInterface *settings)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20PreviewConfiguration12fromSettingsE'
        'RK7QStringPK26QDesignerSettingsInterface',
        prefix, self._addressOf(settings),
    )
