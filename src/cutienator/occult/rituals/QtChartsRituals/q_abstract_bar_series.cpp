//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qabstractbarseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/qabstractbarseries.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/qbarset.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstractBarSeries that Python can take functions over in. Every QAbstractBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAbstractBarSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractBarSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractBarSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractBarSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractBarSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractBarSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractBarSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractBarSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractBarSeries : public QAbstractBarSeries {
public:
  using QAbstractBarSeries::QAbstractBarSeries;
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

  //  SeriesType QAbstractSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractBarSeriesCall0 call = reinterpret_cast<CuteQAbstractBarSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractBarSeriesCall1 call = reinterpret_cast<CuteQAbstractBarSeriesCall1>(taken[1]);
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
      CuteQAbstractBarSeriesCall2 call = reinterpret_cast<CuteQAbstractBarSeriesCall2>(taken[2]);
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
      CuteQAbstractBarSeriesCall3 call = reinterpret_cast<CuteQAbstractBarSeriesCall3>(taken[3]);
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
      CuteQAbstractBarSeriesCall4 call = reinterpret_cast<CuteQAbstractBarSeriesCall4>(taken[4]);
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
      CuteQAbstractBarSeriesCall5 call = reinterpret_cast<CuteQAbstractBarSeriesCall5>(taken[5]);
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
      CuteQAbstractBarSeriesCall6 call = reinterpret_cast<CuteQAbstractBarSeriesCall6>(taken[6]);
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
      CuteQAbstractBarSeriesCall7 call = reinterpret_cast<CuteQAbstractBarSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QAbstractBarSeries10metaObjectEv(
    const QAbstractBarSeries *self) {
  return self->metaObject();
}

//  void *QAbstractBarSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QAbstractBarSeries11qt_metacastEPKc(
    QAbstractBarSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractBarSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QAbstractBarSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractBarSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractBarSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QAbstractBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractBarSeries::tr(s, c, n));
}

//  QAbstractBarSeries::~QAbstractBarSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeriesD1Ev(QAbstractBarSeries *self) {
  delete self;
}

//  void QAbstractBarSeries::setBarWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries11setBarWidthEd(
    QAbstractBarSeries *self,
    qreal width) {
  self->setBarWidth(width);
}

//  qreal QAbstractBarSeries::barWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QAbstractBarSeries8barWidthEv(
    const QAbstractBarSeries *self) {
  return self->barWidth();
}

//  bool QAbstractBarSeries::append(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractBarSeries6appendEP7QBarSet(
    QAbstractBarSeries *self,
    QBarSet *set) {
  return self->append(set);
}

//  bool QAbstractBarSeries::remove(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractBarSeries6removeEP7QBarSet(
    QAbstractBarSeries *self,
    QBarSet *set) {
  return self->remove(set);
}

//  bool QAbstractBarSeries::take(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractBarSeries4takeEP7QBarSet(
    QAbstractBarSeries *self,
    QBarSet *set) {
  return self->take(set);
}

//  bool QAbstractBarSeries::append(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractBarSeries6appendERK5QListIP7QBarSetE(
    QAbstractBarSeries *self,
    const QList<QBarSet *> *sets) {
  return self->append(*sets);
}

//  bool QAbstractBarSeries::insert(int index, QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractBarSeries6insertEiP7QBarSet(
    QAbstractBarSeries *self,
    int index,
    QBarSet *set) {
  return self->insert(index, set);
}

//  int QAbstractBarSeries::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractBarSeries5countEv(const QAbstractBarSeries *self) {
  return self->count();
}

//  QList<QBarSet *> QAbstractBarSeries::barSets() const
extern "C" Q_DECL_EXPORT
QList<QBarSet *> *ritual_ZNK18QAbstractBarSeries7barSetsEv(
    const QAbstractBarSeries *self) {
  return new QList<QBarSet *>(self->barSets());
}

//  void QAbstractBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries5clearEv(QAbstractBarSeries *self) {
  self->clear();
}

//  void QAbstractBarSeries::setLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries16setLabelsVisibleEb(
    QAbstractBarSeries *self,
    bool visible) {
  self->setLabelsVisible(visible);
}

//  bool QAbstractBarSeries::isLabelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractBarSeries15isLabelsVisibleEv(
    const QAbstractBarSeries *self) {
  return self->isLabelsVisible();
}

//  void QAbstractBarSeries::setLabelsFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries15setLabelsFormatERK7QString(
    QAbstractBarSeries *self,
    const QString *format) {
  self->setLabelsFormat(*format);
}

//  QString QAbstractBarSeries::labelsFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QAbstractBarSeries12labelsFormatEv(
    const QAbstractBarSeries *self) {
  return new QString(self->labelsFormat());
}

//  void QAbstractBarSeries::setLabelsAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries14setLabelsAngleEd(
    QAbstractBarSeries *self,
    qreal angle) {
  self->setLabelsAngle(angle);
}

//  qreal QAbstractBarSeries::labelsAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QAbstractBarSeries11labelsAngleEv(
    const QAbstractBarSeries *self) {
  return self->labelsAngle();
}

//  void
//      QAbstractBarSeries::setLabelsPosition(QAbstractBarSeries::LabelsPosit
//      ion position)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries17setLabelsPositionENS_14LabelsPositionE(
    QAbstractBarSeries *self,
    QAbstractBarSeries::LabelsPosition position) {
  self->setLabelsPosition(position);
}

//  QAbstractBarSeries::LabelsPosition QAbstractBarSeries::labelsPosition()
//      const
extern "C" Q_DECL_EXPORT
QAbstractBarSeries::LabelsPosition ritual_ZNK18QAbstractBarSeries14labelsPositionEv(
    const QAbstractBarSeries *self) {
  return self->labelsPosition();
}

//  void QAbstractBarSeries::setLabelsPrecision(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries18setLabelsPrecisionEi(
    QAbstractBarSeries *self,
    int precision) {
  self->setLabelsPrecision(precision);
}

//  int QAbstractBarSeries::labelsPrecision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractBarSeries15labelsPrecisionEv(
    const QAbstractBarSeries *self) {
  return self->labelsPrecision();
}

//  QAbstractBarSeries::QAbstractBarSeries(QAbstractBarSeriesPrivate &d,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_ZN18QAbstractBarSeriesC1ER25QAbstractBarSeriesPrivateP7QObject(
    QAbstractBarSeriesPrivate *d,
    QObject *parent) {
  return new CuteQAbstractBarSeries(*d, parent);
}

//  void QAbstractBarSeries::clicked(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries7clickedEiP7QBarSet(
    QAbstractBarSeries *self,
    int index,
    QBarSet *barset) {
  self->clicked(index, barset);
}

//  void QAbstractBarSeries::hovered(bool status, int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries7hoveredEbiP7QBarSet(
    QAbstractBarSeries *self,
    bool status,
    int index,
    QBarSet *barset) {
  self->hovered(status, index, barset);
}

//  void QAbstractBarSeries::pressed(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries7pressedEiP7QBarSet(
    QAbstractBarSeries *self,
    int index,
    QBarSet *barset) {
  self->pressed(index, barset);
}

//  void QAbstractBarSeries::released(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries8releasedEiP7QBarSet(
    QAbstractBarSeries *self,
    int index,
    QBarSet *barset) {
  self->released(index, barset);
}

//  void QAbstractBarSeries::doubleClicked(int index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries13doubleClickedEiP7QBarSet(
    QAbstractBarSeries *self,
    int index,
    QBarSet *barset) {
  self->doubleClicked(index, barset);
}

//  void QAbstractBarSeries::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries12countChangedEv(
    QAbstractBarSeries *self) {
  self->countChanged();
}

//  void QAbstractBarSeries::labelsVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries20labelsVisibleChangedEv(
    QAbstractBarSeries *self) {
  self->labelsVisibleChanged();
}

//  void QAbstractBarSeries::labelsFormatChanged(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries19labelsFormatChangedERK7QString(
    QAbstractBarSeries *self,
    const QString *format) {
  self->labelsFormatChanged(*format);
}

//  void QAbstractBarSeries::labelsPositionChanged(QAbstractBarSeries::Labels
//      Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries21labelsPositionChangedENS_14LabelsPositionE(
    QAbstractBarSeries *self,
    QAbstractBarSeries::LabelsPosition position) {
  self->labelsPositionChanged(position);
}

//  void QAbstractBarSeries::labelsAngleChanged(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries18labelsAngleChangedEd(
    QAbstractBarSeries *self,
    qreal angle) {
  self->labelsAngleChanged(angle);
}

//  void QAbstractBarSeries::labelsPrecisionChanged(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries22labelsPrecisionChangedEi(
    QAbstractBarSeries *self,
    int precision) {
  self->labelsPrecisionChanged(precision);
}

//  void QAbstractBarSeries::barsetsAdded(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries12barsetsAddedERK5QListIP7QBarSetE(
    QAbstractBarSeries *self,
    const QList<QBarSet *> *sets) {
  self->barsetsAdded(*sets);
}

//  void QAbstractBarSeries::barsetsRemoved(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractBarSeries14barsetsRemovedERK5QListIP7QBarSetE(
    QAbstractBarSeries *self,
    const QList<QBarSet *> *sets) {
  self->barsetsRemoved(*sets);
}

//  QAbstractBarSeriesPrivate *QAbstractBarSeries::d_func()
extern "C" Q_DECL_EXPORT
QAbstractBarSeriesPrivate *ritual_ZN18QAbstractBarSeries6d_funcEv(
    QAbstractBarSeries *self) {
  return self->d_func();
}

//  const QAbstractBarSeriesPrivate *QAbstractBarSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractBarSeriesPrivate *ritual_ZNK18QAbstractBarSeries6d_funcEv(
    const QAbstractBarSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractBarSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractBarSeries(
    QAbstractBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractBarSeries *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_bar_chart)
