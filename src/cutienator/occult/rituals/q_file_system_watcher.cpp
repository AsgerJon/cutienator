//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfilesystemwatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfilesystemwatcher.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QFileSystemWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QFileSystemWatcher10metaObjectEv(
    const QFileSystemWatcher *self) {
  return self->metaObject();
}

//  QString QFileSystemWatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFileSystemWatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileSystemWatcher::tr(s, c, n));
}

//  QFileSystemWatcher::QFileSystemWatcher(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSystemWatcher *ritual_ZN18QFileSystemWatcherC1EP7QObject(
    QObject *parent) {
  return new QFileSystemWatcher(parent);
}

//  QFileSystemWatcher::~QFileSystemWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileSystemWatcherD1Ev(QFileSystemWatcher *self) {
  delete self;
}

//  bool QFileSystemWatcher::addPath(const QString &file)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileSystemWatcher7addPathERK7QString(
    QFileSystemWatcher *self,
    const QString *file) {
  return self->addPath(*file);
}

//  bool QFileSystemWatcher::removePath(const QString &file)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileSystemWatcher10removePathERK7QString(
    QFileSystemWatcher *self,
    const QString *file) {
  return self->removePath(*file);
}
