//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtQmlCompiler/qqmlsa.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmlsa.h>
#include <QtQmlCompiler/private/qqmlsa_p.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtQmlCompiler/private/qqmljsscope_p.h>
#include <QtQmlCompiler/private/qqmljslogger_p.h>
#include <QtQmlCompiler/private/qqmljstyperesolver_p.h>
#include <QtQmlCompiler/private/qqmljsimportvisitor_p.h>
#include <QtQmlCompiler/private/qqmljsutils_p.h>
#include <QtQmlCompiler/private/qdeferredpointer_p.h>
#include <QtQmlCompiler/private/qqmlsasourcelocation_p.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2184, as _ZN6QQmlSA19DocumentEditPrivate13documentEditsERK5QListINS_12DocumentEditEE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QList<QQmlJSDocumentEdit> DocumentEditPrivate::documentEdits(const QList<DocumentEdit> &editsSA)
{
    QList<QQmlJSDocumentEdit> editsJS;
    for (const auto &editsSA : editsSA)
        editsJS << DocumentEditPrivate::documentEdit(editsSA);
    return editsJS;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2179, as _ZN6QQmlSA19DocumentEditPrivate12documentEditERKNS_12DocumentEditE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlJSDocumentEdit DocumentEditPrivate::documentEdit(const DocumentEdit &edit)
{
    return edit.d_ptr->m_documentEdit;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2192, as _ZN6QQmlSA19DocumentEditPrivate24createQQmlSADocumentEditERK18QQmlJSDocumentEdit
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline DocumentEdit DocumentEditPrivate::createQQmlSADocumentEdit(const QQmlJSDocumentEdit &jsEdit)
{
    auto saLocation = QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(jsEdit.m_location);
    return DocumentEdit{ jsEdit.m_filename, saLocation, jsEdit.m_replacement };
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1959, as _ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *iface) : q_ptr{ iface } { }
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1961, as _ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionERK7QStringRKNS_14SourceLocationERK5QListINS_12DocumentEditEE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline FixSuggestionPrivate::FixSuggestionPrivate(
        FixSuggestion *iface, const QString &description, const SourceLocation &location,
        const QList<DocumentEdit> &documentEdits)
    : m_fixSuggestion{ description, SourceLocationPrivate::sourceLocation(location),
                       DocumentEditPrivate::documentEdits(documentEdits) }
    , q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1970, as _ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionERKS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *iface,
                                           const FixSuggestionPrivate &other)
    : m_fixSuggestion{ other.m_fixSuggestion }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1976, as _ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionEOS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *iface, FixSuggestionPrivate &&other)
    : m_fixSuggestion{ std::move(other.m_fixSuggestion) }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1986, as _ZNK6QQmlSA20FixSuggestionPrivate8locationEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::SourceLocation FixSuggestionPrivate::location() const
{
    return QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(m_fixSuggestion.location());
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1981, as _ZNK6QQmlSA20FixSuggestionPrivate11descriptionEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QString FixSuggestionPrivate::description() const
{
    return m_fixSuggestion.description();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1991, as _ZN6QQmlSA20FixSuggestionPrivate15addDocumentEditERKNS_12DocumentEditE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline void FixSuggestionPrivate::addDocumentEdit(const DocumentEdit &editSA)
{
    auto editJS = DocumentEditPrivate::documentEdit(editSA);
    m_fixSuggestion.addDocumentEdit(editJS);
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 1997, as _ZNK6QQmlSA20FixSuggestionPrivate13documentEditsEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QList<DocumentEdit> FixSuggestionPrivate::documentEdits() const
{
    QList<DocumentEdit> edits;
    for (const auto &edit : m_fixSuggestion.documentEdits())
        edits << DocumentEditPrivate::createQQmlSADocumentEdit(edit);
    return edits;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2005, as _ZN6QQmlSA20FixSuggestionPrivate11setFileNameERK7QString
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline void FixSuggestionPrivate::setFileName(const QString &fileName)
{
    m_fixSuggestion.setFilename(fileName);
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2010, as _ZNK6QQmlSA20FixSuggestionPrivate8fileNameEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QString FixSuggestionPrivate::fileName() const
{
    return m_fixSuggestion.filename();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2015, as _ZN6QQmlSA20FixSuggestionPrivate17setAutoApplicableEb
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline void FixSuggestionPrivate::setAutoApplicable(bool autoApplicable)
{
    m_fixSuggestion.setAutoApplicable(autoApplicable);
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2020, as _ZNK6QQmlSA20FixSuggestionPrivate16isAutoApplicableEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline bool FixSuggestionPrivate::isAutoApplicable() const
{
    return m_fixSuggestion.isAutoApplicable();
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2025, as _ZN6QQmlSA20FixSuggestionPrivate13fixSuggestionERNS_13FixSuggestionE
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlJSFixSuggestion &FixSuggestionPrivate::fixSuggestion(FixSuggestion &saFixSuggestion)
{
    return saFixSuggestion.d_func()->m_fixSuggestion;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2035, as _ZN6QQmlSA20FixSuggestionPrivate25createQQmlSAFixSuggestionERK19QQmlJSFixSuggestion
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline FixSuggestion FixSuggestionPrivate::createQQmlSAFixSuggestion(const QQmlJSFixSuggestion &jsFix)
{
    auto saLocation = SourceLocationPrivate::createQQmlSASourceLocation(jsFix.location());
    FixSuggestion saFix(jsFix.description(), saLocation);
    saFix.d_ptr->m_fixSuggestion.setDocumentEdits(jsFix.documentEdits());
    saFix.setAutoApplicable(jsFix.isAutoApplicable());
    return saFix;
}
}  // namespace QQmlSA
//  -----------------------------------------------------------------------

//  FixSuggestion *QQmlSA::FixSuggestionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA20FixSuggestionPrivate6q_funcEv(
    QQmlSA::FixSuggestionPrivate *self) {
  return self->q_func();
}

//  const FixSuggestion *QQmlSA::FixSuggestionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::FixSuggestion *ritual_ZNK6QQmlSA20FixSuggestionPrivate6q_funcEv(
    const QQmlSA::FixSuggestionPrivate *self) {
  return self->q_func();
}

//  QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestionPrivate *ritual_ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionE(
    QQmlSA::FixSuggestion *a0) {
  return new QQmlSA::FixSuggestionPrivate(a0);
}

//  QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0,
//      const QString &description, const SourceLocation &location, const
//      QList<DocumentEdit> &documentEdits)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestionPrivate *ritual_ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionERK7QStringRKNS_14SourceLocationERK5QListINS_12DocumentEditEE(
    QQmlSA::FixSuggestion *a0,
    const QString *description,
    const QQmlSA::SourceLocation *location,
    const QList<QQmlSA::DocumentEdit> *documentEdits) {
  return new QQmlSA::FixSuggestionPrivate(
      a0,
      *description,
      *location,
      *documentEdits);
}

//  QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0,
//      const FixSuggestionPrivate &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestionPrivate *ritual_ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionERKS0_(
    QQmlSA::FixSuggestion *a0,
    const QQmlSA::FixSuggestionPrivate *a1) {
  return new QQmlSA::FixSuggestionPrivate(a0, *a1);
}

//  QQmlSA::FixSuggestionPrivate::FixSuggestionPrivate(FixSuggestion *a0,
//      FixSuggestionPrivate &&a1)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestionPrivate *ritual_ZN6QQmlSA20FixSuggestionPrivateC1EPNS_13FixSuggestionEOS0_(
    QQmlSA::FixSuggestion *a0,
    QQmlSA::FixSuggestionPrivate *a1) {
  return new QQmlSA::FixSuggestionPrivate(a0, std::move(*a1));
}

//  QQmlSA::FixSuggestionPrivate::~FixSuggestionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA20FixSuggestionPrivateD1Ev(
    QQmlSA::FixSuggestionPrivate *self) {
  delete self;
}

//  SourceLocation QQmlSA::FixSuggestionPrivate::location() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA20FixSuggestionPrivate8locationEv(
    const QQmlSA::FixSuggestionPrivate *self) {
  return new QQmlSA::SourceLocation(self->location());
}

//  QString QQmlSA::FixSuggestionPrivate::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA20FixSuggestionPrivate11descriptionEv(
    const QQmlSA::FixSuggestionPrivate *self) {
  return new QString(self->description());
}

//  void QQmlSA::FixSuggestionPrivate::addDocumentEdit(const DocumentEdit
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA20FixSuggestionPrivate15addDocumentEditERKNS_12DocumentEditE(
    QQmlSA::FixSuggestionPrivate *self,
    const QQmlSA::DocumentEdit *a0) {
  self->addDocumentEdit(*a0);
}

//  QList<DocumentEdit> QQmlSA::FixSuggestionPrivate::documentEdits() const
extern "C" Q_DECL_EXPORT
QList<QQmlSA::DocumentEdit> *ritual_ZNK6QQmlSA20FixSuggestionPrivate13documentEditsEv(
    const QQmlSA::FixSuggestionPrivate *self) {
  return new QList<QQmlSA::DocumentEdit>(self->documentEdits());
}

//  void QQmlSA::FixSuggestionPrivate::setFileName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA20FixSuggestionPrivate11setFileNameERK7QString(
    QQmlSA::FixSuggestionPrivate *self,
    const QString *a0) {
  self->setFileName(*a0);
}

//  QString QQmlSA::FixSuggestionPrivate::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA20FixSuggestionPrivate8fileNameEv(
    const QQmlSA::FixSuggestionPrivate *self) {
  return new QString(self->fileName());
}

//  void QQmlSA::FixSuggestionPrivate::setAutoApplicable(bool autoApplicable)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA20FixSuggestionPrivate17setAutoApplicableEb(
    QQmlSA::FixSuggestionPrivate *self,
    bool autoApplicable) {
  self->setAutoApplicable(autoApplicable);
}

//  bool QQmlSA::FixSuggestionPrivate::isAutoApplicable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA20FixSuggestionPrivate16isAutoApplicableEv(
    const QQmlSA::FixSuggestionPrivate *self) {
  return self->isAutoApplicable();
}

//  QQmlJSFixSuggestion
//      &QQmlSA::FixSuggestionPrivate::fixSuggestion(QQmlSA::FixSuggestion
//      &a0)
extern "C" Q_DECL_EXPORT
QQmlJSFixSuggestion *ritual_ZN6QQmlSA20FixSuggestionPrivate13fixSuggestionERNS_13FixSuggestionE(
    QQmlSA::FixSuggestion *a0) {
  return &(QQmlSA::FixSuggestionPrivate::fixSuggestion(*a0));
}

//  FixSuggestion
//      QQmlSA::FixSuggestionPrivate::createQQmlSAFixSuggestion(const
//      QQmlJSFixSuggestion &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestion *ritual_ZN6QQmlSA20FixSuggestionPrivate25createQQmlSAFixSuggestionERK19QQmlJSFixSuggestion(
    const QQmlJSFixSuggestion *a0) {
  return new QQmlSA::FixSuggestion(
      QQmlSA::FixSuggestionPrivate::createQQmlSAFixSuggestion(
          *a0));
}

//  a QList<QQmlSA::DocumentEdit> a ritual of QQmlSA::FixSuggestionPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_FixSuggestionPrivate__QList_QQmlSA_DocumentEdit(
    QList<QQmlSA::DocumentEdit> *self) {
  delete self;
}
