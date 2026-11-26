//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qabstractseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qabstractseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstractSeriesPrivate that Python can take functions over in. Every QAbstractSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractSeriesPrivateCall0)(const void *, int *);
typedef void (*CuteQAbstractSeriesPrivateCall1)(const void *, int *);
typedef void (*CuteQAbstractSeriesPrivateCall2)(const void *, int, ChartTheme *, bool, int *);
typedef void (*CuteQAbstractSeriesPrivateCall3)(const void *, QGraphicsItem *, int *);
typedef int (*CuteQAbstractSeriesPrivateCall4)(const void *, int, int *);
typedef void * (*CuteQAbstractSeriesPrivateCall5)(const void *, int, int *);
typedef void (*CuteQAbstractSeriesPrivateCall6)(const void *, AbstractDomain *, int *);
typedef void (*CuteQAbstractSeriesPrivateCall7)(const void *, ChartPresenter *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSeriesPrivateCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesPrivateCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesPrivateCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesPrivateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractSeriesPrivate : public QAbstractSeriesPrivate {
public:
  using QAbstractSeriesPrivate::QAbstractSeriesPrivate;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate16initializeDomainEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate14initializeAxesEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate15initializeThemeEiP10ChartThemeb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate18initializeGraphicsEP13QGraphicsItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QAbstractSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QAbstractSeriesPrivate17createDefaultAxisEN2Qt11OrientationE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate9setDomainEP14AbstractDomain")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate12setPresenterEP14ChartPresenter")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstractSeriesPrivate::initializeDomain()
  void initializeDomain() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall0 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSeriesPrivate::initializeAxes()
  void initializeAxes() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall1 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSeriesPrivate::initializeTheme(int index, ChartTheme
  //      *theme, bool forced)
  void initializeTheme(int index, ChartTheme *theme, bool forced) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall2 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall2>(taken[2]);
      call(this, index, theme, forced, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSeriesPrivate::initializeGraphics(QGraphicsItem
  //      *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall3 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall3>(taken[3]);
      call(this, parent, &handled);
      if (handled) return;
    }
  }

  //  QAbstractAxis::AxisType
  //      QAbstractSeriesPrivate::defaultAxisType(Qt::Orientation a0) const
  QAbstractAxis::AxisType defaultAxisType(
      Qt::Orientation a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall4 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall4>(taken[4]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return {};
  }

  //  QAbstractAxis
  //      *QAbstractSeriesPrivate::createDefaultAxis(Qt::Orientation a0)
  //      const
  QAbstractAxis *createDefaultAxis(Qt::Orientation a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall5 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall5>(taken[5]);
      void * given = call(this, static_cast<int>(a0), &handled);
      if (handled) return static_cast<QAbstractAxis *>(given);
    }
    return {};
  }

  //  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
  void setDomain(AbstractDomain *domain) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall6 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall6>(taken[6]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QAbstractSeriesPrivate::setDomain(domain);
  }

  //  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall7 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall7>(taken[7]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    QAbstractSeriesPrivate::setPresenter(presenter);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall8 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall9 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall10 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall11 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall12 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall13 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractSeriesPrivateCall14 call = reinterpret_cast<CuteQAbstractSeriesPrivateCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QAbstractSeriesPrivate10metaObjectEv(
    const QAbstractSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QAbstractSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QAbstractSeriesPrivate11qt_metacastEPKc(
    QAbstractSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QAbstractSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QAbstractSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSeriesPrivate::tr(s, c, n));
}

//  QAbstractSeriesPrivate::~QAbstractSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivateD1Ev(QAbstractSeriesPrivate *self) {
  delete self;
}

//  void QAbstractSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate16initializeDomainEv(
    QAbstractSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QAbstractSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate14initializeAxesEv(
    QAbstractSeriesPrivate *self) {
  self->initializeAxes();
}

//  void QAbstractSeriesPrivate::initializeTheme(int index, ChartTheme
//      *theme, bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QAbstractSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  void QAbstractSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QAbstractSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void
//      QAbstractSeriesPrivate::initializeAnimations(QChart::AnimationOptions
//      options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QAbstractSeriesPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
}

//  QList<QLegendMarker *>
//      QAbstractSeriesPrivate::createLegendMarkers(QLegend *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN22QAbstractSeriesPrivate19createLegendMarkersEP7QLegend(
    QAbstractSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType
//      QAbstractSeriesPrivate::defaultAxisType(Qt::Orientation a0) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK22QAbstractSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QAbstractSeriesPrivate *self,
    Qt::Orientation a0) {
  return self->defaultAxisType(a0);
}

//  QAbstractAxis *QAbstractSeriesPrivate::createDefaultAxis(Qt::Orientation
//      a0) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK22QAbstractSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QAbstractSeriesPrivate *self,
    Qt::Orientation a0) {
  return self->createDefaultAxis(a0);
}

//  ChartItem *QAbstractSeriesPrivate::chartItem()
extern "C" Q_DECL_EXPORT
ChartItem *ritual_ZN22QAbstractSeriesPrivate9chartItemEv(
    QAbstractSeriesPrivate *self) {
  return self->chartItem();
}

//  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate9setDomainEP14AbstractDomain(
    QAbstractSeriesPrivate *self,
    AbstractDomain *domain) {
  self->setDomain(domain);
}

//  AbstractDomain *QAbstractSeriesPrivate::domain()
extern "C" Q_DECL_EXPORT
AbstractDomain *ritual_ZN22QAbstractSeriesPrivate6domainEv(
    QAbstractSeriesPrivate *self) {
  return self->domain();
}

//  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate12setPresenterEP14ChartPresenter(
    QAbstractSeriesPrivate *self,
    ChartPresenter *presenter) {
  self->setPresenter(presenter);
}

//  ChartPresenter *QAbstractSeriesPrivate::presenter() const
extern "C" Q_DECL_EXPORT
ChartPresenter *ritual_ZNK22QAbstractSeriesPrivate9presenterEv(
    const QAbstractSeriesPrivate *self) {
  return self->presenter();
}

//  QChart *QAbstractSeriesPrivate::chart()
extern "C" Q_DECL_EXPORT
QChart *ritual_ZN22QAbstractSeriesPrivate5chartEv(
    QAbstractSeriesPrivate *self) {
  return self->chart();
}

//  void QAbstractSeriesPrivate::setBlockOpenGL(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate14setBlockOpenGLEb(
    QAbstractSeriesPrivate *self,
    bool enable) {
  self->setBlockOpenGL(enable);
}

//  void QAbstractSeriesPrivate::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSeriesPrivate12countChangedEv(
    QAbstractSeriesPrivate *self) {
  self->countChanged();
}

//  a Python function taken by a CuteQAbstractSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSeriesPrivate(
    QAbstractSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSeriesPrivate *>(self)->take(key, call);
}

//  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSeriesPrivate9setDomainEP14AbstractDomain(
    QAbstractSeriesPrivate *self,
    AbstractDomain *domain) {
  self->QAbstractSeriesPrivate::setDomain(domain);
}

//  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSeriesPrivate12setPresenterEP14ChartPresenter(
    QAbstractSeriesPrivate *self,
    ChartPresenter *presenter) {
  self->QAbstractSeriesPrivate::setPresenter(presenter);
}
