"""
QSslCertificateExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslcertificateextension.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant


class QSslCertificateExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslCertificateExtension: a plain Python object
  standing in front of one C++ QSslCertificateExtension.

  C++ hands a QSslCertificateExtension around as a copy, so every C++
  QSslCertificateExtension behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslCertificateExtension that has a ritual and that
  Python can call so far, 5 names in all: 'oid', 'name', 'value',
  'isCritical', 'isSupported'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslCertificateExtension
    &QSslCertificateExtension::operator=(QSslCertificateExtension &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSslCertificateExtension &QSslCertificateExtension::operator=(const
    QSslCertificateExtension &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QSslCertificateExtension::~QSslCertificateExtension()': the
    destructor: Python removes its C++ QSslCertificateExtension by it, and
    has no other use for it.
  - Qt's 'void QSslCertificateExtension::swap(QSslCertificateExtension
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSslCertificateExtension is created at the first use, not by
    'QSslCertificateExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslCertificateExtension back gives a copy the ritual
    made for Python, in a new cute QSslCertificateExtension.
  - Each name of Qt's QSslCertificateExtension that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QSslCertificateExtension'

  #  Qt's '~QSslCertificateExtension()'. Naming it makes this a value class:
  #  Python owns every C++ QSslCertificateExtension behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSslCertificateExtensionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def oid(self) -> str:
    """
    Calls Qt's 'QString QSslCertificateExtension::oid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificateextension.html#oid

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCertificateExtension::oid() const
    return self.uglySide.call('ritual_ZNK24QSslCertificateExtension3oidEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QSslCertificateExtension::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcertificateextension.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCertificateExtension::name() const
    return self.uglySide.call('ritual_ZNK24QSslCertificateExtension4nameEv')

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSslCertificateExtension::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateextension.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSslCertificateExtension::value() const
    address = self.uglySide.call(
        'ritual_ZNK24QSslCertificateExtension5valueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isCritical(self) -> bool:
    """
    Calls Qt's 'bool QSslCertificateExtension::isCritical() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateextension.html#isCritical
    """
    #  bool QSslCertificateExtension::isCritical() const
    return self.uglySide.call(
        'ritual_ZNK24QSslCertificateExtension10isCriticalEv',
    )

  def isSupported(self) -> bool:
    """
    Calls Qt's 'bool QSslCertificateExtension::isSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateextension.html#isSupported
    """
    #  bool QSslCertificateExtension::isSupported() const
    return self.uglySide.call(
        'ritual_ZNK24QSslCertificateExtension11isSupportedEv',
    )

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
    'QSslCertificateExtension::QSslCertificateExtension()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateextension.html
    """
    #  QSslCertificateExtension::QSslCertificateExtension()
    self._noteCreation(QSslCertificateExtension, lambda: Rituals.call(
        'ritual_ZN24QSslCertificateExtensionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QSslCertificateExtension) -> None:
    """
    Notes what was given, for Qt's
    'QSslCertificateExtension::QSslCertificateExtension(const
    QSslCertificateExtension &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcertificateextension.html

    Parameters
    ----------

    other : QSslCertificateExtension
      Passed on as a value: Qt reads the C++ QSslCertificateExtension, which
      stays Python's own.
    """
    #  QSslCertificateExtension::QSslCertificateExtension(const
    #      QSslCertificateExtension &other)
    self._noteCreation(QSslCertificateExtension, lambda: Rituals.call(
        'ritual_ZN24QSslCertificateExtensionC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslCertificateExtension::swap(QSslCertificateExtension
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslCertificateExtension.swap' has no cute function yet. Qt's "
        "'void QSslCertificateExtension::swap(QSslCertificateExtension "
        "&other)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QSslCertificateExtension>': the list of
#  QSslCertificateExtension, which 'QList[QSslCertificateExtension]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QSslCertificateExtension.
QList.createKind(
    QSslCertificateExtension, 'value',
    make='ritual_list_make_QSslCertificateExtension',
    add='ritual_list_add_QSslCertificateExtension',
    size='ritual_list_size_QSslCertificateExtension',
    at='ritual_list_at_QSslCertificateExtension',
    drop='ritual_list_drop_QSslCertificateExtension',
)
