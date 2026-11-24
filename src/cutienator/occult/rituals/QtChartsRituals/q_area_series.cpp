//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qareaseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qareaseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAreaSeries that Python can take functions over in. Every QAreaSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAreaSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAreaSeries : public QAreaSeries {
public:
  using QAreaSeries::QAreaSeries;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QAreaSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAreaSeriesCall0 call = reinterpret_cast<CuteQAreaSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QAreaSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAreaSeriesCall1 call = reinterpret_cast<CuteQAreaSeriesCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAreaSeriesCall2 call = reinterpret_cast<CuteQAreaSeriesCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAreaSeriesCall3 call = reinterpret_cast<CuteQAreaSeriesCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAreaSeriesCall4 call = reinterpret_cast<CuteQAreaSeriesCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAreaSeriesCall5 call = reinterpret_cast<CuteQAreaSeriesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAreaSeriesCall6 call = reinterpret_cast<CuteQAreaSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAreaSeriesCall7 call = reinterpret_cast<CuteQAreaSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAreaSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QAreaSeries10metaObjectEv(
    const QAreaSeries *self) {
  return self->metaObject();
}

//  QString QAreaSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QAreaSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAreaSeries::tr(s, c, n));
}

//  QAreaSeries::QAreaSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN11QAreaSeriesC1EP7QObject(QObject *parent) {
  return new CuteQAreaSeries(parent);
}

//  QAreaSeries::QAreaSeries(QLineSeries *upperSeries, QLineSeries
//      *lowerSeries)
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN11QAreaSeriesC1EP11QLineSeriesS1_(
    QLineSeries *upperSeries,
    QLineSeries *lowerSeries) {
  return new CuteQAreaSeries(upperSeries, lowerSeries);
}

//  QAreaSeries::~QAreaSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeriesD1Ev(QAreaSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QAreaSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK11QAreaSeries4typeEv(
    const QAreaSeries *self) {
  return self->type();
}

//  void QAreaSeries::setUpperSeries(QLineSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setUpperSeriesEP11QLineSeries(
    QAreaSeries *self,
    QLineSeries *series) {
  self->setUpperSeries(series);
}

//  QLineSeries *QAreaSeries::upperSeries() const
extern "C" Q_DECL_EXPORT
QLineSeries *ritual_ZNK11QAreaSeries11upperSeriesEv(
    const QAreaSeries *self) {
  return self->upperSeries();
}

//  void QAreaSeries::setLowerSeries(QLineSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setLowerSeriesEP11QLineSeries(
    QAreaSeries *self,
    QLineSeries *series) {
  self->setLowerSeries(series);
}

//  QLineSeries *QAreaSeries::lowerSeries() const
extern "C" Q_DECL_EXPORT
QLineSeries *ritual_ZNK11QAreaSeries11lowerSeriesEv(
    const QAreaSeries *self) {
  return self->lowerSeries();
}

//  void QAreaSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries6setPenERK4QPen(
    QAreaSeries *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QAreaSeries::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK11QAreaSeries3penEv(const QAreaSeries *self) {
  return new QPen(self->pen());
}

//  void QAreaSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries8setBrushERK6QBrush(
    QAreaSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QAreaSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK11QAreaSeries5brushEv(const QAreaSeries *self) {
  return new QBrush(self->brush());
}

//  void QAreaSeries::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries8setColorERK6QColor(
    QAreaSeries *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QAreaSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries5colorEv(const QAreaSeries *self) {
  return new QColor(self->color());
}

//  void QAreaSeries::setBorderColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setBorderColorERK6QColor(
    QAreaSeries *self,
    const QColor *color) {
  self->setBorderColor(*color);
}

//  QColor QAreaSeries::borderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries11borderColorEv(const QAreaSeries *self) {
  return new QColor(self->borderColor());
}

//  void QAreaSeries::setPointsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries16setPointsVisibleEb(
    QAreaSeries *self,
    bool visible) {
  self->setPointsVisible(visible);
}

//  bool QAreaSeries::pointsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QAreaSeries13pointsVisibleEv(const QAreaSeries *self) {
  return self->pointsVisible();
}

//  void QAreaSeries::setPointLabelsFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries20setPointLabelsFormatERK7QString(
    QAreaSeries *self,
    const QString *format) {
  self->setPointLabelsFormat(*format);
}

//  QString QAreaSeries::pointLabelsFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QAreaSeries17pointLabelsFormatEv(
    const QAreaSeries *self) {
  return new QString(self->pointLabelsFormat());
}

//  void QAreaSeries::setPointLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries21setPointLabelsVisibleEb(
    QAreaSeries *self,
    bool visible) {
  self->setPointLabelsVisible(visible);
}

//  bool QAreaSeries::pointLabelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QAreaSeries18pointLabelsVisibleEv(const QAreaSeries *self) {
  return self->pointLabelsVisible();
}

//  void QAreaSeries::setPointLabelsFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries18setPointLabelsFontERK5QFont(
    QAreaSeries *self,
    const QFont *font) {
  self->setPointLabelsFont(*font);
}

//  QFont QAreaSeries::pointLabelsFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QAreaSeries15pointLabelsFontEv(const QAreaSeries *self) {
  return new QFont(self->pointLabelsFont());
}

//  void QAreaSeries::setPointLabelsColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries19setPointLabelsColorERK6QColor(
    QAreaSeries *self,
    const QColor *color) {
  self->setPointLabelsColor(*color);
}

//  QColor QAreaSeries::pointLabelsColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries16pointLabelsColorEv(
    const QAreaSeries *self) {
  return new QColor(self->pointLabelsColor());
}

//  void QAreaSeries::setPointLabelsClipping(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries22setPointLabelsClippingEb(
    QAreaSeries *self,
    bool enabled) {
  self->setPointLabelsClipping(enabled);
}

//  bool QAreaSeries::pointLabelsClipping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QAreaSeries19pointLabelsClippingEv(
    const QAreaSeries *self) {
  return self->pointLabelsClipping();
}

//  QAreaSeriesPrivate *QAreaSeries::d_func()
extern "C" Q_DECL_EXPORT
QAreaSeriesPrivate *ritual_ZN11QAreaSeries6d_funcEv(QAreaSeries *self) {
  return self->d_func();
}

//  const QAreaSeriesPrivate *QAreaSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QAreaSeriesPrivate *ritual_ZNK11QAreaSeries6d_funcEv(
    const QAreaSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAreaSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAreaSeries(
    QAreaSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAreaSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QAreaSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK11QAreaSeries4typeEv(
    const QAreaSeries *self) {
  return self->QAreaSeries::type();
}
