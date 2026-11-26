//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringbuilder.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, rituals for functions the generator leaves out: 2. Kept as it is
//  when the generator runs again.
#include <QtCore/qstringbuilder.h>
#include <QtCore/qlatin1stringview.h>

//  void QAbstractConcatenable::appendLatin1To(QLatin1StringView in, QChar
//      *out)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractConcatenable14appendLatin1ToE13QLatin1StringP5QChar(
    const QLatin1String *in,
    QChar *out) {
  QAbstractConcatenable::appendLatin1To(*in, out);
}

//  QAbstractConcatenable::~QAbstractConcatenable()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractConcatenableD1Ev(QAbstractConcatenable *self) {
  delete self;
}

//  static void QAbstractConcatenable::convertFromUtf8(QByteArrayView in,
//      QChar *&out)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractConcatenable15convertFromUtf8E14QByteArrayViewRP5QChar(
    const QByteArrayView *in,
    QChar **out) {
  QAbstractConcatenable::convertFromUtf8(*in, *out);
}

//  static void QAbstractConcatenable::convertFromAscii(char a, QChar *&out)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractConcatenable16convertFromAsciiEcRP5QChar(
    char a,
    QChar **out) {
  QAbstractConcatenable::convertFromAscii(a, *out);
}
