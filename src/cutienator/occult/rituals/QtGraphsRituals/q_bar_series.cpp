//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qbarseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarset.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QBarSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQBarSeries : QBarSeries {
  using QBarSeries::componentComplete;
};

//  A QBarSeries that Python can take functions over in. Every QBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQBarSeriesCall0)(const void *, int *);
typedef void (*CuteQBarSeriesCall1)(const void *, int *);
typedef void (*CuteQBarSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarSeries : public QBarSeries {
public:
  using QBarSeries::QBarSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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

  //  QAbstractSeries::SeriesType QBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarSeriesCall0 call = reinterpret_cast<CuteQBarSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QBarSeries::type();
  }

  //  void QBarSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarSeriesCall1 call = reinterpret_cast<CuteQBarSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QBarSeries::componentComplete();
  }

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBarSeriesCall2 call = reinterpret_cast<CuteQBarSeriesCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBarSeriesCall3 call = reinterpret_cast<CuteQBarSeriesCall3>(taken[3]);
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
      CuteQBarSeriesCall4 call = reinterpret_cast<CuteQBarSeriesCall4>(taken[4]);
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
      CuteQBarSeriesCall5 call = reinterpret_cast<CuteQBarSeriesCall5>(taken[5]);
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
      CuteQBarSeriesCall6 call = reinterpret_cast<CuteQBarSeriesCall6>(taken[6]);
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
      CuteQBarSeriesCall7 call = reinterpret_cast<CuteQBarSeriesCall7>(taken[7]);
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
      CuteQBarSeriesCall8 call = reinterpret_cast<CuteQBarSeriesCall8>(taken[8]);
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
      CuteQBarSeriesCall9 call = reinterpret_cast<CuteQBarSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QBarSeries10metaObjectEv(
    const QBarSeries *self) {
  return self->metaObject();
}

//  void *QBarSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QBarSeries11qt_metacastEPKc(
    QBarSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QBarSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBarSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarSeries::tr(s, c, n));
}

//  QBarSeries::QBarSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QBarSeries *ritual_ZN10QBarSeriesC1EP7QObject(QObject *parent) {
  return new CuteQBarSeries(parent);
}

//  QBarSeries::~QBarSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeriesD1Ev(QBarSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK10QBarSeries4typeEv(
    const QBarSeries *self) {
  return self->type();
}

//  QList<QColor> QBarSeries::seriesColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK10QBarSeries12seriesColorsEv(
    const QBarSeries *self) {
  return new QList<QColor>(self->seriesColors());
}

//  void QBarSeries::setSeriesColors(const QList<QColor> &newSeriesColors)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15setSeriesColorsERK5QListI6QColorE(
    QBarSeries *self,
    const QList<QColor> *newSeriesColors) {
  self->setSeriesColors(*newSeriesColors);
}

//  QList<QColor> QBarSeries::borderColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK10QBarSeries12borderColorsEv(
    const QBarSeries *self) {
  return new QList<QColor>(self->borderColors());
}

//  void QBarSeries::setBorderColors(const QList<QColor> &newBorderColors)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15setBorderColorsERK5QListI6QColorE(
    QBarSeries *self,
    const QList<QColor> *newBorderColors) {
  self->setBorderColors(*newBorderColors);
}

//  void QBarSeries::setBarsType(QBarSeries::BarsType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries11setBarsTypeENS_8BarsTypeE(
    QBarSeries *self,
    QBarSeries::BarsType type) {
  self->setBarsType(type);
}

//  QBarSeries::BarsType QBarSeries::barsType() const
extern "C" Q_DECL_EXPORT
QBarSeries::BarsType ritual_ZNK10QBarSeries8barsTypeEv(
    const QBarSeries *self) {
  return self->barsType();
}

//  void QBarSeries::setBarWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries11setBarWidthEd(QBarSeries *self, qreal width) {
  self->setBarWidth(width);
}

//  qreal QBarSeries::barWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QBarSeries8barWidthEv(const QBarSeries *self) {
  return self->barWidth();
}

//  bool QBarSeries::append(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries6appendEP7QBarSet(QBarSeries *self, QBarSet *set) {
  return self->append(set);
}

//  bool QBarSeries::take(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries4takeEP7QBarSet(QBarSeries *self, QBarSet *set) {
  return self->take(set);
}

//  qsizetype QBarSeries::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QBarSeries5countEv(const QBarSeries *self) {
  return self->count();
}

//  bool QBarSeries::append(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries6appendERK5QListIP7QBarSetE(
    QBarSeries *self,
    const QList<QBarSet *> *sets) {
  return self->append(*sets);
}

//  bool QBarSeries::remove(QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries6removeEP7QBarSet(QBarSeries *self, QBarSet *set) {
  return self->remove(set);
}

//  bool QBarSeries::insert(qsizetype index, QBarSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries6insertExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *set) {
  return self->insert(index, set);
}

//  void QBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries5clearEv(QBarSeries *self) {
  self->clear();
}

//  void QBarSeries::replace(qsizetype index, QBarSet *set)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries7replaceExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *set) {
  self->replace(index, set);
}

//  QBarSet *QBarSeries::at(qsizetype index)
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN10QBarSeries2atEx(QBarSeries *self, qsizetype index) {
  return self->at(index);
}

//  qsizetype QBarSeries::find(QBarSet *set) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QBarSeries4findEP7QBarSet(
    const QBarSeries *self,
    QBarSet *set) {
  return self->find(set);
}

//  void QBarSeries::removeMultiple(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries14removeMultipleExx(
    QBarSeries *self,
    qsizetype index,
    qsizetype count) {
  self->removeMultiple(index, count);
}

//  bool QBarSeries::remove(qsizetype index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries6removeEx(QBarSeries *self, qsizetype index) {
  return self->remove(index);
}

//  bool QBarSeries::replace(QBarSet *oldValue, QBarSet *newValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries7replaceEP7QBarSetS1_(
    QBarSeries *self,
    QBarSet *oldValue,
    QBarSet *newValue) {
  return self->replace(oldValue, newValue);
}

//  bool QBarSeries::replace(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBarSeries7replaceERK5QListIP7QBarSetE(
    QBarSeries *self,
    const QList<QBarSet *> *sets) {
  return self->replace(*sets);
}

//  QList<QBarSet *> QBarSeries::barSets() const
extern "C" Q_DECL_EXPORT
QList<QBarSet *> *ritual_ZNK10QBarSeries7barSetsEv(const QBarSeries *self) {
  return new QList<QBarSet *>(self->barSets());
}

//  void QBarSeries::setLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries16setLabelsVisibleEb(
    QBarSeries *self,
    bool visible) {
  self->setLabelsVisible(visible);
}

//  bool QBarSeries::labelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBarSeries13labelsVisibleEv(const QBarSeries *self) {
  return self->labelsVisible();
}

//  void QBarSeries::setLabelsFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15setLabelsFormatERK7QString(
    QBarSeries *self,
    const QString *format) {
  self->setLabelsFormat(*format);
}

//  QString QBarSeries::labelsFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QBarSeries12labelsFormatEv(const QBarSeries *self) {
  return new QString(self->labelsFormat());
}

//  void QBarSeries::setLabelsMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15setLabelsMarginEd(
    QBarSeries *self,
    qreal margin) {
  self->setLabelsMargin(margin);
}

//  qreal QBarSeries::labelsMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QBarSeries12labelsMarginEv(const QBarSeries *self) {
  return self->labelsMargin();
}

//  void QBarSeries::setLabelsAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries14setLabelsAngleEd(QBarSeries *self, qreal angle) {
  self->setLabelsAngle(angle);
}

//  qreal QBarSeries::labelsAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QBarSeries11labelsAngleEv(const QBarSeries *self) {
  return self->labelsAngle();
}

//  void QBarSeries::setLabelsPosition(QBarSeries::LabelsPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries17setLabelsPositionENS_14LabelsPositionE(
    QBarSeries *self,
    QBarSeries::LabelsPosition position) {
  self->setLabelsPosition(position);
}

//  QBarSeries::LabelsPosition QBarSeries::labelsPosition() const
extern "C" Q_DECL_EXPORT
QBarSeries::LabelsPosition ritual_ZNK10QBarSeries14labelsPositionEv(
    const QBarSeries *self) {
  return self->labelsPosition();
}

//  void QBarSeries::setLabelsPrecision(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries18setLabelsPrecisionEi(
    QBarSeries *self,
    int precision) {
  self->setLabelsPrecision(precision);
}

//  int QBarSeries::labelsPrecision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QBarSeries15labelsPrecisionEv(const QBarSeries *self) {
  return self->labelsPrecision();
}

//  QQmlComponent *QBarSeries::barDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK10QBarSeries11barDelegateEv(
    const QBarSeries *self) {
  return self->barDelegate();
}

//  void QBarSeries::setBarDelegate(QQmlComponent *newBarDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries14setBarDelegateEP13QQmlComponent(
    QBarSeries *self,
    QQmlComponent *newBarDelegate) {
  self->setBarDelegate(newBarDelegate);
}

//  void QBarSeries::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries9selectAllEv(QBarSeries *self) {
  self->selectAll();
}

//  void QBarSeries::deselectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries11deselectAllEv(QBarSeries *self) {
  self->deselectAll();
}

//  QBarSeries::QBarSeries(QBarSeriesPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QBarSeries *ritual_ZN10QBarSeriesC1ER17QBarSeriesPrivateP7QObject(
    QBarSeriesPrivate *dd,
    QObject *parent) {
  return new CuteQBarSeries(*dd, parent);
}

//  void QBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries17componentCompleteEv(QBarSeries *self) {
  self->componentComplete();
}

//  void QBarSeries::updatedBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries11updatedBarsEv(QBarSeries *self) {
  self->updatedBars();
}

//  void QBarSeries::seriesColorsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries19seriesColorsChangedEv(QBarSeries *self) {
  self->seriesColorsChanged();
}

//  void QBarSeries::borderColorsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries19borderColorsChangedEv(QBarSeries *self) {
  self->borderColorsChanged();
}

//  void QBarSeries::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries12countChangedEv(QBarSeries *self) {
  self->countChanged();
}

//  void QBarSeries::barWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15barWidthChangedEv(QBarSeries *self) {
  self->barWidthChanged();
}

//  void QBarSeries::labelsVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries20labelsVisibleChangedEb(
    QBarSeries *self,
    bool visible) {
  self->labelsVisibleChanged(visible);
}

//  void QBarSeries::labelsFormatChanged(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries19labelsFormatChangedERK7QString(
    QBarSeries *self,
    const QString *format) {
  self->labelsFormatChanged(*format);
}

//  void QBarSeries::labelsPositionChanged(QBarSeries::LabelsPosition
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries21labelsPositionChangedENS_14LabelsPositionE(
    QBarSeries *self,
    QBarSeries::LabelsPosition position) {
  self->labelsPositionChanged(position);
}

//  void QBarSeries::barsTypeChanged(QBarSeries::BarsType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15barsTypeChangedENS_8BarsTypeE(
    QBarSeries *self,
    QBarSeries::BarsType type) {
  self->barsTypeChanged(type);
}

//  void QBarSeries::labelsMarginChanged(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries19labelsMarginChangedEd(
    QBarSeries *self,
    qreal margin) {
  self->labelsMarginChanged(margin);
}

//  void QBarSeries::labelsAngleChanged(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries18labelsAngleChangedEd(
    QBarSeries *self,
    qreal angle) {
  self->labelsAngleChanged(angle);
}

//  void QBarSeries::labelsPrecisionChanged(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries22labelsPrecisionChangedEi(
    QBarSeries *self,
    int precision) {
  self->labelsPrecisionChanged(precision);
}

//  void QBarSeries::barDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries18barDelegateChangedEv(QBarSeries *self) {
  self->barDelegateChanged();
}

//  void QBarSeries::barsetsAdded(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries12barsetsAddedERK5QListIP7QBarSetE(
    QBarSeries *self,
    const QList<QBarSet *> *sets) {
  self->barsetsAdded(*sets);
}

//  void QBarSeries::barsetsReplaced(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15barsetsReplacedERK5QListIP7QBarSetE(
    QBarSeries *self,
    const QList<QBarSet *> *sets) {
  self->barsetsReplaced(*sets);
}

//  void QBarSeries::barsetsRemoved(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries14barsetsRemovedERK5QListIP7QBarSetE(
    QBarSeries *self,
    const QList<QBarSet *> *sets) {
  self->barsetsRemoved(*sets);
}

//  void QBarSeries::setValueChanged(qsizetype index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15setValueChangedExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *barset) {
  self->setValueChanged(index, barset);
}

//  void QBarSeries::setValueAdded(qsizetype index, qsizetype count, QBarSet
//      *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries13setValueAddedExxP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    qsizetype count,
    QBarSet *barset) {
  self->setValueAdded(index, count, barset);
}

//  void QBarSeries::setValueRemoved(qsizetype index, qsizetype count,
//      QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries15setValueRemovedExxP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    qsizetype count,
    QBarSet *barset) {
  self->setValueRemoved(index, count, barset);
}

//  void QBarSeries::barSetsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries14barSetsChangedEv(QBarSeries *self) {
  self->barSetsChanged();
}

//  void QBarSeries::clicked(qsizetype index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries7clickedExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *barset) {
  self->clicked(index, barset);
}

//  void QBarSeries::doubleClicked(qsizetype index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries13doubleClickedExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *barset) {
  self->doubleClicked(index, barset);
}

//  void QBarSeries::pressed(qsizetype index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries7pressedExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *barset) {
  self->pressed(index, barset);
}

//  void QBarSeries::released(qsizetype index, QBarSet *barset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries8releasedExP7QBarSet(
    QBarSeries *self,
    qsizetype index,
    QBarSet *barset) {
  self->released(index, barset);
}

//  void QBarSeries::handleSetValueChange(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries20handleSetValueChangeEx(
    QBarSeries *self,
    qsizetype index) {
  self->handleSetValueChange(index);
}

//  void QBarSeries::handleSetValueAdd(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries17handleSetValueAddExx(
    QBarSeries *self,
    qsizetype index,
    qsizetype count) {
  self->handleSetValueAdd(index, count);
}

//  void QBarSeries::handleSetValueRemove(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries20handleSetValueRemoveExx(
    QBarSeries *self,
    qsizetype index,
    qsizetype count) {
  self->handleSetValueRemove(index, count);
}

//  QBarSeriesPrivate *QBarSeries::d_func()
extern "C" Q_DECL_EXPORT
QBarSeriesPrivate *ritual_ZN10QBarSeries6d_funcEv(QBarSeries *self) {
  return self->d_func();
}

//  const QBarSeriesPrivate *QBarSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QBarSeriesPrivate *ritual_ZNK10QBarSeries6d_funcEv(
    const QBarSeries *self) {
  return self->d_func();
}

//  bool QBarSeries::barDelegateDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBarSeries16barDelegateDirtyEv(const QBarSeries *self) {
  return self->barDelegateDirty();
}

//  void QBarSeries::setBarDelegateDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBarSeries19setBarDelegateDirtyEb(
    QBarSeries *self,
    bool dirty) {
  self->setBarDelegateDirty(dirty);
}

//  a Python function taken by a CuteQBarSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarSeries(QBarSeries *self, const char *key, void *call) {
  return static_cast<CuteQBarSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK10QBarSeries4typeEv(
    const QBarSeries *self) {
  return self->QBarSeries::type();
}

//  void QBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBarSeries17componentCompleteEv(QBarSeries *self) {
  static_cast<OwnQBarSeries *>(self)->OwnQBarSeries::componentComplete();
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
