//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicslinearlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicslinearlayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QGraphicsLinearLayout::QGraphicsLinearLayout(QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLinearLayout *ritual_ZN21QGraphicsLinearLayoutC1EP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *parent) {
  return new QGraphicsLinearLayout(parent);
}

//  QGraphicsLinearLayout::QGraphicsLinearLayout(Qt::Orientation orientation,
//      QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLinearLayout *ritual_ZN21QGraphicsLinearLayoutC1EN2Qt11OrientationEP19QGraphicsLayoutItem(
    Qt::Orientation orientation,
    QGraphicsLayoutItem *parent) {
  return new QGraphicsLinearLayout(orientation, parent);
}

//  QGraphicsLinearLayout::~QGraphicsLinearLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayoutD1Ev(QGraphicsLinearLayout *self) {
  delete self;
}

//  void QGraphicsLinearLayout::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout14setOrientationEN2Qt11OrientationE(
    QGraphicsLinearLayout *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::Orientation QGraphicsLinearLayout::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK21QGraphicsLinearLayout11orientationEv(
    const QGraphicsLinearLayout *self) {
  return self->orientation();
}

//  void QGraphicsLinearLayout::addItem(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout7addItemEP19QGraphicsLayoutItem(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  self->addItem(item);
}

//  void QGraphicsLinearLayout::addStretch(int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10addStretchEi(
    QGraphicsLinearLayout *self,
    int stretch) {
  self->addStretch(stretch);
}

//  void QGraphicsLinearLayout::insertItem(int index, QGraphicsLayoutItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10insertItemEiP19QGraphicsLayoutItem(
    QGraphicsLinearLayout *self,
    int index,
    QGraphicsLayoutItem *item) {
  self->insertItem(index, item);
}

//  void QGraphicsLinearLayout::insertStretch(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout13insertStretchEii(
    QGraphicsLinearLayout *self,
    int index,
    int stretch) {
  self->insertStretch(index, stretch);
}

//  void QGraphicsLinearLayout::removeItem(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10removeItemEP19QGraphicsLayoutItem(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  self->removeItem(item);
}

//  void QGraphicsLinearLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout8removeAtEi(
    QGraphicsLinearLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsLinearLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10setSpacingEd(
    QGraphicsLinearLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  qreal QGraphicsLinearLayout::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsLinearLayout7spacingEv(
    const QGraphicsLinearLayout *self) {
  return self->spacing();
}

//  void QGraphicsLinearLayout::setItemSpacing(int index, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout14setItemSpacingEid(
    QGraphicsLinearLayout *self,
    int index,
    qreal spacing) {
  self->setItemSpacing(index, spacing);
}

//  qreal QGraphicsLinearLayout::itemSpacing(int index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsLinearLayout11itemSpacingEi(
    const QGraphicsLinearLayout *self,
    int index) {
  return self->itemSpacing(index);
}

//  void QGraphicsLinearLayout::setStretchFactor(QGraphicsLayoutItem *item,
//      int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout16setStretchFactorEP19QGraphicsLayoutItemi(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item,
    int stretch) {
  self->setStretchFactor(item, stretch);
}

//  int QGraphicsLinearLayout::stretchFactor(QGraphicsLayoutItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsLinearLayout13stretchFactorEP19QGraphicsLayoutItem(
    const QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  return self->stretchFactor(item);
}

//  void QGraphicsLinearLayout::setAlignment(QGraphicsLayoutItem *item,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout12setAlignmentEP19QGraphicsLayoutItem6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item,
    int alignment) {
  self->setAlignment(item, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsLinearLayout::alignment(QGraphicsLayoutItem *item)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsLinearLayout9alignmentEP19QGraphicsLayoutItem(
    const QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  return static_cast<int>(self->alignment(item).toInt());
}

//  void QGraphicsLinearLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout11setGeometryERK6QRectF(
    QGraphicsLinearLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  int QGraphicsLinearLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsLinearLayout5countEv(
    const QGraphicsLinearLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsLinearLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK21QGraphicsLinearLayout6itemAtEi(
    const QGraphicsLinearLayout *self,
    int index) {
  return self->itemAt(index);
}

//  void QGraphicsLinearLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10invalidateEv(
    QGraphicsLinearLayout *self) {
  self->invalidate();
}

//  QSizeF QGraphicsLinearLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK21QGraphicsLinearLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsLinearLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void QGraphicsLinearLayout::dump(int indent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QGraphicsLinearLayout4dumpEi(
    const QGraphicsLinearLayout *self,
    int indent) {
  self->dump(indent);
}
