//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmargins.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmargins.h>

//  QMargins::QMargins()
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZN8QMarginsC1Ev() {
  return new QMargins();
}

//  QMargins::QMargins(int left, int top, int right, int bottom)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZN8QMarginsC1Eiiii(
    int left,
    int top,
    int right,
    int bottom) {
  return new QMargins(left, top, right, bottom);
}

//  bool QMargins::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMargins6isNullEv(const QMargins *self) {
  return self->isNull();
}

//  int QMargins::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins4leftEv(const QMargins *self) {
  return self->left();
}

//  int QMargins::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins3topEv(const QMargins *self) {
  return self->top();
}

//  int QMargins::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins5rightEv(const QMargins *self) {
  return self->right();
}

//  int QMargins::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins6bottomEv(const QMargins *self) {
  return self->bottom();
}

//  void QMargins::setLeft(int left)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins7setLeftEi(QMargins *self, int left) {
  self->setLeft(left);
}

//  void QMargins::setTop(int top)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins6setTopEi(QMargins *self, int top) {
  self->setTop(top);
}

//  void QMargins::setRight(int right)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins8setRightEi(QMargins *self, int right) {
  self->setRight(right);
}

//  void QMargins::setBottom(int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins9setBottomEi(QMargins *self, int bottom) {
  self->setBottom(bottom);
}

//  QMarginsF QMargins::toMarginsF() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK8QMargins10toMarginsFEv(const QMargins *self) {
  return new QMarginsF(self->toMarginsF());
}

//  QMargins::~QMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsD1Ev(QMargins *self) {
  delete self;
}
