//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qdeclarativeposition_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativeposition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeopositioninfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtPositioning/QGeoCoordinate>
#include <QtCore/QDateTime>

//  A QDeclarativePosition that Python can take functions over in. Every QDeclarativePosition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePositionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePositionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativePosition : public QDeclarativePosition {
public:
  using QDeclarativePosition::QDeclarativePosition;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePositionCall0 call = reinterpret_cast<CuteQDeclarativePositionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePositionCall1 call = reinterpret_cast<CuteQDeclarativePositionCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePositionCall2 call = reinterpret_cast<CuteQDeclarativePositionCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePositionCall3 call = reinterpret_cast<CuteQDeclarativePositionCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePositionCall4 call = reinterpret_cast<CuteQDeclarativePositionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePositionCall5 call = reinterpret_cast<CuteQDeclarativePositionCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePositionCall6 call = reinterpret_cast<CuteQDeclarativePositionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativePosition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QDeclarativePosition10metaObjectEv(
    const QDeclarativePosition *self) {
  return self->metaObject();
}

//  void *QDeclarativePosition::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QDeclarativePosition11qt_metacastEPKc(
    QDeclarativePosition *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativePosition::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QDeclarativePosition11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativePosition *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativePosition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDeclarativePosition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativePosition::tr(s, c, n));
}

//  QDeclarativePosition::QDeclarativePosition(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativePosition *ritual_ZN20QDeclarativePositionC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativePosition(parent);
}

//  QDeclarativePosition::~QDeclarativePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativePositionD1Ev(QDeclarativePosition *self) {
  delete self;
}

//  bool QDeclarativePosition::isLatitudeValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition15isLatitudeValidEv(
    const QDeclarativePosition *self) {
  return self->isLatitudeValid();
}

//  bool QDeclarativePosition::isLongitudeValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition16isLongitudeValidEv(
    const QDeclarativePosition *self) {
  return self->isLongitudeValid();
}

//  bool QDeclarativePosition::isAltitudeValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition15isAltitudeValidEv(
    const QDeclarativePosition *self) {
  return self->isAltitudeValid();
}

//  QDateTime QDeclarativePosition::timestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QDeclarativePosition9timestampEv(
    const QDeclarativePosition *self) {
  return new QDateTime(self->timestamp());
}

//  double QDeclarativePosition::speed() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition5speedEv(
    const QDeclarativePosition *self) {
  return self->speed();
}

//  bool QDeclarativePosition::isSpeedValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition12isSpeedValidEv(
    const QDeclarativePosition *self) {
  return self->isSpeedValid();
}

//  QGeoCoordinate QDeclarativePosition::coordinate() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK20QDeclarativePosition10coordinateEv(
    const QDeclarativePosition *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  bool QDeclarativePosition::isHorizontalAccuracyValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition25isHorizontalAccuracyValidEv(
    const QDeclarativePosition *self) {
  return self->isHorizontalAccuracyValid();
}

//  qreal QDeclarativePosition::horizontalAccuracy() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QDeclarativePosition18horizontalAccuracyEv(
    const QDeclarativePosition *self) {
  return self->horizontalAccuracy();
}

//  bool QDeclarativePosition::isVerticalAccuracyValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition23isVerticalAccuracyValidEv(
    const QDeclarativePosition *self) {
  return self->isVerticalAccuracyValid();
}

//  qreal QDeclarativePosition::verticalAccuracy() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QDeclarativePosition16verticalAccuracyEv(
    const QDeclarativePosition *self) {
  return self->verticalAccuracy();
}

//  bool QDeclarativePosition::isDirectionValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition16isDirectionValidEv(
    const QDeclarativePosition *self) {
  return self->isDirectionValid();
}

//  double QDeclarativePosition::direction() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition9directionEv(
    const QDeclarativePosition *self) {
  return self->direction();
}

//  bool QDeclarativePosition::isVerticalSpeedValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition20isVerticalSpeedValidEv(
    const QDeclarativePosition *self) {
  return self->isVerticalSpeedValid();
}

//  double QDeclarativePosition::verticalSpeed() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition13verticalSpeedEv(
    const QDeclarativePosition *self) {
  return self->verticalSpeed();
}

//  bool QDeclarativePosition::isMagneticVariationValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition24isMagneticVariationValidEv(
    const QDeclarativePosition *self) {
  return self->isMagneticVariationValid();
}

//  double QDeclarativePosition::magneticVariation() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition17magneticVariationEv(
    const QDeclarativePosition *self) {
  return self->magneticVariation();
}

//  void QDeclarativePosition::setPosition(const QGeoPositionInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativePosition11setPositionERK16QGeoPositionInfo(
    QDeclarativePosition *self,
    const QGeoPositionInfo *info) {
  self->setPosition(*info);
}

//  const QGeoPositionInfo &QDeclarativePosition::position() const
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_ZNK20QDeclarativePosition8positionEv(
    const QDeclarativePosition *self) {
  return new QGeoPositionInfo(self->position());
}

//  bool QDeclarativePosition::isDirectionAccuracyValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition24isDirectionAccuracyValidEv(
    const QDeclarativePosition *self) {
  return self->isDirectionAccuracyValid();
}

//  double QDeclarativePosition::directionAccuracy() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition17directionAccuracyEv(
    const QDeclarativePosition *self) {
  return self->directionAccuracy();
}

//  QBindable<bool> QDeclarativePosition::bindableLatitudeValid() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition21bindableLatitudeValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableLatitudeValid());
}

//  QBindable<bool> QDeclarativePosition::bindableLongitudeValid() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition22bindableLongitudeValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableLongitudeValid());
}

//  QBindable<bool> QDeclarativePosition::bindableAltitudeValid() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition21bindableAltitudeValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableAltitudeValid());
}

//  QBindable<QGeoCoordinate> QDeclarativePosition::bindableCoordinate()
//      const
extern "C" Q_DECL_EXPORT
QBindable<QGeoCoordinate> *ritual_ZNK20QDeclarativePosition18bindableCoordinateEv(
    const QDeclarativePosition *self) {
  return new QBindable<QGeoCoordinate>(self->bindableCoordinate());
}

//  QBindable<QDateTime> QDeclarativePosition::bindableTimestamp() const
extern "C" Q_DECL_EXPORT
QBindable<QDateTime> *ritual_ZNK20QDeclarativePosition17bindableTimestampEv(
    const QDeclarativePosition *self) {
  return new QBindable<QDateTime>(self->bindableTimestamp());
}

//  QBindable<double> QDeclarativePosition::bindableSpeed() const
extern "C" Q_DECL_EXPORT
QBindable<double> *ritual_ZNK20QDeclarativePosition13bindableSpeedEv(
    const QDeclarativePosition *self) {
  return new QBindable<double>(self->bindableSpeed());
}

//  QBindable<bool> QDeclarativePosition::bindableSpeedValid() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition18bindableSpeedValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableSpeedValid());
}

//  QBindable<qreal> QDeclarativePosition::bindableHorizontalAccuracy() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK20QDeclarativePosition26bindableHorizontalAccuracyEv(
    const QDeclarativePosition *self) {
  return new QBindable<qreal>(self->bindableHorizontalAccuracy());
}

//  QBindable<qreal> QDeclarativePosition::binableVerticalAccuracy() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK20QDeclarativePosition23binableVerticalAccuracyEv(
    const QDeclarativePosition *self) {
  return new QBindable<qreal>(self->binableVerticalAccuracy());
}

//  QBindable<bool> QDeclarativePosition::bindableHorizontalAccuracyValid()
//      const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition31bindableHorizontalAccuracyValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableHorizontalAccuracyValid());
}

//  QBindable<bool> QDeclarativePosition::bindableVerticalAccuracyValid()
//      const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition29bindableVerticalAccuracyValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableVerticalAccuracyValid());
}

//  QBindable<bool> QDeclarativePosition::bindableDirectionValid() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition22bindableDirectionValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableDirectionValid());
}

//  QBindable<double> QDeclarativePosition::bindableDirection() const
extern "C" Q_DECL_EXPORT
QBindable<double> *ritual_ZNK20QDeclarativePosition17bindableDirectionEv(
    const QDeclarativePosition *self) {
  return new QBindable<double>(self->bindableDirection());
}

//  QBindable<bool> QDeclarativePosition::bindableVerticalSpeedValid() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition26bindableVerticalSpeedValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableVerticalSpeedValid());
}

//  QBindable<double> QDeclarativePosition::bindableVerticalSpeed() const
extern "C" Q_DECL_EXPORT
QBindable<double> *ritual_ZNK20QDeclarativePosition21bindableVerticalSpeedEv(
    const QDeclarativePosition *self) {
  return new QBindable<double>(self->bindableVerticalSpeed());
}

//  QBindable<double> QDeclarativePosition::bindableMagneticVariation() const
extern "C" Q_DECL_EXPORT
QBindable<double> *ritual_ZNK20QDeclarativePosition25bindableMagneticVariationEv(
    const QDeclarativePosition *self) {
  return new QBindable<double>(self->bindableMagneticVariation());
}

//  QBindable<bool> QDeclarativePosition::bindableMagneticVariationValid()
//      const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition30bindableMagneticVariationValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableMagneticVariationValid());
}

//  QBindable<double> QDeclarativePosition::bindableDirectionAccuracy() const
extern "C" Q_DECL_EXPORT
QBindable<double> *ritual_ZNK20QDeclarativePosition25bindableDirectionAccuracyEv(
    const QDeclarativePosition *self) {
  return new QBindable<double>(self->bindableDirectionAccuracy());
}

//  QBindable<bool> QDeclarativePosition::bindableDirectionAccuracyValid()
//      const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK20QDeclarativePosition30bindableDirectionAccuracyValidEv(
    const QDeclarativePosition *self) {
  return new QBindable<bool>(self->bindableDirectionAccuracyValid());
}

//  bool QDeclarativePosition::isLatitudeValidActualCalculation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition32isLatitudeValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isLatitudeValidActualCalculation();
}

//  bool QDeclarativePosition::isLongitudeValidActualCalculation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition33isLongitudeValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isLongitudeValidActualCalculation();
}

//  bool QDeclarativePosition::isAltitudeValidActualCalculation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition32isAltitudeValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isAltitudeValidActualCalculation();
}

//  QGeoCoordinate QDeclarativePosition::coordinateActualCalculation() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK20QDeclarativePosition27coordinateActualCalculationEv(
    const QDeclarativePosition *self) {
  return new QGeoCoordinate(self->coordinateActualCalculation());
}

//  QDateTime QDeclarativePosition::timestampActualCalculation() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QDeclarativePosition26timestampActualCalculationEv(
    const QDeclarativePosition *self) {
  return new QDateTime(self->timestampActualCalculation());
}

//  double QDeclarativePosition::speedActualCalculation() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition22speedActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->speedActualCalculation();
}

//  bool QDeclarativePosition::isSpeedValidActualCalculation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition29isSpeedValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isSpeedValidActualCalculation();
}

//  qreal QDeclarativePosition::horizontalAccuracyActualCalculation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QDeclarativePosition35horizontalAccuracyActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->horizontalAccuracyActualCalculation();
}

//  qreal QDeclarativePosition::verticalAccuracyActualCalculation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QDeclarativePosition33verticalAccuracyActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->verticalAccuracyActualCalculation();
}

//  bool QDeclarativePosition::isHorizontalAccuracyValidActualCalculation()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition42isHorizontalAccuracyValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isHorizontalAccuracyValidActualCalculation();
}

//  bool QDeclarativePosition::isVerticalAccuracyValidActualCalculation()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition40isVerticalAccuracyValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isVerticalAccuracyValidActualCalculation();
}

//  bool QDeclarativePosition::isDirectionValidActualCalculation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition33isDirectionValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isDirectionValidActualCalculation();
}

//  double QDeclarativePosition::directionActualCalculation() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition26directionActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->directionActualCalculation();
}

//  bool QDeclarativePosition::isVerticalSpeedValidActualCalculation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition37isVerticalSpeedValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isVerticalSpeedValidActualCalculation();
}

//  double QDeclarativePosition::verticalSpeedActualCalculation() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition30verticalSpeedActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->verticalSpeedActualCalculation();
}

//  double QDeclarativePosition::magneticVariationActualCalculation() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition34magneticVariationActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->magneticVariationActualCalculation();
}

//  bool QDeclarativePosition::isMagneticVariationValidActualCalculation()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition41isMagneticVariationValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isMagneticVariationValidActualCalculation();
}

//  double QDeclarativePosition::directionAccuracyActualCalculation() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK20QDeclarativePosition34directionAccuracyActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->directionAccuracyActualCalculation();
}

//  bool QDeclarativePosition::isDirectionAccuracyValidActualCalculation()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDeclarativePosition41isDirectionAccuracyValidActualCalculationEv(
    const QDeclarativePosition *self) {
  return self->isDirectionAccuracyValidActualCalculation();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedLatitudeValid_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition43_qt_property_m_computedLatitudeValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedLatitudeValid_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedLongitudeValid_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition44_qt_property_m_computedLongitudeValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedLongitudeValid_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedAltitudeValid_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition43_qt_property_m_computedAltitudeValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedAltitudeValid_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedCoordinate_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition40_qt_property_m_computedCoordinate_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedCoordinate_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedTimestamp_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition39_qt_property_m_computedTimestamp_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedTimestamp_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedSpeed_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition35_qt_property_m_computedSpeed_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedSpeed_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedSpeedValid_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition40_qt_property_m_computedSpeedValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedSpeedValid_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedHorizontalAccuracy_offse
//      t()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition48_qt_property_m_computedHorizontalAccuracy_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedHorizontalAccuracy_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedVerticalAccuracy_offset(
//      )
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition46_qt_property_m_computedVerticalAccuracy_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedVerticalAccuracy_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedHorizontalAccuracyVal
//      id_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition53_qt_property_m_computedHorizontalAccuracyValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedHorizontalAccuracyValid_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedVerticalAccuracyValid
//      _offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition51_qt_property_m_computedVerticalAccuracyValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedVerticalAccuracyValid_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedDirectionValid_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition44_qt_property_m_computedDirectionValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedDirectionValid_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedDirection_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition39_qt_property_m_computedDirection_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedDirection_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedVerticalSpeedValid_offse
//      t()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition48_qt_property_m_computedVerticalSpeedValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedVerticalSpeedValid_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedVerticalSpeed_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition43_qt_property_m_computedVerticalSpeed_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedVerticalSpeed_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedMagneticVariation_offset
//      ()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition47_qt_property_m_computedMagneticVariation_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedMagneticVariation_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedMagneticVariationVali
//      d_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition52_qt_property_m_computedMagneticVariationValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedMagneticVariationValid_offset();
}

//  size_t
//      QDeclarativePosition::_qt_property_m_computedDirectionAccuracy_offset
//      ()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition47_qt_property_m_computedDirectionAccuracy_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedDirectionAccuracy_offset();
}

//  size_t QDeclarativePosition::_qt_property_m_computedDirectionAccuracyVali
//      d_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QDeclarativePosition52_qt_property_m_computedDirectionAccuracyValid_offsetEv() {
  return QDeclarativePosition::_qt_property_m_computedDirectionAccuracyValid_offset();
}

//  a Python function taken by a CuteQDeclarativePosition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePosition(
    QDeclarativePosition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePosition *>(self)->take(key, call);
}

//  a QBindable<bool> a ritual of QDeclarativePosition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativePosition__QBindable_bool(
    QBindable<bool> *self) {
  delete self;
}

//  a QBindable<QGeoCoordinate> a ritual of QDeclarativePosition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativePosition__QBindable_QGeoCoordinate(
    QBindable<QGeoCoordinate> *self) {
  delete self;
}

//  a QBindable<QDateTime> a ritual of QDeclarativePosition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativePosition__QBindable_QDateTime(
    QBindable<QDateTime> *self) {
  delete self;
}

//  a QBindable<double> a ritual of QDeclarativePosition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativePosition__QBindable_double(
    QBindable<double> *self) {
  delete self;
}

//  a QBindable<qreal> a ritual of QDeclarativePosition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativePosition__QBindable_qreal(
    QBindable<qreal> *self) {
  delete self;
}
