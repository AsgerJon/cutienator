"""
QGnomePortalInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgnomeportalinterface_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGnomePortalInterface to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QDBusListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGnomePortalInterface(QObject):
  """
  The cute side of Qt's QGnomePortalInterface: a plain Python object standing
  in front of one C++ QGnomePortalInterface.

  It is built on the cute 'QObject', as Qt's QGnomePortalInterface is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGnomePortalInterface that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'colorScheme',
  'contrastPreference', 'motionPreference', 'querySettings',
  'updateColorScheme', 'updateContrast', 'updateMotion',
  'colorSchemeChanged', 'contrastChanged', 'motionChanged',
  'themeNameChanged', 'dbusSettingChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGnomePortalInterface::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGnomePortalInterface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGnomePortalInterface::~QGnomePortalInterface()': the destructor:
    Python never removes a C++ QGnomePortalInterface.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGnomePortalInterface is created at the first use, not by
    'QGnomePortalInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGnomePortalInterface.
  - Qt tells when it has removed the C++ QGnomePortalInterface. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGnomePortalInterface::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgnomeportalinterface.html#tr

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
    #  QString QGnomePortalInterface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QGnomePortalInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGnomePortalInterface'

  #  A C++ QGnomePortalInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGnomePortalInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGnomePortalInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGnomePortalInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QGnomePortalInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(Qt.ColorScheme)
  def colorScheme(
      self,
      fallback: Qt.ColorScheme = Qt.ColorScheme.Unknown,
  ) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme
    QGnomePortalInterface::colorScheme(Qt::ColorScheme fallback) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#colorScheme

    Parameters
    ----------

    fallback : Qt.ColorScheme
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ColorScheme.Unknown.

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QGnomePortalInterface::colorScheme(Qt::ColorScheme
    #      fallback) const
    return Qt.ColorScheme(self.uglySide.call(
        'ritual_ZNK21QGnomePortalInterface11colorSchemeEN2Qt11ColorSchemeE',
        fallback.value,
    ))

  @overload()
  @overload(Qt.ContrastPreference)
  def contrastPreference(
      self,
      fallback: Qt.ContrastPreference = Qt.ContrastPreference.NoPreference,
  ) -> Qt.ContrastPreference:
    """
    Calls Qt's 'Qt::ContrastPreference
    QGnomePortalInterface::contrastPreference(Qt::ContrastPreference
    fallback) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#contrastPreference

    Parameters
    ----------

    fallback : Qt.ContrastPreference
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ContrastPreference.NoPreference.

    Returns
    -------

    Qt.ContrastPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ContrastPreference(number)' gives.
    """
    #  Qt::ContrastPreference
    #      QGnomePortalInterface::contrastPreference(Qt::ContrastPreference
    #      fallback) const
    return Qt.ContrastPreference(self.uglySide.call(
        'ritual_ZNK21QGnomePortalInterface18contrastPreferenceEN2Qt18Contra'
        'stPreferenceE',
        fallback.value,
    ))

  @overload()
  @overload(Qt.MotionPreference)
  def motionPreference(
      self,
      fallback: Qt.MotionPreference = Qt.MotionPreference.NoPreference,
  ) -> Qt.MotionPreference:
    """
    Calls Qt's 'Qt::MotionPreference
    QGnomePortalInterface::motionPreference(Qt::MotionPreference fallback)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#motionPreference

    Parameters
    ----------

    fallback : Qt.MotionPreference
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MotionPreference.NoPreference.

    Returns
    -------

    Qt.MotionPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MotionPreference(number)' gives.
    """
    #  Qt::MotionPreference
    #      QGnomePortalInterface::motionPreference(Qt::MotionPreference
    #      fallback) const
    return Qt.MotionPreference(self.uglySide.call(
        'ritual_ZNK21QGnomePortalInterface16motionPreferenceEN2Qt16MotionPr'
        'eferenceE',
        fallback.value,
    ))

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGnomePortalInterface::QGnomePortalInterface(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#QGnomePortalInterface

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGnomePortalInterface::QGnomePortalInterface(QObject *parent)
    self._noteCreation(QGnomePortalInterface, lambda: Rituals.call(
        'ritual_ZN21QGnomePortalInterfaceC1EP7QObject',
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

  def querySettings(self) -> None:
    """
    Calls Qt's 'void QGnomePortalInterface::querySettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#querySettings
    """
    #  void QGnomePortalInterface::querySettings()
    self.uglySide.call('ritual_ZN21QGnomePortalInterface13querySettingsEv')

  @overload(Qt.ColorScheme)
  def updateColorScheme(self, colorScheme: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void QGnomePortalInterface::updateColorScheme(Qt::ColorScheme
    colorScheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#updateColorScheme

    Parameters
    ----------

    colorScheme : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QGnomePortalInterface::updateColorScheme(Qt::ColorScheme
    #      colorScheme)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface17updateColorSchemeEN2Qt11ColorSch'
        'emeE',
        colorScheme.value,
    )

  @overload(Qt.ContrastPreference)
  def updateContrast(self, contrast: Qt.ContrastPreference) -> None:
    """
    Calls Qt's 'void
    QGnomePortalInterface::updateContrast(Qt::ContrastPreference contrast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#updateContrast

    Parameters
    ----------

    contrast : Qt.ContrastPreference
      Passed on as its number.
    """
    #  void QGnomePortalInterface::updateContrast(Qt::ContrastPreference
    #      contrast)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface14updateContrastEN2Qt18ContrastPre'
        'ferenceE',
        contrast.value,
    )

  @overload(Qt.MotionPreference)
  def updateMotion(self, motion: Qt.MotionPreference) -> None:
    """
    Calls Qt's 'void QGnomePortalInterface::updateMotion(Qt::MotionPreference
    motion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#updateMotion

    Parameters
    ----------

    motion : Qt.MotionPreference
      Passed on as its number.
    """
    #  void QGnomePortalInterface::updateMotion(Qt::MotionPreference motion)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface12updateMotionEN2Qt16MotionPrefere'
        'nceE',
        motion.value,
    )

  @overload(Qt.ColorScheme)
  def colorSchemeChanged(self, a0: Qt.ColorScheme) -> None:
    """
    Calls Qt's 'void
    QGnomePortalInterface::colorSchemeChanged(Qt::ColorScheme a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#colorSchemeChanged

    Parameters
    ----------

    a0 : Qt.ColorScheme
      Passed on as its number.
    """
    #  void QGnomePortalInterface::colorSchemeChanged(Qt::ColorScheme a0)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface18colorSchemeChangedEN2Qt11ColorSc'
        'hemeE',
        a0.value,
    )

  @overload(Qt.ContrastPreference)
  def contrastChanged(self, a0: Qt.ContrastPreference) -> None:
    """
    Calls Qt's 'void
    QGnomePortalInterface::contrastChanged(Qt::ContrastPreference a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#contrastChanged

    Parameters
    ----------

    a0 : Qt.ContrastPreference
      Passed on as its number.
    """
    #  void QGnomePortalInterface::contrastChanged(Qt::ContrastPreference a0)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface15contrastChangedEN2Qt18ContrastPr'
        'eferenceE',
        a0.value,
    )

  @overload(Qt.MotionPreference)
  def motionChanged(self, a0: Qt.MotionPreference) -> None:
    """
    Calls Qt's 'void
    QGnomePortalInterface::motionChanged(Qt::MotionPreference a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#motionChanged

    Parameters
    ----------

    a0 : Qt.MotionPreference
      Passed on as its number.
    """
    #  void QGnomePortalInterface::motionChanged(Qt::MotionPreference a0)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface13motionChangedEN2Qt16MotionPrefer'
        'enceE',
        a0.value,
    )

  @overload(str)
  def themeNameChanged(self, themeName: str) -> None:
    """
    Calls Qt's 'void QGnomePortalInterface::themeNameChanged(const QString
    &themeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#themeNameChanged

    Parameters
    ----------

    themeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGnomePortalInterface::themeNameChanged(const QString &themeName)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface16themeNameChangedERK7QString',
        themeName,
    )

  @overload(QDBusListener.Provider, QDBusListener.Setting, QVariant)
  def dbusSettingChanged(
      self,
      a0: QDBusListener.Provider,
      a1: QDBusListener.Setting,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QGnomePortalInterface::dbusSettingChanged(QDBusListener::Provider a0,
    QDBusListener::Setting a1, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgnomeportalinterface.html#dbusSettingChanged

    Parameters
    ----------

    a0 : QDBusListener.Provider
      Passed on as its number.

    a1 : QDBusListener.Setting
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QGnomePortalInterface::dbusSettingChanged(QDBusListener::Provider
    #      a0, QDBusListener::Setting a1, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN21QGnomePortalInterface18dbusSettingChangedEN13QDBusListe'
        'ner8ProviderENS0_7SettingERK8QVariant',
        a0.value, a1.value, self._valueOf(value),
    )
