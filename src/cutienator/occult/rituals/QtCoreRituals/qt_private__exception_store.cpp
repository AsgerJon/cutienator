//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#include <QtCore/qexception.h>

//  QtPrivate::ExceptionStore::~ExceptionStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate14ExceptionStoreD1Ev(
    QtPrivate::ExceptionStore *self) {
  delete self;
}

#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
