//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmargins.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmargins.h>

//  QMarginsF::QMarginsF()
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZN9QMarginsFC1Ev() {
  return new QMarginsF();
}

//  QMarginsF::QMarginsF(qreal left, qreal top, qreal right, qreal bottom)
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZN9QMarginsFC1Edddd(
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  return new QMarginsF(left, top, right, bottom);
}

//  QMarginsF::QMarginsF(const QMargins &margins)
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZN9QMarginsFC1ERK8QMargins(const QMargins *margins) {
  return new QMarginsF(*margins);
}

//  bool QMarginsF::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMarginsF6isNullEv(const QMarginsF *self) {
  return self->isNull();
}

//  qreal QMarginsF::left() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QMarginsF4leftEv(const QMarginsF *self) {
  return self->left();
}

//  qreal QMarginsF::top() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QMarginsF3topEv(const QMarginsF *self) {
  return self->top();
}

//  qreal QMarginsF::right() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QMarginsF5rightEv(const QMarginsF *self) {
  return self->right();
}

//  qreal QMarginsF::bottom() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QMarginsF6bottomEv(const QMarginsF *self) {
  return self->bottom();
}

//  void QMarginsF::setLeft(qreal aleft)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMarginsF7setLeftEd(QMarginsF *self, qreal aleft) {
  self->setLeft(aleft);
}

//  void QMarginsF::setTop(qreal atop)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMarginsF6setTopEd(QMarginsF *self, qreal atop) {
  self->setTop(atop);
}

//  void QMarginsF::setRight(qreal aright)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMarginsF8setRightEd(QMarginsF *self, qreal aright) {
  self->setRight(aright);
}

//  void QMarginsF::setBottom(qreal abottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMarginsF9setBottomEd(QMarginsF *self, qreal abottom) {
  self->setBottom(abottom);
}

//  QMargins QMarginsF::toMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK9QMarginsF9toMarginsEv(const QMarginsF *self) {
  return new QMargins(self->toMargins());
}

//  QMarginsF::~QMarginsF()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMarginsFD1Ev(QMarginsF *self) {
  delete self;
}
