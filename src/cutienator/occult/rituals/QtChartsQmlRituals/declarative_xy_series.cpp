//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativexyseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativexyseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A DeclarativeXySeries that Python can take functions over in. Every DeclarativeXySeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteDeclarativeXySeriesCall0)(const void *, int *);
class CuteDeclarativeXySeries : public DeclarativeXySeries {
public:
  using DeclarativeXySeries::DeclarativeXySeries;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19DeclarativeXySeries8xySeriesEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QXYSeries *DeclarativeXySeries::xySeries()
  QXYSeries *xySeries() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeXySeriesCall0 call = reinterpret_cast<CuteDeclarativeXySeriesCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXYSeries *>(given);
    }
    return {};
  }
};

//  DeclarativeXySeries::~DeclarativeXySeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeriesD1Ev(DeclarativeXySeries *self) {
  delete self;
}

//  void DeclarativeXySeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries10classBeginEv(
    DeclarativeXySeries *self) {
  self->classBegin();
}

//  void DeclarativeXySeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries17componentCompleteEv(
    DeclarativeXySeries *self) {
  self->componentComplete();
}

//  QXYSeries *DeclarativeXySeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN19DeclarativeXySeries8xySeriesEv(
    DeclarativeXySeries *self) {
  return self->xySeries();
}

//  void DeclarativeXySeries::append(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries6appendEdd(
    DeclarativeXySeries *self,
    qreal x,
    qreal y) {
  self->append(x, y);
}

//  void DeclarativeXySeries::replace(qreal oldX, qreal oldY, qreal newX,
//      qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries7replaceEdddd(
    DeclarativeXySeries *self,
    qreal oldX,
    qreal oldY,
    qreal newX,
    qreal newY) {
  self->replace(oldX, oldY, newX, newY);
}

//  void DeclarativeXySeries::replace(int index, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries7replaceEidd(
    DeclarativeXySeries *self,
    int index,
    qreal newX,
    qreal newY) {
  self->replace(index, newX, newY);
}

//  void DeclarativeXySeries::remove(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries6removeEdd(
    DeclarativeXySeries *self,
    qreal x,
    qreal y) {
  self->remove(x, y);
}

//  void DeclarativeXySeries::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries6removeEi(
    DeclarativeXySeries *self,
    int index) {
  self->remove(index);
}

//  void DeclarativeXySeries::removePoints(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries12removePointsEii(
    DeclarativeXySeries *self,
    int index,
    int count) {
  self->removePoints(index, count);
}

//  void DeclarativeXySeries::insert(int index, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries6insertEidd(
    DeclarativeXySeries *self,
    int index,
    qreal x,
    qreal y) {
  self->insert(index, x, y);
}

//  void DeclarativeXySeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativeXySeries5clearEv(DeclarativeXySeries *self) {
  self->clear();
}

//  QPointF DeclarativeXySeries::at(int index)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN19DeclarativeXySeries2atEi(
    DeclarativeXySeries *self,
    int index) {
  return new QPointF(self->at(index));
}

//  a Python function taken by a CuteDeclarativeXySeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeXySeries(
    DeclarativeXySeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeXySeries *>(self)->take(key, call);
}
