//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtCore/QList>

//  FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestionPrivate *ritual_ZN6QQmlSA13FixSuggestion6d_funcEv(
    QQmlSA::FixSuggestion *self) {
  return self->d_func();
}

//  const FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::FixSuggestionPrivate *ritual_ZNK6QQmlSA13FixSuggestion6d_funcEv(
    const QQmlSA::FixSuggestion *self) {
  return self->d_func();
}

//  QQmlSA::FixSuggestion::FixSuggestion(const QString &description, const
//      QQmlSA::SourceLocation &location, const DocumentEdit &documentEdit)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA13FixSuggestionC1ERK7QStringRKNS_14SourceLocationERKNS_12DocumentEditE(
    const QString *description,
    const QQmlSA::SourceLocation *location,
    const QQmlSA::DocumentEdit *documentEdit) {
  return new QQmlSA::FixSuggestion(*description, *location, *documentEdit);
}

//  QQmlSA::FixSuggestion::FixSuggestion(const QString &description, const
//      QQmlSA::SourceLocation &location, const QList<DocumentEdit>
//      &documentEdits)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA13FixSuggestionC1ERK7QStringRKNS_14SourceLocationERK5QListINS_12DocumentEditEE(
    const QString *description,
    const QQmlSA::SourceLocation *location,
    const QList<QQmlSA::DocumentEdit> *documentEdits) {
  return new QQmlSA::FixSuggestion(*description, *location, *documentEdits);
}

//  QQmlSA::FixSuggestion::FixSuggestion(const FixSuggestion &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA13FixSuggestionC1ERKS0_(
    const QQmlSA::FixSuggestion *a0) {
  return new QQmlSA::FixSuggestion(*a0);
}

//  QQmlSA::FixSuggestion::FixSuggestion(FixSuggestion &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA13FixSuggestionC1EOS0_(
    QQmlSA::FixSuggestion *a0) {
  return new QQmlSA::FixSuggestion(std::move(*a0));
}

//  FixSuggestion &QQmlSA::FixSuggestion::operator=(const FixSuggestion &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA13FixSuggestionaSERKS0_(
    QQmlSA::FixSuggestion *self,
    const QQmlSA::FixSuggestion *a0) {
  return &(self->operator=(*a0));
}

//  FixSuggestion &QQmlSA::FixSuggestion::operator=(FixSuggestion &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA13FixSuggestionaSEOS0_(
    QQmlSA::FixSuggestion *self,
    QQmlSA::FixSuggestion *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlSA::FixSuggestion::~FixSuggestion()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA13FixSuggestionD1Ev(QQmlSA::FixSuggestion *self) {
  delete self;
}

//  QString QQmlSA::FixSuggestion::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA13FixSuggestion11descriptionEv(
    const QQmlSA::FixSuggestion *self) {
  return new QString(self->description());
}

//  QQmlSA::SourceLocation QQmlSA::FixSuggestion::location() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA13FixSuggestion8locationEv(
    const QQmlSA::FixSuggestion *self) {
  return new QQmlSA::SourceLocation(self->location());
}

//  void QQmlSA::FixSuggestion::addDocumentEdit(const DocumentEdit &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA13FixSuggestion15addDocumentEditERKNS_12DocumentEditE(
    QQmlSA::FixSuggestion *self,
    const QQmlSA::DocumentEdit *a0) {
  self->addDocumentEdit(*a0);
}

//  QList<DocumentEdit> QQmlSA::FixSuggestion::documentEdits() const
extern "C" Q_DECL_EXPORT
QList<QQmlSA::DocumentEdit> *ritual_ZNK6QQmlSA13FixSuggestion13documentEditsEv(
    const QQmlSA::FixSuggestion *self) {
  return new QList<QQmlSA::DocumentEdit>(self->documentEdits());
}

//  void QQmlSA::FixSuggestion::setFileName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA13FixSuggestion11setFileNameERK7QString(
    QQmlSA::FixSuggestion *self,
    const QString *a0) {
  self->setFileName(*a0);
}

//  QString QQmlSA::FixSuggestion::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA13FixSuggestion8fileNameEv(
    const QQmlSA::FixSuggestion *self) {
  return new QString(self->fileName());
}

//  void QQmlSA::FixSuggestion::setAutoApplicable(bool autoApplicable)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA13FixSuggestion17setAutoApplicableEb(
    QQmlSA::FixSuggestion *self,
    bool autoApplicable) {
  self->setAutoApplicable(autoApplicable);
}

//  bool QQmlSA::FixSuggestion::isAutoApplicable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA13FixSuggestion16isAutoApplicableEv(
    const QQmlSA::FixSuggestion *self) {
  return self->isAutoApplicable();
}

//  bool operator==(const FixSuggestion &lhs, const FixSuggestion &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_13FixSuggestionES2_(
    const QQmlSA::FixSuggestion *lhs,
    const QQmlSA::FixSuggestion *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const FixSuggestion &lhs, const FixSuggestion &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_13FixSuggestionES2_(
    const QQmlSA::FixSuggestion *lhs,
    const QQmlSA::FixSuggestion *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QQmlSA::FixSuggestion::operatorEqualsImpl(const FixSuggestion &a0,
//      const FixSuggestion &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA13FixSuggestion18operatorEqualsImplERKS0_S2_(
    const QQmlSA::FixSuggestion *a0,
    const QQmlSA::FixSuggestion *a1) {
  return QQmlSA::FixSuggestion::operatorEqualsImpl(*a0, *a1);
}

//  a QList<QQmlSA::DocumentEdit> a ritual of QQmlSA::FixSuggestion gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_FixSuggestion__QList_QQmlSA_DocumentEdit(
    QList<QQmlSA::DocumentEdit> *self) {
  delete self;
}
