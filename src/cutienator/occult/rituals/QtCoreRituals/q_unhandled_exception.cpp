//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#include <QtCore/qexception.h>

//  QUnhandledException::QUnhandledException(std::exception_ptr exception)
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZN19QUnhandledExceptionC1ENSt15__exception_ptr13exception_ptrE(
    const std::exception_ptr *exception) {
  return new QUnhandledException(*exception);
}

//  QUnhandledException::~QUnhandledException()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QUnhandledExceptionD1Ev(QUnhandledException *self) {
  delete self;
}

//  QUnhandledException::QUnhandledException(QUnhandledException &&other)
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZN19QUnhandledExceptionC1EOS_(
    QUnhandledException *other) {
  return new QUnhandledException(std::move(*other));
}

//  QUnhandledException::QUnhandledException(const QUnhandledException
//      &other)
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZN19QUnhandledExceptionC1ERKS_(
    const QUnhandledException *other) {
  return new QUnhandledException(*other);
}

//  void QUnhandledException::swap(QUnhandledException &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QUnhandledException4swapERS_(
    QUnhandledException *self,
    QUnhandledException *other) {
  self->swap(*other);
}

//  QUnhandledException &QUnhandledException::operator=(QUnhandledException
//      &&other)
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZN19QUnhandledExceptionaSEOS_(
    QUnhandledException *self,
    QUnhandledException *other) {
  return &(self->operator=(std::move(*other)));
}

//  QUnhandledException &QUnhandledException::operator=(const
//      QUnhandledException &other)
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZN19QUnhandledExceptionaSERKS_(
    QUnhandledException *self,
    const QUnhandledException *other) {
  return &(self->operator=(*other));
}

//  void QUnhandledException::raise() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QUnhandledException5raiseEv(
    const QUnhandledException *self) {
  self->raise();
}

//  QUnhandledException *QUnhandledException::clone() const
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZNK19QUnhandledException5cloneEv(
    const QUnhandledException *self) {
  return self->clone();
}

//  std::exception_ptr QUnhandledException::exception() const
extern "C" Q_DECL_EXPORT
std::exception_ptr *ritual_ZNK19QUnhandledException9exceptionEv(
    const QUnhandledException *self) {
  return new std::exception_ptr(self->exception());
}

//  a std::exception_ptr a ritual of QUnhandledException gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QUnhandledException__std_exception_ptr(
    std::exception_ptr *self) {
  delete self;
}

#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
