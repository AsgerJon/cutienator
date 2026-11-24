//  Written by dev_tooling.RitualGenerator from the records of
//  QtConcurrent/qtconcurrentmedian.h, Qt 6.12.0. Changes made here are lost.
#include <QtConcurrent/qtconcurrent_global.h>
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
#include <QtConcurrent/qtconcurrentmedian.h>

//  QtConcurrent::Median::Median()
extern "C" Q_DECL_EXPORT
QtConcurrent::Median *ritual_ZN12QtConcurrent6MedianC1Ev() {
  return new QtConcurrent::Median();
}

//  void QtConcurrent::Median::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent6Median5resetEv(QtConcurrent::Median *self) {
  self->reset();
}

//  void QtConcurrent::Median::addValue(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent6Median8addValueEd(
    QtConcurrent::Median *self,
    double value) {
  self->addValue(value);
}

//  bool QtConcurrent::Median::isMedianValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QtConcurrent6Median13isMedianValidEv(
    const QtConcurrent::Median *self) {
  return self->isMedianValid();
}

//  double QtConcurrent::Median::median()
extern "C" Q_DECL_EXPORT
double ritual_ZN12QtConcurrent6Median6medianEv(QtConcurrent::Median *self) {
  return self->median();
}

//  QtConcurrent::Median::~Median()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent6MedianD1Ev(QtConcurrent::Median *self) {
  delete self;
}

#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
