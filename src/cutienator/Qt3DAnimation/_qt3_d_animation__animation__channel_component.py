"""
Qt3DAnimation::Animation::ChannelComponent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ChannelComponent to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class ChannelComponent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ChannelComponent: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::ChannelComponent.

  C++ hands a Qt3DAnimation::Animation::ChannelComponent around as a copy, so
  every C++ Qt3DAnimation::Animation::ChannelComponent behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ChannelComponent that has
  a ritual and that Python can call so far, 2 names in all: 'read',
  'setFromQChannelComponent'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::ChannelComponent::~ChannelComponent()':
    the destructor: Python removes its C++
    Qt3DAnimation::Animation::ChannelComponent by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ChannelComponent is created at the
    first use, not by 'Qt3DAnimation::Animation::ChannelComponent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::ChannelComponent back gives
    a copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::ChannelComponent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ChannelComponent'

  #  Qt's '~Qt3DAnimation::Animation::ChannelComponent()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DAnimation::Animation::ChannelComponent behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN13Qt3DAnimation9Animation16ChannelComponentD1Ev')

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

  @overload(WAIT['Qt3DAnimation.QChannelComponent'])
  def setFromQChannelComponent(
      self,
      qcc: Qt3DAnimation.QChannelComponent,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelComponent::setFromQChannelComponent(
    const QChannelComponent &qcc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelcomponent.html

    Parameters
    ----------

    qcc : Qt3DAnimation.QChannelComponent
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::QChannelComponent, which stays Python's own.
    """
    #  void Qt3DAnimation::Animation::ChannelComponent::
    #      setFromQChannelComponent(const QChannelComponent &qcc)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation16ChannelComponent24setFromQChan'
        'nelComponentERKNS_17QChannelComponentE',
        self._valueOf(qcc),
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

  @overload(QJsonObject)
  def read(self, json: QJsonObject) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::ChannelComponent::read(const
    QJsonObject &json)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelcomponent.html#read

    Parameters
    ----------

    json : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ChannelComponent::read(const
    #      QJsonObject &json)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation16ChannelComponent4readERK11QJso'
        'nObject',
        self._valueOf(json),
    )
