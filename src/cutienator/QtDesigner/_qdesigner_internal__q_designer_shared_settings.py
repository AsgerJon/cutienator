"""
qdesigner_internal::QDesignerSharedSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/shared_settings_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerSharedSettings to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QDesignerFormEditorInterface, QDesignerSettingsInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerSharedSettings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::QDesignerSharedSettings: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerSharedSettings.

  C++ hands a qdesigner_internal::QDesignerSharedSettings around as a copy,
  so every C++ qdesigner_internal::QDesignerSharedSettings behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerSharedSettings that has
  a ritual and that Python can call so far, 30 names in all: 'defaultGrid',
  'setDefaultGrid', 'formTemplatePaths', 'setFormTemplatePaths',
  'setAdditionalFormTemplatePaths', 'additionalFormTemplatePaths',
  'formTemplate', 'setFormTemplate', 'newFormSize', 'setNewFormSize',
  'customPreviewConfiguration', 'setCustomPreviewConfiguration',
  'isCustomPreviewConfigurationEnabled',
  'setCustomPreviewConfigurationEnabled', 'userDeviceSkins',
  'setUserDeviceSkins', 'zoomEnabled', 'setZoomEnabled', 'zoom', 'setZoom',
  'objectNamingMode', 'setObjectNamingMode', 'currentDeviceProfile',
  'setCurrentDeviceProfileIndex', 'currentDeviceProfileIndex',
  'deviceProfileAt', 'defaultFormTemplatePaths', 'migrateTemplates',
  'settings', 'deviceProfileXml'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DeviceProfileList
    qdesigner_internal::QDesignerSharedSettings::deviceProfiles() const':
    gives a type Python has no way to take yet.
  - Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setDeviceProfiles(const
    DeviceProfileList &dp)': takes a type Python has no way to hand over yet.
  - Qt's
    'qdesigner_internal::QDesignerSharedSettings::~QDesignerSharedSettings(
    )': the destructor: Python removes its C++
    qdesigner_internal::QDesignerSharedSettings by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerSharedSettings is created at the
    first use, not by 'qdesigner_internal::QDesignerSharedSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::QDesignerSharedSettings back
    gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::QDesignerSharedSettings.
  - Each name of Qt's qdesigner_internal::QDesignerSharedSettings that has no
    cute function yet, 'deviceProfiles', 'setDeviceProfiles', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultFormTemplatePaths() -> QStringList:
    """
    Calls Qt's 'const QStringList
    &qdesigner_internal::QDesignerSharedSettings::defaultFormTemplatePaths(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &qdesigner_internal::QDesignerSharedSettings::
    #      defaultFormTemplatePaths()
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings24defaultFor'
        'mTemplatePathsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def migrateTemplates() -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::migrateTemplates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html
    """
    #  void qdesigner_internal::QDesignerSharedSettings::migrateTemplates()
    Rituals.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings16migrateTem'
        'platesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerSharedSettings'

  #  Qt's '~qdesigner_internal::QDesignerSharedSettings()'. Naming it makes
  #  this a value class: Python owns every C++
  #  qdesigner_internal::QDesignerSharedSettings behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal23QDesignerSharedSettingsD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultGrid(self) -> qdesigner_internal.Grid:
    """
    Calls Qt's 'Grid
    qdesigner_internal::QDesignerSharedSettings::defaultGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    qdesigner_internal.Grid
      A new cute qdesigner_internal::Grid around the copy Qt gave back.
      Python owns it.
    """
    #  Grid qdesigner_internal::QDesignerSharedSettings::defaultGrid() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings11defaultGr'
        'idEv',
    )
    return qdesigner_internal.Grid._cuteOwning(address)

  def formTemplatePaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::QDesignerSharedSettings::formTemplatePaths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      qdesigner_internal::QDesignerSharedSettings::formTemplatePaths()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings17formTempl'
        'atePathsEv',
    )
    return QStringList._cuteOwning(address)

  def additionalFormTemplatePaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::QDesignerSharedSettings::additionalFormTemplatePaths(
    ) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::QDesignerSharedSettings::
    #      additionalFormTemplatePaths() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings27additiona'
        'lFormTemplatePathsEv',
    )
    return QStringList._cuteOwning(address)

  def formTemplate(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::QDesignerSharedSettings::formTemplate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::QDesignerSharedSettings::formTemplate()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings12formTempl'
        'ateEv',
    )

  def newFormSize(self) -> QSize:
    """
    Calls Qt's 'QSize
    qdesigner_internal::QDesignerSharedSettings::newFormSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::QDesignerSharedSettings::newFormSize() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings11newFormSi'
        'zeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def customPreviewConfiguration(
      self,
  ) -> qdesigner_internal.PreviewConfiguration:
    """
    Calls Qt's 'PreviewConfiguration
    qdesigner_internal::QDesignerSharedSettings::customPreviewConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    qdesigner_internal.PreviewConfiguration
      A new cute qdesigner_internal::PreviewConfiguration around the copy Qt
      gave back. Python owns it.
    """
    #  PreviewConfiguration qdesigner_internal::QDesignerSharedSettings::
    #      customPreviewConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings26customPre'
        'viewConfigurationEv',
    )
    return qdesigner_internal.PreviewConfiguration._cuteOwning(address)

  def isCustomPreviewConfigurationEnabled(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::QDesignerSharedSettings::
    isCustomPreviewConfigurationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html
    """
    #  bool qdesigner_internal::QDesignerSharedSettings::
    #      isCustomPreviewConfigurationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings35isCustomP'
        'reviewConfigurationEnabledEv',
    )

  def userDeviceSkins(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::QDesignerSharedSettings::userDeviceSkins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      qdesigner_internal::QDesignerSharedSettings::userDeviceSkins()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings15userDevic'
        'eSkinsEv',
    )
    return QStringList._cuteOwning(address)

  def zoomEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerSharedSettings::zoomEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html
    """
    #  bool qdesigner_internal::QDesignerSharedSettings::zoomEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings11zoomEnabl'
        'edEv',
    )

  def zoom(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::QDesignerSharedSettings::zoom()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html
    """
    #  int qdesigner_internal::QDesignerSharedSettings::zoom() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings4zoomEv',
    )

  def objectNamingMode(self) -> qdesigner_internal.ObjectNamingMode:
    """
    Calls Qt's 'ObjectNamingMode
    qdesigner_internal::QDesignerSharedSettings::objectNamingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    qdesigner_internal.ObjectNamingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'qdesigner_internal.ObjectNamingMode(number)' gives.
    """
    #  ObjectNamingMode
    #      qdesigner_internal::QDesignerSharedSettings::objectNamingMode()
    #      const
    return qdesigner_internal.ObjectNamingMode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings16objectNam'
        'ingModeEv',
    ))

  def currentDeviceProfile(self) -> qdesigner_internal.DeviceProfile:
    """
    Calls Qt's 'DeviceProfile
    qdesigner_internal::QDesignerSharedSettings::currentDeviceProfile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    qdesigner_internal.DeviceProfile
      A new cute qdesigner_internal::DeviceProfile around the copy Qt gave
      back. Python owns it.
    """
    #  DeviceProfile
    #      qdesigner_internal::QDesignerSharedSettings::currentDeviceProfile(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings20currentDe'
        'viceProfileEv',
    )
    return qdesigner_internal.DeviceProfile._cuteOwning(address)

  def currentDeviceProfileIndex(self) -> int:
    """
    Calls Qt's 'int
    qdesigner_internal::QDesignerSharedSettings::currentDeviceProfileIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html
    """
    #  int qdesigner_internal::QDesignerSharedSettings::
    #      currentDeviceProfileIndex() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings25currentDe'
        'viceProfileIndexEv',
    )

  @overload(int)
  def deviceProfileAt(self, idx: int) -> qdesigner_internal.DeviceProfile:
    """
    Calls Qt's 'DeviceProfile
    qdesigner_internal::QDesignerSharedSettings::deviceProfileAt(int idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    qdesigner_internal.DeviceProfile
      A new cute qdesigner_internal::DeviceProfile around the copy Qt gave
      back. Python owns it.
    """
    #  DeviceProfile
    #      qdesigner_internal::QDesignerSharedSettings::deviceProfileAt(int
    #      idx) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings15devicePro'
        'fileAtEi',
        idx,
    )
    return qdesigner_internal.DeviceProfile._cuteOwning(address)

  def settings(self) -> Optional[QDesignerSettingsInterface]:
    """
    Calls Qt's 'QDesignerSettingsInterface
    *qdesigner_internal::QDesignerSharedSettings::settings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    Optional[QDesignerSettingsInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerSettingsInterface
    #      *qdesigner_internal::QDesignerSharedSettings::settings() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings8settingsEv',
    )
    from . import QDesignerSettingsInterface
    return QDesignerSettingsInterface._cuteAt(address)

  def deviceProfileXml(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::QDesignerSharedSettings::deviceProfileXml() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      qdesigner_internal::QDesignerSharedSettings::deviceProfileXml()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerSharedSettings16devicePro'
        'fileXmlEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['qdesigner_internal.Grid'])
  def setDefaultGrid(self, grid: qdesigner_internal.Grid) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setDefaultGrid(const Grid
    &grid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    grid : qdesigner_internal.Grid
      Passed on as a value: Qt reads the C++ qdesigner_internal::Grid, which
      stays Python's own.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::setDefaultGrid(const
    #      Grid &grid)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings14setDefault'
        'GridERKNS_4GridE',
        self._valueOf(grid),
    )

  @overload(QStringList)
  def setFormTemplatePaths(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setFormTemplatePaths(const
    QStringList &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void
    #      qdesigner_internal::QDesignerSharedSettings::setFormTemplatePaths(
    #      const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings20setFormTem'
        'platePathsERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(QStringList)
  def setAdditionalFormTemplatePaths(
      self,
      additionalPaths: QStringList,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerSharedSettings::
    setAdditionalFormTemplatePaths(const QStringList &additionalPaths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    additionalPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::
    #      setAdditionalFormTemplatePaths(const QStringList &additionalPaths)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings30setAdditio'
        'nalFormTemplatePathsERK5QListI7QStringE',
        self._valueOf(additionalPaths),
    )

  @overload(str)
  def setFormTemplate(self, t: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setFormTemplate(const
    QString &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    t : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      qdesigner_internal::QDesignerSharedSettings::setFormTemplate(const
    #      QString &t)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings15setFormTem'
        'plateERK7QString',
        t,
    )

  @overload(QSize)
  def setNewFormSize(self, s: QSize) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setNewFormSize(const QSize
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::setNewFormSize(const
    #      QSize &s)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings14setNewForm'
        'SizeERK5QSize',
        self._valueOf(s),
    )

  @overload(WAIT['qdesigner_internal.PreviewConfiguration'])
  def setCustomPreviewConfiguration(
      self,
      configuration: qdesigner_internal.PreviewConfiguration,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerSharedSettings::
    setCustomPreviewConfiguration(const PreviewConfiguration
    &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    configuration : qdesigner_internal.PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::
    #      setCustomPreviewConfiguration(const PreviewConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings29setCustomP'
        'reviewConfigurationERKNS_20PreviewConfigurationE',
        self._valueOf(configuration),
    )

  @overload(bool)
  def setCustomPreviewConfigurationEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerSharedSettings::
    setCustomPreviewConfigurationEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::
    #      setCustomPreviewConfigurationEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings36setCustomP'
        'reviewConfigurationEnabledEb',
        enabled,
    )

  @overload(QStringList)
  def setUserDeviceSkins(self, userDeviceSkins: QStringList) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setUserDeviceSkins(const
    QStringList &userDeviceSkins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    userDeviceSkins : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::setUserDeviceSkins(
    #      const QStringList &userDeviceSkins)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings18setUserDev'
        'iceSkinsERK5QListI7QStringE',
        self._valueOf(userDeviceSkins),
    )

  @overload(bool)
  def setZoomEnabled(self, v: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setZoomEnabled(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::setZoomEnabled(bool
    #      v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings14setZoomEna'
        'bledEb',
        v,
    )

  @overload(int)
  def setZoom(self, z: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerSharedSettings::setZoom(int
    z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    z : int
      Passed on as it is.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::setZoom(int z)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings7setZoomEi',
        z,
    )

  @overload(qdesigner_internal.ObjectNamingMode)
  def setObjectNamingMode(
      self,
      n: qdesigner_internal.ObjectNamingMode,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setObjectNamingMode(
    ObjectNamingMode n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    n : qdesigner_internal.ObjectNamingMode
      Passed on as its number.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::setObjectNamingMode(
    #      ObjectNamingMode n)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings19setObjectN'
        'amingModeENS_16ObjectNamingModeE',
        n.value,
    )

  @overload(int)
  def setCurrentDeviceProfileIndex(self, i: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerSharedSettings::
    setCurrentDeviceProfileIndex(int i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void qdesigner_internal::QDesignerSharedSettings::
    #      setCurrentDeviceProfileIndex(int i)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettings28setCurrent'
        'DeviceProfileIndexEi',
        i,
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def __init__(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerSharedSettings::QDesignerSharedSettings(
    QDesignerFormEditorInterface *core)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignersharedsettings.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::QDesignerSharedSettings::
    #      QDesignerSharedSettings(QDesignerFormEditorInterface *core)
    self._noteCreation(QDesignerSharedSettings, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal23QDesignerSharedSettingsC1EP28QDesig'
        'nerFormEditorInterface',
        self._addressOf(core),
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

  @staticmethod
  def deviceProfiles(*__, **_) -> Never:
    """
    Qt's 'DeviceProfileList
    qdesigner_internal::QDesignerSharedSettings::deviceProfiles() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerSharedSettings.deviceProfiles' has no "
        "cute function yet. Qt's 'DeviceProfileList "
        "qdesigner_internal::QDesignerSharedSettings::deviceProfiles() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setDeviceProfiles(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::QDesignerSharedSettings::setDeviceProfiles(const
    DeviceProfileList &dp)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerSharedSettings.setDeviceProfiles' has "
        "no cute function yet. Qt's 'void "
        "qdesigner_internal::QDesignerSharedSettings::setDeviceProfiles(cons"
        "t DeviceProfileList &dp)': takes a type Python has no way to hand "
        "over yet.")
