//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>

//  DocumentEditPrivate *QQmlSA::DocumentEdit::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEditPrivate *ritual_ZN6QQmlSA12DocumentEdit6d_funcEv(
    QQmlSA::DocumentEdit *self) {
  return self->d_func();
}

//  const DocumentEditPrivate *QQmlSA::DocumentEdit::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::DocumentEditPrivate *ritual_ZNK6QQmlSA12DocumentEdit6d_funcEv(
    const QQmlSA::DocumentEdit *self) {
  return self->d_func();
}

//  bool operator==(const DocumentEdit &lhs, const DocumentEdit &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_12DocumentEditES2_(
    const QQmlSA::DocumentEdit *lhs,
    const QQmlSA::DocumentEdit *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const DocumentEdit &lhs, const DocumentEdit &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_12DocumentEditES2_(
    const QQmlSA::DocumentEdit *lhs,
    const QQmlSA::DocumentEdit *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QQmlSA::DocumentEdit::DocumentEdit(const QString &filename, const
//      SourceLocation &location, const QString &replacement)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA12DocumentEditC1ERK7QStringRKNS_14SourceLocationES3_(
    const QString *filename,
    const QQmlSA::SourceLocation *location,
    const QString *replacement) {
  return new QQmlSA::DocumentEdit(*filename, *location, *replacement);
}

//  QQmlSA::DocumentEdit::DocumentEdit(const DocumentEdit &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA12DocumentEditC1ERKS0_(
    const QQmlSA::DocumentEdit *a0) {
  return new QQmlSA::DocumentEdit(*a0);
}

//  QQmlSA::DocumentEdit::DocumentEdit(DocumentEdit &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA12DocumentEditC1EOS0_(
    QQmlSA::DocumentEdit *a0) {
  return new QQmlSA::DocumentEdit(std::move(*a0));
}

//  DocumentEdit &QQmlSA::DocumentEdit::operator=(const DocumentEdit &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA12DocumentEditaSERKS0_(
    QQmlSA::DocumentEdit *self,
    const QQmlSA::DocumentEdit *a0) {
  return &(self->operator=(*a0));
}

//  DocumentEdit &QQmlSA::DocumentEdit::operator=(DocumentEdit &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA12DocumentEditaSEOS0_(
    QQmlSA::DocumentEdit *self,
    QQmlSA::DocumentEdit *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlSA::DocumentEdit::~DocumentEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA12DocumentEditD1Ev(QQmlSA::DocumentEdit *self) {
  delete self;
}

//  QString QQmlSA::DocumentEdit::filename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA12DocumentEdit8filenameEv(
    const QQmlSA::DocumentEdit *self) {
  return new QString(self->filename());
}

//  SourceLocation QQmlSA::DocumentEdit::location() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA12DocumentEdit8locationEv(
    const QQmlSA::DocumentEdit *self) {
  return new QQmlSA::SourceLocation(self->location());
}

//  QString QQmlSA::DocumentEdit::replacement() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA12DocumentEdit11replacementEv(
    const QQmlSA::DocumentEdit *self) {
  return new QString(self->replacement());
}
