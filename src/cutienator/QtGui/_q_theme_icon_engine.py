"""
QThemeIconEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QThemeIconEngine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QIconEngine, QProxyIconEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QThemeIconEngine(QProxyIconEngine):
  """
  The cute side of Qt's QThemeIconEngine: a plain Python object standing in
  front of one C++ QThemeIconEngine.

  It is built on the cute 'QProxyIconEngine', as Qt's QThemeIconEngine is
  built on Qt's QProxyIconEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QThemeIconEngine that has a ritual and that Python
  can call so far, 3 names in all: 'clone', 'proxiedEngine', 'key'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QThemeIconEngine::read(QDataStream &in)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QThemeIconEngine::write(QDataStream &out) const': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 leans on 'QThemeIconEngine.

  What to expect
  --------------

  - The C++ QThemeIconEngine is created at the first use, not by
    'QThemeIconEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QThemeIconEngine.
  - Each name of Qt's QThemeIconEngine that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QThemeIconEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QThemeIconEngine::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthemeiconengine.html#clone

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QThemeIconEngine::clone() const
    address = self.uglySide.call('ritual_ZNK16QThemeIconEngine5cloneEv')
    return QIconEngine._cuteAt(address)

  def proxiedEngine(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QThemeIconEngine::proxiedEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthemeiconengine.html#proxiedEngine

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QThemeIconEngine::proxiedEngine() const
    address = self.uglySide.call(
        'ritual_ZNK16QThemeIconEngine13proxiedEngineEv',
    )
    return QIconEngine._cuteAt(address)

  def key(self) -> str:
    """
    Calls Qt's 'QString QThemeIconEngine::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthemeiconengine.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QThemeIconEngine::key() const
    ritual = 'ritual_ZNK16QThemeIconEngine3keyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QThemeIconEngine3keyEv'
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QThemeIconEngine::QThemeIconEngine(const QString &iconName)':
      leans on 'QThemeIconEngine::proxiedEngine() const', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'QThemeIconEngine::QThemeIconEngine(const QThemeIconEngine
      &other)': leans on 'QThemeIconEngine::proxiedEngine() const', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QThemeIconEngine.__init__' has no cute function yet. Qt's "
        "'QThemeIconEngine::QThemeIconEngine(const QString &iconName)': "
        "leans on 'QThemeIconEngine::proxiedEngine() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken. Qt's "
        "'QThemeIconEngine::QThemeIconEngine(const QThemeIconEngine "
        "&other)': leans on 'QThemeIconEngine::proxiedEngine() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
