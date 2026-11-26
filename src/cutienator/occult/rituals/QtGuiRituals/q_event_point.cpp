//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qeventpoint.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qpointingdevice.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>

//  QEventPoint::QEventPoint(int id, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN11QEventPointC1EiPK15QPointingDevice(
    int id,
    const QPointingDevice *device) {
  return new QEventPoint(id, device);
}

//  QEventPoint::QEventPoint(int pointId, State state, const QPointF
//      &scenePosition, const QPointF &globalPosition)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN11QEventPointC1EiNS_5StateERK7QPointFS3_(
    int pointId,
    QEventPoint::State state,
    const QPointF *scenePosition,
    const QPointF *globalPosition) {
  return new QEventPoint(pointId, state, *scenePosition, *globalPosition);
}

//  QEventPoint::QEventPoint(const QEventPoint &other)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN11QEventPointC1ERKS_(const QEventPoint *other) {
  return new QEventPoint(*other);
}

//  QEventPoint &QEventPoint::operator=(const QEventPoint &other)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN11QEventPointaSERKS_(
    QEventPoint *self,
    const QEventPoint *other) {
  return &(self->operator=(*other));
}

//  QEventPoint::QEventPoint(QEventPoint &&other)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN11QEventPointC1EOS_(QEventPoint *other) {
  return new QEventPoint(std::move(*other));
}

//  QEventPoint &QEventPoint::operator=(QEventPoint &&other)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN11QEventPointaSEOS_(
    QEventPoint *self,
    QEventPoint *other) {
  return &(self->operator=(std::move(*other)));
}

//  bool QEventPoint::operator==(const QEventPoint &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QEventPointeqERKS_(
    const QEventPoint *self,
    const QEventPoint *other) {
  return self->operator==(*other);
}

//  bool QEventPoint::operator!=(const QEventPoint &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QEventPointneERKS_(
    const QEventPoint *self,
    const QEventPoint *other) {
  return self->operator!=(*other);
}

//  QEventPoint::~QEventPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEventPointD1Ev(QEventPoint *self) {
  delete self;
}

//  void QEventPoint::swap(QEventPoint &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEventPoint4swapERS_(QEventPoint *self, QEventPoint *other) {
  self->swap(*other);
}

//  QPointF QEventPoint::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint8positionEv(const QEventPoint *self) {
  return new QPointF(self->position());
}

//  QPointF QEventPoint::pressPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint13pressPositionEv(const QEventPoint *self) {
  return new QPointF(self->pressPosition());
}

//  QPointF QEventPoint::grabPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint12grabPositionEv(const QEventPoint *self) {
  return new QPointF(self->grabPosition());
}

//  QPointF QEventPoint::lastPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint12lastPositionEv(const QEventPoint *self) {
  return new QPointF(self->lastPosition());
}

//  QPointF QEventPoint::scenePosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint13scenePositionEv(const QEventPoint *self) {
  return new QPointF(self->scenePosition());
}

//  QPointF QEventPoint::scenePressPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint18scenePressPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->scenePressPosition());
}

//  QPointF QEventPoint::sceneGrabPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint17sceneGrabPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->sceneGrabPosition());
}

//  QPointF QEventPoint::sceneLastPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint17sceneLastPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->sceneLastPosition());
}

//  QPointF QEventPoint::globalPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint14globalPositionEv(const QEventPoint *self) {
  return new QPointF(self->globalPosition());
}

//  QPointF QEventPoint::globalPressPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint19globalPressPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->globalPressPosition());
}

//  QPointF QEventPoint::globalGrabPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint18globalGrabPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->globalGrabPosition());
}

//  QPointF QEventPoint::globalLastPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint18globalLastPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->globalLastPosition());
}

//  QPointF QEventPoint::normalizedPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint18normalizedPositionEv(
    const QEventPoint *self) {
  return new QPointF(self->normalizedPosition());
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint3posEv(const QEventPoint *self) {
  return new QPointF(self->pos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::startPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint8startPosEv(const QEventPoint *self) {
  return new QPointF(self->startPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint8scenePosEv(const QEventPoint *self) {
  return new QPointF(self->scenePos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::startScenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint13startScenePosEv(const QEventPoint *self) {
  return new QPointF(self->startScenePos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint9screenPosEv(const QEventPoint *self) {
  return new QPointF(self->screenPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::startScreenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint14startScreenPosEv(const QEventPoint *self) {
  return new QPointF(self->startScreenPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::startNormalizedPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint18startNormalizedPosEv(
    const QEventPoint *self) {
  return new QPointF(self->startNormalizedPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::normalizedPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint13normalizedPosEv(const QEventPoint *self) {
  return new QPointF(self->normalizedPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::lastPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint7lastPosEv(const QEventPoint *self) {
  return new QPointF(self->lastPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::lastScenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint12lastScenePosEv(const QEventPoint *self) {
  return new QPointF(self->lastScenePos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::lastScreenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint13lastScreenPosEv(const QEventPoint *self) {
  return new QPointF(self->lastScreenPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QEventPoint::lastNormalizedPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEventPoint17lastNormalizedPosEv(
    const QEventPoint *self) {
  return new QPointF(self->lastNormalizedPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  QVector2D QEventPoint::velocity() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK11QEventPoint8velocityEv(const QEventPoint *self) {
  return new QVector2D(self->velocity());
}

//  State QEventPoint::state() const
extern "C" Q_DECL_EXPORT
QEventPoint::State ritual_ZNK11QEventPoint5stateEv(const QEventPoint *self) {
  return self->state();
}

//  const QPointingDevice *QEventPoint::device() const
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZNK11QEventPoint6deviceEv(
    const QEventPoint *self) {
  return self->device();
}

//  int QEventPoint::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEventPoint2idEv(const QEventPoint *self) {
  return self->id();
}

//  QPointingDeviceUniqueId QEventPoint::uniqueId() const
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZNK11QEventPoint8uniqueIdEv(
    const QEventPoint *self) {
  return new QPointingDeviceUniqueId(self->uniqueId());
}

//  ulong QEventPoint::timestamp() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK11QEventPoint9timestampEv(const QEventPoint *self) {
  return self->timestamp();
}

//  ulong QEventPoint::lastTimestamp() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK11QEventPoint13lastTimestampEv(const QEventPoint *self) {
  return self->lastTimestamp();
}

//  ulong QEventPoint::pressTimestamp() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK11QEventPoint14pressTimestampEv(const QEventPoint *self) {
  return self->pressTimestamp();
}

//  qreal QEventPoint::timeHeld() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QEventPoint8timeHeldEv(const QEventPoint *self) {
  return self->timeHeld();
}

//  qreal QEventPoint::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QEventPoint8pressureEv(const QEventPoint *self) {
  return self->pressure();
}

//  qreal QEventPoint::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QEventPoint8rotationEv(const QEventPoint *self) {
  return self->rotation();
}

//  QSizeF QEventPoint::ellipseDiameters() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK11QEventPoint16ellipseDiametersEv(
    const QEventPoint *self) {
  return new QSizeF(self->ellipseDiameters());
}

//  bool QEventPoint::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QEventPoint10isAcceptedEv(const QEventPoint *self) {
  return self->isAccepted();
}

//  void QEventPoint::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEventPoint11setAcceptedEb(
    QEventPoint *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QList<QEventPoint>::QList()
extern "C" Q_DECL_EXPORT
QList<QEventPoint> *ritual_list_make_QEventPoint() {
  return new QList<QEventPoint>();
}

//  void QList<QEventPoint>::append(const QEventPoint &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QEventPoint(
    QList<QEventPoint> *self,
    const QEventPoint *element) {
  self->append(*element);
}

//  qsizetype QList<QEventPoint>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QEventPoint(const QList<QEventPoint> *self) {
  return self->size();
}

//  const QEventPoint &QList<QEventPoint>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_list_at_QEventPoint(
    const QList<QEventPoint> *self,
    long long index) {
  return new QEventPoint(self->at(index));
}

//  QList<QEventPoint>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QEventPoint(QList<QEventPoint> *self) {
  delete self;
}
