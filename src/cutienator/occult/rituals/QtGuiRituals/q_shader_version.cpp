//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QShaderVersion::QShaderVersion()
extern "C" Q_DECL_EXPORT
QShaderVersion *ritual_ZN14QShaderVersionC1Ev() {
  return new QShaderVersion();
}

//  QShaderVersion::QShaderVersion(int v, Flags f)
extern "C" Q_DECL_EXPORT
QShaderVersion *ritual_ZN14QShaderVersionC1Ei6QFlagsINS_4FlagEE(
    int v,
    int f) {
  return new QShaderVersion(v, QFlags<QShaderVersion::Flag>::fromInt(f));
}

//  int QShaderVersion::version() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QShaderVersion7versionEv(const QShaderVersion *self) {
  return self->version();
}

//  void QShaderVersion::setVersion(int v)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QShaderVersion10setVersionEi(QShaderVersion *self, int v) {
  self->setVersion(v);
}

//  Flags QShaderVersion::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QShaderVersion5flagsEv(const QShaderVersion *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QShaderVersion::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QShaderVersion8setFlagsE6QFlagsINS_4FlagEE(
    QShaderVersion *self,
    int f) {
  self->setFlags(QFlags<QShaderVersion::Flag>::fromInt(f));
}

//  QShaderVersion::~QShaderVersion()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QShaderVersionD1Ev(QShaderVersion *self) {
  delete self;
}

//  QList<QShaderVersion>::QList()
extern "C" Q_DECL_EXPORT
QList<QShaderVersion> *ritual_list_make_QShaderVersion() {
  return new QList<QShaderVersion>();
}

//  void QList<QShaderVersion>::append(const QShaderVersion &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QShaderVersion(
    QList<QShaderVersion> *self,
    const QShaderVersion *element) {
  self->append(*element);
}

//  qsizetype QList<QShaderVersion>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QShaderVersion(
    const QList<QShaderVersion> *self) {
  return self->size();
}

//  const QShaderVersion &QList<QShaderVersion>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QShaderVersion *ritual_list_at_QShaderVersion(
    const QList<QShaderVersion> *self,
    long long index) {
  return new QShaderVersion(self->at(index));
}

//  QList<QShaderVersion>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QShaderVersion(QList<QShaderVersion> *self) {
  delete self;
}
