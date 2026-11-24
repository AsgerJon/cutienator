//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedpointer_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qsharedpointer.h>

//  QtPrivate::EnableInternalData::~EnableInternalData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate18EnableInternalDataD1Ev(
    QtPrivate::EnableInternalData *self) {
  delete self;
}

#endif  // !defined(Q_QDOC)
