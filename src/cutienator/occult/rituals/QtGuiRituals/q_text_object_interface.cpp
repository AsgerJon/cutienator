//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  QTextObjectInterface::~QTextObjectInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextObjectInterfaceD1Ev(QTextObjectInterface *self) {
  delete self;
}

//  QSizeF QTextObjectInterface::intrinsicSize(QTextDocument *doc, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN20QTextObjectInterface13intrinsicSizeEP13QTextDocumentiRK11QTextFormat(
    QTextObjectInterface *self,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  return new QSizeF(self->intrinsicSize(doc, posInDocument, *format));
}

//  void QTextObjectInterface::drawObject(QPainter *painter, const QRectF
//      &rect, QTextDocument *doc, int posInDocument, const QTextFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextObjectInterface10drawObjectEP8QPainterRK6QRectFP13QTextDocumentiRK11QTextFormat(
    QTextObjectInterface *self,
    QPainter *painter,
    const QRectF *rect,
    QTextDocument *doc,
    int posInDocument,
    const QTextFormat *format) {
  self->drawObject(painter, *rect, doc, posInDocument, *format);
}
