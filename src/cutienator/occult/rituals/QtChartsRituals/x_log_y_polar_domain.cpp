//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/xlogypolardomain_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/xlogypolardomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A XLogYPolarDomain that Python can take functions over in. Every XLogYPolarDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteXLogYPolarDomainCall0)(const void *, int *);
typedef void (*CuteXLogYPolarDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteXLogYPolarDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteXLogYPolarDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteXLogYPolarDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteXLogYPolarDomainCall5)(const void *, const QPointF *, int *);
typedef bool (*CuteXLogYPolarDomainCall6)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteXLogYPolarDomainCall7)(const void *, QAbstractAxis *, int *);
typedef void (*CuteXLogYPolarDomainCall8)(const void *, const QSizeF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXLogYPolarDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXLogYPolarDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYPolarDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYPolarDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYPolarDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYPolarDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYPolarDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteXLogYPolarDomain : public XLogYPolarDomain {
public:
  using XLogYPolarDomain::XLogYPolarDomain;
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
    if (!std::strcmp(key, "_ZN14AbstractDomain10attachAxisEP13QAbstractAxis")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10detachAxisEP13QAbstractAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7setSizeERK6QSizeF")) {
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

  //  DomainType XLogYPolarDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteXLogYPolarDomainCall0 call = reinterpret_cast<CuteXLogYPolarDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return XLogYPolarDomain::type();
  }

  //  void XLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY,
  //      qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteXLogYPolarDomainCall1 call = reinterpret_cast<CuteXLogYPolarDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    XLogYPolarDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void XLogYPolarDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteXLogYPolarDomainCall2 call = reinterpret_cast<CuteXLogYPolarDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XLogYPolarDomain::zoomIn(rect);
  }

  //  void XLogYPolarDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteXLogYPolarDomainCall3 call = reinterpret_cast<CuteXLogYPolarDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XLogYPolarDomain::zoomOut(rect);
  }

  //  void XLogYPolarDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteXLogYPolarDomainCall4 call = reinterpret_cast<CuteXLogYPolarDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    XLogYPolarDomain::move(dx, dy);
  }

  //  QPointF XLogYPolarDomain::calculateDomainPoint(const QPointF &point)
  //      const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteXLogYPolarDomainCall5 call = reinterpret_cast<CuteXLogYPolarDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return XLogYPolarDomain::calculateDomainPoint(point);
  }

  //  bool XLogYPolarDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[6]) {
      int handled = 0;
      CuteXLogYPolarDomainCall6 call = reinterpret_cast<CuteXLogYPolarDomainCall6>(taken[6]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return XLogYPolarDomain::attachAxis(axis);
  }

  //  bool XLogYPolarDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteXLogYPolarDomainCall7 call = reinterpret_cast<CuteXLogYPolarDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return XLogYPolarDomain::detachAxis(axis);
  }

  //  void PolarDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteXLogYPolarDomainCall8 call = reinterpret_cast<CuteXLogYPolarDomainCall8>(taken[8]);
      call(this, &size, &handled);
      if (handled) return;
    }
    PolarDomain::setSize(size);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteXLogYPolarDomainCall9 call = reinterpret_cast<CuteXLogYPolarDomainCall9>(taken[9]);
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
      CuteXLogYPolarDomainCall10 call = reinterpret_cast<CuteXLogYPolarDomainCall10>(taken[10]);
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
      CuteXLogYPolarDomainCall11 call = reinterpret_cast<CuteXLogYPolarDomainCall11>(taken[11]);
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
      CuteXLogYPolarDomainCall12 call = reinterpret_cast<CuteXLogYPolarDomainCall12>(taken[12]);
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
      CuteXLogYPolarDomainCall13 call = reinterpret_cast<CuteXLogYPolarDomainCall13>(taken[13]);
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
      CuteXLogYPolarDomainCall14 call = reinterpret_cast<CuteXLogYPolarDomainCall14>(taken[14]);
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
      CuteXLogYPolarDomainCall15 call = reinterpret_cast<CuteXLogYPolarDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *XLogYPolarDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16XLogYPolarDomain10metaObjectEv(
    const XLogYPolarDomain *self) {
  return self->metaObject();
}

//  void *XLogYPolarDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16XLogYPolarDomain11qt_metacastEPKc(
    XLogYPolarDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int XLogYPolarDomain::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16XLogYPolarDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    XLogYPolarDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString XLogYPolarDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16XLogYPolarDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(XLogYPolarDomain::tr(s, c, n));
}

//  XLogYPolarDomain::XLogYPolarDomain(QObject *object)
extern "C" Q_DECL_EXPORT
XLogYPolarDomain *ritual_ZN16XLogYPolarDomainC1EP7QObject(QObject *object) {
  return new CuteXLogYPolarDomain(object);
}

//  XLogYPolarDomain::~XLogYPolarDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN16XLogYPolarDomainD1Ev(XLogYPolarDomain *self) {
  delete self;
}

//  DomainType XLogYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN16XLogYPolarDomain4typeEv(
    XLogYPolarDomain *self) {
  return self->type();
}

//  void XLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN16XLogYPolarDomain8setRangeEdddd(
    XLogYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void XLogYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16XLogYPolarDomain6zoomInERK6QRectF(
    XLogYPolarDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void XLogYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16XLogYPolarDomain7zoomOutERK6QRectF(
    XLogYPolarDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void XLogYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16XLogYPolarDomain4moveEdd(
    XLogYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->move(dx, dy);
}

//  QPointF XLogYPolarDomain::calculateDomainPoint(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16XLogYPolarDomain20calculateDomainPointERK7QPointF(
    const XLogYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  bool XLogYPolarDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16XLogYPolarDomain10attachAxisEP13QAbstractAxis(
    XLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool XLogYPolarDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16XLogYPolarDomain10detachAxisEP13QAbstractAxis(
    XLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void XLogYPolarDomain::handleVerticalAxisBaseChanged(qreal baseY)
extern "C" Q_DECL_EXPORT
void ritual_ZN16XLogYPolarDomain29handleVerticalAxisBaseChangedEd(
    XLogYPolarDomain *self,
    qreal baseY) {
  self->handleVerticalAxisBaseChanged(baseY);
}

//  qreal XLogYPolarDomain::toAngularCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16XLogYPolarDomain19toAngularCoordinateEdRb(
    const XLogYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toAngularCoordinate(value, *ok);
}

//  qreal XLogYPolarDomain::toRadialCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16XLogYPolarDomain18toRadialCoordinateEdRb(
    const XLogYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toRadialCoordinate(value, *ok);
}

//  a Python function taken by a CuteXLogYPolarDomain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_XLogYPolarDomain(
    XLogYPolarDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteXLogYPolarDomain *>(self)->take(key, call);
}

//  DomainType XLogYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN16XLogYPolarDomain4typeEv(
    XLogYPolarDomain *self) {
  return self->XLogYPolarDomain::type();
}

//  void XLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16XLogYPolarDomain8setRangeEdddd(
    XLogYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->XLogYPolarDomain::setRange(minX, maxX, minY, maxY);
}

//  void XLogYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16XLogYPolarDomain6zoomInERK6QRectF(
    XLogYPolarDomain *self,
    const QRectF *rect) {
  self->XLogYPolarDomain::zoomIn(*rect);
}

//  void XLogYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16XLogYPolarDomain7zoomOutERK6QRectF(
    XLogYPolarDomain *self,
    const QRectF *rect) {
  self->XLogYPolarDomain::zoomOut(*rect);
}

//  void XLogYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16XLogYPolarDomain4moveEdd(
    XLogYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->XLogYPolarDomain::move(dx, dy);
}

//  QPointF XLogYPolarDomain::calculateDomainPoint(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK16XLogYPolarDomain20calculateDomainPointERK7QPointF(
    const XLogYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->XLogYPolarDomain::calculateDomainPoint(*point));
}

//  bool XLogYPolarDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16XLogYPolarDomain10attachAxisEP13QAbstractAxis(
    XLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->XLogYPolarDomain::attachAxis(axis);
}

//  bool XLogYPolarDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16XLogYPolarDomain10detachAxisEP13QAbstractAxis(
    XLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->XLogYPolarDomain::detachAxis(axis);
}
