//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qpieseries_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/qpieseries.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qpieseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPieSeriesPrivate that Python can take functions over in. Every QPieSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPieSeriesPrivateCall0)(const void *, int *);
typedef void (*CuteQPieSeriesPrivateCall1)(const void *, int *);
typedef void (*CuteQPieSeriesPrivateCall2)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQPieSeriesPrivateCall3)(const void *, int, ChartTheme *, bool, int *);
typedef int (*CuteQPieSeriesPrivateCall4)(const void *, int, int *);
typedef void * (*CuteQPieSeriesPrivateCall5)(const void *, int, int *);
typedef void (*CuteQPieSeriesPrivateCall6)(const void *, AbstractDomain *, int *);
typedef void (*CuteQPieSeriesPrivateCall7)(const void *, ChartPresenter *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSeriesPrivateCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesPrivateCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesPrivateCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesPrivateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieSeriesPrivate : public QPieSeriesPrivate {
public:
  using QPieSeriesPrivate::QPieSeriesPrivate;
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
    if (!std::strcmp(key, "_ZN22QAbstractSeriesPrivate18initializeGraphicsEP13QGraphicsItem")) {
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

  //  void QPieSeriesPrivate::initializeDomain()
  void initializeDomain() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall0 call = reinterpret_cast<CuteQPieSeriesPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPieSeriesPrivate::initializeDomain();
  }

  //  void QPieSeriesPrivate::initializeAxes()
  void initializeAxes() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall1 call = reinterpret_cast<CuteQPieSeriesPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPieSeriesPrivate::initializeAxes();
  }

  //  void QPieSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall2 call = reinterpret_cast<CuteQPieSeriesPrivateCall2>(taken[2]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QPieSeriesPrivate::initializeGraphics(parent);
  }

  //  void QPieSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
  //      bool forced)
  void initializeTheme(int index, ChartTheme *theme, bool forced) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall3 call = reinterpret_cast<CuteQPieSeriesPrivateCall3>(taken[3]);
      call(this, index, theme, forced, &handled);
      if (handled) return;
    }
    QPieSeriesPrivate::initializeTheme(index, theme, forced);
  }

  //  QAbstractAxis::AxisType
  //      QPieSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
  //      const
  QAbstractAxis::AxisType defaultAxisType(
      Qt::Orientation orientation) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall4 call = reinterpret_cast<CuteQPieSeriesPrivateCall4>(taken[4]);
      int given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QPieSeriesPrivate::defaultAxisType(orientation);
  }

  //  QAbstractAxis *QPieSeriesPrivate::createDefaultAxis(Qt::Orientation
  //      orientation) const
  QAbstractAxis *createDefaultAxis(
      Qt::Orientation orientation) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall5 call = reinterpret_cast<CuteQPieSeriesPrivateCall5>(taken[5]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstractAxis *>(given);
    }
    return QPieSeriesPrivate::createDefaultAxis(orientation);
  }

  //  void QAbstractSeriesPrivate::setDomain(AbstractDomain *domain)
  void setDomain(AbstractDomain *domain) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall6 call = reinterpret_cast<CuteQPieSeriesPrivateCall6>(taken[6]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QAbstractSeriesPrivate::setDomain(domain);
  }

  //  void QAbstractSeriesPrivate::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPieSeriesPrivateCall7 call = reinterpret_cast<CuteQPieSeriesPrivateCall7>(taken[7]);
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
      CuteQPieSeriesPrivateCall8 call = reinterpret_cast<CuteQPieSeriesPrivateCall8>(taken[8]);
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
      CuteQPieSeriesPrivateCall9 call = reinterpret_cast<CuteQPieSeriesPrivateCall9>(taken[9]);
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
      CuteQPieSeriesPrivateCall10 call = reinterpret_cast<CuteQPieSeriesPrivateCall10>(taken[10]);
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
      CuteQPieSeriesPrivateCall11 call = reinterpret_cast<CuteQPieSeriesPrivateCall11>(taken[11]);
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
      CuteQPieSeriesPrivateCall12 call = reinterpret_cast<CuteQPieSeriesPrivateCall12>(taken[12]);
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
      CuteQPieSeriesPrivateCall13 call = reinterpret_cast<CuteQPieSeriesPrivateCall13>(taken[13]);
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
      CuteQPieSeriesPrivateCall14 call = reinterpret_cast<CuteQPieSeriesPrivateCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QPieSeriesPrivate10metaObjectEv(
    const QPieSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QPieSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QPieSeriesPrivate11qt_metacastEPKc(
    QPieSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPieSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPieSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QPieSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPieSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QPieSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieSeriesPrivate::tr(s, c, n));
}

//  QPieSeriesPrivate::QPieSeriesPrivate(QPieSeries *parent)
extern "C" Q_DECL_EXPORT
QPieSeriesPrivate *ritual_ZN17QPieSeriesPrivateC1EP10QPieSeries(
    QPieSeries *parent) {
  return new CuteQPieSeriesPrivate(parent);
}

//  QPieSeriesPrivate::~QPieSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivateD1Ev(QPieSeriesPrivate *self) {
  delete self;
}

//  void QPieSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate16initializeDomainEv(
    QPieSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QPieSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate14initializeAxesEv(
    QPieSeriesPrivate *self) {
  self->initializeAxes();
}

//  void QPieSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QPieSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QPieSeriesPrivate::initializeAnimations(QChart::AnimationOptions
//      options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QPieSeriesPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
}

//  void QPieSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QPieSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  QList<QLegendMarker *> QPieSeriesPrivate::createLegendMarkers(QLegend
//      *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN17QPieSeriesPrivate19createLegendMarkersEP7QLegend(
    QPieSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType
//      QPieSeriesPrivate::defaultAxisType(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK17QPieSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QPieSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->defaultAxisType(orientation);
}

//  QAbstractAxis *QPieSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK17QPieSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QPieSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  void QPieSeriesPrivate::updateDerivativeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate20updateDerivativeDataEv(
    QPieSeriesPrivate *self) {
  self->updateDerivativeData();
}

//  void QPieSeriesPrivate::setSizes(qreal innerSize, qreal outerSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate8setSizesEdd(
    QPieSeriesPrivate *self,
    qreal innerSize,
    qreal outerSize) {
  self->setSizes(innerSize, outerSize);
}

//  QPieSeriesPrivate *QPieSeriesPrivate::fromSeries(QPieSeries *series)
extern "C" Q_DECL_EXPORT
QPieSeriesPrivate *ritual_ZN17QPieSeriesPrivate10fromSeriesEP10QPieSeries(
    QPieSeries *series) {
  return QPieSeriesPrivate::fromSeries(series);
}

//  void QPieSeriesPrivate::calculatedDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate21calculatedDataChangedEv(
    QPieSeriesPrivate *self) {
  self->calculatedDataChanged();
}

//  void QPieSeriesPrivate::pieSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate14pieSizeChangedEv(
    QPieSeriesPrivate *self) {
  self->pieSizeChanged();
}

//  void QPieSeriesPrivate::pieStartAngleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate20pieStartAngleChangedEv(
    QPieSeriesPrivate *self) {
  self->pieStartAngleChanged();
}

//  void QPieSeriesPrivate::pieEndAngleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate18pieEndAngleChangedEv(
    QPieSeriesPrivate *self) {
  self->pieEndAngleChanged();
}

//  void QPieSeriesPrivate::horizontalPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate25horizontalPositionChangedEv(
    QPieSeriesPrivate *self) {
  self->horizontalPositionChanged();
}

//  void QPieSeriesPrivate::verticalPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate23verticalPositionChangedEv(
    QPieSeriesPrivate *self) {
  self->verticalPositionChanged();
}

//  void QPieSeriesPrivate::sliceValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate17sliceValueChangedEv(
    QPieSeriesPrivate *self) {
  self->sliceValueChanged();
}

//  void QPieSeriesPrivate::sliceClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate12sliceClickedEv(QPieSeriesPrivate *self) {
  self->sliceClicked();
}

//  void QPieSeriesPrivate::sliceHovered(bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate12sliceHoveredEb(
    QPieSeriesPrivate *self,
    bool state) {
  self->sliceHovered(state);
}

//  void QPieSeriesPrivate::slicePressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate12slicePressedEv(QPieSeriesPrivate *self) {
  self->slicePressed();
}

//  void QPieSeriesPrivate::sliceReleased()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate13sliceReleasedEv(QPieSeriesPrivate *self) {
  self->sliceReleased();
}

//  void QPieSeriesPrivate::sliceDoubleClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPieSeriesPrivate18sliceDoubleClickedEv(
    QPieSeriesPrivate *self) {
  self->sliceDoubleClicked();
}

//  QPieSeries *QPieSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZN17QPieSeriesPrivate6q_funcEv(QPieSeriesPrivate *self) {
  return self->q_func();
}

//  const QPieSeries *QPieSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPieSeries *ritual_ZNK17QPieSeriesPrivate6q_funcEv(
    const QPieSeriesPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQPieSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieSeriesPrivate(
    QPieSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPieSeriesPrivate *>(self)->take(key, call);
}

//  void QPieSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPieSeriesPrivate16initializeDomainEv(
    QPieSeriesPrivate *self) {
  self->QPieSeriesPrivate::initializeDomain();
}

//  void QPieSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPieSeriesPrivate14initializeAxesEv(
    QPieSeriesPrivate *self) {
  self->QPieSeriesPrivate::initializeAxes();
}

//  void QPieSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPieSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QPieSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QPieSeriesPrivate::initializeGraphics(parent);
}

//  void QPieSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPieSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QPieSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QPieSeriesPrivate::initializeTheme(index, theme, forced);
}

//  QAbstractAxis::AxisType
//      QPieSeriesPrivate::defaultAxisType(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK17QPieSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QPieSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QPieSeriesPrivate::defaultAxisType(orientation);
}

//  QAbstractAxis *QPieSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_own_ZNK17QPieSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QPieSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QPieSeriesPrivate::createDefaultAxis(orientation);
}

#endif  // QT_CONFIG(charts_pie_chart)
