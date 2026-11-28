"""
QQmlSA::GenericPropertyPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::GenericPropertyPass to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GenericPropertyPass(QQmlSA.PropertyPass):
  """
  The cute side of Qt's QQmlSA::GenericPropertyPass: a plain Python object
  standing in front of one C++ QQmlSA::GenericPropertyPass.

  It is built on the cute 'QQmlSA::PropertyPass', as Qt's
  QQmlSA::GenericPropertyPass is built on Qt's QQmlSA::PropertyPass, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSA::GenericPropertyPass that has a ritual and
  that Python can call so far, 8 names in all: 'onBindingDefault',
  'onReadDefault', 'onCallDefault', 'onWriteDefault', 'onBinding', 'onRead',
  'onCall', 'onWrite'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What to expect
  --------------

  - The C++ QQmlSA::GenericPropertyPass is created at the first use, not by
    'QQmlSA::GenericPropertyPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::GenericPropertyPass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QQmlSA.PropertyPass, WAIT['QQmlSA.Element'], str,
      WAIT['QQmlSA.Binding'], WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'],
  )
  @overload(
      NoneType, WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Binding'],
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'],
  )
  def onBindingDefault(
      a0: Optional[QQmlSA.PropertyPass],
      a1: QQmlSA.Element,
      a2: str,
      a3: QQmlSA.Binding,
      a4: QQmlSA.Element,
      a5: QQmlSA.Element,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSA::GenericPropertyPass::onBindingDefault(PropertyPass *a0, const
    Element &a1, const QString &a2, const Binding &a3, const Element &a4,
    const Element &a5)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onBindingDefault

    Parameters
    ----------

    a0 : Optional[QQmlSA.PropertyPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : QQmlSA.Binding
      Passed on as a value: Qt reads the C++ QQmlSA::Binding, which stays
      Python's own.

    a4 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a5 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onBindingDefault(PropertyPass *a0,
    #      const Element &a1, const QString &a2, const Binding &a3, const
    #      Element &a4, const Element &a5)
    Rituals.call(
        'ritual_ZN6QQmlSA19GenericPropertyPass16onBindingDefaultEPNS_12Prop'
        'ertyPassERKNS_7ElementERK7QStringRKNS_7BindingES5_S5_',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
        CuteMixin._valueOf(a3), CuteMixin._valueOf(a4),
        CuteMixin._valueOf(a5),
    )

  @staticmethod
  @overload(
      QQmlSA.PropertyPass, WAIT['QQmlSA.Element'], str,
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.SourceLocation'],
  )
  @overload(
      NoneType, WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def onReadDefault(
      a0: Optional[QQmlSA.PropertyPass],
      a1: QQmlSA.Element,
      a2: str,
      a3: QQmlSA.Element,
      a4: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onReadDefault(PropertyPass
    *a0, const Element &a1, const QString &a2, const Element &a3,
    SourceLocation a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onReadDefault

    Parameters
    ----------

    a0 : Optional[QQmlSA.PropertyPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a4 : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onReadDefault(PropertyPass *a0,
    #      const Element &a1, const QString &a2, const Element &a3,
    #      SourceLocation a4)
    Rituals.call(
        'ritual_ZN6QQmlSA19GenericPropertyPass13onReadDefaultEPNS_12Propert'
        'yPassERKNS_7ElementERK7QStringS5_NS_14SourceLocationE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
        CuteMixin._valueOf(a3), CuteMixin._valueOf(a4),
    )

  @staticmethod
  @overload(
      QQmlSA.PropertyPass, WAIT['QQmlSA.Element'], str,
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.SourceLocation'],
  )
  @overload(
      NoneType, WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def onCallDefault(
      a0: Optional[QQmlSA.PropertyPass],
      a1: QQmlSA.Element,
      a2: str,
      a3: QQmlSA.Element,
      a4: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onCallDefault(PropertyPass
    *a0, const Element &a1, const QString &a2, const Element &a3,
    SourceLocation a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onCallDefault

    Parameters
    ----------

    a0 : Optional[QQmlSA.PropertyPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a4 : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onCallDefault(PropertyPass *a0,
    #      const Element &a1, const QString &a2, const Element &a3,
    #      SourceLocation a4)
    Rituals.call(
        'ritual_ZN6QQmlSA19GenericPropertyPass13onCallDefaultEPNS_12Propert'
        'yPassERKNS_7ElementERK7QStringS5_NS_14SourceLocationE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
        CuteMixin._valueOf(a3), CuteMixin._valueOf(a4),
    )

  @staticmethod
  @overload(
      QQmlSA.PropertyPass, WAIT['QQmlSA.Element'], str,
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  @overload(
      NoneType, WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.SourceLocation'],
  )
  def onWriteDefault(
      a0: Optional[QQmlSA.PropertyPass],
      a1: QQmlSA.Element,
      a2: str,
      a3: QQmlSA.Element,
      a4: QQmlSA.Element,
      a5: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onWriteDefault(PropertyPass
    *a0, const Element &a1, const QString &a2, const Element &a3, const
    Element &a4, SourceLocation a5)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onWriteDefault

    Parameters
    ----------

    a0 : Optional[QQmlSA.PropertyPass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a4 : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    a5 : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onWriteDefault(PropertyPass *a0,
    #      const Element &a1, const QString &a2, const Element &a3, const
    #      Element &a4, SourceLocation a5)
    Rituals.call(
        'ritual_ZN6QQmlSA19GenericPropertyPass14onWriteDefaultEPNS_12Proper'
        'tyPassERKNS_7ElementERK7QStringS5_S5_NS_14SourceLocationE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1), a2,
        CuteMixin._valueOf(a3), CuteMixin._valueOf(a4),
        CuteMixin._valueOf(a5),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::GenericPropertyPass'

  #  A C++ QQmlSA::GenericPropertyPass Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSA_GenericPropertyPass'

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

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Binding'],
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'],
  )
  def onBinding(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      binding: QQmlSA.Binding,
      bindingScope: QQmlSA.Element,
      value: QQmlSA.Element,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onBinding(const Element
    &element, const QString &propertyName, const Binding &binding, const
    Element &bindingScope, const Element &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onBinding

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    binding : QQmlSA.Binding
      Passed on as a value: Qt reads the C++ QQmlSA::Binding, which stays
      Python's own.

    bindingScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    value : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onBinding(const Element &element,
    #      const QString &propertyName, const Binding &binding, const Element
    #      &bindingScope, const Element &value)
    ritual = (
        'ritual_ZN6QQmlSA19GenericPropertyPass9onBindingERKNS_7ElementERK7Q'
        'StringRKNS_7BindingES3_S3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA19GenericPropertyPass9onBindingERKNS_7Elemen'
          'tERK7QStringRKNS_7BindingES3_S3_')
    self.uglySide.call(
        ritual,
        self._valueOf(element), propertyName, self._valueOf(binding),
        self._valueOf(bindingScope), self._valueOf(value),
    )

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def onRead(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      readScope: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onRead(const Element
    &element, const QString &propertyName, const Element &readScope,
    SourceLocation location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onRead

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    readScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onRead(const Element &element, const
    #      QString &propertyName, const Element &readScope, SourceLocation
    #      location)
    ritual = (
        'ritual_ZN6QQmlSA19GenericPropertyPass6onReadERKNS_7ElementERK7QStr'
        'ingS3_NS_14SourceLocationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA19GenericPropertyPass6onReadERKNS_7ElementER'
          'K7QStringS3_NS_14SourceLocationE')
    self.uglySide.call(
        ritual,
        self._valueOf(element), propertyName, self._valueOf(readScope),
        self._valueOf(location),
    )

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def onCall(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      readScope: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onCall(const Element
    &element, const QString &propertyName, const Element &readScope,
    SourceLocation location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onCall

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    readScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onCall(const Element &element, const
    #      QString &propertyName, const Element &readScope, SourceLocation
    #      location)
    ritual = (
        'ritual_ZN6QQmlSA19GenericPropertyPass6onCallERKNS_7ElementERK7QStr'
        'ingS3_NS_14SourceLocationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA19GenericPropertyPass6onCallERKNS_7ElementER'
          'K7QStringS3_NS_14SourceLocationE')
    self.uglySide.call(
        ritual,
        self._valueOf(element), propertyName, self._valueOf(readScope),
        self._valueOf(location),
    )

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.SourceLocation'],
  )
  def onWrite(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      value: QQmlSA.Element,
      writeScope: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPropertyPass::onWrite(const Element
    &element, const QString &propertyName, const Element &value, const
    Element &writeScope, SourceLocation location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpropertypass.html#onWrite

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    writeScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPropertyPass::onWrite(const Element &element,
    #      const QString &propertyName, const Element &value, const Element
    #      &writeScope, SourceLocation location)
    ritual = (
        'ritual_ZN6QQmlSA19GenericPropertyPass7onWriteERKNS_7ElementERK7QSt'
        'ringS3_S3_NS_14SourceLocationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA19GenericPropertyPass7onWriteERKNS_7ElementE'
          'RK7QStringS3_S3_NS_14SourceLocationE')
    self.uglySide.call(
        ritual,
        self._valueOf(element), propertyName, self._valueOf(value),
        self._valueOf(writeScope), self._valueOf(location),
    )
