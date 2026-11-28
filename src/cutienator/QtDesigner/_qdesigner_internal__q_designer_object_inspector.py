"""
qdesigner_internal::QDesignerObjectInspector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_objectinspector_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerObjectInspector to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QDesignerObjectInspectorInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerObjectInspector(QDesignerObjectInspectorInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerObjectInspector: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerObjectInspector.

  It is built on the cute 'QDesignerObjectInspectorInterface', as Qt's
  qdesigner_internal::QDesignerObjectInspector is built on Qt's
  QDesignerObjectInspectorInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerObjectInspector that
  has a ritual and that Python can call so far, 5 names in all: 'metaObject',
  'tr', 'selectObject', 'clearSelection', 'mainContainerChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *qdesigner_internal::QDesignerObjectInspector::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerObjectInspector::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    qdesigner_internal::QDesignerObjectInspector::getSelection(Selection &s)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerObjectInspector is created at the
    first use, not by 'qdesigner_internal::QDesignerObjectInspector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::QDesignerObjectInspector.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerObjectInspector. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerObjectInspector that has
    no cute function yet, '__init__', 'getSelection', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::QDesignerObjectInspector::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerobjectinspector.html

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::QDesignerObjectInspector::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal24QDesignerObjectInspector2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerObjectInspector'

  #  A C++ qdesigner_internal::QDesignerObjectInspector Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QDesignerObjectInspector'

  #  The functions Qt calls itself that
  #  qdesigner_internal::QDesignerObjectInspector is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getSelection': (
          'void '
          'qdesigner_internal::QDesignerObjectInspector::getSelection(Selec'
          'tion &) const',
      ),
  }

  #  The functions Qt calls itself that
  #  qdesigner_internal::QDesignerObjectInspector is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'selectObject': (
          ('_ZN18qdesigner_internal24QDesignerObjectInspector12selectObject'
           'EP7QObject',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'clearSelection': (
          ('_ZN18qdesigner_internal24QDesignerObjectInspector14clearSelecti'
           'onEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'mainContainerChanged': (
          ('_ZN18qdesigner_internal24QDesignerObjectInspector20mainContaine'
           'rChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::QDesignerObjectInspector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerobjectinspector.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::QDesignerObjectInspector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24QDesignerObjectInspector10metaObje'
        'ctEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's
    'qdesigner_internal::QDesignerObjectInspector::QDesignerObjectInspector(
    QWidget *parent, Qt::WindowFlags flags)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerObjectInspector.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::QDesignerObjectInspector::QDesignerObjectInspe"
        "ctor(QWidget *parent, Qt::WindowFlags flags)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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
  def selectObject(self, o: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerObjectInspector::selectObject(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerobjectinspector.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      qdesigner_internal::QDesignerObjectInspector::selectObject(QObject
    #      *o)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerObjectInspector12selectObj'
        'ectEP7QObject',
        self._addressOf(o, 'QObject'),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerObjectInspector::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerobjectinspector.html
    """
    #  void qdesigner_internal::QDesignerObjectInspector::clearSelection()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerObjectInspector14clearSele'
        'ctionEv',
    )

  def mainContainerChanged(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerObjectInspector::mainContainerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerobjectinspector.html
    """
    #  void qdesigner_internal::QDesignerObjectInspector::
    #      mainContainerChanged()
    ritual = (
        'ritual_ZN18qdesigner_internal24QDesignerObjectInspector20mainConta'
        'inerChangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24QDesignerObjectInspector20mai'
          'nContainerChangedEv')
    self.uglySide.call(ritual)

  @staticmethod
  def getSelection(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::QDesignerObjectInspector::getSelection(Selection &s)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerObjectInspector.getSelection' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::QDesignerObjectInspector::getSelection(Selectio"
        "n &s) const': takes a type Python has no way to hand over yet.")
