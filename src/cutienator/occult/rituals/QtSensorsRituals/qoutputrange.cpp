//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensor.h>
#include <QtCore/qlist.h>

//  qoutputrange::~qoutputrange()
extern "C" Q_DECL_EXPORT
void ritual_ZN12qoutputrangeD1Ev(qoutputrange *self) {
  delete self;
}

//  QList<qoutputrange>::QList()
extern "C" Q_DECL_EXPORT
QList<qoutputrange> *ritual_list_make_qoutputrange() {
  return new QList<qoutputrange>();
}

//  void QList<qoutputrange>::append(const qoutputrange &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_qoutputrange(
    QList<qoutputrange> *self,
    const qoutputrange *element) {
  self->append(*element);
}

//  qsizetype QList<qoutputrange>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_qoutputrange(const QList<qoutputrange> *self) {
  return self->size();
}

//  const qoutputrange &QList<qoutputrange>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
qoutputrange *ritual_list_at_qoutputrange(
    const QList<qoutputrange> *self,
    long long index) {
  return new qoutputrange(self->at(index));
}

//  QList<qoutputrange>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_qoutputrange(QList<qoutputrange> *self) {
  delete self;
}
