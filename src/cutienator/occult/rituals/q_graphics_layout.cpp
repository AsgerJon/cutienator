//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicslayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicslayout.h>

//  QGraphicsLayout::~QGraphicsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayoutD1Ev(QGraphicsLayout *self) {
  delete self;
}

//  void QGraphicsLayout::setContentsMargins(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout18setContentsMarginsEdddd(
    QGraphicsLayout *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QGraphicsLayout::getContentsMargins(qreal *left, qreal *top, qreal
//      *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsLayout18getContentsMarginsEPdS0_S0_S0_(
    const QGraphicsLayout *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  void QGraphicsLayout::activate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout8activateEv(QGraphicsLayout *self) {
  self->activate();
}

//  bool QGraphicsLayout::isActivated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsLayout11isActivatedEv(
    const QGraphicsLayout *self) {
  return self->isActivated();
}

//  void QGraphicsLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout10invalidateEv(QGraphicsLayout *self) {
  self->invalidate();
}

//  void QGraphicsLayout::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout14updateGeometryEv(QGraphicsLayout *self) {
  self->updateGeometry();
}

//  void QGraphicsLayout::widgetEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout11widgetEventEP6QEvent(
    QGraphicsLayout *self,
    QEvent *e) {
  self->widgetEvent(e);
}

//  int QGraphicsLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGraphicsLayout5countEv(const QGraphicsLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsLayout::itemAt(int i) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK15QGraphicsLayout6itemAtEi(
    const QGraphicsLayout *self,
    int i) {
  return self->itemAt(i);
}

//  void QGraphicsLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout8removeAtEi(
    QGraphicsLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsLayout::setInstantInvalidatePropagation(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout31setInstantInvalidatePropagationEb(
    bool enable) {
  QGraphicsLayout::setInstantInvalidatePropagation(enable);
}

//  bool QGraphicsLayout::instantInvalidatePropagation()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsLayout28instantInvalidatePropagationEv() {
  return QGraphicsLayout::instantInvalidatePropagation();
}
