//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QQmlJSFixSuggestion::QQmlJSFixSuggestion()
extern "C" Q_DECL_EXPORT
QQmlJSFixSuggestion *ritual_ZN19QQmlJSFixSuggestionC1Ev() {
  return new QQmlJSFixSuggestion();
}

//  QQmlJSFixSuggestion::QQmlJSFixSuggestion(const QString &description,
//      const QQmlJS::SourceLocation &location, const QQmlJSDocumentEdit &a2)
extern "C" Q_DECL_EXPORT
QQmlJSFixSuggestion *ritual_ZN19QQmlJSFixSuggestionC1ERK7QStringRKN6QQmlJS14SourceLocationERK18QQmlJSDocumentEdit(
    const QString *description,
    const QQmlJS::SourceLocation *location,
    const QQmlJSDocumentEdit *a2) {
  return new QQmlJSFixSuggestion(*description, *location, *a2);
}

//  QQmlJSFixSuggestion::QQmlJSFixSuggestion(const QString &description,
//      const QQmlJS::SourceLocation &location, const
//      QList<QQmlJSDocumentEdit> &a2)
extern "C" Q_DECL_EXPORT
QQmlJSFixSuggestion *ritual_ZN19QQmlJSFixSuggestionC1ERK7QStringRKN6QQmlJS14SourceLocationERK5QListI18QQmlJSDocumentEditE(
    const QString *description,
    const QQmlJS::SourceLocation *location,
    const QList<QQmlJSDocumentEdit> *a2) {
  return new QQmlJSFixSuggestion(*description, *location, *a2);
}

//  QString QQmlJSFixSuggestion::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSFixSuggestion11descriptionEv(
    const QQmlJSFixSuggestion *self) {
  return new QString(self->description());
}

//  QQmlJS::SourceLocation QQmlJSFixSuggestion::location() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK19QQmlJSFixSuggestion8locationEv(
    const QQmlJSFixSuggestion *self) {
  return new QQmlJS::SourceLocation(self->location());
}

//  void QQmlJSFixSuggestion::addDocumentEdit(const QQmlJSDocumentEdit
//      &documentEdit)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSFixSuggestion15addDocumentEditERK18QQmlJSDocumentEdit(
    QQmlJSFixSuggestion *self,
    const QQmlJSDocumentEdit *documentEdit) {
  self->addDocumentEdit(*documentEdit);
}

//  void QQmlJSFixSuggestion::setDocumentEdits(const
//      QList<QQmlJSDocumentEdit> &documentEdits)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSFixSuggestion16setDocumentEditsERK5QListI18QQmlJSDocumentEditE(
    QQmlJSFixSuggestion *self,
    const QList<QQmlJSDocumentEdit> *documentEdits) {
  self->setDocumentEdits(*documentEdits);
}

//  QList<QQmlJSDocumentEdit> QQmlJSFixSuggestion::documentEdits() const
extern "C" Q_DECL_EXPORT
QList<QQmlJSDocumentEdit> *ritual_ZNK19QQmlJSFixSuggestion13documentEditsEv(
    const QQmlJSFixSuggestion *self) {
  return new QList<QQmlJSDocumentEdit>(self->documentEdits());
}

//  void QQmlJSFixSuggestion::setFilename(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSFixSuggestion11setFilenameERK7QString(
    QQmlJSFixSuggestion *self,
    const QString *filename) {
  self->setFilename(*filename);
}

//  QString QQmlJSFixSuggestion::filename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSFixSuggestion8filenameEv(
    const QQmlJSFixSuggestion *self) {
  return new QString(self->filename());
}

//  void QQmlJSFixSuggestion::setAutoApplicable(bool autoApply)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSFixSuggestion17setAutoApplicableEb(
    QQmlJSFixSuggestion *self,
    bool autoApply) {
  self->setAutoApplicable(autoApply);
}

//  bool QQmlJSFixSuggestion::isAutoApplicable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSFixSuggestion16isAutoApplicableEv(
    const QQmlJSFixSuggestion *self) {
  return self->isAutoApplicable();
}

//  bool QQmlJSFixSuggestion::operator==(const QQmlJSFixSuggestion &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSFixSuggestioneqERKS_(
    const QQmlJSFixSuggestion *self,
    const QQmlJSFixSuggestion *a0) {
  return self->operator==(*a0);
}

//  bool QQmlJSFixSuggestion::operator!=(const QQmlJSFixSuggestion &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSFixSuggestionneERKS_(
    const QQmlJSFixSuggestion *self,
    const QQmlJSFixSuggestion *a0) {
  return self->operator!=(*a0);
}

//  QQmlJSFixSuggestion::~QQmlJSFixSuggestion()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSFixSuggestionD1Ev(QQmlJSFixSuggestion *self) {
  delete self;
}
