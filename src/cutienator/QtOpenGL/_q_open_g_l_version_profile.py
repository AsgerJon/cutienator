"""
QOpenGLVersionProfile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionprofile.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtGui import QSurfaceFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpenGLVersionProfile(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLVersionProfile: a plain Python object standing
  in front of one C++ QOpenGLVersionProfile.

  C++ hands a QOpenGLVersionProfile around as a copy, so every C++
  QOpenGLVersionProfile behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLVersionProfile that has a ritual and that
  Python can call so far, 8 names in all: 'setVersion', 'profile',
  'setProfile', 'hasProfiles', 'isLegacyVersion', 'isValid', '__eq__',
  '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLVersionProfile::~QOpenGLVersionProfile()': the destructor:
    Python removes its C++ QOpenGLVersionProfile by it, and has no other use
    for it.
  - Qt's 'QOpenGLVersionProfile &QOpenGLVersionProfile::operator=(const
    QOpenGLVersionProfile &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'std::pair<int, int> QOpenGLVersionProfile::version() const': gives
    a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpenGLVersionProfile is created at the first use, not by
    'QOpenGLVersionProfile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLVersionProfile back gives a copy the ritual
    made for Python, in a new cute QOpenGLVersionProfile.
  - Each name of Qt's QOpenGLVersionProfile that has no cute function yet,
    'version', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLVersionProfile'

  #  Qt's '~QOpenGLVersionProfile()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLVersionProfile behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QOpenGLVersionProfileD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def profile(self) -> QSurfaceFormat.OpenGLContextProfile:
    """
    Calls Qt's 'QSurfaceFormat::OpenGLContextProfile
    QOpenGLVersionProfile::profile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglversionprofile.html#profile

    Returns
    -------

    QSurfaceFormat.OpenGLContextProfile
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurfaceFormat.OpenGLContextProfile(number)' gives.
    """
    #  QSurfaceFormat::OpenGLContextProfile QOpenGLVersionProfile::profile()
    #      const
    return QSurfaceFormat.OpenGLContextProfile(self.uglySide.call(
        'ritual_ZNK21QOpenGLVersionProfile7profileEv',
    ))

  def hasProfiles(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLVersionProfile::hasProfiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#hasProfiles
    """
    #  bool QOpenGLVersionProfile::hasProfiles() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLVersionProfile11hasProfilesEv',
    )

  def isLegacyVersion(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLVersionProfile::isLegacyVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#isLegacyVersion
    """
    #  bool QOpenGLVersionProfile::isLegacyVersion() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLVersionProfile15isLegacyVersionEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLVersionProfile::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglversionprofile.html#isValid
    """
    #  bool QOpenGLVersionProfile::isValid() const
    return self.uglySide.call('ritual_ZNK21QOpenGLVersionProfile7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setVersion(self, majorVersion: int, minorVersion: int) -> None:
    """
    Calls Qt's 'void QOpenGLVersionProfile::setVersion(int majorVersion, int
    minorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#setVersion

    Parameters
    ----------

    majorVersion : int
      Passed on as it is.

    minorVersion : int
      Passed on as it is.
    """
    #  void QOpenGLVersionProfile::setVersion(int majorVersion, int
    #      minorVersion)
    self.uglySide.call(
        'ritual_ZN21QOpenGLVersionProfile10setVersionEii',
        majorVersion, minorVersion,
    )

  @overload(QSurfaceFormat.OpenGLContextProfile)
  def setProfile(self, profile: QSurfaceFormat.OpenGLContextProfile) -> None:
    """
    Calls Qt's 'void
    QOpenGLVersionProfile::setProfile(QSurfaceFormat::OpenGLContextProfile
    profile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#setProfile

    Parameters
    ----------

    profile : QSurfaceFormat.OpenGLContextProfile
      Passed on as its number.
    """
    #  void QOpenGLVersionProfile::setProfile(QSurfaceFormat::
    #      OpenGLContextProfile profile)
    self.uglySide.call(
        'ritual_ZN21QOpenGLVersionProfile10setProfileEN14QSurfaceFormat20Op'
        'enGLContextProfileE',
        profile.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpenGLVersionProfile) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpenGLVersionProfile &lhs, const
    QOpenGLVersionProfile &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#operator==

    Parameters
    ----------

    rhs : QOpenGLVersionProfile
      Passed on as a value: Qt reads the C++ QOpenGLVersionProfile, which
      stays Python's own.
    """
    #  bool operator==(const QOpenGLVersionProfile &lhs, const
    #      QOpenGLVersionProfile &rhs)
    return Rituals.call(
        'ritual_ZeqRK21QOpenGLVersionProfileS1_',
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
  def __ne__(self, rhs: QOpenGLVersionProfile) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpenGLVersionProfile &lhs, const
    QOpenGLVersionProfile &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#operator!=

    Parameters
    ----------

    rhs : QOpenGLVersionProfile
      Passed on as a value: Qt reads the C++ QOpenGLVersionProfile, which
      stays Python's own.
    """
    #  bool operator!=(const QOpenGLVersionProfile &lhs, const
    #      QOpenGLVersionProfile &rhs)
    return Rituals.call(
        'ritual_ZneRK21QOpenGLVersionProfileS1_',
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
    'QOpenGLVersionProfile::QOpenGLVersionProfile()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#QOpenGLVersionProfile
    """
    #  QOpenGLVersionProfile::QOpenGLVersionProfile()
    self._noteCreation(QOpenGLVersionProfile, lambda: Rituals.call(
        'ritual_ZN21QOpenGLVersionProfileC1Ev',
    ))

  @overload(QSurfaceFormat)
  def __init__(self, format: QSurfaceFormat) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVersionProfile::QOpenGLVersionProfile(const QSurfaceFormat
    &format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#QOpenGLVersionProfile

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  QOpenGLVersionProfile::QOpenGLVersionProfile(const QSurfaceFormat
    #      &format)
    self._noteCreation(QOpenGLVersionProfile, lambda: Rituals.call(
        'ritual_ZN21QOpenGLVersionProfileC1ERK14QSurfaceFormat',
        self._valueOf(format),
    ))

  @overload(THIS)
  def __init__(self, other: QOpenGLVersionProfile) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVersionProfile::QOpenGLVersionProfile(const QOpenGLVersionProfile
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionprofile.html#QOpenGLVersionProfile

    Parameters
    ----------

    other : QOpenGLVersionProfile
      Passed on as a value: Qt reads the C++ QOpenGLVersionProfile, which
      stays Python's own.
    """
    #  QOpenGLVersionProfile::QOpenGLVersionProfile(const
    #      QOpenGLVersionProfile &other)
    self._noteCreation(QOpenGLVersionProfile, lambda: Rituals.call(
        'ritual_ZN21QOpenGLVersionProfileC1ERKS_', self._valueOf(other),
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
  def version(*__, **_) -> Never:
    """
    Qt's 'std::pair<int, int> QOpenGLVersionProfile::version() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLVersionProfile.version' has no cute function yet. Qt's "
        "'std::pair<int, int> QOpenGLVersionProfile::version() const': "
        "gives a type Python has no way to take yet.")
