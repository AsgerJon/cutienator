"""
QQmlSA::PropertyPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PropertyPass(QQmlSA.GenericPass):
  """
  The cute side of Qt's QQmlSA::PropertyPass: a plain Python object standing
  in front of one C++ QQmlSA::PropertyPass.

  It is built on the cute 'QQmlSA::GenericPass', as Qt's QQmlSA::PropertyPass
  is built on Qt's QQmlSA::GenericPass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSA::PropertyPass that has a ritual and that
  Python can call so far, 4 names in all: 'onBinding', 'onRead', 'onCall',
  'onWrite'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQmlSA::PropertyPass is created at the first use, not by
    'QQmlSA::PropertyPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::PropertyPass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::PropertyPass'

  #  A C++ QQmlSA::PropertyPass Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSA_PropertyPass'

  #  The functions Qt calls itself that QQmlSA::PropertyPass is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'onBinding': (
          ('_ZN6QQmlSA12PropertyPass9onBindingERKNS_7ElementERK7QStringRKNS'
           '_7BindingES3_S3_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'text', ''),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Binding'),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
           )),
      ),
      'onRead': (
          ('_ZN6QQmlSA12PropertyPass6onReadERKNS_7ElementERK7QStringS3_NS_1'
           '4SourceLocationE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'text', ''),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.SourceLocation'),
           )),
      ),
      'onCall': (
          ('_ZN6QQmlSA12PropertyPass6onCallERKNS_7ElementERK7QStringS3_NS_1'
           '4SourceLocationE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'text', ''),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.SourceLocation'),
           )),
      ),
      'onWrite': (
          ('_ZN6QQmlSA12PropertyPass7onWriteERKNS_7ElementERK7QStringS3_S3_'
           'NS_14SourceLocationE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'text', ''),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
               ('address', 'value', 'QtQmlCompiler:QQmlSA.SourceLocation'),
           )),
      ),
  }

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

  @overload(WAIT['QQmlSA.PassManager'])
  @overload(NoneType)
  def __init__(self, manager: Optional[QQmlSA.PassManager]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::PropertyPass::PropertyPass(PassManager *manager)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertypass.html#PropertyPass

    Parameters
    ----------

    manager : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::PropertyPass::PropertyPass(PassManager *manager)
    self._noteCreation(PropertyPass, lambda: Rituals.call(
        'ritual_ZN6QQmlSA12PropertyPassC1EPNS_11PassManagerE',
        self._addressOf(manager),
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
    Calls Qt's 'void QQmlSA::PropertyPass::onBinding(const QQmlSA::Element
    &element, const QString &propertyName, const QQmlSA::Binding &binding,
    const QQmlSA::Element &bindingScope, const QQmlSA::Element &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-propertypass.html#onBinding

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
    #  void QQmlSA::PropertyPass::onBinding(const QQmlSA::Element &element,
    #      const QString &propertyName, const QQmlSA::Binding &binding, const
    #      QQmlSA::Element &bindingScope, const QQmlSA::Element &value)
    ritual = (
        'ritual_ZN6QQmlSA12PropertyPass9onBindingERKNS_7ElementERK7QStringR'
        'KNS_7BindingES3_S3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA12PropertyPass9onBindingERKNS_7ElementERK7QS'
          'tringRKNS_7BindingES3_S3_')
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
    Calls Qt's 'void QQmlSA::PropertyPass::onRead(const QQmlSA::Element
    &element, const QString &propertyName, const QQmlSA::Element &readScope,
    QQmlSA::SourceLocation location)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-propertypass.html#onRead

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
    #  void QQmlSA::PropertyPass::onRead(const QQmlSA::Element &element,
    #      const QString &propertyName, const QQmlSA::Element &readScope,
    #      QQmlSA::SourceLocation location)
    ritual = (
        'ritual_ZN6QQmlSA12PropertyPass6onReadERKNS_7ElementERK7QStringS3_N'
        'S_14SourceLocationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA12PropertyPass6onReadERKNS_7ElementERK7QStri'
          'ngS3_NS_14SourceLocationE')
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
    Calls Qt's 'void QQmlSA::PropertyPass::onCall(const QQmlSA::Element
    &element, const QString &propertyName, const QQmlSA::Element &readScope,
    QQmlSA::SourceLocation location)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-propertypass.html#onCall

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
    #  void QQmlSA::PropertyPass::onCall(const QQmlSA::Element &element,
    #      const QString &propertyName, const QQmlSA::Element &readScope,
    #      QQmlSA::SourceLocation location)
    ritual = (
        'ritual_ZN6QQmlSA12PropertyPass6onCallERKNS_7ElementERK7QStringS3_N'
        'S_14SourceLocationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA12PropertyPass6onCallERKNS_7ElementERK7QStri'
          'ngS3_NS_14SourceLocationE')
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
    Calls Qt's 'void QQmlSA::PropertyPass::onWrite(const QQmlSA::Element
    &element, const QString &propertyName, const QQmlSA::Element &value,
    const QQmlSA::Element &writeScope, QQmlSA::SourceLocation location)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-propertypass.html#onWrite

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
    #  void QQmlSA::PropertyPass::onWrite(const QQmlSA::Element &element,
    #      const QString &propertyName, const QQmlSA::Element &value, const
    #      QQmlSA::Element &writeScope, QQmlSA::SourceLocation location)
    ritual = (
        'ritual_ZN6QQmlSA12PropertyPass7onWriteERKNS_7ElementERK7QStringS3_'
        'S3_NS_14SourceLocationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlSA12PropertyPass7onWriteERKNS_7ElementERK7QStr'
          'ingS3_S3_NS_14SourceLocationE')
    self.uglySide.call(
        ritual,
        self._valueOf(element), propertyName, self._valueOf(value),
        self._valueOf(writeScope), self._valueOf(location),
    )
