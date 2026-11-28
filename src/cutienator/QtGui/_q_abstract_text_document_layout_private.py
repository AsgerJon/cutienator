"""
QAbstractTextDocumentLayoutPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qabstracttextdocumentlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractTextDocumentLayoutPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QSizeF
  from . import QAbstractTextDocumentLayout, QTextDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractTextDocumentLayout = WAIT['QAbstractTextDocumentLayout']
  QObject = WAIT['QObject']
  QTextDocument = WAIT['QTextDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractTextDocumentLayoutPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractTextDocumentLayoutPrivate: a plain Python
  object standing in front of one C++ QAbstractTextDocumentLayoutPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QAbstractTextDocumentLayoutPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractTextDocumentLayoutPrivate that has a ritual
  and that Python can call so far, 7 names in all: 'q_func', 'setDocument',
  'get', 'hasHandlers', '_q_dynamicPageCountSlot',
  '_q_dynamicDocumentSizeSlot', '_q_handlerDestroyed'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractTextDocumentLayout
    *QAbstractTextDocumentLayoutPrivate::q_func() const': takes in Python
    what 'QAbstractTextDocumentLayout
    *QAbstractTextDocumentLayoutPrivate::q_func()' takes.
  - Qt's
    'QAbstractTextDocumentLayoutPrivate::~QAbstractTextDocumentLayoutPrivate(
    )': the destructor: Python never removes a C++
    QAbstractTextDocumentLayoutPrivate.

  What to expect
  --------------

  - The C++ QAbstractTextDocumentLayoutPrivate is created at the first use,
    not by 'QAbstractTextDocumentLayoutPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractTextDocumentLayoutPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAbstractTextDocumentLayout)
  @overload(NoneType)
  def get(
      layout: Optional[QAbstractTextDocumentLayout],
  ) -> Optional[QAbstractTextDocumentLayoutPrivate]:
    """
    Calls Qt's 'QAbstractTextDocumentLayoutPrivate
    *QAbstractTextDocumentLayoutPrivate::get(QAbstractTextDocumentLayout
    *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html#get

    Parameters
    ----------

    layout : Optional[QAbstractTextDocumentLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractTextDocumentLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextDocumentLayoutPrivate
    #      *QAbstractTextDocumentLayoutPrivate::get(
    #      QAbstractTextDocumentLayout *layout)
    address = Rituals.call(
        'ritual_ZN34QAbstractTextDocumentLayoutPrivate3getEP27QAbstractText'
        'DocumentLayout',
        CuteMixin._addressOf(layout),
    )
    return QAbstractTextDocumentLayoutPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractTextDocumentLayoutPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasHandlers(self) -> bool:
    """
    Calls Qt's 'bool QAbstractTextDocumentLayoutPrivate::hasHandlers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html
    """
    #  bool QAbstractTextDocumentLayoutPrivate::hasHandlers() const
    return self.uglySide.call(
        'ritual_ZNK34QAbstractTextDocumentLayoutPrivate11hasHandlersEv',
    )

  def _q_dynamicPageCountSlot(self) -> int:
    """
    Calls Qt's 'int
    QAbstractTextDocumentLayoutPrivate::_q_dynamicPageCountSlot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html
    """
    #  int QAbstractTextDocumentLayoutPrivate::_q_dynamicPageCountSlot()
    #      const
    return self.uglySide.call(
        'ritual_ZNK34QAbstractTextDocumentLayoutPrivate23_q_dynamicPageCoun'
        'tSlotEv',
    )

  def _q_dynamicDocumentSizeSlot(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF
    QAbstractTextDocumentLayoutPrivate::_q_dynamicDocumentSizeSlot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF
    #      QAbstractTextDocumentLayoutPrivate::_q_dynamicDocumentSizeSlot()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QAbstractTextDocumentLayoutPrivate26_q_dynamicDocument'
        'SizeSlotEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, doc: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void
    QAbstractTextDocumentLayoutPrivate::setDocument(QTextDocument *doc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTextDocumentLayoutPrivate::setDocument(QTextDocument
    #      *doc)
    self.uglySide.call(
        'ritual_ZN34QAbstractTextDocumentLayoutPrivate11setDocumentEP13QTex'
        'tDocument',
        self._addressOf(doc),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractTextDocumentLayoutPrivate::QAbstractTextDocumentLayoutPrivate(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html
    """
    #  QAbstractTextDocumentLayoutPrivate::
    #      QAbstractTextDocumentLayoutPrivate()
    self._noteCreation(
        QAbstractTextDocumentLayoutPrivate, lambda: Rituals.call(
            'ritual_ZN34QAbstractTextDocumentLayoutPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractTextDocumentLayout]:
    """
    Calls Qt's 'QAbstractTextDocumentLayout
    *QAbstractTextDocumentLayoutPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html#q_func

    Returns
    -------

    Optional[QAbstractTextDocumentLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextDocumentLayout
    #      *QAbstractTextDocumentLayoutPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN34QAbstractTextDocumentLayoutPrivate6q_funcEv',
    )
    from . import QAbstractTextDocumentLayout
    return QAbstractTextDocumentLayout._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def _q_handlerDestroyed(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QAbstractTextDocumentLayoutPrivate::_q_handlerDestroyed(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayoutprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTextDocumentLayoutPrivate::_q_handlerDestroyed(QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN34QAbstractTextDocumentLayoutPrivate19_q_handlerDestroyed'
        'EP7QObject',
        self._addressOf(obj, 'QObject'),
    )
