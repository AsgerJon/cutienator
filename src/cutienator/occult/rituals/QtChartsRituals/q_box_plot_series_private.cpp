//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qboxplotseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qboxplotseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qboxplotseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCharts/qboxset.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBoxPlotSeriesPrivate that Python can take functions over in. Every QBoxPlotSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBoxPlotSeriesPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQBoxPlotSeriesPrivateCall1)(const void *, int *);
typedef void (*CuteQBoxPlotSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQBoxPlotSeriesPrivateCall3)(const void *, int, ChartTheme *, bool, int *);
typedef int (*CuteQBoxPlotSeriesPrivateCall4)(const void *, int, int *);
typedef void * (*CuteQBoxPlotSeriesPrivateCall5)(const void *, int, int *);
typedef void (*CuteQBoxPlotSeriesPrivateCall6)(const void *, AbstractDomain *, int *);
typedef void (*CuteQBoxPlotSeriesPrivateCall7)(const void *, ChartPresenter *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotSeriesPrivateCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesPrivateCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesPrivateCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesPrivateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxPlotSeriesPrivate : public QBoxPlotSeriesPrivate {
public:
  using QBoxPlotSeriesPrivate::QBoxPlotSeriesPrivate;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate18initializeGraphicsEP13QGraphicsItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate16initializeDomainEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate14initializeAxesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate15initializeThemeEiP10ChartThemeb")) {
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

  //  void QBoxPlotSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall0 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QBoxPlotSeriesPrivate::initializeGraphics(parent);
  }

  //  void QBoxPlotSeriesPrivate::initializeDomain()
  void initializeDomain() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall1 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QBoxPlotSeriesPrivate::initializeDomain();
  }

  //  void QBoxPlotSeriesPrivate::initializeAxes()
  void initializeAxes() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall2 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QBoxPlotSeriesPrivate::initializeAxes();
  }

  //  void QBoxPlotSeriesPrivate::initializeTheme(int index, ChartTheme
  //      *theme, bool forced)
  void initializeTheme(int index, ChartTheme *theme, bool forced) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall3 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall3>(taken[3]);
      call(this, index, theme, forced, &handled);
      if (handled) return;
    }
    QBoxPlotSeriesPrivate::initializeTheme(index, theme, forced);
  }

  //  QAbstractAxis::AxisType
  //      QBoxPlotSeriesPrivate::defaultAxisType(Qt::Orientation
  //      orientation) const
  QAbstractAxis::AxisType defaultAxisType(
      Qt::Orientation orientation) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall4 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall4>(taken[4]);
      int given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QBoxPlotSeriesPrivate::defaultAxisType(orientation);
  }

  //  QAbstractAxis
  //      *QBoxPlotSeriesPrivate::createDefaultAxis(Qt::Orientation
  //      orientation) const
  QAbstractAxis *createDefaultAxis(
      Qt::Orientation orientation) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall5 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall5>(taken[5]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstractAxis *>(given);
    }
    return QBoxPlotSeriesPrivate::createDefaultAxis(orientation);
  }

  //  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
  void setDomain(AbstractDomain *domain) override {
    if (taken[6]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall6 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall6>(taken[6]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QAbstractSeriesPrivate::setDomain(domain);
  }

  //  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[7]) {
      int handled = 0;
      CuteQBoxPlotSeriesPrivateCall7 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall7>(taken[7]);
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
      CuteQBoxPlotSeriesPrivateCall8 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall8>(taken[8]);
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
      CuteQBoxPlotSeriesPrivateCall9 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall9>(taken[9]);
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
      CuteQBoxPlotSeriesPrivateCall10 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall10>(taken[10]);
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
      CuteQBoxPlotSeriesPrivateCall11 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall11>(taken[11]);
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
      CuteQBoxPlotSeriesPrivateCall12 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall12>(taken[12]);
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
      CuteQBoxPlotSeriesPrivateCall13 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall13>(taken[13]);
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
      CuteQBoxPlotSeriesPrivateCall14 call = reinterpret_cast<CuteQBoxPlotSeriesPrivateCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxPlotSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QBoxPlotSeriesPrivate10metaObjectEv(
    const QBoxPlotSeriesPrivate *self) {
  return self->metaObject();
}

//  QString QBoxPlotSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QBoxPlotSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxPlotSeriesPrivate::tr(s, c, n));
}

//  QBoxPlotSeriesPrivate::QBoxPlotSeriesPrivate(QBoxPlotSeries *q)
extern "C" Q_DECL_EXPORT
QBoxPlotSeriesPrivate *ritual_ZN21QBoxPlotSeriesPrivateC1EP14QBoxPlotSeries(
    QBoxPlotSeries *q) {
  return new CuteQBoxPlotSeriesPrivate(q);
}

//  QBoxPlotSeriesPrivate::~QBoxPlotSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivateD1Ev(QBoxPlotSeriesPrivate *self) {
  delete self;
}

//  void QBoxPlotSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QBoxPlotSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QBoxPlotSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate16initializeDomainEv(
    QBoxPlotSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QBoxPlotSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate14initializeAxesEv(
    QBoxPlotSeriesPrivate *self) {
  self->initializeAxes();
}

//  void QBoxPlotSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QBoxPlotSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  QList<QLegendMarker *> QBoxPlotSeriesPrivate::createLegendMarkers(QLegend
//      *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN21QBoxPlotSeriesPrivate19createLegendMarkersEP7QLegend(
    QBoxPlotSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType
//      QBoxPlotSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK21QBoxPlotSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QBoxPlotSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->defaultAxisType(orientation);
}

//  QAbstractAxis *QBoxPlotSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK21QBoxPlotSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QBoxPlotSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  bool QBoxPlotSeriesPrivate::append(QBoxSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBoxPlotSeriesPrivate6appendEP7QBoxSet(
    QBoxPlotSeriesPrivate *self,
    QBoxSet *set) {
  return self->append(set);
}

//  bool QBoxPlotSeriesPrivate::remove(QBoxSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBoxPlotSeriesPrivate6removeEP7QBoxSet(
    QBoxPlotSeriesPrivate *self,
    QBoxSet *set) {
  return self->remove(set);
}

//  bool QBoxPlotSeriesPrivate::append(const QList<QBoxSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBoxPlotSeriesPrivate6appendERK5QListIP7QBoxSetE(
    QBoxPlotSeriesPrivate *self,
    const QList<QBoxSet *> *sets) {
  return self->append(*sets);
}

//  bool QBoxPlotSeriesPrivate::remove(const QList<QBoxSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBoxPlotSeriesPrivate6removeERK5QListIP7QBoxSetE(
    QBoxPlotSeriesPrivate *self,
    const QList<QBoxSet *> *sets) {
  return self->remove(*sets);
}

//  bool QBoxPlotSeriesPrivate::insert(int index, QBoxSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBoxPlotSeriesPrivate6insertEiP7QBoxSet(
    QBoxPlotSeriesPrivate *self,
    int index,
    QBoxSet *set) {
  return self->insert(index, set);
}

//  QBoxSet *QBoxPlotSeriesPrivate::boxSetAt(int index)
extern "C" Q_DECL_EXPORT
QBoxSet *ritual_ZN21QBoxPlotSeriesPrivate8boxSetAtEi(
    QBoxPlotSeriesPrivate *self,
    int index) {
  return self->boxSetAt(index);
}

//  qreal QBoxPlotSeriesPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN21QBoxPlotSeriesPrivate3maxEv(QBoxPlotSeriesPrivate *self) {
  return self->max();
}

//  qreal QBoxPlotSeriesPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN21QBoxPlotSeriesPrivate3minEv(QBoxPlotSeriesPrivate *self) {
  return self->min();
}

//  void QBoxPlotSeriesPrivate::populateCategories(QBarCategoryAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate18populateCategoriesEP16QBarCategoryAxis(
    QBoxPlotSeriesPrivate *self,
    QBarCategoryAxis *axis) {
  self->populateCategories(axis);
}

//  void QBoxPlotSeriesPrivate::handleSeriesChange(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate18handleSeriesChangeEP15QAbstractSeries(
    QBoxPlotSeriesPrivate *self,
    QAbstractSeries *series) {
  self->handleSeriesChange(series);
}

//  void QBoxPlotSeriesPrivate::handleSeriesRemove(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBoxPlotSeriesPrivate18handleSeriesRemoveEP15QAbstractSeries(
    QBoxPlotSeriesPrivate *self,
    QAbstractSeries *series) {
  self->handleSeriesRemove(series);
}

//  QBoxPlotSeries *QBoxPlotSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_ZN21QBoxPlotSeriesPrivate6q_funcEv(
    QBoxPlotSeriesPrivate *self) {
  return self->q_func();
}

//  const QBoxPlotSeries *QBoxPlotSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBoxPlotSeries *ritual_ZNK21QBoxPlotSeriesPrivate6q_funcEv(
    const QBoxPlotSeriesPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQBoxPlotSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxPlotSeriesPrivate(
    QBoxPlotSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBoxPlotSeriesPrivate *>(self)->take(key, call);
}

//  void QBoxPlotSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QBoxPlotSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QBoxPlotSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QBoxPlotSeriesPrivate::initializeGraphics(parent);
}

//  void QBoxPlotSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QBoxPlotSeriesPrivate16initializeDomainEv(
    QBoxPlotSeriesPrivate *self) {
  self->QBoxPlotSeriesPrivate::initializeDomain();
}

//  void QBoxPlotSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QBoxPlotSeriesPrivate14initializeAxesEv(
    QBoxPlotSeriesPrivate *self) {
  self->QBoxPlotSeriesPrivate::initializeAxes();
}

//  void QBoxPlotSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QBoxPlotSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QBoxPlotSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QBoxPlotSeriesPrivate::initializeTheme(index, theme, forced);
}

//  QAbstractAxis::AxisType
//      QBoxPlotSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK21QBoxPlotSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QBoxPlotSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QBoxPlotSeriesPrivate::defaultAxisType(orientation);
}

//  QAbstractAxis *QBoxPlotSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_own_ZNK21QBoxPlotSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QBoxPlotSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QBoxPlotSeriesPrivate::createDefaultAxis(orientation);
}

#endif  // QT_CONFIG(charts_boxplot_chart)
