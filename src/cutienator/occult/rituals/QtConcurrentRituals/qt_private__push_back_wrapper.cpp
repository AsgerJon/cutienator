//  Written by dev_tooling.RitualGenerator from the records of
//  QtConcurrent/qtconcurrentfunctionwrappers.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtConcurrent/qtconcurrent_global.h>
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
#include <QtConcurrent/qtconcurrentfunctionwrappers.h>

//  QtPrivate::PushBackWrapper::~PushBackWrapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15PushBackWrapperD1Ev(
    QtPrivate::PushBackWrapper *self) {
  delete self;
}

#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
