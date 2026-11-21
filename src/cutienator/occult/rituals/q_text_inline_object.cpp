//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextlayout.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextformat.h>

//  QTextInlineObject::QTextInlineObject()
extern "C" Q_DECL_EXPORT
QTextInlineObject *ritual_ZN17QTextInlineObjectC1Ev() {
  return new QTextInlineObject();
}

//  bool QTextInlineObject::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTextInlineObject7isValidEv(const QTextInlineObject *self) {
  return self->isValid();
}

//  QRectF QTextInlineObject::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QTextInlineObject4rectEv(const QTextInlineObject *self) {
  return new QRectF(self->rect());
}

//  qreal QTextInlineObject::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QTextInlineObject5widthEv(const QTextInlineObject *self) {
  return self->width();
}

//  qreal QTextInlineObject::ascent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QTextInlineObject6ascentEv(const QTextInlineObject *self) {
  return self->ascent();
}

//  qreal QTextInlineObject::descent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QTextInlineObject7descentEv(
    const QTextInlineObject *self) {
  return self->descent();
}

//  qreal QTextInlineObject::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QTextInlineObject6heightEv(const QTextInlineObject *self) {
  return self->height();
}

//  Qt::LayoutDirection QTextInlineObject::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK17QTextInlineObject13textDirectionEv(
    const QTextInlineObject *self) {
  return self->textDirection();
}

//  void QTextInlineObject::setWidth(qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextInlineObject8setWidthEd(
    QTextInlineObject *self,
    qreal w) {
  self->setWidth(w);
}

//  void QTextInlineObject::setAscent(qreal a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextInlineObject9setAscentEd(
    QTextInlineObject *self,
    qreal a) {
  self->setAscent(a);
}

//  void QTextInlineObject::setDescent(qreal d)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextInlineObject10setDescentEd(
    QTextInlineObject *self,
    qreal d) {
  self->setDescent(d);
}

//  int QTextInlineObject::textPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTextInlineObject12textPositionEv(
    const QTextInlineObject *self) {
  return self->textPosition();
}

//  int QTextInlineObject::formatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTextInlineObject11formatIndexEv(
    const QTextInlineObject *self) {
  return self->formatIndex();
}

//  QTextFormat QTextInlineObject::format() const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK17QTextInlineObject6formatEv(
    const QTextInlineObject *self) {
  return new QTextFormat(self->format());
}

//  QTextInlineObject::~QTextInlineObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextInlineObjectD1Ev(QTextInlineObject *self) {
  delete self;
}
