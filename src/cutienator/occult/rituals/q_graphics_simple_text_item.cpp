//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>

//  QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsSimpleTextItem *ritual_ZN23QGraphicsSimpleTextItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsSimpleTextItem(parent);
}

//  QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(const QString &text,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsSimpleTextItem *ritual_ZN23QGraphicsSimpleTextItemC1ERK7QStringP13QGraphicsItem(
    const QString *text,
    QGraphicsItem *parent) {
  return new QGraphicsSimpleTextItem(*text, parent);
}

//  QGraphicsSimpleTextItem::~QGraphicsSimpleTextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItemD1Ev(QGraphicsSimpleTextItem *self) {
  delete self;
}

//  void QGraphicsSimpleTextItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem7setTextERK7QString(
    QGraphicsSimpleTextItem *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QGraphicsSimpleTextItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QGraphicsSimpleTextItem4textEv(
    const QGraphicsSimpleTextItem *self) {
  return new QString(self->text());
}

//  void QGraphicsSimpleTextItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem7setFontERK5QFont(
    QGraphicsSimpleTextItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QFont QGraphicsSimpleTextItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QGraphicsSimpleTextItem4fontEv(
    const QGraphicsSimpleTextItem *self) {
  return new QFont(self->font());
}

//  QRectF QGraphicsSimpleTextItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK23QGraphicsSimpleTextItem12boundingRectEv(
    const QGraphicsSimpleTextItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsSimpleTextItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QGraphicsSimpleTextItem5shapeEv(
    const QGraphicsSimpleTextItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsSimpleTextItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGraphicsSimpleTextItem8containsERK7QPointF(
    const QGraphicsSimpleTextItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsSimpleTextItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSimpleTextItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsSimpleTextItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsSimpleTextItem::isObscuredBy(const QGraphicsItem *item)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGraphicsSimpleTextItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsSimpleTextItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsSimpleTextItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QGraphicsSimpleTextItem10opaqueAreaEv(
    const QGraphicsSimpleTextItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsSimpleTextItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QGraphicsSimpleTextItem4typeEv(
    const QGraphicsSimpleTextItem *self) {
  return self->type();
}
