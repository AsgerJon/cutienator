"""
QSSGRenderPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererutil_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderPath to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSSGRenderPath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderPath: a plain Python object standing in
  front of one C++ QSSGRenderPath.

  C++ hands a QSSGRenderPath around as a copy, so every C++ QSSGRenderPath
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderPath that has a ritual and that Python can
  call so far, 5 names in all: 'isNull', 'isEmpty', 'path', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderPath::~QSSGRenderPath()': the destructor: Python removes
    its C++ QSSGRenderPath by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderPath is created at the first use, not by
    'QSSGRenderPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderPath back gives a copy the ritual made for
    Python, in a new cute QSSGRenderPath.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderPath'

  #  Qt's '~QSSGRenderPath()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGRenderPath behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSSGRenderPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderPath::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#isNull
    """
    #  bool QSSGRenderPath::isNull() const
    return self.uglySide.call('ritual_ZNK14QSSGRenderPath6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderPath::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#isEmpty
    """
    #  bool QSSGRenderPath::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QSSGRenderPath7isEmptyEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QSSGRenderPath::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGRenderPath::path() const
    return self.uglySide.call('ritual_ZNK14QSSGRenderPath4pathEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, p2: QSSGRenderPath) -> bool:
    """
    Calls Qt's 'bool operator==(const QSSGRenderPath &p1, const
    QSSGRenderPath &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#operator==

    Parameters
    ----------

    p2 : QSSGRenderPath
      Passed on as a value: Qt reads the C++ QSSGRenderPath, which stays
      Python's own.
    """
    #  bool operator==(const QSSGRenderPath &p1, const QSSGRenderPath &p2)
    return Rituals.call(
        'ritual_ZeqRK14QSSGRenderPathS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(p2),
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
  def __ne__(self, p2: QSSGRenderPath) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSSGRenderPath &p1, const
    QSSGRenderPath &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#operator!=

    Parameters
    ----------

    p2 : QSSGRenderPath
      Passed on as a value: Qt reads the C++ QSSGRenderPath, which stays
      Python's own.
    """
    #  bool operator!=(const QSSGRenderPath &p1, const QSSGRenderPath &p2)
    return Rituals.call(
        'ritual_ZneRK14QSSGRenderPathS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(p2),
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
    Notes what was given, for Qt's 'QSSGRenderPath::QSSGRenderPath()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#QSSGRenderPath
    """
    #  QSSGRenderPath::QSSGRenderPath()
    self._noteCreation(QSSGRenderPath, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderPathC1Ev',
    ))

  @overload(str)
  @overload(str, str)
  def __init__(self, p: str, lightmapKey: str = '') -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderPath::QSSGRenderPath(const
    QString &p, const QString &lightmapKey)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpath.html#QSSGRenderPath

    Parameters
    ----------

    p : str
      Passed on as it is: a QString is made of it for the call.

    lightmapKey : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSSGRenderPath::QSSGRenderPath(const QString &p, const QString
    #      &lightmapKey)
    self._noteCreation(QSSGRenderPath, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderPathC1ERK7QStringS2_', p, lightmapKey,
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
