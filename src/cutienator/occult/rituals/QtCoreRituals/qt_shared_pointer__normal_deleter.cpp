//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedpointer_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qsharedpointer.h>

//  QtSharedPointer::NormalDeleter::~NormalDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer13NormalDeleterD1Ev(
    QtSharedPointer::NormalDeleter *self) {
  delete self;
}

#endif  // !defined(Q_QDOC)
