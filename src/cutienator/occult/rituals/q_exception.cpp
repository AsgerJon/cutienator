//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qexception.h>

//  QException::QException()
extern "C" Q_DECL_EXPORT
QException *ritual_ZN10QExceptionC1Ev() {
  return new QException();
}

//  QException::~QException()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QExceptionD1Ev(QException *self) {
  delete self;
}

//  QException::QException(const QException &a0)
extern "C" Q_DECL_EXPORT
QException *ritual_ZN10QExceptionC1ERKS_(const QException *a0) {
  return new QException(*a0);
}

//  void QException::raise() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QException5raiseEv(const QException *self) {
  self->raise();
}

//  QException *QException::clone() const
extern "C" Q_DECL_EXPORT
QException *ritual_ZNK10QException5cloneEv(const QException *self) {
  return self->clone();
}
