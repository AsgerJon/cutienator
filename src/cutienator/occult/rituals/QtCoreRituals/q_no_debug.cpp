//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdebug.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 5. Kept as it is when the generator
//  runs again.
#include <QtCore/qdebug.h>
#include <QtCore/qtextstream.h>

//  QNoDebug &QNoDebug::operator<<(QTextStreamFunction a0)
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebuglsEPFR11QTextStreamS1_E(
    QNoDebug *self,
    void *a0) {
  return &(self->operator<<(reinterpret_cast<QTextStreamFunction>(a0)));
}

//  QNoDebug &QNoDebug::operator<<(QTextStreamManipulator a0)
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebuglsE22QTextStreamManipulator(
    QNoDebug *self,
    const QTextStreamManipulator *a0) {
  return &(self->operator<<(*a0));
}

//  QNoDebug &QNoDebug::space()
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug5spaceEv(QNoDebug *self) {
  return &(self->space());
}

//  QNoDebug &QNoDebug::nospace()
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug7nospaceEv(QNoDebug *self) {
  return &(self->nospace());
}

//  QNoDebug &QNoDebug::maybeSpace()
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug10maybeSpaceEv(QNoDebug *self) {
  return &(self->maybeSpace());
}

//  QNoDebug &QNoDebug::quote()
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug5quoteEv(QNoDebug *self) {
  return &(self->quote());
}

//  QNoDebug &QNoDebug::noquote()
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug7noquoteEv(QNoDebug *self) {
  return &(self->noquote());
}

//  QNoDebug &QNoDebug::maybeQuote(const char a0)
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug10maybeQuoteEc(QNoDebug *self, char a0) {
  return &(self->maybeQuote(a0));
}

//  QNoDebug &QNoDebug::verbosity(int a0)
extern "C" Q_DECL_EXPORT
QNoDebug *ritual_ZN8QNoDebug9verbosityEi(QNoDebug *self, int a0) {
  return &(self->verbosity(a0));
}

//  QNoDebug::~QNoDebug()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QNoDebugD1Ev(QNoDebug *self) {
  delete self;
}

//  QNoDebug &QNoDebug::operator<<<int>(const int &a0)
extern "C" Q_DECL_EXPORT
QNoDebug * ritual_ZN8QNoDebuglsIiEERS_RKT_(QNoDebug *self, int value) {
  return &(self->operator<< <int>(value));
}

//  QNoDebug &QNoDebug::operator<<<double>(const double &a0)
extern "C" Q_DECL_EXPORT
QNoDebug * ritual_ZN8QNoDebuglsIdEERS_RKT_(QNoDebug *self, double value) {
  return &(self->operator<< <double>(value));
}

//  QNoDebug &QNoDebug::operator<<<bool>(const bool &a0)
extern "C" Q_DECL_EXPORT
QNoDebug * ritual_ZN8QNoDebuglsIbEERS_RKT_(QNoDebug *self, bool value) {
  return &(self->operator<< <bool>(value));
}

//  QNoDebug &QNoDebug::operator<<<QString>(const QString &a0)
extern "C" Q_DECL_EXPORT
QNoDebug * ritual_ZN8QNoDebuglsI7QStringEERS_RKT_(
    QNoDebug *self,
    const QString *value) {
  return &(self->operator<< <QString>(*value));
}

//  QNoDebug &QNoDebug::operator<<<QByteArray>(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
QNoDebug * ritual_ZN8QNoDebuglsI10QByteArrayEERS_RKT_(
    QNoDebug *self,
    const QByteArray *value) {
  return &(self->operator<< <QByteArray>(*value));
}
