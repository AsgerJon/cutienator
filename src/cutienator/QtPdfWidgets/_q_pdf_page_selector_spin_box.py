"""
QPdfPageSelectorSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdfWidgets/6.12.0/QtPdfWidgets/private/qpdfpageselector_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPdfPageSelectorSpinBox to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtWidgets import QSpinBox

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtPdf import QPdfDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPdfDocument = WAIT['QPdfDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfPageSelectorSpinBox(QSpinBox):
  """
  The cute side of Qt's QPdfPageSelectorSpinBox: a plain Python object
  standing in front of one C++ QPdfPageSelectorSpinBox.

  It is built on the cute 'QSpinBox', as Qt's QPdfPageSelectorSpinBox is
  built on Qt's QSpinBox, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfPageSelectorSpinBox that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'document',
  '_q_documentChanged', 'valueFromText', 'textFromValue',
  'documentStatusChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfPageSelectorSpinBox::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPdfPageSelectorSpinBox::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfPageSelectorSpinBox::~QPdfPageSelectorSpinBox()': the
    destructor: Python never removes a C++ QPdfPageSelectorSpinBox.
  - Qt's 'QValidator::State QPdfPageSelectorSpinBox::validate(QString &text,
    int &pos) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 16 functions Qt declares: 4 leans on 'QPdfPageSelectorSpinBox; 2
  not a gap.

  What to expect
  --------------

  - The C++ QPdfPageSelectorSpinBox is created at the first use, not by
    'QPdfPageSelectorSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfPageSelectorSpinBox.
  - Qt tells when it has removed the C++ QPdfPageSelectorSpinBox. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPdfPageSelectorSpinBox that has no cute function yet,
    '__init__', 'setDocument', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfPageSelectorSpinBox'

  #  A C++ QPdfPageSelectorSpinBox Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfPageSelectorSpinBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfPageSelectorSpinBox::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselectorspinbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfPageSelectorSpinBox::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QPdfPageSelectorSpinBox10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QPdfDocument]:
    """
    Calls Qt's 'QPdfDocument *QPdfPageSelectorSpinBox::document() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselectorspinbox.html#document

    Returns
    -------

    Optional[QPdfDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfDocument *QPdfPageSelectorSpinBox::document() const
    address = self.uglySide.call(
        'ritual_ZNK23QPdfPageSelectorSpinBox8documentEv',
    )
    from ..QtPdf import QPdfDocument
    return QPdfDocument._cuteAt(address)

  @overload(str)
  def valueFromText(self, text: str) -> int:
    """
    Calls Qt's 'int QPdfPageSelectorSpinBox::valueFromText(const QString
    &text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselectorspinbox.html#valueFromText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QPdfPageSelectorSpinBox::valueFromText(const QString &text) const
    ritual = 'ritual_ZNK23QPdfPageSelectorSpinBox13valueFromTextERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QPdfPageSelectorSpinBox13valueFromTextERK7QStrin'
          'g')
    return self.uglySide.call(ritual, text)

  @overload(int)
  def textFromValue(self, value: int) -> str:
    """
    Calls Qt's 'QString QPdfPageSelectorSpinBox::textFromValue(int value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselectorspinbox.html#textFromValue

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfPageSelectorSpinBox::textFromValue(int value) const
    ritual = 'ritual_ZNK23QPdfPageSelectorSpinBox13textFromValueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPdfPageSelectorSpinBox13textFromValueEi'
    return self.uglySide.call(ritual, value)

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
    - Qt's 'QPdfPageSelectorSpinBox::QPdfPageSelectorSpinBox()': leans on
      'QPdfPageSelectorSpinBox::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QPdfPageSelectorSpinBox::QPdfPageSelectorSpinBox(QWidget
      *parent)': leans on
      'QPdfPageSelectorSpinBox::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QPdfPageSelectorSpinBox.__init__' has no cute function yet. Qt's "
        "'QPdfPageSelectorSpinBox::QPdfPageSelectorSpinBox()': leans on "
        "'QPdfPageSelectorSpinBox::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QPdfPageSelectorSpinBox::QPdfPageSelectorSpinBox(QWidget "
        "*parent)': leans on "
        "'QPdfPageSelectorSpinBox::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QPdfDocument)
  @overload(NoneType)
  def _q_documentChanged(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfPageSelectorSpinBox::_q_documentChanged(QPdfDocument
    *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselectorspinbox.html#_q_documentChanged

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfPageSelectorSpinBox::_q_documentChanged(QPdfDocument
    #      *document)
    self.uglySide.call(
        'ritual_ZN23QPdfPageSelectorSpinBox18_q_documentChangedEP12QPdfDocu'
        'ment',
        self._addressOf(document),
    )

  def documentStatusChanged(self) -> None:
    """
    Calls Qt's 'void QPdfPageSelectorSpinBox::documentStatusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselectorspinbox.html#documentStatusChanged
    """
    #  void QPdfPageSelectorSpinBox::documentStatusChanged()
    self.uglySide.call(
        'ritual_ZN23QPdfPageSelectorSpinBox21documentStatusChangedEv',
    )

  @staticmethod
  def setDocument(*__, **_) -> Never:
    """
    Qt's 'void QPdfPageSelectorSpinBox::setDocument(QPdfDocument *document)':
    leans on 'QPdfPageSelectorSpinBox::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QPdfPageSelectorSpinBox.setDocument' has no cute function yet. "
        "Qt's 'void QPdfPageSelectorSpinBox::setDocument(QPdfDocument "
        "*document)': leans on 'QPdfPageSelectorSpinBox::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
