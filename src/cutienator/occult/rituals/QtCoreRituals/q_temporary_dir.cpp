//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtemporarydir.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtemporarydir.h>
#include <QtCore/qstring.h>

//  QTemporaryDir::QTemporaryDir()
extern "C" Q_DECL_EXPORT
QTemporaryDir *ritual_ZN13QTemporaryDirC1Ev() {
  return new QTemporaryDir();
}

//  QTemporaryDir::QTemporaryDir(const QString &templateName)
extern "C" Q_DECL_EXPORT
QTemporaryDir *ritual_ZN13QTemporaryDirC1ERK7QString(
    const QString *templateName) {
  return new QTemporaryDir(*templateName);
}

//  QTemporaryDir::~QTemporaryDir()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTemporaryDirD1Ev(QTemporaryDir *self) {
  delete self;
}

//  bool QTemporaryDir::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTemporaryDir7isValidEv(const QTemporaryDir *self) {
  return self->isValid();
}

//  QString QTemporaryDir::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTemporaryDir11errorStringEv(
    const QTemporaryDir *self) {
  return new QString(self->errorString());
}

//  bool QTemporaryDir::autoRemove() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTemporaryDir10autoRemoveEv(const QTemporaryDir *self) {
  return self->autoRemove();
}

//  void QTemporaryDir::setAutoRemove(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTemporaryDir13setAutoRemoveEb(QTemporaryDir *self, bool b) {
  self->setAutoRemove(b);
}

//  bool QTemporaryDir::remove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QTemporaryDir6removeEv(QTemporaryDir *self) {
  return self->remove();
}

//  QString QTemporaryDir::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTemporaryDir4pathEv(const QTemporaryDir *self) {
  return new QString(self->path());
}

//  QString QTemporaryDir::filePath(const QString &fileName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTemporaryDir8filePathERK7QString(
    const QTemporaryDir *self,
    const QString *fileName) {
  return new QString(self->filePath(*fileName));
}
