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
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A DeclarativeStackedBarSeries that Python can take functions over in. Every DeclarativeStackedBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativeStackedBarSeriesCall0)(const void *, int *);
typedef void (*CuteDeclarativeStackedBarSeriesCall1)(const void *, int *);
typedef int (*CuteDeclarativeStackedBarSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeStackedBarSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeStackedBarSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeStackedBarSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeStackedBarSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeStackedBarSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeStackedBarSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeStackedBarSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeStackedBarSeries : public DeclarativeStackedBarSeries {
public:
  using DeclarativeStackedBarSeries::DeclarativeStackedBarSeries;
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

  //  void DeclarativeStackedBarSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeStackedBarSeriesCall0 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeStackedBarSeries::classBegin();
  }

  //  void DeclarativeStackedBarSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeStackedBarSeriesCall1 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeStackedBarSeries::componentComplete();
  }

  //  QAbstractSeries::SeriesType QStackedBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeStackedBarSeriesCall2 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QStackedBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeStackedBarSeriesCall3 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall3>(taken[3]);
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
      CuteDeclarativeStackedBarSeriesCall4 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall4>(taken[4]);
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
      CuteDeclarativeStackedBarSeriesCall5 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall5>(taken[5]);
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
      CuteDeclarativeStackedBarSeriesCall6 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall6>(taken[6]);
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
      CuteDeclarativeStackedBarSeriesCall7 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall7>(taken[7]);
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
      CuteDeclarativeStackedBarSeriesCall8 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall8>(taken[8]);
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
      CuteDeclarativeStackedBarSeriesCall9 call = reinterpret_cast<CuteDeclarativeStackedBarSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeStackedBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27DeclarativeStackedBarSeries10metaObjectEv(
    const DeclarativeStackedBarSeries *self) {
  return self->metaObject();
}

//  void *DeclarativeStackedBarSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27DeclarativeStackedBarSeries11qt_metacastEPKc(
    DeclarativeStackedBarSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeStackedBarSeries::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27DeclarativeStackedBarSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeStackedBarSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeStackedBarSeries::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27DeclarativeStackedBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeStackedBarSeries::tr(s, c, n));
}

//  DeclarativeStackedBarSeries::DeclarativeStackedBarSeries(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
DeclarativeStackedBarSeries *ritual_ZN27DeclarativeStackedBarSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativeStackedBarSeries(parent);
}

//  QAbstractAxis *DeclarativeStackedBarSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativeStackedBarSeries5axisXEv(
    DeclarativeStackedBarSeries *self) {
  return self->axisX();
}

//  void DeclarativeStackedBarSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries8setAxisXEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeStackedBarSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativeStackedBarSeries5axisYEv(
    DeclarativeStackedBarSeries *self) {
  return self->axisY();
}

//  void DeclarativeStackedBarSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries8setAxisYEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeStackedBarSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativeStackedBarSeries8axisXTopEv(
    DeclarativeStackedBarSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeStackedBarSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeStackedBarSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN27DeclarativeStackedBarSeries10axisYRightEv(
    DeclarativeStackedBarSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeStackedBarSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QQmlListProperty<QObject> DeclarativeStackedBarSeries::seriesChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN27DeclarativeStackedBarSeries14seriesChildrenEv(
    DeclarativeStackedBarSeries *self) {
  return new QQmlListProperty<QObject>(self->seriesChildren());
}

//  DeclarativeBarSet *DeclarativeStackedBarSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN27DeclarativeStackedBarSeries2atEi(
    DeclarativeStackedBarSeries *self,
    int index) {
  return self->at(index);
}

//  DeclarativeBarSet *DeclarativeStackedBarSeries::append(QString label,
//      QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN27DeclarativeStackedBarSeries6appendE7QString5QListI8QVariantE(
    DeclarativeStackedBarSeries *self,
    const QString *label,
    const QList<QVariant> *values) {
  return self->append(*label, *values);
}

//  DeclarativeBarSet *DeclarativeStackedBarSeries::insert(int index, QString
//      label, QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN27DeclarativeStackedBarSeries6insertEi7QString5QListI8QVariantE(
    DeclarativeStackedBarSeries *self,
    int index,
    const QString *label,
    const QList<QVariant> *values) {
  return self->insert(index, *label, *values);
}

//  bool DeclarativeStackedBarSeries::remove(QBarSet *barset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27DeclarativeStackedBarSeries6removeEP7QBarSet(
    DeclarativeStackedBarSeries *self,
    QBarSet *barset) {
  return self->remove(barset);
}

//  void DeclarativeStackedBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries5clearEv(
    DeclarativeStackedBarSeries *self) {
  self->clear();
}

//  void DeclarativeStackedBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries10classBeginEv(
    DeclarativeStackedBarSeries *self) {
  self->classBegin();
}

//  void DeclarativeStackedBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries17componentCompleteEv(
    DeclarativeStackedBarSeries *self) {
  self->componentComplete();
}

//  void DeclarativeStackedBarSeries::axisXChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries12axisXChangedEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->axisXChanged(axis);
}

//  void DeclarativeStackedBarSeries::axisYChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries12axisYChangedEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->axisYChanged(axis);
}

//  void DeclarativeStackedBarSeries::axisXTopChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries15axisXTopChangedEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->axisXTopChanged(axis);
}

//  void DeclarativeStackedBarSeries::axisYRightChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries17axisYRightChangedEP13QAbstractAxis(
    DeclarativeStackedBarSeries *self,
    QAbstractAxis *axis) {
  self->axisYRightChanged(axis);
}

//  void DeclarativeStackedBarSeries::appendSeriesChildren(QQmlListProperty<Q
//      Object> *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeStackedBarSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeStackedBarSeries::appendSeriesChildren(list, element);
}

//  DeclarativeStackedBarSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeStackedBarSeries_QQmlParserStatus(
    DeclarativeStackedBarSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteDeclarativeStackedBarSeries, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeStackedBarSeries(
    DeclarativeStackedBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeStackedBarSeries *>(self)->take(key, call);
}

//  void DeclarativeStackedBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativeStackedBarSeries10classBeginEv(
    DeclarativeStackedBarSeries *self) {
  self->DeclarativeStackedBarSeries::classBegin();
}

//  void DeclarativeStackedBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativeStackedBarSeries17componentCompleteEv(
    DeclarativeStackedBarSeries *self) {
  self->DeclarativeStackedBarSeries::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativeStackedBarSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativeStackedBarSeries__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_bar_chart)
