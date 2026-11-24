//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlatin1stringmatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlatin1stringmatcher.h>

//  QtPrivate::QCaseInsensitiveLatin1Hash::QCaseInsensitiveLatin1Hash()
extern "C" Q_DECL_EXPORT
QtPrivate::QCaseInsensitiveLatin1Hash *ritual_ZN9QtPrivate26QCaseInsensitiveLatin1HashC1Ev() {
  return new QtPrivate::QCaseInsensitiveLatin1Hash();
}

//  int QtPrivate::QCaseInsensitiveLatin1Hash::difference(char lhs, char rhs)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate26QCaseInsensitiveLatin1Hash10differenceEcc(
    char lhs,
    char rhs) {
  return QtPrivate::QCaseInsensitiveLatin1Hash::difference(lhs, rhs);
}

//  QtPrivate::QCaseInsensitiveLatin1Hash::~QCaseInsensitiveLatin1Hash()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate26QCaseInsensitiveLatin1HashD1Ev(
    QtPrivate::QCaseInsensitiveLatin1Hash *self) {
  delete self;
}
