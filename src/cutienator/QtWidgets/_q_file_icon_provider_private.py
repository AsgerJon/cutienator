"""
QFileIconProviderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfileiconprovider_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QFileIconProviderPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAbstractFileIconProviderPrivate
from . import QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo
  from ..QtGui import QIcon
  from . import QFileIconProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileIconProvider = WAIT['QFileIconProvider']
  QFileInfo = WAIT['QFileInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileIconProviderPrivate(QAbstractFileIconProviderPrivate):
  """
  The cute side of Qt's QFileIconProviderPrivate: a plain Python object
  standing in front of one C++ QFileIconProviderPrivate.

  It is built on the cute 'QAbstractFileIconProviderPrivate', as Qt's
  QFileIconProviderPrivate is built on Qt's QAbstractFileIconProviderPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileIconProviderPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'getIcon'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFileIconProvider *QFileIconProviderPrivate::q_func() const':
    takes in Python what 'QFileIconProvider
    *QFileIconProviderPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QFileIconProviderPrivate is created at the first use, not by
    'QFileIconProviderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileIconProviderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileIconProviderPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStyle.StandardPixmap)
  def getIcon(self, name: QStyle.StandardPixmap) -> QIcon:
    """
    Calls Qt's 'QIcon
    QFileIconProviderPrivate::getIcon(QStyle::StandardPixmap name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileiconproviderprivate.html#getIcon

    Parameters
    ----------

    name : QStyle.StandardPixmap
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFileIconProviderPrivate::getIcon(QStyle::StandardPixmap name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QFileIconProviderPrivate7getIconEN6QStyle14StandardPix'
        'mapE',
        name.value,
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(QFileInfo)
  def getIcon(self, fi: QFileInfo) -> QIcon:
    """
    Calls Qt's 'QIcon QFileIconProviderPrivate::getIcon(const QFileInfo &fi)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileiconproviderprivate.html#getIcon

    Parameters
    ----------

    fi : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFileIconProviderPrivate::getIcon(const QFileInfo &fi) const
    address = self.uglySide.call(
        'ritual_ZNK24QFileIconProviderPrivate7getIconERK9QFileInfo',
        self._valueOf(fi),
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

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

  @overload(QFileIconProvider)
  @overload(NoneType)
  def __init__(self, q: Optional[QFileIconProvider]) -> None:
    """
    Notes what was given, for Qt's
    'QFileIconProviderPrivate::QFileIconProviderPrivate(QFileIconProvider
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileiconproviderprivate.html

    Parameters
    ----------

    q : Optional[QFileIconProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFileIconProviderPrivate::QFileIconProviderPrivate(QFileIconProvider
    #      *q)
    self._noteCreation(QFileIconProviderPrivate, lambda: Rituals.call(
        'ritual_ZN24QFileIconProviderPrivateC1EP17QFileIconProvider',
        self._addressOf(q),
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

  def q_func(self) -> Optional[QFileIconProvider]:
    """
    Calls Qt's 'QFileIconProvider *QFileIconProviderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileiconproviderprivate.html#q_func

    Returns
    -------

    Optional[QFileIconProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileIconProvider *QFileIconProviderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QFileIconProviderPrivate6q_funcEv',
    )
    from . import QFileIconProvider
    return QFileIconProvider._cuteAt(address)
