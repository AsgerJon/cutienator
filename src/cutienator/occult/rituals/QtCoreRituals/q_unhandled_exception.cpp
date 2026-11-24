//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#include <QtCore/qexception.h>

//  QUnhandledException::~QUnhandledException()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QUnhandledExceptionD1Ev(QUnhandledException *self) {
  delete self;
}

//  QUnhandledException::QUnhandledException(const QUnhandledException
//      &other)
extern "C" Q_DECL_EXPORT
QUnhandledException *ritual_ZN19QUnhandledExceptionC1ERKS_(
    const QUnhandledException *other) {
  return new QUnhandledException(*other);
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

#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
