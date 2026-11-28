"""
QWebEngineGlobalSettingsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineglobalsettings_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineGlobalSettingsPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QWebEngineGlobalSettingsPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineGlobalSettingsPrivate: a plain Python
  object standing in front of one C++ QWebEngineGlobalSettingsPrivate.

  C++ hands a QWebEngineGlobalSettingsPrivate around as a copy, so every C++
  QWebEngineGlobalSettingsPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineGlobalSettingsPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'instance',
  'configureStubHostResolver'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QWebEngineGlobalSettingsPrivate::~QWebEngineGlobalSettingsPrivate()':
    the destructor: Python removes its C++ QWebEngineGlobalSettingsPrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QWebEngineGlobalSettingsPrivate is created at the first use, not
    by 'QWebEngineGlobalSettingsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineGlobalSettingsPrivate back gives a copy the
    ritual made for Python, in a new cute QWebEngineGlobalSettingsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QWebEngineGlobalSettingsPrivate]:
    """
    Calls Qt's 'QWebEngineGlobalSettingsPrivate
    *QWebEngineGlobalSettingsPrivate::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineglobalsettingsprivate.html#instance

    Returns
    -------

    Optional[QWebEngineGlobalSettingsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineGlobalSettingsPrivate
    #      *QWebEngineGlobalSettingsPrivate::instance()
    address = Rituals.call(
        'ritual_ZN31QWebEngineGlobalSettingsPrivate8instanceEv',
    )
    return QWebEngineGlobalSettingsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineGlobalSettingsPrivate'

  #  Qt's '~QWebEngineGlobalSettingsPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineGlobalSettingsPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QWebEngineGlobalSettingsPrivateD1Ev'

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
    'QWebEngineGlobalSettingsPrivate::QWebEngineGlobalSettingsPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineglobalsettingsprivate.html
    """
    #  QWebEngineGlobalSettingsPrivate::QWebEngineGlobalSettingsPrivate()
    self._noteCreation(QWebEngineGlobalSettingsPrivate, lambda: Rituals.call(
        'ritual_ZN31QWebEngineGlobalSettingsPrivateC1Ev',
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

  def configureStubHostResolver(self) -> None:
    """
    Calls Qt's 'void
    QWebEngineGlobalSettingsPrivate::configureStubHostResolver()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineglobalsettingsprivate.html
    """
    #  void QWebEngineGlobalSettingsPrivate::configureStubHostResolver()
    self.uglySide.call(
        'ritual_ZN31QWebEngineGlobalSettingsPrivate25configureStubHostResol'
        'verEv',
    )
