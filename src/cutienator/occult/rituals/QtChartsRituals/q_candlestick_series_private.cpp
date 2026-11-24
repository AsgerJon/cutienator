//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qcandlestickseries_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qcandlestickseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qcandlestickseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCharts/qcandlestickset.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCandlestickSeriesPrivate that Python can take functions over in. Every QCandlestickSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCandlestickSeriesPrivateCall0)(const void *, int *);
typedef void (*CuteQCandlestickSeriesPrivateCall1)(const void *, int *);
typedef void (*CuteQCandlestickSeriesPrivateCall2)(const void *, int, ChartTheme *, bool, int *);
typedef void (*CuteQCandlestickSeriesPrivateCall3)(const void *, QGraphicsItem *, int *);
typedef int (*CuteQCandlestickSeriesPrivateCall4)(const void *, int, int *);
typedef void * (*CuteQCandlestickSeriesPrivateCall5)(const void *, int, int *);
typedef void (*CuteQCandlestickSeriesPrivateCall6)(const void *, AbstractDomain *, int *);
typedef void (*CuteQCandlestickSeriesPrivateCall7)(const void *, ChartPresenter *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickSeriesPrivateCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesPrivateCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesPrivateCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesPrivateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCandlestickSeriesPrivate : public QCandlestickSeriesPrivate {
public:
  using QCandlestickSeriesPrivate::QCandlestickSeriesPrivate;
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

  //  void QCandlestickSeriesPrivate::initializeDomain()
  void initializeDomain() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall0 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QCandlestickSeriesPrivate::initializeDomain();
  }

  //  void QCandlestickSeriesPrivate::initializeAxes()
  void initializeAxes() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall1 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QCandlestickSeriesPrivate::initializeAxes();
  }

  //  void QCandlestickSeriesPrivate::initializeTheme(int index, ChartTheme
  //      *theme, bool forced)
  void initializeTheme(int index, ChartTheme *theme, bool forced) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall2 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall2>(taken[2]);
      call(this, index, theme, forced, &handled);
      if (handled) return;
    }
    QCandlestickSeriesPrivate::initializeTheme(index, theme, forced);
  }

  //  void QCandlestickSeriesPrivate::initializeGraphics(QGraphicsItem
  //      *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall3 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall3>(taken[3]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QCandlestickSeriesPrivate::initializeGraphics(parent);
  }

  //  QAbstractAxis::AxisType
  //      QCandlestickSeriesPrivate::defaultAxisType(Qt::Orientation
  //      orientation) const
  QAbstractAxis::AxisType defaultAxisType(
      Qt::Orientation orientation) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall4 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall4>(taken[4]);
      int given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QCandlestickSeriesPrivate::defaultAxisType(orientation);
  }

  //  QAbstractAxis
  //      *QCandlestickSeriesPrivate::createDefaultAxis(Qt::Orientation
  //      orientation) const
  QAbstractAxis *createDefaultAxis(
      Qt::Orientation orientation) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall5 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall5>(taken[5]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstractAxis *>(given);
    }
    return QCandlestickSeriesPrivate::createDefaultAxis(orientation);
  }

  //  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
  void setDomain(AbstractDomain *domain) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall6 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall6>(taken[6]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QAbstractSeriesPrivate::setDomain(domain);
  }

  //  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCandlestickSeriesPrivateCall7 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall7>(taken[7]);
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
      CuteQCandlestickSeriesPrivateCall8 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall8>(taken[8]);
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
      CuteQCandlestickSeriesPrivateCall9 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall9>(taken[9]);
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
      CuteQCandlestickSeriesPrivateCall10 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall10>(taken[10]);
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
      CuteQCandlestickSeriesPrivateCall11 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall11>(taken[11]);
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
      CuteQCandlestickSeriesPrivateCall12 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall12>(taken[12]);
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
      CuteQCandlestickSeriesPrivateCall13 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall13>(taken[13]);
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
      CuteQCandlestickSeriesPrivateCall14 call = reinterpret_cast<CuteQCandlestickSeriesPrivateCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCandlestickSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QCandlestickSeriesPrivate10metaObjectEv(
    const QCandlestickSeriesPrivate *self) {
  return self->metaObject();
}

//  QString QCandlestickSeriesPrivate::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QCandlestickSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickSeriesPrivate::tr(s, c, n));
}

//  QCandlestickSeriesPrivate::QCandlestickSeriesPrivate(QCandlestickSeries
//      *q)
extern "C" Q_DECL_EXPORT
QCandlestickSeriesPrivate *ritual_ZN25QCandlestickSeriesPrivateC1EP18QCandlestickSeries(
    QCandlestickSeries *q) {
  return new CuteQCandlestickSeriesPrivate(q);
}

//  QCandlestickSeriesPrivate::~QCandlestickSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivateD1Ev(
    QCandlestickSeriesPrivate *self) {
  delete self;
}

//  void QCandlestickSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate16initializeDomainEv(
    QCandlestickSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QCandlestickSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate14initializeAxesEv(
    QCandlestickSeriesPrivate *self) {
  self->initializeAxes();
}

//  void QCandlestickSeriesPrivate::initializeTheme(int index, ChartTheme
//      *theme, bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QCandlestickSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  void QCandlestickSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QCandlestickSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  QList<QLegendMarker *>
//      QCandlestickSeriesPrivate::createLegendMarkers(QLegend *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN25QCandlestickSeriesPrivate19createLegendMarkersEP7QLegend(
    QCandlestickSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType
//      QCandlestickSeriesPrivate::defaultAxisType(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK25QCandlestickSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QCandlestickSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->defaultAxisType(orientation);
}

//  QAbstractAxis
//      *QCandlestickSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK25QCandlestickSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QCandlestickSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  bool QCandlestickSeriesPrivate::append(const QList<QCandlestickSet *>
//      &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QCandlestickSeriesPrivate6appendERK5QListIP15QCandlestickSetE(
    QCandlestickSeriesPrivate *self,
    const QList<QCandlestickSet *> *sets) {
  return self->append(*sets);
}

//  bool QCandlestickSeriesPrivate::remove(const QList<QCandlestickSet *>
//      &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QCandlestickSeriesPrivate6removeERK5QListIP15QCandlestickSetE(
    QCandlestickSeriesPrivate *self,
    const QList<QCandlestickSet *> *sets) {
  return self->remove(*sets);
}

//  bool QCandlestickSeriesPrivate::insert(int index, QCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QCandlestickSeriesPrivate6insertEiP15QCandlestickSet(
    QCandlestickSeriesPrivate *self,
    int index,
    QCandlestickSet *set) {
  return self->insert(index, set);
}

//  void QCandlestickSeriesPrivate::handleSeriesChange(QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate18handleSeriesChangeEP15QAbstractSeries(
    QCandlestickSeriesPrivate *self,
    QAbstractSeries *series) {
  self->handleSeriesChange(series);
}

//  void QCandlestickSeriesPrivate::handleSeriesRemove(QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate18handleSeriesRemoveEP15QAbstractSeries(
    QCandlestickSeriesPrivate *self,
    QAbstractSeries *series) {
  self->handleSeriesRemove(series);
}

//  void QCandlestickSeriesPrivate::populateBarCategories(QBarCategoryAxis
//      *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCandlestickSeriesPrivate21populateBarCategoriesEP16QBarCategoryAxis(
    QCandlestickSeriesPrivate *self,
    QBarCategoryAxis *axis) {
  self->populateBarCategories(axis);
}

//  QCandlestickSeries *QCandlestickSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCandlestickSeries *ritual_ZN25QCandlestickSeriesPrivate6q_funcEv(
    QCandlestickSeriesPrivate *self) {
  return self->q_func();
}

//  const QCandlestickSeries *QCandlestickSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCandlestickSeries *ritual_ZNK25QCandlestickSeriesPrivate6q_funcEv(
    const QCandlestickSeriesPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCandlestickSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCandlestickSeriesPrivate(
    QCandlestickSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCandlestickSeriesPrivate *>(self)->take(key, call);
}

//  void QCandlestickSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QCandlestickSeriesPrivate16initializeDomainEv(
    QCandlestickSeriesPrivate *self) {
  self->QCandlestickSeriesPrivate::initializeDomain();
}

//  void QCandlestickSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QCandlestickSeriesPrivate14initializeAxesEv(
    QCandlestickSeriesPrivate *self) {
  self->QCandlestickSeriesPrivate::initializeAxes();
}

//  void QCandlestickSeriesPrivate::initializeTheme(int index, ChartTheme
//      *theme, bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QCandlestickSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QCandlestickSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QCandlestickSeriesPrivate::initializeTheme(index, theme, forced);
}

//  void QCandlestickSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QCandlestickSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QCandlestickSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QCandlestickSeriesPrivate::initializeGraphics(parent);
}

//  QAbstractAxis::AxisType
//      QCandlestickSeriesPrivate::defaultAxisType(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK25QCandlestickSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QCandlestickSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QCandlestickSeriesPrivate::defaultAxisType(orientation);
}

//  QAbstractAxis
//      *QCandlestickSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_own_ZNK25QCandlestickSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QCandlestickSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QCandlestickSeriesPrivate::createDefaultAxis(orientation);
}
