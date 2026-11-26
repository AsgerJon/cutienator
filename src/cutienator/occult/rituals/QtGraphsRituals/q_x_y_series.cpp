//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qxyseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qxyseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QXYSeries that Python can take functions over in. Every QXYSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXYSeriesCall0)(const void *, int *);
typedef void (*CuteQXYSeriesCall1)(const void *, int *);
typedef int (*CuteQXYSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYSeries : public QXYSeries {
public:
  using QXYSeries::QXYSeries;
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

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQXYSeriesCall0 call = reinterpret_cast<CuteQXYSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

  //  void QAbstractSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXYSeriesCall1 call = reinterpret_cast<CuteQXYSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::componentComplete();
  }

  //  SeriesType QAbstractSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQXYSeriesCall2 call = reinterpret_cast<CuteQXYSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXYSeriesCall3 call = reinterpret_cast<CuteQXYSeriesCall3>(taken[3]);
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
      CuteQXYSeriesCall4 call = reinterpret_cast<CuteQXYSeriesCall4>(taken[4]);
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
      CuteQXYSeriesCall5 call = reinterpret_cast<CuteQXYSeriesCall5>(taken[5]);
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
      CuteQXYSeriesCall6 call = reinterpret_cast<CuteQXYSeriesCall6>(taken[6]);
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
      CuteQXYSeriesCall7 call = reinterpret_cast<CuteQXYSeriesCall7>(taken[7]);
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
      CuteQXYSeriesCall8 call = reinterpret_cast<CuteQXYSeriesCall8>(taken[8]);
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
      CuteQXYSeriesCall9 call = reinterpret_cast<CuteQXYSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QXYSeries10metaObjectEv(
    const QXYSeries *self) {
  return self->metaObject();
}

//  void *QXYSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QXYSeries11qt_metacastEPKc(QXYSeries *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXYSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QXYSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QXYSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QXYSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QXYSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYSeries::tr(s, c, n));
}

//  QXYSeries::QXYSeries(QXYSeriesPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN9QXYSeriesC1ER16QXYSeriesPrivateP7QObject(
    QXYSeriesPrivate *dd,
    QObject *parent) {
  return new CuteQXYSeries(*dd, parent);
}

//  void QXYSeries::append(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6appendEdd(QXYSeries *self, qreal x, qreal y) {
  self->append(x, y);
}

//  void QXYSeries::append(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6appendE7QPointF(
    QXYSeries *self,
    const QPointF *point) {
  self->append(*point);
}

//  void QXYSeries::append(const QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6appendERK5QListI7QPointFE(
    QXYSeries *self,
    const QList<QPointF> *points) {
  self->append(*points);
}

//  void QXYSeries::replace(qreal oldX, qreal oldY, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceEdddd(
    QXYSeries *self,
    qreal oldX,
    qreal oldY,
    qreal newX,
    qreal newY) {
  self->replace(oldX, oldY, newX, newY);
}

//  void QXYSeries::replace(QPointF oldPoint, QPointF newPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceE7QPointFS0_(
    QXYSeries *self,
    const QPointF *oldPoint,
    const QPointF *newPoint) {
  self->replace(*oldPoint, *newPoint);
}

//  void QXYSeries::replace(qsizetype index, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceExdd(
    QXYSeries *self,
    qsizetype index,
    qreal newX,
    qreal newY) {
  self->replace(index, newX, newY);
}

//  void QXYSeries::replace(qsizetype index, QPointF newPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceEx7QPointF(
    QXYSeries *self,
    qsizetype index,
    const QPointF *newPoint) {
  self->replace(index, *newPoint);
}

//  void QXYSeries::replace(const QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7replaceERK5QListI7QPointFE(
    QXYSeries *self,
    const QList<QPointF> *points) {
  self->replace(*points);
}

//  void QXYSeries::remove(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6removeEdd(QXYSeries *self, qreal x, qreal y) {
  self->remove(x, y);
}

//  void QXYSeries::remove(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6removeE7QPointF(
    QXYSeries *self,
    const QPointF *point) {
  self->remove(*point);
}

//  void QXYSeries::remove(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6removeEx(QXYSeries *self, qsizetype index) {
  self->remove(index);
}

//  void QXYSeries::insert(qsizetype index, QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries6insertEx7QPointF(
    QXYSeries *self,
    qsizetype index,
    const QPointF *point) {
  self->insert(index, *point);
}

//  void QXYSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries5clearEv(QXYSeries *self) {
  self->clear();
}

//  QPointF QXYSeries::at(qsizetype index) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QXYSeries2atEx(const QXYSeries *self, qsizetype index) {
  return new QPointF(self->at(index));
}

//  qsizetype QXYSeries::find(QPointF point) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QXYSeries4findE7QPointF(
    const QXYSeries *self,
    const QPointF *point) {
  return self->find(*point);
}

//  void QXYSeries::removeMultiple(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries14removeMultipleExx(
    QXYSeries *self,
    qsizetype index,
    qsizetype count) {
  self->removeMultiple(index, count);
}

//  bool QXYSeries::take(QPointF point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QXYSeries4takeE7QPointF(
    QXYSeries *self,
    const QPointF *point) {
  return self->take(*point);
}

//  QXYSeries::~QXYSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeriesD1Ev(QXYSeries *self) {
  delete self;
}

//  QList<QPointF> QXYSeries::points() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK9QXYSeries6pointsEv(const QXYSeries *self) {
  return new QList<QPointF>(self->points());
}

//  QXYSeries &QXYSeries::operator<<(QPointF point)
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN9QXYSerieslsE7QPointF(
    QXYSeries *self,
    const QPointF *point) {
  return &(self->operator<<(*point));
}

//  QXYSeries &QXYSeries::operator<<(const QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN9QXYSerieslsERK5QListI7QPointFE(
    QXYSeries *self,
    const QList<QPointF> *points) {
  return &(self->operator<<(*points));
}

//  void QXYSeries::setColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries8setColorE6QColor(
    QXYSeries *self,
    const QColor *newColor) {
  self->setColor(*newColor);
}

//  QColor QXYSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QXYSeries5colorEv(const QXYSeries *self) {
  return new QColor(self->color());
}

//  void QXYSeries::setSelectedColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16setSelectedColorE6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->setSelectedColor(*color);
}

//  QColor QXYSeries::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QXYSeries13selectedColorEv(const QXYSeries *self) {
  return new QColor(self->selectedColor());
}

//  qsizetype QXYSeries::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QXYSeries5countEv(const QXYSeries *self) {
  return self->count();
}

//  QVariantList QXYSeries::values() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK9QXYSeries6valuesEv(const QXYSeries *self) {
  return new QList<QVariant>(self->values());
}

//  void QXYSeries::setValues(QVariantList values)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries9setValuesE5QListI8QVariantE(
    QXYSeries *self,
    const QList<QVariant> *values) {
  self->setValues(*values);
}

//  bool QXYSeries::isPointSelected(qsizetype index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QXYSeries15isPointSelectedEx(
    const QXYSeries *self,
    qsizetype index) {
  return self->isPointSelected(index);
}

//  void QXYSeries::selectPoint(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries11selectPointEx(QXYSeries *self, qsizetype index) {
  self->selectPoint(index);
}

//  void QXYSeries::deselectPoint(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13deselectPointEx(QXYSeries *self, qsizetype index) {
  self->deselectPoint(index);
}

//  void QXYSeries::setPointSelected(qsizetype index, bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16setPointSelectedExb(
    QXYSeries *self,
    qsizetype index,
    bool selected) {
  self->setPointSelected(index, selected);
}

//  void QXYSeries::selectAllPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries15selectAllPointsEv(QXYSeries *self) {
  self->selectAllPoints();
}

//  void QXYSeries::deselectAllPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries17deselectAllPointsEv(QXYSeries *self) {
  self->deselectAllPoints();
}

//  void QXYSeries::selectPoints(const QList<qsizetype> &indexes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries12selectPointsERK5QListIxE(
    QXYSeries *self,
    const QList<qsizetype> *indexes) {
  self->selectPoints(*indexes);
}

//  void QXYSeries::deselectPoints(const QList<qsizetype> &indexes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries14deselectPointsERK5QListIxE(
    QXYSeries *self,
    const QList<qsizetype> *indexes) {
  self->deselectPoints(*indexes);
}

//  void QXYSeries::toggleSelection(const QList<qsizetype> &indexes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries15toggleSelectionERK5QListIxE(
    QXYSeries *self,
    const QList<qsizetype> *indexes) {
  self->toggleSelection(*indexes);
}

//  QList<qsizetype> QXYSeries::selectedPoints() const
extern "C" Q_DECL_EXPORT
QList<qsizetype> *ritual_ZNK9QXYSeries14selectedPointsEv(
    const QXYSeries *self) {
  return new QList<qsizetype>(self->selectedPoints());
}

//  QQmlComponent *QXYSeries::pointDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK9QXYSeries13pointDelegateEv(const QXYSeries *self) {
  return self->pointDelegate();
}

//  void QXYSeries::setPointDelegate(QQmlComponent *newPointDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16setPointDelegateEP13QQmlComponent(
    QXYSeries *self,
    QQmlComponent *newPointDelegate) {
  self->setPointDelegate(newPointDelegate);
}

//  void QXYSeries::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries24qt_qmlMarker_uncreatableEv(QXYSeries *self) {
  self->qt_qmlMarker_uncreatable();
}

//  bool QXYSeries::isDraggable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QXYSeries11isDraggableEv(const QXYSeries *self) {
  return self->isDraggable();
}

//  void QXYSeries::setDraggable(bool newDraggable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries12setDraggableEb(
    QXYSeries *self,
    bool newDraggable) {
  self->setDraggable(newDraggable);
}

//  ValueMapping QXYSeries::valueMapping() const
extern "C" Q_DECL_EXPORT
QXYSeries::ValueMapping ritual_ZNK9QXYSeries12valueMappingEv(
    const QXYSeries *self) {
  return self->valueMapping();
}

//  void QXYSeries::setValueMapping(ValueMapping newHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries15setValueMappingENS_12ValueMappingE(
    QXYSeries *self,
    QXYSeries::ValueMapping newHint) {
  self->setValueMapping(newHint);
}

//  qreal QXYSeries::valueMin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QXYSeries8valueMinEv(const QXYSeries *self) {
  return self->valueMin();
}

//  void QXYSeries::setValueMin(qreal newMin)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries11setValueMinEd(QXYSeries *self, qreal newMin) {
  self->setValueMin(newMin);
}

//  qreal QXYSeries::stepSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QXYSeries8stepSizeEv(const QXYSeries *self) {
  return self->stepSize();
}

//  void QXYSeries::setStepSize(qreal stepSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries11setStepSizeEd(QXYSeries *self, qreal stepSize) {
  self->setStepSize(stepSize);
}

//  void QXYSeries::pointReplaced(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13pointReplacedEx(QXYSeries *self, qsizetype index) {
  self->pointReplaced(index);
}

//  void QXYSeries::pointRemoved(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries12pointRemovedEx(QXYSeries *self, qsizetype index) {
  self->pointRemoved(index);
}

//  void QXYSeries::pointAdded(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries10pointAddedEx(QXYSeries *self, qsizetype index) {
  self->pointAdded(index);
}

//  void QXYSeries::pointsAdded(qsizetype start, qsizetype end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries11pointsAddedExx(
    QXYSeries *self,
    qsizetype start,
    qsizetype end) {
  self->pointsAdded(start, end);
}

//  void QXYSeries::colorChanged(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries12colorChangedE6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QXYSeries::selectedColorChanged(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries20selectedColorChangedE6QColor(
    QXYSeries *self,
    const QColor *color) {
  self->selectedColorChanged(*color);
}

//  void QXYSeries::pointsReplaced()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries14pointsReplacedEv(QXYSeries *self) {
  self->pointsReplaced();
}

//  void QXYSeries::pointsRemoved(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13pointsRemovedExx(
    QXYSeries *self,
    qsizetype index,
    qsizetype count) {
  self->pointsRemoved(index, count);
}

//  void QXYSeries::selectedPointsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries21selectedPointsChangedEv(QXYSeries *self) {
  self->selectedPointsChanged();
}

//  void QXYSeries::pointDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries20pointDelegateChangedEv(QXYSeries *self) {
  self->pointDelegateChanged();
}

//  void QXYSeries::draggableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries16draggableChangedEv(QXYSeries *self) {
  self->draggableChanged();
}

//  void QXYSeries::seriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13seriesUpdatedEv(QXYSeries *self) {
  self->seriesUpdated();
}

//  void QXYSeries::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries12countChangedEv(QXYSeries *self) {
  self->countChanged();
}

//  void QXYSeries::clicked(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7clickedE6QPoint(
    QXYSeries *self,
    const QPoint *point) {
  self->clicked(*point);
}

//  void QXYSeries::doubleClicked(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13doubleClickedE6QPoint(
    QXYSeries *self,
    const QPoint *point) {
  self->doubleClicked(*point);
}

//  void QXYSeries::pressed(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries7pressedE6QPoint(
    QXYSeries *self,
    const QPoint *point) {
  self->pressed(*point);
}

//  void QXYSeries::released(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries8releasedE6QPoint(
    QXYSeries *self,
    const QPoint *point) {
  self->released(*point);
}

//  void QXYSeries::valuesChanged(const QVariantList &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries13valuesChangedERK5QListI8QVariantE(
    QXYSeries *self,
    const QList<QVariant> *values) {
  self->valuesChanged(*values);
}

//  void QXYSeries::valueMappingChanged(QXYSeries::ValueMapping newHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries19valueMappingChangedENS_12ValueMappingE(
    QXYSeries *self,
    QXYSeries::ValueMapping newHint) {
  self->valueMappingChanged(newHint);
}

//  void QXYSeries::valueMinChanged(qreal newMin)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries15valueMinChangedEd(QXYSeries *self, qreal newMin) {
  self->valueMinChanged(newMin);
}

//  void QXYSeries::stepSizeChanged(qreal newStepSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QXYSeries15stepSizeChangedEd(
    QXYSeries *self,
    qreal newStepSize) {
  self->stepSizeChanged(newStepSize);
}

//  QXYSeriesPrivate *QXYSeries::d_func()
extern "C" Q_DECL_EXPORT
QXYSeriesPrivate *ritual_ZN9QXYSeries6d_funcEv(QXYSeries *self) {
  return self->d_func();
}

//  const QXYSeriesPrivate *QXYSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QXYSeriesPrivate *ritual_ZNK9QXYSeries6d_funcEv(
    const QXYSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQXYSeries, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYSeries(QXYSeries *self, const char *key, void *call) {
  return static_cast<CuteQXYSeries *>(self)->take(key, call);
}

//  a QList<qsizetype> a ritual of QXYSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXYSeries__QList_qsizetype(QList<qsizetype> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
