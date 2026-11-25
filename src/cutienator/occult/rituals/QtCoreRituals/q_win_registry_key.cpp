//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qwinregistry_p.h, Qt 6.12.0, as the Qt
//  of Windows installs it. Kept as it is when the generator runs again.
//  Not written: the constructor and 'value' and 'stringValue' taking a
//  'const wchar_t *', a type no row has a word for; the constructor
//  taking a 'QWinRegistryKey &&' and 'swap', which take the object
//  itself; and the templates of 'value'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qwinregistry_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QWinRegistryKey::QWinRegistryKey()
extern "C" Q_DECL_EXPORT
QWinRegistryKey *ritual_ZN15QWinRegistryKeyC1Ev() {
  return new QWinRegistryKey();
}

//  QWinRegistryKey::QWinRegistryKey(HKEY parentHandle, const QString
//      &subKey, REGSAM permissions, REGSAM access)
extern "C" Q_DECL_EXPORT
QWinRegistryKey *ritual_ZN15QWinRegistryKeyC1EP6HKEY__RK7QStringmm(
    HKEY parentHandle,
    const QString *subKey,
    REGSAM permissions,
    REGSAM access) {
  return new QWinRegistryKey(parentHandle, *subKey, permissions, access);
}

//  QWinRegistryKey::~QWinRegistryKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWinRegistryKeyD1Ev(QWinRegistryKey *self) {
  delete self;
}

//  bool QWinRegistryKey::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWinRegistryKey7isValidEv(const QWinRegistryKey *self) {
  return self->isValid();
}

//  HKEY QWinRegistryKey::handle() const
extern "C" Q_DECL_EXPORT
HKEY ritual_ZNK15QWinRegistryKey6handleEv(const QWinRegistryKey *self) {
  return self->handle();
}

//  HKEY QWinRegistryKey::operator HKEY() const
extern "C" Q_DECL_EXPORT
HKEY ritual_ZNK15QWinRegistryKeycvP6HKEY__Ev(const QWinRegistryKey *self) {
  return self->operator HKEY();
}

//  void QWinRegistryKey::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWinRegistryKey5closeEv(QWinRegistryKey *self) {
  self->close();
}

//  QString QWinRegistryKey::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWinRegistryKey4nameEv(const QWinRegistryKey *self) {
  return new QString(self->name());
}

//  QVariant QWinRegistryKey::value(const QString &subKey) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QWinRegistryKey5valueERK7QString(
    const QWinRegistryKey *self,
    const QString *subKey) {
  return new QVariant(self->value(*subKey));
}

//  QString QWinRegistryKey::stringValue(const QString &subKey) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWinRegistryKey11stringValueERK7QString(
    const QWinRegistryKey *self,
    const QString *subKey) {
  return new QString(self->stringValue(*subKey));
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QWinRegistryKey &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK15QWinRegistryKey(
    const QDebug *dbg,
    const QWinRegistryKey *a1) {
  return new QDebug(operator<<(*dbg, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#endif  // defined(Q_OS_WIN)
