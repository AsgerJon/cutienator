//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qoperatingsystemversion.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED) && !defined(Q_QDOC)
#include <QtCore/qoperatingsystemversion.h>

//  QOperatingSystemVersionUnexported::QOperatingSystemVersionUnexported(QOpe
//      ratingSystemVersionBase other)
extern "C" Q_DECL_EXPORT
QOperatingSystemVersionUnexported *ritual_ZN33QOperatingSystemVersionUnexportedC1E27QOperatingSystemVersionBase(
    const QOperatingSystemVersionBase *other) {
  return new QOperatingSystemVersionUnexported(*other);
}

//  QOperatingSystemVersionUnexported::~QOperatingSystemVersionUnexported()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QOperatingSystemVersionUnexportedD1Ev(
    QOperatingSystemVersionUnexported *self) {
  delete self;
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED) && !defined(Q_QDOC)
