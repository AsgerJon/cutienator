//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/xlogydomain_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/xlogydomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A XLogYDomain that Python can take functions over in. Every XLogYDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteXLogYDomainCall0)(const void *, int *);
typedef void (*CuteXLogYDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteXLogYDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteXLogYDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteXLogYDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteXLogYDomainCall5)(const void *, const QPointF *, int *);
typedef bool (*CuteXLogYDomainCall6)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteXLogYDomainCall7)(const void *, QAbstractAxis *, int *);
typedef void (*CuteXLogYDomainCall8)(const void *, const QSizeF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXLogYDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXLogYDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXLogYDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteXLogYDomain : public XLogYDomain {
public:
  using XLogYDomain::XLogYDomain;
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

  //  DomainType XLogYDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteXLogYDomainCall0 call = reinterpret_cast<CuteXLogYDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return XLogYDomain::type();
  }

  //  void XLogYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
  //      maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteXLogYDomainCall1 call = reinterpret_cast<CuteXLogYDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    XLogYDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void XLogYDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteXLogYDomainCall2 call = reinterpret_cast<CuteXLogYDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XLogYDomain::zoomIn(rect);
  }

  //  void XLogYDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteXLogYDomainCall3 call = reinterpret_cast<CuteXLogYDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    XLogYDomain::zoomOut(rect);
  }

  //  void XLogYDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteXLogYDomainCall4 call = reinterpret_cast<CuteXLogYDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    XLogYDomain::move(dx, dy);
  }

  //  QPointF XLogYDomain::calculateDomainPoint(const QPointF &point) const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteXLogYDomainCall5 call = reinterpret_cast<CuteXLogYDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return XLogYDomain::calculateDomainPoint(point);
  }

  //  bool XLogYDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[6]) {
      int handled = 0;
      CuteXLogYDomainCall6 call = reinterpret_cast<CuteXLogYDomainCall6>(taken[6]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return XLogYDomain::attachAxis(axis);
  }

  //  bool XLogYDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteXLogYDomainCall7 call = reinterpret_cast<CuteXLogYDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return XLogYDomain::detachAxis(axis);
  }

  //  void AbstractDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteXLogYDomainCall8 call = reinterpret_cast<CuteXLogYDomainCall8>(taken[8]);
      call(this, &size, &handled);
      if (handled) return;
    }
    AbstractDomain::setSize(size);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteXLogYDomainCall9 call = reinterpret_cast<CuteXLogYDomainCall9>(taken[9]);
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
      CuteXLogYDomainCall10 call = reinterpret_cast<CuteXLogYDomainCall10>(taken[10]);
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
      CuteXLogYDomainCall11 call = reinterpret_cast<CuteXLogYDomainCall11>(taken[11]);
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
      CuteXLogYDomainCall12 call = reinterpret_cast<CuteXLogYDomainCall12>(taken[12]);
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
      CuteXLogYDomainCall13 call = reinterpret_cast<CuteXLogYDomainCall13>(taken[13]);
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
      CuteXLogYDomainCall14 call = reinterpret_cast<CuteXLogYDomainCall14>(taken[14]);
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
      CuteXLogYDomainCall15 call = reinterpret_cast<CuteXLogYDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *XLogYDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11XLogYDomain10metaObjectEv(
    const XLogYDomain *self) {
  return self->metaObject();
}

//  void *XLogYDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11XLogYDomain11qt_metacastEPKc(
    XLogYDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int XLogYDomain::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11XLogYDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    XLogYDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString XLogYDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11XLogYDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(XLogYDomain::tr(s, c, n));
}

//  XLogYDomain::XLogYDomain(QObject *object)
extern "C" Q_DECL_EXPORT
XLogYDomain *ritual_ZN11XLogYDomainC1EP7QObject(QObject *object) {
  return new CuteXLogYDomain(object);
}

//  XLogYDomain::~XLogYDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN11XLogYDomainD1Ev(XLogYDomain *self) {
  delete self;
}

//  DomainType XLogYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN11XLogYDomain4typeEv(XLogYDomain *self) {
  return self->type();
}

//  void XLogYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XLogYDomain8setRangeEdddd(
    XLogYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void XLogYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XLogYDomain6zoomInERK6QRectF(
    XLogYDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void XLogYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XLogYDomain7zoomOutERK6QRectF(
    XLogYDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void XLogYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XLogYDomain4moveEdd(XLogYDomain *self, qreal dx, qreal dy) {
  self->move(dx, dy);
}

//  QPointF XLogYDomain::calculateGeometryPoint(const QPointF &point, bool
//      &ok) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11XLogYDomain22calculateGeometryPointERK7QPointFRb(
    const XLogYDomain *self,
    const QPointF *point,
    bool *ok) {
  return new QPointF(self->calculateGeometryPoint(*point, *ok));
}

//  QPointF XLogYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11XLogYDomain20calculateDomainPointERK7QPointF(
    const XLogYDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  QList<QPointF> XLogYDomain::calculateGeometryPoints(const QList<QPointF>
//      &list) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK11XLogYDomain23calculateGeometryPointsERK5QListI7QPointFE(
    const XLogYDomain *self,
    const QList<QPointF> *list) {
  return new QList<QPointF>(self->calculateGeometryPoints(*list));
}

//  bool XLogYDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11XLogYDomain10attachAxisEP13QAbstractAxis(
    XLogYDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool XLogYDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11XLogYDomain10detachAxisEP13QAbstractAxis(
    XLogYDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void XLogYDomain::handleVerticalAxisBaseChanged(qreal baseY)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XLogYDomain29handleVerticalAxisBaseChangedEd(
    XLogYDomain *self,
    qreal baseY) {
  self->handleVerticalAxisBaseChanged(baseY);
}

//  a Python function taken by a CuteXLogYDomain, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_XLogYDomain(
    XLogYDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteXLogYDomain *>(self)->take(key, call);
}

//  DomainType XLogYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN11XLogYDomain4typeEv(
    XLogYDomain *self) {
  return self->XLogYDomain::type();
}

//  void XLogYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11XLogYDomain8setRangeEdddd(
    XLogYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->XLogYDomain::setRange(minX, maxX, minY, maxY);
}

//  void XLogYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11XLogYDomain6zoomInERK6QRectF(
    XLogYDomain *self,
    const QRectF *rect) {
  self->XLogYDomain::zoomIn(*rect);
}

//  void XLogYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11XLogYDomain7zoomOutERK6QRectF(
    XLogYDomain *self,
    const QRectF *rect) {
  self->XLogYDomain::zoomOut(*rect);
}

//  void XLogYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11XLogYDomain4moveEdd(
    XLogYDomain *self,
    qreal dx,
    qreal dy) {
  self->XLogYDomain::move(dx, dy);
}

//  QPointF XLogYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK11XLogYDomain20calculateDomainPointERK7QPointF(
    const XLogYDomain *self,
    const QPointF *point) {
  return new QPointF(self->XLogYDomain::calculateDomainPoint(*point));
}

//  bool XLogYDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11XLogYDomain10attachAxisEP13QAbstractAxis(
    XLogYDomain *self,
    QAbstractAxis *axis) {
  return self->XLogYDomain::attachAxis(axis);
}

//  bool XLogYDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11XLogYDomain10detachAxisEP13QAbstractAxis(
    XLogYDomain *self,
    QAbstractAxis *axis) {
  return self->XLogYDomain::detachAxis(axis);
}
