//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#include <QtCore/qobjectdefs.h>

//  QGenericReturnArgument::~QGenericReturnArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGenericReturnArgumentD1Ev(QGenericReturnArgument *self) {
  delete self;
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
