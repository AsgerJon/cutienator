//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qbardataitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qbardataitem.h>

//  QBarDataItem::QBarDataItem()
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1Ev() {
  return new QBarDataItem();
}

//  QBarDataItem::QBarDataItem(float value)
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1Ef(float value) {
  return new QBarDataItem(value);
}

//  QBarDataItem::QBarDataItem(float value, float angle)
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1Eff(float value, float angle) {
  return new QBarDataItem(value, angle);
}

//  QBarDataItem::QBarDataItem(const QBarDataItem &other)
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1ERKS_(const QBarDataItem *other) {
  return new QBarDataItem(*other);
}

//  QBarDataItem::~QBarDataItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItemD1Ev(QBarDataItem *self) {
  delete self;
}

//  void QBarDataItem::setValue(float val)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItem8setValueEf(QBarDataItem *self, float val) {
  self->setValue(val);
}

//  float QBarDataItem::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QBarDataItem5valueEv(const QBarDataItem *self) {
  return self->value();
}

//  void QBarDataItem::setRotation(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItem11setRotationEf(
    QBarDataItem *self,
    float angle) {
  self->setRotation(angle);
}

//  float QBarDataItem::rotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QBarDataItem8rotationEv(const QBarDataItem *self) {
  return self->rotation();
}

//  void QBarDataItem::createExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItem15createExtraDataEv(QBarDataItem *self) {
  self->createExtraData();
}
