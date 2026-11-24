//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QShaderKey::QShaderKey()
extern "C" Q_DECL_EXPORT
QShaderKey *ritual_ZN10QShaderKeyC1Ev() {
  return new QShaderKey();
}

//  QShaderKey::QShaderKey(QShader::Source s, const QShaderVersion &sver,
//      QShader::Variant svar)
extern "C" Q_DECL_EXPORT
QShaderKey *ritual_ZN10QShaderKeyC1EN7QShader6SourceERK14QShaderVersionNS0_7VariantE(
    QShader::Source s,
    const QShaderVersion *sver,
    QShader::Variant svar) {
  return new QShaderKey(s, *sver, svar);
}

//  QShader::Source QShaderKey::source() const
extern "C" Q_DECL_EXPORT
QShader::Source ritual_ZNK10QShaderKey6sourceEv(const QShaderKey *self) {
  return self->source();
}

//  void QShaderKey::setSource(QShader::Source s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QShaderKey9setSourceEN7QShader6SourceE(
    QShaderKey *self,
    QShader::Source s) {
  self->setSource(s);
}

//  QShaderVersion QShaderKey::sourceVersion() const
extern "C" Q_DECL_EXPORT
QShaderVersion *ritual_ZNK10QShaderKey13sourceVersionEv(
    const QShaderKey *self) {
  return new QShaderVersion(self->sourceVersion());
}

//  void QShaderKey::setSourceVersion(const QShaderVersion &sver)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QShaderKey16setSourceVersionERK14QShaderVersion(
    QShaderKey *self,
    const QShaderVersion *sver) {
  self->setSourceVersion(*sver);
}

//  QShader::Variant QShaderKey::sourceVariant() const
extern "C" Q_DECL_EXPORT
QShader::Variant ritual_ZNK10QShaderKey13sourceVariantEv(
    const QShaderKey *self) {
  return self->sourceVariant();
}

//  void QShaderKey::setSourceVariant(QShader::Variant svar)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QShaderKey16setSourceVariantEN7QShader7VariantE(
    QShaderKey *self,
    QShader::Variant svar) {
  self->setSourceVariant(svar);
}

//  QShaderKey::~QShaderKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QShaderKeyD1Ev(QShaderKey *self) {
  delete self;
}

//  QList<QShaderKey>::QList()
extern "C" Q_DECL_EXPORT
QList<QShaderKey> *ritual_list_make_QShaderKey() {
  return new QList<QShaderKey>();
}

//  void QList<QShaderKey>::append(const QShaderKey &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QShaderKey(
    QList<QShaderKey> *self,
    const QShaderKey *element) {
  self->append(*element);
}

//  qsizetype QList<QShaderKey>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QShaderKey(const QList<QShaderKey> *self) {
  return self->size();
}

//  const QShaderKey &QList<QShaderKey>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QShaderKey *ritual_list_at_QShaderKey(
    const QList<QShaderKey> *self,
    long long index) {
  return new QShaderKey(self->at(index));
}

//  QList<QShaderKey>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QShaderKey(QList<QShaderKey> *self) {
  delete self;
}
