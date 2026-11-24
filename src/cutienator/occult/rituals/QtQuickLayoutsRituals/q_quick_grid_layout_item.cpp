//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickgridlayoutengine_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>

//  QQuickGridLayoutItem::QQuickGridLayoutItem(QQuickItem *item, int row, int
//      column, int rowSpan, int columnSpan, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
QQuickGridLayoutItem *ritual_ZN20QQuickGridLayoutItemC1EP10QQuickItemiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickItem *item,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int alignment) {
  return new QQuickGridLayoutItem(
      item,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QSizeF QQuickGridLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK20QQuickGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QQuickGridLayoutItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  QSizeF *QQuickGridLayoutItem::effectiveSizeHints() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK20QQuickGridLayoutItem18effectiveSizeHintsEv(
    const QQuickGridLayoutItem *self) {
  return self->effectiveSizeHints();
}

//  void QQuickGridLayoutItem::setCachedSizeHints(QSizeF *sizeHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGridLayoutItem18setCachedSizeHintsEP6QSizeF(
    QQuickGridLayoutItem *self,
    QSizeF *sizeHints) {
  self->setCachedSizeHints(sizeHints);
}

//  QLayoutPolicy::Policy QQuickGridLayoutItem::sizePolicy(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickGridLayoutItem10sizePolicyEN2Qt11OrientationE(
    const QQuickGridLayoutItem *self,
    Qt::Orientation orientation) {
  return static_cast<int>(self->sizePolicy(orientation).toInt());
}

//  void QQuickGridLayoutItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGridLayoutItem11setGeometryERK6QRectF(
    QQuickGridLayoutItem *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QString QQuickGridLayoutItem::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickGridLayoutItem8toStringEv(
    const QQuickGridLayoutItem *self) {
  return new QString(self->toString());
}

//  QQuickItem *QQuickGridLayoutItem::layoutItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickGridLayoutItem10layoutItemEv(
    const QQuickGridLayoutItem *self) {
  return self->layoutItem();
}

//  QQuickGridLayoutItem::~QQuickGridLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGridLayoutItemD1Ev(QQuickGridLayoutItem *self) {
  delete self;
}

//  QSizeF QQuickGridLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK20QQuickGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QQuickGridLayoutItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      self->QQuickGridLayoutItem::sizeHint(
          which,
          *constraint));
}

//  QLayoutPolicy::Policy QQuickGridLayoutItem::sizePolicy(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QQuickGridLayoutItem10sizePolicyEN2Qt11OrientationE(
    const QQuickGridLayoutItem *self,
    Qt::Orientation orientation) {
  return static_cast<int>(
      self->QQuickGridLayoutItem::sizePolicy(
          orientation).toInt());
}

//  void QQuickGridLayoutItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickGridLayoutItem11setGeometryERK6QRectF(
    QQuickGridLayoutItem *self,
    const QRectF *rect) {
  self->QQuickGridLayoutItem::setGeometry(*rect);
}

//  QString QQuickGridLayoutItem::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QQuickGridLayoutItem8toStringEv(
    const QQuickGridLayoutItem *self) {
  return new QString(self->QQuickGridLayoutItem::toString());
}
