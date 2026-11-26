//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlatin1stringmatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlatin1stringmatcher.h>

//  QtPrivate::QCaseSensitiveLatin1Hash::QCaseSensitiveLatin1Hash()
extern "C" Q_DECL_EXPORT
QtPrivate::QCaseSensitiveLatin1Hash *ritual_ZN9QtPrivate24QCaseSensitiveLatin1HashC1Ev() {
  return new QtPrivate::QCaseSensitiveLatin1Hash();
}

//  std::size_t QtPrivate::QCaseSensitiveLatin1Hash::operator()(char c) const
extern "C" Q_DECL_EXPORT
std::size_t ritual_ZNK9QtPrivate24QCaseSensitiveLatin1HashclEc(
    const QtPrivate::QCaseSensitiveLatin1Hash *self,
    char c) {
  return self->operator()(c);
}

//  QtPrivate::QCaseSensitiveLatin1Hash::~QCaseSensitiveLatin1Hash()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate24QCaseSensitiveLatin1HashD1Ev(
    QtPrivate::QCaseSensitiveLatin1Hash *self) {
  delete self;
}
