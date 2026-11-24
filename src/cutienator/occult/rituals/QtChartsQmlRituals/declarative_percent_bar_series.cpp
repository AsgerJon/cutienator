//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A DeclarativePercentBarSeries that Python can take functions over in. Every DeclarativePercentBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativePercentBarSeriesCall0)(const void *, int *);
typedef void (*CuteDeclarativePercentBarSeriesCall1)(const void *, int *);
typedef int (*CuteDeclarativePercentBarSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativePercentBarSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativePercentBarSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePercentBarSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePercentBarSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePercentBarSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePercentBarSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativePercentBarSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativePercentBarSeries : public DeclarativePercentBarSeries {
public:
  using DeclarativePercentBarSeries::DeclarativePercentBarSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void DeclarativePercentBarSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall0 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativePercentBarSeries::classBegin();
  }

  //  void DeclarativePercentBarSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall1 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativePercentBarSeries::componentComplete();
  }

  //  QAbstractSeries::SeriesType QPercentBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall2 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QPercentBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall3 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall4 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall5 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall6 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall7 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall8 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteDeclarativePercentBarSeriesCall9 call = reinterpret_cast<CuteDeclarativePercentBarSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativePercentBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27DeclarativePercentBarSeries10metaObjectEv(
    const DeclarativePercentBarSeries *self) {
  return self->metaObject();
}

//  QString DeclarativePercentBarSeries::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27DeclarativePercentBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativePercentBarSeries::tr(s, c, n));
}

//  DeclarativePercentBarSeries::DeclarativePercentBarSeries(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
DeclarativePercentBarSeries *ritual_ZN27DeclarativePercentBarSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativePercentBarSeries(parent);
}

//  QAbstractAxis *DeclarativePercentBarSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativePercentBarSeries5axisXEv(
    DeclarativePercentBarSeries *self) {
  return self->axisX();
}

//  void DeclarativePercentBarSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries8setAxisXEP13QAbstractAxis(
    DeclarativePercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativePercentBarSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativePercentBarSeries5axisYEv(
    DeclarativePercentBarSeries *self) {
  return self->axisY();
}

//  void DeclarativePercentBarSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries8setAxisYEP13QAbstractAxis(
    DeclarativePercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativePercentBarSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativePercentBarSeries8axisXTopEv(
    DeclarativePercentBarSeries *self) {
  return self->axisXTop();
}

//  void DeclarativePercentBarSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativePercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativePercentBarSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativePercentBarSeries10axisYRightEv(
    DeclarativePercentBarSeries *self) {
  return self->axisYRight();
}

//  void DeclarativePercentBarSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativePercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  DeclarativeBarSet *DeclarativePercentBarSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN27DeclarativePercentBarSeries2atEi(
    DeclarativePercentBarSeries *self,
    int index) {
  return self->at(index);
}

//  DeclarativeBarSet *DeclarativePercentBarSeries::append(QString label,
//      QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN27DeclarativePercentBarSeries6appendE7QString5QListI8QVariantE(
    DeclarativePercentBarSeries *self,
    const QString *label,
    const QList<QVariant> *values) {
  return self->append(*label, *values);
}

//  DeclarativeBarSet *DeclarativePercentBarSeries::insert(int index, QString
//      label, QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN27DeclarativePercentBarSeries6insertEi7QString5QListI8QVariantE(
    DeclarativePercentBarSeries *self,
    int index,
    const QString *label,
    const QList<QVariant> *values) {
  return self->insert(index, *label, *values);
}

//  bool DeclarativePercentBarSeries::remove(QBarSet *barset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27DeclarativePercentBarSeries6removeEP7QBarSet(
    DeclarativePercentBarSeries *self,
    QBarSet *barset) {
  return self->remove(barset);
}

//  void DeclarativePercentBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries5clearEv(
    DeclarativePercentBarSeries *self) {
  self->clear();
}

//  void DeclarativePercentBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries10classBeginEv(
    DeclarativePercentBarSeries *self) {
  self->classBegin();
}

//  void DeclarativePercentBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativePercentBarSeries17componentCompleteEv(
    DeclarativePercentBarSeries *self) {
  self->componentComplete();
}

//  DeclarativePercentBarSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativePercentBarSeries_QQmlParserStatus(
    DeclarativePercentBarSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteDeclarativePercentBarSeries, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativePercentBarSeries(
    DeclarativePercentBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativePercentBarSeries *>(self)->take(key, call);
}

//  void DeclarativePercentBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativePercentBarSeries10classBeginEv(
    DeclarativePercentBarSeries *self) {
  self->DeclarativePercentBarSeries::classBegin();
}

//  void DeclarativePercentBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativePercentBarSeries17componentCompleteEv(
    DeclarativePercentBarSeries *self) {
  self->DeclarativePercentBarSeries::componentComplete();
}

#endif  // QT_CONFIG(charts_bar_chart)
