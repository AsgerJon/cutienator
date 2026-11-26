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

//  A DeclarativeBarSeries that Python can take functions over in. Every DeclarativeBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativeBarSeriesCall0)(const void *, int *);
typedef void (*CuteDeclarativeBarSeriesCall1)(const void *, int *);
typedef int (*CuteDeclarativeBarSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeBarSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeBarSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeBarSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeBarSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeBarSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeBarSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeBarSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeBarSeries : public DeclarativeBarSeries {
public:
  using DeclarativeBarSeries::DeclarativeBarSeries;
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

  //  void DeclarativeBarSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeBarSeriesCall0 call = reinterpret_cast<CuteDeclarativeBarSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeBarSeries::classBegin();
  }

  //  void DeclarativeBarSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeBarSeriesCall1 call = reinterpret_cast<CuteDeclarativeBarSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeBarSeries::componentComplete();
  }

  //  QAbstractSeries::SeriesType QBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeBarSeriesCall2 call = reinterpret_cast<CuteDeclarativeBarSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeBarSeriesCall3 call = reinterpret_cast<CuteDeclarativeBarSeriesCall3>(taken[3]);
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
      CuteDeclarativeBarSeriesCall4 call = reinterpret_cast<CuteDeclarativeBarSeriesCall4>(taken[4]);
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
      CuteDeclarativeBarSeriesCall5 call = reinterpret_cast<CuteDeclarativeBarSeriesCall5>(taken[5]);
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
      CuteDeclarativeBarSeriesCall6 call = reinterpret_cast<CuteDeclarativeBarSeriesCall6>(taken[6]);
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
      CuteDeclarativeBarSeriesCall7 call = reinterpret_cast<CuteDeclarativeBarSeriesCall7>(taken[7]);
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
      CuteDeclarativeBarSeriesCall8 call = reinterpret_cast<CuteDeclarativeBarSeriesCall8>(taken[8]);
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
      CuteDeclarativeBarSeriesCall9 call = reinterpret_cast<CuteDeclarativeBarSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20DeclarativeBarSeries10metaObjectEv(
    const DeclarativeBarSeries *self) {
  return self->metaObject();
}

//  void *DeclarativeBarSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20DeclarativeBarSeries11qt_metacastEPKc(
    DeclarativeBarSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeBarSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20DeclarativeBarSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeBarSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeBarSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20DeclarativeBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeBarSeries::tr(s, c, n));
}

//  DeclarativeBarSeries::DeclarativeBarSeries(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
DeclarativeBarSeries *ritual_ZN20DeclarativeBarSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativeBarSeries(parent);
}

//  QAbstractAxis *DeclarativeBarSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN20DeclarativeBarSeries5axisXEv(
    DeclarativeBarSeries *self) {
  return self->axisX();
}

//  void DeclarativeBarSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries8setAxisXEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeBarSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN20DeclarativeBarSeries5axisYEv(
    DeclarativeBarSeries *self) {
  return self->axisY();
}

//  void DeclarativeBarSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries8setAxisYEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeBarSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN20DeclarativeBarSeries8axisXTopEv(
    DeclarativeBarSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeBarSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeBarSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN20DeclarativeBarSeries10axisYRightEv(
    DeclarativeBarSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeBarSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QQmlListProperty<QObject> DeclarativeBarSeries::seriesChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20DeclarativeBarSeries14seriesChildrenEv(
    DeclarativeBarSeries *self) {
  return new QQmlListProperty<QObject>(self->seriesChildren());
}

//  DeclarativeBarSet *DeclarativeBarSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN20DeclarativeBarSeries2atEi(
    DeclarativeBarSeries *self,
    int index) {
  return self->at(index);
}

//  DeclarativeBarSet *DeclarativeBarSeries::append(QString label,
//      QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN20DeclarativeBarSeries6appendE7QString5QListI8QVariantE(
    DeclarativeBarSeries *self,
    const QString *label,
    const QList<QVariant> *values) {
  return self->append(*label, *values);
}

//  DeclarativeBarSet *DeclarativeBarSeries::insert(int index, QString label,
//      QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN20DeclarativeBarSeries6insertEi7QString5QListI8QVariantE(
    DeclarativeBarSeries *self,
    int index,
    const QString *label,
    const QList<QVariant> *values) {
  return self->insert(index, *label, *values);
}

//  bool DeclarativeBarSeries::remove(QBarSet *barset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20DeclarativeBarSeries6removeEP7QBarSet(
    DeclarativeBarSeries *self,
    QBarSet *barset) {
  return self->remove(barset);
}

//  void DeclarativeBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries5clearEv(DeclarativeBarSeries *self) {
  self->clear();
}

//  void DeclarativeBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries10classBeginEv(
    DeclarativeBarSeries *self) {
  self->classBegin();
}

//  void DeclarativeBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries17componentCompleteEv(
    DeclarativeBarSeries *self) {
  self->componentComplete();
}

//  void DeclarativeBarSeries::axisXChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries12axisXChangedEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->axisXChanged(axis);
}

//  void DeclarativeBarSeries::axisYChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries12axisYChangedEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->axisYChanged(axis);
}

//  void DeclarativeBarSeries::axisXTopChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries15axisXTopChangedEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->axisXTopChanged(axis);
}

//  void DeclarativeBarSeries::axisYRightChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries17axisYRightChangedEP13QAbstractAxis(
    DeclarativeBarSeries *self,
    QAbstractAxis *axis) {
  self->axisYRightChanged(axis);
}

//  void DeclarativeBarSeries::appendSeriesChildren(QQmlListProperty<QObject>
//      *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeBarSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeBarSeries::appendSeriesChildren(list, element);
}

//  DeclarativeBarSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeBarSeries_QQmlParserStatus(
    DeclarativeBarSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteDeclarativeBarSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeBarSeries(
    DeclarativeBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeBarSeries *>(self)->take(key, call);
}

//  void DeclarativeBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20DeclarativeBarSeries10classBeginEv(
    DeclarativeBarSeries *self) {
  self->DeclarativeBarSeries::classBegin();
}

//  void DeclarativeBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20DeclarativeBarSeries17componentCompleteEv(
    DeclarativeBarSeries *self) {
  self->DeclarativeBarSeries::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativeBarSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativeBarSeries__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_bar_chart)
