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
#include <QtCore/qlist.h>
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

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2144, as _ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditERK7QStringRKNS_14SourceLocationES5_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline DocumentEditPrivate::DocumentEditPrivate(
        DocumentEdit *iface, const QString &filename, const SourceLocation &location,
        const QString &replacement)
    : m_documentEdit{ filename, SourceLocationPrivate::sourceLocation(location), replacement }
    , q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2152, as _ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditERKS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline DocumentEditPrivate::DocumentEditPrivate(
        DocumentEdit *iface, const DocumentEditPrivate &other)
    : m_documentEdit{ other.m_documentEdit }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2158, as _ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditEOS0_
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline DocumentEditPrivate::DocumentEditPrivate(
        DocumentEdit *iface, DocumentEditPrivate &&other)
    : m_documentEdit{ std::move(other.m_documentEdit) }, q_ptr{ iface }
{
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2164, as _ZNK6QQmlSA19DocumentEditPrivate8filenameEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QString DocumentEditPrivate::filename() const
{
    return m_documentEdit.m_filename;
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2169, as _ZNK6QQmlSA19DocumentEditPrivate8locationEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QQmlSA::SourceLocation DocumentEditPrivate::location() const
{
    return QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(m_documentEdit.m_location);
}
}  // namespace QQmlSA

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2174, as _ZNK6QQmlSA19DocumentEditPrivate11replacementEv
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline QString DocumentEditPrivate::replacement() const
{
    return m_documentEdit.m_replacement;
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

//  from ../qtdeclarative/src/qmlcompiler/qqmlsa.cpp, line 2192, as _ZN6QQmlSA19DocumentEditPrivate24createQQmlSADocumentEditERK18QQmlJSDocumentEdit
namespace QQmlSA {
using namespace Qt::StringLiterals;
inline DocumentEdit DocumentEditPrivate::createQQmlSADocumentEdit(const QQmlJSDocumentEdit &jsEdit)
{
    auto saLocation = QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(jsEdit.m_location);
    return DocumentEdit{ jsEdit.m_filename, saLocation, jsEdit.m_replacement };
}
}  // namespace QQmlSA
//  -----------------------------------------------------------------------

//  DocumentEdit *QQmlSA::DocumentEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA19DocumentEditPrivate6q_funcEv(
    QQmlSA::DocumentEditPrivate *self) {
  return self->q_func();
}

//  const DocumentEdit *QQmlSA::DocumentEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::DocumentEdit *ritual_ZNK6QQmlSA19DocumentEditPrivate6q_funcEv(
    const QQmlSA::DocumentEditPrivate *self) {
  return self->q_func();
}

//  QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0, const
//      QString &filename, const SourceLocation &location, const QString
//      &replacement)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEditPrivate *ritual_ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditERK7QStringRKNS_14SourceLocationES5_(
    QQmlSA::DocumentEdit *a0,
    const QString *filename,
    const QQmlSA::SourceLocation *location,
    const QString *replacement) {
  return new QQmlSA::DocumentEditPrivate(
      a0,
      *filename,
      *location,
      *replacement);
}

//  QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0, const
//      DocumentEditPrivate &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEditPrivate *ritual_ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditERKS0_(
    QQmlSA::DocumentEdit *a0,
    const QQmlSA::DocumentEditPrivate *a1) {
  return new QQmlSA::DocumentEditPrivate(a0, *a1);
}

//  QQmlSA::DocumentEditPrivate::DocumentEditPrivate(DocumentEdit *a0,
//      DocumentEditPrivate &&a1)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEditPrivate *ritual_ZN6QQmlSA19DocumentEditPrivateC1EPNS_12DocumentEditEOS0_(
    QQmlSA::DocumentEdit *a0,
    QQmlSA::DocumentEditPrivate *a1) {
  return new QQmlSA::DocumentEditPrivate(a0, std::move(*a1));
}

//  QQmlSA::DocumentEditPrivate::~DocumentEditPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19DocumentEditPrivateD1Ev(
    QQmlSA::DocumentEditPrivate *self) {
  delete self;
}

//  QString QQmlSA::DocumentEditPrivate::filename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA19DocumentEditPrivate8filenameEv(
    const QQmlSA::DocumentEditPrivate *self) {
  return new QString(self->filename());
}

//  SourceLocation QQmlSA::DocumentEditPrivate::location() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA19DocumentEditPrivate8locationEv(
    const QQmlSA::DocumentEditPrivate *self) {
  return new QQmlSA::SourceLocation(self->location());
}

//  QString QQmlSA::DocumentEditPrivate::replacement() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA19DocumentEditPrivate11replacementEv(
    const QQmlSA::DocumentEditPrivate *self) {
  return new QString(self->replacement());
}

//  QQmlJSDocumentEdit QQmlSA::DocumentEditPrivate::documentEdit(const
//      DocumentEdit &edit)
extern "C" Q_DECL_EXPORT
QQmlJSDocumentEdit *ritual_ZN6QQmlSA19DocumentEditPrivate12documentEditERKNS_12DocumentEditE(
    const QQmlSA::DocumentEdit *edit) {
  return new QQmlJSDocumentEdit(
      QQmlSA::DocumentEditPrivate::documentEdit(
          *edit));
}

//  QList<QQmlJSDocumentEdit>
//      QQmlSA::DocumentEditPrivate::documentEdits(const QList<DocumentEdit>
//      &edits)
extern "C" Q_DECL_EXPORT
QList<QQmlJSDocumentEdit> *ritual_ZN6QQmlSA19DocumentEditPrivate13documentEditsERK5QListINS_12DocumentEditEE(
    const QList<QQmlSA::DocumentEdit> *edits) {
  return new QList<QQmlJSDocumentEdit>(
      QQmlSA::DocumentEditPrivate::documentEdits(
          *edits));
}

//  DocumentEdit QQmlSA::DocumentEditPrivate::createQQmlSADocumentEdit(const
//      QQmlJSDocumentEdit &edit)
extern "C" Q_DECL_EXPORT
QQmlSA::DocumentEdit *ritual_ZN6QQmlSA19DocumentEditPrivate24createQQmlSADocumentEditERK18QQmlJSDocumentEdit(
    const QQmlJSDocumentEdit *edit) {
  return new QQmlSA::DocumentEdit(
      QQmlSA::DocumentEditPrivate::createQQmlSADocumentEdit(
          *edit));
}
