//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  A 'CFStringRef' is passed as an address.
//  Not written: what it has from the template QCFType.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstring.h>

//  QCFString::QCFString(const QString &str)
extern "C" Q_DECL_EXPORT
QCFString *ritual_ZN9QCFStringC1ERK7QString(const QString *str) {
  return new QCFString(*str);
}

//  QCFString::QCFString(const CFStringRef cfstr)
extern "C" Q_DECL_EXPORT
QCFString *ritual_ZN9QCFStringC1EPK10__CFString(const CFStringRef cfstr) {
  return new QCFString(cfstr);
}

//  QCFString::QCFString(const QCFType<CFStringRef> &other)
extern "C" Q_DECL_EXPORT
QCFString *ritual_ZN9QCFStringC1ERK7QCFTypeIPK10__CFStringE(
    const QCFType<CFStringRef> *other) {
  return new QCFString(*other);
}

//  QString QCFString::operator QString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QCFStringcv7QStringEv(const QCFString *self) {
  return new QString(self->operator QString());
}

//  CFStringRef QCFString::operator CFStringRef() const
extern "C" Q_DECL_EXPORT
CFStringRef ritual_ZNK9QCFStringcvPK10__CFStringEv(const QCFString *self) {
  return self->operator CFStringRef();
}

//  QCFString::~QCFString()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCFStringD1Ev(QCFString *self) {
  delete self;
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QCFString &string)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK9QCFString(
    const QDebug *debug,
    const QCFString *string) {
  return new QDebug(operator<<(*debug, *string));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#endif  // defined(Q_OS_DARWIN)
