//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextdocument.h>

//  QAbstractUndoItem::~QAbstractUndoItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractUndoItemD1Ev(QAbstractUndoItem *self) {
  delete self;
}

//  void QAbstractUndoItem::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractUndoItem4undoEv(QAbstractUndoItem *self) {
  self->undo();
}

//  void QAbstractUndoItem::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractUndoItem4redoEv(QAbstractUndoItem *self) {
  self->redo();
}
