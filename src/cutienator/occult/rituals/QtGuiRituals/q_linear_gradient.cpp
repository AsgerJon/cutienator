//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbrush.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  QLinearGradient::QLinearGradient()
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZN15QLinearGradientC1Ev() {
  return new QLinearGradient();
}

//  QLinearGradient::QLinearGradient(const QPointF &start, const QPointF
//      &finalStop)
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZN15QLinearGradientC1ERK7QPointFS2_(
    const QPointF *start,
    const QPointF *finalStop) {
  return new QLinearGradient(*start, *finalStop);
}

//  QLinearGradient::QLinearGradient(qreal xStart, qreal yStart, qreal
//      xFinalStop, qreal yFinalStop)
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZN15QLinearGradientC1Edddd(
    qreal xStart,
    qreal yStart,
    qreal xFinalStop,
    qreal yFinalStop) {
  return new QLinearGradient(xStart, yStart, xFinalStop, yFinalStop);
}

//  QLinearGradient::~QLinearGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLinearGradientD1Ev(QLinearGradient *self) {
  delete self;
}

//  QPointF QLinearGradient::start() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QLinearGradient5startEv(const QLinearGradient *self) {
  return new QPointF(self->start());
}

//  void QLinearGradient::setStart(const QPointF &start)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLinearGradient8setStartERK7QPointF(
    QLinearGradient *self,
    const QPointF *start) {
  self->setStart(*start);
}

//  void QLinearGradient::setStart(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLinearGradient8setStartEdd(
    QLinearGradient *self,
    qreal x,
    qreal y) {
  self->setStart(x, y);
}

//  QPointF QLinearGradient::finalStop() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QLinearGradient9finalStopEv(
    const QLinearGradient *self) {
  return new QPointF(self->finalStop());
}

//  void QLinearGradient::setFinalStop(const QPointF &stop)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLinearGradient12setFinalStopERK7QPointF(
    QLinearGradient *self,
    const QPointF *stop) {
  self->setFinalStop(*stop);
}

//  void QLinearGradient::setFinalStop(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLinearGradient12setFinalStopEdd(
    QLinearGradient *self,
    qreal x,
    qreal y) {
  self->setFinalStop(x, y);
}

//  QList<QLinearGradient>::QList()
extern "C" Q_DECL_EXPORT
QList<QLinearGradient> *ritual_list_make_QLinearGradient() {
  return new QList<QLinearGradient>();
}

//  void QList<QLinearGradient>::append(const QLinearGradient &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLinearGradient(
    QList<QLinearGradient> *self,
    const QLinearGradient *element) {
  self->append(*element);
}

//  qsizetype QList<QLinearGradient>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLinearGradient(
    const QList<QLinearGradient> *self) {
  return self->size();
}

//  const QLinearGradient &QList<QLinearGradient>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_list_at_QLinearGradient(
    const QList<QLinearGradient> *self,
    long long index) {
  return new QLinearGradient(self->at(index));
}

//  QList<QLinearGradient>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLinearGradient(QList<QLinearGradient> *self) {
  delete self;
}
