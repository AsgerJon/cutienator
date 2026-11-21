//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsproxywidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QGraphicsProxyWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QGraphicsProxyWidget10metaObjectEv(
    const QGraphicsProxyWidget *self) {
  return self->metaObject();
}

//  QString QGraphicsProxyWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QGraphicsProxyWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsProxyWidget::tr(s, c, n));
}

//  QGraphicsProxyWidget::QGraphicsProxyWidget(QGraphicsItem *parent,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN20QGraphicsProxyWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsItem *parent,
    int wFlags) {
  return new QGraphicsProxyWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QGraphicsProxyWidget::~QGraphicsProxyWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidgetD1Ev(QGraphicsProxyWidget *self) {
  delete self;
}

//  void QGraphicsProxyWidget::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget9setWidgetEP7QWidget(
    QGraphicsProxyWidget *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QGraphicsProxyWidget::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK20QGraphicsProxyWidget6widgetEv(
    const QGraphicsProxyWidget *self) {
  return self->widget();
}

//  QRectF QGraphicsProxyWidget::subWidgetRect(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsProxyWidget13subWidgetRectEPK7QWidget(
    const QGraphicsProxyWidget *self,
    const QWidget *widget) {
  return new QRectF(self->subWidgetRect(widget));
}

//  void QGraphicsProxyWidget::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget11setGeometryERK6QRectF(
    QGraphicsProxyWidget *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  void QGraphicsProxyWidget::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsProxyWidget5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsProxyWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  int QGraphicsProxyWidget::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsProxyWidget4typeEv(
    const QGraphicsProxyWidget *self) {
  return self->type();
}

//  QGraphicsProxyWidget
//      *QGraphicsProxyWidget::createProxyForChildWidget(QWidget *child)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN20QGraphicsProxyWidget25createProxyForChildWidgetEP7QWidget(
    QGraphicsProxyWidget *self,
    QWidget *child) {
  return self->createProxyForChildWidget(child);
}
