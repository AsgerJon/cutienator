//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qpieseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qpieseries.h>
#include <QtCore/qstring.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qpieslice.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  Only a class built on QPieSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPieSeries : QPieSeries {
  using QPieSeries::componentComplete;
};

//  A QPieSeries that Python can take functions over in. Every QPieSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPieSeriesCall0)(const void *, int *);
typedef void (*CuteQPieSeriesCall1)(const void *, int *);
typedef void (*CuteQPieSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieSeries : public QPieSeries {
public:
  using QPieSeries::QPieSeries;
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

  //  QAbstractSeries::SeriesType QPieSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPieSeriesCall0 call = reinterpret_cast<CuteQPieSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QPieSeries::type();
  }

  //  void QPieSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPieSeriesCall1 call = reinterpret_cast<CuteQPieSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPieSeries::componentComplete();
  }

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPieSeriesCall2 call = reinterpret_cast<CuteQPieSeriesCall2>(taken[2]);
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
      CuteQPieSeriesCall3 call = reinterpret_cast<CuteQPieSeriesCall3>(taken[3]);
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
      CuteQPieSeriesCall4 call = reinterpret_cast<CuteQPieSeriesCall4>(taken[4]);
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
      CuteQPieSeriesCall5 call = reinterpret_cast<CuteQPieSeriesCall5>(taken[5]);
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
      CuteQPieSeriesCall6 call = reinterpret_cast<CuteQPieSeriesCall6>(taken[6]);
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
      CuteQPieSeriesCall7 call = reinterpret_cast<CuteQPieSeriesCall7>(taken[7]);
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
      CuteQPieSeriesCall8 call = reinterpret_cast<CuteQPieSeriesCall8>(taken[8]);
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
      CuteQPieSeriesCall9 call = reinterpret_cast<CuteQPieSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QPieSeries10metaObjectEv(
    const QPieSeries *self) {
  return self->metaObject();
}

//  void *QPieSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QPieSeries11qt_metacastEPKc(
    QPieSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPieSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QPieSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QPieSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPieSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QPieSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieSeries::tr(s, c, n));
}

//  QPieSeries::QPieSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZN10QPieSeriesC1EP7QObject(QObject *parent) {
  return new CuteQPieSeries(parent);
}

//  QPieSeries::~QPieSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeriesD1Ev(QPieSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QPieSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK10QPieSeries4typeEv(
    const QPieSeries *self) {
  return self->type();
}

//  bool QPieSeries::append(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries6appendEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  return self->append(slice);
}

//  bool QPieSeries::append(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries6appendERK5QListIP9QPieSliceE(
    QPieSeries *self,
    const QList<QPieSlice *> *slices) {
  return self->append(*slices);
}

//  bool QPieSeries::insert(qsizetype index, QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries6insertExP9QPieSlice(
    QPieSeries *self,
    qsizetype index,
    QPieSlice *slice) {
  return self->insert(index, slice);
}

//  bool QPieSeries::remove(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries6removeEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  return self->remove(slice);
}

//  void QPieSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries5clearEv(QPieSeries *self) {
  self->clear();
}

//  QPieSlice *QPieSeries::append(const QString &label, qreal value)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN10QPieSeries6appendERK7QStringd(
    QPieSeries *self,
    const QString *label,
    qreal value) {
  return self->append(*label, value);
}

//  QPieSlice *QPieSeries::at(qsizetype index)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN10QPieSeries2atEx(QPieSeries *self, qsizetype index) {
  return self->at(index);
}

//  QPieSlice *QPieSeries::find(const QString &label)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN10QPieSeries4findERK7QString(
    QPieSeries *self,
    const QString *label) {
  return self->find(*label);
}

//  bool QPieSeries::replace(qsizetype index, QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries7replaceExP9QPieSlice(
    QPieSeries *self,
    qsizetype index,
    QPieSlice *slice) {
  return self->replace(index, slice);
}

//  void QPieSeries::removeMultiple(qsizetype index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries14removeMultipleExi(
    QPieSeries *self,
    qsizetype index,
    int count) {
  self->removeMultiple(index, count);
}

//  bool QPieSeries::remove(qsizetype index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries6removeEx(QPieSeries *self, qsizetype index) {
  return self->remove(index);
}

//  bool QPieSeries::replace(QPieSlice *oldSlice, QPieSlice *newSlice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries7replaceEP9QPieSliceS1_(
    QPieSeries *self,
    QPieSlice *oldSlice,
    QPieSlice *newSlice) {
  return self->replace(oldSlice, newSlice);
}

//  bool QPieSeries::replace(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries7replaceERK5QListIP9QPieSliceE(
    QPieSeries *self,
    const QList<QPieSlice *> *slices) {
  return self->replace(*slices);
}

//  bool QPieSeries::take(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPieSeries4takeEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  return self->take(slice);
}

//  QPieSeries &QPieSeries::operator<<(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZN10QPieSerieslsEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  return &(self->operator<<(slice));
}

//  QList<QPieSlice *> QPieSeries::slices() const
extern "C" Q_DECL_EXPORT
QList<QPieSlice *> *ritual_ZNK10QPieSeries6slicesEv(const QPieSeries *self) {
  return new QList<QPieSlice *>(self->slices());
}

//  qsizetype QPieSeries::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QPieSeries5countEv(const QPieSeries *self) {
  return self->count();
}

//  bool QPieSeries::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QPieSeries7isEmptyEv(const QPieSeries *self) {
  return self->isEmpty();
}

//  qreal QPieSeries::sum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries3sumEv(const QPieSeries *self) {
  return self->sum();
}

//  void QPieSeries::setHorizontalPosition(qreal relativePosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries21setHorizontalPositionEd(
    QPieSeries *self,
    qreal relativePosition) {
  self->setHorizontalPosition(relativePosition);
}

//  qreal QPieSeries::horizontalPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries18horizontalPositionEv(const QPieSeries *self) {
  return self->horizontalPosition();
}

//  void QPieSeries::setVerticalPosition(qreal relativePosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries19setVerticalPositionEd(
    QPieSeries *self,
    qreal relativePosition) {
  self->setVerticalPosition(relativePosition);
}

//  qreal QPieSeries::verticalPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries16verticalPositionEv(const QPieSeries *self) {
  return self->verticalPosition();
}

//  void QPieSeries::setPieSize(qreal relativeSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries10setPieSizeEd(
    QPieSeries *self,
    qreal relativeSize) {
  self->setPieSize(relativeSize);
}

//  qreal QPieSeries::pieSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries7pieSizeEv(const QPieSeries *self) {
  return self->pieSize();
}

//  void QPieSeries::setStartAngle(qreal startAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries13setStartAngleEd(
    QPieSeries *self,
    qreal startAngle) {
  self->setStartAngle(startAngle);
}

//  qreal QPieSeries::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries10startAngleEv(const QPieSeries *self) {
  return self->startAngle();
}

//  void QPieSeries::setEndAngle(qreal endAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries11setEndAngleEd(QPieSeries *self, qreal endAngle) {
  self->setEndAngle(endAngle);
}

//  qreal QPieSeries::endAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries8endAngleEv(const QPieSeries *self) {
  return self->endAngle();
}

//  void QPieSeries::setHoleSize(qreal holeSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries11setHoleSizeEd(QPieSeries *self, qreal holeSize) {
  self->setHoleSize(holeSize);
}

//  qreal QPieSeries::holeSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries8holeSizeEv(const QPieSeries *self) {
  return self->holeSize();
}

//  void QPieSeries::setLabelsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries16setLabelsVisibleEb(
    QPieSeries *self,
    bool visible) {
  self->setLabelsVisible(visible);
}

//  void QPieSeries::setLabelsPosition(QPieSlice::LabelPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries17setLabelsPositionEN9QPieSlice13LabelPositionE(
    QPieSeries *self,
    QPieSlice::LabelPosition position) {
  self->setLabelsPosition(position);
}

//  qreal QPieSeries::angleSpanVisibleLimit() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QPieSeries21angleSpanVisibleLimitEv(
    const QPieSeries *self) {
  return self->angleSpanVisibleLimit();
}

//  void QPieSeries::setAngleSpanVisibleLimit(qreal newAngleSpanVisibleLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries24setAngleSpanVisibleLimitEd(
    QPieSeries *self,
    qreal newAngleSpanVisibleLimit) {
  self->setAngleSpanVisibleLimit(newAngleSpanVisibleLimit);
}

//  LabelVisibility QPieSeries::angleSpanLabelVisibility() const
extern "C" Q_DECL_EXPORT
QPieSeries::LabelVisibility ritual_ZNK10QPieSeries24angleSpanLabelVisibilityEv(
    const QPieSeries *self) {
  return self->angleSpanLabelVisibility();
}

//  void QPieSeries::setAngleSpanLabelVisibility(LabelVisibility
//      newAngleSpanVisibleMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries27setAngleSpanLabelVisibilityENS_15LabelVisibilityE(
    QPieSeries *self,
    QPieSeries::LabelVisibility newAngleSpanVisibleMode) {
  self->setAngleSpanLabelVisibility(newAngleSpanVisibleMode);
}

//  QList<qreal> QPieSeries::sliceData() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK10QPieSeries9sliceDataEv(const QPieSeries *self) {
  return new QList<qreal>(self->sliceData());
}

//  void QPieSeries::setSliceData(const QList<qreal> &newSliceData)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries12setSliceDataERK5QListIdE(
    QPieSeries *self,
    const QList<qreal> *newSliceData) {
  self->setSliceData(*newSliceData);
}

//  const QStringList &QPieSeries::sliceLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNKR10QPieSeries11sliceLabelsEv(
    const QPieSeries *self) {
  return new QList<QString>(self->sliceLabels());
}

//  void QPieSeries::setSliceLabels(QStringList newLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries14setSliceLabelsE5QListI7QStringE(
    QPieSeries *self,
    const QList<QString> *newLabels) {
  self->setSliceLabels(*newLabels);
}

//  void QPieSeries::handleSliceChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries17handleSliceChangeEv(QPieSeries *self) {
  self->handleSliceChange();
}

//  QPieSeries::QPieSeries(QPieSeriesPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZN10QPieSeriesC1ER17QPieSeriesPrivateP7QObject(
    QPieSeriesPrivate *dd,
    QObject *parent) {
  return new CuteQPieSeries(*dd, parent);
}

//  void QPieSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries17componentCompleteEv(QPieSeries *self) {
  self->componentComplete();
}

//  void QPieSeries::added(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries5addedERK5QListIP9QPieSliceE(
    QPieSeries *self,
    const QList<QPieSlice *> *slices) {
  self->added(*slices);
}

//  void QPieSeries::removed(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries7removedERK5QListIP9QPieSliceE(
    QPieSeries *self,
    const QList<QPieSlice *> *slices) {
  self->removed(*slices);
}

//  void QPieSeries::replaced(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries8replacedERK5QListIP9QPieSliceE(
    QPieSeries *self,
    const QList<QPieSlice *> *slices) {
  self->replaced(*slices);
}

//  void QPieSeries::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries12countChangedEv(QPieSeries *self) {
  self->countChanged();
}

//  void QPieSeries::sumChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries10sumChangedEv(QPieSeries *self) {
  self->sumChanged();
}

//  void QPieSeries::pieSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries14pieSizeChangedEv(QPieSeries *self) {
  self->pieSizeChanged();
}

//  void QPieSeries::startAngleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries17startAngleChangedEv(QPieSeries *self) {
  self->startAngleChanged();
}

//  void QPieSeries::endAngleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries15endAngleChangedEv(QPieSeries *self) {
  self->endAngleChanged();
}

//  void QPieSeries::horizontalPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries25horizontalPositionChangedEv(QPieSeries *self) {
  self->horizontalPositionChanged();
}

//  void QPieSeries::verticalPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries23verticalPositionChangedEv(QPieSeries *self) {
  self->verticalPositionChanged();
}

//  void QPieSeries::holeSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries15holeSizeChangedEv(QPieSeries *self) {
  self->holeSizeChanged();
}

//  void QPieSeries::clicked(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries7clickedEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  self->clicked(slice);
}

//  void QPieSeries::doubleClicked(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries13doubleClickedEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  self->doubleClicked(slice);
}

//  void QPieSeries::pressed(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries7pressedEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  self->pressed(slice);
}

//  void QPieSeries::released(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries8releasedEP9QPieSlice(
    QPieSeries *self,
    QPieSlice *slice) {
  self->released(slice);
}

//  void QPieSeries::angleSpanVisibleLimitChanged(qreal limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries28angleSpanVisibleLimitChangedEd(
    QPieSeries *self,
    qreal limit) {
  self->angleSpanVisibleLimitChanged(limit);
}

//  void QPieSeries::angleSpanLabelVisibilityChanged(LabelVisibility
//      visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries31angleSpanLabelVisibilityChangedENS_15LabelVisibilityE(
    QPieSeries *self,
    QPieSeries::LabelVisibility visibility) {
  self->angleSpanLabelVisibilityChanged(visibility);
}

//  void QPieSeries::sliceDataChanged(const QList<qreal> &sliceData)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries16sliceDataChangedERK5QListIdE(
    QPieSeries *self,
    const QList<qreal> *sliceData) {
  self->sliceDataChanged(*sliceData);
}

//  void QPieSeries::sliceLabelsChanged(const QStringList &sliceLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPieSeries18sliceLabelsChangedERK5QListI7QStringE(
    QPieSeries *self,
    const QList<QString> *sliceLabels) {
  self->sliceLabelsChanged(*sliceLabels);
}

//  QPieSeriesPrivate *QPieSeries::d_func()
extern "C" Q_DECL_EXPORT
QPieSeriesPrivate *ritual_ZN10QPieSeries6d_funcEv(QPieSeries *self) {
  return self->d_func();
}

//  const QPieSeriesPrivate *QPieSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QPieSeriesPrivate *ritual_ZNK10QPieSeries6d_funcEv(
    const QPieSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPieSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieSeries(QPieSeries *self, const char *key, void *call) {
  return static_cast<CuteQPieSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QPieSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK10QPieSeries4typeEv(
    const QPieSeries *self) {
  return self->QPieSeries::type();
}

//  void QPieSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPieSeries17componentCompleteEv(QPieSeries *self) {
  static_cast<OwnQPieSeries *>(self)->OwnQPieSeries::componentComplete();
}

//  a QList<qreal> a ritual of QPieSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPieSeries__QList_qreal(QList<qreal> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
