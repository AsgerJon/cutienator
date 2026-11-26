//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#include <QtCore/qexception.h>

//  void QtPrivate::ExceptionStore::setException(const QException &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14ExceptionStore12setExceptionERK10QException(
    QtPrivate::ExceptionStore *self,
    const QException *e) {
  self->setException(*e);
}

//  void QtPrivate::ExceptionStore::setException(std::exception_ptr e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14ExceptionStore12setExceptionENSt15__exception_ptr13exception_ptrE(
    QtPrivate::ExceptionStore *self,
    const std::exception_ptr *e) {
  self->setException(*e);
}

//  bool QtPrivate::ExceptionStore::hasException() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate14ExceptionStore12hasExceptionEv(
    const QtPrivate::ExceptionStore *self) {
  return self->hasException();
}

//  std::exception_ptr QtPrivate::ExceptionStore::exception() const
extern "C" Q_DECL_EXPORT
std::exception_ptr *ritual_ZNK9QtPrivate14ExceptionStore9exceptionEv(
    const QtPrivate::ExceptionStore *self) {
  return new std::exception_ptr(self->exception());
}

//  void QtPrivate::ExceptionStore::throwPossibleException()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14ExceptionStore22throwPossibleExceptionEv(
    QtPrivate::ExceptionStore *self) {
  self->throwPossibleException();
}

//  void QtPrivate::ExceptionStore::rethrowException() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate14ExceptionStore16rethrowExceptionEv(
    const QtPrivate::ExceptionStore *self) {
  self->rethrowException();
}

//  QtPrivate::ExceptionStore::~ExceptionStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14ExceptionStoreD1Ev(
    QtPrivate::ExceptionStore *self) {
  delete self;
}

//  a std::exception_ptr a ritual of QtPrivate::ExceptionStore gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtPrivate_ExceptionStore__std_exception_ptr(
    std::exception_ptr *self) {
  delete self;
}

#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
