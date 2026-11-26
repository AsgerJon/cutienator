//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartpresenter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartpresenter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartaxiselement_p.h>
#include <QtCharts/6.12.0/QtCharts/private/chartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtGui/qfont.h>
#include <QtCore/qlocale.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A ChartPresenter that Python can take functions over in. Every ChartPresenter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartPresenterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartPresenterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartPresenterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartPresenterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartPresenterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartPresenterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartPresenterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteChartPresenter : public ChartPresenter {
public:
  using ChartPresenter::ChartPresenter;
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
      CuteChartPresenterCall0 call = reinterpret_cast<CuteChartPresenterCall0>(taken[0]);
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
      CuteChartPresenterCall1 call = reinterpret_cast<CuteChartPresenterCall1>(taken[1]);
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
      CuteChartPresenterCall2 call = reinterpret_cast<CuteChartPresenterCall2>(taken[2]);
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
      CuteChartPresenterCall3 call = reinterpret_cast<CuteChartPresenterCall3>(taken[3]);
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
      CuteChartPresenterCall4 call = reinterpret_cast<CuteChartPresenterCall4>(taken[4]);
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
      CuteChartPresenterCall5 call = reinterpret_cast<CuteChartPresenterCall5>(taken[5]);
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
      CuteChartPresenterCall6 call = reinterpret_cast<CuteChartPresenterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ChartPresenter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14ChartPresenter10metaObjectEv(
    const ChartPresenter *self) {
  return self->metaObject();
}

//  void *ChartPresenter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14ChartPresenter11qt_metacastEPKc(
    ChartPresenter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ChartPresenter::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14ChartPresenter11qt_metacallEN11QMetaObject4CallEiPPv(
    ChartPresenter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ChartPresenter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14ChartPresenter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartPresenter::tr(s, c, n));
}

//  ChartPresenter::ChartPresenter(QChart *chart, QChart::ChartType type)
extern "C" Q_DECL_EXPORT
ChartPresenter *ritual_ZN14ChartPresenterC1EP6QChartNS0_9ChartTypeE(
    QChart *chart,
    QChart::ChartType type) {
  return new CuteChartPresenter(chart, type);
}

//  ChartPresenter::~ChartPresenter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenterD1Ev(ChartPresenter *self) {
  delete self;
}

//  bool ChartPresenter::isFixedGeometry() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14ChartPresenter15isFixedGeometryEv(
    const ChartPresenter *self) {
  return self->isFixedGeometry();
}

//  void ChartPresenter::setFixedGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter16setFixedGeometryERK6QRectF(
    ChartPresenter *self,
    const QRectF *rect) {
  self->setFixedGeometry(*rect);
}

//  void ChartPresenter::setGeometry(QRectF rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter11setGeometryE6QRectF(
    ChartPresenter *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QRectF ChartPresenter::geometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14ChartPresenter8geometryEv(const ChartPresenter *self) {
  return new QRectF(self->geometry());
}

//  void ChartPresenter::updateGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter14updateGeometryERK6QRectF(
    ChartPresenter *self,
    const QRectF *rect) {
  self->updateGeometry(*rect);
}

//  QGraphicsItem *ChartPresenter::rootItem()
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZN14ChartPresenter8rootItemEv(ChartPresenter *self) {
  return self->rootItem();
}

//  ChartBackground *ChartPresenter::backgroundElement()
extern "C" Q_DECL_EXPORT
ChartBackground *ritual_ZN14ChartPresenter17backgroundElementEv(
    ChartPresenter *self) {
  return self->backgroundElement();
}

//  QAbstractGraphicsShapeItem *ChartPresenter::plotAreaElement()
extern "C" Q_DECL_EXPORT
QAbstractGraphicsShapeItem *ritual_ZN14ChartPresenter15plotAreaElementEv(
    ChartPresenter *self) {
  return self->plotAreaElement();
}

//  ChartTitle *ChartPresenter::titleElement()
extern "C" Q_DECL_EXPORT
ChartTitle *ritual_ZN14ChartPresenter12titleElementEv(ChartPresenter *self) {
  return self->titleElement();
}

//  QList<ChartAxisElement *> ChartPresenter::axisItems() const
extern "C" Q_DECL_EXPORT
QList<ChartAxisElement *> *ritual_ZNK14ChartPresenter9axisItemsEv(
    const ChartPresenter *self) {
  return new QList<ChartAxisElement *>(self->axisItems());
}

//  QList<ChartItem *> ChartPresenter::chartItems() const
extern "C" Q_DECL_EXPORT
QList<ChartItem *> *ritual_ZNK14ChartPresenter10chartItemsEv(
    const ChartPresenter *self) {
  return new QList<ChartItem *>(self->chartItems());
}

//  QLegend *ChartPresenter::legend()
extern "C" Q_DECL_EXPORT
QLegend *ritual_ZN14ChartPresenter6legendEv(ChartPresenter *self) {
  return self->legend();
}

//  void ChartPresenter::setBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter18setBackgroundBrushERK6QBrush(
    ChartPresenter *self,
    const QBrush *brush) {
  self->setBackgroundBrush(*brush);
}

//  QBrush ChartPresenter::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14ChartPresenter15backgroundBrushEv(
    const ChartPresenter *self) {
  return new QBrush(self->backgroundBrush());
}

//  void ChartPresenter::setBackgroundPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter16setBackgroundPenERK4QPen(
    ChartPresenter *self,
    const QPen *pen) {
  self->setBackgroundPen(*pen);
}

//  QPen ChartPresenter::backgroundPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK14ChartPresenter13backgroundPenEv(
    const ChartPresenter *self) {
  return new QPen(self->backgroundPen());
}

//  void ChartPresenter::setBackgroundRoundness(qreal diameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter22setBackgroundRoundnessEd(
    ChartPresenter *self,
    qreal diameter) {
  self->setBackgroundRoundness(diameter);
}

//  qreal ChartPresenter::backgroundRoundness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14ChartPresenter19backgroundRoundnessEv(
    const ChartPresenter *self) {
  return self->backgroundRoundness();
}

//  void ChartPresenter::setPlotAreaBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter26setPlotAreaBackgroundBrushERK6QBrush(
    ChartPresenter *self,
    const QBrush *brush) {
  self->setPlotAreaBackgroundBrush(*brush);
}

//  QBrush ChartPresenter::plotAreaBackgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14ChartPresenter23plotAreaBackgroundBrushEv(
    const ChartPresenter *self) {
  return new QBrush(self->plotAreaBackgroundBrush());
}

//  void ChartPresenter::setPlotAreaBackgroundPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter24setPlotAreaBackgroundPenERK4QPen(
    ChartPresenter *self,
    const QPen *pen) {
  self->setPlotAreaBackgroundPen(*pen);
}

//  QPen ChartPresenter::plotAreaBackgroundPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK14ChartPresenter21plotAreaBackgroundPenEv(
    const ChartPresenter *self) {
  return new QPen(self->plotAreaBackgroundPen());
}

//  void ChartPresenter::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter8setTitleERK7QString(
    ChartPresenter *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString ChartPresenter::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14ChartPresenter5titleEv(const ChartPresenter *self) {
  return new QString(self->title());
}

//  void ChartPresenter::setTitleFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter12setTitleFontERK5QFont(
    ChartPresenter *self,
    const QFont *font) {
  self->setTitleFont(*font);
}

//  QFont ChartPresenter::titleFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14ChartPresenter9titleFontEv(const ChartPresenter *self) {
  return new QFont(self->titleFont());
}

//  void ChartPresenter::setTitleBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter13setTitleBrushERK6QBrush(
    ChartPresenter *self,
    const QBrush *brush) {
  self->setTitleBrush(*brush);
}

//  QBrush ChartPresenter::titleBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14ChartPresenter10titleBrushEv(
    const ChartPresenter *self) {
  return new QBrush(self->titleBrush());
}

//  void ChartPresenter::setBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter20setBackgroundVisibleEb(
    ChartPresenter *self,
    bool visible) {
  self->setBackgroundVisible(visible);
}

//  bool ChartPresenter::isBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14ChartPresenter19isBackgroundVisibleEv(
    const ChartPresenter *self) {
  return self->isBackgroundVisible();
}

//  void ChartPresenter::setPlotAreaBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter28setPlotAreaBackgroundVisibleEb(
    ChartPresenter *self,
    bool visible) {
  self->setPlotAreaBackgroundVisible(visible);
}

//  bool ChartPresenter::isPlotAreaBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14ChartPresenter27isPlotAreaBackgroundVisibleEv(
    const ChartPresenter *self) {
  return self->isPlotAreaBackgroundVisible();
}

//  void ChartPresenter::setBackgroundDropShadowEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter30setBackgroundDropShadowEnabledEb(
    ChartPresenter *self,
    bool enabled) {
  self->setBackgroundDropShadowEnabled(enabled);
}

//  bool ChartPresenter::isBackgroundDropShadowEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14ChartPresenter29isBackgroundDropShadowEnabledEv(
    const ChartPresenter *self) {
  return self->isBackgroundDropShadowEnabled();
}

//  void ChartPresenter::setLocalizeNumbers(bool localize)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter18setLocalizeNumbersEb(
    ChartPresenter *self,
    bool localize) {
  self->setLocalizeNumbers(localize);
}

//  bool ChartPresenter::localizeNumbers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14ChartPresenter15localizeNumbersEv(
    const ChartPresenter *self) {
  return self->localizeNumbers();
}

//  void ChartPresenter::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter9setLocaleERK7QLocale(
    ChartPresenter *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  const QLocale &ChartPresenter::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK14ChartPresenter6localeEv(const ChartPresenter *self) {
  return new QLocale(self->locale());
}

//  void ChartPresenter::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter10setVisibleEb(
    ChartPresenter *self,
    bool visible) {
  self->setVisible(visible);
}

//  void ChartPresenter::setAnimationOptions(QChart::AnimationOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter19setAnimationOptionsE6QFlagsIN6QChart15AnimationOptionEE(
    ChartPresenter *self,
    int options) {
  self->setAnimationOptions(
      QFlags<QChart::AnimationOption>::fromInt(options));
}

//  QChart::AnimationOptions ChartPresenter::animationOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14ChartPresenter16animationOptionsEv(
    const ChartPresenter *self) {
  return static_cast<int>(self->animationOptions().toInt());
}

//  void ChartPresenter::setAnimationDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter20setAnimationDurationEi(
    ChartPresenter *self,
    int msecs) {
  self->setAnimationDuration(msecs);
}

//  int ChartPresenter::animationDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14ChartPresenter17animationDurationEv(
    const ChartPresenter *self) {
  return self->animationDuration();
}

//  void ChartPresenter::setAnimationEasingCurve(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter23setAnimationEasingCurveERK12QEasingCurve(
    ChartPresenter *self,
    const QEasingCurve *curve) {
  self->setAnimationEasingCurve(*curve);
}

//  QEasingCurve ChartPresenter::animationEasingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK14ChartPresenter20animationEasingCurveEv(
    const ChartPresenter *self) {
  return new QEasingCurve(self->animationEasingCurve());
}

//  void ChartPresenter::startAnimation(ChartAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter14startAnimationEP14ChartAnimation(
    ChartPresenter *self,
    ChartAnimation *animation) {
  self->startAnimation(animation);
}

//  void ChartPresenter::setState(State state, QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter8setStateENS_5StateE7QPointF(
    ChartPresenter *self,
    ChartPresenter::State state,
    const QPointF *point) {
  self->setState(state, *point);
}

//  State ChartPresenter::state() const
extern "C" Q_DECL_EXPORT
ChartPresenter::State ritual_ZNK14ChartPresenter5stateEv(
    const ChartPresenter *self) {
  return self->state();
}

//  QPointF ChartPresenter::statePoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14ChartPresenter10statePointEv(
    const ChartPresenter *self) {
  return new QPointF(self->statePoint());
}

//  AbstractChartLayout *ChartPresenter::layout()
extern "C" Q_DECL_EXPORT
AbstractChartLayout *ritual_ZN14ChartPresenter6layoutEv(
    ChartPresenter *self) {
  return self->layout();
}

//  QChart::ChartType ChartPresenter::chartType() const
extern "C" Q_DECL_EXPORT
QChart::ChartType ritual_ZNK14ChartPresenter9chartTypeEv(
    const ChartPresenter *self) {
  return self->chartType();
}

//  QChart *ChartPresenter::chart()
extern "C" Q_DECL_EXPORT
QChart *ritual_ZN14ChartPresenter5chartEv(ChartPresenter *self) {
  return self->chart();
}

//  QRectF ChartPresenter::textBoundingRect(const QFont &font, const QString
//      &text, qreal angle)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN14ChartPresenter16textBoundingRectERK5QFontRK7QStringd(
    const QFont *font,
    const QString *text,
    qreal angle) {
  return new QRectF(ChartPresenter::textBoundingRect(*font, *text, angle));
}

//  QString ChartPresenter::truncatedText(const QFont &font, const QString
//      &text, qreal angle, qreal maxWidth, qreal maxHeight, QRectF
//      &boundingRect)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14ChartPresenter13truncatedTextERK5QFontRK7QStringdddR6QRectF(
    const QFont *font,
    const QString *text,
    qreal angle,
    qreal maxWidth,
    qreal maxHeight,
    QRectF *boundingRect) {
  return new QString(
      ChartPresenter::truncatedText(
          *font,
          *text,
          angle,
          maxWidth,
          maxHeight,
          *boundingRect));
}

//  qreal ChartPresenter::textMargin()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14ChartPresenter10textMarginEv() {
  return ChartPresenter::textMargin();
}

//  QString ChartPresenter::numberToString(double value, char f, int prec)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14ChartPresenter14numberToStringEdci(
    ChartPresenter *self,
    double value,
    char f,
    int prec) {
  return new QString(self->numberToString(value, f, prec));
}

//  QString ChartPresenter::numberToString(int value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14ChartPresenter14numberToStringEi(
    ChartPresenter *self,
    int value) {
  return new QString(self->numberToString(value));
}

//  void ChartPresenter::updateGLWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter14updateGLWidgetEv(ChartPresenter *self) {
  self->updateGLWidget();
}

//  void ChartPresenter::glSetUseWidget(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter14glSetUseWidgetEb(
    ChartPresenter *self,
    bool enable) {
  self->glSetUseWidget(enable);
}

//  void ChartPresenter::createBackgroundItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter20createBackgroundItemEv(
    ChartPresenter *self) {
  self->createBackgroundItem();
}

//  void ChartPresenter::createPlotAreaBackgroundItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter28createPlotAreaBackgroundItemEv(
    ChartPresenter *self) {
  self->createPlotAreaBackgroundItem();
}

//  void ChartPresenter::createTitleItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter15createTitleItemEv(ChartPresenter *self) {
  self->createTitleItem();
}

//  void ChartPresenter::handleSeriesAdded(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter17handleSeriesAddedEP15QAbstractSeries(
    ChartPresenter *self,
    QAbstractSeries *series) {
  self->handleSeriesAdded(series);
}

//  void ChartPresenter::handleSeriesRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter19handleSeriesRemovedEP15QAbstractSeries(
    ChartPresenter *self,
    QAbstractSeries *series) {
  self->handleSeriesRemoved(series);
}

//  void ChartPresenter::handleAxisAdded(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter15handleAxisAddedEP13QAbstractAxis(
    ChartPresenter *self,
    QAbstractAxis *axis) {
  self->handleAxisAdded(axis);
}

//  void ChartPresenter::handleAxisRemoved(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter17handleAxisRemovedEP13QAbstractAxis(
    ChartPresenter *self,
    QAbstractAxis *axis) {
  self->handleAxisRemoved(axis);
}

//  void ChartPresenter::plotAreaChanged(const QRectF &plotArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN14ChartPresenter15plotAreaChangedERK6QRectF(
    ChartPresenter *self,
    const QRectF *plotArea) {
  self->plotAreaChanged(*plotArea);
}

//  a Python function taken by a CuteChartPresenter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartPresenter(
    ChartPresenter *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartPresenter *>(self)->take(key, call);
}
