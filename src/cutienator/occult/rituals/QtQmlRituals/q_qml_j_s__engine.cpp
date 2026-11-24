//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  void QQmlJS::Engine::setCode(const QString &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine7setCodeERK7QString(
    QQmlJS::Engine *self,
    const QString *code) {
  self->setCode(*code);
}

//  const QString &QQmlJS::Engine::code() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS6Engine4codeEv(const QQmlJS::Engine *self) {
  return new QString(self->code());
}

//  void QQmlJS::Engine::addComment(int pos, int len, int line, int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine10addCommentEiiii(
    QQmlJS::Engine *self,
    int pos,
    int len,
    int line,
    int col) {
  self->addComment(pos, len, line, col);
}

//  Directives *QQmlJS::Engine::directives() const
extern "C" Q_DECL_EXPORT
QQmlJS::Directives *ritual_ZNK6QQmlJS6Engine10directivesEv(
    const QQmlJS::Engine *self) {
  return self->directives();
}

//  void QQmlJS::Engine::setDirectives(Directives *directives)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS6Engine13setDirectivesEPNS_10DirectivesE(
    QQmlJS::Engine *self,
    QQmlJS::Directives *directives) {
  self->setDirectives(directives);
}

//  MemoryPool *QQmlJS::Engine::pool()
extern "C" Q_DECL_EXPORT
QQmlJS::MemoryPool *ritual_ZN6QQmlJS6Engine4poolEv(QQmlJS::Engine *self) {
  return self->pool();
}

//  const MemoryPool *QQmlJS::Engine::pool() const
extern "C" Q_DECL_EXPORT
const QQmlJS::MemoryPool *ritual_ZNK6QQmlJS6Engine4poolEv(
    const QQmlJS::Engine *self) {
  return self->pool();
}

//  QStringView QQmlJS::Engine::midRef(int position, int size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QQmlJS6Engine6midRefEii(
    QQmlJS::Engine *self,
    int position,
    int size) {
  return new QString(self->midRef(position, size).toString());
}

//  QStringView QQmlJS::Engine::newStringRef(const QString &text)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QQmlJS6Engine12newStringRefERK7QString(
    QQmlJS::Engine *self,
    const QString *text) {
  return new QString(self->newStringRef(*text).toString());
}

//  QStringView QQmlJS::Engine::newStringRef(const QChar *chars, int size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QQmlJS6Engine12newStringRefEPK5QChari(
    QQmlJS::Engine *self,
    const QChar *chars,
    int size) {
  return new QString(self->newStringRef(chars, size).toString());
}
