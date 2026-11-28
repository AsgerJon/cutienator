"""
QQuickLabsPlatformIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformicon_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformIcon to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QQuickLabsPlatformIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformIcon: a plain Python object
  standing in front of one C++ QQuickLabsPlatformIcon.

  C++ hands a QQuickLabsPlatformIcon around as a copy, so every C++
  QQuickLabsPlatformIcon behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformIcon that has a ritual and that
  Python can call so far, 8 names in all: 'source', 'setSource', 'name',
  'setName', 'isMask', 'setMask', '__eq__', '__ne__'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickLabsPlatformIcon::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQuickLabsPlatformIcon::~QQuickLabsPlatformIcon()': the destructor:
    Python removes its C++ QQuickLabsPlatformIcon by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformIcon is created at the first use, not by
    'QQuickLabsPlatformIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickLabsPlatformIcon back gives a copy the ritual
    made for Python, in a new cute QQuickLabsPlatformIcon.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformIcon'

  #  Qt's '~QQuickLabsPlatformIcon()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickLabsPlatformIcon behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QQuickLabsPlatformIconD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformIcon::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformicon.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformIcon::source() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformIcon6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformIcon::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformicon.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformIcon::name() const
    return self.uglySide.call('ritual_ZNK22QQuickLabsPlatformIcon4nameEv')

  def isMask(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformIcon::isMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabsplatformicon.html#isMask
    """
    #  bool QQuickLabsPlatformIcon::isMask() const
    return self.uglySide.call('ritual_ZNK22QQuickLabsPlatformIcon6isMaskEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformIcon::setSource(const QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformicon.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickLabsPlatformIcon::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformIcon9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformIcon::setName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformicon.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickLabsPlatformIcon::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN22QQuickLabsPlatformIcon7setNameERK7QString', name,
    )

  @overload(bool)
  def setMask(self, mask: bool) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformIcon::setMask(bool mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformicon.html#setMask

    Parameters
    ----------

    mask : bool
      Passed on as it is.
    """
    #  void QQuickLabsPlatformIcon::setMask(bool mask)
    self.uglySide.call('ritual_ZN22QQuickLabsPlatformIcon7setMaskEb', mask)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QQuickLabsPlatformIcon) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformIcon::operator==(const
    QQuickLabsPlatformIcon &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformicon.html#operator==

    Parameters
    ----------

    other : QQuickLabsPlatformIcon
      Passed on as a value: Qt reads the C++ QQuickLabsPlatformIcon, which
      stays Python's own.
    """
    #  bool QQuickLabsPlatformIcon::operator==(const QQuickLabsPlatformIcon
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformIconeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QQuickLabsPlatformIcon) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformIcon::operator!=(const
    QQuickLabsPlatformIcon &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformicon.html#operator!=

    Parameters
    ----------

    other : QQuickLabsPlatformIcon
      Passed on as a value: Qt reads the C++ QQuickLabsPlatformIcon, which
      stays Python's own.
    """
    #  bool QQuickLabsPlatformIcon::operator!=(const QQuickLabsPlatformIcon
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickLabsPlatformIconneERKS_', self._valueOf(other),
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
