//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringbuilder.h, Qt 6.12.0. Changes made here are lost.
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
