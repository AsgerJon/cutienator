//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qabstracttextdocumentlayout.h>

//  QAbstractTextDocumentLayout::PaintContext::PaintContext()
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout::PaintContext *ritual_ZN27QAbstractTextDocumentLayout12PaintContextC1Ev() {
  return new QAbstractTextDocumentLayout::PaintContext();
}

//  QAbstractTextDocumentLayout::PaintContext::~PaintContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout12PaintContextD1Ev(
    QAbstractTextDocumentLayout::PaintContext *self) {
  delete self;
}
