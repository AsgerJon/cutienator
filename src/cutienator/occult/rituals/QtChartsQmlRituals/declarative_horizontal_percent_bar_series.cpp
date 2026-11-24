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

//  A DeclarativeHorizontalPercentBarSeries that Python can take functions over in. Every DeclarativeHorizontalPercentBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall0)(const void *, int *);
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall1)(const void *, int *);
typedef int (*CuteDeclarativeHorizontalPercentBarSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeHorizontalPercentBarSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeHorizontalPercentBarSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalPercentBarSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeHorizontalPercentBarSeries : public DeclarativeHorizontalPercentBarSeries {
public:
  using DeclarativeHorizontalPercentBarSeries::DeclarativeHorizontalPercentBarSeries;
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

  //  void DeclarativeHorizontalPercentBarSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeHorizontalPercentBarSeriesCall0 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeHorizontalPercentBarSeries::classBegin();
  }

  //  void DeclarativeHorizontalPercentBarSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeHorizontalPercentBarSeriesCall1 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeHorizontalPercentBarSeries::componentComplete();
  }

  //  QAbstractSeries::SeriesType QHorizontalPercentBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeHorizontalPercentBarSeriesCall2 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QHorizontalPercentBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeHorizontalPercentBarSeriesCall3 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall3>(taken[3]);
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
      CuteDeclarativeHorizontalPercentBarSeriesCall4 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall4>(taken[4]);
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
      CuteDeclarativeHorizontalPercentBarSeriesCall5 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall5>(taken[5]);
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
      CuteDeclarativeHorizontalPercentBarSeriesCall6 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall6>(taken[6]);
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
      CuteDeclarativeHorizontalPercentBarSeriesCall7 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall7>(taken[7]);
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
      CuteDeclarativeHorizontalPercentBarSeriesCall8 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall8>(taken[8]);
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
      CuteDeclarativeHorizontalPercentBarSeriesCall9 call = reinterpret_cast<CuteDeclarativeHorizontalPercentBarSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeHorizontalPercentBarSeries::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37DeclarativeHorizontalPercentBarSeries10metaObjectEv(
    const DeclarativeHorizontalPercentBarSeries *self) {
  return self->metaObject();
}

//  QString DeclarativeHorizontalPercentBarSeries::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN37DeclarativeHorizontalPercentBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeHorizontalPercentBarSeries::tr(s, c, n));
}

//  DeclarativeHorizontalPercentBarSeries::DeclarativeHorizontalPercentBarSer
//      ies(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
DeclarativeHorizontalPercentBarSeries *ritual_ZN37DeclarativeHorizontalPercentBarSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativeHorizontalPercentBarSeries(parent);
}

//  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN37DeclarativeHorizontalPercentBarSeries5axisXEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  return self->axisX();
}

//  void DeclarativeHorizontalPercentBarSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries8setAxisXEP13QAbstractAxis(
    DeclarativeHorizontalPercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN37DeclarativeHorizontalPercentBarSeries5axisYEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  return self->axisY();
}

//  void DeclarativeHorizontalPercentBarSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries8setAxisYEP13QAbstractAxis(
    DeclarativeHorizontalPercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN37DeclarativeHorizontalPercentBarSeries8axisXTopEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeHorizontalPercentBarSeries::setAxisXTop(QAbstractAxis
//      *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeHorizontalPercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeHorizontalPercentBarSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN37DeclarativeHorizontalPercentBarSeries10axisYRightEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeHorizontalPercentBarSeries::setAxisYRight(QAbstractAxis
//      *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeHorizontalPercentBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  DeclarativeBarSet *DeclarativeHorizontalPercentBarSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN37DeclarativeHorizontalPercentBarSeries2atEi(
    DeclarativeHorizontalPercentBarSeries *self,
    int index) {
  return self->at(index);
}

//  DeclarativeBarSet *DeclarativeHorizontalPercentBarSeries::append(QString
//      label, QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN37DeclarativeHorizontalPercentBarSeries6appendE7QString5QListI8QVariantE(
    DeclarativeHorizontalPercentBarSeries *self,
    const QString *label,
    const QList<QVariant> *values) {
  return self->append(*label, *values);
}

//  DeclarativeBarSet *DeclarativeHorizontalPercentBarSeries::insert(int
//      index, QString label, QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN37DeclarativeHorizontalPercentBarSeries6insertEi7QString5QListI8QVariantE(
    DeclarativeHorizontalPercentBarSeries *self,
    int index,
    const QString *label,
    const QList<QVariant> *values) {
  return self->insert(index, *label, *values);
}

//  bool DeclarativeHorizontalPercentBarSeries::remove(QBarSet *barset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN37DeclarativeHorizontalPercentBarSeries6removeEP7QBarSet(
    DeclarativeHorizontalPercentBarSeries *self,
    QBarSet *barset) {
  return self->remove(barset);
}

//  void DeclarativeHorizontalPercentBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries5clearEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  self->clear();
}

//  void DeclarativeHorizontalPercentBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries10classBeginEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  self->classBegin();
}

//  void DeclarativeHorizontalPercentBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN37DeclarativeHorizontalPercentBarSeries17componentCompleteEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  self->componentComplete();
}

//  DeclarativeHorizontalPercentBarSeries as the QQmlParserStatus it is built
//      on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeHorizontalPercentBarSeries_QQmlParserStatus(
    DeclarativeHorizontalPercentBarSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteDeclarativeHorizontalPercentBarSeries,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeHorizontalPercentBarSeries(
    DeclarativeHorizontalPercentBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeHorizontalPercentBarSeries *>(self)->take(key, call);
}

//  void DeclarativeHorizontalPercentBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37DeclarativeHorizontalPercentBarSeries10classBeginEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  self->DeclarativeHorizontalPercentBarSeries::classBegin();
}

//  void DeclarativeHorizontalPercentBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37DeclarativeHorizontalPercentBarSeries17componentCompleteEv(
    DeclarativeHorizontalPercentBarSeries *self) {
  self->DeclarativeHorizontalPercentBarSeries::componentComplete();
}

#endif  // QT_CONFIG(charts_bar_chart)
