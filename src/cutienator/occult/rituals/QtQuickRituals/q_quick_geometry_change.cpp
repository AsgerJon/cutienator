//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickGeometryChange::QQuickGeometryChange(int change)
extern "C" Q_DECL_EXPORT
QQuickGeometryChange *ritual_ZN20QQuickGeometryChangeC1Ei(int change) {
  return new QQuickGeometryChange(change);
}

//  bool QQuickGeometryChange::noChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange8noChangeEv(
    const QQuickGeometryChange *self) {
  return self->noChange();
}

//  bool QQuickGeometryChange::anyChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange9anyChangeEv(
    const QQuickGeometryChange *self) {
  return self->anyChange();
}

//  bool QQuickGeometryChange::xChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange7xChangeEv(
    const QQuickGeometryChange *self) {
  return self->xChange();
}

//  bool QQuickGeometryChange::yChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange7yChangeEv(
    const QQuickGeometryChange *self) {
  return self->yChange();
}

//  bool QQuickGeometryChange::widthChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange11widthChangeEv(
    const QQuickGeometryChange *self) {
  return self->widthChange();
}

//  bool QQuickGeometryChange::heightChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange12heightChangeEv(
    const QQuickGeometryChange *self) {
  return self->heightChange();
}

//  bool QQuickGeometryChange::positionChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange14positionChangeEv(
    const QQuickGeometryChange *self) {
  return self->positionChange();
}

//  bool QQuickGeometryChange::sizeChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange10sizeChangeEv(
    const QQuickGeometryChange *self) {
  return self->sizeChange();
}

//  bool QQuickGeometryChange::horizontalChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange16horizontalChangeEv(
    const QQuickGeometryChange *self) {
  return self->horizontalChange();
}

//  bool QQuickGeometryChange::verticalChange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange14verticalChangeEv(
    const QQuickGeometryChange *self) {
  return self->verticalChange();
}

//  void QQuickGeometryChange::setXChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange10setXChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setXChange(enabled);
}

//  void QQuickGeometryChange::setYChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange10setYChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setYChange(enabled);
}

//  void QQuickGeometryChange::setWidthChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange14setWidthChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setWidthChange(enabled);
}

//  void QQuickGeometryChange::setHeightChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange15setHeightChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setHeightChange(enabled);
}

//  void QQuickGeometryChange::setSizeChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange13setSizeChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setSizeChange(enabled);
}

//  void QQuickGeometryChange::setAllChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange13setAllChangedEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setAllChanged(enabled);
}

//  void QQuickGeometryChange::setHorizontalChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange19setHorizontalChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setHorizontalChange(enabled);
}

//  void QQuickGeometryChange::setVerticalChange(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange17setVerticalChangeEb(
    QQuickGeometryChange *self,
    bool enabled) {
  self->setVerticalChange(enabled);
}

//  void QQuickGeometryChange::set(int bits, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChange3setEib(
    QQuickGeometryChange *self,
    int bits,
    bool enabled) {
  self->set(bits, enabled);
}

//  bool QQuickGeometryChange::matches(QQuickGeometryChange other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickGeometryChange7matchesES_(
    const QQuickGeometryChange *self,
    const QQuickGeometryChange *other) {
  return self->matches(*other);
}

//  QQuickGeometryChange::~QQuickGeometryChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickGeometryChangeD1Ev(QQuickGeometryChange *self) {
  delete self;
}
