//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>

//  QDBusObjectPath::QDBusObjectPath()
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZN15QDBusObjectPathC1Ev() {
  return new QDBusObjectPath();
}

//  QDBusObjectPath::QDBusObjectPath(const char *path)
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZN15QDBusObjectPathC1EPKc(const char *path) {
  return new QDBusObjectPath(path);
}

//  QDBusObjectPath::QDBusObjectPath(QLatin1StringView path)
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZN15QDBusObjectPathC1E13QLatin1String(
    const QLatin1String *path) {
  return new QDBusObjectPath(*path);
}

//  QDBusObjectPath::QDBusObjectPath(const QString &path)
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZN15QDBusObjectPathC1ERK7QString(
    const QString *path) {
  return new QDBusObjectPath(*path);
}

//  void QDBusObjectPath::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusObjectPath7setPathERK7QString(
    QDBusObjectPath *self,
    const QString *path) {
  self->setPath(*path);
}

//  QString QDBusObjectPath::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDBusObjectPath4pathEv(const QDBusObjectPath *self) {
  return new QString(self->path());
}

//  QVariant QDBusObjectPath::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QDBusObjectPathcv8QVariantEv(
    const QDBusObjectPath *self) {
  return new QVariant(self->operator QVariant());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QDBusObjectPath &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK15QDBusObjectPath(
    const QDebug *a0,
    const QDBusObjectPath *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  void QDBusObjectPath::doCheck()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusObjectPath7doCheckEv(QDBusObjectPath *self) {
  self->doCheck();
}

//  QDBusObjectPath::~QDBusObjectPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusObjectPathD1Ev(QDBusObjectPath *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
