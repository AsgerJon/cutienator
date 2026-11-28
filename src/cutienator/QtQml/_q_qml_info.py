"""
QQmlInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QDebug


class QQmlInfo(QDebug):
  """
  The cute side of Qt's QQmlInfo: a plain Python object standing in front of
  one C++ QQmlInfo.

  It is built on the cute 'QDebug', as Qt's QQmlInfo is built on Qt's QDebug,
  and has everything that class has.

  C++ hands a QQmlInfo around as a copy, so every C++ QQmlInfo behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlInfo yet. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlInfo::~QQmlInfo()': the destructor: Python removes its C++
    QQmlInfo by it, and has no other use for it.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(QChar t)': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(bool t)': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(char t)': takes a single letter as C
    has it.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(short t)': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(unsigned short t)': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(int t)': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(unsigned int t)': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(long t)': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(unsigned long t)': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(qint64 t)': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(quint64 t)': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(float t)': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(double t)': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(const char *t)': gives a type Python
    has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(const QString &t)': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(QStringView t)': gives a type Python
    has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(const QLatin1String &t)': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(const QByteArray &t)': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(const void *t)': names 'void', which
    has no cute class yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(QTextStreamFunction f)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(QTextStreamManipulator m)': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlInfo &QQmlInfo::operator<<(const QUrl &t)': gives a type Python
    has no way to take yet.
  - Qt's 'QQmlInfo::QQmlInfo(QQmlInfoPrivate *a0)': names 'QQmlInfoPrivate',
    which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlInfo is created at the first use, not by 'QQmlInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlInfo back gives a copy the ritual made for
    Python, in a new cute QQmlInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInfo'

  #  Qt's '~QQmlInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QQmlInfoD1Ev'

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

  @overload(THIS)
  def __init__(self, a0: QQmlInfo) -> None:
    """
    Notes what was given, for Qt's 'QQmlInfo::QQmlInfo(const QQmlInfo &a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinfo.html#QQmlInfo

    Parameters
    ----------

    a0 : QQmlInfo
      Passed on as a value: Qt reads the C++ QQmlInfo, which stays Python's
      own.
    """
    #  QQmlInfo::QQmlInfo(const QQmlInfo &a0)
    self._noteCreation(QQmlInfo, lambda: Rituals.call(
        'ritual_ZN8QQmlInfoC1ERKS_', self._valueOf(a0),
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
