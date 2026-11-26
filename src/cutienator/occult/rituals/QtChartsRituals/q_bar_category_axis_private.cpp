//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qbarcategoryaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qbarcategoryaxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qbarcategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBarCategoryAxisPrivate that Python can take functions over in. Every QBarCategoryAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBarCategoryAxisPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall1)(const void *, AbstractDomain *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall2)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall3)(const void *, const QVariant *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall4)(const void *, const QVariant *, int *);
typedef qreal (*CuteQBarCategoryAxisPrivateCall5)(const void *, int *);
typedef qreal (*CuteQBarCategoryAxisPrivateCall6)(const void *, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall7)(const void *, qreal, qreal, int *);
typedef void (*CuteQBarCategoryAxisPrivateCall8)(const void *, ChartTheme *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarCategoryAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarCategoryAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarCategoryAxisPrivate : public QBarCategoryAxisPrivate {
public:
  using QBarCategoryAxisPrivate::QBarCategoryAxisPrivate;
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
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
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

  //  void QBarCategoryAxisPrivate::initializeGraphics(QGraphicsItem
  //      *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall0 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::initializeGraphics(parent);
  }

  //  void QBarCategoryAxisPrivate::initializeDomain(AbstractDomain
  //      *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall1 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall1>(taken[1]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::initializeDomain(domain);
  }

  //  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall2 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall2>(taken[2]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setRange(min, max);
  }

  //  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall3 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall3>(taken[3]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setMin(min);
  }

  //  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall4 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall4>(taken[4]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setMax(max);
  }

  //  qreal QBarCategoryAxisPrivate::min()
  qreal min() override {
    if (taken[5]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall5 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QBarCategoryAxisPrivate::min();
  }

  //  qreal QBarCategoryAxisPrivate::max()
  qreal max() override {
    if (taken[6]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall6 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QBarCategoryAxisPrivate::max();
  }

  //  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[7]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall7 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall7>(taken[7]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QBarCategoryAxisPrivate::setRange(min, max);
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[8]) {
      int handled = 0;
      CuteQBarCategoryAxisPrivateCall8 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall8>(taken[8]);
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
      CuteQBarCategoryAxisPrivateCall9 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall9>(taken[9]);
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
      CuteQBarCategoryAxisPrivateCall10 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall10>(taken[10]);
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
      CuteQBarCategoryAxisPrivateCall11 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall11>(taken[11]);
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
      CuteQBarCategoryAxisPrivateCall12 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall12>(taken[12]);
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
      CuteQBarCategoryAxisPrivateCall13 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall13>(taken[13]);
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
      CuteQBarCategoryAxisPrivateCall14 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall14>(taken[14]);
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
      CuteQBarCategoryAxisPrivateCall15 call = reinterpret_cast<CuteQBarCategoryAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarCategoryAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QBarCategoryAxisPrivate10metaObjectEv(
    const QBarCategoryAxisPrivate *self) {
  return self->metaObject();
}

//  void *QBarCategoryAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QBarCategoryAxisPrivate11qt_metacastEPKc(
    QBarCategoryAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarCategoryAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QBarCategoryAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarCategoryAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBarCategoryAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QBarCategoryAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarCategoryAxisPrivate::tr(s, c, n));
}

//  QBarCategoryAxisPrivate::QBarCategoryAxisPrivate(QBarCategoryAxis *q)
extern "C" Q_DECL_EXPORT
QBarCategoryAxisPrivate *ritual_ZN23QBarCategoryAxisPrivateC1EP16QBarCategoryAxis(
    QBarCategoryAxis *q) {
  return new CuteQBarCategoryAxisPrivate(q);
}

//  QBarCategoryAxisPrivate::~QBarCategoryAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivateD1Ev(QBarCategoryAxisPrivate *self) {
  delete self;
}

//  void QBarCategoryAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QBarCategoryAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QBarCategoryAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate16initializeDomainEP14AbstractDomain(
    QBarCategoryAxisPrivate *self,
    AbstractDomain *domain) {
  self->initializeDomain(domain);
}

//  void QBarCategoryAxisPrivate::updateCategoryDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate20updateCategoryDomainEv(
    QBarCategoryAxisPrivate *self) {
  self->updateCategoryDomain();
}

//  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
//      QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_(
    QBarCategoryAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate6setMinERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  qreal QBarCategoryAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN23QBarCategoryAxisPrivate3minEv(
    QBarCategoryAxisPrivate *self) {
  return self->min();
}

//  qreal QBarCategoryAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN23QBarCategoryAxisPrivate3maxEv(
    QBarCategoryAxisPrivate *self) {
  return self->max();
}

//  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate8setRangeEdd(
    QBarCategoryAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QBarCategoryAxisPrivate::setRange(const QString &minCategory, const
//      QString &maxCategory)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarCategoryAxisPrivate8setRangeERK7QStringS2_(
    QBarCategoryAxisPrivate *self,
    const QString *minCategory,
    const QString *maxCategory) {
  self->setRange(*minCategory, *maxCategory);
}

//  QBarCategoryAxis *QBarCategoryAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarCategoryAxis *ritual_ZN23QBarCategoryAxisPrivate6q_funcEv(
    QBarCategoryAxisPrivate *self) {
  return self->q_func();
}

//  const QBarCategoryAxis *QBarCategoryAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarCategoryAxis *ritual_ZNK23QBarCategoryAxisPrivate6q_funcEv(
    const QBarCategoryAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQBarCategoryAxisPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarCategoryAxisPrivate(
    QBarCategoryAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarCategoryAxisPrivate *>(self)->take(key, call);
}

//  void QBarCategoryAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QBarCategoryAxisPrivate *self,
    QGraphicsItem *parent) {
  self->QBarCategoryAxisPrivate::initializeGraphics(parent);
}

//  void QBarCategoryAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate16initializeDomainEP14AbstractDomain(
    QBarCategoryAxisPrivate *self,
    AbstractDomain *domain) {
  self->QBarCategoryAxisPrivate::initializeDomain(domain);
}

//  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
//      QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_(
    QBarCategoryAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->QBarCategoryAxisPrivate::setRange(*min, *max);
}

//  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate6setMinERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *min) {
  self->QBarCategoryAxisPrivate::setMin(*min);
}

//  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant(
    QBarCategoryAxisPrivate *self,
    const QVariant *max) {
  self->QBarCategoryAxisPrivate::setMax(*max);
}

//  qreal QBarCategoryAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN23QBarCategoryAxisPrivate3minEv(
    QBarCategoryAxisPrivate *self) {
  return self->QBarCategoryAxisPrivate::min();
}

//  qreal QBarCategoryAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN23QBarCategoryAxisPrivate3maxEv(
    QBarCategoryAxisPrivate *self) {
  return self->QBarCategoryAxisPrivate::max();
}

//  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarCategoryAxisPrivate8setRangeEdd(
    QBarCategoryAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QBarCategoryAxisPrivate::setRange(min, max);
}
