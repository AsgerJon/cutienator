//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsavefile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsavefile.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSaveFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSaveFile10metaObjectEv(
    const QSaveFile *self) {
  return self->metaObject();
}

//  QString QSaveFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSaveFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSaveFile::tr(s, c, n));
}

//  QSaveFile::QSaveFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QSaveFile *ritual_ZN9QSaveFileC1EP7QObject(QObject *parent) {
  return new QSaveFile(parent);
}

//  QSaveFile::QSaveFile(const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QSaveFile *ritual_ZN9QSaveFileC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new QSaveFile(*name, parent);
}

//  QSaveFile::~QSaveFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFileD1Ev(QSaveFile *self) {
  delete self;
}

//  QString QSaveFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSaveFile8fileNameEv(const QSaveFile *self) {
  return new QString(self->fileName());
}

//  void QSaveFile::setFileName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile11setFileNameERK7QString(
    QSaveFile *self,
    const QString *name) {
  self->setFileName(*name);
}

//  bool QSaveFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSaveFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSaveFile *self,
    int flags) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  bool QSaveFile::commit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSaveFile6commitEv(QSaveFile *self) {
  return self->commit();
}

//  void QSaveFile::cancelWriting()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile13cancelWritingEv(QSaveFile *self) {
  self->cancelWriting();
}

//  void QSaveFile::setDirectWriteFallback(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile22setDirectWriteFallbackEb(
    QSaveFile *self,
    bool enabled) {
  self->setDirectWriteFallback(enabled);
}

//  bool QSaveFile::directWriteFallback() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSaveFile19directWriteFallbackEv(const QSaveFile *self) {
  return self->directWriteFallback();
}
