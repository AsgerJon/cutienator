//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/xypolardomain_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/xypolardomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A XYPolarDomain that Python can take functions over in. Every XYPolarDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteXYPolarDomainCall0)(const void *, int *);
typedef void (*CuteXYPolarDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteXYPolarDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteXYPolarDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteXYPolarDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteXYPolarDomainCall5)(const void *, const QPointF *, int *);
typedef void (*CuteXYPolarDomainCall6)(const void *, const QSizeF *, int *);
typedef bool (*CuteXYPolarDomainCall7)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteXYPolarDomainCall8)(const void *, QAbstractAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXYPolarDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXYPolarDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYPolarDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYPolarDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYPolarDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYPolarDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYPolarDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteXYPolarDomain : public XYPolarDomain {
public:
  using XYPolarDomain::XYPolarDomain;
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

  //  DomainType XYPolarDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteXYPolarDomainCall0 call = reinterpret_cast<CuteXYPolarDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return XYPolarDomain::type();
  }

  //  void XYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY,
  //      qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteXYPolarDomainCall1 call = reinterpret_cast<CuteXYPolarDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    XYPolarDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void XYPolarDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteXYPolarDomainCall2 call = reinterpret_cast<CuteXYPolarDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XYPolarDomain::zoomIn(rect);
  }

  //  void XYPolarDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteXYPolarDomainCall3 call = reinterpret_cast<CuteXYPolarDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XYPolarDomain::zoomOut(rect);
  }

  //  void XYPolarDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteXYPolarDomainCall4 call = reinterpret_cast<CuteXYPolarDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    XYPolarDomain::move(dx, dy);
  }

  //  QPointF XYPolarDomain::calculateDomainPoint(const QPointF &point)
  //      const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteXYPolarDomainCall5 call = reinterpret_cast<CuteXYPolarDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return XYPolarDomain::calculateDomainPoint(point);
  }

  //  void PolarDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[6]) {
      int handled = 0;
      CuteXYPolarDomainCall6 call = reinterpret_cast<CuteXYPolarDomainCall6>(taken[6]);
      call(this, &size, &handled);
      if (handled) return;
    }
    PolarDomain::setSize(size);
  }

  //  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteXYPolarDomainCall7 call = reinterpret_cast<CuteXYPolarDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return AbstractDomain::attachAxis(axis);
  }

  //  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CuteXYPolarDomainCall8 call = reinterpret_cast<CuteXYPolarDomainCall8>(taken[8]);
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
      CuteXYPolarDomainCall9 call = reinterpret_cast<CuteXYPolarDomainCall9>(taken[9]);
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
      CuteXYPolarDomainCall10 call = reinterpret_cast<CuteXYPolarDomainCall10>(taken[10]);
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
      CuteXYPolarDomainCall11 call = reinterpret_cast<CuteXYPolarDomainCall11>(taken[11]);
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
      CuteXYPolarDomainCall12 call = reinterpret_cast<CuteXYPolarDomainCall12>(taken[12]);
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
      CuteXYPolarDomainCall13 call = reinterpret_cast<CuteXYPolarDomainCall13>(taken[13]);
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
      CuteXYPolarDomainCall14 call = reinterpret_cast<CuteXYPolarDomainCall14>(taken[14]);
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
      CuteXYPolarDomainCall15 call = reinterpret_cast<CuteXYPolarDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *XYPolarDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13XYPolarDomain10metaObjectEv(
    const XYPolarDomain *self) {
  return self->metaObject();
}

//  void *XYPolarDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13XYPolarDomain11qt_metacastEPKc(
    XYPolarDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int XYPolarDomain::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13XYPolarDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    XYPolarDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString XYPolarDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13XYPolarDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(XYPolarDomain::tr(s, c, n));
}

//  XYPolarDomain::XYPolarDomain(QObject *object)
extern "C" Q_DECL_EXPORT
XYPolarDomain *ritual_ZN13XYPolarDomainC1EP7QObject(QObject *object) {
  return new CuteXYPolarDomain(object);
}

//  XYPolarDomain::~XYPolarDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN13XYPolarDomainD1Ev(XYPolarDomain *self) {
  delete self;
}

//  DomainType XYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN13XYPolarDomain4typeEv(
    XYPolarDomain *self) {
  return self->type();
}

//  void XYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN13XYPolarDomain8setRangeEdddd(
    XYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void XYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13XYPolarDomain6zoomInERK6QRectF(
    XYPolarDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void XYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13XYPolarDomain7zoomOutERK6QRectF(
    XYPolarDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void XYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13XYPolarDomain4moveEdd(
    XYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->move(dx, dy);
}

//  QPointF XYPolarDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13XYPolarDomain20calculateDomainPointERK7QPointF(
    const XYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  qreal XYPolarDomain::toAngularCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13XYPolarDomain19toAngularCoordinateEdRb(
    const XYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toAngularCoordinate(value, *ok);
}

//  qreal XYPolarDomain::toRadialCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13XYPolarDomain18toRadialCoordinateEdRb(
    const XYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toRadialCoordinate(value, *ok);
}

//  a Python function taken by a CuteXYPolarDomain, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_XYPolarDomain(
    XYPolarDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteXYPolarDomain *>(self)->take(key, call);
}

//  DomainType XYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN13XYPolarDomain4typeEv(
    XYPolarDomain *self) {
  return self->XYPolarDomain::type();
}

//  void XYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13XYPolarDomain8setRangeEdddd(
    XYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->XYPolarDomain::setRange(minX, maxX, minY, maxY);
}

//  void XYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13XYPolarDomain6zoomInERK6QRectF(
    XYPolarDomain *self,
    const QRectF *rect) {
  self->XYPolarDomain::zoomIn(*rect);
}

//  void XYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13XYPolarDomain7zoomOutERK6QRectF(
    XYPolarDomain *self,
    const QRectF *rect) {
  self->XYPolarDomain::zoomOut(*rect);
}

//  void XYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13XYPolarDomain4moveEdd(
    XYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->XYPolarDomain::move(dx, dy);
}

//  QPointF XYPolarDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK13XYPolarDomain20calculateDomainPointERK7QPointF(
    const XYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->XYPolarDomain::calculateDomainPoint(*point));
}
