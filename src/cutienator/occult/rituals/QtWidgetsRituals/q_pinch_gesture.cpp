//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QPinchGesture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPinchGesture10metaObjectEv(
    const QPinchGesture *self) {
  return self->metaObject();
}

//  QString QPinchGesture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPinchGesture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPinchGesture::tr(s, c, n));
}

//  QPinchGesture::QPinchGesture(QObject *parent)
extern "C" Q_DECL_EXPORT
QPinchGesture *ritual_ZN13QPinchGestureC1EP7QObject(QObject *parent) {
  return new QPinchGesture(parent);
}

//  QPinchGesture::~QPinchGesture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGestureD1Ev(QPinchGesture *self) {
  delete self;
}

//  ChangeFlags QPinchGesture::totalChangeFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPinchGesture16totalChangeFlagsEv(
    const QPinchGesture *self) {
  return static_cast<int>(self->totalChangeFlags().toInt());
}

//  void QPinchGesture::setTotalChangeFlags(ChangeFlags value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture19setTotalChangeFlagsE6QFlagsINS_10ChangeFlagEE(
    QPinchGesture *self,
    int value) {
  self->setTotalChangeFlags(
      QFlags<QPinchGesture::ChangeFlag>::fromInt(value));
}

//  ChangeFlags QPinchGesture::changeFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPinchGesture11changeFlagsEv(const QPinchGesture *self) {
  return static_cast<int>(self->changeFlags().toInt());
}

//  void QPinchGesture::setChangeFlags(ChangeFlags value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture14setChangeFlagsE6QFlagsINS_10ChangeFlagEE(
    QPinchGesture *self,
    int value) {
  self->setChangeFlags(QFlags<QPinchGesture::ChangeFlag>::fromInt(value));
}

//  QPointF QPinchGesture::startCenterPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPinchGesture16startCenterPointEv(
    const QPinchGesture *self) {
  return new QPointF(self->startCenterPoint());
}

//  QPointF QPinchGesture::lastCenterPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPinchGesture15lastCenterPointEv(
    const QPinchGesture *self) {
  return new QPointF(self->lastCenterPoint());
}

//  QPointF QPinchGesture::centerPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPinchGesture11centerPointEv(
    const QPinchGesture *self) {
  return new QPointF(self->centerPoint());
}

//  void QPinchGesture::setStartCenterPoint(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture19setStartCenterPointERK7QPointF(
    QPinchGesture *self,
    const QPointF *value) {
  self->setStartCenterPoint(*value);
}

//  void QPinchGesture::setLastCenterPoint(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture18setLastCenterPointERK7QPointF(
    QPinchGesture *self,
    const QPointF *value) {
  self->setLastCenterPoint(*value);
}

//  void QPinchGesture::setCenterPoint(const QPointF &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture14setCenterPointERK7QPointF(
    QPinchGesture *self,
    const QPointF *value) {
  self->setCenterPoint(*value);
}

//  qreal QPinchGesture::totalScaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture16totalScaleFactorEv(
    const QPinchGesture *self) {
  return self->totalScaleFactor();
}

//  qreal QPinchGesture::lastScaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture15lastScaleFactorEv(
    const QPinchGesture *self) {
  return self->lastScaleFactor();
}

//  qreal QPinchGesture::scaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture11scaleFactorEv(const QPinchGesture *self) {
  return self->scaleFactor();
}

//  void QPinchGesture::setTotalScaleFactor(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture19setTotalScaleFactorEd(
    QPinchGesture *self,
    qreal value) {
  self->setTotalScaleFactor(value);
}

//  void QPinchGesture::setLastScaleFactor(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture18setLastScaleFactorEd(
    QPinchGesture *self,
    qreal value) {
  self->setLastScaleFactor(value);
}

//  void QPinchGesture::setScaleFactor(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture14setScaleFactorEd(
    QPinchGesture *self,
    qreal value) {
  self->setScaleFactor(value);
}

//  qreal QPinchGesture::totalRotationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture18totalRotationAngleEv(
    const QPinchGesture *self) {
  return self->totalRotationAngle();
}

//  qreal QPinchGesture::lastRotationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture17lastRotationAngleEv(
    const QPinchGesture *self) {
  return self->lastRotationAngle();
}

//  qreal QPinchGesture::rotationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPinchGesture13rotationAngleEv(const QPinchGesture *self) {
  return self->rotationAngle();
}

//  void QPinchGesture::setTotalRotationAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture21setTotalRotationAngleEd(
    QPinchGesture *self,
    qreal value) {
  self->setTotalRotationAngle(value);
}

//  void QPinchGesture::setLastRotationAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture20setLastRotationAngleEd(
    QPinchGesture *self,
    qreal value) {
  self->setLastRotationAngle(value);
}

//  void QPinchGesture::setRotationAngle(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPinchGesture16setRotationAngleEd(
    QPinchGesture *self,
    qreal value) {
  self->setRotationAngle(value);
}
