//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qcategoryaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qcategoryaxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qcategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCategoryAxisPrivate that Python can take functions over in. Every QCategoryAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCategoryAxisPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQCategoryAxisPrivateCall1)(const void *, AbstractDomain *, int *);
typedef qreal (*CuteQCategoryAxisPrivateCall2)(const void *, int *);
typedef qreal (*CuteQCategoryAxisPrivateCall3)(const void *, int *);
typedef void (*CuteQCategoryAxisPrivateCall4)(const void *, qreal, qreal, int *);
typedef void (*CuteQCategoryAxisPrivateCall5)(const void *, const QVariant *, int *);
typedef void (*CuteQCategoryAxisPrivateCall6)(const void *, const QVariant *, int *);
typedef void (*CuteQCategoryAxisPrivateCall7)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQCategoryAxisPrivateCall8)(const void *, ChartTheme *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategoryAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategoryAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCategoryAxisPrivate : public QCategoryAxisPrivate {
public:
  using QCategoryAxisPrivate::QCategoryAxisPrivate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate18initializeGraphicsEP13QGraphicsItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate16initializeDomainEP14AbstractDomain")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb")) {
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

  //  void QCategoryAxisPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall0 call = reinterpret_cast<CuteQCategoryAxisPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QCategoryAxisPrivate::initializeGraphics(parent);
  }

  //  void QValueAxisPrivate::initializeDomain(AbstractDomain *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall1 call = reinterpret_cast<CuteQCategoryAxisPrivateCall1>(taken[1]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::initializeDomain(domain);
  }

  //  qreal QValueAxisPrivate::min()
  qreal min() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall2 call = reinterpret_cast<CuteQCategoryAxisPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QValueAxisPrivate::min();
  }

  //  qreal QValueAxisPrivate::max()
  qreal max() override {
    if (taken[3]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall3 call = reinterpret_cast<CuteQCategoryAxisPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QValueAxisPrivate::max();
  }

  //  void QValueAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall4 call = reinterpret_cast<CuteQCategoryAxisPrivateCall4>(taken[4]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setRange(min, max);
  }

  //  void QValueAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall5 call = reinterpret_cast<CuteQCategoryAxisPrivateCall5>(taken[5]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setMin(min);
  }

  //  void QValueAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall6 call = reinterpret_cast<CuteQCategoryAxisPrivateCall6>(taken[6]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setMax(max);
  }

  //  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
  //      &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall7 call = reinterpret_cast<CuteQCategoryAxisPrivateCall7>(taken[7]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setRange(min, max);
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall8 call = reinterpret_cast<CuteQCategoryAxisPrivateCall8>(taken[8]);
      call(this, theme, forced, &handled);
      if (handled) return;
    }
    QAbstractAxisPrivate::initializeTheme(theme, forced);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCategoryAxisPrivateCall9 call = reinterpret_cast<CuteQCategoryAxisPrivateCall9>(taken[9]);
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
      CuteQCategoryAxisPrivateCall10 call = reinterpret_cast<CuteQCategoryAxisPrivateCall10>(taken[10]);
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
      CuteQCategoryAxisPrivateCall11 call = reinterpret_cast<CuteQCategoryAxisPrivateCall11>(taken[11]);
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
      CuteQCategoryAxisPrivateCall12 call = reinterpret_cast<CuteQCategoryAxisPrivateCall12>(taken[12]);
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
      CuteQCategoryAxisPrivateCall13 call = reinterpret_cast<CuteQCategoryAxisPrivateCall13>(taken[13]);
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
      CuteQCategoryAxisPrivateCall14 call = reinterpret_cast<CuteQCategoryAxisPrivateCall14>(taken[14]);
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
      CuteQCategoryAxisPrivateCall15 call = reinterpret_cast<CuteQCategoryAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCategoryAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QCategoryAxisPrivate10metaObjectEv(
    const QCategoryAxisPrivate *self) {
  return self->metaObject();
}

//  void *QCategoryAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QCategoryAxisPrivate11qt_metacastEPKc(
    QCategoryAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCategoryAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QCategoryAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QCategoryAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCategoryAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QCategoryAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCategoryAxisPrivate::tr(s, c, n));
}

//  QCategoryAxisPrivate::QCategoryAxisPrivate(QCategoryAxis *q)
extern "C" Q_DECL_EXPORT
QCategoryAxisPrivate *ritual_ZN20QCategoryAxisPrivateC1EP13QCategoryAxis(
    QCategoryAxis *q) {
  return new CuteQCategoryAxisPrivate(q);
}

//  QCategoryAxisPrivate::~QCategoryAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCategoryAxisPrivateD1Ev(QCategoryAxisPrivate *self) {
  delete self;
}

//  void QCategoryAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCategoryAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QCategoryAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  int QCategoryAxisPrivate::ticksCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QCategoryAxisPrivate10ticksCountEv(
    const QCategoryAxisPrivate *self) {
  return self->ticksCount();
}

//  QCategoryAxis *QCategoryAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCategoryAxis *ritual_ZN20QCategoryAxisPrivate6q_funcEv(
    QCategoryAxisPrivate *self) {
  return self->q_func();
}

//  const QCategoryAxis *QCategoryAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCategoryAxis *ritual_ZNK20QCategoryAxisPrivate6q_funcEv(
    const QCategoryAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCategoryAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCategoryAxisPrivate(
    QCategoryAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCategoryAxisPrivate *>(self)->take(key, call);
}

//  void QCategoryAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCategoryAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QCategoryAxisPrivate *self,
    QGraphicsItem *parent) {
  self->QCategoryAxisPrivate::initializeGraphics(parent);
}
