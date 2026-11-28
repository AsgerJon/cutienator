"""
QQmlGuiProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlGuiProvider to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QUrl
  from . import QQmlApplication
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGuiProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlGuiProvider: a plain Python object standing in
  front of one C++ QQmlGuiProvider.

  C++ hands a QQmlGuiProvider around as a copy, so every C++ QQmlGuiProvider
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlGuiProvider that has a ritual and that Python
  can call so far, 6 names in all: 'application', 'inputMethod',
  'styleHints', 'fontFamilies', 'openUrlExternally', 'pluginName'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlGuiProvider::~QQmlGuiProvider()': the destructor: Python
    removes its C++ QQmlGuiProvider by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlGuiProvider is created at the first use, not by
    'QQmlGuiProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlGuiProvider back gives a copy the ritual made for
    Python, in a new cute QQmlGuiProvider.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGuiProvider'

  #  A C++ QQmlGuiProvider Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlGuiProvider'

  #  The functions Qt calls itself that QQmlGuiProvider is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'fontFamilies': (
          'QStringList QQmlGuiProvider::fontFamilies()',
      ),
  }

  #  The functions Qt calls itself that QQmlGuiProvider is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'application': (
          ('_ZN15QQmlGuiProvider11applicationEP7QObject',
           ('address', 'address', 'QtQml:QQmlApplication'),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'inputMethod': (
          ('_ZN15QQmlGuiProvider11inputMethodEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'styleHints': (
          ('_ZN15QQmlGuiProvider10styleHintsEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'openUrlExternally': (
          ('_ZN15QQmlGuiProvider17openUrlExternallyERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'pluginName': (
          ('_ZNK15QQmlGuiProvider10pluginNameEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Qt's '~QQmlGuiProvider()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlGuiProvider behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QQmlGuiProviderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pluginName(self) -> str:
    """
    Calls Qt's 'QString QQmlGuiProvider::pluginName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguiprovider.html#pluginName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlGuiProvider::pluginName() const
    ritual = 'ritual_ZNK15QQmlGuiProvider10pluginNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQmlGuiProvider10pluginNameEv'
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

  @overload(QObject)
  @overload(NoneType)
  def application(
      self,
      parent: Optional[QObject],
  ) -> Optional[QQmlApplication]:
    """
    Calls Qt's 'QQmlApplication *QQmlGuiProvider::application(QObject
    *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguiprovider.html#application

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlApplication]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlApplication *QQmlGuiProvider::application(QObject *parent)
    ritual = 'ritual_ZN15QQmlGuiProvider11applicationEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlGuiProvider11applicationEP7QObject'
    address = self.uglySide.call(ritual, self._addressOf(parent, 'QObject'))
    from . import QQmlApplication
    return QQmlApplication._cuteAt(address)

  def inputMethod(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlGuiProvider::inputMethod()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguiprovider.html#inputMethod

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlGuiProvider::inputMethod()
    ritual = 'ritual_ZN15QQmlGuiProvider11inputMethodEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlGuiProvider11inputMethodEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def styleHints(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlGuiProvider::styleHints()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguiprovider.html#styleHints

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlGuiProvider::styleHints()
    ritual = 'ritual_ZN15QQmlGuiProvider10styleHintsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlGuiProvider10styleHintsEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def fontFamilies(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlGuiProvider::fontFamilies()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlguiprovider.html#fontFamilies

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlGuiProvider::fontFamilies()
    address = self.uglySide.call(
        'ritual_ZN15QQmlGuiProvider12fontFamiliesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QUrl)
  def openUrlExternally(self, a0: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlGuiProvider::openUrlExternally(const QUrl &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlguiprovider.html#openUrlExternally

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlGuiProvider::openUrlExternally(const QUrl &a0)
    ritual = 'ritual_ZN15QQmlGuiProvider17openUrlExternallyERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlGuiProvider17openUrlExternallyERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(a0))
