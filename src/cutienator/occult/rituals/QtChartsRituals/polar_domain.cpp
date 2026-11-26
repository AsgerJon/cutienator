//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/polardomain_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/polardomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A PolarDomain that Python can take functions over in. Every PolarDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CutePolarDomainCall0)(const void *, const QSizeF *, int *);
typedef int (*CutePolarDomainCall1)(const void *, int *);
typedef void (*CutePolarDomainCall2)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CutePolarDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CutePolarDomainCall4)(const void *, const QRectF *, int *);
typedef void (*CutePolarDomainCall5)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CutePolarDomainCall6)(const void *, const QPointF *, int *);
typedef bool (*CutePolarDomainCall7)(const void *, QAbstractAxis *, int *);
typedef bool (*CutePolarDomainCall8)(const void *, QAbstractAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePolarDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePolarDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CutePolarDomain : public PolarDomain {
public:
  using PolarDomain::PolarDomain;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14AbstractDomain7setSizeERK6QSizeF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain8setRangeEdddd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain6zoomInERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7zoomOutERK6QRectF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain4moveEdd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14AbstractDomain20calculateDomainPointERK7QPointF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10attachAxisEP13QAbstractAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10detachAxisEP13QAbstractAxis")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void PolarDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[0]) {
      int handled = 0;
      CutePolarDomainCall0 call = reinterpret_cast<CutePolarDomainCall0>(taken[0]);
      call(this, &size, &handled);
      if (handled) return;
    }
    PolarDomain::setSize(size);
  }

  //  DomainType AbstractDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[1]) {
      int handled = 0;
      CutePolarDomainCall1 call = reinterpret_cast<CutePolarDomainCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return {};
  }

  //  void AbstractDomain::setRange(qreal minX, qreal maxX, qreal minY,
  //      qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[2]) {
      int handled = 0;
      CutePolarDomainCall2 call = reinterpret_cast<CutePolarDomainCall2>(taken[2]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
  }

  //  void AbstractDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CutePolarDomainCall3 call = reinterpret_cast<CutePolarDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void AbstractDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[4]) {
      int handled = 0;
      CutePolarDomainCall4 call = reinterpret_cast<CutePolarDomainCall4>(taken[4]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void AbstractDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[5]) {
      int handled = 0;
      CutePolarDomainCall5 call = reinterpret_cast<CutePolarDomainCall5>(taken[5]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
  }

  //  QPointF AbstractDomain::calculateDomainPoint(const QPointF &point)
  //      const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CutePolarDomainCall6 call = reinterpret_cast<CutePolarDomainCall6>(taken[6]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CutePolarDomainCall7 call = reinterpret_cast<CutePolarDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return AbstractDomain::attachAxis(axis);
  }

  //  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CutePolarDomainCall8 call = reinterpret_cast<CutePolarDomainCall8>(taken[8]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return AbstractDomain::detachAxis(axis);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CutePolarDomainCall9 call = reinterpret_cast<CutePolarDomainCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CutePolarDomainCall10 call = reinterpret_cast<CutePolarDomainCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CutePolarDomainCall11 call = reinterpret_cast<CutePolarDomainCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CutePolarDomainCall12 call = reinterpret_cast<CutePolarDomainCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CutePolarDomainCall13 call = reinterpret_cast<CutePolarDomainCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CutePolarDomainCall14 call = reinterpret_cast<CutePolarDomainCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CutePolarDomainCall15 call = reinterpret_cast<CutePolarDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *PolarDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11PolarDomain10metaObjectEv(
    const PolarDomain *self) {
  return self->metaObject();
}

//  void *PolarDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11PolarDomain11qt_metacastEPKc(
    PolarDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int PolarDomain::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11PolarDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    PolarDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString PolarDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11PolarDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(PolarDomain::tr(s, c, n));
}

//  PolarDomain::~PolarDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN11PolarDomainD1Ev(PolarDomain *self) {
  delete self;
}

//  void PolarDomain::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11PolarDomain7setSizeERK6QSizeF(
    PolarDomain *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  QPointF PolarDomain::calculateGeometryPoint(const QPointF &point, bool
//      &ok) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11PolarDomain22calculateGeometryPointERK7QPointFRb(
    const PolarDomain *self,
    const QPointF *point,
    bool *ok) {
  return new QPointF(self->calculateGeometryPoint(*point, *ok));
}

//  QList<QPointF> PolarDomain::calculateGeometryPoints(const QList<QPointF>
//      &list) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK11PolarDomain23calculateGeometryPointsERK5QListI7QPointFE(
    const PolarDomain *self,
    const QList<QPointF> *list) {
  return new QList<QPointF>(self->calculateGeometryPoints(*list));
}

//  qreal PolarDomain::toAngularCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11PolarDomain19toAngularCoordinateEdRb(
    const PolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toAngularCoordinate(value, *ok);
}

//  qreal PolarDomain::toRadialCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11PolarDomain18toRadialCoordinateEdRb(
    const PolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toRadialCoordinate(value, *ok);
}

//  QPointF PolarDomain::polarCoordinateToPoint(qreal angularCoordinate,
//      qreal radialCoordinate) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11PolarDomain22polarCoordinateToPointEdd(
    const PolarDomain *self,
    qreal angularCoordinate,
    qreal radialCoordinate) {
  return new QPointF(
      self->polarCoordinateToPoint(
          angularCoordinate,
          radialCoordinate));
}

//  a Python function taken by a CutePolarDomain, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PolarDomain(
    PolarDomain *self,
    const char *key,
    void *call) {
  return static_cast<CutePolarDomain *>(self)->take(key, call);
}

//  void PolarDomain::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11PolarDomain7setSizeERK6QSizeF(
    PolarDomain *self,
    const QSizeF *size) {
  self->PolarDomain::setSize(*size);
}
