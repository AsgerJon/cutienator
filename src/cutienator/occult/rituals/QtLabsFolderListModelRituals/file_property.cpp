//  Written by dev_tooling.RitualGenerator from the records of QtLabsFolderLi
//  stModel/6.12.0/QtLabsFolderListModel/private/fileproperty_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/qquickfolderlistmodelglobal_p.h>
#include <QtLabsFolderListModel/QtLabsFolderListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/fileproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>

//  void FileProperty::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN12FileProperty22qt_qmlMarker_anonymousEv(FileProperty *self) {
  self->qt_qmlMarker_anonymous();
}

//  FileProperty::FileProperty(const QFileInfo &info)
extern "C" Q_DECL_EXPORT
FileProperty *ritual_ZN12FilePropertyC1ERK9QFileInfo(const QFileInfo *info) {
  return new FileProperty(*info);
}

//  QString FileProperty::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12FileProperty8fileNameEv(const FileProperty *self) {
  return new QString(self->fileName());
}

//  QString FileProperty::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12FileProperty8filePathEv(const FileProperty *self) {
  return new QString(self->filePath());
}

//  QString FileProperty::baseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12FileProperty8baseNameEv(const FileProperty *self) {
  return new QString(self->baseName());
}

//  qint64 FileProperty::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12FileProperty4sizeEv(const FileProperty *self) {
  return self->size();
}

//  QString FileProperty::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12FileProperty6suffixEv(const FileProperty *self) {
  return new QString(self->suffix());
}

//  bool FileProperty::isDir() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12FileProperty5isDirEv(const FileProperty *self) {
  return self->isDir();
}

//  bool FileProperty::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12FileProperty6isFileEv(const FileProperty *self) {
  return self->isFile();
}

//  QDateTime FileProperty::lastModified() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK12FileProperty12lastModifiedEv(
    const FileProperty *self) {
  return new QDateTime(self->lastModified());
}

//  QDateTime FileProperty::lastRead() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK12FileProperty8lastReadEv(const FileProperty *self) {
  return new QDateTime(self->lastRead());
}

//  bool FileProperty::operator!=(const FileProperty &fileInfo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12FilePropertyneERKS_(
    const FileProperty *self,
    const FileProperty *fileInfo) {
  return self->operator!=(*fileInfo);
}

//  bool FileProperty::operator==(const FileProperty &property) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12FilePropertyeqERKS_(
    const FileProperty *self,
    const FileProperty *property) {
  return self->operator==(*property);
}

//  FileProperty::~FileProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN12FilePropertyD1Ev(FileProperty *self) {
  delete self;
}

//  QList<FileProperty>::QList()
extern "C" Q_DECL_EXPORT
QList<FileProperty> *ritual_list_make_FileProperty() {
  return new QList<FileProperty>();
}

//  void QList<FileProperty>::append(const FileProperty &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_FileProperty(
    QList<FileProperty> *self,
    const FileProperty *element) {
  self->append(*element);
}

//  qsizetype QList<FileProperty>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_FileProperty(const QList<FileProperty> *self) {
  return self->size();
}

//  const FileProperty &QList<FileProperty>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
FileProperty *ritual_list_at_FileProperty(
    const QList<FileProperty> *self,
    long long index) {
  return new FileProperty(self->at(index));
}

//  QList<FileProperty>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_FileProperty(QList<FileProperty> *self) {
  delete self;
}
