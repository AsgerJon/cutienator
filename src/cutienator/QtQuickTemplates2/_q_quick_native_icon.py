"""
QQuickNativeIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativeicon_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickNativeIcon to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QQuickNativeIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickNativeIcon: a plain Python object standing in
  front of one C++ QQuickNativeIcon.

  C++ hands a QQuickNativeIcon around as a copy, so every C++
  QQuickNativeIcon behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickNativeIcon that has a ritual and that Python
  can call so far, 8 names in all: 'source', 'setSource', 'name', 'setName',
  'isMask', 'setMask', '__eq__', '__ne__'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickNativeIcon::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickNativeIcon::~QQuickNativeIcon()': the destructor: Python
    removes its C++ QQuickNativeIcon by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickNativeIcon is created at the first use, not by
    'QQuickNativeIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickNativeIcon back gives a copy the ritual made
    for Python, in a new cute QQuickNativeIcon.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickNativeIcon'

  #  Qt's '~QQuickNativeIcon()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickNativeIcon behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQuickNativeIconD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickNativeIcon::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickNativeIcon::source() const
    address = self.uglySide.call('ritual_ZNK16QQuickNativeIcon6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickNativeIcon::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickNativeIcon::name() const
    return self.uglySide.call('ritual_ZNK16QQuickNativeIcon4nameEv')

  def isMask(self) -> bool:
    """
    Calls Qt's 'bool QQuickNativeIcon::isMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#isMask
    """
    #  bool QQuickNativeIcon::isMask() const
    return self.uglySide.call('ritual_ZNK16QQuickNativeIcon6isMaskEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickNativeIcon::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickNativeIcon::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN16QQuickNativeIcon9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickNativeIcon::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickNativeIcon::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN16QQuickNativeIcon7setNameERK7QString', name,
    )

  @overload(bool)
  def setMask(self, mask: bool) -> None:
    """
    Calls Qt's 'void QQuickNativeIcon::setMask(bool mask)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#setMask

    Parameters
    ----------

    mask : bool
      Passed on as it is.
    """
    #  void QQuickNativeIcon::setMask(bool mask)
    self.uglySide.call('ritual_ZN16QQuickNativeIcon7setMaskEb', mask)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QQuickNativeIcon) -> bool:
    """
    Calls Qt's 'bool QQuickNativeIcon::operator==(const QQuickNativeIcon
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#operator==

    Parameters
    ----------

    other : QQuickNativeIcon
      Passed on as a value: Qt reads the C++ QQuickNativeIcon, which stays
      Python's own.
    """
    #  bool QQuickNativeIcon::operator==(const QQuickNativeIcon &other) const
    return self.uglySide.call(
        'ritual_ZNK16QQuickNativeIconeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QQuickNativeIcon) -> bool:
    """
    Calls Qt's 'bool QQuickNativeIcon::operator!=(const QQuickNativeIcon
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeicon.html#operator!=

    Parameters
    ----------

    other : QQuickNativeIcon
      Passed on as a value: Qt reads the C++ QQuickNativeIcon, which stays
      Python's own.
    """
    #  bool QQuickNativeIcon::operator!=(const QQuickNativeIcon &other) const
    return self.uglySide.call(
        'ritual_ZNK16QQuickNativeIconneERKS_', self._valueOf(other),
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
