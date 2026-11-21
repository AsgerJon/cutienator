//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintengine.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  qreal QTextItem::descent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextItem7descentEv(const QTextItem *self) {
  return self->descent();
}

//  qreal QTextItem::ascent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextItem6ascentEv(const QTextItem *self) {
  return self->ascent();
}

//  qreal QTextItem::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextItem5widthEv(const QTextItem *self) {
  return self->width();
}

//  RenderFlags QTextItem::renderFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextItem11renderFlagsEv(const QTextItem *self) {
  return static_cast<int>(self->renderFlags().toInt());
}

//  QString QTextItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextItem4textEv(const QTextItem *self) {
  return new QString(self->text());
}

//  QFont QTextItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK9QTextItem4fontEv(const QTextItem *self) {
  return new QFont(self->font());
}

//  QTextItem::~QTextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextItemD1Ev(QTextItem *self) {
  delete self;
}
