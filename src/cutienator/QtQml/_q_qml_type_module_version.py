"""
QQmlTypeModuleVersion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypemoduleversion_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlTypeModuleVersion to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision
  from . import QQmlTypeModule
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlTypeModule = WAIT['QQmlTypeModule']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeModuleVersion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeModuleVersion: a plain Python object standing
  in front of one C++ QQmlTypeModuleVersion.

  C++ hands a QQmlTypeModuleVersion around as a copy, so every C++
  QQmlTypeModuleVersion behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlTypeModuleVersion yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeModuleVersion &QQmlTypeModuleVersion::operator=(const
    QQmlTypeModuleVersion &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQmlTypeModuleVersion::~QQmlTypeModuleVersion()': the destructor:
    Python removes its C++ QQmlTypeModuleVersion by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlTypeModuleVersion is created at the first use, not by
    'QQmlTypeModuleVersion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTypeModuleVersion back gives a copy the ritual
    made for Python, in a new cute QQmlTypeModuleVersion.
  - Each name of Qt's QQmlTypeModuleVersion that has no cute function yet,
    'type', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQmlTypeModuleVersion'

  #  Qt's '~QQmlTypeModuleVersion()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlTypeModuleVersion behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQmlTypeModuleVersionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeModuleVersion::QQmlTypeModuleVersion()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypemoduleversion.html#QQmlTypeModuleVersion
    """
    #  QQmlTypeModuleVersion::QQmlTypeModuleVersion()
    self._noteCreation(QQmlTypeModuleVersion, lambda: Rituals.call(
        'ritual_ZN21QQmlTypeModuleVersionC1Ev',
    ))

  @overload(QQmlTypeModule, QTypeRevision)
  @overload(NoneType, QTypeRevision)
  def __init__(
      self,
      a0: Optional[QQmlTypeModule],
      a1: QTypeRevision,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeModuleVersion::QQmlTypeModuleVersion(QQmlTypeModule *a0,
    QTypeRevision a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypemoduleversion.html#QQmlTypeModuleVersion

    Parameters
    ----------

    a0 : Optional[QQmlTypeModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  QQmlTypeModuleVersion::QQmlTypeModuleVersion(QQmlTypeModule *a0,
    #      QTypeRevision a1)
    self._noteCreation(QQmlTypeModuleVersion, lambda: Rituals.call(
        'ritual_ZN21QQmlTypeModuleVersionC1EP14QQmlTypeModule13QTypeRevisio'
        'n',
        self._addressOf(a0), self._valueOf(a1),
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlTypeModuleVersion) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeModuleVersion::QQmlTypeModuleVersion(const QQmlTypeModuleVersion
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypemoduleversion.html#QQmlTypeModuleVersion

    Parameters
    ----------

    a0 : QQmlTypeModuleVersion
      Passed on as a value: Qt reads the C++ QQmlTypeModuleVersion, which
      stays Python's own.
    """
    #  QQmlTypeModuleVersion::QQmlTypeModuleVersion(const
    #      QQmlTypeModuleVersion &a0)
    self._noteCreation(QQmlTypeModuleVersion, lambda: Rituals.call(
        'ritual_ZN21QQmlTypeModuleVersionC1ERKS_', self._valueOf(a0),
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
  def type(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeModuleVersion::type': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypeModuleVersion.type' has no cute function yet. Qt's "
        "'QQmlTypeModuleVersion::type': a template: a pattern and no single "
        "function.")
