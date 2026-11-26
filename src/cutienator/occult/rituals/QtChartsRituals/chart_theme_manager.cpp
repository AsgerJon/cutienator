//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartthememanager_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the header of ChartTheme is included,
//  for QScopedPointer<ChartTheme> needs the complete type. Kept as it
//  is when the generator runs again.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartthememanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/charttheme_p.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A ChartThemeManager that Python can take functions over in. Every ChartThemeManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartThemeManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartThemeManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartThemeManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartThemeManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartThemeManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartThemeManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartThemeManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteChartThemeManager : public ChartThemeManager {
public:
  using ChartThemeManager::ChartThemeManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteChartThemeManagerCall0 call = reinterpret_cast<CuteChartThemeManagerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteChartThemeManagerCall1 call = reinterpret_cast<CuteChartThemeManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteChartThemeManagerCall2 call = reinterpret_cast<CuteChartThemeManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteChartThemeManagerCall3 call = reinterpret_cast<CuteChartThemeManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteChartThemeManagerCall4 call = reinterpret_cast<CuteChartThemeManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteChartThemeManagerCall5 call = reinterpret_cast<CuteChartThemeManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteChartThemeManagerCall6 call = reinterpret_cast<CuteChartThemeManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ChartThemeManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17ChartThemeManager10metaObjectEv(
    const ChartThemeManager *self) {
  return self->metaObject();
}

//  void *ChartThemeManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17ChartThemeManager11qt_metacastEPKc(
    ChartThemeManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString ChartThemeManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17ChartThemeManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartThemeManager::tr(s, c, n));
}

//  ChartThemeManager::ChartThemeManager(QChart *chart)
extern "C" Q_DECL_EXPORT
ChartThemeManager *ritual_ZN17ChartThemeManagerC1EP6QChart(QChart *chart) {
  return new CuteChartThemeManager(chart);
}

//  void ChartThemeManager::setTheme(QChart::ChartTheme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ChartThemeManager8setThemeEN6QChart10ChartThemeE(
    ChartThemeManager *self,
    QChart::ChartTheme theme) {
  self->setTheme(theme);
}

//  ChartTheme *ChartThemeManager::theme() const
extern "C" Q_DECL_EXPORT
ChartTheme *ritual_ZNK17ChartThemeManager5themeEv(
    const ChartThemeManager *self) {
  return self->theme();
}

//  void ChartThemeManager::decorateChart(QChart *chart, ChartTheme *theme)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17ChartThemeManager13decorateChartEP6QChartP10ChartTheme(
    const ChartThemeManager *self,
    QChart *chart,
    ChartTheme *theme) {
  self->decorateChart(chart, theme);
}

//  void ChartThemeManager::decorateLegend(QLegend *legend, ChartTheme
//      *theme) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17ChartThemeManager14decorateLegendEP7QLegendP10ChartTheme(
    const ChartThemeManager *self,
    QLegend *legend,
    ChartTheme *theme) {
  self->decorateLegend(legend, theme);
}

//  void ChartThemeManager::updateSeries(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ChartThemeManager12updateSeriesEP15QAbstractSeries(
    ChartThemeManager *self,
    QAbstractSeries *series) {
  self->updateSeries(series);
}

//  QList<QGradient> ChartThemeManager::generateSeriesGradients(const
//      QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
QList<QGradient> *ritual_ZN17ChartThemeManager23generateSeriesGradientsERK5QListI6QColorE(
    const QList<QColor> *colors) {
  return new QList<QGradient>(
      ChartThemeManager::generateSeriesGradients(
          *colors));
}

//  QColor ChartThemeManager::colorAt(const QColor &start, const QColor &end,
//      qreal pos)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17ChartThemeManager7colorAtERK6QColorS2_d(
    const QColor *start,
    const QColor *end,
    qreal pos) {
  return new QColor(ChartThemeManager::colorAt(*start, *end, pos));
}

//  QColor ChartThemeManager::colorAt(const QGradient &gradient, qreal pos)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17ChartThemeManager7colorAtERK9QGradientd(
    const QGradient *gradient,
    qreal pos) {
  return new QColor(ChartThemeManager::colorAt(*gradient, pos));
}

//  int ChartThemeManager::createIndexKey(const QList<int> &keys) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17ChartThemeManager14createIndexKeyERK5QListIiE(
    const ChartThemeManager *self,
    const QList<int> *keys) {
  return self->createIndexKey(*keys);
}

//  int ChartThemeManager::seriesCount(QAbstractSeries::SeriesType type)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17ChartThemeManager11seriesCountEN15QAbstractSeries10SeriesTypeE(
    const ChartThemeManager *self,
    QAbstractSeries::SeriesType type) {
  return self->seriesCount(type);
}

//  void ChartThemeManager::handleSeriesAdded(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ChartThemeManager17handleSeriesAddedEP15QAbstractSeries(
    ChartThemeManager *self,
    QAbstractSeries *series) {
  self->handleSeriesAdded(series);
}

//  void ChartThemeManager::handleSeriesRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ChartThemeManager19handleSeriesRemovedEP15QAbstractSeries(
    ChartThemeManager *self,
    QAbstractSeries *series) {
  self->handleSeriesRemoved(series);
}

//  void ChartThemeManager::handleAxisAdded(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ChartThemeManager15handleAxisAddedEP13QAbstractAxis(
    ChartThemeManager *self,
    QAbstractAxis *axis) {
  self->handleAxisAdded(axis);
}

//  void ChartThemeManager::handleAxisRemoved(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ChartThemeManager17handleAxisRemovedEP13QAbstractAxis(
    ChartThemeManager *self,
    QAbstractAxis *axis) {
  self->handleAxisRemoved(axis);
}

//  a Python function taken by a CuteChartThemeManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartThemeManager(
    ChartThemeManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartThemeManager *>(self)->take(key, call);
}
