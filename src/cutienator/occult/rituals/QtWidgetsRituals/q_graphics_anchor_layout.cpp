//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsanchorlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsanchorlayout.h>
#include <QtCore/qrect.h>

//  QGraphicsAnchorLayout::QGraphicsAnchorLayout(QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayout *ritual_ZN21QGraphicsAnchorLayoutC1EP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *parent) {
  return new QGraphicsAnchorLayout(parent);
}

//  QGraphicsAnchorLayout::~QGraphicsAnchorLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayoutD1Ev(QGraphicsAnchorLayout *self) {
  delete self;
}

//  QGraphicsAnchor *QGraphicsAnchorLayout::addAnchor(QGraphicsLayoutItem
//      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
//      *secondItem, Qt::AnchorPoint secondEdge)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN21QGraphicsAnchorLayout9addAnchorEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge,
    QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge) {
  return self->addAnchor(firstItem, firstEdge, secondItem, secondEdge);
}

//  QGraphicsAnchor *QGraphicsAnchorLayout::anchor(QGraphicsLayoutItem
//      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
//      *secondItem, Qt::AnchorPoint secondEdge)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN21QGraphicsAnchorLayout6anchorEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge,
    QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge) {
  return self->anchor(firstItem, firstEdge, secondItem, secondEdge);
}

//  void QGraphicsAnchorLayout::addCornerAnchors(QGraphicsLayoutItem
//      *firstItem, Qt::Corner firstCorner, QGraphicsLayoutItem *secondItem,
//      Qt::Corner secondCorner)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout16addCornerAnchorsEP19QGraphicsLayoutItemN2Qt6CornerES1_S3_(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    Qt::Corner firstCorner,
    QGraphicsLayoutItem *secondItem,
    Qt::Corner secondCorner) {
  self->addCornerAnchors(firstItem, firstCorner, secondItem, secondCorner);
}

//  void QGraphicsAnchorLayout::addAnchors(QGraphicsLayoutItem *firstItem,
//      QGraphicsLayoutItem *secondItem, Qt::Orientations orientations)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout10addAnchorsEP19QGraphicsLayoutItemS1_6QFlagsIN2Qt11OrientationEE(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    QGraphicsLayoutItem *secondItem,
    int orientations) {
  self->addAnchors(
      firstItem,
      secondItem,
      QFlags<Qt::Orientation>::fromInt(orientations));
}

//  void QGraphicsAnchorLayout::setHorizontalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout20setHorizontalSpacingEd(
    QGraphicsAnchorLayout *self,
    qreal spacing) {
  self->setHorizontalSpacing(spacing);
}

//  void QGraphicsAnchorLayout::setVerticalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout18setVerticalSpacingEd(
    QGraphicsAnchorLayout *self,
    qreal spacing) {
  self->setVerticalSpacing(spacing);
}

//  void QGraphicsAnchorLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout10setSpacingEd(
    QGraphicsAnchorLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  qreal QGraphicsAnchorLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsAnchorLayout17horizontalSpacingEv(
    const QGraphicsAnchorLayout *self) {
  return self->horizontalSpacing();
}

//  qreal QGraphicsAnchorLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsAnchorLayout15verticalSpacingEv(
    const QGraphicsAnchorLayout *self) {
  return self->verticalSpacing();
}

//  void QGraphicsAnchorLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout8removeAtEi(
    QGraphicsAnchorLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsAnchorLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout11setGeometryERK6QRectF(
    QGraphicsAnchorLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  int QGraphicsAnchorLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsAnchorLayout5countEv(
    const QGraphicsAnchorLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsAnchorLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK21QGraphicsAnchorLayout6itemAtEi(
    const QGraphicsAnchorLayout *self,
    int index) {
  return self->itemAt(index);
}

//  void QGraphicsAnchorLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout10invalidateEv(
    QGraphicsAnchorLayout *self) {
  self->invalidate();
}
