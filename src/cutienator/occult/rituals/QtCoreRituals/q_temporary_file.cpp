//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtemporaryfile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QTemporaryFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QTemporaryFile10metaObjectEv(
    const QTemporaryFile *self) {
  return self->metaObject();
}

//  QString QTemporaryFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QTemporaryFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTemporaryFile::tr(s, c, n));
}

//  QTemporaryFile::QTemporaryFile()
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1Ev() {
  return new QTemporaryFile();
}

//  QTemporaryFile::QTemporaryFile(const QString &templateName)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1ERK7QString(
    const QString *templateName) {
  return new QTemporaryFile(*templateName);
}

//  QTemporaryFile::QTemporaryFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1EP7QObject(QObject *parent) {
  return new QTemporaryFile(parent);
}

//  QTemporaryFile::QTemporaryFile(const QString &templateName, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1ERK7QStringP7QObject(
    const QString *templateName,
    QObject *parent) {
  return new QTemporaryFile(*templateName, parent);
}

//  QTemporaryFile::~QTemporaryFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTemporaryFileD1Ev(QTemporaryFile *self) {
  delete self;
}

//  bool QTemporaryFile::autoRemove() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTemporaryFile10autoRemoveEv(const QTemporaryFile *self) {
  return self->autoRemove();
}

//  void QTemporaryFile::setAutoRemove(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTemporaryFile13setAutoRemoveEb(
    QTemporaryFile *self,
    bool b) {
  self->setAutoRemove(b);
}

//  bool QTemporaryFile::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile4openEv(QTemporaryFile *self) {
  return self->open();
}

//  QString QTemporaryFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QTemporaryFile8fileNameEv(const QTemporaryFile *self) {
  return new QString(self->fileName());
}

//  QString QTemporaryFile::fileTemplate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QTemporaryFile12fileTemplateEv(
    const QTemporaryFile *self) {
  return new QString(self->fileTemplate());
}

//  void QTemporaryFile::setFileTemplate(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTemporaryFile15setFileTemplateERK7QString(
    QTemporaryFile *self,
    const QString *name) {
  self->setFileTemplate(*name);
}

//  bool QTemporaryFile::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile6renameERK7QString(
    QTemporaryFile *self,
    const QString *newName) {
  return self->rename(*newName);
}

//  bool QTemporaryFile::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile15renameOverwriteERK7QString(
    QTemporaryFile *self,
    const QString *newName) {
  return self->renameOverwrite(*newName);
}

//  QTemporaryFile *QTemporaryFile::createNativeFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFile16createNativeFileERK7QString(
    const QString *fileName) {
  return QTemporaryFile::createNativeFile(*fileName);
}
