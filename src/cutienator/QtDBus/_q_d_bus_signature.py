"""
QDBusSignature binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusSignature(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusSignature: a plain Python object standing in
  front of one C++ QDBusSignature.

  C++ hands a QDBusSignature around as a copy, so every C++ QDBusSignature
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusSignature that has a ritual and that Python can
  call so far, 3 names in all: 'setSignature', 'signature', 'doCheck'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusSignature::QDBusSignature(const QString &signature)': takes in
    Python what 'QDBusSignature::QDBusSignature(const char *signature)'
    takes.
  - Qt's 'QDBusSignature::QDBusSignature(QString &&sig)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QDBusSignature::swap(QDBusSignature &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDBusSignature::~QDBusSignature()': the destructor: Python removes
    its C++ QDBusSignature by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDBusSignature is created at the first use, not by
    'QDBusSignature(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusSignature back gives a copy the ritual made for
    Python, in a new cute QDBusSignature.
  - Each name of Qt's QDBusSignature that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusSignature'

  #  Qt's '~QDBusSignature()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusSignature behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QDBusSignatureD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def signature(self) -> str:
    """
    Calls Qt's 'QString QDBusSignature::signature() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbussignature.html#signature

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusSignature::signature() const
    return self.uglySide.call('ritual_ZNK14QDBusSignature9signatureEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSignature(self, signature: str) -> None:
    """
    Calls Qt's 'void QDBusSignature::setSignature(const QString &signature)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbussignature.html#setSignature

    Parameters
    ----------

    signature : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusSignature::setSignature(const QString &signature)
    self.uglySide.call(
        'ritual_ZN14QDBusSignature12setSignatureERK7QString', signature,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDBusSignature::QDBusSignature()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbussignature.html#QDBusSignature
    """
    #  QDBusSignature::QDBusSignature()
    self._noteCreation(QDBusSignature, lambda: Rituals.call(
        'ritual_ZN14QDBusSignatureC1Ev',
    ))

  @overload(str)
  @overload(NoneType)
  def __init__(self, signature: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QDBusSignature::QDBusSignature(const char
    *signature)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbussignature.html#QDBusSignature

    Parameters
    ----------

    signature : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QDBusSignature::QDBusSignature(const char *signature)
    self._noteCreation(QDBusSignature, lambda: Rituals.call(
        'ritual_ZN14QDBusSignatureC1EPKc', self._bytesOf(signature),
    ))

  @overload(QLatin1String)
  def __init__(self, signature: QLatin1String) -> None:
    """
    Notes what was given, for Qt's
    'QDBusSignature::QDBusSignature(QLatin1StringView signature)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbussignature.html#QDBusSignature

    Parameters
    ----------

    signature : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QDBusSignature::QDBusSignature(QLatin1StringView signature)
    self._noteCreation(QDBusSignature, lambda: Rituals.call(
        'ritual_ZN14QDBusSignatureC1E13QLatin1String',
        self._valueOf(signature),
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

  def doCheck(self) -> None:
    """
    Calls Qt's 'void QDBusSignature::doCheck()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbussignature.html#doCheck
    """
    #  void QDBusSignature::doCheck()
    self.uglySide.call('ritual_ZN14QDBusSignature7doCheckEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusSignature::swap(QDBusSignature &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusSignature.swap' has no cute function yet. Qt's 'void "
        "QDBusSignature::swap(QDBusSignature &other)': takes a type Python "
        "has no way to hand over yet.")
