//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/xydomain_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/xydomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A XYDomain that Python can take functions over in. Every XYDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteXYDomainCall0)(const void *, int *);
typedef void (*CuteXYDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteXYDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteXYDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteXYDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteXYDomainCall5)(const void *, const QPointF *, int *);
typedef void (*CuteXYDomainCall6)(const void *, const QSizeF *, int *);
typedef bool (*CuteXYDomainCall7)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteXYDomainCall8)(const void *, QAbstractAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXYDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXYDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteXYDomain : public XYDomain {
public:
  using XYDomain::XYDomain;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14AbstractDomain4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain8setRangeEdddd")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain6zoomInERK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7zoomOutERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain4moveEdd")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14AbstractDomain20calculateDomainPointERK7QPointF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7setSizeERK6QSizeF")) {
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

  //  DomainType XYDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteXYDomainCall0 call = reinterpret_cast<CuteXYDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return XYDomain::type();
  }

  //  void XYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
  //      maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteXYDomainCall1 call = reinterpret_cast<CuteXYDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    XYDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void XYDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteXYDomainCall2 call = reinterpret_cast<CuteXYDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XYDomain::zoomIn(rect);
  }

  //  void XYDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteXYDomainCall3 call = reinterpret_cast<CuteXYDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XYDomain::zoomOut(rect);
  }

  //  void XYDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteXYDomainCall4 call = reinterpret_cast<CuteXYDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    XYDomain::move(dx, dy);
  }

  //  QPointF XYDomain::calculateDomainPoint(const QPointF &point) const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteXYDomainCall5 call = reinterpret_cast<CuteXYDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return XYDomain::calculateDomainPoint(point);
  }

  //  void AbstractDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[6]) {
      int handled = 0;
      CuteXYDomainCall6 call = reinterpret_cast<CuteXYDomainCall6>(taken[6]);
      call(this, &size, &handled);
      if (handled) return;
    }
    AbstractDomain::setSize(size);
  }

  //  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteXYDomainCall7 call = reinterpret_cast<CuteXYDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return AbstractDomain::attachAxis(axis);
  }

  //  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CuteXYDomainCall8 call = reinterpret_cast<CuteXYDomainCall8>(taken[8]);
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
      CuteXYDomainCall9 call = reinterpret_cast<CuteXYDomainCall9>(taken[9]);
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
      CuteXYDomainCall10 call = reinterpret_cast<CuteXYDomainCall10>(taken[10]);
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
      CuteXYDomainCall11 call = reinterpret_cast<CuteXYDomainCall11>(taken[11]);
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
      CuteXYDomainCall12 call = reinterpret_cast<CuteXYDomainCall12>(taken[12]);
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
      CuteXYDomainCall13 call = reinterpret_cast<CuteXYDomainCall13>(taken[13]);
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
      CuteXYDomainCall14 call = reinterpret_cast<CuteXYDomainCall14>(taken[14]);
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
      CuteXYDomainCall15 call = reinterpret_cast<CuteXYDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *XYDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8XYDomain10metaObjectEv(const XYDomain *self) {
  return self->metaObject();
}

//  QString XYDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8XYDomain2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(XYDomain::tr(s, c, n));
}

//  XYDomain::XYDomain(QObject *object)
extern "C" Q_DECL_EXPORT
XYDomain *ritual_ZN8XYDomainC1EP7QObject(QObject *object) {
  return new CuteXYDomain(object);
}

//  XYDomain::~XYDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN8XYDomainD1Ev(XYDomain *self) {
  delete self;
}

//  DomainType XYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN8XYDomain4typeEv(XYDomain *self) {
  return self->type();
}

//  void XYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN8XYDomain8setRangeEdddd(
    XYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void XYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8XYDomain6zoomInERK6QRectF(
    XYDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void XYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8XYDomain7zoomOutERK6QRectF(
    XYDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void XYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8XYDomain4moveEdd(XYDomain *self, qreal dx, qreal dy) {
  self->move(dx, dy);
}

//  QPointF XYDomain::calculateGeometryPoint(const QPointF &point, bool &ok)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8XYDomain22calculateGeometryPointERK7QPointFRb(
    const XYDomain *self,
    const QPointF *point,
    bool *ok) {
  return new QPointF(self->calculateGeometryPoint(*point, *ok));
}

//  QPointF XYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8XYDomain20calculateDomainPointERK7QPointF(
    const XYDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  QList<QPointF> XYDomain::calculateGeometryPoints(const QList<QPointF>
//      &list) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK8XYDomain23calculateGeometryPointsERK5QListI7QPointFE(
    const XYDomain *self,
    const QList<QPointF> *list) {
  return new QList<QPointF>(self->calculateGeometryPoints(*list));
}

//  a Python function taken by a CuteXYDomain, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_XYDomain(XYDomain *self, const char *key, void *call) {
  return static_cast<CuteXYDomain *>(self)->take(key, call);
}

//  DomainType XYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN8XYDomain4typeEv(XYDomain *self) {
  return self->XYDomain::type();
}

//  void XYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8XYDomain8setRangeEdddd(
    XYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->XYDomain::setRange(minX, maxX, minY, maxY);
}

//  void XYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8XYDomain6zoomInERK6QRectF(
    XYDomain *self,
    const QRectF *rect) {
  self->XYDomain::zoomIn(*rect);
}

//  void XYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8XYDomain7zoomOutERK6QRectF(
    XYDomain *self,
    const QRectF *rect) {
  self->XYDomain::zoomOut(*rect);
}

//  void XYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8XYDomain4moveEdd(XYDomain *self, qreal dx, qreal dy) {
  self->XYDomain::move(dx, dy);
}

//  QPointF XYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK8XYDomain20calculateDomainPointERK7QPointF(
    const XYDomain *self,
    const QPointF *point) {
  return new QPointF(self->XYDomain::calculateDomainPoint(*point));
}
